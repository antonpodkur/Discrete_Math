from PyQt5 import QtCore, QtGui, QtWidgets
import random
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
import networkx as nx
import matplotlib.pyplot as plt


class Ui_MainWindow2(object):
    nodes_amount = 0
    final_list = list()
    flag = True
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(924, 751)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(160, 80, 621, 611))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(370, 20, 171, 41))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        print(self.nodes_amount)
        print(self.final_list)
        print()

        self.position = {1:[1,4],2:[2,4],3:[3,4],4:[1.5,3],5:[2.5,3],6:[1,2],7:[2,2],8:[3,2],9:[1.5,1],10:[2.5,1]}


        self.nodes = list(range(1,self.nodes_amount+1))

        

        self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        self.gridLayout.addWidget(self.canvas, 0, 0, 0, 0)

        if self.flag:
            self.g = nx.Graph()
            self.g.add_nodes_from(self.nodes)
            nx.draw(self.g,pos= nx.shell_layout(self.g), with_labels=True, font_weight='bold')
            nx.draw_networkx_edges(self.g, pos= nx.shell_layout(self.g), edgelist=self.final_list, edge_color='black', with_labels=True)

        else:
            self.g = nx.Graph()
            self.g.add_nodes_from(self.nodes)
            nx.draw(self.g,pos= self.position, with_labels=True, font_weight='bold')
            nx.draw_networkx_edges(self.g, pos= self.position, edgelist=self.final_list, edge_color='black', with_labels=True)


        self.n = self.nodes_amount
        self.curcol = 1
        self.colarr = [0 for i in range(self.n)]

        self.a = [[0 for i in range(self.n)] for j in range(self.n)]
        for i in self.final_list:
            self.a[i[0]-1][i[1]-1] = 1
       

        ####### Функція формування списку упорядкованих степенів ########
        def degforming():
            def getkey(item):
                return item[0]
            def degcount(d): #степень вкршини d
                degnum=0
                for k in range(self.n):
                    degnum += self.a[k][d]
                return degnum
            degarr=[[0 for i in range(2)] for j in range(self.n)]
            # Формування degarr
            for j in range(self.n):
                degarr[j][0]=degcount(j)*100
                degarr[j][1] = j
                for i in range(self.n):
                    if self.a[i][j]==1:
                        degarr[j][0]+=degcount(i)
            # Сортування за спаданням степенів
            degarr.sort(key=getkey, reverse=True)
            return degarr

        
        def dyer(i):
            for j in range(self.n):
                if self.a[j][i] == 0 and self.colarr[j] == 0 and CheckDop(j):
                    self.colarr[j]= self.curcol

        def CheckDop(k): # Функція перевірки кольору суміжних вершин при поточному розфарбуванні
            p=True
            for j in range(0, self.n):
                if self.a[j][k]==1 and self.colarr[j]== self.curcol: p=False
            return p

        def main():
            self.sortarr=degforming()
            for i in range(self.n):
                if not self.colarr[self.sortarr[i][1]]:
                    self.colarr[self.sortarr[i][1]]=self.curcol
                    dyer(self.sortarr[i][1])
                    self.curcol+=1 
            # for r in range(self.n):
            #     print(self.a[r])
            #print(self.sortarr)
            print(self.colarr)

            self.figure = plt.figure()
            self.canvas = FigureCanvas(self.figure)
            self.gridLayout.addWidget(self.canvas, 0, 0, 0, 0)

            if self.flag:
                self.g = nx.Graph()
                self.g.add_nodes_from(self.nodes)
                nx.draw(self.g,pos= nx.shell_layout(self.g),node_color=self.colarr, with_labels=True, font_weight='bold')
                nx.draw_networkx_edges(self.g, pos= nx.shell_layout(self.g), edgelist=self.final_list, edge_color='black', with_labels=True)

            else:
                self.g = nx.Graph()
                self.g.add_nodes_from(self.nodes)
                nx.draw(self.g,pos= self.position,node_color=self.colarr, with_labels=True, font_weight='bold')
                nx.draw_networkx_edges(self.g, pos= self.position, edgelist=self.final_list, edge_color='black', with_labels=True)

                


         
        self.pushButton.clicked.connect(main)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Розфарбувати"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow2()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
