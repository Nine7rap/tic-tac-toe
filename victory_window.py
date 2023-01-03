# -*- coding: utf-8 -*-

"""file describes VictoryWindow class"""

from PyQt5 import QtCore, QtGui, QtWidgets
import menu_1pl_window


class Ui_Form(QtWidgets.QWidget):
    def __init__(self):
        super(Ui_Form, self).__init__()
        self.setObjectName("VictoryWindow")
        self.resize(800, 600)

        font = QtGui.QFont()
        font.setFamily("Bradley Hand ITC")

        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(-40, -10, 871, 650))
        self.frame.setStyleSheet("background-image: url(res/frame_1.jfif);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(230, 60, 431, 351))
        self.label.setFont(font)
        self.label.setStyleSheet("background-image: url(res/yagami.png);")
        self.label.setObjectName("label")

        font.setPointSize(12)

        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(370, 490, 151, 41))
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-image: url(res/white.jfif);")
        self.pushButton.setObjectName("pushButton")

        QtCore.QMetaObject.connectSlotsByName(self)

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("VictoryWindow", "Victory"))
        self.label.setText(_translate("VictoryWindow",
                                      "<html><head/><body><p align=\"center\"><br/></p><p align=\"center\"><br/></p><p align=\"center\"><br/><span style=\" font-size:36pt; color:#ffffff;\">YOU WON</span></p></body></html>"))
        self.pushButton.setText(_translate("VictoryWindow", "BACK TO MENU"))

        self.pushButton.clicked.connect(lambda: click())

        def click():
            """method closes the current window and show a needed window"""
            self.close()
            self.ui = menu_1pl_window.Ui_Form()
            self.ui.show()


