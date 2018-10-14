#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#--------------------------------
# Packages needed
#Matplotlib
#Python3
#PyQt5
#
#------------------------------------------------------------
# Files needed:
# Cabinet_GUI
# Outlet_1
# Outlet_2
# Outlet_1_DataPlots
# Outlet_2_DataPlots
#
# Written by Luis Martinez : luizmartines@gmail.com
#                          : luizm929@nmsu.edu
# Thanks to Jose Tabarez for his help.


import sys
import time
import os
import datetime
import socket
from time import sleep
#from Queue import Queue
import threading
from PyQt5.QtWidgets import (QSizePolicy, QGridLayout)
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from Outlet_1 import *
from Outlet_2 import *
# icon size
x = 100
y = 90

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
#from get_time import get_time_func

# One canvas for all plots this is why plots update
# with a bit of latency in the milli seconds. We want less latency we create
# one class for each plot with the risk of using more memory.
# TODO
# Create classes for all the houses so there is less latency.
class mplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)

        # we clear the screen otherwise we run out of memory.
        #self.axes.hold(False)

        self.compute_initial_figure()

        #
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)
        # TODO change expanding to Fixed to avoid zooming in of plot
        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Expanding,
                                   QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    #def compute_initial_figure(self):
    #    pass


#############################################################
# Each plot has one of these.
# Outlet 1

class dynPlot1(mplCanvas):

    def __init__(self, *args, **kwargs):
        mplCanvas.__init__(self, *args, **kwargs)
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.update_figure)
        timer.start(1000)

    def compute_initial_figure(self):
        self.axes.plot([0, 1, 2, 3], [0, 1, 2, 3], 'r')
        self.axes.plot(x, y, 'r', color='black', label='Power (W)')
        self.axes.plot(y, 'r', color='red', label='Schedule (SCH)')
        self.axes.set_xlabel('Time (s)')
        self.axes.set_ylabel('Power (W)')
        ###Legend on plot
        self.axes.legend(loc='upper left')

    def update_figure(self):
        ###########################
        # C_dir = os.getcwd()
        # f = open(C_dir + '\Files\\' + 'outlet001.txt', 'r')
        # d = f.readlines()
        # f.close()
        # x = []
        # y = []
        # for i in range(len(d)):
        #     hold = d[i].split(',')
        #
        #     x.append(float(hold[0]))
        #     y.append(float(hold[1]))

        # self.axes.plot(x, y, 'r', color='black', label='Power (W)')
        # self.axes.plot(y, 'r', color='red', label='Schedule (SCH)')
        # self.axes.set_xlabel('Time (s)')
        # self.axes.set_ylabel('Power (W)')
        # ###Legend on plot
        # self.axes.legend(loc='upper left')

        self.draw()


# Outlet 2
class dynPlot2(mplCanvas):
    def __init__(self, *args, **kwargs):
        mplCanvas.__init__(self, *args, **kwargs)
        timer = QtCore.QTimer(self)
        timer.timeout.connect(self.update_figure)
        timer.start(1000)

    def compute_initial_figure(self):
        self.axes.plot([0, 1, 2, 3], [0, 1, 2, 3], 'r')
        self.axes.plot(x, y, 'r', color='black', label='Power (W)')
        self.axes.plot(y, 'r', color='red', label='Schedule (SCH)')
        self.axes.set_xlabel('Time (s)')
        self.axes.set_ylabel('Power (W)')
        ###Legend on plot
        self.axes.legend(loc='upper left')

    def update_figure(self):
        # C_dir = os.getcwd()
        #
        # f = open(C_dir + '\Files\\' + 'outlet002.txt', 'r')
        #
        # d = f.readlines()
        # f.close()
        # x = []
        # y = []
        # for i in range(len(d)):
        #     hold = d[i].split(',')
        #
        #     x.append(float(hold[0]))
        #     y.append(float(hold[1]))

        self.axes.plot(x, y, 'r')
        self.draw()


####################################################################################

