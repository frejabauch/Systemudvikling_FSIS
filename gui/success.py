from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Succes(object):
    def setupUi(self, Succes):
        Succes.setObjectName("Succes")
        Succes.resize(400, 100)
        self.label = QtWidgets.QLabel(Succes)
        self.label.setGeometry(QtCore.QRect(10, 30, 381, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setObjectName("label")

        self.retranslateUi(Succes)
        QtCore.QMetaObject.connectSlotsByName(Succes)

    def retranslateUi(self, Succes):
        _translate = QtCore.QCoreApplication.translate
        Succes.setWindowTitle(_translate("Succes", "Form"))
        self.label.setText(_translate("Succes", "Success your request has been send"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Succes = QtWidgets.QWidget()
    ui = Ui_Succes()
    ui.setupUi(Succes)
    Succes.show()
    sys.exit(app.exec())
