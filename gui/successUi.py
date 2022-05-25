from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtWidgets import QCheckBox

class successUi(QtWidgets.QMainWindow):
    def __init__(self):
        super(successUi, self).__init__()
        uic.loadUi('success.ui', self)