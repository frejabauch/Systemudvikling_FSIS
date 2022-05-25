from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtWidgets import QCheckBox

from frontpage_backUi import *

class loginUi(QtWidgets.QMainWindow):
    def __init__(self):
        super(loginUi, self).__init__()
        uic.loadUi('login.ui', self)

        self.label.setPixmap(QtGui.QPixmap("ku_logo_uk_v.png"))
        #Knapper:
        self.loginButton.clicked.connect(self.openWindow)

    def openWindow(self):
        self.ui = frontpage_backUi()
        self.ui.show()
        self.close()