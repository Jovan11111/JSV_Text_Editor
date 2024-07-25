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


import os
import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class FileTree(ttk.Treeview):
    def __init__(self, root, *args, **kwargs):
        super().__init__(root, *args, **kwargs)
        self.root = root

        # Load icons
        self.folder_icon = ImageTk.PhotoImage(Image.open("./static/folder-7-16.png").resize((16, 16), Image.ADAPTIVE))
        self.file_icon = ImageTk.PhotoImage(Image.open("./static/report-3-16.png").resize((16, 16), Image.ADAPTIVE))

        self.bind("<Double-1>", self.on_double_click)
        self.bind("<Return>", self.on_double_click)
        self.bind("<<TreeviewOpen>>", self.on_tree_open)
        self.bind("<<TreeviewExpand>>", self.on_tree_expand)

    def populate_tree(self, folder_path):
        self.delete(*self.get_children())
        self.folder_path = folder_path
        node = self.insert("", "end", text=os.path.basename(folder_path), values=[folder_path], open=True, image=self.folder_icon)
        self.add_items(node, folder_path)

    def add_items(self, parent, directory):
        items = os.listdir(directory)
        # Separate folders and files
        folders = [item for item in items if os.path.isdir(os.path.join(directory, item))]
        files = [item for item in items if os.path.isfile(os.path.join(directory, item))]
        
        # Add folders first
        for item in sorted(folders):
            path = os.path.join(directory, item)
            folder_id = self.insert(parent, "end", text=item, values=[path], open=False, image=self.folder_icon)
            self.insert(folder_id, "end")  # Add a dummy child to make it expandable
        
        # Add files next
        for item in sorted(files):
            path = os.path.join(directory, item)
            self.insert(parent, "end", text=item, values=[path], image=self.file_icon)

    def update_tree(self, item):
        # Clear the dummy child
        self.delete(*self.get_children(item))
        # Add actual files and folders
        path = self.item(item, 'values')[0]
        self.add_items(item, path)

    def on_double_click(self, event):
        item = self.focus()
        file_path = self.get_file_path(item)
        if file_path and os.path.isfile(file_path):
            self.root.event_generate("<<TreeviewOpen>>")

    def on_tree_open(self, event):
        item = self.focus()
        file_path = self.get_file_path(item)
        if file_path and os.path.isfile(file_path):
            self.root.event_generate("<<TreeviewOpen>>")

    def on_tree_expand(self, event):
        item = self.focus()
        self.update_tree(item)

    def get_file_path(self, item):
        parent_id = self.parent(item)
        if parent_id:
            parent_path = self.get_file_path(parent_id)
            return os.path.join(parent_path, self.item(item, "text"))
        else:
            return self.folder_path if self.item(item, "text") == os.path.basename(self.folder_path) else os.path.join(self.folder_path, self.item(item, "text"))
