import tkinter as tk
from tkinter import ttk


class Preferences:
    def __init__(self, master, text_editor):
        self.master = master
        self.text_editor = text_editor

    def open_preferences(self):
        self.preferences_window = tk.Toplevel(self.master)
        self.preferences_window.title("Preferences")
        self.preferences_window.geometry("300x200")

        # Add tab width setting
        label_tab_width = ttk.Label(self.preferences_window, text="Tab Width:")
        label_tab_width.grid(row=0, column=0, padx=10, pady=5, sticky='w')

        self.tab_width_var = tk.StringVar()
        self.tab_width_var.set(str(self.text_editor.scroll_text.text['tabs'][0]))  # Set current tab width

        entry_tab_width = ttk.Entry(self.preferences_window, textvariable=self.tab_width_var)
        entry_tab_width.grid(row=0, column=1, padx=10, pady=5, sticky='w')

        # Add line numbers checkbox
        self.line_numbers_var = tk.BooleanVar(value=self.text_editor.scroll_text.numberLines.winfo_ismapped())
        checkbox_line_numbers = ttk.Checkbutton(self.preferences_window, text="Display Line Numbers",
                                                variable=self.line_numbers_var,
                                                command=self.toggle_line_numbers)
        checkbox_line_numbers.grid(row=1, column=0, columnspan=2, padx=10, pady=5, sticky='w')

        # Add Apply button
        apply_button = ttk.Button(self.preferences_window, text="Apply", command=self.apply_preferences)
        apply_button.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky='e')

    def toggle_line_numbers(self):
        self.text_editor.toggle_line_numbers(self.line_numbers_var.get())

    def apply_preferences(self):
        try:
            # Update tab width in the text area
            tab_width = int(self.tab_width_var.get())
            self.text_editor.update_tab_width(tab_width)

            # Close the preferences window
            self.preferences_window.destroy()
        except ValueError:
            error_window = tk.Toplevel(self.master)
            error_window.title("Error entering preferences")
            error_window.geometry("300x200")
            error_window.resizable(False, False)  # Make the window non-resizable
            error_window.grab_set()  # Make the window modal

            # Center the label vertically
            error_frame = ttk.Frame(error_window)
            error_frame.pack(fill='both', expand=True)

            label = ttk.Label(error_frame, text="Wrong value in preference field!", justify='center')
            label.pack(pady=5, fill='both', expand=True)
