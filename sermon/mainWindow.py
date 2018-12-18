import os
from PyQt5 import QtCore, QtGui, QtWidgets
from uiMainWindow import Ui_MainWindow
from portSelect import PortSelect


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setIcon("./assets/icon.png")

        self.centralWidget = PortSelect()
        self.setCentralWidget(self.centralWidget)

        self.show()

    
if __name__ == "__main__":
    import sys
    APP = QtWidgets.QApplication(sys.argv)    
    MAIN = MainWindow()
    sys.exit(APP.exec_())
