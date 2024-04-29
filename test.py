import tkinter as tk

class TextEditor:
    def __init__(self, root):
        self.root = root
        self.text = tk.Text(root)
        self.text.pack(expand=True, fill="both")

        # Bind the Return key to the auto_indent function
        self.text.bind("<Return>", self.auto_indent)

    def auto_indent(self, event):
        # Get the index of the current cursor position
        cursor_index = self.text.index(tk.INSERT)

        # Get the content of the current line
        line, column = cursor_index.split(".")
        line_content = self.text.get(f"{line}.0", f"{line}.end")

        # Count the number of leading spaces or tabs
        indent_level = 0
        for char in line_content:
            if char == "\t":
                indent_level += 1
            else:
                break

        # Insert the same indentation in the new line
        self.text.insert(tk.INSERT, "\n" + "\t" * indent_level)

        # Return 'break' to prevent the default behavior of Enter key
        return 'break'

root = tk.Tk()
editor = TextEditor(root)
root.mainloop()
