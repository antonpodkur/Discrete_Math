
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Window5(object):
    Res1 = None
    Res2 = None
    Res3 = None
    Res4 = set()
    temp = None
    X = None
    Y = None
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(953, 430)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(80, 20, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(80, 120, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(80, 50, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(80, 160, 89, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(280, 20, 67, 17))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(280, 130, 67, 17))
        self.label_4.setObjectName("label_4")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(-3, 210, 951, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(280, 240, 67, 17))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(80, 240, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(80, 270, 89, 25))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(80, 320, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(80, 350, 89, 25))
        self.pushButton_4.setObjectName("pushButton_4")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(280, 320, 67, 17))
        self.label_8.setObjectName("label_8")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(510, 160, 89, 51))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(510, 350, 89, 51))
        self.pushButton_6.setObjectName("pushButton_6")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(630, 360, 111, 31))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(630, 170, 111, 31))
        self.label_10.setObjectName("label_10")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 953, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.get_res1)
        self.pushButton_2.clicked.connect(self.get_res2)
        self.pushButton_3.clicked.connect(self.get_res3)
        self.pushButton_4.clicked.connect(self.get_res4)
        self.pushButton_5.clicked.connect(self.compare1)
        self.pushButton_6.clicked.connect(self.compare2)

        
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Standart Expression"))
        self.label_2.setText(_translate("MainWindow", "Simplified Expression"))
        self.pushButton.setText(_translate("MainWindow", "Get it"))
        self.pushButton_2.setText(_translate("MainWindow", "Get it"))
        self.label_3.setText(_translate("MainWindow", "None"))
        self.label_4.setText(_translate("MainWindow", "None"))
        self.label_5.setText(_translate("MainWindow", "None"))
        self.label_6.setText(_translate("MainWindow", "My Z calculating"))
        self.pushButton_3.setText(_translate("MainWindow", "Get it"))
        self.label_7.setText(_translate("MainWindow", "Python Z calculating"))
        self.pushButton_4.setText(_translate("MainWindow", "Get it"))
        self.label_8.setText(_translate("MainWindow", "None"))
        self.pushButton_5.setText(_translate("MainWindow", "Compare"))
        self.pushButton_6.setText(_translate("MainWindow", "Compare"))
        self.label_9.setText(_translate("MainWindow", "None"))
        self.label_10.setText(_translate("MainWindow", "None"))

    def get_res1(self):
        f =open("D-is.txt","r")
        self.temp = f.read()
        f.close()
        self.Res1 = self.temp
        self.label_3.setText(self.Res1)
        self.label_3.adjustSize()
    def get_res2(self):
        f =open("D2-is.txt","r")
        self.temp = f.read()
        f.close()
        self.Res2 = self.temp
        self.label_4.setText(self.Res2)
        self.label_4.adjustSize()
    def get_res3(self):
        f =open("D3-is.txt","r")
        self.temp = f.read()
        f.close()
        self.Res3 = self.temp
        self.label_5.setText(self.Res3)
        self.label_5.adjustSize()
    def get_res4(self):
        self.Res4 = self.X - self.Y
        self.label_8.setText(str(self.Res4))
        self.label_8.adjustSize()

    def compare1(self):
        counter =0
        for i in range(len(self.Res1)):
            if(self.Res1[i]==self.Res2[i]): counter +=1
        if(counter == len(self.Res1)): 
            self.label_10.setText("Same")
            self.label_10.adjustSize()
        else:
            self.label_10.setText("Different")
            self.label_10.adjustSize()
    
    def compare2(self):
        counter =0
        for i in range(len(self.Res3)):
            if(self.Res3[i]==str(self.Res4)[i]): counter +=1
        if(counter == len(self.Res3)): 
            self.label_9.setText("Same")
            self.label_9.adjustSize()
        else:
            self.label_9.setText("Different")
            self.label_9.adjustSize()


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
