from PyQt6 import QtWidgets, QtCore, QtGui
from PyQt6.QtWidgets import QWidget

class MoneyScreen(QWidget):
    def __init__(self, main_window=None):  # Accept main_window if needed later
        super().__init__()

        self.setObjectName("MoneyScreen")
        self.resize(800, 600)

        self.title_label = QtWidgets.QLabel(self)
        self.title_label.setGeometry(QtCore.QRect(30, 10, 739, 78))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(20)
        self.title_label.setFont(font)
        self.title_label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.title_label.setObjectName("title_label")

        self.pushButton = QtWidgets.QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(350, 130, 93, 28))
        self.pushButton.setObjectName("pushButton")

        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(30, 90, 91, 21))
        self.label.setObjectName("label")

        self.lineEdit = QtWidgets.QLineEdit(self)
        self.lineEdit.setGeometry(QtCore.QRect(30, 130, 113, 22))
        self.lineEdit.setObjectName("lineEdit")

        self.label_2 = QtWidgets.QLabel(self)
        self.label_2.setGeometry(QtCore.QRect(660, 130, 121, 41))
        self.label_2.setObjectName("label_2")

        self.scrollArea = QtWidgets.QScrollArea(self)
        self.scrollArea.setGeometry(QtCore.QRect(590, 190, 181, 311))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")

        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 179, 309))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.label_3 = QtWidgets.QLabel(self)
        self.label_3.setGeometry(QtCore.QRect(190, 80, 91, 31))
        self.label_3.setObjectName("label_3")

        self.comboBox = QtWidgets.QComboBox(self)
        self.comboBox.setGeometry(QtCore.QRect(190, 130, 131, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.label_4 = QtWidgets.QLabel(self)
        self.label_4.setGeometry(QtCore.QRect(30, 295, 111, 31))
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(self)
        self.label_5.setGeometry(QtCore.QRect(30, 340, 55, 16))
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(self)
        self.label_6.setGeometry(QtCore.QRect(30, 380, 55, 16))
        self.label_6.setObjectName("label_6")

        self.label_7 = QtWidgets.QLabel(self)
        self.label_7.setGeometry(QtCore.QRect(10, 480, 61, 21))
        self.label_7.setObjectName("label_7")

        self.pushButton_2 = QtWidgets.QPushButton(self)
        self.pushButton_2.setGeometry(QtCore.QRect(70, 480, 93, 28))
        self.pushButton_2.setObjectName("pushButton_2")

        self.progressBar = QtWidgets.QProgressBar(self)
        self.progressBar.setGeometry(QtCore.QRect(200, 480, 118, 23))
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")

        self.label_8 = QtWidgets.QLabel(self)
        self.label_8.setGeometry(QtCore.QRect(110, 340, 55, 16))
        self.label_8.setObjectName("label_8")

        self.label_9 = QtWidgets.QLabel(self)
        self.label_9.setGeometry(QtCore.QRect(110, 380, 55, 16))
        self.label_9.setObjectName("label_9")

        self.retranslateUi()

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("MoneyScreen", "MoneyScreen"))
        self.title_label.setText(_translate("MoneyScreen", "Money Tracker"))
        self.pushButton.setText(_translate("MoneyScreen", "Submit"))
        self.label.setText(_translate("MoneyScreen", "Transaction:"))
        self.lineEdit.setPlaceholderText(_translate("MoneyScreen", "enter amount"))
        self.label_2.setText(_translate("MoneyScreen", "Transaction History"))
        self.label_3.setText(_translate("MoneyScreen", "Account Used:"))
        self.comboBox.setItemText(0, _translate("MoneyScreen", "SBI Bank Account"))
        self.comboBox.setItemText(1, _translate("MoneyScreen", "Wallet"))
        self.label_4.setText(_translate("MoneyScreen", "Total Money Left:"))
        self.label_5.setText(_translate("MoneyScreen", "Bank"))
        self.label_6.setText(_translate("MoneyScreen", "Wallet"))
        self.label_7.setText(_translate("MoneyScreen", "Target:"))
        self.pushButton_2.setText(_translate("MoneyScreen", "Change Target"))
        self.label_8.setText(_translate("MoneyScreen", ": 0"))
        self.label_9.setText(_translate("MoneyScreen", ": 0"))
