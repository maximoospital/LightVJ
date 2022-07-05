import webbrowser
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtWidgets import (QApplication)
from qt_material import apply_stylesheet
from screens.about import About
from screens.MainWidget import mainWidget

# Main window
class MainWindow(QtWidgets.QMainWindow):
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
        settings_menu = bar.addMenu('Settings')
        # adding actions to edit menu
        gen_action = QtWidgets.QAction('General Settings', self)
        output_action = QtWidgets.QAction('Output Settings', self)
        link_action = QtWidgets.QAction('Ableton Link Settings', self)
        spout_action = QtWidgets.QAction('Spout Settings', self)
        settings_menu.addAction(gen_action)
        settings_menu.addAction(output_action)
        settings_menu.addAction(link_action)
        settings_menu.addAction(spout_action)
        # Edit menu
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
        gh_action.triggered.connect(lambda: webbrowser.open('https://github.com/maximoospital'))
        about_action.triggered.connect(self.about_clicked)

    def about_clicked(self, s):
        dlg = About(self)
        button = dlg.exec()

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("LightVJ")
        self.setWindowIcon(QtGui.QIcon('resources\lvjicon.png'))
        self.mainWidget = mainWidget(parent=self)
        self.setCentralWidget(self.mainWidget)
        self._createMenuBar()
        self.resize(640, 480)


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_red.xml')

    main = MainWindow()
    main.show()

    sys.exit(app.exec_())
