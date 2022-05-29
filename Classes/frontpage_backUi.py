from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtWidgets import QCheckBox
from proposeScheduleUi import *

class frontpage_backUi(QtWidgets.QMainWindow):
    def __init__(self):
        super(frontpage_backUi, self).__init__()
        uic.loadUi('frontpage_back2.ui', self)
        self.toSchedule.clicked.connect(self.openWindow)

    def openWindow(self):
        self.ui = proposeScheduleUi()
        self.ui.show()
        self.close()