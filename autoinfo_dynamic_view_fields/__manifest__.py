{
    "name": "AutoInfo Dynamic View Fields",
    "version": "15.0.1.5.1",
    "summary": "Dynamic List/Search fields from Form view with governance controls",
    "category": "Tools",
    "author": "Odoo S.A. and The Auto-Info Co., Ltd.",
    "maintainer": "The Auto-Info Co., Ltd.",
    "license": "LGPL-3",
    "depends": ["base", "web"],
    "assets": {
        "web.assets_backend": [
            "autoinfo_dynamic_view_fields/static/src/js/optional_columns_search.js",
        ],
    },
    "post_init_hook": "post_init_hook",
    "data": [
        "security/view_auto_fields_security.xml",
        "data/ir_config_parameter.xml",
        "views/res_config_settings_views.xml",
    ],
    "installable": True,
}
