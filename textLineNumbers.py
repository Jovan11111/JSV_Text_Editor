"""
==================================================================
Project Name:    JSV_Text_Editor
File Name:       textLineNumbers.py
Description:     A custom text editor with features tailored for UVM code, 
                 including syntax highlighting, autocompletion, auto-indentation,
                 line numbering, commenting, and find/replace functionality.

Author:          Jovan11111
Creation Date:   13.7.2024
Version:         1.0

==================================================================
"""

import tkinter as tk


class TextLineNumbers(tk.Canvas):
    def __init__(self, *args, **kwargs):
        tk.Canvas.__init__(self, *args, **kwargs, highlightthickness=0)
        self.textwidget = None


    """
    
    """
    def attach(self, text_widget):
        self.textwidget = text_widget


    """
    
    """
    def redraw(self, *args):
        self.delete("all")

        i = self.textwidget.index("@0,0")
        while True:
            dline = self.textwidget.dlineinfo(i)
            if dline is None:
                break
            y = dline[1]
            linenum = str(i).split(".")[0]
            self.create_text(2, y, anchor="nw", text=linenum, fill="#606366")
            i = self.textwidget.index("%s+1line" % i)
