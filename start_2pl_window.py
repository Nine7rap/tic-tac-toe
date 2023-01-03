# -*- coding: utf-8 -*-

"""file describes StartWindow for 2 players mode class"""

from PyQt5 import QtCore, QtGui, QtWidgets
import menu_2pl_window

import tic_tac_toe
from os import path
import csv

class Ui_Form(QtWidgets.QWidget):

    def __init__(self):
        super(Ui_Form, self).__init__()
        self.setObjectName("Start2PlWindow")
        self.resize(800, 600)

        font = QtGui.QFont()
        font.setFamily("Algerian")

        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(-30, -10, 841, 650))
        self.frame.setStyleSheet("background-image: url(res/frame_3.jpg);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(130, 100, 651, 121))
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.change_label = QtWidgets.QLabel(self.frame)
        self.change_label.setGeometry(QtCore.QRect(240, 360, 421, 81))
        self.change_label.setFont(font)
        self.change_label.setObjectName("change_label")

        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(330, 420, 231, 31))
        self.lineEdit.setStyleSheet("background-image: url(res/white.jfif);")
        self.lineEdit.setObjectName("lineEdit")

        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(390, 470, 101, 31))
        self.pushButton.setStyleSheet("background-image: url(res/white.jfif);")
        self.pushButton.setObjectName("pushButton")

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Start2PlWindow", "Tic-Tac-Toe"))
        self.label.setText(_translate("Start2PlWindow",
                                      "<html><head/><body><p align=\"center\"><span style=\" font-size:28pt;\">Now, type your nicknames</span></p><p align=\"center\"><span style=\" font-size:28pt;\">P.S. one by one</span></p></body></html>"))
        self.change_label.setText(_translate("Start2PlWindow",
                                             "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">enter 1\'st player nickname</span></p></body></html>"))
        self.pushButton.setText(_translate("Start2PlWindow", "ENTER"))
        QtCore.QMetaObject.connectSlotsByName(self)

        self.pushButton.clicked.connect(lambda: second_pl())


        def click(arg):
            """method closes the current window and shows a needed one"""
            self.close()
            self.ui = arg.Ui_Form()
            self.ui.show()
        def second_pl():
            """method gives to the 2'nd player to enter the name and calls db_upload() and click() funs"""
            nick_1 = self.lineEdit.text()

            self.change_label.setText(_translate("Start2PlWindow",
                                             "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Now, enter 2\'nd player nickname</span></p></body></html>"))
            self.pushButton.clicked.connect(lambda: click(menu_2pl_window))
            self.pushButton.clicked.connect(lambda: csv_upload(nick_1))

        def csv_upload(nick):
            nick_2 = self.lineEdit.text()
            checker_1 = True
            checker_2 = True
            if path.exists('table.csv'):
                with open('table.csv') as f:
                    reader = list(csv.reader(f))
                    list_1 = [el for el in reader if el]

                for el in list_1:
                    if nick in el:
                        checker_1 = False
                    if nick_2 in el:
                        checker_2 = False
                if checker_1:
                    list_1.append([nick, 0, 0, 0])
                if checker_2:
                    list_1.append([nick_2, 0, 0, 0])
                with open('table.csv', 'w') as f:
                    writer = csv.writer(f)
                    writer.writerows(list_1)
            else:
                with open('table.csv', 'w') as f:
                    writer = csv.writer(f)
                    list_1 = [[nick, 0, 0, 0], [nick_2, 0, 0, 0]]
                    writer.writerows(list_1)
            with open('players_2.txt', 'w') as f:
                f.write(f"{nick} {nick_2}")