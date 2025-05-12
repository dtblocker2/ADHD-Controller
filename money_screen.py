from PyQt6 import QtWidgets
from PyQt6.QtWidgets import (
    QWidget, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout, QFrame, QPushButton, QComboBox, QProgressBar
)
from PyQt6.QtCore import Qt
import sys
from math import floor

class MoneyScreen(QWidget):
    FONT_HEADING = "font-family: 'Montserrat'; font-size: 20px; border: None"
    FONT_LABEL = "font-family: 'Montserrat'; font-size: 16px; border: None"
    BOX_STYLE = """
        QFrame {
            border: 2px solid #007ACC;
            border-radius: 10px;
            background-color: #f0f0f0;
            padding: 15px;
        }
        QLabel {
            color: #333;
        }
        QPushButton {
            background-color: #007ACC;
            color: white;
            border-radius: 5px;
            padding: 10px;
            font-size: 16px;
        }
        QPushButton:hover {
            background-color: #005B8D;
        }
        QProgressBar {
            border: 2px solid #007ACC;
            border-radius: 5px;
            height: 18px;
        }
        QProgressBar::chunk {
            background-color: #007ACC;
            border-radius: 5px;
        }
        QComboBox {
            padding: 8px;
            font-size: 16px;
            background-color: #f8f8f8;
            border: 1px solid #007ACC;
            border-radius: 5px;
        }
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("MoneyScreen")
        if parent:
            parent.resize(1000, 600)
        self.main_window = parent
        
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
        self.back_btn.clicked.connect(self.main_window.load_home_screen)

        main_layout = QVBoxLayout()
        main_layout.addWidget(self.back_btn)
        main_layout.addWidget(self.build_greeting())
        main_layout.addLayout(self.build_input_section())
        main_layout.addLayout(self.build_existing_budgets())
        main_layout.addLayout(self.build_recent_expenses())
        self.setLayout(main_layout)

    def build_greeting(self):
        greet_label = QLabel(
            'Welcome back, <span style="color: #007ACC;">Dtblocker02</span>', self
        )
        greet_label.setTextFormat(Qt.TextFormat.RichText)
        greet_label.setStyleSheet(self.FONT_HEADING)
        return greet_label
    
    def build_existing_budgets(self):
        layout = QVBoxLayout()

        heading = QLabel("Existing Budgets")
        heading.setTextFormat(Qt.TextFormat.RichText)
        heading.setStyleSheet(self.FONT_HEADING)
        layout.addWidget(heading)

        self.budget_area = QHBoxLayout()
        self.budget_area.addWidget(self.budget_box_layout(10, 20, "Alpha"))

        layout.addLayout(self.budget_area)
        return layout
    
    def build_recent_expenses(self):
        layout = QVBoxLayout()

        heading = QLabel("Recent Expenses")
        heading.setTextFormat(Qt.TextFormat.RichText)
        heading.setStyleSheet(self.FONT_HEADING)
        layout.addWidget(heading)
        return layout

    def build_input_section(self):
        input_layout = QHBoxLayout()
        input_layout.addWidget(self.build_box("Create Budget", [
            ("Budget Name", "e.g. Groceries"),
            ("Amount", "₹690"),
        ], "Create Budget"))
        input_layout.addWidget(self.build_box2("Add New Expense", [
            ("Expense Name", "e.g. Coffee"),
            ("Amount", "₹69"),
        ], "Add Expense"))
        return input_layout

    def build_box(self, title: str, fields: list[tuple[str, str]], button: str) -> QFrame:
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
        layout.addWidget(QPushButton(button))

        return frame
    
    def build_box2(self, title: str, fields: list[tuple[str, str]], button: str) -> QFrame:
        frame = QFrame()
        frame.setStyleSheet(self.BOX_STYLE)
        frame.setFrameShape(QFrame.Shape.NoFrame)

        layout = QVBoxLayout(frame)
        layout2 = QHBoxLayout()

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
            layout2.addWidget(label)
            layout2.addWidget(input_field)
        layout.addLayout(layout2)

        label = QLabel("Budget Category")
        label.setTextFormat(Qt.TextFormat.RichText)
        label.setStyleSheet(self.FONT_LABEL)
        input_field = QComboBox()
        input_field.setStyleSheet("Border: Solid #007ACC")
        input_field.addItems(["Groceries", "Entertainment", "Transport", "Utilities"])

        layout.addWidget(label)
        layout.addWidget(input_field)

        layout.addWidget(QPushButton(button))

        return frame
    
    def budget_box_layout(self, spent, limit, budget_name):
        frame = QFrame()
        frame.setFixedWidth(260)

        BOX_STYLE = """
            QFrame {
                border: 2px solid #007ACC;
                background-color: #f8f8f8;
                border-radius: 10px;
                padding: 15px;
            }
            QLabel {
                font-size: 16px;
                color: #333;
                border: None;
            }
            QPushButton {
                background-color: #007ACC;
                color: white;
                border-radius: 5px;
                padding: 10px;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #005B8D;
            }
        """

        frame.setStyleSheet(BOX_STYLE)

        layout = QVBoxLayout(frame)

        # Line 1: Heading + limit_2 (total limit)
        heading_layout = QHBoxLayout()
        heading = QLabel(budget_name)
        heading.setStyleSheet("font-weight: bold;")
        limit_2 = QLabel(f"₹{limit:.2f}")
        limit_2.setStyleSheet("font-weight: bold; color: #007ACC;")
        heading_layout.addWidget(heading, alignment=Qt.AlignmentFlag.AlignLeft)
        heading_layout.addWidget(limit_2, alignment=Qt.AlignmentFlag.AlignRight)
        layout.addLayout(heading_layout)

        # Progress bar
        spent_percentage = floor((spent / limit) * 100)
        spent_line = QProgressBar()
        spent_line.setValue(spent_percentage)
        spent_line.setFixedWidth(300)
        spent_line.setFormat("")
        layout.addWidget(spent_line, alignment=Qt.AlignmentFlag.AlignCenter)

        # Line 2: Spent + Limit (under progress bar)
        values_layout = QHBoxLayout()
        spent_label = QLabel(f"₹{spent:.2f}")
        spent_label.setStyleSheet("color: #007ACC;")
        limit_label = QLabel(f"₹{limit:.2f}")
        limit_label.setStyleSheet("color: #333;")
        values_layout.addWidget(spent_label, alignment=Qt.AlignmentFlag.AlignLeft)
        values_layout.addWidget(limit_label, alignment=Qt.AlignmentFlag.AlignRight)
        layout.addLayout(values_layout)

        # Centered button
        details_btn = QPushButton("Details")
        layout.addWidget(details_btn, alignment=Qt.AlignmentFlag.AlignCenter)

        return frame

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MoneyScreen()
    window.show()
    sys.exit(app.exec())
