from PyQt6.QtWidgets import QPushButton
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QSize
import os

def create_icon_button(icon_path):
    button = QPushButton()
    if os.path.exists(icon_path):
        button.setIcon(QIcon(icon_path))
    else:
        print(f"Warning: Icon '{icon_path}' not found.")
    button.setIconSize(QSize(100, 100))
    button.setFixedSize(100, 100)
    button.setStyleSheet("""
        QPushButton {
            background-color: white;
            border: none;
        }
    """)
    return button
