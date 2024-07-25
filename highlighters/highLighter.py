"""
==================================================================
Project Name:    JSV_Text_Editor
File Name:       highLighter.py
Description:     

Author:          Jovan11111
Creation Date:   13.7.2024
Version:         1.0

==================================================================
"""

from abc import ABC, abstractmethod


class Highlighter(ABC):
    def __init__(self, text_widget):
        self.text_widget = text_widget

    @abstractmethod
    def highlight(self):
        pass
