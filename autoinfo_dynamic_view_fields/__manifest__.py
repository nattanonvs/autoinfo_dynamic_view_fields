{
    "name": "AutoInfo Dynamic View Fields",
    "version": "15.0.1.4.2",
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
