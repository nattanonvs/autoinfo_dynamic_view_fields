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
