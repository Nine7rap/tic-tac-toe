# -*- coding: utf-8 -*-

"""file describes StartWindow for 1 player mode class"""
import csv

from PyQt5 import QtCore, QtGui, QtWidgets
import menu_1pl_window

from os import path

class Ui_Form(QtWidgets.QWidget):
    def __init__(self):
        super(Ui_Form, self).__init__()
        self.setObjectName("Form")
        self.resize(800, 600)

        font = QtGui.QFont()
        font.setFamily("Algerian")

        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(-11, -11, 821, 631))
        self.frame.setStyleSheet("background-image: url(res/frame_3.jpg);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(120, 90, 641, 81))

        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(240, 360, 411, 41))
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(320, 410, 221, 31))
        self.lineEdit.setStyleSheet("background-image: url(res/white.jfif);")
        self.lineEdit.setObjectName("lineEdit")

        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(370, 460, 121, 31))
        self.pushButton.setStyleSheet("background-image: url(res/white.jfif);")
        self.pushButton.setObjectName("pushButton")

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Form", "Tic-Tac-Toe"))
        self.label.setText(_translate("Form",
                                      "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">now, type your nickname</span></p></body></html>"))
        self.label_2.setText(_translate("Form",
                                        "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt;\">enter your nickname</span></p><p align=\"center\"><br/></p></body></html>"))
        self.pushButton.setText(_translate("Form", "ENTER"))
        QtCore.QMetaObject.connectSlotsByName(self)

        self.pushButton.clicked.connect(lambda: click(menu_1pl_window))
        self.pushButton.clicked.connect(lambda: csv_upload())

        def click(arg):
            """method closes the current window and shows a needed one"""
            self.close()
            self.ui = arg.Ui_Form()
            self.ui.show()

        def csv_upload():
            """method writes to csv file the object of the user"""
            nick = self.lineEdit.text()
            checker = True
            if path.exists('table.csv'):
                with open('table.csv') as f:
                    reader = list(csv.reader(f))
                    list_1 = [el for el in reader if el]

                for el in list_1:
                    if nick in el:
                        checker=False

                if checker:
                    list_1.append([nick, 0, 0, 0])
                    with open('table.csv', 'w') as f:
                        writer = csv.writer(f)
                        writer.writerows(list_1)
            else:
                with open('table.csv', 'w') as f:
                    writer = csv.writer(f)
                    writer.writerow([nick, 0, 0, 0])

            with open('player.txt', 'w') as f:
                f.write(f'{nick}')


