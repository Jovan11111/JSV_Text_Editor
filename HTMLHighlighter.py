"""
==================================================================
Project Name:    JSV_Text_Editor
File Name:       HTMLHighlighter.py
Description:     HTML syntax highlighter for JSV Text Editor.

Author:          Jovan11111
Creation Date:   16.7.2024
Version:         1.0

==================================================================
"""

from highLighter import Highlighter
import re
import tkinter as tk


class HTMLHighlighter(Highlighter):
    def __init__(self, text_widget):
        super().__init__(text_widget)
        self.tag_tag = "tag"
        self.attribute_tag = "attribute"
        self.comment_tag = "comment"
        self.string_tag = "string"

        self.tags = [
            "!DOCTYPE", "a", "abbr", "address", "area", "article", "aside", "audio", "b", "base", "bdi", "bdo", "blockquote", 
            "body", "br", "button", "canvas", "caption", "cite", "code", "col", "colgroup", "data", "datalist", "dd", "del", 
            "details", "dfn", "dialog", "div", "dl", "dt", "em", "embed", "fieldset", "figcaption", "figure", "footer", "form", 
            "h1", "h2", "h3", "h4", "h5", "h6", "head", "header", "hr", "html", "i", "iframe", "img", "input", "ins", "kbd", 
            "label", "legend", "li", "link", "main", "map", "mark", "meta", "meter", "nav", "noscript", "object", "ol", "optgroup", 
            "option", "output", "p", "param", "picture", "pre", "progress", "q", "rp", "rt", "ruby", "s", "samp", "script", "section", 
            "select", "small", "source", "span", "strong", "style", "sub", "summary", "sup", "svg", "table", "tbody", "td", "template", 
            "textarea", "tfoot", "th", "thead", "time", "title", "tr", "track", "u", "ul", "var", "video", "wbr"
        ]

        self.attributes = [
            "accept", "accept-charset", "accesskey", "action", "align", "alt", "async", "autocomplete", "autofocus", "autoplay", 
            "bgcolor", "border", "charset", "checked", "cite", "class", "color", "cols", "colspan", "content", "contenteditable", 
            "controls", "coords", "data", "datetime", "default", "defer", "dir", "dirname", "disabled", "download", "draggable", 
            "enctype", "for", "form", "formaction", "headers", "height", "hidden", "high", "href", "hreflang", "http-equiv", "id", 
            "integrity", "ismap", "kind", "label", "lang", "list", "loop", "low", "max", "maxlength", "media", "method", "min", 
            "multiple", "muted", "name", "novalidate", "onabort", "onafterprint", "onbeforeprint", "onbeforeunload", "onblur", 
            "oncanplay", "oncanplaythrough", "onchange", "onclick", "oncontextmenu", "oncopy", "oncuechange", "oncut", "ondblclick", 
            "ondrag", "ondragend", "ondragenter", "ondragleave", "ondragover", "ondragstart", "ondrop", "ondurationchange", "onemptied", 
            "onended", "onerror", "onfocus", "onhashchange", "oninput", "oninvalid", "onkeydown", "onkeypress", "onkeyup", "onload", 
            "onloadeddata", "onloadedmetadata", "onloadstart", "onmessage", "onmousedown", "onmousemove", "onmouseout", "onmouseover", 
            "onmouseup", "onmousewheel", "onoffline", "ononline", "onpagehide", "onpageshow", "onpaste", "onpause", "onplay", 
            "onplaying", "onpopstate", "onprogress", "onratechange", "onreset", "onresize", "onscroll", "onsearch", "onseeked", 
            "onseeking", "onselect", "onstalled", "onstorage", "onsubmit", "onsuspend", "ontimeupdate", "ontoggle", "onunload", 
            "onvolumechange", "onwaiting", "onwheel", "open", "optimum", "pattern", "placeholder", "poster", "preload", "readonly", 
            "rel", "required", "reversed", "rows", "rowspan", "sandbox", "scope", "selected", "shape", "size", "sizes", "span", 
            "spellcheck", "src", "srcdoc", "srclang", "srcset", "start", "step", "style", "tabindex", "target", "title", "translate", 
            "type", "usemap", "value", "width", "wrap"
        ]

    def highlight_tags(self):
        self.text_widget.tag_remove(self.tag_tag, "1.0", tk.END)
        text_content = self.text_widget.get("1.0", tk.END)
        for tag in self.tags:
            matches = re.finditer(rf'<\/?{tag}[^>]*>', text_content, flags=re.DOTALL)
            for match in matches:
                start_pos = match.start()
                end_pos = match.end()
                start = self.text_widget.index(f"1.0 + {start_pos}c")
                end = self.text_widget.index(f"1.0 + {end_pos}c")
                self.text_widget.tag_add(self.tag_tag, start, end)
                self.text_widget.tag_configure(self.tag_tag, foreground="#33abf9")

    def highlight_attributes(self):
        self.text_widget.tag_remove(self.attribute_tag, "1.0", tk.END)
        text_content = self.text_widget.get("1.0", tk.END)
        for attr in self.attributes:
            matches = re.finditer(rf'\b{attr}\b(?=\s*=\s*["\'])', text_content, flags=re.DOTALL)
            for match in matches:
                start_pos = match.start()
                end_pos = match.end()
                start = self.text_widget.index(f"1.0 + {start_pos}c")
                end = self.text_widget.index(f"1.0 + {end_pos}c")
                self.text_widget.tag_add(self.attribute_tag, start, end)
                self.text_widget.tag_configure(self.attribute_tag, foreground="orange")

    def highlight_comments(self):
        self.text_widget.tag_remove(self.comment_tag, "1.0", tk.END)
        text_content = self.text_widget.get("1.0", tk.END)
        matches = re.finditer(r'<!--.*?-->', text_content, flags=re.DOTALL)
        for match in matches:
            start_pos = match.start()
            end_pos = match.end()
            start = self.text_widget.index(f"1.0 + {start_pos}c")
            end = self.text_widget.index(f"1.0 + {end_pos}c")
            self.text_widget.tag_add(self.comment_tag, start, end)
            self.text_widget.tag_configure(self.comment_tag, foreground="gray")

    def highlight_strings(self):
        self.text_widget.tag_remove(self.string_tag, "1.0", tk.END)
        text_content = self.text_widget.get("1.0", tk.END)
        matches = re.finditer(r'["\'][^"\']*["\']', text_content, flags=re.DOTALL)
        for match in matches:
            start_pos = match.start()
            end_pos = match.end()
            start = self.text_widget.index(f"1.0 + {start_pos}c")
            end = self.text_widget.index(f"1.0 + {end_pos}c")
            self.text_widget.tag_add(self.string_tag, start, end)
            self.text_widget.tag_configure(self.string_tag, foreground="green")

    def highlight(self):
        self.highlight_tags()
        self.highlight_attributes()
        self.highlight_comments()
        self.highlight_strings()

