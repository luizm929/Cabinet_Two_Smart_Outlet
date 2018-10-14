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

import time
import random
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_InOutlet_1_Window(object):
    def __init__(self):
        super(Ui_InOutlet_1_Window, self).__init__()

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        MainWindow.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # --------------Layout-----------------------
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetMinimumSize)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        # -----------------Power Live Label
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setAlignment(QtCore.Qt.AlignCenter)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_2.addWidget(self.label_8)
        # ---------------Voltage Live Label---------------------
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setAlignment(QtCore.Qt.AlignCenter)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_2.addWidget(self.label_9)
        # -----------------Current Live Label--------------------------
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setAlignment(QtCore.Qt.AlignCenter)
        self.label_10.setObjectName("label_10")
        self.verticalLayout_2.addWidget(self.label_10)
        # ------------------Temp Live Label---------------------
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_2.addWidget(self.label_7)
        # ------------------Reactive Power Live Label ----------
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setAlignment(QtCore.Qt.AlignCenter)
        self.label_11.setObjectName("label_11")
        self.verticalLayout_2.addWidget(self.label_11)
        # ------------------------------------------------------
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.dial = QtWidgets.QDial(self.centralwidget)
        self.dial.setObjectName("dial")
        self.verticalLayout.addWidget(self.dial)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.onOffLoadDial = QtWidgets.QPushButton(self.centralwidget)
        self.onOffLoadDial.setObjectName("onOffLoadDial")
        self.onOffLoadDial.setStyleSheet("#onOffLoadDial {background-color: red;\n"
                                         "border-image: url(:/img/Power_off_icon.png);\n"
                                         #"background-repeat: no-repeat;\n"
                                         "border-radius:30px;\n"
                                         "max-width:65px;\n"
                                         "max-height:65px;\n"
                                         "min-width:65px;\n"
                                         "min-height:65px;\n"
                                         "}\n"
                                         "\n"
                                         "#onOffLoadDial:checked{\n"
                                         "background-color: green;\\n\n"
                                         "}")
        self.onOffLoadDial.setText("")
        self.onOffLoadDial.setCheckable(True)
        self.onOffLoadDial.setChecked(False)
        # We toggle loads online/offline
        #self.onOffLoadDial.clicked.connect(self.toggleLoads)
        self.verticalLayout.addWidget(self.onOffLoadDial)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.widget_3 = dynPlot1(self.centralwidget)
        self.widget_3.setStyleSheet("background-color: rgb(85, 170, 127);")
        self.widget_3.setObjectName("widget_3")
        self.gridLayout.addWidget(self.widget_3, 0, 0, 1, 1)
        self.widget = dynPlot2(self.centralwidget)
        self.widget.setStyleSheet("background-color: rgb(255, 85, 255);")
        self.widget.setObjectName("widget")
        self.gridLayout.addWidget(self.widget, 0, 1, 1, 1)
        self.widget_2 = dynPlot3(self.centralwidget)
        self.widget_2.setStyleSheet("background-color: rgb(255, 85, 0);")
        self.widget_2.setObjectName("widget_2")
        self.gridLayout.addWidget(self.widget_2, 1, 0, 1, 1)
        self.widget_4 = dynPlot4(self.centralwidget)
        self.widget_4.setStyleSheet("background-color: rgb(170, 85, 0);")
        self.widget_4.setObjectName("widget_4")
        self.gridLayout.addWidget(self.widget_4, 1, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.widget_5 = LedWidget(self.centralwidget)
        self.widget_5.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_5.setObjectName("widget_5")
        self.horizontalLayout.addWidget(self.widget_5)
        self.widget_6 = LedWidget(self.centralwidget)
        self.widget_6.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout.addWidget(self.widget_6)
        self.widget_7 = LedWidget(self.centralwidget)
        self.widget_7.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_7.setObjectName("widget_7")
        self.horizontalLayout.addWidget(self.widget_7)
        self.widget_8 = LedWidget(self.centralwidget)
        self.widget_8.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_8.setObjectName("widget_8")
        self.horizontalLayout.addWidget(self.widget_8)
        self.widget_9 = LedWidget(self.centralwidget)
        self.widget_9.setMinimumSize(QtCore.QSize(0, 0))
        self.widget_9.setObjectName("widget_9")
        self.horizontalLayout.addWidget(self.widget_9)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2.addLayout(self.verticalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        # call QTimer to update live labels every second more or less
        #label_7 = temp, label_8 = Power, label_9 = voltage, label_10 = current, label_11= reactive power
        QtCore.QTimer.singleShot(1000, lambda: self.updateLabel(self.label_7,
                                                                self.label_8,
                                                                self.label_9,
                                                                self.label_10,
                                                                self.label_11))

    def updateLabel(self,Present_Temp_Reading, Present_Power_Reading, Present_Voltage_Reading,
                    Present_Current_Reading, Present_Reactive_Power_Reading):

        #create a random number every second.
        self.label_7 = random.gauss(70.0, 5.0)
        self.label_8 = random.gauss(1200.0, 4.0)
        self.label_9 = random.gauss(120.0, 4.0)
        self.label_10 = random.gauss(15.0, 4.0)
        self.label_11 = random.gauss(10.0, 4.0)

        #update the label with new reading
        self.new_label_7 = float('%.1f' % self.label_7)
        self.new_label_8 = float('%.1f' % self.label_8)
        self.new_label_9 = float('%.1f' % self.label_9)
        self.new_label_10 = float('%.1f' % self.label_10)
        self.new_label_11 = float('%.1f' % self.label_11)
        # Current readings
        Present_Temp_Reading.setText(str(self.new_label_7))
        Present_Power_Reading.setText(str( self.new_label_8 ))
        Present_Voltage_Reading.setText(str(self.new_label_9))
        Present_Current_Reading.setText(str(self.new_label_10))
        Present_Reactive_Power_Reading.setText(str(self.new_label_11))


        QtCore.QTimer.singleShot(1000, lambda: self.updateLabel(Present_Temp_Reading, Present_Power_Reading,
                                                                Present_Voltage_Reading, Present_Current_Reading,
                                                                Present_Reactive_Power_Reading))

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("Outlet 1", "Outlet 1"))
        self.label_8.setText(_translate("MainWindow", "P"))
        self.label_9.setText(_translate("MainWindow", "V"))
        self.label_10.setText(_translate("MainWindow", "I"))
        self.label_7.setText(_translate("MainWindow", "Temp"))
        self.label_11.setText(_translate("MainWindow", "Q"))
        self.label.setText(_translate("MainWindow", "TextLabel"))


from inLedWidgetV5 import LedWidget
from Outlet_1_DataPlots import dynPlot1, dynPlot2, dynPlot3, dynPlot4
import resources_rc

if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_InOutlet_1_Window()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
