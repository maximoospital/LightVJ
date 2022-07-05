import webbrowser
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import QDir, Qt, QUrl
import resources.resources
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import (QApplication, QFileDialog, QHBoxLayout, QLabel,
                             QPushButton, QSizePolicy, QSlider, QStyle, QVBoxLayout, QWidget, QDialog)
from qt_material import apply_stylesheet
from screens.about import About

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


class mainWidget(QWidget):

    def __init__(self, parent=None):
        super(mainWidget, self).__init__(parent)

        self.mediaPlayer = QMediaPlayer(None, QMediaPlayer.VideoSurface)

        videoWidget = QVideoWidget()

        openButton = QPushButton("Open...")
        openButton.clicked.connect(self.openFile)

        self.playButton = QPushButton()
        self.playButton.setEnabled(False)
        self.playButton.setIcon(self.style().standardIcon(QStyle.SP_MediaPlay))
        self.playButton.clicked.connect(self.play)

        self.positionSlider = QSlider(Qt.Horizontal)
        self.positionSlider.setRange(0, 0)
        self.positionSlider.sliderMoved.connect(self.setPosition)

        self.errorLabel = QLabel()
        self.errorLabel.setSizePolicy(QSizePolicy.Preferred,
                                      QSizePolicy.Maximum)

        controlLayout = QHBoxLayout()
        controlLayout.setContentsMargins(0, 0, 0, 0)
        controlLayout.addWidget(openButton)
        controlLayout.addWidget(self.playButton)
        controlLayout.addWidget(self.positionSlider)

        layout = QVBoxLayout()
        layout.addWidget(videoWidget)
        layout.addLayout(controlLayout)
        layout.addWidget(self.errorLabel)

        self.setLayout(layout)

        self.mediaPlayer.setVideoOutput(videoWidget)
        self.mediaPlayer.stateChanged.connect(self.mediaStateChanged)
        self.mediaPlayer.positionChanged.connect(self.positionChanged)
        self.mediaPlayer.durationChanged.connect(self.durationChanged)
        self.mediaPlayer.error.connect(self.handleError)

    def openFile(self):
        fileName, _ = QFileDialog.getOpenFileName(self, "Open Movie",
                                                  QDir.homePath())

        if fileName != '':
            self.mediaPlayer.setMedia(
                QMediaContent(QUrl.fromLocalFile(fileName)))
            self.playButton.setEnabled(True)

    def play(self):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.mediaPlayer.pause()
        else:
            self.mediaPlayer.play()

    def mediaStateChanged(self, state):
        if self.mediaPlayer.state() == QMediaPlayer.PlayingState:
            self.playButton.setIcon(
                self.style().standardIcon(QStyle.SP_MediaPause))
        else:
            self.playButton.setIcon(
                self.style().standardIcon(QStyle.SP_MediaPlay))

    def positionChanged(self, position):
        self.positionSlider.setValue(position)

    def durationChanged(self, duration):
        self.positionSlider.setRange(0, duration)

    def setPosition(self, position):
        self.mediaPlayer.setPosition(position)

    def handleError(self):
        self.playButton.setEnabled(False)
        self.errorLabel.setText("Error: " + self.mediaPlayer.errorString())

    def setMenuBar(self):
        pass


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    apply_stylesheet(app, theme='dark_red.xml')

    main = MainWindow()
    main.show()

    sys.exit(app.exec_())
