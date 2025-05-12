import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton, QLabel,
    QCalendarWidget, QFrame
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont


class CalendarScreen(QWidget):
    BOX_STYLE = """
        QFrame {
            border: None;
        }
        QCalendarWidget QToolButton {
            color: #007ACC;
            font-size: 16px;
        }
        QCalendarWidget QAbstractItemView {
            selection-background-color: #007ACC;
            font-size: 14px;
        }
        QLabel {
            font-size: 16px;
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
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("CalendarScreen")
        if parent:
            parent.resize(1000, 600)
        self.main_window = parent

        layout = QVBoxLayout()
        self.setLayout(layout)

        # Back button
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
        layout.addWidget(self.back_btn)

        # Calendar box
        layout.addWidget(self.build_calendar_box())

    def build_calendar_box(self):
        frame = QFrame()
        frame.setStyleSheet(self.BOX_STYLE)
        inner_layout = QVBoxLayout(frame)

        heading = QLabel("Calendar")
        heading.setStyleSheet("font-size: 20px; font-weight: bold; color: #007ACC;")
        inner_layout.addWidget(heading)

        self.calendar = QCalendarWidget()
        self.calendar.setGridVisible(True)
        self.calendar.clicked.connect(self.show_selected_date)
        inner_layout.addWidget(self.calendar)

        self.selected_date_label = QLabel("Selected Date: None")
        self.selected_date_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        inner_layout.addWidget(self.selected_date_label)

        return frame

    def show_selected_date(self, date):
        self.selected_date_label.setText(f"Selected Date: {date.toString('dd MMMM yyyy')}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalendarScreen()
    window.show()
    sys.exit(app.exec())
