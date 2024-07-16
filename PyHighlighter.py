"""
==================================================================
Project Name:    JSV_Text_Editor
File Name:       PyHighlighter.py
Description:     Python syntax highlighter for JSV Text Editor.

Author:          Jovan11111
Creation Date:   16.7.2024
Version:         1.0

==================================================================
"""

from highLighter import Highlighter
import re
import tkinter as tk

class PyHighlighter(Highlighter):
    def __init__(self, text_widget):
        super().__init__(text_widget)
        self.keyword_tag = "keyword"
        self.builtin_tag = "builtin"
        self.comment_tag = "comment"
        self.string_tag = "string"
        self.class_tag = "class"
        self.number_tag = "number"

        self.keywords = [
            "False", "await", "else", "import", "pass", "None", "break", "except", "in", "raise", "True", "class", 
            "finally", "is", "return", "and", "continue", "for", "lambda", "try", "as", "def", "from", "nonlocal", 
            "while", "assert", "del", "global", "not", "with", "async", "elif", "if", "or", "yield"
        ]

        self.builtins = [
            "abs", "dict", "help", "min", "setattr", "all", "dir", "hex", "next", "slice", "any", "divmod", "id", 
            "object", "sorted", "ascii", "enumerate", "input", "oct", "staticmethod", "bin", "eval", "int", "open", 
            "str", "bool", "exec", "isinstance", "ord", "sum", "bytearray", "filter", "issubclass", "pow", "super", 
            "bytes", "float", "iter", "print", "tuple", "callable", "format", "len", "property", "type", "chr", 
            "frozenset", "list", "range", "vars", "classmethod", "getattr", "locals", "repr", "zip", "compile", 
            "globals", "map", "reversed", "__import__", "complex", "hasattr", "max", "round", "delattr", "hash", 
            "memoryview", "set"
        ]

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

    def highlight_builtins(self):
        self.text_widget.tag_remove(self.builtin_tag, "1.0", tk.END)
        text_content = self.text_widget.get("1.0", tk.END)
        for word in self.builtins:
            matches = re.finditer(rf'\b{word}\b', text_content, flags=re.DOTALL)
            for match in matches:
                start_pos = match.start()
                end_pos = match.end()
                start = self.text_widget.index(f"1.0 + {start_pos}c")
                end = self.text_widget.index(f"1.0 + {end_pos}c")
                self.text_widget.tag_add(self.builtin_tag, start, end)
                self.text_widget.tag_configure(self.builtin_tag, foreground="#33abf9")

    def highlight_comments(self):
        self.text_widget.tag_remove(self.comment_tag, "1.0", tk.END)
        text_content = self.text_widget.get("1.0", tk.END)

        matches = re.finditer(r'#.*?\n', text_content, flags=re.DOTALL)
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

        matches = re.finditer(r'\".*?\"|\'[^\']*\'|\'\'\'.*?\'\'\'|\"\"\".*?\"\"\"', text_content, flags=re.DOTALL)
        for match in matches:
            start_pos = match.start()
            end_pos = match.end()
            start = self.text_widget.index(f"1.0 + {start_pos}c")
            end = self.text_widget.index(f"1.0 + {end_pos}c")
            self.text_widget.tag_add(self.string_tag, start, end)
            self.text_widget.tag_configure(self.string_tag, foreground="green")

    def highlight_classes(self):
        self.text_widget.tag_remove(self.class_tag, "1.0", tk.END)
        text_content = self.text_widget.get("1.0", tk.END)

        matches = re.finditer(r'\bclass\s+\w+', text_content, flags=re.DOTALL)
        for match in matches:
            start_pos = match.start()
            end_pos = match.end()
            start = self.text_widget.index(f"1.0 + {start_pos}c")
            end = self.text_widget.index(f"1.0 + {end_pos}c")
            self.text_widget.tag_add(self.class_tag, start, end)
            self.text_widget.tag_configure(self.class_tag, foreground="#d912fb")
    
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

    def highlight(self):
        self.highlight_keywords()
        self.highlight_builtins()
        self.highlight_comments()
        self.highlight_strings()
        self.highlight_classes()
        self.highlight_numbers()
