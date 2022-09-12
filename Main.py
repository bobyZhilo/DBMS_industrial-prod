from PyQt5 import QtWidgets  # Импортируем библиотеку для использования интерфейса
from PyQt5.QtWidgets import QTableWidgetItem, QInputDialog
from PyQt5.QtCore import QTimer
import sys  # sys нужен для передачи argv в QApplication
import DB
from design import design_V55
from design import Dialog_Change
from design import Dialog_Add_Line


class MainLogick(QtWidgets.QMainWindow, design_V55.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi_Main(self)                                          # Это нужно для инициализации нашего дизайна

        QTimer.singleShot(1, self.Show_again)                           # При старте сразу вызывать таблицу
                                                                            # Команды для кнопок
        self.Refresh.clicked.connect(lambda: self.Show_again())         # Выполнить функцию Show_again при нажатии кнопки
        self.AddLine.clicked.connect(lambda: self.Add_line())
        self.ChangeLine.clicked.connect(lambda: self.show_dialog())
        self.RemoveLine.clicked.connect(lambda: self.Remove_Line())
        self.Exit.clicked.connect(self.close)

    def Show_again(self):

        self.tableWidget_1.setRowCount(DB.Select_All()[-1][0])
        self.tableWidget_2.setRowCount(DB.Select_All()[-1][0])
        count = 0
        for i in DB.Select_All():
            self.tableWidget_1.setItem(count, 0, QTableWidgetItem(str(i[0])))
            self.tableWidget_1.setItem(count, 1, QTableWidgetItem(i[1]))
            self.tableWidget_1.setItem(count, 2, QTableWidgetItem(i[2]))
            self.tableWidget_1.setItem(count, 3, QTableWidgetItem(str(i[3]) + " Руб."))
            self.tableWidget_1.setItem(count, 4, QTableWidgetItem(i[4]))
            self.tableWidget_1.setItem(count, 5, QTableWidgetItem(i[5]))

            self.tableWidget_2.setItem(count, 0, QTableWidgetItem(i[1]))
            self.tableWidget_2.setItem(count, 1, QTableWidgetItem(i[2]))
            self.tableWidget_2.setItem(count, 2, QTableWidgetItem(str(i[3]) + "Руб."))
            self.tableWidget_2.setItem(count, 3, QTableWidgetItem(i[4]))

            count += 1

    def show_dialog(self):                                                                  #Изменить запись
        try:
            text, ok = QInputDialog.getText(self, 'Выбор записи', 'Введите Id записи')
            if ok:
                DialogWindow_1_inst = DialogWindow_1(text)
                DialogWindow_1_inst.show()
                DialogWindow_1_inst.exec_()
        except:
            print("Error!")

    def Add_line(self):
        self.tableWidget_1.setRowCount(DB.Select_All()[-1][0] + 1)
        DialogWindow_2_inst = DialogWindow_2()
        DialogWindow_2_inst.show()
        DialogWindow_2_inst.exec_()

    def Remove_Line(self):
        try:
            text, ok = QInputDialog.getText(self, 'Удаление записи', 'Введите Id записи')
            if ok:
                try:
                    DB.Remove_Line(text)
                except DB.sqlite3.DatabaseError as err:
                    print("Error: ", err)
        except:
            print("Error!")


# Окно изменения записи

class DialogWindow_1(QtWidgets.QDialog, Dialog_Change.Ui_Dialog_1):
    def __init__(self, text):
        super().__init__()
        self.setupUi_Dialog_1(self)
        try:
            results = DB.Select_By_Id(text)
        except DB.sqlite3.DatabaseError as err:
            print("Error: ", err)
        self.lineEdit_Id.setText(str(results[0][0]))
        self.lineEdit_Booker.setText(results[0][1])
        self.lineEdit_Date.setText(results[0][2])
        self.lineEdit_Costs.setText(str(results[0][3]))
        self.lineEdit_Status.setText(results[0][4])
        self.lineEdit_Email.setText(results[0][5])
        self.buttonBox.accepted.connect(lambda: self.Save_char())

    def Save_char(self):
        Id = self.lineEdit_Id.text()
        Booker = self.lineEdit_Booker.text()
        Date = self.lineEdit_Date.text()
        Costs = self.lineEdit_Costs.text()
        Status = self.lineEdit_Status.text()
        Email = self.lineEdit_Email.text()

        try:
            DB.Update_Line(Booker, Date, Costs, Status, Email, Id)
        except DB.sqlite3.DatabaseError as err:
            print("Error: ", err)

class DialogWindow_2(QtWidgets.QDialog, Dialog_Add_Line.Ui_Dialog_2):
    def __init__(self):
        super().__init__()
        self.setupUi_Dialog_2(self)

        self.lineEdit_Id.setText(str(DB.Select_All()[-1][0] + 1))

        self.buttonBox.accepted.connect(lambda: self.Save_line())

    def Save_line(self):
        Booker = self.lineEdit_Booker.text()
        Date = self.lineEdit_Date.text()
        Costs = self.lineEdit_Costs.text()
        Status = self.lineEdit_Status.text()
        Email = self.lineEdit_Email.text()

        try:
            DB.Insert_Line(Booker, Date, Costs, Status, Email)
        except DB.sqlite3.DatabaseError as err:
            print("Error: ", err)


def main():
    app = QtWidgets.QApplication(sys.argv)                          # Новый экземпляр QApplication
    window = MainLogick()                                           # Создаём объект класса ExampleApp
    window.show()                                                   # Показываем окно
    app.exec_()                                                     # и запускаем приложение

if __name__ == '__main__':                                          # Если мы запускаем файл напрямую, а не импортируем
    main()                                                          # то запускаем функцию main()