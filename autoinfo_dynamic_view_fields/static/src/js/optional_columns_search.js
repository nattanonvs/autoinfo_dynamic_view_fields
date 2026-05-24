odoo.define("autoinfo_dynamic_view_fields.optional_columns_search", function (require) {
    "use strict";

    const $ = require("jquery");
    const core = require("web.core");
    const ListRenderer = require("web.ListRenderer");

    const _t = core._t;
    const original = ListRenderer.prototype._renderOptionalColumnsDropdown;

    ListRenderer.include({
        _renderOptionalColumnsDropdown: function () {
            const $el = original.apply(this, arguments);
            const $dropdown = $el.find(".o_optional_columns_dropdown");
            if (!$dropdown.length || $dropdown.find(".o_optional_columns_search_input").length) {
                return $el;
            }

            const $container = $("<div>", { class: "o_optional_columns_search_container px-2 py-1" });
            const $input = $("<input>", {
                type: "text",
                class: "form-control form-control-sm o_optional_columns_search_input",
                placeholder: _t("Search..."),
                autocomplete: "off",
            });
            $container.append($input);
            $dropdown.prepend($container);

            const applyFilter = function () {
                const query = ($input.val() || "").toString().trim().toLowerCase();
                $dropdown.children(".dropdown-item").each(function () {
                    const $item = $(this);
                    const text = ($item.text() || "").toString().trim().toLowerCase();
                    $item.toggle(!query || text.indexOf(query) !== -1);
                });
            };

            $dropdown.on("input", ".o_optional_columns_search_input", applyFilter);
            $el.on("shown.bs.dropdown", function () {
                $input.focus();
            });
            $el.on("hidden.bs.dropdown", function () {
                $input.val("");
                $dropdown.children(".dropdown-item").show();
            });

            return $el;
        },
    });
});

