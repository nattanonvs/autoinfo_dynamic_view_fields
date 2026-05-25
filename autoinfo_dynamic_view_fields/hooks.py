from odoo import SUPERUSER_ID, api


def post_init_hook(cr, registry):
    env = api.Environment(cr, SUPERUSER_ID, {})
    legacy_names = [
        "view_users_form_inherit_view_auto_fields",
        "view_users_preferences_form_inherit_view_auto_fields",
    ]
    imd = env["ir.model.data"].sudo().search(
        [
            ("model", "=", "ir.ui.view"),
            ("name", "in", legacy_names),
        ]
    )
    views = env["ir.ui.view"].sudo().browse(imd.mapped("res_id")).exists()
    if views:
        views.write({"active": False})

