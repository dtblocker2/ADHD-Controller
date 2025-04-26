from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout
from PyQt6.QtGui import QIcon
import sys
from home_screen import HomeScreen

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ADHD Controller")
        self.setGeometry(100,100,500,500)
        self.setWindowIcon(QIcon('app_icon.ico'))
        self.setStyleSheet("background-color: #ffffff; font-family: Arial; font-size: 14px;")

        # Main Layout
        self.main_layout = QVBoxLayout()
        self.main_layout.setContentsMargins(20, 20, 20, 20)
        self.main_layout.setSpacing(20)
        self.setLayout(self.main_layout)

        # Load home screen initially
        self.load_home_screen()

    def load_home_screen(self):
        """Load the home screen."""
        self.clear_layout()
        home_screen = HomeScreen(self)
        self.main_layout.addWidget(home_screen)

    def clear_layout(self):
        """Remove all widgets from the main layout."""
        while self.main_layout.count():
            child = self.main_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('app_icon.ico'))
    window = Window()
    window.show()
    sys.exit(app.exec())
