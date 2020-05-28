from PyQt5 import QtCore, QtGui, QtWidgets
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import networkx as nx
import matplotlib.pyplot as plt


class Ui_MainWindow_4(object):
    set_A = list()
    set_B = list()
    set_S = list()
    set_R = list()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1226, 881)
        MainWindow.setWindowTitle("Window 4")
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 110, 371, 271))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(430, 110, 371, 271))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(830, 110, 371, 271))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(210, 500, 371, 271))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(640, 500, 371, 271))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(500, 400, 201, 81))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        def operations():

            #####Union######
            self.United = list()
            for i in self.set_S:
                self.United.append(i)
            for i in self.set_R:
                if i not in self.United:
                    self.United.append(i)

            self.figure = plt.figure()
            self.figure.suptitle('S⋃R', fontsize=20)
            self.canvas = FigureCanvas(self.figure)
            self.gridLayout.addWidget(self.canvas, 0, 0, 0, 0)

            
            self.g1 = nx.DiGraph()
            tmp = 3
            for n in self.set_A:
                self.g1.add_node(n, pos=(tmp, 2))
                tmp += 3
            tmp = 3
            for n in self.set_B:
                self.g1.add_node(n, pos=(tmp, 1))
                tmp += 3
            self.g1.add_edges_from(self.United)
            pos = nx.get_node_attributes(self.g1,'pos')
            nx.draw_networkx(self.g1, pos=pos, arrows=True, with_labels=True, edges=self.g1.edges(), edge_color="b")


            #####Intersection######
            self.Intersection = list()
            for i in self.set_R:
                for j in self.set_S:
                    if i == j:
                        self.Intersection.append(i)

            self.figure_2 = plt.figure()
            self.figure_2.suptitle('R⋂S', fontsize=20)
            self.canvas_2 = FigureCanvas(self.figure_2)
            self.gridLayout_2.addWidget(self.canvas_2, 0, 0, 0, 0)

            self.g2 = nx.DiGraph()
            tmp = 3
            for n in self.set_A:
                self.g2.add_node(n, pos=(tmp, 2))
                tmp += 3
            tmp = 3
            for n in self.set_B:
                self.g2.add_node(n, pos=(tmp, 1))
                tmp += 3
            self.g2.add_edges_from(self.Intersection)
            pos = nx.get_node_attributes(self.g2,'pos')
            nx.draw_networkx(self.g2, pos=pos, arrows=True, with_labels=True, edges=self.g2.edges(), edge_color="b")


            ########Subtraction############
            self.Subs = list()

            for i in self.set_R:
                if i in self.Intersection:
                    pass
                else: self.Subs.append(i)

            print("Subs",self.Subs)

            self.figure_3 = plt.figure()
            self.figure_3.suptitle('R\S', fontsize=20)
            self.canvas_3 = FigureCanvas(self.figure_3)
            self.gridLayout_3.addWidget(self.canvas_3, 0, 0, 0, 0)

            self.g3 = nx.DiGraph()
            tmp = 3
            for n in self.set_A:
                self.g3.add_node(n, pos=(tmp, 2))
                tmp += 3
            tmp = 3
            for n in self.set_B:
                self.g3.add_node(n, pos=(tmp, 1))
                tmp += 3
            self.g3.add_edges_from(self.Subs)
            pos = nx.get_node_attributes(self.g3,'pos')
            nx.draw_networkx(self.g3, pos=pos, arrows=True, with_labels=True, edges=self.g3.edges(), edge_color="b")


            ########R+#################
            self.Rplus = list()
            self.Vers = list()
            for a in self.set_A:
                for b in self.set_B:
                    if [a,b] not in self.Vers:
                        self.Vers.append([a,b])
                
            for i in self.Vers:
                if i not in self.set_R:
                    self.Rplus.append(i) 

            self.figure_4 = plt.figure()
            self.figure_4.suptitle('U\R', fontsize=20)
            self.canvas_4 = FigureCanvas(self.figure_4)
            self.gridLayout_4.addWidget(self.canvas_4, 0, 0, 0, 0)

            self.g4 = nx.DiGraph()
            tmp = 3
            for n in self.set_A:
                self.g4.add_node(n, pos=(tmp, 2))
                tmp += 3
            tmp = 3
            for n in self.set_B:
                self.g4.add_node(n, pos=(tmp, 1))
                tmp += 3
            self.g4.add_edges_from(self.Rplus)
            pos = nx.get_node_attributes(self.g4,'pos')
            nx.draw_networkx(self.g4, pos=pos, arrows=True, with_labels=True, edges=self.g4.edges(), edge_color="b")

            ######Opposite_S###############
            self.Reverse_S = list()
            for i in self.set_S:
                self.Reverse_S.append([i[1],i[0]])

            self.figure_5 = plt.figure()
            self.figure_5.suptitle('S^-1', fontsize=20)
            self.canvas_5 = FigureCanvas(self.figure_5)
            self.gridLayout_5.addWidget(self.canvas_5, 0, 0, 0, 0)

            self.g5 = nx.DiGraph()
            tmp = 3
            for n in self.set_A:
                self.g5.add_node(n, pos=(tmp, 2))
                tmp += 3
            tmp = 3
            for n in self.set_B:
                self.g5.add_node(n, pos=(tmp, 1))
                tmp += 3
            self.g5.add_edges_from(self.Reverse_S)
            pos = nx.get_node_attributes(self.g5,'pos')
            nx.draw_networkx(self.g5, pos=pos, arrows=True, with_labels=True, edges=self.g5.edges(), edge_color="b")



        self.pushButton.clicked.connect(operations)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Show graphs"))
        #self.pushButton.adjustSize()



