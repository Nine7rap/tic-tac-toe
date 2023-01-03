# -*- coding: utf-8 -*-

"""file describes MenuWindow for 1 player mode class"""
import csv

from PyQt5 import QtCore, QtGui, QtWidgets
from time import sleep
import game_window
import info_window
import scoreboard
from random import choice



class Ui_Form(QtWidgets.QWidget):
    def __init__(self):
        super(Ui_Form, self).__init__()

        with open("t.txt", "w") as f:
            f.write("1")

        self.setObjectName("Menu1PlWindow")
        self.resize(800, 600)

        font = QtGui.QFont()
        font.setFamily("Algerian")

        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(-21, -11, 841, 641))
        self.frame.setStyleSheet("background-image: url(res/frame_3.jpg);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.info_button = QtWidgets.QPushButton(self.frame)
        self.info_button.setGeometry(QtCore.QRect(30, 20, 71, 61))
        self.info_button.setStyleSheet("image: url(res/info.png);")
        self.info_button.setText("")
        self.info_button.setObjectName("info_button")

        font.setPointSize(10)

        self.score_button = QtWidgets.QPushButton(self.frame)
        self.score_button.setGeometry(QtCore.QRect(570, 30, 91, 41))
        self.score_button.setFont(font)
        self.score_button.setStyleSheet("background-image: url(res/white.jfif);")
        self.score_button.setObjectName("score_button")

        self.on_vol_button = QtWidgets.QPushButton(self.frame)
        self.on_vol_button.setGeometry(QtCore.QRect(740, 30, 61, 21))
        self.on_vol_button.setFont(font)
        self.on_vol_button.setStyleSheet("background-image: url(res/white.jfif);")
        self.on_vol_button.setObjectName("on_vol_button")

        self.off_vol_button = QtWidgets.QPushButton(self.frame)
        self.off_vol_button.setGeometry(QtCore.QRect(740, 50, 61, 21))
        self.off_vol_button.setFont(font)
        self.off_vol_button.setStyleSheet("background-image: url(res/white.jfif);")
        self.off_vol_button.setObjectName("off_vol_button")

        self.volume_label = QtWidgets.QLabel(self.frame)
        self.volume_label.setGeometry(QtCore.QRect(690, 30, 51, 41))
        self.volume_label.setStyleSheet("image: url(res/volume.png);")
        self.volume_label.setText("")
        self.volume_label.setObjectName("volume_label")

        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(220, 300, 451, 81))
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.comboBox = QtWidgets.QComboBox(self.frame)
        self.comboBox.setGeometry(QtCore.QRect(320, 370, 251, 31))

        font.setPointSize(14)

        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.enter_button = QtWidgets.QPushButton(self.frame)
        self.enter_button.setGeometry(QtCore.QRect(380, 430, 121, 31))

        self.enter_button.setFont(font)
        self.enter_button.setStyleSheet("background-image: url(res/white.jfif);")
        self.enter_button.setObjectName("enter_button")

        def volumeoff():
        #     tic_tac_toe.ui.player.setMuted(True)
            pass
        self.off_vol_button.clicked.connect(lambda: volumeoff())

        def volumeon():
            # choose_window.ui.player.setMuted(True)
            pass
        self.on_vol_button.clicked.connect(lambda: volumeon())

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Menu1PlWindow", "Form"))
        self.score_button.setText(_translate("Menu1PlWindow", "Scoreboard"))
        self.on_vol_button.setText(_translate("Menu1PlWindow", "ON"))
        self.off_vol_button.setText(_translate("Menu1PlWindow", "OFF"))
        self.label_2.setText(_translate("Menu1PlWindow",
                                        "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">Select a difficulty level</span></p></body></html>"))
        self.comboBox.setItemText(0, _translate("Menu1PlWindow", "EASY"))
        self.comboBox.setItemText(1, _translate("Menu1PlWindow", "MEDIUM"))
        self.comboBox.setItemText(2, _translate("Menu1PlWindow", "VETERAN OMG"))
        self.enter_button.setText(_translate("Menu1PlWindow", "DECIDE"))
        QtCore.QMetaObject.connectSlotsByName(self)

        self.info_button.clicked.connect(lambda: clickinfo(info_window))
        self.enter_button.clicked.connect(lambda: label_set())
        self.score_button.clicked.connect(lambda: clickinfo(scoreboard))

        def click(arg, types, checker):
            """method writing in the file who plays what and closes the current window and shows a needed one"""
            checker_1 = True
            bot_name = ''
            label_1 = self.comboBox.currentText()
            print(label_1)
            if label_1 == 'EASY':
                bot_name = 'BotFrank'
            if label_1 == 'MEDIUM':
                bot_name = 'BotKevin'
            if label_1 == 'VETERAN OMG':
                bot_name = 'BotRyuk'

            with open('table.csv') as f:
                reader = list(csv.reader(f))
                g_1 = [el for el in reader if el]
                for el in g_1:
                    if bot_name in el:
                        checker_1=False

                if checker_1:
                    g_1.append([bot_name, 0, 0, 0])
                    with open('table.csv', 'w') as f:
                        writer = csv.writer(f)
                        writer.writerows(g_1)

            with open('player.txt') as f:
                list_1 = [f.read(), bot_name]
                print(list_1)
            with open('players.txt', 'w') as f:
                print(checker)
                f.write(f'{list_1[0]} {checker} \n{list_1[1]} {types[0]}')

            sleep(2)
            self.close()
            self.ui = arg.Ui_Form()
            self.ui.show()

        def clickinfo(arg):
            """method shows the needed form"""
            self.ui = arg.Ui_Form()
            self.ui.show()

        def label_set():
            """method changes the label and decide who play crosses"""

            types = ['crosses', 'circules']
            checker = choice(types)
            types.remove(checker)
            self.label_2.setText(_translate("Menu2PlWindow",
                                            f"<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">You play {checker} </span></p></body></html>"))

            self.enter_button.setText(_translate("Menu2PlWindow", "PLAY"))
            self.enter_button.clicked.connect(lambda: click(game_window, types, checker))
