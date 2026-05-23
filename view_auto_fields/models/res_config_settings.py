from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    view_auto_fields_enabled = fields.Boolean(
        string="Auto add fields from Form into List/Search",
        config_parameter="view_auto_fields.enabled",
    )
    view_auto_fields_allowed_modules = fields.Char(
        string="Allowed modules (comma-separated)",
        config_parameter="view_auto_fields.allowed_modules",
    )
    view_auto_fields_allowed_models = fields.Char(
        string="Allowed models (comma-separated)",
        config_parameter="view_auto_fields.allowed_models",
    )
    view_auto_fields_filter_active_fields = fields.Boolean(
        string="Use only active fields (has data)",
        config_parameter="view_auto_fields.filter_active_fields",
    )
    view_auto_fields_active_fields_cache_hours = fields.Integer(
        string="Active fields cache (hours)",
        config_parameter="view_auto_fields.active_fields_cache_hours",
        default=24,
    )
    view_auto_fields_hide_technical_fields = fields.Boolean(
        string="Hide technical/system fields",
        config_parameter="view_auto_fields.hide_technical_fields",
    )
    view_auto_fields_reduction_scope = fields.Selection(
        [
            ("both", "Columns + Search"),
            ("list", "Columns only"),
            ("search", "Search only"),
        ],
        string="Apply reduction to",
        config_parameter="view_auto_fields.reduction_scope",
        default="both",
    )
    view_auto_fields_max_fields_preset = fields.Selection(
        [
            ("0", "Unlimited"),
            ("30", "30"),
            ("50", "50"),
            ("80", "80"),
            ("custom", "Custom"),
        ],
        string="Max fields to auto add",
        config_parameter="view_auto_fields.max_fields_preset",
        default="50",
    )
    view_auto_fields_max_fields_custom = fields.Integer(
        string="Custom max fields",
        config_parameter="view_auto_fields.max_fields_custom",
        default=50,
    )
