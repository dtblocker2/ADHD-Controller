from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QVBoxLayout
from PyQt6.QtCore import Qt

class PlaceholderScreen(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        label = QLabel("Feature Coming Soon!")
        label.setStyleSheet("font-size: 18px; color: gray;")
        back_btn = QPushButton("Back to Home")
        back_btn.clicked.connect(self.main_window.load_home_screen)

        self.layout.addWidget(label, alignment=Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(back_btn, alignment=Qt.AlignmentFlag.AlignCenter)
