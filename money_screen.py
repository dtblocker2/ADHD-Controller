from PyQt6 import QtWidgets
from PyQt6.QtWidgets import (
    QWidget, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QFrame, QPushButton
)
from PyQt6.QtCore import Qt
import sys

class MoneyScreen(QWidget):
    FONT_HEADING = "font-family: 'Montserrat'; font-size: 20px; border: None"
    FONT_LABEL = "font-family: 'Montserrat'; font-size: 16px; border: None"
    BOX_STYLE = """
        QFrame {
            border: 2px dotted #007ACC;
            border-radius: 8px;
            background-color: #f8f8f8;
        }
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("MoneyScreen")
        if parent:
            parent.resize(1000, 600)
        self.main_window = parent
        
        self.back_btn = QPushButton("Back to Home")
        self.back_btn.clicked.connect(self.main_window.load_home_screen)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.back_btn)
        main_layout.addWidget(self.build_greeting())
        main_layout.addLayout(self.build_input_section())
        self.setLayout(main_layout)

    def build_greeting(self):
        greet_label = QLabel(
            'Welcome back, <span style="color: #007ACC;">Dtblocker</span>', self
        )
        greet_label.setTextFormat(Qt.TextFormat.RichText)
        greet_label.setStyleSheet(self.FONT_HEADING)
        return greet_label

    def build_input_section(self):
        input_layout = QHBoxLayout()
        input_layout.addWidget(self.build_box("Create Budget", [
            ("Budget Name", "e.g. Groceries"),
            ("Amount", "₹690"),
        ]))
        input_layout.addWidget(self.build_box("Add New Expense", [
            ("Expense Name", "e.g. Coffee"),
            ("Amount", "₹69"),
        ]))
        return input_layout

    def build_box(self, title: str, fields: list[tuple[str, str]]) -> QFrame:
        frame = QFrame()
        frame.setStyleSheet(self.BOX_STYLE)
        frame.setFrameShape(QFrame.Shape.NoFrame)

        layout = QVBoxLayout(frame)

        title_label = QLabel(title)
        title_label.setTextFormat(Qt.TextFormat.RichText)
        title_label.setStyleSheet(self.FONT_HEADING)
        layout.addWidget(title_label)

        for label_text, placeholder in fields:
            label = QLabel(label_text)
            label.setTextFormat(Qt.TextFormat.RichText)
            label.setStyleSheet(self.FONT_LABEL)
            input_field = QLineEdit()
            input_field.setPlaceholderText(placeholder)
            layout.addWidget(label)
            layout.addWidget(input_field)

        return frame
    

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MoneyScreen()
    window.show()
    sys.exit(app.exec())
