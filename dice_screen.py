from PyQt6.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from PyQt6.QtCore import Qt
from random import randint

class DiceScreen(QWidget):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        # Title label styling
        title = QLabel("Choose Size of Dice")
        title.setStyleSheet("""
            font-size: 24px;
            color: #2d2d2d;
            font-weight: bold;
            margin-bottom: 20px;
        """)
        
        # Input box styling
        self.input_box = QLineEdit()
        self.input_box.setPlaceholderText("Enter number (e.g., 6)")
        self.input_box.setFixedWidth(250)
        self.input_box.setStyleSheet("""
            padding: 10px;
            font-size: 18px;
            border: 2px solid #ccc;
            border-radius: 10px;
            background-color: #f4f4f4;
        """)

        # Roll button styling
        self.roll_btn = QPushButton("Roll Dice")
        self.roll_btn.setStyleSheet("""
            background-color: #4CAF50;
            color: white;
            font-size: 18px;
            padding: 10px 20px;
            border-radius: 12px;
            border: none;
            margin-top: 20px;
        """)
        self.roll_btn.setCursor(Qt.CursorShape.PointingHandCursor)

        # Back button styling
        self.back_btn = QPushButton("Back to Home")
        self.back_btn.setStyleSheet("""
            background-color: #f44336;
            color: white;
            font-size: 18px;
            padding: 10px 20px;
            border-radius: 12px;
            border: none;
            margin-top: 10px;
        """)
        self.back_btn.setCursor(Qt.CursorShape.PointingHandCursor)

        # Result label styling
        self.label_result = QLabel("")
        self.label_result.setStyleSheet("""
            font-size: 24px;
            color: #3333cc;
            font-weight: bold;
            margin-top: 20px;
        """)

        # Error label styling
        self.error_label = QLabel("")
        self.error_label.setStyleSheet("""
            color: red;
            font-size: 16px;
            margin-top: 10px;
        """)

        # Connecting buttons to methods
        self.roll_btn.clicked.connect(self.roll_dice)
        self.back_btn.clicked.connect(self.main_window.load_home_screen)

        # Adding widgets to layout
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
