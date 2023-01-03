# -*- coding: utf-8 -*-

"""file describes LoseWindow class"""

from PyQt5 import QtCore, QtGui, QtWidgets
import menu_1pl_window

class Ui_Form(QtWidgets.QWidget):
    def __init__(self):
        super(Ui_Form, self).__init__()
        self.setObjectName("LoseWindow")
        self.resize(800, 600)

        font = QtGui.QFont()
        font.setFamily("Bradley Hand ITC")

        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(-50, -10, 861, 650))
        self.frame.setStyleSheet("background-image: url(res/frame_1.jfif);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(270, 100, 371, 301))

        self.label.setFont(font)
        self.label.setStyleSheet("background-image: url(res/ryuk.png);")
        self.label.setObjectName("label")

        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(380, 500, 151, 41))

        font.setPointSize(12)

        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-image: url(res/white.jfif);")
        self.pushButton.setObjectName("pushButton")

        QtCore.QMetaObject.connectSlotsByName(self)

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("LoseWindow", "Lose"))
        self.label.setText(_translate("LoseWindow", "<html><head/><body><p align=\"center\"><br/></p><p align=\"center\"><span style=\" font-size:36pt; color:#ffffff;\">YOU LOST</span><span style=\" font-size:18pt; color:#ffffff;\"><br/></span></p></body></html>"))
        self.pushButton.setText(_translate("LoseWindow", "BACK TO MENU"))

        self.pushButton.clicked.connect(lambda: click())

        def click():
            """method closes the current window and show a needed window"""
            self.close()
            self.ui = menu_1pl_window.Ui_Form()
            self.ui.show()





