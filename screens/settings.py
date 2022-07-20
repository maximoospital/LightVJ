from PyQt5.QtCore import Qt, QSettings
from PyQt5 import uic
from qt_material import apply_stylesheet
from PyQt5.QtWidgets import (QDialog)

class Settings(QDialog):
    def apply(self):
        self.settings.setValue('theme', self.theme.currentText())
        apply_stylesheet(self, theme=self.settings.value('theme'))

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.setWindowFlags(self.windowFlags() & (~Qt.WindowContextHelpButtonHint))
        uic.loadUi('screens/settings.ui', self)  # Load the .ui file
        self.settings = QSettings('Maximo Ospital', 'LightVJ')
        apply_stylesheet(self, theme=self.settings.value('theme'))
        self.applybutton.clicked.connect(self.apply)
        try:
            self.move(self.settings.value('help window position'))
        except:
            pass
        self.show()  # Show the GUI

    def closeEvent(self, event):
        self.settings.setValue('help window position', self.pos())
