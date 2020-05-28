from PyQt5 import QtCore, QtGui, QtWidgets
import random
from window2 import Ui_MainWindow2


class Ui_MainWindow(object):
    final_list = list()
    list1 = list()
    list2 = list()
    flag = True
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(682, 450)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(30, 20, 201, 151))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setGeometry(QtCore.QRect(40, 10, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setUnderline(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 60, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(30, 100, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(30, 180, 631, 221))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_5 = QtWidgets.QLabel(self.frame_2)
        self.label_5.setGeometry(QtCore.QRect(30, 50, 601, 171))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(30, 20, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setUnderline(True)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(250, 20, 231, 151))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_6 = QtWidgets.QLabel(self.frame_3)
        self.label_6.setGeometry(QtCore.QRect(30, 10, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setUnderline(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame_3)
        self.label_7.setGeometry(QtCore.QRect(10, 60, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.spinBox = QtWidgets.QSpinBox(self.frame_3)
        self.spinBox.setGeometry(QtCore.QRect(180, 70, 42, 25))
        self.spinBox.setObjectName("spinBox")
        self.pushButton = QtWidgets.QPushButton(self.frame_3)
        self.pushButton.setGeometry(QtCore.QRect(60, 110, 80, 24))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(530, 80, 111, 41))
        self.pushButton_4.setObjectName("pushButton_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        def action1():
            self.nodes_amount = self.spinBox.value()
            self.nodes = list(range(1,self.nodes_amount+1))
            self.final_list.clear()

            for i in range(1,self.nodes_amount+1):
                num = random.randint(1,4)
                for j in range(num):
                    number = random.randint(1, self.nodes_amount)
                    if i!=number:
                        if [i,number] not in self.list1:
                            self.list1.append([i,number])
                            self.list1.append([number,i])
            #print(self.list1)
            self.final_list = self.list1

            Ui_MainWindow2.nodes_amount = self.spinBox.value()
            Ui_MainWindow2.final_list = self.list1
            Ui_MainWindow2.flag  = True

            self.window2 = QtWidgets.QMainWindow()
            self.ui_2 = Ui_MainWindow2()
            self.ui_2.setupUi(self.window2)
            self.window2.setWindowTitle("Вікно 2")

            self.window2.show()

        def action2():
            self.final_list.clear()
            self.list2 = [[1,2],[1,4],[1,6],[4,2],[4,6],[4,7],[2,3],[2,5],[2,7],[5,3],[5,7],[5,8],[3,8],[6,7],[6,9],[7,9],[7,10],[9,10],[7,8],[7,10],[8,10]]
            for i in self.list2:
                self.final_list.append(i)
                self.final_list.append([i[1],i[0]])

            Ui_MainWindow2.nodes_amount = 10
            Ui_MainWindow2.final_list = self.final_list
            Ui_MainWindow2.flag  = False

            self.window2 = QtWidgets.QMainWindow()
            self.ui_2 = Ui_MainWindow2()
            self.ui_2.setupUi(self.window2)
            self.window2.setWindowTitle("Вікно 2")

            self.window2.show()
            #print(self.final_list)


        self.pushButton.clicked.connect(action1)
        self.pushButton_4.clicked.connect(action2)



    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Інформація"))
        self.label.setText(_translate("MainWindow", "Подкур Антон ІВ-92"))
        self.label_2.setText(_translate("MainWindow", "18 номер у списку"))
        self.label_5.setText(_translate("MainWindow", "3. Вивчити основні означення та теореми про розфарбування графів.\n"
"Створити програму розфарбування графів, яка реалізує модифікований\n"
"евристичний алгоритм розфарбування."))
        self.label_4.setText(_translate("MainWindow", "Завдання"))
        self.label_6.setText(_translate("MainWindow", "Створити граф"))
        self.label_7.setText(_translate("MainWindow", "Кількість вершин:"))
        self.pushButton.setText(_translate("MainWindow", "Створити"))
        self.pushButton_4.setText(_translate("MainWindow", "Готовий граф"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
