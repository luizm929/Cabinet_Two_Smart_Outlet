# -*- coding: utf-8 -*-
#--------------------------------
# Packages needed
#Matplotlib
#Python3
#PyQt5
#
#------------------------------------------------------------
#
# Written by Luis Martinez : luizmartines@gmail.com
#                          : luizm929@nmsu.edu
# Thanks to Jose Tabarez for his help.
#------------------------------------------------------------


from PyQt5.QtCore import QSize, Qt
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QLabel, QWidget, QVBoxLayout, QApplication


class Led(QWidget):
    def __init__(self, colorOn, colorOff, parent=None):
        QLabel.__init__(self, parent)
        self.colorOn = colorOn
        self.colorOff = colorOff
        self.state = True

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(self.colorOn if self.state else self.colorOff)
        painter.drawEllipse(self.rect())

    def minimumSizeHint(self):
        return QSize(40, 40)

    def setState(self, state):
        self.state = state


class LedWidget(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        text = "TEXT"
        onColor = QColor("red")
        offColor = QColor("green")
        self.led = Led(onColor, offColor, self)
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(self.led)
        label = QLabel(text, self)
        label.setAlignment(Qt.AlignCenter)
        self.layout().addWidget(label)

class temp_led(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        text = "Temp"
        onColor = QColor("red")
        offColor = QColor("green")
        self.led = Led(onColor, offColor, self)
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(self.led)
        label = QLabel(text, self)
        label.setAlignment(Qt.AlignCenter)
        self.layout().addWidget(label)

class loads_online_led(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        text = "Loads Online"
        onColor = QColor("red")
        offColor = QColor("green")
        self.led = Led(onColor, offColor, self)
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(self.led)
        label = QLabel(text, self)
        label.setAlignment(Qt.AlignCenter)
        self.layout().addWidget(label)

class room_occupancy_led(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        text = "Occup"
        onColor = QColor("red")
        offColor = QColor("green")
        self.led = Led(onColor, offColor, self)
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(self.led)
        label = QLabel(text, self)
        label.setAlignment(Qt.AlignCenter)
        self.layout().addWidget(label)

class xtra_led(QWidget):
    def __init__(self, parent=None):
        QWidget.__init__(self, parent)
        text = "TEXT"
        onColor = QColor("red")
        offColor = QColor("green")
        self.led = Led(onColor, offColor, self)
        self.setLayout(QVBoxLayout())
        self.layout().addWidget(self.led)
        label = QLabel(text, self)
        label.setAlignment(Qt.AlignCenter)
        self.layout().addWidget(label)

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    w = LedWidget("Text", QColor("red"), QColor("green"))
    w.show()
    sys.exit(app.exec_())
