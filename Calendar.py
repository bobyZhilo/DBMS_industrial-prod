from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import *
from PyQt5 import uic
from PyQt5.QtCore import pyqtSignal
import DB


def Get_data():
    try:
        Origin = DB.Get_Date()
        Events = []
        EventsData = []
        EventsQData = []

        for i in Origin:
            Events.append(i[0].split('.'))

        for i in Events:
            i[0] = int(i[0])
            i[1] = int(i[1])
            i[2] = int(i[2])
            EventsData.append([i[2], i[1], i[0]])

        for i in EventsData:
            EventsQData.append(QDate(i[0], i[1], i[2]))
        return EventsQData
    except:
        print("Error!!")


class MyCalendar(QtWidgets.QCalendarWidget):
    def __init__(self, parent=None):
        QtWidgets.QCalendarWidget.__init__(self, parent)

    def paintCell(self, painter, rect, date):
        try:
            QtWidgets.QCalendarWidget.paintCell(self, painter, rect, date)


            if date in Get_data():
                painter.setBrush(QtGui.QColor(0, 200, 200, 50))
                painter.drawRect(rect)
        except:
            print("Error!!")

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("main_window.ui", self)
        self.sec = SecondWindow()
        self.pushButton.clicked.connect(self.on_click)
        self.sec.login_data[str, str].connect(self.handle_input)

    def on_click(self):
        self.sec.show()

    def handle_input(self, name, login):
        self.label.setText(name)
        self.label_2.setText(login)


class SecondWindow(QMainWindow):
    login_data = pyqtSignal(str, str)

    def __init__(self):
        super().__init__()
        uic.loadUi("second_window.ui", self)
        self.pushButton.clicked.connect(self.send_data)

    def send_data(self):
        self.login_data.emit(self.lineEdit.text(), self.lineEdit_2.text())
        self.close()