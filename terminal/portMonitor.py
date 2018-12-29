from PyQt5 import QtCore, QtGui, QtWidgets
from terminal.ui.uiPortSelect import Ui_PortSelect

class PortMonitor(QtWidgets.QDialog, Ui_PortSelect):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == "__main__":
    import sys
    APP = QtWidgets.QApplication(sys.argv)
    MAIN = PortSelect()
    MAIN.show()
    sys.exit(APP.exec_())
