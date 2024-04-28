import os
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk


class ScrollText(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.text = tk.Text(self, bg='#2b2b2b', foreground="#d1dce8",
                            insertbackground='white',
                            selectbackground="blue", width=120, height=30)

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

    def onScrollPress(self, *args):
        self.scrollbar.bind("<B1-Motion>", self.numberLines.redraw)

    def onScrollRelease(self, *args):
        self.scrollbar.unbind("<B1-Motion>", self.numberLines.redraw)

    def onPressDelay(self, *args):
        self.after(2, self.numberLines.redraw)

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


class TextLineNumbers(tk.Canvas):
    def __init__(self, *args, **kwargs):
        tk.Canvas.__init__(self, *args, **kwargs, highlightthickness=0)
        self.textwidget = None

    def attach(self, text_widget):
        self.textwidget = text_widget

    def redraw(self, *args):
        '''redraw line numbers'''
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


class TextEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("Simple Text Editor")

        # Save the folder path
        self.folder_path = ""

        self.preferences_window = None

        # Create menu bar
        self.menu_bar = tk.Menu(self.root)

        # File menu
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="New File", command=self.new_file)
        self.file_menu.add_command(label="Open File", command=self.open_file)
        self.file_menu.add_command(label="Open Folder", command=self.open_folder)
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_command(label="Save As", command=self.save_as_file)
        self.file_menu.add_command(label="Exit", command=self.root.quit)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

        # Edit menu
        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.edit_menu.add_command(label="Undo", command=self.undo)
        self.edit_menu.add_command(label="Redo", command=self.redo)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)

        # Preferences menu
        self.preferences_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.preferences_menu.add_command(label="General", command=self.open_preferences)
        self.menu_bar.add_cascade(label="Preferences", menu=self.preferences_menu)

        self.root.config(menu=self.menu_bar)

        # Create the text area and file tree
        self.splitter = ttk.PanedWindow(self.root, orient=tk.HORIZONTAL)
        self.scroll_text = ScrollText(self.splitter)
        self.scroll_text.text.config(tabs=32)
        self.file_tree = FileTree(self.splitter)
        self.splitter.add(self.file_tree)
        self.splitter.add(self.scroll_text)
        self.splitter.pack(expand=True, fill='both')

        self.file_tree.bind("<Double-1>", self.open_selected_file)

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
        self.file_tree.delete(*self.file_tree.get_children())

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

    def open_selected_file(self, event):
        item = self.file_tree.selection()[0]  # Get the selected item
        file_path = self.get_file_path(item)
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

    def open_preferences(self):
        self.preferences_window = tk.Toplevel(self.root)
        self.preferences_window.title("Preferences")
        self.preferences_window.geometry("600x400")

        # Add tab width setting
        label_tab_width = ttk.Label(self.preferences_window, text="Tab Width:")
        label_tab_width.grid(row=0, column=0, padx=10, pady=5, sticky='w')

        self.tab_width_var = tk.StringVar()
        self.tab_width_var.set("4")  # Default tab width

        entry_tab_width = ttk.Entry(self.preferences_window, textvariable=self.tab_width_var)
        entry_tab_width.grid(row=0, column=1, padx=10, pady=5, sticky='w')

        # Add line numbers checkbox
        self.line_numbers_var = tk.BooleanVar(value=False)  # Set the initial value
        checkbox_line_numbers = ttk.Checkbutton(self.preferences_window, text="Display Line Numbers",
                                                variable=self.line_numbers_var)
        checkbox_line_numbers.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky='w')

        # Add Apply button
        apply_button = ttk.Button(self.preferences_window, text="Apply", command=self.apply_preferences)
        apply_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky='e')

    def apply_preferences(self):
        try:
            # Update tab width in the text area
            tab_width = int(self.tab_width_var.get())
            self.scroll_text.text.config(tabs=tab_width * 8)

            # Check if line numbers should be displayed
            if self.line_numbers_var.get():
                self.scroll_text.numberLines.redraw()
            else:
                self.scroll_text.numberLines.pack_forget()

            # Close the preferences window
            self.preferences_window.destroy()
        except ValueError:
            error_window = tk.Toplevel(self.root)
            error_window.title("Error entering preferences")
            error_window.geometry("300x200")
            error_window.resizable(False, False)  # Make the window non-resizable
            error_window.grab_set()  # Make the window modal

            # Center the label vertically
            error_frame = ttk.Frame(error_window)
            error_frame.pack(fill='both', expand=True)

            label = ttk.Label(error_frame, text="Wrong value in preference field!", justify='center')
            label.pack(pady=5, fill='both', expand=True)


class FileTree(ttk.Treeview):
    def __init__(self, *args, **kwargs):
        ttk.Treeview.__init__(self, *args, **kwargs)


if __name__ == "__main__":
    root = tk.Tk()
    editor = TextEditor(root)
    root.mainloop()
