from PyQt5 import QtCore, QtGui, QtWidgets
from random import sample, randint, shuffle
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import networkx as nx
import matplotlib.pyplot as plt



class Ui_MainWindow_3(object):
    set_A =list()
    set_B = list()
    men = list()
    women = list()


    set_R = list()
    set_S = list()


    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1057, 886)
        MainWindow.setWindowTitle("Window 3")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.listWidget = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget.setGeometry(QtCore.QRect(50, 60, 241, 341))
        self.listWidget.setObjectName("listWidget")
        self.listWidget_2 = QtWidgets.QListWidget(self.centralwidget)
        self.listWidget_2.setGeometry(QtCore.QRect(50, 480, 241, 341))
        self.listWidget_2.setObjectName("listWidget_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(140, 20, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(140, 430, 71, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(310, 400, 171, 81))
        MainWindow.setCentralWidget(self.centralwidget)

##############CANVAS 1
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(490, 40, 551, 381))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")

        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")

        
##############CANVAS 2
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(490, 450, 551, 381))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")

        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")

        


        # self.label_3 = QtWidgets.QLabel(self.centralwidget)
        # self.label_3.setGeometry(QtCore.QRect(490, 40, 551, 381))
        # self.label_3.setObjectName("label_3")
        # self.label_4 = QtWidgets.QLabel(self.centralwidget)
        # self.label_4.setGeometry(QtCore.QRect(490, 450, 551, 381))
        # self.label_4.setObjectName("label_4")
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


        for i in self.set_A:
            self.listWidget.addItem(i)

        for i in self.set_B:
            self.listWidget_2.addItem(i)

        def relation():
            
            self.figure = plt.figure()
            self.figure.suptitle('S graph', fontsize=20)
            self.canvas = FigureCanvas(self.figure)
            self.gridLayout.addWidget(self.canvas, 0, 0, 0, 0)

            temp_s = list()

            for a in sample(self.set_A,randint(len(self.set_A)//2, len(self.set_A))):
                num = randint(1,3)
                for b in sample(self.set_B, num):
                    if a in self.women:
                        s= True
                        for i in temp_s:
                            if b in i[1]:
                                s=False                         
                        if(s):
                            temp_s.append([a,b])

            for i in temp_s:
                self.set_S.append(i)
            self.g1 = nx.DiGraph()
            tmp = 3
            for n in self.set_A:
                self.g1.add_node(n, pos=(tmp, 2))
                tmp += 3
            tmp = 3
            for n in self.set_B:
                self.g1.add_node(n, pos=(tmp, 1))
                tmp += 3
            self.g1.add_edges_from(self.set_S)
            pos = nx.get_node_attributes(self.g1,'pos')
            nx.draw_networkx(self.g1, pos=pos, arrows=True, with_labels=True, edges=self.g1.edges(), edge_color="b")
            #self.canvas.draw()

            print("S..................")                
            print(self.set_S)

            print("R.................")


            self.figure_2 = plt.figure()
            self.figure_2.suptitle('R graph', fontsize=20)
            self.canvas_2 = FigureCanvas(self.figure_2)
            self.gridLayout_2.addWidget(self.canvas_2, 0, 0, 0, 0)

        
            temp_r = list()

            for a in sample(self.set_A,randint(len(self.set_A)//2, len(self.set_A))):
                num = randint(1,3)
                for b in sample(self.set_B, num):
                    if a in self.women:
                        for i in self.set_S:
                            if b in i and [a,b] not in self.set_S:
                                #pass
                                temp_r.append([a,i[0]])
                                # temp_r.append([a,i[1]])
                            if (b in self.men) and ([a,b] not in self.set_S) and ([b,a] not in self.set_S):
                                temp_r.append([a,b])

            
            for i in temp_r:
                self.set_R.append(i)
            print(self.set_R)
            self.g2 = nx.DiGraph()
            tmp = 3
            for n in self.set_A:
                self.g2.add_node(n, pos=(tmp, 2))
                tmp += 3
            tmp = 3
            for n in self.set_B:
                self.g2.add_node(n, pos=(tmp, 1))
                tmp += 3
            self.g2.add_edges_from(self.set_R)
            pos = nx.get_node_attributes(self.g2,'pos')
            nx.draw_networkx(self.g2, pos=pos, arrows=True, with_labels=True, edges=self.g2.edges(), edge_color="b")
            
            print("before exit")
            print(self.set_R)
            print(self.set_S)

            
        
        self.pushButton.clicked.connect(relation)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "set A"))
        self.label.adjustSize()
        self.label_2.setText(_translate("MainWindow", "set B"))
        self.label_2.adjustSize()
        self.pushButton.setText(_translate("MainWindow", "Get relation"))


