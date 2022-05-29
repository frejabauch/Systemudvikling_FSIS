from PyQt6 import QtCore, QtGui, QtWidgets, uic
from PyQt6.QtWidgets import QCheckBox
from successUi import *

class proposeScheduleUi(QtWidgets.QMainWindow):
    def __init__(self):
        super(proposeScheduleUi, self).__init__()
        uic.loadUi('proposeSchedule.ui', self)

        self.textBrowser.setText("Not available dates:")
        #Knapper:
        self.saveButton.clicked.connect(self.save_btn)
        self.undoButton.clicked.connect(self.undo_btn)
        self.uploadButton.clicked.connect(self.openPopup)
        self.addButton.clicked.connect(self.upload_btn)

    dateList = []
    
    def timeList(self):
        timeList = []
        objlist = self.scrollAreaWidgetContents_2.findChildren(QCheckBox)

        for o in objlist:
            if o.isChecked():
                timeList.append(o.objectName())
        print(timeList)

    def save_btn(self):
        self.timeList()

    def upload_btn(self):
        date = self.dateTimeEdit.date().toPyDate()
        dateStr = date.strftime("%d %m %Y")
        self.dateList.append(dateStr)
        self.textBrowser.append(dateStr)

    def undo_btn(self):
        self.textBrowser.setText("Not available dates:")
        self.dateList.pop()
        for date in self.dateList:
            self.textBrowser.append(date)
        print(self.dateList)

    def openPopup(self):
        self.ui = successUi()
        self.ui.show()
        self.timeList()