"""
==================================================================
Project Name:    JSV_Text_Editor
File Name:       scrolltext.py
Description:     

Author:          Jovan11111
Creation Date:   13.7.2024
Version:         1.0

==================================================================
"""

import tkinter as tk

from components.textLineNumbers import TextLineNumbers

from highlighters.SVHihglighter import SVHighlighter
from highlighters.CHighlighter import CHighLighter
from highlighters.CppHighlighter import CppHighlighter
from highlighters.HTMLHighlighter import HTMLHighlighter
from highlighters.JavaHighlighter import JavaHighlighter
from highlighters.JSHighlighter import JavaScriptHighlighter
from highlighters.PyHighlighter import PyHighlighter

from autocompleters.UVMAutocompleter import UVMAutocompleter, uvm_classes, uvm_macros


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

        self.numberLines = TextLineNumbers(self, width=40, bg='#313335')
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
        self.text.bind('<Control-f>', self.toggle_widgets)
        self.text.bind("<Alt-c>", self.toggle_comment)
        self.text.bind("<Tab>", self.handle_tab)
        self.text.bind("<parenleft>", self.handle_left_paren)
        self.text.bind("<braceleft>", self.handle_left_brace)
        self.text.bind("<quotedbl>", self.handle_dblquote)
        self.text.bind("<bracketleft>", self.handle_left_bracket)
        self.text.bind("<apostrophe>", self.handle_quote)

        if self.file_path.split('.')[-1] == "c":
            self.highlighter = CHighLighter(self.text)
            print("C HAJLAJTER")
        else:
            self.highlighter = SVHighlighter(self.text)
            print("SV HAJLAJTER")
        self.frFram = tk.Frame(self.text)

        self.find_entry = tk.Entry(self.frFram, bg='#606366')
        self.find_entry.bind("<KeyRelease>", self.find)
        self.replace_entry = tk.Entry(self.frFram, bg='#606366')
        self.replace_button = tk.Button(self.frFram, text='FindNReplace', command=self.findNreplace, bg='#606366')


        self.find_entry.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        self.replace_entry.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)
        self.replace_button.pack(side=tk.LEFT, fill=tk.BOTH, expand=1)

        self.frFram.place(relx=1.0, y=0, anchor=tk.NE)
        self.frFram.place_forget()
        

    """
    autoIndent
    """
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


    """
    
    """
    def onScrollPress(self, *args):
        self.scrollbar.bind("<B1-Motion>", self.numberLines.redraw)


    """
    
    """
    def onScrollRelease(self, *args):
        self.scrollbar.unbind("<B1-Motion>", self.numberLines.redraw)


    """
    
    """
    def onPressDelay(self, *args):
        self.after(2, self.numberLines.redraw)
    

    """
    
    """
    def on_key_release(self, event):
        self.highlighter.highlight()

        if event.keysym not in ("BackSpace", "Delete", "Left", "Right", "Up", "Down"):
            self.text._autocomplete(event)
            cursor_index = self.text.index(tk.INSERT)

            #if event.keysym == 'braceleft':
            #    self.text.insert(cursor_index, '}')
            #    self.text.mark_set(tk.INSERT, cursor_index)
            #if event.keysym == 'parenleft':
            #    self.text.insert(cursor_index, ')')
            #    self.text.mark_set(tk.INSERT, cursor_index)
            #if event.keysym == 'quotedbl':
            #    self.text.insert(cursor_index, '"')
            #    self.text.mark_set(tk.INSERT, cursor_index)
            #if event.keysym == 'bracketleft':
            #    self.text.insert(cursor_index, ']')
            #    self.text.mark_set(tk.INSERT, cursor_index)
            #if event.keysym == 'apostrophe': 
            #    self.text.insert(cursor_index, "'")
            #    self.text.mark_set(tk.INSERT, cursor_index)


    """
    
    """
    def set_highlighter(self, file_path):
        if file_path.split('.')[-1] == "sv":
            self.highlighter = SVHighlighter(self.text)
        else:
            self.highlighter = CHighLighter(self.text)


    """
    
    """
    def get(self, *args, **kwargs):
        return self.text.get(*args, **kwargs)


    """
    
    """
    def insert(self, *args, **kwargs):
        return self.text.insert(*args, **kwargs)


    """
    
    """
    def delete(self, *args, **kwargs):
        return self.text.delete(*args, **kwargs)


    """
    
    """
    def index(self, *args, **kwargs):
        return self.text.index(*args, **kwargs)


    """ 
    
    """
    def redraw(self):
        self.numberLines.redraw()


    """
    
    """
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
    

    """
    
    """
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
    

    """
    
    """
    def delete_shortcut(self, *args, **kwargs):
        cursor_index = self.text.index(tk.INSERT)
        line_start = f"{cursor_index.split('.')[0]}.0"
        line_end = f"{cursor_index.split('.')[0]}.end"
        self.text.tag_add(tk.SEL, line_start, line_end)
        self.text.mark_set(tk.INSERT, line_end)
        self.text.delete(tk.SEL_FIRST, tk.SEL_LAST)
        self.text.tag_remove(tk.SEL, "1.0", tk.END)  


    """
    
    """
    def toggle_widgets(self, event):
        if self.frFram.winfo_viewable():
            self.frFram.place_forget()  
        else:
            self.frFram.place(relx=1.0, rely=1.0, x=1, y=0, anchor=tk.SE)  


    """
    
    """
    def find(self, *args, **kwargs):
        self.text.tag_remove('found', '1.0', tk.END) 

        s = self.find_entry.get()

        if (s): 
            idx = '1.0'
            while 1: 
                idx = self.text.search(s, idx, nocase=1, stopindex=tk.END)

                if not idx: break
                lastidx = '%s+%dc' % (idx, len(s))

                self.text.tag_add('found', idx, lastidx) 
                idx = lastidx 

            self.text.tag_config('found', foreground='red')
        self.find_entry.focus_set()


    """
    
    """
    def findNreplace(self):
        self.text.tag_remove('found', '1.0', tk.END) 

        s = self.find_entry.get()
        r = self.replace_entry.get()

        if (s and r): 
            idx = '1.0'
            while 1: 
                idx = self.text.search(s, idx, nocase=1, stopindex=tk.END)
                if not idx: break

                lastidx = '%s+%dc' % (idx, len(s))

                self.text.delete(idx, lastidx)
                self.text.insert(idx, r)

                lastidx = '%s+%dc' % (idx, len(r))

                self.text.tag_add('found', idx, lastidx) 
                idx = lastidx 

            self.text.tag_config('found', foreground='green', background='yellow')
        self.find_entry.focus_set()


    """
    
    """
    def toggle_comment(self, event):
        try:
            selected_text = self.text.selection_get()
            start = self.text.index(tk.SEL_FIRST)
            self.text.insert(start, '/*')
            end = self.text.index(tk.SEL_LAST)
            self.text.insert(end, '*/')
        except tk.TclError:
            line_start = self.text.index("insert linestart")
            line_end = self.text.index("insert lineend")
            line_text = self.text.get(line_start, line_end)
            
            if line_text.strip().startswith("//"):
                uncommented_text = line_text.replace("//", "", 1)
                self.text.delete(line_start, line_end)
                self.text.insert(line_start, uncommented_text)
            else:
                self.text.insert(line_start, "//")
        
        return 'break'
    

    """
    
    """
    def handle_tab(self, event):
        try:
            selected_text = self.text.selection_get()
            start = self.text.index(tk.SEL_FIRST)
            end = self.text.index(tk.SEL_LAST)
            
            start_line = int(start.split('.')[0])
            end_line = int(end.split('.')[0])
            
            for line in range(start_line, end_line + 1):
                line_start = f"{line}.0"
                self.text.insert(line_start, '\t')
            
            return 'break'
        except tk.TclError:
            return None

    def load_file(self, file_path):
        self.file_path = file_path
        with open(file_path, 'r') as file:
            content = file.read()
            self.text.delete(1.0, tk.END)
            self.text.insert(tk.END, content)

        if self.file_path.split('.')[-1] == "c":
            self.highlighter = CHighLighter(self.text)
        
        elif self.file_path.split('.')[-1] == "java":
            self.highlighter = JavaHighlighter(self.text)

        elif self.file_path.split('.')[-1] == "html":
            self.highlighter = HTMLHighlighter(self.text)
        
        elif self.file_path.split('.')[-1] == "py":
            self.highlighter = PyHighlighter(self.text)
        
        elif self.file_path.split('.')[-1] == "js":
            self.highlighter = JavaScriptHighlighter(self.text)
        
        elif self.file_path.split('.')[-1] == "cpp" or self.file_path.split('.')[-1] == "hpp":
            self.highlighter = CppHighlighter(self.text)

        else:
            self.highlighter = SVHighlighter(self.text)
        
        self.highlighter.highlight()

    def save_file(self, file_path):
        with open(file_path, 'w') as file:
            content = self.text.get(1.0, tk.END)
            file.write(content)

    def handle_left_paren(self, event):
        try:
            selected_text = self.text.selection_get()
            start = self.text.index(tk.SEL_FIRST)
            self.text.insert(start, '(')
            end = self.text.index(tk.SEL_LAST)
            self.text.insert(end, ')')
        except tk.TclError:
            cursor_index = self.text.index(tk.INSERT)
            self.text.insert(cursor_index, ')')
            self.text.mark_set(tk.INSERT, cursor_index)
            self.text.insert(cursor_index, '(')
        
        return 'break'
    
    def handle_left_brace(self, event):
        try:
            selected_text = self.text.selection_get()
            start = self.text.index(tk.SEL_FIRST)
            self.text.insert(start, '{')
            end = self.text.index(tk.SEL_LAST)
            self.text.insert(end, '}')
        except tk.TclError:
            cursor_index = self.text.index(tk.INSERT)
            self.text.insert(cursor_index, '}')
            self.text.mark_set(tk.INSERT, cursor_index)
            self.text.insert(cursor_index, '{')
        
        return 'break'
    
    def handle_left_bracket(self, event):
        try:
            selected_text = self.text.selection_get()
            start = self.text.index(tk.SEL_FIRST)
            self.text.insert(start, '[')
            end = self.text.index(tk.SEL_LAST)
            self.text.insert(end, ']')
        except tk.TclError:
            cursor_index = self.text.index(tk.INSERT)
            self.text.insert(cursor_index, ']')
            self.text.mark_set(tk.INSERT, cursor_index)
            self.text.insert(cursor_index, '[')
        
        return 'break'

    def handle_dblquote(self, event):
        try:
            selected_text = self.text.selection_get()
            start = self.text.index(tk.SEL_FIRST)
            self.text.insert(start, '"')
            end = self.text.index(tk.SEL_LAST)
            self.text.insert(end, '"')
        except tk.TclError:
            cursor_index = self.text.index(tk.INSERT)
            self.text.insert(cursor_index, '"')
            self.text.mark_set(tk.INSERT, cursor_index)
            self.text.insert(cursor_index, '"')
        
        return 'break'
    
    def handle_quote(self, event):
        try:
            selected_text = self.text.selection_get()
            start = self.text.index(tk.SEL_FIRST)
            self.text.insert(start, "'")
            end = self.text.index(tk.SEL_LAST)
            self.text.insert(end, "'")
        except tk.TclError:
            cursor_index = self.text.index(tk.INSERT)
            self.text.insert(cursor_index, "'")
            self.text.mark_set(tk.INSERT, cursor_index)
            self.text.insert(cursor_index, "'")
        
        return 'break'
    
    