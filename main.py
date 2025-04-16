from PyQt6.QtWidgets import QWidget, QApplication, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
from PyQt6.QtGui import QIcon, QCursor, QColor
import sys
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtQml import QQmlApplicationEngine
class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(500,500)
        self.setWindowTitle("ADHD Controller")
        self.setWindowIcon(QIcon('app_icon.ico'))

        buttons_container = QHBoxLayout() #initialize box layout
        buttons_container.setContentsMargins(20, 20, 20, 20)  # Padding inside the container
        buttons_container.setSpacing(20) #padding between buttons

        #add buttons to layout
        buttons_container.addWidget(self.options_button("Notepad","notepad_icon.png"))
        buttons_container.addWidget(self.options_button("Calendar","calendar_icon.png"))
        buttons_container.addWidget(self.options_button("Money","money_icon.png"))
        buttons_container.addWidget(self.options_button("Account","account_icon.png"))

        self.setLayout(buttons_container) # setting layout
        
    def options_button(self, text,icon="blank.png"):
        button_n = QPushButton("", self)
        button_n.setIcon(QIcon(icon))
        button_n.setIconSize(QSize(100,100))
        button_n.setFixedSize(100, 100)
        black = QColor(0, 0, 0)
        white = QColor(255, 255, 255)
        button_n.setStyleSheet(f"""
            QPushButton {{
                background-color: {white.name()};
                color: {black.name()};
                border: 2px solid {white.name()};
                font-size: 16px;
            }}
        """)
        return button_n

app = QApplication(sys.argv)
app.setWindowIcon(QIcon("app_icon.ico"))
window = Window()
window.show()
sys.exit(app.exec())