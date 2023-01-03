# -*- coding: utf-8 -*-

"""file describes MenuWindow for 2 players mode class"""

from PyQt5 import QtCore, QtGui, QtWidgets
from time import sleep
import game_window
import info_window
import scoreboard
from random import choice


class Ui_Form(QtWidgets.QWidget):
    def __init__(self):
        super(Ui_Form, self).__init__()
        self.setObjectName("Menu2PlWindow")
        self.resize(800, 600)

        with open("t.txt", "w") as f:
            f.write("2")

        font = QtGui.QFont()
        font.setFamily("Algerian")

        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(-50, -10, 861, 650))
        self.frame.setStyleSheet("background-image: url(res/frame_3.jpg);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.info_button = QtWidgets.QPushButton(self.frame)
        self.info_button.setGeometry(QtCore.QRect(60, 20, 71, 61))
        self.info_button.setStyleSheet("image: url(res/info.png);")
        self.info_button.setText("")
        self.info_button.setObjectName("info_button")

        font.setPointSize(8)

        self.scoreboard_button = QtWidgets.QPushButton(self.frame)
        self.scoreboard_button.setGeometry(QtCore.QRect(570, 30, 91, 41))
        self.scoreboard_button.setFont(font)
        self.scoreboard_button.setStyleSheet("background-image: url(res/white.jfif);")
        self.scoreboard_button.setObjectName("scoreboard_button")

        self.on_vol_button = QtWidgets.QPushButton(self.frame)
        self.on_vol_button.setGeometry(QtCore.QRect(740, 30, 61, 23))
        self.on_vol_button.setStyleSheet("background-image: url(res/white.jfif);")
        self.on_vol_button.setObjectName("on_vol_button")

        self.off_vol_button = QtWidgets.QPushButton(self.frame)
        self.off_vol_button.setGeometry(QtCore.QRect(740, 50, 61, 23))
        self.off_vol_button.setStyleSheet("background-image: url(res/white.jfif);")
        self.off_vol_button.setObjectName("off_vol_button")

        self.volume_label = QtWidgets.QLabel(self.frame)
        self.volume_label.setGeometry(QtCore.QRect(690, 30, 51, 41))
        self.volume_label.setStyleSheet("image: url(res/volume.png);")
        self.volume_label.setText("")
        self.volume_label.setObjectName("volume_label")

        self.paly_button = QtWidgets.QPushButton(self.frame)
        self.paly_button.setGeometry(QtCore.QRect(400, 410, 131, 41))

        font.setPointSize(10)

        self.paly_button.setFont(font)
        self.paly_button.setStyleSheet("background-image: url(res/white.jfif);")
        self.paly_button.setObjectName("paly_button")

        self.decide_label = QtWidgets.QLabel(self.frame)
        self.decide_label.setGeometry(QtCore.QRect(240, 340, 461, 61))
        self.decide_label.setFont(font)
        self.decide_label.setObjectName("decide_label")

        self.who = QtWidgets.QLabel(self.frame)
        self.who.setGeometry(QtCore.QRect(240, 250, 461, 61))
        self.who.setFont(font)
        self.who.setObjectName('who')

        QtCore.QMetaObject.connectSlotsByName(self)

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Menu2PlWindow", "Menu"))
        self.scoreboard_button.setText(_translate("Menu2PlWindow", "Scoreboard"))
        self.on_vol_button.setText(_translate("Menu2PlWindow", "ON"))
        self.off_vol_button.setText(_translate("Menu2PlWindow", "OFF"))
        self.paly_button.setText(_translate("Menu2PlWindow", "DECIDE"))
        self.decide_label.setText(_translate("Menu2PlWindow",
                                             "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">Push to decide who plays what</span></p></body></html>"))

        self.paly_button.clicked.connect(lambda: label_set())
        self.info_button.clicked.connect(lambda: clickinfo(info_window))
        self.scoreboard_button.clicked.connect(lambda: clickinfo(scoreboard))

        def click(arg, list_1, checker):
            """method writing in the file who plays what and closes the current window and shows a needed one"""
            with open('players.txt', 'w+') as f:
                for el in list_1:
                    if not el == checker:
                        circules = el
                f.write(f'{checker} crosses\n{circules} circules')

            sleep(2)
            self.close()
            self.ui = arg.Ui_Form()
            self.ui.show()

        def clickinfo(arg):
            """method show a needed window"""
            self.ui = arg.Ui_Form()
            self.ui.show()

        def label_set():
            """method changes the label and decide who play crosses"""
            with open('players_2.txt') as f:
                list_1 = [el for el in f.read().split()]
            checker = choice([list_1[0], list_1[1]])
            self.decide_label.setText(_translate("Menu2PlWindow",
                                                 f"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">{checker} plays crosses</span></p></body></html>"))
            self.paly_button.setText(_translate("Menu2PlWindow", "PLAY"))
            self.paly_button.clicked.connect(lambda: click(game_window, list_1, checker))
