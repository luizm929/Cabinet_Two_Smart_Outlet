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

import matplotlib
from PyQt5.QtCore import QTimer, QSize
#matplotlib.use("Qt5Agg")
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
# Style ideal for engineering
import matplotlib.style as style
#style.use(['bmh' , 'dark_background'])
style.use('bmh')
from PyQt5.QtWidgets import QSizePolicy
import time
import os
import errno
#


class mplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        # we clear the screen otherwise we run out of memory.
        self.compute_initial_figure()
        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QSizePolicy.Preferred,
                                   QSizePolicy.Preferred)
        FigureCanvas.updateGeometry(self)

        timer = QTimer(self)
        timer.timeout.connect(self.update_figure)
        timer.start(500)

    def minimumSizeHint(self):
        return QSize(450, 400)

    def compute_initial_figure(self):
        pass

    def update_figure(self):
        pass


# -----------------------------------------------------------------
#We have two vectors x,y which are the columns on the text file so
#we only have to change column number in order to plot different values
#like current,power etc.
#Package format:
#---| Time(s) | Voltage(V) | Current (A) | Phase | Temp (F) | OCC (bool) | Power (W) | Power Schedule | ---

# Outlet 1 Voltage
class dynPlot1(mplCanvas):
    def __init__(self, *args, **kwargs):
        mplCanvas.__init__(self, *args, **kwargs)

    def compute_initial_figure(self):
        self.axes.plot([0, 1, 2, 3], [0, 1, 2, 3], 'r', color='black')

    def update_figure(self):
        self.axes.clear()
        f = open('outlet2.txt', 'r')
        d = f.readlines()
        f.close()
        x = []
        y = []
        for i in range(len(d)):
            hold = d[i].split(',')

            x.append(float(hold[0]))
            y.append(float(hold[1]))

        self.axes.plot(x, y, 'r', color='black', label='Voltage (V)')
        self.axes.set_xlabel('Time (s)')
        self.axes.set_ylabel('Voltage (V)')
        ###Legend on plot
        self.axes.legend(loc='upper left')

        self.draw()


# Outlet 1 Power
class dynPlot2(mplCanvas):
    def __init__(self, *args, **kwargs):
        mplCanvas.__init__(self, *args, **kwargs)

    def compute_initial_figure(self):
        self.axes.plot([0, 1, 2, 3], [0, 1, 2, 3], 'r', color='black')

    def update_figure(self):
        self.axes.clear()
        f = open('outlet2.txt', 'r')
        d = f.readlines()
        f.close()
        x = []
        y = []
        y1 = []
        for i in range(len(d)):
            hold = d[i].split(',')
            x.append(float(hold[0]))
            y.append(float(hold[4]))
            y1.append(float(hold[16]))
        self.axes.plot(x, y, 'r', color='black', label='Power (W)')
        # This is the schedule for power
        self.axes.plot(y1, 'r', color='red', label='Schedule (SCH)')
        self.axes.set_xlabel('Time (s)')

        self.axes.set_ylabel('Power (W)')
        ###Legend on plot
        self.axes.legend(loc='upper left')
        self.draw()


# Current
class dynPlot3(mplCanvas):
    def __init__(self, *args, **kwargs):
        mplCanvas.__init__(self, *args, **kwargs)

    def compute_initial_figure(self):
        self.axes.plot([0, 1, 2, 3], [0, 1, 2, 3], 'r', color='black')

    def update_figure(self):
        self.axes.clear()
        f = open('outlet2.txt', 'r')
        d = f.readlines()
        f.close()
        x = []
        y = []
        for i in range(len(d)):
            hold = d[i].split(',')

            x.append(float(hold[0]))
            y.append(float(hold[2]))

        self.axes.plot(x, y, 'r', color='black', label='Current (A)')
        self.axes.set_xlabel('Time (s)')
        self.axes.set_ylabel('Current (A)')
        self.axes.legend(loc='upper left')
        self.draw()


