from PyQt5 import QtCore, QtGui, QtWidgets
from window2 import Ui_MainWindow_2
from window3 import Ui_MainWindow_3
from window4 import Ui_MainWindow_4



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 349)
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(150, 20, 171, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(620, 20, 81, 51))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(510, 10, 20, 431))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(160, 100, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(160, 140, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(160, 180, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(160, 220, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(570, 80, 161, 33))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(570, 130, 161, 33))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(570, 180, 161, 33))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)




        def call_window2():
            self.window2 = QtWidgets.QMainWindow()
            self.ui_2 = Ui_MainWindow_2()
            self.ui_2.setupUi(self.window2)
            self.window2.setWindowTitle("Window 2")
            self.window2.show()

        

        def call_window3():
            self.window3 = QtWidgets.QMainWindow()
            self.ui_3 = Ui_MainWindow_3()
            Ui_MainWindow_3.set_A = Ui_MainWindow_2.set_A
            Ui_MainWindow_3.set_B = Ui_MainWindow_2.set_B
            Ui_MainWindow_3.men = Ui_MainWindow_2.men
            Ui_MainWindow_3.women = Ui_MainWindow_2.women
            self.ui_3.setupUi(self.window3)
            self.window3.setWindowTitle("Window 3")
            self.window3.show()
            print(Ui_MainWindow_3.men, "\n", Ui_MainWindow_3.women)
        
        def call_window4():
            self.window4 = QtWidgets.QMainWindow()
            self.ui_4 = Ui_MainWindow_4()
            Ui_MainWindow_4.set_A = Ui_MainWindow_3.set_A
            Ui_MainWindow_4.set_B = Ui_MainWindow_3.set_B
            Ui_MainWindow_4.set_S = Ui_MainWindow_3.set_S
            Ui_MainWindow_4.set_R = Ui_MainWindow_3.set_R
            self.ui_4.setupUi(self.window4)
            self.window4.setWindowTitle("Window 4")
            self.window4.show()

        self.pushButton.clicked.connect(call_window2)
        self.pushButton_2.clicked.connect(call_window3)
        self.pushButton_3.clicked.connect(call_window4)




        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Information"))
        self.label.adjustSize()
        self.label_2.setText(_translate("MainWindow", "Go to"))
        self.label_3.setText(_translate("MainWindow", "Name: Подкур Антон"))
        self.label_4.setText(_translate("MainWindow", "Group: ІВ-92"))
        self.label_5.setText(_translate("MainWindow", "Number: 18"))
        self.label_6.setText(_translate("MainWindow", "Variant: 21"))
        self.pushButton.setText(_translate("MainWindow", "Window2"))
        self.pushButton_2.setText(_translate("MainWindow", "Window3"))
        self.pushButton_3.setText(_translate("MainWindow", "Window4"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.setWindowTitle("Window 1")
    MainWindow.show()
    sys.exit(app.exec_())

