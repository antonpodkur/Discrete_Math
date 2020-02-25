
import random
from window2 import Ui_Window2
from window3 import Ui_Window3
from window4 import Ui_Window4
from window5 import Ui_Window5

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    A = None
    B = None
    C = None
    vers_set = None
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setFixedSize(830, 450)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(300, 70, 113, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 70, 191, 16))
        self.label.setObjectName("label")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 110, 191, 16))
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(300, 100, 113, 25))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(30, 140, 261, 20))
        self.label_4.setObjectName("label_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(300, 140, 113, 25))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(200, 180, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(40, 220, 101, 20))
        self.label_5.setObjectName("label_5")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(160, 220, 141, 17))
        self.label_2.setObjectName("label_2")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(160, 20, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(520, 20, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(440, 70, 61, 20))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(440, 100, 61, 20))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(440, 140, 61, 20))
        self.label_10.setObjectName("label_10")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_4.setGeometry(QtCore.QRect(520, 70, 255, 25))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(520, 100, 255, 25))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_6.setGeometry(QtCore.QRect(520, 140, 255, 25))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(440, 180, 89, 25))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(686, 180, 89, 25))
        self.pushButton_3.setObjectName("pushButton_3")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(420, 0, 16, 261))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(0, 260, 801, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(320, 290, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        self.spinBox = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(340, 330, 42, 26))
        self.spinBox.setObjectName("spinBox")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(290, 330, 41, 21))
        self.label_12.setObjectName("label_12")
        self.spinBox_2 = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_2.setGeometry(QtCore.QRect(500, 330, 42, 26))
        self.spinBox_2.setObjectName("spinBox_2")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(470, 330, 21, 21))
        self.label_13.setObjectName("label_13")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(410, 350, 41, 25))
        self.pushButton_4.setObjectName("pushButton_4")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuwindow1 = QtWidgets.QMenu(self.menubar)
        self.menuwindow1.setObjectName("menuwindow1")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionWindow1 = QtWidgets.QAction(MainWindow)
        self.actionWindow1.setObjectName("actionWindow1")
        self.actionWindow2 = QtWidgets.QAction(MainWindow)
        self.actionWindow2.setObjectName("actionWindow2")
        self.actionWindow3 = QtWidgets.QAction(MainWindow)
        self.actionWindow3.setObjectName("actionWindow3")
        self.actionWindow4 = QtWidgets.QAction(MainWindow)
        self.actionWindow4.setObjectName("actionWindow4")
        self.actionWindow5 = QtWidgets.QAction(MainWindow)
        self.actionWindow5.setObjectName("actionWindow5")
        self.menuwindow1.addAction(self.actionWindow1)
        self.menuwindow1.addAction(self.actionWindow2)
        self.menuwindow1.addAction(self.actionWindow3)
        self.menuwindow1.addAction(self.actionWindow4)
        self.menuwindow1.addAction(self.actionWindow5)
        self.menubar.addAction(self.menuwindow1.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.calculate)
        self.pushButton_2.clicked.connect(self.setabcset)
        self.pushButton_3.clicked.connect(self.randomsets)
        self.pushButton_4.clicked.connect(self.set_vers)
        self.actionWindow2.triggered.connect(self.window2)
        self.actionWindow3.triggered.connect(self.window3)
        self.actionWindow4.triggered.connect(self.window4)
        self.actionWindow5.triggered.connect(self.window5)

       
        





    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Enter the number of group:"))
        self.label_3.setText(_translate("MainWindow", "Enter your  number in group:"))
        self.label_3.adjustSize()
        self.label_4.setText(_translate("MainWindow", "Enter the lineral part of group`s name:"))
        self.pushButton.setText(_translate("MainWindow", "Calculate"))
        self.label_5.setText(_translate("MainWindow", "Your variant: "))
        self.label_2.setText(_translate("MainWindow", "None"))
        self.label_6.setText(_translate("MainWindow", "Chosing your variant"))
        self.label_7.setText(_translate("MainWindow", "Setting the power of the set"))
        self.label_8.setText(_translate("MainWindow", "Enter A:"))
        self.label_9.setText(_translate("MainWindow", "Enter B:"))
        self.label_10.setText(_translate("MainWindow", "Enter C:"))
        self.pushButton_2.setText(_translate("MainWindow", "Enter"))
        self.pushButton_3.setText(_translate("MainWindow", "Random"))
        self.label_11.setText(_translate("MainWindow", "Setting the versatile set"))
        self.label_12.setText(_translate("MainWindow", "From"))
        self.label_13.setText(_translate("MainWindow", "to"))
        self.pushButton_4.setText(_translate("MainWindow", "Set"))
        self.menuwindow1.setTitle(_translate("MainWindow", "Choose"))
        self.actionWindow1.setText(_translate("MainWindow", "Window1"))
        self.actionWindow1.setStatusTip(_translate("MainWindow", "Open window 1"))
        self.actionWindow1.setShortcut(_translate("MainWindow", "W, 1"))
        self.actionWindow2.setText(_translate("MainWindow", "Window2"))
        self.actionWindow2.setStatusTip(_translate("MainWindow", "Open window 2"))
        self.actionWindow2.setShortcut(_translate("MainWindow", "W, 2"))
        self.actionWindow3.setText(_translate("MainWindow", "Window3"))
        self.actionWindow3.setStatusTip(_translate("MainWindow", "Open window 3"))
        self.actionWindow3.setShortcut(_translate("MainWindow", "W, 3"))
        self.actionWindow4.setText(_translate("MainWindow", "Window4"))
        self.actionWindow4.setStatusTip(_translate("MainWindow", "Open window 4"))
        self.actionWindow4.setShortcut(_translate("MainWindow", "W, 4"))
        self.actionWindow5.setText(_translate("MainWindow", "Window5"))
        self.actionWindow5.setStatusTip(_translate("MainWindow", "Open window 5"))
        self.actionWindow5.setShortcut(_translate("MainWindow", "W, 5"))

       
        

    def calculate(self):
        G=int(self.lineEdit.text())
        N=int(self.lineEdit_2.text())
        M=self.lineEdit_3.text()
        if M=="ІО": N+=2
        self.label_2.setText("Мій варіант:"+str((N+G%60)%30+1))
    
    def setabcset(self):
        A = []
        B = []
        C = []
        for i in self.lineEdit_4.text().split():
            A.append(int(i))    
        for i in self.lineEdit_5.text().split():
            B.append(int(i)) 
        for i in self.lineEdit_6.text().split():
            C.append(int(i))  
        A = set(A)
        B = set(B)
        C = set(C)
        self.A = A
        self.B = B
        self.C = C
    
    def randomsets(self):
        random.seed()
        sizA = random.randint(1,20)
        sizB = random.randint(1,20)
        sizC = random.randint(1,20)
        A = set()
        B = set()
        C = set()
        for i in range(sizA):
            num = random.randint(1,30)
            A.add(num)
        for i in range(sizB):
            num = random.randint(1,30)
            B.add(num)
        for i in range(sizC):
            num = random.randint(1,30)
            C.add(num)
        self.A = A
        self.B = B
        self.C = C

    def set_vers(self):
            vers_set = set()
            for i in range(self.spinBox.value(),self.spinBox_2.value()+1):
                vers_set.add(i)
            self.vers_set = vers_set

    def window2(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Window2()
        self.ui.setupUi(self.window)
        Ui_Window2.A = self.A
        Ui_Window2.B = self.B
        Ui_Window2.C = self.C
        Ui_Window2.vers_set = self.vers_set
        self.window.show()
    
    def window3(self):
        self.window1 = QtWidgets.QMainWindow()
        self.ui = Ui_Window3()
        self.ui.setupUi(self.window1)
        Ui_Window3.A = self.A
        Ui_Window3.B = self.B
        Ui_Window3.C = self.C
        Ui_Window3.vers_set = self.vers_set
        self.window1.show()

    def window4(self):
        self.window2 = QtWidgets.QMainWindow()
        self.ui = Ui_Window4()
        self.ui.setupUi(self.window2)
        Ui_Window4.X = self.C
        Ui_Window4.Y = self.B
        self.window2.show()

    def window5(self):
        self.window3 = QtWidgets.QMainWindow()
        self.ui = Ui_Window5()
        self.ui.setupUi(self.window3)
        Ui_Window5.X = self.C
        Ui_Window5.Y = self.B
        self.window3.show()
        


  

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
