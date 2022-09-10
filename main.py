import numpy as np
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QSettings
import sys


class MainPage(QMainWindow):
    def __init__(self):
        super().__init__()
        loadUi("mainwindow.ui", self)
        self.setWindowTitle("Calculator")

        self.display = ""
        self.total = 0

        # giving number buttons functionality
        for i in range(self.gridLayout_3.count()):
            item = self.gridLayout_3.itemAt(i).widget()
            if "_" in item.objectName():
                item.clicked.connect(self.number_clicked)
            elif item.text() in ["+", "-", "X", "÷", "="]:
                item.clicked.connect(self.calculation)

    def number_clicked(self):
        self.display = self.display + self.sender().text()
        self.label.setText(self.display)

    def calculation(self):
        item = self.sender().objectName()
        print(item)
        if item == "plus":
            self.total += int(self.display)
            self.display = ""
            # self.total += int(self.display)
            # self.label.setText(str(self.total))
        elif item == "minus":
            pass
        elif item == "divide":
            pass
        elif item == "multiplication":
            pass
        elif item == "equal":
            self.total += int(self.display)
            self.label.setText(str(self.total))
            self.display = str(self.total)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainPage = MainPage()
    MainPage.show()
    sys.exit(app.exec_())
