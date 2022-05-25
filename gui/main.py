from loginUi import *
import sys

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = loginUi()
    window.show()
    app.exec()