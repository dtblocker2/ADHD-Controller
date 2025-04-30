from PyQt6.QtWidgets import QWidget, QPushButton, QVBoxLayout
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QSize, Qt

from dice_screen import DiceScreen
from placeholder_screen import PlaceholderScreen
from money_screen import MoneyScreen

from utils import create_icon_button
import os

#gives out base directory of the file so that any python interpretor can file assets file with absolute location
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

class HomeScreen(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        feature_icon_directory = os.path.join(BASE_DIR, "assets/")
        features = [
            ("Dice", feature_icon_directory+"dice_icon.png", self.load_dice_screen),
            ("Account", feature_icon_directory+"account_icon.png", self.load_placeholder_screen),
            ("Money", feature_icon_directory+"money_icon.png", self.load_money_screen),
            ("Calendar", feature_icon_directory+"calendar_icon.png", self.load_placeholder_screen),
            ("Notepad", feature_icon_directory+"notepad_icon.png", self.load_placeholder_screen)
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
    
    def load_money_screen(self):
        self.main_window.clear_layout()
        money_screen = MoneyScreen(self.main_window)
        self.main_window.main_layout.addWidget(money_screen)
