import os
from PyQt5 import QtCore, QtGui, QtWidgets
from sermon.ui.uiMainWindow import Ui_MainWindow
from sermon.portSelect import PortSelect
from sermon.portMonitor import PortMonitor


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setIcon("./assets/icon.png")

        self.portSelect = PortSelect()
        self.setCentralWidget(self.portSelect)

        # Finally
        self.show()

    
if __name__ == "__main__":
    import sys
    APP = QtWidgets.QApplication(sys.argv)    
    MAIN = MainWindow()
    sys.exit(APP.exec_())
