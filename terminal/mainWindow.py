from PyQt5 import QtCore, QtGui, QtWidgets
from terminal.ui.uiMainWindow import Ui_MainWindow
from terminal.portSelect import PortSelect

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.portSelect = PortSelect()
        self.setCentralWidget(self.portSelect)

    def initActionsConnections(self):

        return
    

    
    def about(self):
        self.aboutProgram = QtWidgets.QMessageBox()
        self.aboutProgram.about(self, 
            tr("About Simple Terminal"),
            tr("The <b>Simple Terminal</b> example demonstrates how to "
               "use the Qt Serial Port module in modern GUI applications "
               "using Qt, with a menu bar, toolbars, and a status bar."))
        return
