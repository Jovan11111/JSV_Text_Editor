import tkinter as tk
from tkinter import filedialog
from scrolltext import ScrollText
from filetree import FileTree
from preferences import Preferences
import os


class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("JSVTE")

        # Save the folder path
        self.folder_path = ""

        # Create the text area
        self.create_scroll_text()
        # blabla
        # Create the file tree
        self.file_tree = FileTree(self.root)
        self.file_tree.pack(side='left', fill='both', expand=True)

        # Create menu bar
        self.menu_bar = tk.Menu(self.root)

        # File menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="New File", command=self.new_file, accelerator="Ctrl+N")
        self.file_menu.add_command(label="Open File", command=self.open_file, accelerator="Ctrl+O")
        self.file_menu.add_command(label="Open Folder", command=self.open_folder, accelerator="Alt+F")
        self.file_menu.add_command(label="Save", command=self.save_file, accelerator="Ctrl+S")
        self.file_menu.add_command(label="Save As", command=self.save_as_file, accelerator="Ctrl+Shift+S")
        self.file_menu.add_command(label="Exit", command=self.root.quit)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

        # Edit menu
        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.edit_menu.add_command(label="Undo", command=self.undo)
        self.edit_menu.add_command(label="Redo", command=self.redo)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)

        # Preferences menu
        self.preferences = Preferences(self.root, self)
        self.preferences_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.preferences_menu.add_command(label="General", command=self.preferences.open_preferences)
        self.menu_bar.add_cascade(label="Preferences", menu=self.preferences_menu)

        self.root.config(menu=self.menu_bar)

        # Bind the open selected file method to the file tree
        self.file_tree.bind("<<TreeviewOpen>>", self.open_selected_file)

        self.root.bind("<Control-n>", lambda event: self.new_file())
        self.root.bind("<Control-o>", lambda event: self.open_file())
        self.root.bind("<Alt-f>", lambda event: self.open_folder())
        self.root.bind("<Control-s>", lambda event: self.save_file())
        self.root.bind("<Control-Shift-S>", lambda event: self.save_as_file())

    def create_scroll_text(self):
        if hasattr(self, 'scroll_text'):
            self.scroll_text.destroy()

        self.scroll_text = ScrollText(self.root)
        self.scroll_text.pack(side='right', expand=True, fill='both')
        self.scroll_text.text.config(tabs=32)

    def new_file(self):
        self.scroll_text.delete('1.0', tk.END)
        self.root.title("Simple Text Editor")

    def open_file(self):
        file_path = filedialog.askopenfilename()
        if file_path:
            self.open_text_file(file_path)

    def open_folder(self):
        folder_path = filedialog.askdirectory()
        if folder_path:
            self.folder_path = folder_path  # Save the folder path
            self.load_file_hierarchy(folder_path)

    def load_file_hierarchy(self, folder):
        self.clear_tree()

        # Function to add files recursively
        def add_files(parent, directory):
            for item in os.listdir(directory):
                path = os.path.join(directory, item)
                if os.path.isdir(path):
                    folder_id = self.file_tree.insert(parent, 'end', text=item, open=False)
                    add_files(folder_id, path)
                else:
                    self.file_tree.insert(parent, 'end', text=item, open=False)

        add_files('', folder)

    def clear_tree(self):
        # Clear the tree
        self.file_tree.delete(*self.file_tree.get_children())

    def open_selected_file(self, event):
        selected_item = self.file_tree.focus()
        file_path = self.get_file_path(selected_item)
        if file_path:
            full_path = os.path.join(self.folder_path, file_path)  # Concatenate folder path with file path
            self.open_text_file(full_path)

    def get_file_path(self, item):
        # Recursive function to get the relative path of a file
        parent_id = self.file_tree.parent(item)
        if parent_id:
            parent_path = self.get_file_path(parent_id)
            return os.path.join(parent_path, self.file_tree.item(item, "text"))
        else:
            return self.file_tree.item(item, "text")

    def open_text_file(self, file_path):
        with open(file_path, "r") as file:
            content = file.read()
            self.scroll_text.delete("1.0", tk.END)
            self.scroll_text.insert(tk.END, content)
            self.root.title("Simple Text Editor - " + os.path.basename(file_path))

    def save_file(self):
        if not self.folder_path:
            return self.save_as_file()
        file_path = os.path.join(self.folder_path, self.root.title().split(" - ")[-1])
        with open(file_path, "w") as file:
            content = self.scroll_text.get("1.0", tk.END)
            file.write(content)

    def save_as_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt")
        if file_path:
            with open(file_path, "w") as file:
                content = self.scroll_text.get("1.0", tk.END)
                file.write(content)
            self.root.title("Simple Text Editor - " + os.path.basename(file_path))

    def undo(self):
        self.scroll_text.text.edit_undo()

    def redo(self):
        self.scroll_text.text.edit_redo()

    def toggle_line_numbers(self, show_line_numbers):
        if show_line_numbers:
            self.scroll_text.numberLines.pack(side="left", fill="y")
        else:
            self.scroll_text.numberLines.pack_forget()

    def update_tab_width(self, new_tab_width):
        self.scroll_text.text.config(tabs=new_tab_width)
        self.scroll_text.text.edit_modified(True)
