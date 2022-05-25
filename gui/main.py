from samletUi import *
import sys

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = samletUi()
    window.show()
    app.exec()