# The GUI class starts here.
class Ui_MainWindow(QtWidgets.QWidget):
    def __init__(self):
        super(Ui_MainWindow, self).__init__()


    def home1(self):
        self.Outlet_1 = QtWidgets.QMainWindow()
        self.ui = Ui_InOutlet_1_Window()
        self.ui.setupUi(self.Outlet_1)
        # w.hide() # this hides the previous window after the new window opens
        self.Outlet_1.show()
        #w.hide()# this hides the previous window after the new window opens
        #print("Outlet 1 clicked")

    def home2(self):
        self.Outlet_2 = QtWidgets.QMainWindow()
        self.ui = Ui_InOutlet_2_Window()
        self.ui.setupUi(self.Outlet_2)
        # w.hide()# this hides the previous window after the new window opens
        self.Outlet_2.show()
        #w.hide()# this hides the previous window after the new window opens
        #print("Outlet 2 clicked")

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("Window")
        MainWindow.resize(1108, 672)
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet("background-color: rgb(211, 211, 211);")
        MainWindow.setIconSize(QtCore.QSize(40, 40))
        ##########################Create plot widgets######
        ##Maximize window
        # MainWindow.showMaximized()
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        ##This is where the embedded widgets which hold the live plots live. If
        ##there are performance issues we will use pyqtgraph which is suppossed
        ##to be built for perfomrance
        # This is we call the canvas and put it in the main gui(or centralwidget).
        self.PowPlotHouse1 = QtWidgets.QWidget(self.centralwidget)
        self.PowPlotHouse2 = QtWidgets.QWidget(self.centralwidget)

        # Create the layout horizontally of the plots above
        # if we want a vertical layout QVBoxLayout()
        # We create one instance of the grid layout and use it throughout
        layout = QGridLayout()

        # We call the function with the plot or idata to create the plot
        power = dynPlot1(self.PowPlotHouse1)
        #power = dynPlot1(self.PowPlotHouse1, width=2, height=1, dpi=80)
        power2 = dynPlot2(self.PowPlotHouse2, width=2, height=1, dpi=80)

        ##LAYOUT position of widget (row,column)
        layout.addWidget(power, 1, 1)
        layout.addWidget(power2, 1, 3)

        self.PowPlotHouse1.setFocus()
        self.PowPlotHouse2.setFocus()

        ######################End Plot Widget creation###############################
        # TODO
        # Need to work on scroll bars to snap to window when resized.
        """
        ## Vertical Scroll bar
        self.verticalScrollBar = QtWidgets.QScrollBar(self.centralwidget)
        self.verticalScrollBar.setGeometry(QtCore.QRect(0, 0, 21, 611))
        sizePolicy=QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed,QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.verticalScrollBar.sizePolicy().hasHeightForWidth())
        self.verticalScrollBar.setSizePolicy(sizePolicy)
        self.verticalScrollBar.setOrientation(QtCore.Qt.Vertical)
        self.verticalScrollBar.setObjectName("verticalScrollBar")
        ## Horizontal scroll bar
        """
        """
        self.horizontalScrollBar = QtWidgets.QScrollBar(self.centralwidget)
        self.horizontalScrollBar.setGeometry(QtCore.QRect(0, 610, 1051, 16))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalScrollBar.sizePolicy().hasHeightForWidth())
        self.horizontalScrollBar.setSizePolicy(sizePolicy)
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar.setObjectName("horizontalScrollBar")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(900, -30, 151, 141))
        self.label.setStyleSheet("border-image: url(:/img/NM_State_University_logo.png);")
        self.label.setText("")
        self.label.setObjectName("SWTDI Main Window")
        """

        ############################House 1#########################################
        self.house1 = QtWidgets.QPushButton(self.centralwidget)
        self.house1.setGeometry(QtCore.QRect(50, 31, x, y))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.house1.sizePolicy().hasHeightForWidth())
        self.house1.setSizePolicy(sizePolicy)
        self.house1.setAutoFillBackground(False)
        # object house1 is case sensitive stylesheet is also case sensitive.
        self.house1.setObjectName("house1")
        self.house1.setStyleSheet("#house1 {\n"
                                  "border-image: url(:/img/outlet.png);\n"
                                  "font-size: 15px;"
                                  "font-weight: 600;"
                                  "text-align: left,top;"
                                  "}\n"
                                  "#house1:pressed {\n"
                                  "background: white;\n"
                                  "}")

        self.house1.setText("1\n")

        self.house1.clicked.connect(self.home1)
        ## we add this widget to the gridlayout at position (0,0)
        layout.addWidget(self.house1, 0, 0)

        ############################House 2#########################################

        self.house2 = QtWidgets.QPushButton(self.centralwidget)
        # Arguments are ( h, v, x, y)
        # h, v are location, x,y are size arguments
        self.house2.setGeometry(QtCore.QRect(590, 31, x, y))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.house2.sizePolicy().hasHeightForWidth())
        self.house2.setSizePolicy(sizePolicy)
        self.house2.setObjectName("house2")
        self.house2.setStyleSheet("#house2 {\n"
                                  "border-image: url(:/img/outlet.png);\n"
                                  "font-size: 15px;"
                                  "font-weight: 600;"
                                  "text-align: left,top;"
                                  "}\n"
                                  "#house2:pressed {\n"
                                  "background: white;\n"
                                  "}")
        self.house2.setText("2\n")

        ###Button house1
        self.house2.clicked.connect(self.home2)

        layout.addWidget(self.house2, 0, 2)

        # Here we set the size of different rows and columnsof the gridlayout
        # QGridLayout.setRowMinimumHeight (self, int row, int minSize)
        # minSize in pixels
        layout.setRowMinimumHeight(0, 60)
        # QGridLayout.setColumnMinimumWidth (self, int column, int minSize)
        # minSize in pixels
        layout.setColumnMinimumWidth(0, 80)

        # layout.setRowMinimumHeight(0,110)
        layout.setColumnMinimumWidth(2, 80)

        # we could stretch rows,columns but it had undesired results.
        # layout.setColumnStretch(0,1)

        # WE set the layout on the centralwidget as this is the
        # layout of mainwindow
        self.centralwidget.setLayout(layout)
        self.centralwidget.setGeometry(QtCore.QRect(590, 150, 475, 450))
        self.centralwidget.show()

        ######################Plot for house1#######################
        # This is were we embed th plot into the main window.
        """
        self.PowPlotHouse1 = QtWidgets.QWidget(self.centralwidget)

        lay = QVBoxLayout(self.PowPlotHouse1)
        power = dynPlot(self.PowPlotHouse1, width=5, height=4, dpi=100)
        #Location in the GUI of the widget
        self.PowPlotHouse1.setGeometry(QtCore.QRect(86, 30, 171, 121))
        self.PowPlotHouse1.setObjectName("Plot of Power")
        lay.addWidget(power)
        
        self.PowPlotHouse1.setFocus()
        """

        #####################END of widget

        # This is where the whole menu lives
        # Menu entries.
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1108, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuEdit = QtWidgets.QMenu(self.menubar)
        self.menuEdit.setObjectName("menuEdit")
        self.menuOptions = QtWidgets.QMenu(self.menubar)
        self.menuOptions.setObjectName("menuComm")
        self.menuAdmin = QtWidgets.QMenu(self.menubar)
        self.menuAdmin.setObjectName("menuAdmin")
        ####About menu entry
        self.menuAbout = QtWidgets.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")
        ##################################

        # Actions of menu entries
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionResetComms = QtWidgets.QAction(MainWindow)
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_As = QtWidgets.QAction(MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        # Action of menuentries
        self.actionAbout = QtWidgets.QAction(MainWindow)
        self.actionAbout.setObjectName("actionAbout")

        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_As)
        self.menuOptions.addAction(self.actionResetComms)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuOptions.menuAction())
        self.menubar.addAction(self.menuAdmin.menuAction())
        self.menubar.addAction(self.menuAdmin.menuAction())
        ########About
        self.menubar.addAction(self.menuAbout.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Outlets Window", "Cabinet Window"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuEdit.setTitle(_translate("MainWindow", "Edit"))
        self.menuOptions.setTitle(_translate("MainWindow", "Communication"))
        self.actionResetComms.setText(_translate("MainWindow", "Reset All Communications"))
        self.menuAdmin.setTitle(_translate("MainWindow", "Admin"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As"))
        ##########ABOut
        self.actionAbout.setText(_translate("MainWindow", "About"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(w)
    w.show()
    sys.exit(app.exec_())
