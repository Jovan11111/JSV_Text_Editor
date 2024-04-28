from tkinter import ttk


class FileTree(ttk.Treeview):
    def __init__(self, root, *args, **kwargs):
        ttk.Treeview.__init__(self, root, *args, **kwargs)
