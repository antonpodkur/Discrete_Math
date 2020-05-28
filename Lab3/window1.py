from PyQt5 import QtCore, QtGui, QtWidgets
from window2 import Ui_MainWindow_2


class Ui_MainWindow(object):
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
        self.frame_3.setGeometry(QtCore.QRect(250, 20, 411, 151))
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_6 = QtWidgets.QLabel(self.frame_3)
        self.label_6.setGeometry(QtCore.QRect(130, 10, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setUnderline(True)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.frame_3)
        self.label_7.setGeometry(QtCore.QRect(110, 60, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.spinBox = QtWidgets.QSpinBox(self.frame_3)
        self.spinBox.setGeometry(QtCore.QRect(280, 70, 42, 25))
        self.spinBox.setObjectName("spinBox")
        self.pushButton = QtWidgets.QPushButton(self.frame_3)
        self.pushButton.setGeometry(QtCore.QRect(160, 110, 80, 24))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        def window2():
            Ui_MainWindow_2.nodes = self.spinBox.value()
            # app = QtWidgets.QApplication(sys.argv)
            self.window2 = QtWidgets.QMainWindow()
            self.ui_2 = Ui_MainWindow_2()
            self.ui_2.setupUi(self.window2)
            self.window2.setWindowTitle("Вікно 2")
            self.window2.show()

        self.pushButton.clicked.connect(window2)


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_3.setText(_translate("MainWindow", "Інформація"))
        self.label.setText(_translate("MainWindow", "Подкур Антон ІВ-92"))
        self.label_2.setText(_translate("MainWindow", "18 номер у списку"))
        self.label_5.setText(_translate("MainWindow", "1. Розглянути алгоритм пошуку шляхів у глибину та написати програму пошуку\n \
найкоротших шляхів у графі за цим алгоритмом.\n\
2. Знайти найкоротший шлях між вершинами, номери яких задані викладачем.\n\
3. Представити граф у графічній формі та виділити найкоротший шлях,\n\
сформований за алгоритмом пошуку в глибину."))
        self.label_4.setText(_translate("MainWindow", "Завдання: 9 варіант"))
        self.label_4.adjustSize()
        self.label_6.setText(_translate("MainWindow", "Створити граф"))
        self.label_7.setText(_translate("MainWindow", "Кількість вершин:"))
        self.pushButton.setText(_translate("MainWindow", "Створити"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.setWindowTitle("Вікно 1")
    MainWindow.show()
    sys.exit(app.exec_())