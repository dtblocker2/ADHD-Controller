from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt6.QtCore import Qt
from random import randint

class DiceScreen(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        title = QLabel("Choose Size of Dice")
        title.setStyleSheet("font-size: 18px; color: black;")
        
        self.input_box = QLineEdit()
        self.input_box.setPlaceholderText("Enter number (e.g., 6)")
        self.input_box.setFixedWidth(200)

        self.roll_btn = QPushButton("Roll Dice")
        self.back_btn = QPushButton("Back to Home")
        
        self.label_result = QLabel("")
        self.label_result.setStyleSheet("font-size: 24px; color: #3333cc;")
        
        self.error_label = QLabel("")
        self.error_label.setStyleSheet("color: red;")

        self.roll_btn.clicked.connect(self.roll_dice)
        self.back_btn.clicked.connect(self.main_window.load_home_screen)

        widgets = [title, self.input_box, self.roll_btn, self.label_result, self.error_label, self.back_btn]
        for widget in widgets:
            self.layout.addWidget(widget, alignment=Qt.AlignmentFlag.AlignCenter)

    def roll_dice(self):
        try:
            sides = int(self.input_box.text().strip())
            if sides < 1:
                raise ValueError
            result = randint(1, sides)
            self.label_result.setText(f"Rolled: {result}")
            self.error_label.setText("")
        except ValueError:
            self.error_label.setText("Please enter a valid positive number!")
