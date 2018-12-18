from PyQt5 import QtCore, QtGui, QtWidgets
from uiPortSelect import Ui_PortSelect

class PortSelect(QtWidgets.QDialog, Ui_PortSelect):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == "__main__":
    import sys
    APP = QtWidgets.QApplication(sys.argv)
    MAIN = PortSelect()
    MAIN.show()
    sys.exit(APP.exec_())
