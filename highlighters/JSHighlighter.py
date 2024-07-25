"""
==================================================================
Project Name:    JSV_Text_Editor
File Name:       JavaScriptHighlighter.py
Description:     JavaScript syntax highlighter for JSV Text Editor.

Author:          Jovan11111
Creation Date:   16.7.2024
Version:         1.0

==================================================================
"""

from highlighters.highLighter import Highlighter
import re
import tkinter as tk

class JavaScriptHighlighter(Highlighter):
    def __init__(self, text_widget):
        super().__init__(text_widget)
        self.keyword_tag = "keyword"
        self.builtin_tag = "builtin"
        self.comment_tag = "comment"
        self.string_tag = "string"
        self.number_tag = "number"
        self.function_tag = "function"

        self.keywords = [
            "abstract", "await", "boolean", "break", "byte", "case", "catch", "char", "class", "const", "continue",
            "debugger", "default", "delete", "do", "double", "else", "enum", "export", "extends", "false", "final",
            "finally", "float", "for", "function", "goto", "if", "implements", "import", "in", "instanceof", "int",
            "interface", "let", "long", "native", "new", "null", "package", "private", "protected", "public", "return",
            "short", "static", "super", "switch", "synchronized", "this", "throw", "throws", "transient", "true",
            "try", "typeof", "var", "void", "volatile", "while", "with", "yield"
        ]

        self.builtins = [
            "Array", "Date", "eval", "function", "hasOwnProperty", "Infinity", "isFinite", "isNaN", "isPrototypeOf",
            "length", "Math", "NaN", "name", "Number", "Object", "prototype", "String", "toString", "undefined", 
            "valueOf"
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
                self.text_widget.tag_configure(self.builtin_tag, foreground="#d912fb")

    def highlight_comments(self):
        self.text_widget.tag_remove(self.comment_tag, "1.0", tk.END)
        text_content = self.text_widget.get("1.0", tk.END)

        matches = re.finditer(r'//.*?\n', text_content, flags=re.DOTALL)
        for match in matches:
            start_pos = match.start()
            end_pos = match.end()
            start = self.text_widget.index(f"1.0 + {start_pos}c")
            end = self.text_widget.index(f"1.0 + {end_pos}c")
            self.text_widget.tag_add(self.comment_tag, start, end)
            self.text_widget.tag_configure(self.comment_tag, foreground="gray")

        matches = re.finditer(r'/\*.*?\*/', text_content, flags=re.DOTALL)
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

        matches = re.finditer(r'\".*?\"|\'[^\']*\'', text_content, flags=re.DOTALL)
        for match in matches:
            start_pos = match.start()
            end_pos = match.end()
            start = self.text_widget.index(f"1.0 + {start_pos}c")
            end = self.text_widget.index(f"1.0 + {end_pos}c")
            self.text_widget.tag_add(self.string_tag, start, end)
            self.text_widget.tag_configure(self.string_tag, foreground="green")

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

    def highlight_functions(self):
        self.text_widget.tag_remove(self.function_tag, "1.0", tk.END)
        text_content = self.text_widget.get("1.0", tk.END)

        matches = re.finditer(r'\bfunction\s+\w+\b', text_content, flags=re.DOTALL)
        for match in matches:
            start_pos = match.start()
            end_pos = match.end()
            start = self.text_widget.index(f"1.0 + {start_pos}c")
            end = self.text_widget.index(f"1.0 + {end_pos}c")
            self.text_widget.tag_add(self.function_tag, start, end)
            self.text_widget.tag_configure(self.function_tag, foreground="#d912fb")

    def highlight(self):
        self.highlight_keywords()
        self.highlight_builtins()
        self.highlight_comments()
        self.highlight_strings()
        self.highlight_numbers()
        self.highlight_functions()
