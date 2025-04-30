from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QWidget, QLabel, QPushButton, QLineEdit, QComboBox, QScrollArea, QProgressBar, QFormLayout
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
import sys

class MoneyScreen(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("MoneyScreen")
        self.main_window = parent
        if parent is not None:
            self.main_window.resize(1000, 600)

        self.title_label = QLabel("Money Tracker", self)
        self.title_label.setGeometry(QtCore.QRect(30, 10, 739, 78))
        self.title_label.setStyleSheet("font-size: 40px;")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label = QLabel("Transaction:", self)
        self.label.setGeometry(30, 90, 91, 21)

        self.lineEdit = QLineEdit(self)
        self.lineEdit.setGeometry(30, 130, 113, 22)
        self.lineEdit.setPlaceholderText("enter amount")

        self.comboBox = QComboBox(self)
        self.comboBox.setGeometry(190, 130, 131, 22)
        self.comboBox.addItems(["Bank Account", "Wallet"])

        self.label_3 = QLabel("Account Used:", self)
        self.label_3.setGeometry(190, 80, 91, 31)

        self.pushButton = QPushButton("Submit", self)
        self.pushButton.setGeometry(350, 130, 93, 28)

        self.label_2 = QLabel("Transaction History", self)
        self.label_2.setGeometry(660, 130, 121, 41)

        self.scrollArea = QScrollArea(self)
        self.scrollArea.setGeometry(590, 190, 181, 311)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 179, 309))
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        text_label = QLabel()
        text_label.setText("This is a long message.\n" * 50)  # Repeat text to demonstrate scrolling
        text_label.setWordWrap(True)
        self.scrollArea.setWidget(text_label)

        self.label_4 = QLabel("Total Money Left:", self)
        self.label_4.setGeometry(30, 295, 111, 31)

        self.label_5 = QLabel("Bank", self)
        self.label_5.setGeometry(30, 340, 55, 16)

        self.label_6 = QLabel("Wallet", self)
        self.label_6.setGeometry(30, 380, 55, 16)

        self.label_8 = QLabel(": 0", self)
        self.label_8.setGeometry(110, 340, 55, 16)

        self.label_9 = QLabel(": 0", self)
        self.label_9.setGeometry(110, 380, 55, 16)

        self.label_7 = QLabel("Target:", self)
        self.label_7.setGeometry(10, 480, 61, 21)

        self.pushButton_2 = QPushButton("Change Target", self)
        self.pushButton_2.setGeometry(70, 480, 93, 28)

        self.progressBar = QProgressBar(self)
        self.progressBar.setGeometry(200, 480, 118, 23)
        self.progressBar.setValue(24)

        form_layout = QFormLayout()
        form_layout.addRow("Transaction:", self.lineEdit)
        form_layout.addRow("Account Used:", self.comboBox)



if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv) #dont forget to initialize app
    window = MoneyScreen()
    window.show()
    sys.exit(app.exec())