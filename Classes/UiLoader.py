from enum import Enum
import sys
from PyQt6 import QtWidgets, uic, QtCore, QtGui
from PyQt6.QtWidgets import QCheckBox

class EventCommunicator(QtCore.QObject):
    """Class that holds PyQt signals to communicate ui actions"""
    loginPressed = QtCore.pyqtSignal()
    loginSuccess = QtCore.pyqtSignal()
    loginFailed = QtCore.pyqtSignal()
    frontPage = QtCore.pyqtSignal()
    proposed = QtCore.pyqtSignal()


class UiLoader():
    """Class that handles loading of ui windows and button connections"""
    def __init__(self, EventCommunicator):
        self.app = QtWidgets.QApplication(sys.argv)
        self.eventHandler = EventCommunicator
        self.loginWindow = loginUi(self.eventHandler)
        self.frontPageWindow = frontpage_backUi(self.eventHandler)
        self.proposeWindow = proposeScheduleUi(self.eventHandler)
        self.successWindow = successUi()


        self.eventHandler.loginSuccess.connect(self.frontPageWindow.show)
        self.eventHandler.frontPage.connect(self.proposeWindow.show)
        self.eventHandler.proposed.connect(self.successWindow.show)

    def loadUi(self):
        """Load ui window and start GUI"""
        self.loginWindow.show()
        self.app.exec()
    
    def displayTeacher(self, name):
        """Update ui text to show teacher name fetched from database at login"""
        self.frontPageWindow.setName(name)
        self.proposeWindow.setName(name)
        

class loginUi(QtWidgets.QMainWindow):
    def __init__(self, EventCommunicator):
        super(loginUi, self).__init__()
        uic.loadUi('login.ui', self)
        self.eventHandler = EventCommunicator
        self.label.setPixmap(QtGui.QPixmap("ku_logo_uk_v.png"))
        #Knapper:
        self.loginButton.clicked.connect(self.processLogin)  

    def processLogin(self):
        """Save userID from login GUI"""
        self.userID = self.username.text()
        self.eventHandler.loginPressed.emit()

class frontpage_backUi(QtWidgets.QMainWindow):
    def __init__(self, EventCommunicator):
        super(frontpage_backUi, self).__init__()
        uic.loadUi('frontpage_back2.ui', self)
        self.toSchedule.clicked.connect(self.openWindow)
        self.eventHandler = EventCommunicator

    def openWindow(self):
        """Send Qt signal that opens next window, and closes current window"""
        self.eventHandler.frontPage.emit()
        self.close()
    
    def setName(self, name: str):
        """Set name in GUI to input name"""
        self.userName.setText(name)

class proposeScheduleUi(QtWidgets.QMainWindow):
    def __init__(self, EventCommunicator):
        super(proposeScheduleUi, self).__init__()
        uic.loadUi('proposeSchedule.ui', self)

        self.textBrowser.setText("Not available dates:")
        self.proposedTimeList = []
        self.notAvailableDateList = []
        #Knapper:
        self.saveButton.clicked.connect(self.save_btn)
        self.undoButton.clicked.connect(self.undo_btn)
        self.uploadButton.clicked.connect(self.openPopup)
        self.addButton.clicked.connect(self.upload_btn)
        self.eventHandler = EventCommunicator


    def saveUiTimeList(self):
        """Saves list of selected checkboxes from ui"""
        objlist = self.scrollAreaWidgetContents_2.findChildren(QCheckBox)
        for o in objlist:
            if o.isChecked():
                self.proposedTimeList.append(o.objectName())

    def save_btn(self):
        self.saveUiTimeList()

    def upload_btn(self):
        """Add input date to list of not available dates"""
        date = self.dateTimeEdit.date().toPyDate()
        dateStr = date.strftime("%d %m %Y")
        self.notAvailableDateList.append(dateStr)
        self.textBrowser.append(dateStr)

    def undo_btn(self):
        """Remove last added date from list of not available dates"""
        self.textBrowser.setText("Not available dates:")
        self.notAvailableDateList.pop()
        for date in self.notAvailableDateList:
            self.textBrowser.append(date)

    def openPopup(self):
        """Sends signal that opens success window"""
        self.saveUiTimeList()
        self.eventHandler.proposed.emit()
    
    def setName(self, name):
        """Set name in GUI to input name"""
        self.userName.setText(name)

class successUi(QtWidgets.QMainWindow):
    def __init__(self):
        super(successUi, self).__init__()
        uic.loadUi('success.ui', self)

