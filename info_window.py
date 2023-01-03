# -*- coding: utf-8 -*-

"""file describes InfoWindow class"""

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(QtWidgets.QWidget):
    def __init__(self):
        super(Ui_Form, self).__init__()
        self.setObjectName("InfoWindow")
        self.resize(800, 600)

        font = QtGui.QFont()
        font.setFamily("Algerian")

        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(-21, -11, 841, 650))
        self.frame.setStyleSheet("background-image: url(res/frame_3.jpg);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(60, 20, 751, 571))

        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("InfoWindow", "About"))
        self.label_2.setText(_translate("InfoWindow",
                                        "<html><head/><body><p align=\"center\"><span style=\" font-size:18pt;\">About game</span></p><p><span style=\" font-size:16pt;\">This is a game \'Tic-Tac-Toe\' where You compete with AI or with</span></p><p><span style=\" font-size:16pt;\">Your friend who seats near.</span></p><p align=\"center\"><span style=\" font-size:18pt;\">Rules</span></p><p><span style=\" font-size:16pt;\">There are crosses and zeros in the game like types of moving. Also, </span></p><p><span style=\" font-size:16pt;\">there is a 3x3 field where user can set the sign in one of the cells.</span></p><p><span style=\" font-size:16pt;\">You take turns choosing where to put your sign untill one of</span></p><p><span style=\" font-size:16pt;\">users fill 3 cells vertically, horizontally or diagonally. </span></p><p><span style=\" font-size:16pt;\">After achieving this point the current user wins the game.</span></p><p><span style=\" font-size:16pt;\">If nobody filled 3 cells but there is no way to move, the game</span></p><p><span style=\" font-size:16pt;\">ends with a draw.</span></p><p align=\"center\"><span style=\" font-size:18pt;\">Author</span></p><p><span style=\" font-size:16pt;\">The game is made by Konstantin Utyupin and Danylo Kameniev </span></p></body></html>"))

        QtCore.QMetaObject.connectSlotsByName(self)
