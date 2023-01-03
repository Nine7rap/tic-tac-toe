# -*- coding: utf-8 -*-

"""class describes the MainWindow -'ChooseWindow' """

import sys
from PyQt5 import QtCore, QtGui, QtWidgets, QtMultimedia
from PyQt5.QtCore import QUrl
from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
import start_1pl_window
import start_2pl_window


class Ui_MainWindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.mode: int
        font = QtGui.QFont()
        font.setFamily("Algerian")

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-21, -11, 831, 601))
        self.frame.setStyleSheet("background-image: url(res/frame_3.jpg);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")

        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(100, 80, 651, 61))

        self.label.setFont(font)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(200, 320, 471, 71))
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")

        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(340, 400, 151, 31))
        self.pushButton.setStyleSheet("background-image: url(res/white.jfif);")
        self.pushButton.setObjectName("pushButton")

        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setGeometry(QtCore.QRect(340, 440, 151, 31))
        self.pushButton_2.setStyleSheet("background-image: url(res/white.jfif);")
        self.pushButton_2.setObjectName("pushButton_2")

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")

        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)

        self.player = QMediaPlayer()
        # fullfilepath = os.path.join(os.getcwd(), "res/music.mp3")
        # url = QUrl.fromLocalFile(fullfilepath)
        # content = QMediaContent(url)
        #
        # self.player.setMedia(content)
        # self.player.play()

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Choose, don't look here"))
        self.label.setText(_translate("MainWindow",
                                      "<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">Welcome to tic-tac-toe</span></p><p align=\"center\"><br/></p></body></html>"))
        self.label_2.setText(_translate("MainWindow",
                                        "<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; text-decoration: underline;\">select number of players</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "1 Player"))
        self.pushButton_2.setText(_translate("MainWindow", "2 Players"))
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(lambda: click1(start_1pl_window))
        self.pushButton_2.clicked.connect(lambda: click2(start_2pl_window))

        def click1(arg):
            """method closes the current window and shows a needed one"""
            MainWindow.close()
            self.ui = arg.Ui_Form()
            self.mode = 1
            self.ui.show()

        def click2(arg):
            """method closes the current window and shows a needed one"""
            MainWindow.close()
            self.ui = arg.Ui_Form()
            self.mode = 2
            self.ui.show()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    window = Ui_MainWindow()
    MainWindow.show()
    sys.exit(app.exec_())
