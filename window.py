from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QWidget


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Geekscoders.com - PyQt6 Window")
        self.setWindowIcon(QIcon("qt.png"))
        self.setGeometry(500,200, 400,300)
        #self.setFixedHeight(200)
        #self.setFixedWidth(200)
        #self.setStyleSheet('background-color:red')

        stylesheet = (
            "background-color : red;"
        )

        self.setStyleSheet(stylesheet)