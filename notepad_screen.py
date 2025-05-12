import sys
from PyQt6.QtWidgets import (
    QApplication, QWidget, QTextEdit, QFileDialog,
    QVBoxLayout, QPushButton, QHBoxLayout, QFrame, QLabel
)
from PyQt6.QtGui import QIcon
from PyQt6.QtCore import QFileInfo, Qt


class NotepadScreen(QWidget):
    BOX_STYLE = """
        QFrame {
            border: 2px solid #007ACC;
            border-radius: 10px;
            background-color: #f0f0f0;
            padding: 15px;
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
        QTextEdit {
            background-color: white;
            font-size: 14px;
            border: 1px solid #ccc;
            border-radius: 5px;
        }
    """

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setObjectName("NotepadScreen")
        if parent:
            parent.resize(1000, 600)
        self.main_window = parent
        self.current_file = None

        main_layout = QVBoxLayout()
        self.setLayout(main_layout)

        # Back Button
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
        main_layout.addWidget(self.back_btn)

        # Action Buttons
        main_layout.addLayout(self.build_action_buttons())

        # Text Editor Box
        main_layout.addWidget(self.build_editor_box())

    def build_action_buttons(self):
        layout = QHBoxLayout()

        self.new_btn = QPushButton("New")
        self.open_btn = QPushButton("Open")
        self.save_btn = QPushButton("Save")
        self.saveas_btn = QPushButton("Save As")

        for btn, func in zip(
            [self.new_btn, self.open_btn, self.save_btn, self.saveas_btn],
            [self.new_file, self.open_file, self.save_file, self.save_file_as]
        ):
            btn.setCursor(Qt.CursorShape.PointingHandCursor)
            btn.clicked.connect(func)
            layout.addWidget(btn)

        return layout

    def build_editor_box(self):
        frame = QFrame()
        frame.setStyleSheet(self.BOX_STYLE)
        layout = QVBoxLayout(frame)

        label = QLabel("Notepad Editor")
        label.setStyleSheet("font-size: 20px; font-weight: bold; color: #007ACC; border: None")
        layout.addWidget(label)

        self.editor = QTextEdit()
        layout.addWidget(self.editor)

        return frame

    def new_file(self):
        self.editor.clear()
        self.current_file = None

    def open_file(self):
        path, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Text Files (*.txt);;All Files (*)")
        if path:
            with open(path, 'r', encoding='utf-8') as file:
                self.editor.setText(file.read())
                self.current_file = path

    def save_file(self):
        if self.current_file:
            with open(self.current_file, 'w', encoding='utf-8') as file:
                file.write(self.editor.toPlainText())
        else:
            self.save_file_as()

    def save_file_as(self):
        path, _ = QFileDialog.getSaveFileName(self, "Save File As", "", "Text Files (*.txt);;All Files (*)")
        if path:
            with open(path, 'w', encoding='utf-8') as file:
                file.write(self.editor.toPlainText())
                self.current_file = path


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = NotepadScreen()
    window.show()
    sys.exit(app.exec())
