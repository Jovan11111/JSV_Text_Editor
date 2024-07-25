"""
==================================================================
Project Name:    JSV_Text_Editor
File Name:       main.py
Description:     A custom text editor with features tailored for UVM code, 
                 including syntax highlighting, autocompletion, auto-indentation,
                 line numbering, commenting, and find/replace functionality.

Author:          Jovan11111
Creation Date:   13.7.2024
Version:         1.0

==================================================================
"""

import tkinter as tk
from components.texteditor import TextEditor

if __name__ == "__main__":
    app = TextEditor()
    app.mainloop()
