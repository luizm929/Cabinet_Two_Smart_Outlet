#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import os
import shutil

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from get_time import *
# -- BEGIN CONFIG --#

appTitle = "PyQt5 Process Test App"
scriptPath = "E:\\NMSU_Software_Projects\\Cabinet\\get_time.py"


# --- END CONFIG ---#

def cmd_exists(cmd):
    return shutil.which(cmd) is not None


class Widget(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        startButton = QPushButton('Start')
        stopButton = QPushButton('Stop')
        clearButton = QPushButton('Clear')

        self.logArea = QTextBrowser()

        startButton.clicked.connect(self.startButtonClicked)
        stopButton.clicked.connect(self.stopButtonClicked)
        clearButton.clicked.connect(self.clearButtonClicked)

        grid = QGridLayout()
        grid.setSpacing(10)

        grid.addWidget(startButton, 0, 0)
        grid.addWidget(stopButton, 0, 1)
        grid.addWidget(clearButton, 0, 2)
        grid.addWidget(self.logArea, 1, 0, 3, 0)

        self.setLayout(grid)

        self.setWindowTitle(appTitle)
        self.show()


    def startButtonClicked(self):
        self.process = QProcess()
        self.process.setProgram(getTime(5))
        self.process.readyReadStandardOutput.connect(self.readData)
        self.process.start()

    def stopButtonClicked(self):
        self.process.terminate()
        self.process.waitForFinished()
        self.process.close()

    def clearButtonClicked(self):
        self.logArea.clear()

    def readData(self):
        while self.process.canReadLine():
            line = self.process.readLine()
            self.logArea.append(str(line.data().decode()).strip())


if __name__ == '__main__':

    # run as root
    # if os.geteuid() != 0:
    # print("Must run as root")
    # exit(1)

    #if not cmd_exists(scriptPath):
    #    print("Could not find script at " + scriptPath)
    #    exit(1)

    app = QApplication(sys.argv)
    w = Widget()
    sys.exit(app.exec_())