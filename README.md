# JSV Text Editor

JSV Text Editor is a powerful and versatile text editor built with Tkinter, designed to enhance your coding experience with a variety of features and shortcuts. It supports multiple programming languages, provides syntax highlighting, and offers advanced functionalities such as autocompletion for the UVM framework in SystemVerilog.

**Note:** This program is designed to be used on Linux only.

## Features

### File Operations
- **Open File:** Quickly open any file with a simple shortcut.
- **Open Folder:** Browse and open folders to easily navigate your project directory.
- **New File:** Create a new file with ease using a dedicated shortcut.

### Integrated File Tree
- **File Tree:** Navigate through your project directory with a built-in file tree for efficient file management.

### Built-in Terminal
- **Terminal:** Execute commands and scripts directly within the text editor using the integrated terminal.

### Text Editing
- **Language Recognition:** Automatically detects the programming language based on the file extension (e.g., `.cpp` for C++).
- **Syntax Highlighting:** Supports syntax highlighting for HTML, JavaScript, Java, Python, SystemVerilog, C, and C++.
- **Autocompletion:** Provides autocompletion for UVM framework classes and macros in SystemVerilog.

### Keyboard Shortcuts
- **Copy (Ctrl+C):** Copies the current line if no text is selected; copies selected text if something is selected.
- **Cut (Ctrl+X):** Cuts the current line if no text is selected; cuts selected text if something is selected.
- **Paste (Ctrl+V):** Pastes the copied or cut text.
- **Find and Replace (Ctrl+F):** Opens a find and replace dialog.
- **Delete Line (Ctrl+D):** Deletes the entire line where the cursor is located.
- **Toggle Comment (Alt+C):** 
  - Comments/uncomments the current line if no text is selected.
  - Wraps the selected text with block comment delimiters if text is selected.

## Installation

To use JSV Text Editor, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/Jovan11111/JSV_Text_Editor
    ```
2. Navigate to the project directory:
    ```bash
    cd JSV_Text_Editor
    ```
3. Create a virtual environment (optional but recommended):
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
5. Run the application:
    ```bash
    python main.py
    ```

## Usage

Once the application is running, you can start using JSV Text Editor to create and edit your code. Use the provided shortcuts for efficient coding and file management.

## Contributing

I welcome contributions to improve JSV Text Editor.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Tkinter: The Python library for creating graphical user interfaces.

## Contact

For any questions or feedback, please contact me.

---
