from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QSize, Qt
from dice_screen import DiceScreen
from placeholder_screen import PlaceholderScreen
from utils import create_icon_button

class HomeScreen(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        features = [
            ("Dice", "assets/dice_icon.png", self.load_dice_screen),
            ("Account", "assets/account_icon.png", self.load_placeholder_screen),
            ("Money", "assets/money_icon.png", self.load_placeholder_screen),
            ("Calendar", "assets/calendar_icon.png", self.load_placeholder_screen),
            ("Notepad", "assets/notepad_icon.png", self.load_placeholder_screen)
        ]

        for text, icon_path, action in features:
            btn = create_icon_button(icon_path)
            btn.clicked.connect(action)
            self.layout.addWidget(btn, alignment=Qt.AlignmentFlag.AlignCenter)

    def load_dice_screen(self):
        self.main_window.clear_layout()
        dice_screen = DiceScreen(self.main_window)
        self.main_window.main_layout.addWidget(dice_screen)

    def load_placeholder_screen(self):
        self.main_window.clear_layout()
        placeholder = PlaceholderScreen(self.main_window)
        self.main_window.main_layout.addWidget(placeholder)
