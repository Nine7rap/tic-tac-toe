# -*- coding: utf-8 -*-

"""file describes Scoreboard class"""
import csv

from PyQt5 import QtCore, QtGui, QtWidgets
import sys




class Ui_Form(QtWidgets.QWidget):
    def __init__(self):
        super(Ui_Form, self).__init__()
        self.setObjectName("Scoreboard")
        self.resize(800, 600)

        font = QtGui.QFont()
        font.setFamily("Algerian")

        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(-21, -11, 831, 650))
        self.frame.setStyleSheet("background-image: url(res/frame_3.jpg);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setGeometry(QtCore.QRect(220, 110, 425, 421))
        self.tableWidget.setStyleSheet("background-image: url(res/white.jfif);")
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setRowCount(12)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setHorizontalHeaderLabels(('Name', 'Matches', 'Wins', 'Winrate'))

        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(160, 50, 551, 51))
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(380, 550, 121, 41))

        font.setPointSize(10)

        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-image: url(res/white.jfif);")
        self.pushButton.setObjectName("pushButton")

        QtCore.QMetaObject.connectSlotsByName(self)

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Scoreboard", "Scoreboard"))
        self.label.setText(_translate("Scoreboard", "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt;\">Score board of the leaders</span></p><p align=\"center\"><br/></p></body></html>"))
        self.pushButton.setText(_translate("Scoreboard", "BACK TO MENU"))

        self.pushButton.clicked.connect(lambda: self.close())

        with open('table.csv') as f:
            reader = csv.reader(f)
            data = [tuple(el) for el in reader if el]

        row = 0
        for tup in data:
            col = 0

            for item in tup:
                cellinfo = QtWidgets.QTableWidgetItem(item)
                cellinfo.setFont(font)
                self.tableWidget.setItem(row, col, cellinfo)
                col += 1

            row += 1
