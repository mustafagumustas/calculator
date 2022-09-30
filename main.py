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
        # when user clicks on nubmer buttons, this function will detect which
        # one it is and then adds to the label
        self.x += self.sender().text()
        self.change_label(self.x)

    def calculation(self):
        item = self.sender().text()
        if item == "+":
            self.y += str(self.x) + "+"
            self.x = ""
        elif item == "-":
            self.y += str(self.x) + "-"
            self.x = ""
        elif item == "÷":
            if len(self.y) > 2:
                self.y = f"({self.y})/{self.x}"
            else:
                self.y += str(self.x) + "/"
            self.x = ""
        elif item == "*":
            if len(self.y) > 2:
                self.y = f"({self.y})*{self.x}"
            else:
                self.y += str(self.x) + "*"
            self.x = ""
        elif item == "=":
            try:
                # ERROR WHEN THERE IS NO Y VALUE PROGRAMME CRASHES
                self.y += self.x
                solution = eval(self.y)
                self.change_label(solution)
                self.x = ""
            except Exception as er:
                print(er)
        print(self.y)

    def change_label(self, value):
        # changing the label based on what kind of number it is
        if len(str(value)) > 14:
            value = round(value, 12)
        if value != "":
            if float(value).is_integer():
                value = int(value)
            else:
                value = float(value)
        self.label.setText(str(value))

    def func(self):
        item = self.sender().text()
        if item == "AC":
            if self.y != "":
                self.y = ""
            if self.x != "":
                self.x = ""
            self.change_label("")
        elif item == "+/-":
            number = self.label.text()
            if float(number) > 0:
                self.x = f"-{number}"
                self.change_label(self.x)
            elif "-" in number:
                self.x = number.split("-")[1]
                self.change_label(self.x)
            else:
                pass
        elif item == ",":
            self.x += "."
            self.label.setText(self.x)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainPage = MainPage()
    MainPage.show()
    sys.exit(app.exec_())
