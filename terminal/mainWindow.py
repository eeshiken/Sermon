from PyQt5 import QtCore, QtGui, QtWidgets, QtSerialPort
from terminal.ui.uiMainWindow import Ui_MainWindow
from terminal.portSelect import PortSelect
from terminal.portMonitor import PortMonitor

class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.portSelect = PortSelect()
        self.serialInfo = QtSerialPort.QSerialPortInfo()
        self.setCentralWidget(self.portSelect)
        self.initActionsConnections()
    
    def about(self):
        QtWidgets.QMessageBox().about(self, 
            ("About Sermon"),
            '''
            <b>Sermon</b> is a serial communication tool for embedded development
            ''')
        return

    def initActionsConnections(self):
        self.actionAbout.triggered.connect(self.about)
        self.actionExit.triggered.connect(self.close)
        
        self.portSelect.portsRefreshButton.clicked.connect(self.__refreshBtnClickedEvent)
        return
    
    def __refreshBtnClickedEvent(self):
        self.portSelect.fillPortsInfo()
        return
