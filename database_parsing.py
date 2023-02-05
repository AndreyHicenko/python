import sqlite3
import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QTableWidgetItem


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("UI.ui", self)
        self.con = sqlite3.connect("datebase.db")
        self.pushButton.clicked.connect(self.update_result)
        self.pushButton_2.clicked.connect(self.full_result)
        cur = self.con.cursor()
        a = cur.execute("SELECT * FROM tochka_rosta WHERE Имя=?",
                             (item_id := self.lineEdit.text(),)).fetchall()
        self.titles = [description[0] for description in cur.description]
        self.comboBox.addItems(self.titles)

    def update_result(self):
        cur = self.con.cursor()
        result = cur.execute(f"SELECT * FROM tochka_rosta WHERE {self.comboBox.currentText()}=?",
                             (item_id := self.lineEdit.text(),)).fetchall()
        self.tableWidget.setRowCount(len(result))

        self.tableWidget.setColumnCount(len(result[0]))
        self.titles = [description[0] for description in cur.description]
        self.tableWidget.setHorizontalHeaderLabels(self.titles)
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))

    def full_result(self):
        result = """SELECT * from tochka_rosta"""
        cursor = self.con.cursor()
        cursor.execute(result)
        result = cursor.fetchall()
        self.tableWidget.setRowCount(len(result))

        self.tableWidget.setColumnCount(len(result[0]))
        self.titles = [description[0] for description in cursor.description]
        self.tableWidget.setHorizontalHeaderLabels(self.titles)
        for i, elem in enumerate(result):
            for j, val in enumerate(elem):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(val)))

def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())
