"""
==================================================================
Project Name:    JSV_Text_Editor
File Name:       JavaHighlighter.py
Description:     

Author:          Jovan11111
Creation Date:   16.7.2024
Version:         1.0

==================================================================
"""

from highLighter import Highlighter
import re
import tkinter as tk


class JavaHighlighter(Highlighter):
    def __init__(self, text_widget):
        super().__init__(text_widget)
        self.keyword_tag = "keyword"
        self.type_tag = "type"
        self.comment_tag = "comment"
        self.string_tag = "string"
        self.annotation_tag = "annotation"
        self.number_tag = "number"

        self.keywords = [
            "abstract", "continue", "for", "new", "switch", "assert", "default", "goto", "package", "synchronized", 
            "boolean", "do", "if", "private", "this", "break", "double", "implements", "protected", "throw", 
            "byte", "else", "import", "public", "throws", "case", "enum", "instanceof", "return", "transient", 
            "catch", "extends", "int", "short", "try", "char", "final", "interface", "static", "void", 
            "class", "finally", "long", "strictfp", "volatile", "const", "float", "native", "super", "while"
        ]

        self.types = [
            "byte", "short", "int", "long", "float", "double", "boolean", "char", "String", "Object"
        ]

        self.annotations = [
            "@Override", "@SuppressWarnings", "@Deprecated", "@FunctionalInterface", "@SafeVarargs"
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

    def highlight_comments(self):
        self.text_widget.tag_remove(self.comment_tag, "1.0", tk.END)
        text_content = self.text_widget.get("1.0", tk.END)

        # Multiline comments
        matches = re.finditer(r'/\*.*?\*/', text_content, flags=re.DOTALL)
        for match in matches:
            start_pos = match.start()
            end_pos = match.end()
            start = self.text_widget.index(f"1.0 + {start_pos}c")
            end = self.text_widget.index(f"1.0 + {end_pos}c")
            self.text_widget.tag_add(self.comment_tag, start, end)
            self.text_widget.tag_configure(self.comment_tag, foreground="gray")

        # Single line comments
        matches = re.finditer(r'//.*?\n', text_content, flags=re.DOTALL)
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

    def highlight_annotations(self):
        self.text_widget.tag_remove(self.annotation_tag, "1.0", tk.END)
        text_content = self.text_widget.get("1.0", tk.END)
        for word in self.annotations:
            matches = re.finditer(rf'\b{word}\b', text_content, flags=re.DOTALL)
            for match in matches:
                start_pos = match.start()
                end_pos = match.end()
                start = self.text_widget.index(f"1.0 + {start_pos}c")
                end = self.text_widget.index(f"1.0 + {end_pos}c")
                self.text_widget.tag_add(self.annotation_tag, start, end)
                self.text_widget.tag_configure(self.annotation_tag, foreground="#add8e6")
    
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
        self.highlight_types()
        self.highlight_annotations()
        self.highlight_strings()
        self.highlight_comments()
        self.highlight_numbers()
