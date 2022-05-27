from enum import Enum
import sys
from PyQt6 import QtWidgets, uic, QtCore, QtGui
from PyQt6.QtWidgets import QCheckBox

class EventCommunicator(QtCore.QObject):
    loginPressed = QtCore.pyqtSignal()
    loginSuccess = QtCore.pyqtSignal()
    loginFailed = QtCore.pyqtSignal()
    frontPage = QtCore.pyqtSignal()
    proposed = QtCore.pyqtSignal()


# class UiWindowType(Enum):
#     login = "gui/login.ui"
#     success = "gui/success.ui"
#     frontpage = "gui/frontpage_back2.ui"
#     propose = "gui/proposeSchedule.ui"


class UiLoader():
    def __init__(self, EventCommunicator):
        self.app = QtWidgets.QApplication(sys.argv)
        self.eventHandler = EventCommunicator
        self.loginWindow = loginUi(self.eventHandler)
        self.frontPageWindow = frontpage_backUi(self.eventHandler)
        self.proposeWindow = proposeScheduleUi(self.eventHandler)
        self.successWindow = successUi()

        # self.state.loginPressed.connect(self.frontPageWindow.show)
        self.eventHandler.loginSuccess.connect(self.frontPageWindow.show)
        self.eventHandler.frontPage.connect(self.proposeWindow.show)
        self.eventHandler.proposed.connect(self.successWindow.show)

    def loadUi(self):
        
        self.loginWindow.show()
        self.app.exec()
    
    def showUi(self):
        self.show()
    
    def displayTeacher(self, name):
        self.frontPageWindow.setName(name)
        self.proposeWindow.setName(name)
        

class loginUi(QtWidgets.QMainWindow):
    def __init__(self, EventCommunicator):
        super(loginUi, self).__init__()
        uic.loadUi('gui/login.ui', self)
        self.eventHandler = EventCommunicator
        self.label.setPixmap(QtGui.QPixmap("gui/ku_logo_uk_v.png"))
        #Knapper:
        self.loginButton.clicked.connect(self.processLogin)

    def saveUser(self):
        self.userID = self.username.text()

    def processLogin(self):
        self.saveUser()
        self.eventHandler.loginPressed.emit()

class frontpage_backUi(QtWidgets.QMainWindow):
    def __init__(self, EventCommunicator):
        super(frontpage_backUi, self).__init__()
        uic.loadUi('gui/frontpage_back2.ui', self)
        self.toSchedule.clicked.connect(self.openWindow)
        self.eventHandler = EventCommunicator

    def openWindow(self):
        # self.ui = proposeScheduleUi()
        # self.ui.show()
        self.eventHandler.frontPage.emit()
        self.close()
    
    def setName(self, name: str):
        self.userName.setText(name)

class proposeScheduleUi(QtWidgets.QMainWindow):
    def __init__(self, EventCommunicator):
        super(proposeScheduleUi, self).__init__()
        uic.loadUi('gui/proposeSchedule.ui', self)

        self.textBrowser.setText("Not available dates:")
        #Knapper:
        self.saveButton.clicked.connect(self.save_btn)
        self.undoButton.clicked.connect(self.undo_btn)
        self.uploadButton.clicked.connect(self.openPopup)
        self.addButton.clicked.connect(self.upload_btn)
        self.eventHandler = EventCommunicator

    dateList = []
    proposedTimeList = []
    def timeList(self):
        
        objlist = self.scrollAreaWidgetContents_2.findChildren(QCheckBox)

        for o in objlist:
            if o.isChecked():
                self.proposedTimeList.append(o.objectName())
        # print(timeList)

    def save_btn(self):
        self.timeList()
        print(self.dateList)

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
        # self.ui = successUi()
        # self.ui.show()
        self.timeList()
        self.eventHandler.proposed.emit()

    
    def setName(self, name):
        self.userName.setText(name)

class successUi(QtWidgets.QMainWindow):
    def __init__(self):
        super(successUi, self).__init__()
        uic.loadUi('gui/success.ui', self)

# ui = UiLoader()
# # ui.loadUiType(UiWindowType.login)
# ui.showUi()

# ui.loadUiType(UiWindowType.frontpage)
# ui.showUi()

