from PyQt5 import uic
from PyQt5.QtCore import Qt, QSettings
import resources.resources
from PyQt5.QtWidgets import (QDialog)


class Settings(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.setWindowFlags(self.windowFlags() & (~Qt.WindowContextHelpButtonHint))
        uic.loadUi('screens/settings.ui', self)  # Load the .ui file
        self.show()  # Show the GUI