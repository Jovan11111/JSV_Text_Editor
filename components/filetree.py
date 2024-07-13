"""
==================================================================
Project Name:    JSV_Text_Editor
File Name:       filetree.py
Description:     A custom text editor with features tailored for UVM code, 
                 including syntax highlighting, autocompletion, auto-indentation,
                 line numbering, commenting, and find/replace functionality.

Author:          Jovan11111
Creation Date:   13.7.2024
Version:         1.0

==================================================================
"""

from tkinter import ttk


class FileTree(ttk.Treeview):
    def __init__(self, root, *args, **kwargs):
        ttk.Treeview.__init__(self, root, *args, **kwargs)
