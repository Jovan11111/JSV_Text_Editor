import tkinter as tk

class ResizableFramesApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Resizable Frames Example")

        # Set window size
        self.root.geometry("600x800")

        # Create the main frame for holding everything
        self.main_frame = tk.Frame(root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Create a PanedWindow for the left (red) and right (blue and green) sides
        self.paned_window = tk.PanedWindow(self.main_frame, orient=tk.HORIZONTAL)

        # Create the left red frame with initial width of 100px
        self.red_frame = tk.Frame(self.paned_window, bg='red', width=100)
        self.red_frame.pack_propagate(False)  # Prevent frame from shrinking to fit contents
        self.red_frame.grid(row=0, column=0, sticky="nsew")

        # Create a PanedWindow for the right side
        self.paned_window_right = tk.PanedWindow(self.paned_window, orient=tk.VERTICAL)

        # Create frames for the right side
        self.blue_frame = tk.Frame(self.paned_window_right, bg='blue')
        self.green_frame = tk.Frame(self.paned_window_right, bg='green')

        # Add frames to PanedWindow on the right
        self.paned_window_right.add(self.blue_frame)
        self.paned_window_right.add(self.green_frame)

        # Add red frame and right side PanedWindow to the main PanedWindow
        self.paned_window.add(self.red_frame)
        self.paned_window.add(self.paned_window_right)

        # Pack the main PanedWindow
        self.paned_window.pack(fill=tk.BOTH, expand=True)

        # Configure resizing behavior
        self.main_frame.grid_rowconfigure(0, weight=1)
        self.main_frame.grid_columnconfigure(0, weight=1)

        # Example of configuring weight for resizing
        self.paned_window.paneconfigure(self.red_frame, minsize=100)  # Minimum size for red frame

        self.paned_window_right.paneconfigure(self.blue_frame, minsize=30)
        self.paned_window_right.paneconfigure(self.green_frame, minsize=30)

if __name__ == "__main__":
    root = tk.Tk()
    app = ResizableFramesApp(root)
    root.mainloop()
