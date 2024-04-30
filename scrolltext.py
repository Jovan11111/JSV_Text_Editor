import tkinter as tk
import highLighter
import textLineNumbers
from SVHihglighter import SVHighlighter
from CHighlighter import CHighLighter


class ScrollText(tk.Frame):
    def __init__(self, master, *args, **kwargs):
        self.file_path = ""

        tk.Frame.__init__(self, *args, **kwargs)
        self.text = tk.Text(self, bg='#2b2b2b', foreground="#d1dce8",
                            insertbackground='white',
                            selectbackground="blue", width=120, height=30)

        self.scrollbar = tk.Scrollbar(self, orient=tk.VERTICAL, command=self.text.yview)
        self.text.configure(yscrollcommand=self.scrollbar.set)

        self.numberLines = textLineNumbers.TextLineNumbers(self, width=40, bg='#313335')
        self.numberLines.attach(self.text)

        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.numberLines.pack(side=tk.LEFT, fill=tk.Y, padx=(5, 0))
        self.text.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.text.bind("<Key>", self.onPressDelay)
        self.text.bind("<Button-1>", self.numberLines.redraw)
        self.scrollbar.bind("<Button-1>", self.onScrollPress)
        self.text.bind("<MouseWheel>", self.onPressDelay)
        self.text.bind("<KeyRelease>", self.on_key_release)
        if self.file_path.split('.')[-1] == "sv":
            self.highlighter = SVHighlighter(self.text)
        else:
            self.highlighter = CHighLighter(self.text)

    def onScrollPress(self, *args):
        self.scrollbar.bind("<B1-Motion>", self.numberLines.redraw)

    def onScrollRelease(self, *args):
        self.scrollbar.unbind("<B1-Motion>", self.numberLines.redraw)

    def onPressDelay(self, *args):
        self.after(2, self.numberLines.redraw)

    def on_key_release(self, *args):
        self.highlighter.highlight()

    def set_highlighter(self, file_path):
        if file_path.split('.')[-1] == "sv":
            self.highlighter = SVHighlighter(self.text)
        else:
            self.highlighter = CHighLighter(self.text)

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
