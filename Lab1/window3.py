from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Window3(object):
    A = None
    B = None
    C = None
    vers_set = None
    nBnA = set()
    notB = set()
    D = set()
    counter = 0
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(1050, 489)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(60, 10, 67, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 40, 67, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 40, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(60, 70, 67, 17))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 70, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 116, 1200, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(260, 144, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(470, 150, 67, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(170, 196, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(450, 190, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(160, 230, 151, 41))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(440, 230, 151, 41))
        self.label_12.setObjectName("label_12")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(290, 290, 131, 41))
        self.pushButton.setObjectName("pushButton")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(90, 360, 67, 21))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(50, 360, 21, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 400, 89, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(20, 95, 89, 25))
        self.pushButton_3.setObjectName("pushButton_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 982, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton_3.clicked.connect(self.setw)
        self.pushButton.clicked.connect(self.steps)
        self.pushButton.clicked.connect(self.save_the_file)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "A"))
        self.label_2.setText(_translate("MainWindow", "None"))
        self.label_3.setText(_translate("MainWindow", "None"))
        self.label_4.setText(_translate("MainWindow", "B"))
        self.label_5.setText(_translate("MainWindow", "None"))
        self.label_6.setText(_translate("MainWindow", "C"))
        self.label_7.setText(_translate("MainWindow", "Number of operation: "))
        self.label_8.setText(_translate("MainWindow", "0"))
        self.label_9.setText(_translate("MainWindow", "Set-operand"))
        self.label_10.setText(_translate("MainWindow", "Set-result"))
        self.label_11.setText(_translate("MainWindow", "None"))
        self.label_12.setText(_translate("MainWindow", "None"))
        self.pushButton.setText(_translate("MainWindow", "Next Step"))
        self.label_13.setText(_translate("MainWindow", "none"))
        self.label_14.setText(_translate("MainWindow", "D"))
        self.pushButton_2.setText(_translate("MainWindow", "Save to file"))
        self.pushButton_3.setText(_translate("MainWindow", "Show"))

    def setw(self):
        self.label_2.setText(str(self.A))
        self.label_2.adjustSize()
        self.label_3.setText(str(self.B))
        self.label_3.adjustSize()
        self.label_5.setText(str(self.C))
        self.label_5.adjustSize()
    
    def steps(self):
        self.counter+=1
        if self.counter == 1:
            self.label_11.setText("-B")
            self.label_11.adjustSize()
            self.notB = self.vers_set - self.B
            self.label_12.setText(str(self.notB))
            self.label_12.adjustSize()
            self.label_8.setText("1")
            self.label_8.adjustSize()
        elif self.counter == 2:
            self.label_11.setText("-B & A")
            self.label_11.adjustSize()
            self.nBnA = self.A & self.notB
            self.label_12.setText(str(self.nBnA))
            self.label_12.adjustSize()
            self.label_8.setText("2")
            self.label_8.adjustSize()
        elif self.counter == 3:
            self.label_11.setText("(-B & A) | C")
            self.label_11.adjustSize()
            self.D = self.nBnA | self.C
            self.label_12.setText(str(self.D))
            self.label_12.adjustSize()
            self.label_8.setText("3")
            self.label_8.adjustSize()
            self.label_13.setText(str(self.D))
            self.label_13.adjustSize()

    def save_the_file(self):
        f = open("D2-is.txt","w+")
        f.write(str(self.D))
        f.close()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    app.setStyleSheet('QMainWindow{background-color:#1a1d23;}\
    QPushButton{color:#e0e0e0 ;background-color:#202b3a; border-style: outset; border-width: 2px; border-radius: 10px; border-color: beige;}\
    QPushButton:pressed{border-side:inset;border-color: red}\
    QMenuBar{color: #e0e0e0;background-color:#33364c;}\
    QSpinBox{color: #e0e0e0;background-color:#202b3a;}\
    QLineEdit{color: #e0e0e0; background-color:#202b3a;selection-color: yellow;selection-background-color: red;}\
    QLabel{color: #e0e0e0;}\
    QMenu{color: #e0e0e0;background-color:#33364c;}')
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
