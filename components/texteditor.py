import os
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from components.scrolltext import ScrollText
from components.filetree import FileTree
from tkterm import Terminal

class TextEditor(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("JSV Text Editor")
        ttk.Style().configure("Treeview", background="#2b2b2b", foreground="white", fieldbackground="#2b2b2b")

        self.file_path = None
        self.directory_path = None

        # Create PanedWindow for organizing resizable components
        self.paned_window = tk.PanedWindow(self, orient=tk.HORIZONTAL)
        self.paned_window.pack(fill=tk.BOTH, expand=True)

        # Left side: FileTree
        self.file_tree = FileTree(self.paned_window)
        self.paned_window.add(self.file_tree)

        # Right side: PanedWindow for ScrollText (top right) and Terminal (bottom right)
        self.paned_window_right = tk.PanedWindow(self.paned_window, orient=tk.VERTICAL)
        self.paned_window.add(self.paned_window_right)

        # Top right: ScrollText
        self.scroll_text = ScrollText(self.paned_window_right)
        self.scroll_text.text.config(tabs=32)
        self.paned_window_right.add(self.scroll_text)

        # Bottom right: Terminal
        self.terminal = Terminal(self.paned_window_right)
        self.paned_window_right.add(self.terminal)

        # Configure resizing behavior
        self.paned_window.pack(fill=tk.BOTH, expand=True)
        self.paned_window.paneconfigure(self.file_tree, minsize=150)  # Minimum width for FileTree
        self.paned_window.paneconfigure(self.paned_window_right, minsize=200)  # Minimum height for PanedWindow on right

        self.create_menu()

        self.file_tree.bind("<<TreeviewSelect>>", self.on_tree_select)
        self.file_tree.bind("<<TreeviewOpen>>", self.on_tree_open)

        self.bind("<Control-s>", self.save_file)
        self.bind("<Control-n>", self.new_file)
        self.bind("<Control-Shift-S>", self.save_as_file)
        self.bind("<Control-o>", self.open_file)
        self.bind("<Control-Shift-F>", self.open_folder)

    def create_menu(self):
        menu = tk.Menu(self)

        file_menu = tk.Menu(menu, tearoff=0)
        file_menu.add_command(label="New File (Ctrl+N)", command=self.new_file)
        file_menu.add_command(label="Open File (Ctrl+O)", command=self.open_file)
        file_menu.add_command(label="Open Folder (Ctrl+Shift+F)", command=self.open_folder)
        file_menu.add_command(label="Save File (Ctrl+S)", command=self.save_file)
        file_menu.add_command(label="Save As File (Ctrl+Shift+S)", command=self.save_as_file)

        menu.add_cascade(label="File", menu=file_menu)
        self.config(menu=menu)

    def new_file(self, *args):
        self.scroll_text.text.delete(1.0, tk.END)
        self.file_path = None

    def open_file(self, *args):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.file_path = file_path
            self.scroll_text.load_file(file_path)

    def open_folder(self, *args):
        directory_path = filedialog.askdirectory()
        if directory_path:
            self.directory_path = directory_path
            self.file_tree.populate_tree(directory_path)

    def save_file(self, *args):
        if self.file_path:
            self.scroll_text.save_file(self.file_path)
        else:
            self.save_as_file()

    def save_as_file(self, *args):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file_path:
            self.file_path = file_path
            self.scroll_text.save_file(file_path)

    def on_tree_select(self, event):
        selected_item = self.file_tree.selection()[0]
        file_path = self.file_tree.get_file_path(selected_item)
        if os.path.isfile(file_path):
            self.file_path = file_path
            self.scroll_text.load_file(file_path)

    def on_tree_open(self, event):
        selected_item = self.file_tree.selection()[0]
        self.file_tree.update_tree(selected_item)


