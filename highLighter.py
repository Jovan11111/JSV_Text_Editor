from abc import ABC, abstractmethod


class Highlighter(ABC):
    def __init__(self, text_widget):
        self.text_widget = text_widget

    @abstractmethod
    def highlight(self):
        pass
