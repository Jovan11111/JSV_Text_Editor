import tkinter as tk
import re


class Highlighter:
    def __init__(self, text_widget):
        self.text_widget = text_widget
        self.keyword_tag = "keyword"
        self.type_tag = "type"
        self.comment_tag = "comment"
        self.string_tag = "string"

        self.keywords = ["rtranif0", "begin", "always", "ifnone", "rpmos", "and", "initial", "rtran", "assign",
                         "rtranif1", "buf", "bufif0", "join", "small", "bufif1", "large", "specify", "case",
                         "macromodule", "specparam", "casex", "medium", "strong0", "casez", "module", "strong1", "cmos",
                         "nand", "deassign", "negedge", "default", "nmos", "table", "defparam", "nor", "task",
                         "disable", "not", "edge", "notif0", "tran", "else", "notif1", "tranif0", "end", "or",
                         "tranif1", "endcase", "endmodule", "endprimitive", "posedge", "endspecify", "primitive",
                         "endfunction", "pmos", "endtable", "pull0", "endtask", "pull1", "pullup", "wait", "for",
                         "pulldown", "while", "function", "weak1", "fork", "force", "rcmos", "weak0", "forever",
                         "highz0", "release", "highz1", "repeat", "xnor", "if", "rnmos", "xor", "return", "super",
                         "new", "package", "endpackage"]

        self.types = ["input", "inout", "integer", "scalared", "supply0", "supply1", "time", "output", "tri",
                      "parameter", "tri0", "tri1", "triand", "trior", "trireg", "vectored", "event", "wand", "real",
                      "realtime", "reg", "wire", "wor", "int", "string"]

    def highlight_keywords(self):
        self.text_widget.tag_remove(self.keyword_tag, "1.0", tk.END)
        text_content = self.text_widget.get("1.0", tk.END)
        for word in self.keywords:
            matches = re.finditer(rf'\b{word}\b', text_content, flags=re.IGNORECASE)
            for match in matches:
                start_pos = match.start()
                end_pos = match.end()
                start = self.text_widget.index(f"1.0 + {start_pos}c")
                end = self.text_widget.index(f"1.0 + {end_pos}c")
                self.text_widget.tag_add(self.keyword_tag, start, end)
                self.text_widget.tag_configure(self.keyword_tag, foreground="orange")

    def highlight_types(self):
        self.text_widget.tag_remove(self.type_tag, "1.0", tk.END)
        text_content = self.text_widget.get("1.0", tk.END)
        for word in self.types:
            matches = re.finditer(rf'\b{word}\b', text_content, flags=re.IGNORECASE)
            for match in matches:
                start_pos = match.start()
                end_pos = match.end()
                start = self.text_widget.index(f"1.0 + {start_pos}c")
                end = self.text_widget.index(f"1.0 + {end_pos}c")
                self.text_widget.tag_add(self.type_tag, start, end)
                self.text_widget.tag_configure(self.type_tag, foreground="#77d197")

    def highlight_comments(self):
        self.text_widget.tag_remove(self.comment_tag, "1.0", tk.END)
        text_content = self.text_widget.get("1.0", tk.END)

        matches = re.finditer(r'/\*.*?\*/', text_content, flags=re.DOTALL)
        for match in matches:
            start_pos = match.start()
            end_pos = match.end()
            start = self.text_widget.index(f"1.0 + {start_pos}c")
            end = self.text_widget.index(f"1.0 + {end_pos}c")
            self.text_widget.tag_add(self.comment_tag, start, end)
            self.text_widget.tag_configure(self.comment_tag, foreground="gray")

        matches = re.finditer(r'//.*?\n', text_content)
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

        matches = re.finditer(r'".*?"', text_content, flags=re.DOTALL)
        for match in matches:
            start_pos = match.start()
            end_pos = match.end()
            start = self.text_widget.index(f"1.0 + {start_pos}c")
            end = self.text_widget.index(f"1.0 + {end_pos}c")
            self.text_widget.tag_add(self.string_tag, start, end)
            self.text_widget.tag_configure(self.string_tag, foreground="green")

    def highlight(self):
        self.highlight_keywords()
        self.highlight_types()
        self.highlight_strings()
        self.highlight_comments()
