"""class describes the DrawWindow"""

from PyQt5 import QtCore, QtGui, QtWidgets
import menu_1pl_window
import menu_2pl_window


class Ui_Form(QtWidgets.QWidget):
    def __init__(self):
        super(Ui_Form, self).__init__()
        self.twopl = None
        self.setObjectName("Ui_Form")
        self.resize(800, 600)

        font = QtGui.QFont()
        font.setFamily("Bradley Hand ITC")
        font.setPointSize(46)

        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(-30, -20, 841, 641))
        self.frame.setStyleSheet("background-image: url(res/frame_1.jfif);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(60, 130, 741, 331))
        self.label.setFont(font)
        self.label.setStyleSheet("background-image: url(res/yagami.png);\n"
                                 "background-image: url(res/ryuk.png);")
        self.label.setObjectName("label")

        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(390, 520, 114, 34))

        font.setPointSize(10)

        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-image: url(res/white.jfif);")
        self.pushButton.setObjectName("pushButton")

        QtCore.QMetaObject.connectSlotsByName(self)

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("Ui_Form", "Form"))
        self.label.setText(_translate("Ui_Form",
                                      "<html><head/><body><p align=\"center\"><span style=\" font-size:48pt; font-weight:600; color:#ffffff;\">Draw</span></p></body></html>"))
        self.pushButton.setText(_translate("Ui_Form", "BACK TO MENU"))

        self.pushButton.clicked.connect(lambda: click(self.twopl))

        def click(twoch):
            """method closes the current window and show a needed window"""
            self.close()
            if twoch:
                self.ui = menu_2pl_window.Ui_Form()
            elif not twoch:
                self.ui = menu_1pl_window.Ui_Form()
            self.ui.show()
