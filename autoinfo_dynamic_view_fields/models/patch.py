import time
from lxml import etree

from odoo import api, models


_ORIGINAL_LOAD_VIEWS = models.BaseModel.load_views

_LIST_ALLOWED_TYPES = {
    "boolean",
    "char",
    "date",
    "datetime",
    "float",
    "integer",
    "many2one",
    "monetary",
    "selection",
    "text",
}

_SEARCH_ALLOWED_TYPES = {
    "boolean",
    "char",
    "date",
    "datetime",
    "float",
    "integer",
    "many2one",
    "monetary",
    "selection",
    "text",
}

_ACTIVE_FIELDS_CACHE = {}
_TECHNICAL_FIELD_PREFIXES = (
    "activity_",
    "message_",
)
_TECHNICAL_FIELD_NAMES = {
    "__last_update",
    "create_date",
    "create_uid",
    "display_name",
    "id",
    "message_attachment_count",
    "message_channel_ids",
    "message_follower_ids",
    "message_has_error",
    "message_has_error_counter",
    "message_has_sms_error",
    "message_ids",
    "message_is_follower",
    "message_main_attachment_id",
    "message_needaction",
    "message_needaction_counter",
    "message_partner_ids",
    "message_unread",
    "message_unread_counter",
    "website_message_ids",
    "write_date",
    "write_uid",
}


def _param_truthy(value):
    return str(value).strip().lower() in {"1", "true", "yes", "y", "on"}


def _csv_set(value):
    if not value:
        return set()
    items = []
    for part in str(value).split(","):
        part = part.strip()
        if part:
            items.append(part)
    return set(items)


def _has_group(user, xmlid):
    try:
        return user.has_group(xmlid)
    except Exception:
        return False


def _get_view_module(env, view_id):
    if not view_id:
        return None
    view = env["ir.ui.view"].sudo().browse(view_id)
    if not view:
        return None
    external = view.get_external_id().get(view.id)
    if not external or "." not in external:
        return None
    return external.split(".", 1)[0]


def _is_enabled(model, view_dict=None):
    env = model.env
    context = model._context
    if "view_auto_fields_enabled" in context:
        return bool(context["view_auto_fields_enabled"])
    if not _param_truthy(env["ir.config_parameter"].sudo().get_param("view_auto_fields.enabled", "0")):
        return False

    user = env.user
    if _has_group(user, "autoinfo_dynamic_view_fields.group_view_auto_fields_none") or _has_group(
        user, "view_auto_fields.group_view_auto_fields_none"
    ):
        return False
    if _has_group(user, "autoinfo_dynamic_view_fields.group_view_auto_fields_all") or _has_group(
        user, "view_auto_fields.group_view_auto_fields_all"
    ):
        return True
    if not (
        _has_group(user, "autoinfo_dynamic_view_fields.group_view_auto_fields_restricted")
        or _has_group(user, "view_auto_fields.group_view_auto_fields_restricted")
    ):
        return True

    allowed_modules = _csv_set(env["ir.config_parameter"].sudo().get_param("view_auto_fields.allowed_modules", ""))
    allowed_models = _csv_set(env["ir.config_parameter"].sudo().get_param("view_auto_fields.allowed_models", ""))

    view_module = _get_view_module(env, (view_dict or {}).get("view_id"))
    if view_module and view_module in allowed_modules:
        return True
    if model._name in allowed_models:
        return True
    return False


def _pg_ident(value):
    return '"' + str(value).replace('"', '""') + '"'


def _active_fields_settings(model):
    env = model.env
    context = model._context
    enabled = context.get("view_auto_fields_filter_active_fields")
    if enabled is None:
        enabled = _param_truthy(
            env["ir.config_parameter"].sudo().get_param("view_auto_fields.filter_active_fields", "0")
        )
    cache_hours = context.get("view_auto_fields_active_fields_cache_hours")
    if cache_hours is None:
        cache_hours = env["ir.config_parameter"].sudo().get_param("view_auto_fields.active_fields_cache_hours", "24")
    try:
        cache_hours = float(cache_hours)
    except Exception:
        cache_hours = 24.0
    return bool(enabled), max(cache_hours, 0.0)


