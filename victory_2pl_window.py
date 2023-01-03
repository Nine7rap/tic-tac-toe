# -*- coding: utf-8 -*-

"""class describes Victory2plWindow"""

from PyQt5 import QtCore, QtGui, QtWidgets
import menu_2pl_window


class Ui_Form(QtWidgets.QWidget):
    def __init__(self):
        super(Ui_Form, self).__init__()
        self.setObjectName("Victory2PlWindow")
        self.resize(800, 600)

        font = QtGui.QFont()
        font.setFamily("Bradley Hand ITC")

        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(-40, -10, 861, 641))
        self.frame.setStyleSheet("background-image: url(res/frame_1.jfif);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(250, 40, 451, 350))
        self.label.setFont(font)
        self.label.setStyleSheet("background-image: url(res/yagami.png);")
        self.label.setObjectName("label")

        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(390, 490, 131, 41))

        font.setPointSize(10)

        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-image: url(res/white.jfif);")
        self.pushButton.setObjectName("pushButton")


        QtCore.QMetaObject.connectSlotsByName(self)

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Victory2PlWindow", "Victory"))
        self.pushButton.setText(_translate("Victory2PlWindow", "BACK TO MENU"))

        self.pushButton.clicked.connect(lambda: click())

        def click():
            """method closes the current window and show a needed window"""
            self.close()
            self.ui = menu_2pl_window.Ui_Form()
            self.ui.show()
