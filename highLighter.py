import tkinter as tk
import re


class Highlighter:
    def __init__(self, text_widget):
        self.text_widget = text_widget
        self.tag_name = "green"

    def highlight_jovan(self):
        self.text_widget.tag_remove(self.tag_name, "1.0", tk.END)  # Clear previous highlights
        text_content = self.text_widget.get("1.0", tk.END)
        matches = re.finditer(r'\bJOVAN\b', text_content, flags=re.IGNORECASE)

        for match in matches:
            start_pos = match.start()
            end_pos = match.end()
            start = self.text_widget.index(f"1.0 + {start_pos}c")
            end = self.text_widget.index(f"1.0 + {end_pos}c")
            self.text_widget.tag_add(self.tag_name, start, end)
            self.text_widget.tag_configure(self.tag_name, foreground="green")