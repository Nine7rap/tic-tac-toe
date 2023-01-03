# -*- coding: utf-8 -*-

"""file describes Ui_Form class of GameWindow and contain the main code of the exact game"""

from PyQt5 import QtCore, QtGui, QtWidgets
import victory_2pl_window
import victory_window

import random
import lose_window
import draw_window
import csv


class GameButton(QtWidgets.QPushButton):
    def __init__(self, arg):
        super(GameButton, self).__init__(arg)
        self.valuecross = None
        self.corns = None
        self.sides = None


class Ui_Form(QtWidgets.QWidget):
    def __init__(self):
        self.difficulty = None
        self.botmove = None
        with open("players.txt") as f:
            text = f.readlines()
            if text[1].split()[0] == "BotFrank":
                self.difficulty = 1
            elif text[1].split()[0] == "BotKevin":
                self.difficulty = 2
            elif text[1].split()[0] == "BotRyuk":
                self.difficulty = 3
            if text[1].split()[1] == "crosses":
                self.botmove = True
            elif text[1].split()[1] == "circules":
                self.botmove = False
        self.moves = 0
        super(Ui_Form, self).__init__()
        self.movecross = True
        self.setObjectName("GameWindow")
        self.resize(800, 600)
        self.frame = QtWidgets.QFrame(self)
        self.frame.setGeometry(QtCore.QRect(-30, -20, 841, 650))
        self.frame.setStyleSheet("background-image: url(res/frame_3.jpg);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame_in_grid_2 = QtWidgets.QFrame(self.frame)
        self.frame_in_grid_2.setEnabled(True)
        self.frame_in_grid_2.setGeometry(QtCore.QRect(180, 70, 499, 479))
        self.frame_in_grid_2.setStyleSheet("background-image: url(res/white.jfif);\n"
                                           "image: url(res/net.png);")
        self.frame_in_grid_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_in_grid_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_in_grid_2.setObjectName("frame_in_grid_2")

        self.i2 = GameButton(self.frame_in_grid_2)
        self.i2.setGeometry(QtCore.QRect(180, 10, 140, 131))
        self.i2.setStyleSheet("image: url(res/white.jfif);")
        self.i2.setText("")
        self.i2.setObjectName("i2")
        self.i3 = GameButton(self.frame_in_grid_2)
        self.i3.setGeometry(QtCore.QRect(350, 10, 131, 131))
        self.i3.setStyleSheet("image: url(res/white.jfif);")
        self.i3.setText("")
        self.i3.setObjectName("i3")
        self.i5 = GameButton(self.frame_in_grid_2)
        self.i5.setGeometry(QtCore.QRect(180, 170, 140, 131))
        self.i5.setStyleSheet("image: url(res/white.jfif);")
        self.i5.setText("")
        self.i5.setObjectName("i5")
        self.i6 = GameButton(self.frame_in_grid_2)
        self.i6.setGeometry(QtCore.QRect(350, 170, 131, 131))
        self.i6.setStyleSheet("image: url(res/white.jfif);")
        self.i6.setText("")
        self.i6.setObjectName("i6")
        self.i9 = GameButton(self.frame_in_grid_2)
        self.i9.setGeometry(QtCore.QRect(350, 330, 131, 131))
        self.i9.setStyleSheet("image: url(res/white.jfif);")
        self.i9.setText("")
        self.i9.setObjectName("i9")
        self.i4 = GameButton(self.frame_in_grid_2)
        self.i4.setGeometry(QtCore.QRect(20, 170, 131, 131))
        self.i4.setStyleSheet("image: url(res//white.jfif);")
        self.i4.setText("")
        self.i4.setObjectName("i4")
        self.i7 = GameButton(self.frame_in_grid_2)
        self.i7.setGeometry(QtCore.QRect(20, 330, 131, 131))
        self.i7.setStyleSheet("image: url(res/white.jfif);")
        self.i7.setText("")
        self.i7.setObjectName("i7")
        self.i8 = GameButton(self.frame_in_grid_2)
        self.i8.setGeometry(QtCore.QRect(180, 330, 140, 131))
        self.i8.setStyleSheet("image: url(res/white.jfif);")
        self.i8.setText("")
        self.i8.setObjectName("i8")
        self.i1 = GameButton(self.frame_in_grid_2)
        self.i1.setGeometry(QtCore.QRect(20, 10, 131, 131))
        self.i1.setStyleSheet("image: url(res/white.jfif);")
        self.i1.setText("")
        self.i1.setObjectName("i1")

        _translate = QtCore.QCoreApplication.translate
        self.setWindowTitle(_translate("GameWindow", "Tic-Tac-Toe"))
        QtCore.QMetaObject.connectSlotsByName(self)

        self.i1.clicked.connect(lambda: gameclick(self.i1))
        self.i2.clicked.connect(lambda: gameclick(self.i2))
        self.i3.clicked.connect(lambda: gameclick(self.i3))
        self.i4.clicked.connect(lambda: gameclick(self.i4))
        self.i5.clicked.connect(lambda: gameclick(self.i5))
        self.i6.clicked.connect(lambda: gameclick(self.i6))
        self.i7.clicked.connect(lambda: gameclick(self.i7))
        self.i8.clicked.connect(lambda: gameclick(self.i8))
        self.i9.clicked.connect(lambda: gameclick(self.i9))

        self.buts = [self.i1, self.i2, self.i3, self.i4, self.i5, self.i6, self.i7, self.i8, self.i9]

        self.i1.sides = [self.i2, self.i4]
        self.i3.sides = [self.i2, self.i6]
        self.i7.sides = [self.i4, self.i8]
        self.i9.sides = [self.i6, self.i8]
        self.i2.corns = [self.i1, self.i3]
        self.i4.corns = [self.i1, self.i7]
        self.i6.corns = [self.i3, self.i9]
        self.i8.corns = [self.i7, self.i9]

        self.corners = [self.i1, self.i3, self.i7, self.i9]
        self.center = [self.i5]
        self.sides = [self.i2, self.i4, self.i6, self.i8]

        self.row1 = [self.i1, self.i2, self.i3]
        self.row2 = [self.i4, self.i5, self.i6]
        self.row3 = [self.i7, self.i8, self.i9]
        self.rows = [self.row1, self.row2, self.row3]

        self.col1 = [self.i1, self.i4, self.i7]
        self.col2 = [self.i2, self.i5, self.i8]
        self.col3 = [self.i3, self.i6, self.i9]
        self.cols = [self.col1, self.col2, self.col3]

        self.dig1 = [self.i1, self.i5, self.i9]
        self.dig2 = [self.i3, self.i5, self.i7]
        self.digs = [self.dig1, self.dig2]

        self.wins = [self.rows, self.cols, self.digs]

        def lightmove():
            checker = True
            while checker:
                if self.buts:
                    button = random.choice(self.buts)
                else:
                    break
                self.buts.remove(button)
                if button.valuecross is None:
                    botclick(button)
                    self.botmove = False
                    checker = False

        def mediummove():
            def winprob():
                for i in self.wins:
                    for j in i:
                        temp = []
                        for x in j:
                            if self.movecross and x.valuecross:
                                temp.append(x)
                            elif self.movecross is False and x.valuecross is False:
                                temp.append(x)
                            elif self.movecross and x.valuecross is False:
                                temp.append(x)
                                temp.append(x)
                                temp.append(x)
                            elif self.movecross is False and x.valuecross:
                                temp.append(x)
                                temp.append(x)
                                temp.append(x)
                        if len(temp) == 2:
                            return list(set(j) - set(temp))[0]
                return False

            def loseprob():
                for i in self.wins:
                    for j in i:
                        temp = []
                        for x in j:
                            if self.movecross and x.valuecross is False:
                                temp.append(x)
                            elif self.movecross is False and x.valuecross:
                                temp.append(x)
                            elif self.movecross and x.valuecross:
                                temp.append(x)
                                temp.append(x)
                                temp.append(x)
                            elif self.movecross is False and x.valuecross is False:
                                temp.append(x)
                                temp.append(x)
                                temp.append(x)
                        if len(temp) == 2:
                            return list(set(j) - set(temp))[0]
                return False

            x = winprob()
            z = loseprob()
            if x:
                botclick(x)
            elif z:
                botclick(z)
            else:
                lightmove()

        def hardmove():
            def winprob():
                for i in self.wins:
                    for j in i:
                        temp = []
                        for x in j:
                            if self.movecross and x.valuecross:
                                temp.append(x)
                            elif self.movecross is False and x.valuecross is False:
                                temp.append(x)
                            elif self.movecross and x.valuecross is False:
                                temp.append(x)
                                temp.append(x)
                                temp.append(x)
                            elif self.movecross is False and x.valuecross:
                                temp.append(x)
                                temp.append(x)
                                temp.append(x)
                        if len(temp) == 2:
                            return list(set(j) - set(temp))[0]
                return False

            def loseprob():
                for i in self.wins:
                    for j in i:
                        temp = []
                        for x in j:
                            if self.movecross and x.valuecross is False:
                                temp.append(x)
                            elif self.movecross is False and x.valuecross:
                                temp.append(x)
                            elif self.movecross and x.valuecross:
                                temp.append(x)
                                temp.append(x)
                                temp.append(x)
                            elif self.movecross is False and x.valuecross is False:
                                temp.append(x)
                                temp.append(x)
                                temp.append(x)
                        if len(temp) == 2:
                            return list(set(j) - set(temp))[0]
                return False

            x = winprob()
            z = loseprob()
            if x:
                botclick(x)
            elif z:
                botclick(z)
            else:
                if self.moves == 0:
                    botclick(random.choice(self.corners))
                elif self.moves == 1:
                    for i in self.buts:
                        print(i)
                        if i.valuecross:
                            x = i
                    print(x)
                    if x in self.center:
                        botclick(random.choice(self.corners))
                    elif x in self.corners:
                        for j in self.digs:
                            if x in j:
                                t = j
                                t.remove(x)
                                t.remove(self.i5)
                                i = t[0]
                        botclick(i)
                    elif x in self.sides:
                        botclick(random.choice(x.corns))
                elif self.moves == 2:
                    for i in self.buts:
                        if i.valuecross is False:
                            x = i
                        elif i.valuecross:
                            z = i
                    print(0)
                    print(x)
                    print(1)
                    print(z)
                    if x in self.center:
                        if z in [self.i1, self.i9]:
                            botclick(self.i1)
                            botclick(self.i9)
                        if z in [self.i3, self.i7]:
                            botclick(self.i3)
                            botclick(self.i7)
                    elif x in self.corners:
                        onedig = False
                        for j in self.digs:
                            if z in j:
                                t = j
                            if x in j and z in j:
                                onedig = True
                        if not onedig:
                            t.remove(z)
                            t.remove(self.i5)
                            botclick(t[0])
                        elif onedig:
                            botclick(self.i5)
                    elif x in self.sides:
                        botclick(self.i5)
                elif self.moves == 3:
                    if self.i7.valuecross is not None and self.i3.valuecross is not None:
                        botclick(random.choice([self.i1, self.i9]))
                    elif self.i1.valuecross is not None and self.i9.valuecross is not None:
                        botclick(random.choice([self.i7, self.i3]))
                else:
                    lightmove()

        def bot():
            if self.difficulty == 1:
                lightmove()
            elif self.difficulty == 2:
                mediummove()
            elif self.difficulty == 3:
                hardmove()

        def gameclick(arg):
            if self.moves != 9:
                if self.movecross:
                    if arg.valuecross is None:
                        try:
                            if self.difficulty != 3:
                                self.buts.remove(arg)
                                self.corners.remove(arg)
                                self.center.remove(arg)
                                self.sides.remove(arg)
                        except:
                            pass
                        self.moves += 1
                        arg.valuecross = True
                        arg.setStyleSheet("image: url(res/cross.png)")
                        self.movecross = False
                        checker = None
                        if self.difficulty:
                            checker = checkwin(True, isbot=True)
                        elif not self.difficulty:
                            checker = checkwin(True)
                        if self.difficulty is not None and not checker:
                            bot()
                        elif not self.difficulty and not checker:
                            if self.moves == 9:
                                self.close()
                                if self.difficulty:
                                    self.ui2.twopl = False
                                elif not self.difficulty:
                                    self.ui2.twopl = True
                                # self.ui2.show()
                                csv_update()
                        elif self.difficulty and self.moves == 9 and not checker:
                            self.close()
                            if self.difficulty:
                                self.ui2.twopl = False
                            elif not self.difficulty:
                                self.ui2.twopl = True
                            # self.ui2.show()
                            csv_update()

                elif not self.movecross:
                    if arg.valuecross is None:
                        try:
                            if self.difficulty != 3:
                                self.buts.remove(arg)
                                self.corners.remove(arg)
                                self.center.remove(arg)
                                self.sides.remove(arg)
                        except:
                            pass
                        self.moves += 1
                        arg.valuecross = False
                        arg.setStyleSheet("image: url(res/circle.png)")
                        self.movecross = True
                        checker = None
                        if self.difficulty:
                            checker = checkwin(False, isbot=True)
                        elif not self.difficulty:
                            checker = checkwin(False)
                        if self.difficulty is not None and not checker:
                            bot()
                        elif not self.difficulty and not checker:
                            if self.moves == 9:
                                self.close()
                                if self.difficulty:
                                    self.ui2.twopl = False
                                elif not self.difficulty:
                                    self.ui2.twopl = True
                                # self.ui2.show()
                                csv_update()
                        elif self.difficulty and self.moves == 9 and not checker:
                            self.close()
                            if self.difficulty:
                                self.ui2.twopl = False
                            elif not self.difficulty:
                                self.ui2.twopl = True
                            # self.ui2.show()
                            csv_update()

        def botclick(arg):
            if self.moves != 9:
                if self.movecross:
                    if arg.valuecross is None:
                        self.moves += 1
                        arg.valuecross = True
                        arg.setStyleSheet("image: url(res/cross.png)")
                        self.movecross = False
                        if self.moves == 9 and not checkwin(True, isbot=True):
                            self.close()
                            self.ui2 = draw_window.Ui_Form()
                            if self.difficulty:
                                self.ui2.twopl = False
                            elif not self.difficulty:
                                self.ui2.twopl = True
                            # self.ui2.show()
                            csv_update()
                        else:
                            checkwin(True, isbot=True)
                elif not self.movecross:
                    if arg.valuecross is None:
                        self.moves += 1
                        arg.valuecross = False
                        arg.setStyleSheet("image: url(res/circle.png)")
                        self.movecross = True
                        if self.moves == 9 and not checkwin(False, isbot=True):
                            self.close()
                            self.ui2 = draw_window.Ui_Form()
                            if self.difficulty:
                                self.ui2.twopl = False
                            elif not self.difficulty:
                                self.ui2.twopl = True
                            # self.ui2.show()
                            csv_update()
                        else:
                            checkwin(False, isbot=True)
            else:
                print("no move")

        def checkwin(arg, isbot=False):
            if (self.i1.valuecross == arg and self.i2.valuecross == arg and self.i3.valuecross == arg) or \
                    (self.i1.valuecross == arg and self.i4.valuecross == arg and self.i7.valuecross == arg) or \
                    (self.i1.valuecross == arg and self.i5.valuecross == arg and self.i9.valuecross == arg) or \
                    (self.i4.valuecross == arg and self.i5.valuecross == arg and self.i6.valuecross == arg) or \
                    (self.i7.valuecross == arg and self.i8.valuecross == arg and self.i9.valuecross == arg) or \
                    (self.i2.valuecross == arg and self.i5.valuecross == arg and self.i8.valuecross == arg) or \
                    (self.i3.valuecross == arg and self.i6.valuecross == arg and self.i9.valuecross == arg) or \
                    (self.i3.valuecross == arg and self.i5.valuecross == arg and self.i7.valuecross == arg):
                self.close()

                with open('players.txt') as f:
                    list_1 = [el.split() for el in f.readlines()]

                if arg and list_1[0][1] == 'crosses' and not isbot:
                    csv_update(list_1[0][0])
                    self.ui2 = victory_2pl_window.Ui_Form()
                    self.ui2.label.setText(_translate("Victory2PlWindow",
                                                      f"<html><head/><body><p align=\"center\"><br/></p><p align=\"center\"><br/></p><p align=\"center\"><br/></p><p align=\"center\"><br/></p><p align=\"center\"><span style=\" font-size:36pt; color:#ffffff;\">{list_1[0][0]} won</span></p></body></html>"))
                    # win cross
                elif arg and list_1[0][1] != 'crosses' and not isbot:
                    csv_update(list_1[1][0])
                    self.ui2 = victory_2pl_window.Ui_Form()
                    self.ui2.label.setText(_translate("Victory2PlWindow",
                                                      f"<html><head/><body><p align=\"center\"><br/></p><p align=\"center\"><br/></p><p align=\"center\"><br/></p><p align=\"center\"><br/></p><p align=\"center\"><span style=\" font-size:36pt; color:#ffffff;\">{list_1[1][0]} won</span></p></body></html>"))
                    # win circle
                elif not arg and list_1[0][1] == 'crosses' and not isbot:
                    csv_update(list_1[1][0])
                    self.ui2 = victory_2pl_window.Ui_Form()
                    self.ui2.label.setText(_translate("Victory2PlWindow",
                                                      f"<html><head/><body><p align=\"center\"><br/></p><p align=\"center\"><br/></p><p align=\"center\"><br/></p><p align=\"center\"><br/></p><p align=\"center\"><span style=\" font-size:36pt; color:#ffffff;\">{list_1[1][0]} won</span></p></body></html>"))
                    # win cross
                elif not arg and list_1[0][1] != 'crosses' and not isbot:
                    csv_update(list_1[0][0])
                    self.ui2 = victory_2pl_window.Ui_Form()
                    self.ui2.label.setText(_translate("Victory2PlWindow",
                                                      f"<html><head/><body><p align=\"center\"><br/></p><p align=\"center\"><br/></p><p align=\"center\"><br/></p><p align=\"center\"><br/></p><p align=\"center\"><span style=\" font-size:36pt; color:#ffffff;\">{list_1[0][0]} won</span></p></body></html>"))
                    # win circle
                elif arg and list_1[0][1] == 'crosses' and isbot:
                    csv_update(list_1[0][0])
                    self.ui2 = victory_window.Ui_Form()
                    # you crosses win
                elif arg and list_1[0][1] != 'crosses' and isbot:
                    csv_update(list_1[1][0])
                    self.ui2 = lose_window.Ui_Form()
                    # you circles lose
                elif not arg and list_1[0][1] != 'crosses' and isbot:
                    csv_update(list_1[0][0])
                    self.ui2 = victory_window.Ui_Form()
                    # you circles win
                elif not arg and list_1[0][1] == 'crosses' and isbot:
                    csv_update(list_1[1][0])
                    self.ui2 = lose_window.Ui_Form()
                    # you crosses lose
                else:
                    print('Error')
                self.ui2.show()
                return True
            elif self.moves == 9:
                self.ui2 = draw_window.Ui_Form()
                if self.difficulty:
                    self.ui2.twopl = False
                else:
                    self.ui2.twopl = True
                self.close()
                self.ui2.show()

                csv_update()

        def csv_update(winner=None):
            """Summary"""
            with open('players.txt') as f:
                list_1 = [el.split()[0] for el in f.readlines()]
            with open('table.csv') as f:
                reader = list(csv.reader(f))
                users = [el for el in reader if el]

            if winner is not None:
                win = [el for el in users if winner in el]
                users[users.index(win[0])][2] = int(users[users.index(win[0])][2]) + 1

            for el in users:
                if el[0] in list_1:
                    el[1] = int(el[1]) + 1
                    el[3] = int(round(int(el[2]) / int(el[1]) * 100, -1))
                    print(el[3])
            with open('table.csv', 'w') as f:
                writer = csv.writer(f)
                writer.writerows(users)

        if self.botmove:
            bot()
