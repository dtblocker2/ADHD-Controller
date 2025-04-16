from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QHBoxLayout
import sys

class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setFixedSize(500, 100)

        layout = QHBoxLayout()
        layout.setContentsMargins(20, 20, 20, 20)  # Padding inside the container
        layout.setSpacing(20)  # Space between buttons

        for i in range(4):
            button = QPushButton(f"Button {i+1}")
            layout.addWidget(button)

        self.setLayout(layout)

app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
