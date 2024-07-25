from highlighters.highLighter import Highlighter
import tkinter as tk
import re

class CppHighlighter(Highlighter):
    def __init__(self, text_widget):
        self.text_widget = text_widget

        self.keyword_tag = "keyword"
        self.type_tag = "type"
        self.comment_tag = "comment"
        self.string_tag = "string"
        self.number_tag = "number"
        self.standard_library_tag = "standard_library"
        self.class_tag = "class"

        # Define lists of keywords and other elements to highlight
        self.keywords = [
            "auto", "bool", "break", "case", "char", "class", "const", "continue",
            "default", "do", "double", "else", "enum", "extern", "false", "float",
            "for", "goto", "if", "inline", "int", "long", "namespace", "new", "nullptr",
            "operator", "private", "protected", "public", "return", "short", "sizeof",
            "static", "struct", "switch", "template", "this", "true", "typedef", "union",
            "unsigned", "void", "volatile", "while"
        ]

        self.types = [
            "int", "float", "double", "char", "long", "short", "bool",
            "void", "auto", "unsigned", "signed", "const", "volatile", "wchar_t"
        ]

        self.standard_library_functions = [
            "cout", "cin", "endl", "malloc", "free", "printf", "scanf", "fclose",
            "fopen", "fprintf", "fscanf", "sprintf", "sscanf", "strcpy", "strcat", "strlen",
            "memcpy", "memmove", "memset", "strcmp", "strncmp", "strchr", "strstr", "strtok"
        ]

        self.comment_patterns = [
            r'//.*?\n',     # Single-line comments
            r'/\*.*?\*/',   # Multi-line comments
        ]

        self.string_pattern = r'"(.*?)"'

        self.number_pattern = r'\b\d+\b'

        # Configure tag settings
        self.text_widget.tag_configure(self.keyword_tag, foreground="orange")
        self.text_widget.tag_configure(self.type_tag, foreground="#77d197")
        self.text_widget.tag_configure(self.comment_tag, foreground="gray")
        self.text_widget.tag_configure(self.string_tag, foreground="green")
        self.text_widget.tag_configure(self.number_tag, foreground="#d31a38")
        self.text_widget.tag_configure(self.standard_library_tag, foreground="#cd7f32")
        self.text_widget.tag_configure(self.class_tag, foreground="#33abf9")

    def remove_all_tags(self):
        for tag in [self.keyword_tag, self.type_tag, self.comment_tag,
                    self.string_tag, self.number_tag, self.standard_library_tag, self.class_tag]:
            self.text_widget.tag_remove(tag, "1.0", tk.END)

    def highlight(self):
        self.remove_all_tags()
        self.highlight_keywords()
        self.highlight_types()
        self.highlight_standard_library_functions()
        self.highlight_comments()
        self.highlight_strings()
        self.highlight_numbers()
        self.highlight_classes()

    def highlight_keywords(self):
        self.highlight_patterns_with_tag(self.keywords, self.keyword_tag)

    def highlight_types(self):
        self.highlight_patterns_with_tag(self.types, self.type_tag)

    def highlight_standard_library_functions(self):
        self.highlight_patterns_with_tag(self.standard_library_functions, self.standard_library_tag)

    def highlight_comments(self):
        for pattern in self.comment_patterns:
            self.highlight_pattern_with_tag(pattern, self.comment_tag)

    def highlight_strings(self):
        self.highlight_pattern_with_tag(self.string_pattern, self.string_tag)

    def highlight_numbers(self):
        self.highlight_pattern_with_tag(self.number_pattern, self.number_tag)

    def highlight_classes(self):
        self.highlight_pattern_with_tag(r'\bclass\s+(\w+)', self.class_tag)

    def highlight_patterns_with_tag(self, patterns, tag):
        for pattern in patterns:
            self.highlight_pattern_with_tag(rf'\b{pattern}\b', tag)

    def highlight_pattern_with_tag(self, pattern, tag):
        text_content = self.text_widget.get("1.0", tk.END)
        for match in re.finditer(pattern, text_content, flags=re.DOTALL):
            start_pos, end_pos = match.span()
            start = self.text_widget.index(f"1.0 + {start_pos}c")
            end = self.text_widget.index(f"1.0 + {end_pos}c")
            self.text_widget.tag_add(tag, start, end)

