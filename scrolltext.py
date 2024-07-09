import tkinter as tk
import highLighter
import textLineNumbers
from SVHihglighter import SVHighlighter
from CHighlighter import CHighLighter
from UVMAutocompleter import UVMAutocompleter, uvm_classes, uvm_macros


class ScrollText(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        self.file_path = ""
        self.auto_indent_enabled = True
        tk.Frame.__init__(self, *args, **kwargs)

        self.text = UVMAutocompleter(self, uvm_classes=uvm_classes, uvm_macros=uvm_macros,
                                     bg='#2b2b2b', foreground="#d1dce8",
                                     insertbackground='white',
                                     selectbackground="#4e77e7", width=120, height=30,
                                     undo=True, autoseparators=True, maxundo=-1
                                    )

        self.scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL, command=self.text.yview)
        self.text.configure(yscrollcommand=self.scrollbar.set)

        self.numberLines = textLineNumbers.TextLineNumbers(self, width=40, bg='#313335')
        self.numberLines.attach(self.text)

        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.numberLines.pack(side=tk.LEFT, fill=tk.Y, padx=(5, 0))
        self.text.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.text.bind("<Key>", self.onPressDelay)
        self.text.bind("<Button-1>", self.numberLines.redraw)
        self.scrollbar.bind("<Button-1>", self.onScrollPress)
        self.text.bind("<MouseWheel>", self.onPressDelay)
        self.text.bind("<KeyRelease>", self.on_key_release)
        self.text.bind("<Return>", self.autoIndent)
        self.text.bind("<KP_Enter>", self.autoIndent)

        self.text.bind("<Control-c>", self.copy_shortcut)
        self.text.bind("<Control-x>", self.cut_shortcut)
        self.text.bind("<Control-d>", self.delete_shortcut)

        if self.file_path.split('.')[-1] == "c":
            self.highlighter = CHighLighter(self.text)
        else:
            self.highlighter = SVHighlighter(self.text)

    def autoIndent(self, event):
        if self.auto_indent_enabled:
            cursor_index = self.text.index(tk.INSERT)

            line, column = cursor_index.split(".")
            line_content = self.text.get(f"{line}.0", f"{line}.end")

            indent_level = 0
            for char in line_content:
                if char == "\t":
                    indent_level += 1
                else:
                    break

            self.text.insert(tk.INSERT, "\n" + "\t" * indent_level)
            self.numberLines.redraw()
            self.text.see(tk.INSERT) 
            return 'break'
        return None

    def onScrollPress(self, *args):
        self.scrollbar.bind("<B1-Motion>", self.numberLines.redraw)

    def onScrollRelease(self, *args):
        self.scrollbar.unbind("<B1-Motion>", self.numberLines.redraw)

    def onPressDelay(self, *args):
        self.after(2, self.numberLines.redraw)

    def on_key_release(self, event):
        self.highlighter.highlight()

        if event.keysym not in ("BackSpace", "Delete", "Left", "Right", "Up", "Down"):
            self.text._autocomplete(event)
            cursor_index = self.text.index(tk.INSERT)
            if event.keysym == 'braceleft':
                self.text.insert(cursor_index, '}')
                self.text.mark_set(tk.INSERT, cursor_index)
            if event.keysym == 'parenleft':
                self.text.insert(cursor_index, ')')
                self.text.mark_set(tk.INSERT, cursor_index)
            if event.keysym == 'quotedbl':
                self.text.insert(cursor_index, '"')
                self.text.mark_set(tk.INSERT, cursor_index)
            if event.keysym == 'bracketleft':
                self.text.insert(cursor_index, ']')
                self.text.mark_set(tk.INSERT, cursor_index)
            if event.keysym == 'apostrophe': 
                self.text.insert(cursor_index, "'")
                self.text.mark_set(tk.INSERT, cursor_index)


    def set_highlighter(self, file_path):
        if file_path.split('.')[-1] == "sv":
            self.highlighter = SVHighlighter(self.text)
        else:
            self.highlighter = CHighLighter(self.text)

    def get(self, *args, **kwargs):
        return self.text.get(*args, **kwargs)

    def insert(self, *args, **kwargs):
        return self.text.insert(*args, **kwargs)

    def delete(self, *args, **kwargs):
        return self.text.delete(*args, **kwargs)

    def index(self, *args, **kwargs):
        return self.text.index(*args, **kwargs)

    def redraw(self):
        self.numberLines.redraw()

    def copy_shortcut(self, event):
        try:
            selected_text = self.text.selection_get()
        except tk.TclError:
            cursor_index = self.text.index(tk.INSERT)
            line_start = f"{cursor_index.split('.')[0]}.0"
            line_end = f"{cursor_index.split('.')[0]}.end"
            self.text.tag_add(tk.SEL, line_start, line_end)
            self.text.mark_set(tk.INSERT, line_end)
            self.text.see(tk.INSERT)
            selected_text = self.text.selection_get()

        self.clipboard_clear()
        self.clipboard_append(selected_text)
        self.text.tag_remove(tk.SEL, "1.0", tk.END)  
        return 'break'
    
    def cut_shortcut(self, *args, **kwargs):
        try:
            selected_text = self.text.selection_get()
        except tk.TclError:
            cursor_index = self.text.index(tk.INSERT)
            line_start = f"{cursor_index.split('.')[0]}.0"
            line_end = f"{cursor_index.split('.')[0]}.end"
            self.text.tag_add(tk.SEL, line_start, line_end)
            self.text.mark_set(tk.INSERT, line_end)
            self.text.see(tk.INSERT)
            selected_text = self.text.selection_get()

        self.clipboard_clear()
        self.clipboard_append(selected_text)
        self.text.delete(tk.SEL_FIRST, tk.SEL_LAST)  
        self.text.tag_remove(tk.SEL, "1.0", tk.END)  
        return 'break'
    
    def delete_shortcut(self, *args, **kwargs):
        cursor_index = self.text.index(tk.INSERT)
        line_start = f"{cursor_index.split('.')[0]}.0"
        line_end = f"{cursor_index.split('.')[0]}.end"
        self.text.tag_add(tk.SEL, line_start, line_end)
        self.text.mark_set(tk.INSERT, line_end)
        self.text.delete(tk.SEL_FIRST, tk.SEL_LAST)
        self.text.tag_remove(tk.SEL, "1.0", tk.END)  
