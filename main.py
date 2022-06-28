from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout
from qt_material import apply_stylesheet
from qt_material import list_themes
app = QApplication([])
window = QWidget()
apply_stylesheet(app, theme='dark_red.xml')
layout = QVBoxLayout()
layout.addWidget(QPushButton('Top'))
layout.addWidget(QPushButton('Bottom'))
window.setLayout(layout)
window.show()
app.exec()
