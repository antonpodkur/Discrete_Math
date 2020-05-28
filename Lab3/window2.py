
from PyQt5 import QtCore, QtGui, QtWidgets
import random
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import networkx as nx
import matplotlib.pyplot as plt

class Ui_MainWindow_2(object):
    nodes = 0
    avaible_nodes = list()
    adj = dict()
    contacts=list()
    edges_list=list()

    answer_edges=list()
    shortway = list()
    final_edges = list()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(402, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(20, 10, 361, 231))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_2 = QtWidgets.QLabel(self.frame_2)
        self.label_2.setGeometry(QtCore.QRect(10, 20, 341, 81))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(30, 110, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.frame_2)
        self.label_4.setGeometry(QtCore.QRect(30, 160, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.spinBox = QtWidgets.QSpinBox(self.frame_2)
        self.spinBox.setGeometry(QtCore.QRect(130, 110, 42, 25))
        self.spinBox.setObjectName("spinBox")
        self.spinBox_2 = QtWidgets.QSpinBox(self.frame_2)
        self.spinBox_2.setGeometry(QtCore.QRect(130, 160, 42, 25))
        self.spinBox_2.setObjectName("spinBox_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_3.setGeometry(QtCore.QRect(210, 130, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 250, 361, 301))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.msg = QtWidgets.QMessageBox()
        self.msg.setWindowTitle("Error")
        self.msg.setText("There is no way")
        self.msg.setIcon(QtWidgets.QMessageBox.Critical)
        self.msg.setStandardButtons(QtWidgets.QMessageBox.Ok)
        self.msg.setDefaultButton(QtWidgets.QMessageBox.Ok)

        self.avaible_nodes = list(range(1,self.nodes+1))

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.gridLayout.addWidget(self.canvas, 0, 0, 0, 0)

        for i in range(len(self.avaible_nodes)):
            random.seed()
            num1 = random.randint(1,3)
            temp = list()
            for j in range(num1):
                num2 = random.randint(1,len(self.avaible_nodes))
                if self.avaible_nodes[i] != num2:
                    if num2 not in temp:
                        temp.append(num2)
                        self.contacts.append([i+1, num2])
            self.adj.update({int(i+1):set(temp)})
        print(self.adj)
        for i in self.contacts:
            if i[0] != i[1]:
                self.edges_list.append(i)
                    
        self.g = nx.DiGraph()
        self.g.add_nodes_from(self.avaible_nodes)
        self.g.add_edges_from(self.edges_list)
        nx.draw(self.g,pos=nx.shell_layout(self.g), with_labels=True, font_weight='bold')

        print(self.edges_list)

        #SEARCHING FOR THE WAYS
        def dfs_paths(adj, start, goal):
            stack = [(int(start), [int(start)])]
            while stack:
                (vertex, path) = stack.pop()
                for next in adj[vertex] - set(path):
                    if next == goal:
                        self.answer_edges.append(path + [next])
                        #yield path + [next]
                    else:
                        stack.append((next, path + [next]))
                
       

        def run():
            dfs_paths(self.adj,int(self.spinBox.value()),int(self.spinBox_2.value()))

 


            self.shortway=self.answer_edges[0]

            for i in self.answer_edges:
                if len(i)<len(self.shortway):
                    self.shortway = i


            last = False

            for i in self.shortway:
                if int(self.spinBox_2.value()) in self.shortway:
                    last = True

            for i in range(len(self.shortway)-1):
                self.final_edges.append([self.shortway[i],self.shortway[i+1]])

            self.edges_list1 = list()
            
            for i in self.edges_list:
                if i not in self.final_edges:
                    self.edges_list1.append(i)



            if last:
                self.figure = plt.figure()
                self.canvas = FigureCanvas(self.figure)
                self.gridLayout.addWidget(self.canvas, 0, 0, 0, 0)


                self.g = nx.DiGraph()
                self.g.add_nodes_from(self.avaible_nodes)
                nx.draw(self.g,pos=nx.shell_layout(self.g), with_labels=True, font_weight='bold')
                nx.draw_networkx_edges(self.g, pos=nx.shell_layout(self.g), edgelist=self.final_edges, edge_color='r', with_labels=True)
                nx.draw_networkx_edges(self.g, pos=nx.shell_layout(self.g), edgelist=self.edges_list1, edge_color='b', with_labels=True)
            else:
                x = self.msg.exec_()




        self.pushButton_3.clicked.connect(run)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_2.setText(_translate("MainWindow", "Визначити найкоротший шлях\n"
" між вершинами:"))
        self.label_3.setText(_translate("MainWindow", "Початок"))
        self.label_4.setText(_translate("MainWindow", "Кінець"))
        self.pushButton_3.setText(_translate("MainWindow", "Визначити"))

