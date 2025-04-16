from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
from PyQt6.QtGui import QColor
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(300, 200)

        button = QPushButton("Click Me", self)
        button.setGeometry(80, 70, 140, 50)

        # Set black background and white text using QColor
        black = QColor(0, 0, 0)
        white = QColor(255, 255, 255)
        button.setStyleSheet(f"""
            QPushButton {{
                background-color: {black.name()};
                color: {white.name()};
                border: 2px solid {white.name()};
                font-size: 16px;
            }}
        """)

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
