"""
==================================================================
Project Name:    JSV_Text_Editor
File Name:       CHighligher.py
Description:     A custom text editor with features tailored for UVM code, 
                 including syntax highlighting, autocompletion, auto-indentation,
                 line numbering, commenting, and find/replace functionality.

Author:          Jovan11111
Creation Date:   13.7.2024
Version:         1.0

==================================================================
"""

from highlighters.highLighter import Highlighter
import re
import tkinter as tk


class CHighLighter(Highlighter):
    def __init__(self, text_widget):
        super().__init__(text_widget)
        self.keyword_tag = "keyword"
        self.type_tag = "type"
        self.comment_tag = "comment"
        self.string_tag = "string"
        self.special_tag = "special"
        self.number_tag = "number"

        self.keywords = ["break", "case", "alignas", "alignof", "const", "constexpr", "continue", "default", "do",
                         "else", "extern", "for", "goto", "if", "inline", "register", "restrict", "return", "sizeof",
                         "static", "static_assert", "switch", "thread_local", "typedef", "typeof", "typeof_unqual",
                         "void", "volatile", "while"]

        self.types = ["auto", "bool", "char", "double", "enum", "float", "int", "long", "short", "signed",
                      "struct", "union", "unsigned"]

        self.values = ["false", "true", "nullptr"]

        self.special = ["_Alignas", "_Alignof", "_Atomic", "_BitInt", "_Bool", "_Complex", "_Decimal128",
                        "_Decimal32", "_Decimal64", "_Generic", "_Imaginary", "_Noreturn", "_Static_assert",
                        "_Thread_local"]


    """
    
    """
    def highlight_keywords(self):
        self.text_widget.tag_remove(self.keyword_tag, "1.0", tk.END)
        text_content = self.text_widget.get("1.0", tk.END)
        for word in self.keywords:
            matches = re.finditer(rf'\b{word}\b', text_content, flags=re.DOTALL)
            for match in matches:
                start_pos = match.start()
                end_pos = match.end()
                start = self.text_widget.index(f"1.0 + {start_pos}c")
                end = self.text_widget.index(f"1.0 + {end_pos}c")
                self.text_widget.tag_add(self.keyword_tag, start, end)
                self.text_widget.tag_configure(self.keyword_tag, foreground="orange")


    """
    
    """
    def highlight_types(self):
        self.text_widget.tag_remove(self.type_tag, "1.0", tk.END)
        text_content = self.text_widget.get("1.0", tk.END)
        for word in self.types:
            matches = re.finditer(rf'\b{word}\b', text_content, flags=re.DOTALL)
            for match in matches:
                start_pos = match.start()
                end_pos = match.end()
                start = self.text_widget.index(f"1.0 + {start_pos}c")
                end = self.text_widget.index(f"1.0 + {end_pos}c")
                self.text_widget.tag_add(self.type_tag, start, end)
                self.text_widget.tag_configure(self.type_tag, foreground="#77d197")


    """
    
    """
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

        matches = re.finditer(r'//.*?\n', text_content, flags=re.DOTALL)
        for match in matches:
            start_pos = match.start()
            end_pos = match.end()
            start = self.text_widget.index(f"1.0 + {start_pos}c")
            end = self.text_widget.index(f"1.0 + {end_pos}c")
            self.text_widget.tag_add(self.comment_tag, start, end)
            self.text_widget.tag_configure(self.comment_tag, foreground="gray")
    

    """
    
    """
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

        matches = re.finditer(r"'.*?'", text_content, flags=re.DOTALL)
        for match in matches:
            start_pos = match.start()
            end_pos = match.end()
            start = self.text_widget.index(f"1.0 + {start_pos}c")
            end = self.text_widget.index(f"1.0 + {end_pos}c")
            self.text_widget.tag_add(self.string_tag, start, end)
            self.text_widget.tag_configure(self.string_tag, foreground="green")


    """
    
    """
    def highlight_numbers(self):
        self.text_widget.tag_remove(self.number_tag, "1.0", tk.END)
        text_content = self.text_widget.get("1.0", tk.END)

        matches = re.finditer(r'\b\d+\b', text_content, flags=re.DOTALL)
        for match in matches:
            start_pos = match.start()
            end_pos = match.end()
            start = self.text_widget.index(f"1.0 + {start_pos}c")
            end = self.text_widget.index(f"1.0 + {end_pos}c")
            self.text_widget.tag_add(self.number_tag, start, end)
            self.text_widget.tag_configure(self.number_tag, foreground="#d31a38")


    """
    
    """
    def highlight_special(self):
        self.text_widget.tag_remove(self.special_tag, "1.0", tk.END)
        text_content = self.text_widget.get("1.0", tk.END)
        for word in self.special:
            matches = re.finditer(rf'\b{word}\b', text_content, flags=re.DOTALL)
            for match in matches:
                start_pos = match.start()
                end_pos = match.end()
                start = self.text_widget.index(f"1.0 + {start_pos}c")
                end = self.text_widget.index(f"1.0 + {end_pos}c")
                self.text_widget.tag_add(self.special_tag, start, end)
                self.text_widget.tag_configure(self.special_tag, foreground="blue")


    """
    
    """
    def highlight(self):
        self.highlight_keywords()
        self.highlight_types()
        self.highlight_special()
        self.highlight_numbers()
        self.highlight_strings()
        self.highlight_comments()
