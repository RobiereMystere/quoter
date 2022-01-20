import sys

from PyQt6.QtWidgets import QApplication

from pdf_manager import PdfManager
from window import Window

if __name__ == '__main__':
    """app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())"""
    pdf_manager=PdfManager()
