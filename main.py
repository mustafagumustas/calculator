from itertools import count
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

        self.x = ""
        self.y = ""

        # giving number buttons functionality
        for i in range(self.gridLayout_3.count()):
            item = self.gridLayout_3.itemAt(i).widget()
            if "_" in item.objectName():
                item.clicked.connect(self.number_clicked)
            elif item.text() in ["+", "-", "*", "÷", "="]:
                item.clicked.connect(self.calculation)
            else:
                item.clicked.connect(self.func)

    def number_clicked(self):
        # self.display = self.display + self.sender().text()
        self.x += self.sender().text()
        self.label.setText(self.x)

    def calculation(self):
        item = self.sender().text()
        if item == "+":
            self.y += str(self.x) + "+"
            self.x = ""
        elif item == "-":
            self.y += str(self.x) + "-"
            self.x = ""
        elif item == "÷":
            self.y = f"({self.y})/{self.x}"
            self.x = ""
        elif item == "*":
            if len(self.y) > 2:
                self.y = f"({self.y})*{self.x}"
            else:
                self.y += str(self.x) + "*"
            self.x = ""
        elif item == "=":
            try:
                self.y += self.x
                solution = eval(self.y)
                if len(str(solution)) > 14:
                    self.label.setText(str(round(solution, 12)))
                else:
                    self.label.setText(str(solution))
                self.x = ""
            except Exception as er:
                print(er)
        print(self.y)

    def func(self):
        item = self.sender().text()
        if item == "AC":
            self.y = ""
            self.x = ""
            self.label.setText("")
        elif item == "+/-":
            pass
        elif item == ",":
            self.x += "."
            self.label.setText(self.x)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainPage = MainPage()
    MainPage.show()
    sys.exit(app.exec_())
