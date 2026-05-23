from odoo import fields, models


class ResUsers(models.Model):
    _inherit = "res.users"

    view_auto_fields_policy = fields.Selection(
        [
            ("all", "Allowed in all modules"),
            ("restricted", "Allowed only in allowed modules"),
            ("none", "Not allowed"),
        ],
        default="all",
    )
