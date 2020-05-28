from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow_2(object):
    men = set()
    women = set()

    set_A = list()

    set_B = list()
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(886, 572)
        MainWindow.setWindowTitle("Window 2")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(30, 50, 256, 192))
        self.listWidget.setObjectName("listWidget")
        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(30, 300, 256, 192))
        self.listWidget_2.setObjectName("listWidget_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 20, 201, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 270, 171, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.radioButton = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton.setGeometry(QtCore.QRect(350, 240, 98, 21))
        self.radioButton.setObjectName("radioButton")
        self.radioButton.setChecked(True)
        self.radioButton_2 = QtWidgets.QRadioButton(self.centralwidget)
        self.radioButton_2.setGeometry(QtCore.QRect(350, 270, 98, 21))
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_2.setChecked(False)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(350, 190, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.listWidget_3 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_3.setGeometry(QtCore.QRect(480, 50, 256, 192))
        self.listWidget_3.setObjectName("listWidget_3")
        self.listWidget_4 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_4.setGeometry(QtCore.QRect(480, 300, 256, 192))
        self.listWidget_4.setObjectName("listWidget_4")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(580, 20, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(590, 270, 51, 20))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(770, 80, 84, 33))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(770, 120, 84, 33))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(770, 160, 84, 33))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(770, 340, 84, 33))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(770, 380, 84, 33))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(770, 420, 84, 33))
        self.pushButton_6.setObjectName("pushButton_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        names_men =("Борис,Василь,Максим,Іван,Аркадій,Артем,Петро").split(",")
        for i in names_men:
            self.men.add(i)

        names_women = ("Антоніна,Оксана,Галина,Ольга,Світлана,Тетяна,Катерина").split(",")
        for i in names_women:
            self.women.add(i)

#########   Creating the mens objects for list widget  ################
        Borys = QtWidgets.QListWidgetItem("Борис")
        self.listWidget.addItem(Borys)
        Vasyl = QtWidgets.QListWidgetItem("Василь")
        self.listWidget.addItem(Vasyl)
        Maksym = QtWidgets.QListWidgetItem("Максим")
        self.listWidget.addItem(Maksym)
        Ivan = QtWidgets.QListWidgetItem("Іван")
        self.listWidget.addItem(Ivan)
        Arkadiy = QtWidgets.QListWidgetItem("Аркадій")
        self.listWidget.addItem(Arkadiy)
        Artem = QtWidgets.QListWidgetItem("Артем")
        self.listWidget.addItem(Artem)
        Petro = QtWidgets.QListWidgetItem("Петро")
        self.listWidget.addItem(Petro)


#########   Creating the womens objects for list widget  ################
        Antonina = QtWidgets.QListWidgetItem("Антоніна")
        self.listWidget_2.addItem(Antonina)
        Oksana = QtWidgets.QListWidgetItem("Оксана")
        self.listWidget_2.addItem(Oksana)
        Galyna = QtWidgets.QListWidgetItem("Галина")
        self.listWidget_2.addItem(Galyna)
        Olga = QtWidgets.QListWidgetItem("Ольга")
        self.listWidget_2.addItem(Olga)
        Svitlana = QtWidgets.QListWidgetItem("Світлана")
        self.listWidget_2.addItem(Svitlana)
        Tetyana = QtWidgets.QListWidgetItem("Тетяна")
        self.listWidget_2.addItem(Tetyana)
        Kateryna = QtWidgets.QListWidgetItem("Катерина")
        self.listWidget_2.addItem(Kateryna)


        def itemActivated_event_1():
            item1 = self.listWidget.currentItem()
            value1 = item1.text()
            print(value1)
            if self.radioButton.isChecked():
                self.listWidget_3.addItem(value1)
                self.set_A.append(value1)
            elif self.radioButton_2.isChecked():
                    self.listWidget_4.addItem(value1)
                    self.set_B.append(value1)

        def itemActivated_event_2():
            item2 = self.listWidget_2.currentItem()
            value2 = item2.text()
            print(value2)
            if self.radioButton.isChecked():
                self.listWidget_3.addItem(value2)
                self.set_A.append(value2)
            elif self.radioButton_2.isChecked():
                    self.listWidget_4.addItem(value2)
                    self.set_B.append(value2)

                    print(self.set_A,"\n", self.set_B)    


        self.listWidget.itemActivated.connect(itemActivated_event_1)
        self.listWidget_2.itemActivated.connect(itemActivated_event_2)

        def savedAction_A():
            with open("saved_A.txt","w+") as f:
                for i in self.set_A:
                    f.write(i + ",")

        def savedAction_B():
            with open("saved_B.txt","w+") as f:
                for i in self.set_B:
                    f.write(i + ",")

        def readAction_A():
            with open("load_A.txt","r+") as f:
                data = f.read().split(" ")
                self.set_A.clear()
                self.listWidget_3.clear()
                for i in data:
                    self.set_A.append(i)
                    self.listWidget_3.addItem(i)

        def readAction_B():
            with open("load_B.txt","r+") as f:
                data = f.read().split(" ")
                self.set_B.clear()
                self.listWidget_4.clear()
                for i in data:
                    self.set_B.append(i)
                    self.listWidget_4.addItem(i)

        def clearAction_A():
            self.set_A.clear()
            self.listWidget_3.clear()

        def clearAction_B():
            self.set_B.clear()
            self.listWidget_4.clear()


        self.pushButton.clicked.connect(savedAction_A)
        self.pushButton_4.clicked.connect(savedAction_B)

        self.pushButton_2.clicked.connect(readAction_A)
        self.pushButton_5.clicked.connect(readAction_B)

        self.pushButton_3.clicked.connect(clearAction_A)
        self.pushButton_6.clicked.connect(clearAction_B)
       
            

        

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Set of female names"))
        self.label.adjustSize()
        self.label_2.setText(_translate("MainWindow", "Set of male names"))
        self.label_2.adjustSize()
        self.radioButton.setText(_translate("MainWindow", "A"))
        self.radioButton_2.setText(_translate("MainWindow", "B"))
        self.label_3.setText(_translate("MainWindow", "Add to set:"))
        self.label_3.adjustSize()
        self.label_4.setText(_translate("MainWindow", "Set A"))
        self.label_4.adjustSize()
        self.label_5.setText(_translate("MainWindow", "Set B"))
        self.label_5.adjustSize()
        self.pushButton.setText(_translate("MainWindow", "Save"))
        self.pushButton_2.setText(_translate("MainWindow", "Read"))
        self.pushButton_3.setText(_translate("MainWindow", "Clear"))
        self.pushButton_4.setText(_translate("MainWindow", "Save"))
        self.pushButton_5.setText(_translate("MainWindow", "Read"))
        self.pushButton_6.setText(_translate("MainWindow", "Clear"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow_2()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())

