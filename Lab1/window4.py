from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Window4(object):
    Z = set()
    X = None
    Y = None
    temp = set()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(944, 259)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(40, 20, 21, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 26, 141, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 66, 141, 31))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(40, 60, 21, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(40, 100, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(70, 146, 141, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(40, 140, 21, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(40, 180, 89, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 130, 941, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 944, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.setw)
        self.pushButton_2.clicked.connect(self.count)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "X"))
        self.label_2.setText(_translate("MainWindow", "None"))
        self.label_3.setText(_translate("MainWindow", "None"))
        self.label_4.setText(_translate("MainWindow", "Y"))
        self.pushButton.setText(_translate("MainWindow", "Show"))
        self.label_5.setText(_translate("MainWindow", "None"))
        self.label_6.setText(_translate("MainWindow", "Z"))
        self.pushButton_2.setText(_translate("MainWindow", "Calculate"))
    
    def setw(self):
        self.label_2.setText(str(self.X))
        self.label_2.adjustSize()
        self.label_3.setText(str(self.Y))
        self.label_3.adjustSize()

    def count(self):
        for i in self.X:
            for j in self.Y:
                if i == j:
                    self.temp.add(i)
        for i in self.X:
            if i not in self.temp:
                self.Z.add(i)
        self.label_5.setText(str(self.Z))
        self.label_5.adjustSize()
        f = open("D3-is.txt","w+")
        f.write(str(self.Z))
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