def _get_active_stored_fields(model, stored_field_names, cache_hours):
    if not stored_field_names:
        return set()

    key = (model.env.cr.dbname, model._name, tuple(stored_field_names))
    now = time.time()
    if cache_hours > 0:
        cached = _ACTIVE_FIELDS_CACHE.get(key)
        if cached and cached[0] > now:
            return cached[1]

    cr = model.env.cr
    table = model._table
    table_ident = _pg_ident(table)

    try:
        cr.execute(f"SELECT 1 FROM {table_ident} LIMIT 1")
        if not cr.fetchone():
            active = set()
            _ACTIVE_FIELDS_CACHE[key] = (now + (cache_hours * 3600.0), active)
            return active

        cr.execute(
            """
            SELECT column_name
            FROM information_schema.columns
            WHERE table_schema = current_schema()
              AND table_name = %s
              AND column_name = ANY(%s)
            """,
            [table, list(stored_field_names)],
        )
        existing = {r[0] for r in cr.fetchall()}
        if not existing:
            active = set()
            _ACTIVE_FIELDS_CACHE[key] = (now + (cache_hours * 3600.0), active)
            return active

        cr.execute(
            """
            SELECT attname, null_frac
            FROM pg_stats
            WHERE schemaname = current_schema()
              AND tablename = %s
              AND attname = ANY(%s)
            """,
            [table, list(existing)],
        )
        stats = {r[0]: r[1] for r in cr.fetchall()}

        active = {name for name, null_frac in stats.items() if null_frac is not None and float(null_frac) < 1.0}
        missing_stats = existing - set(stats)
        for col in missing_stats:
            col_ident = _pg_ident(col)
            cr.execute(f"SELECT 1 FROM {table_ident} WHERE {col_ident} IS NOT NULL LIMIT 1")
            if cr.fetchone():
                active.add(col)
    except Exception:
        active = set(stored_field_names)

    if cache_hours > 0:
        _ACTIVE_FIELDS_CACHE[key] = (now + (cache_hours * 3600.0), active)
    return active


def _filter_active_fields(model, field_names):
    enabled, cache_hours = _active_fields_settings(model)
    if not enabled or not field_names or not getattr(model, "_auto", False):
        return field_names

    non_stored = []
    stored = []
    for name in field_names:
        field = model._fields.get(name)
        if not field:
            continue
        if getattr(field, "company_dependent", False):
            non_stored.append(name)
            continue
        if getattr(field, "store", False):
            stored.append(name)
        else:
            non_stored.append(name)

    active_stored = _get_active_stored_fields(model, stored, cache_hours)
    return non_stored + [name for name in stored if name in active_stored]


def _reduction_settings(model):
    env = model.env
    context = model._context

    hide_technical = context.get("view_auto_fields_hide_technical_fields")
    if hide_technical is None:
        hide_technical = _param_truthy(
            env["ir.config_parameter"].sudo().get_param("view_auto_fields.hide_technical_fields", "1")
        )

    scope = context.get("view_auto_fields_reduction_scope")
    if not scope:
        scope = env["ir.config_parameter"].sudo().get_param("view_auto_fields.reduction_scope", "both") or "both"

    preset = context.get("view_auto_fields_max_fields_preset")
    if preset is None:
        preset = env["ir.config_parameter"].sudo().get_param("view_auto_fields.max_fields_preset", "50")

    custom = context.get("view_auto_fields_max_fields_custom")
    if custom is None:
        custom = env["ir.config_parameter"].sudo().get_param("view_auto_fields.max_fields_custom", "50")

    max_fields = 0
    try:
        if preset == "custom":
            max_fields = int(custom or 0)
        else:
            max_fields = int(preset or 0)
    except Exception:
        max_fields = 0

    if max_fields < 0:
        max_fields = 0

    if scope not in {"both", "list", "search"}:
        scope = "both"

    return bool(hide_technical), scope, max_fields


def _is_technical_field(field_name):
    if field_name in _TECHNICAL_FIELD_NAMES:
        return True
    for prefix in _TECHNICAL_FIELD_PREFIXES:
        if field_name.startswith(prefix):
            return True
    return False


def _apply_reduction(model, field_names, kind):
    if not field_names:
        return field_names
    hide_technical, scope, max_fields = _reduction_settings(model)
    if scope not in {"both", kind}:
        return field_names

    if hide_technical:
        field_names = [n for n in field_names if not _is_technical_field(n)]

    if max_fields:
        field_names = field_names[:max_fields]

    return field_names