# Temperature
class dynPlot4(mplCanvas):
    def __init__(self, *args, **kwargs):
        mplCanvas.__init__(self, *args, **kwargs)

    def compute_initial_figure(self):
        self.axes.plot([0, 1, 2, 3], [0, 1, 2, 3], 'r', color='black')

    def update_figure(self):
        self.axes.clear()
        f = open('outlet2.txt', 'r')
        d = f.readlines()
        f.close()
        x = []
        y = []
        for i in range(len(d)):
            hold = d[i].split(',')

            x.append(float(hold[0]))
            y.append(float(hold[3]))

        self.axes.plot(x, y, 'r', color='black', label='Temperature (F)')
        self.axes.set_xlabel('Time (s)')
        self.axes.set_ylabel('Temperature (F)')
        self.axes.legend(loc='upper left')
        self.draw()

#--------------------------------------------------------------------
# The next plotting classes are not used, this is just room to grow
#--------------------------------------------------------------------
# class dynPlot5(mplCanvas):
#     def __init__(self, *args, **kwargs):
#         mplCanvas.__init__(self, *args, **kwargs)
#
#     def compute_initial_figure(self):
#         self.axes.plot([0, 1, 2, 3], [0, 1, 2, 3], 'r')
#
#     def update_figure(self):
#         self.axes.clear()
#         f = open('E:\SWTDI_GUI\outlet4.txt', 'r')
#         d = f.readlines()
#         f.close()
#         x = []
#         y = []
#         for i in range(len(d)):
#             hold = d[i].split(',')
#
#             x.append(float(hold[0]))
#             y.append(float(hold[1]))
#
#         self.axes.plot(x, y, 'r', label='Temperature (F)')
#         self.axes.set_xlabel('Time (s)')
#         self.axes.set_ylabel('Temperature (F)')
#         self.axes.legend(loc='upper left')
#         self.draw()
#
#
# class dynPlot6(mplCanvas):
#     def __init__(self, *args, **kwargs):
#         mplCanvas.__init__(self, *args, **kwargs)
#
#     def compute_initial_figure(self):
#         self.axes.plot([0, 1, 2, 3], [0, 1, 2, 3], 'r')
#
#     def update_figure(self):
#         self.axes.clear()
#         f = open(new_path + 'outletPlotDataH1R1O1.txt', 'r')
#         d = f.readlines()
#         f.close()
#         x = []
#         y = []
#         for i in range(len(d)):
#             hold = d[i].split(',')
#
#             x.append(float(hold[0]))
#             y.append(float(hold[1]))
#
#         self.axes.plot(x, y, 'r', label='Temperature (F)')
#         self.axes.set_xlabel('Time (s)')
#         self.axes.set_ylabel('Temperature (F)')
#         self.axes.legend(loc='upper left')
#         self.draw()
#
# class dynPlot7(mplCanvas):
#     def __init__(self, *args, **kwargs):
#         mplCanvas.__init__(self, *args, **kwargs)
#
#     def compute_initial_figure(self):
#         self.axes.plot([0, 1, 2, 3], [0, 1, 2, 3], 'r')
#
#     def update_figure(self):
#         self.axes.clear()
#         f = open(new_path + 'outletPlotDataH1R1O1.txt', 'r')
#         d = f.readlines()
#         f.close()
#         x = []
#         y = []
#         for i in range(len(d)):
#             hold = d[i].split(',')
#
#             x.append(float(hold[0]))
#             y.append(float(hold[1]))
#
#         self.axes.plot(x, y, 'r', label='Temperature (F)')
#         self.axes.set_xlabel('Time (s)')
#         self.axes.set_ylabel('Temperature (F)')
#         self.axes.legend(loc='upper left')
#         self.draw()
#
# class dynPlot8(mplCanvas):
#     def __init__(self, *args, **kwargs):
#         mplCanvas.__init__(self, *args, **kwargs)
#
#     def compute_initial_figure(self):
#         self.axes.plot([0, 1, 2, 3], [0, 1, 2, 3], 'r')
#
#     def update_figure(self):
#         self.axes.clear()
#         f = open(new_path + 'outletPlotDataH1R1O1.txt', 'r')
#         d = f.readlines()
#         f.close()
#         x = []
#         y = []
#         for i in range(len(d)):
#             hold = d[i].split(',')
#
#             x.append(float(hold[0]))
#             y.append(float(hold[1]))
#
#         self.axes.plot(x, y, 'r', label='Temperature (F)')
#         self.axes.set_xlabel('Time (s)')
#         self.axes.set_ylabel('Temperature (F)')
#         self.axes.legend(loc='upper left')
#         self.draw()
#
# class dynPlot9(mplCanvas):
#     def __init__(self, *args, **kwargs):
#         mplCanvas.__init__(self, *args, **kwargs)
#
#     def compute_initial_figure(self):
#         self.axes.plot([0, 1, 2, 3], [0, 1, 2, 3], 'r')
#
#     def update_figure(self):
#         self.axes.clear()
#         f = open(new_path + 'outletPlotDataH1R1O1.txt', 'r')
#         d = f.readlines()
#         f.close()
#         x = []
#         y = []
#         for i in range(len(d)):
#             hold = d[i].split(',')
#
#             x.append(float(hold[0]))
#             y.append(float(hold[1]))
#
#         self.axes.plot(x, y, 'r', label='Temperature (F)')
#         self.axes.set_xlabel('Time (s)')
#         self.axes.set_ylabel('Temperature (F)')
#         self.axes.legend(loc='upper left')
#         self.draw()
#
# class dynPlot10(mplCanvas):
#     def __init__(self, *args, **kwargs):
#         mplCanvas.__init__(self, *args, **kwargs)
#
#     def compute_initial_figure(self):
#         self.axes.plot([0, 1, 2, 3], [0, 1, 2, 3], 'r')
#
#     def update_figure(self):
#         self.axes.clear()
#         f = open(new_path + 'outletPlotDataH1R1O1.txt', 'r')
#         d = f.readlines()
#         f.close()
#         x = []
#         y = []
#         for i in range(len(d)):
#             hold = d[i].split(',')
#
#             x.append(float(hold[0]))
#             y.append(float(hold[1]))
#
#         self.axes.plot(x, y, 'r', label='Temperature (F)')
#         self.axes.set_xlabel('Time (s)')
#         self.axes.set_ylabel('Temperature (F)')
#         self.axes.legend(loc='upper left')
#         self.draw()
#
# class dynPlot11(mplCanvas):
#     def __init__(self, *args, **kwargs):
#         mplCanvas.__init__(self, *args, **kwargs)
#
#     def compute_initial_figure(self):
#         self.axes.plot([0, 1, 2, 3], [0, 1, 2, 3], 'r')
#
#     def update_figure(self):
#         self.axes.clear()
#         f = open(new_path + 'outletPlotDataH1R1O1.txt', 'r')
#         d = f.readlines()
#         f.close()
#         x = []
#         y = []
#         for i in range(len(d)):
#             hold = d[i].split(',')
#
#             x.append(float(hold[0]))
#             y.append(float(hold[1]))
#
#         self.axes.plot(x, y, 'r', label='Temperature (F)')
#         self.axes.set_xlabel('Time (s)')
#         self.axes.set_ylabel('Temperature (F)')
#         self.axes.legend(loc='upper left')
#         self.draw()
#
# class dynPlot12(mplCanvas):
#     def __init__(self, *args, **kwargs):
#         mplCanvas.__init__(self, *args, **kwargs)
#
#     def compute_initial_figure(self):
#         self.axes.plot([0, 1, 2, 3], [0, 1, 2, 3], 'r')
#
#     def update_figure(self):
#         self.axes.clear()
#         f = open(new_path + 'outletPlotDataH1R1O1.txt', 'r')
#         d = f.readlines()
#         f.close()
#         x = []
#         y = []
#         for i in range(len(d)):
#             hold = d[i].split(',')
#
#             x.append(float(hold[0]))
#             y.append(float(hold[1]))
#
#         self.axes.plot(x, y, 'r', label='Temperature (F)')
#         self.axes.set_xlabel('Time (s)')
#         self.axes.set_ylabel('Temperature (F)')
#         self.axes.legend(loc='upper left')
#         self.draw()

