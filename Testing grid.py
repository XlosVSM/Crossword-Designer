import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLineEdit
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        # set the window title
        self.setWindowTitle('Testing making a grid')

        # Testing a square
        self.textInputTest = QLineEdit(self)
        self.textInputTest.setMaxLength(1)
        self.textInputTest.setFont(QFont('Arial', 20))
        self.textInputTest.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.textInputTest.resize(30, 30)
        self.textInputTest.textChanged.connect(self.capitaliseLetters)

        # show the window
        self.showMaximized()
    
    def capitaliseLetters(self, txt):
        capitalisedLetter = txt.title()
        self.textInputTest.setText(capitalisedLetter)

if __name__ == '__main__':
    app = QApplication(sys.argv)

    # create the main window
    window = MainWindow()

    # start the event loop
    sys.exit(app.exec())