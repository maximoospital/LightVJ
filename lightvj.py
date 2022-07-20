import webbrowser

from PyQt5 import QtGui, QtWidgets, uic
from PyQt5.QtCore import Qt, QSettings, pyqtSignal, pyqtSlot
from PyQt5.QtWidgets import (QApplication, QDialog)
from qt_material import apply_stylesheet

from screens.MainWidget import mainWidget
from screens.about import About

QtWidgets.QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)

# Main window
class MainWindow(QtWidgets.QMainWindow):

    # menu bar creation
    def _createMenuBar(self):
        # filling up a menu bar
        bar = self.menuBar()
        # File menu
        file_menu = bar.addMenu('File')
        # adding actions to file menu
        open_action = QtWidgets.QAction('Open', self)
        save_action = QtWidgets.QAction('Save', self)
        saveas_action = QtWidgets.QAction('Save as', self)
        close_action = QtWidgets.QAction('Quit', self)
        file_menu.addAction(open_action)
        file_menu.addAction(save_action)
        file_menu.addAction(saveas_action)
        file_menu.addAction(close_action)
        # Edit menu
        edit_menu = bar.addMenu('Edit')
        # adding actions to edit menu
        set_action = QtWidgets.QAction('Settings', self)
        edit_menu.addAction(set_action)
        # Help menu
        help_menu = bar.addMenu('Help')
        # adding actions to edit menu
        update_action = QtWidgets.QAction('Check for Updates', self)
        guide_action = QtWidgets.QAction('Guide', self)
        gh_action = QtWidgets.QAction('My Github', self)
        about_action = QtWidgets.QAction('About LightVJ', self)
        help_menu.addAction(update_action)
        help_menu.addAction(guide_action)
        help_menu.addAction(gh_action)
        help_menu.addAction(about_action)

        # use `connect` method to bind signals to desired behavior
        close_action.triggered.connect(self.close)
        set_action.triggered.connect(self.set_clicked)
        gh_action.triggered.connect(lambda: webbrowser.open('https://github.com/maximoospital'))
        about_action.triggered.connect(self.about_clicked)

    # settings button functionality
    def set_clicked(self, s):
        button = Settings().exec_()

    # about button functionality
    def about_clicked(self, s):
        dlg = About()
        button = dlg.exec()

    def __init__(self, parent=None):
        super().__init__(parent)
        # title, icon and size definition
        self.setWindowTitle("LightVJ")
        self.setWindowIcon(QtGui.QIcon('resources/lvjicon.png'))
        self.mainWidget = mainWidget(parent=self)
        self.setCentralWidget(self.mainWidget)
        self._createMenuBar()
        self.resize(640, 480)
        self.settings = QSettings('Maximo Ospital', 'LightVJ')
        # print(self.settings.fileName())
        try:
            self.resize(self.settings.value('window size'))
            self.move(self.settings.value('window position'))
        except:
            pass

    @pyqtSlot()
    def CambioDeOpciones(self):
        configuracion = QSettings('Maximo Ospital', 'LightVJ')
        if configuracion.contains("theme"):
            apply_stylesheet(app, theme=configuracion.value('theme'))
        else:
            apply_stylesheet(app, theme=configuracion.value('dark_red.xml'))

    def closeEvent(self, event):
        self.settings.setValue('window size', self.size())
        self.settings.setValue('window position', self.pos())


class Settings(QDialog):
    settingsSignal = pyqtSignal()

    def apply(self):
        self.settings.setValue('theme', self.theme.currentText())
        apply_stylesheet(app, theme=self.settings.value('theme'))
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


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    # apply material style and show window
    config = QSettings('Maximo Ospital', 'LightVJ')
    if config.contains("theme"):
        apply_stylesheet(app, theme=config.value('theme'))
    else:
        apply_stylesheet(app, theme=config.value('dark_red.xml'))
    main = MainWindow()
    main.show()

    sys.exit(app.exec_())