def _extract_form_fields(model, form_arch):
    try:
        root = etree.fromstring(form_arch)
    except Exception:
        return [], []

    list_fields = []
    search_fields = []
    seen = set()
    for node in root.xpath(".//field[@name]"):
        name = node.get("name")
        if not name or name in seen:
            continue
        field = model._fields.get(name)
        if not field:
            continue
        if field.type in _LIST_ALLOWED_TYPES:
            list_fields.append(name)
        if field.type in _SEARCH_ALLOWED_TYPES and (field.store or field.search):
            search_fields.append(name)
        seen.add(name)

    return list_fields, search_fields


def _postprocess_view(model, view_dict, root):
    view_id = view_dict.get("view_id")
    base_model = view_dict.get("base_model", model._name)

    view = model.env["ir.ui.view"].sudo().browse(view_id) if view_id else model.env["ir.ui.view"].sudo().browse()
    if view_id and base_model != model._name:
        view = view.with_context(base_model_name=base_model)

    arch, fields = view.postprocess_and_fields(root, model=model._name)
    view_dict["arch"] = arch
    view_dict["fields"] = fields


def _add_optional_fields_to_tree(tree_arch, field_names):
    try:
        root = etree.fromstring(tree_arch)
    except Exception:
        return None, False

    tree = root if root.tag == "tree" else root.find(".//tree")
    if tree is None:
        return None, False

    changed = False
    for node in tree.xpath("./field[@name]"):
        if "optional" in node.attrib:
            continue
        if node.get("invisible") in {"1", "True", "true"}:
            continue
        node.set("optional", "show")
        changed = True

    existing = {n.get("name") for n in tree.xpath(".//field[@name]")}
    for name in field_names:
        if name in existing:
            continue
        etree.SubElement(tree, "field", name=name, optional="hide")
        existing.add(name)
        changed = True

    return root, changed


def _add_fields_to_search(search_arch, field_names):
    try:
        root = etree.fromstring(search_arch)
    except Exception:
        return None, False

    search = root if root.tag == "search" else root.find(".//search")
    if search is None:
        return None, False

    existing = {n.get("name") for n in search.xpath(".//field[@name]")}
    added = False
    for name in field_names:
        if name in existing:
            continue
        etree.SubElement(search, "field", name=name)
        existing.add(name)
        added = True

    return root, added


@api.model
def _patched_load_views(self, views, options=None):
    result = _ORIGINAL_LOAD_VIEWS(self, views, options=options)

    fields_views = result.get("fields_views") or {}
    if not fields_views:
        return result

    list_key = "list" if "list" in fields_views else "tree" if "tree" in fields_views else None
    list_view = fields_views.get(list_key) if list_key else None
    search_view = fields_views.get("search")

    list_allowed = bool(list_view) and _is_enabled(self, list_view)
    search_allowed = bool(search_view) and _is_enabled(self, search_view)
    if not list_allowed and not search_allowed:
        return result

    if list_allowed:
        root, changed = _add_optional_fields_to_tree(list_view.get("arch", ""), [])
        if changed:
            _postprocess_view(self, list_view, root)

    form_arch = (fields_views.get("form") or {}).get("arch")
    if not form_arch:
        try:
            form_arch = self.fields_view_get(view_type="form").get("arch")
        except Exception:
            return result

    list_field_names, search_field_names = _extract_form_fields(self, form_arch)
    list_field_names = _filter_active_fields(self, list_field_names)
    search_field_names = _filter_active_fields(self, search_field_names)
    list_field_names = _apply_reduction(self, list_field_names, "list")
    search_field_names = _apply_reduction(self, search_field_names, "search")
    if list_allowed and list_field_names:
        root, changed = _add_optional_fields_to_tree(list_view.get("arch", ""), list_field_names)
        if changed:
            _postprocess_view(self, list_view, root)

    if search_allowed and search_field_names:
        root, changed = _add_fields_to_search(search_view.get("arch", ""), search_field_names)
        if changed:
            _postprocess_view(self, search_view, root)

    return result


_patched_load_views._api = "model"
models.BaseModel.load_views = _patched_load_views
