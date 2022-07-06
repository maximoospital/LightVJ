from PyQt5 import uic
from PyQt5.QtCore import Qt, QSettings
import resources.resources
from PyQt5.QtWidgets import (QDialog)


class About(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.setWindowFlags(self.windowFlags() & (~Qt.WindowContextHelpButtonHint))
        uic.loadUi('screens/about.ui', self)  # Load the .ui file
        self.show()  # Show the GUI
        self.settings = QSettings('Maximo Ospital', 'LightVJ')
        try:
            self.move(self.settings.value('help window position'))
        except:
            pass

    def closeEvent(self, event):
        self.settings.setValue('help window position', self.pos())