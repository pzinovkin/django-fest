function(__fest_context, __fest_error) {
    "use strict";
    var __fest_str = "",
        __fest_result = [],
        __fest_contexts = [],
        __fest_if, __fest_foreach, __fest_from, __fest_to, __fest_html = "",
        __fest_blocks = {},
        __fest_params, __fest_htmlchars = /[&<>\"]/g,
        __fest_htmlhash = {
            '&': '&amp;',
            '<': '&lt;',
            '>': '&gt;',
            '"': '&quot;'
        },
        __fest_jschars = /[\'\"\/\n\t\b\f]/g,
        __fest_jshash = {
            "\"": "\\\"",
            "\\": "\\\\",
            "/": "\\/",
            "\n": "\\n",
            "\t": "\\t",
            "\b": "\\b",
            "\f": "\\f",
            "'": "\\'"
        };
    if (typeof __fest_error === "undefined") {
        __fest_error = function() {
            return console.error.apply(console, arguments);
        };
    }
    function __fest_replaceHTML(char) {
        return __fest_htmlhash[char];
    }
    function __fest_replaceJS(char) {
        return __fest_jshash[char];
    }
    function __fest_escapeJS(s) {
        if (typeof s !== "string") s += "";
        return s.replace(__fest_jschars, __fest_replaceJS);
    }
    function __fest_escapeHTML(s) {
        if (typeof s !== "string") s += "";
        return s.replace(__fest_htmlchars, __fest_replaceHTML);
    }
    if (typeof document === "undefined") {
        var document = {
            write: function(string) {
                __fest_str += string;
            }
        };
    }
    var json = __fest_context;
    __fest_str += "<!DOCTYPE html>";
    __fest_result[__fest_result.length] = __fest_str;
    if (__fest_result.length === 1) {
        return __fest_result[0]
    }
    function setblocks(list) {
        var __fest_i, __fest_l;
        for (__fest_i = 0, __fest_l = list.length; __fest_i < __fest_l; __fest_i++) {
            if (typeof list[__fest_i] === "string") {
                __fest_html += list[__fest_i];
            } else {
                setblocks(list[__fest_i]());
            }
        }
    }
    setblocks(__fest_result);
    return __fest_html;
}
