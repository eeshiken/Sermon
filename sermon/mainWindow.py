from PyQt5 import QtCore, QtGui, QtWidgets, QtSerialPort
from sermon.ui.uiMainWindow import Ui_MainWindow
from sermon.portSelect import PortSelect
from sermon.portMonitor import PortMonitor


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.portSelect = PortSelect()
        self.serialPort = QtSerialPort.QSerialPort()
        self.setCentralWidget(self.portSelect)
        self.initActionsConnections()

        self.serialPort.errorOccurred.connect(self.handleError)
        # self.serialPort.readyRead.connect(self.readData)
    
    def about(self):
        QtWidgets.QMessageBox(QtWidgets.QMessageBox.Icon.Information).about(self, 
            'About Sermon',
            '<b>Sermon</b> is a serial communication tool for embedded development'
        )
        return

    def initActionsConnections(self):
        self.actionAbout.triggered.connect(self.about)
        self.actionExit.triggered.connect(self.close)
        
        self.portSelect.portsRefreshButton.clicked.connect(self.portSelect.fillPortsInfo)
        self.portSelect.portOpenButton.clicked.connect(self.openSerialPort)
        return
    
    def writeData(self, data: QtCore.QByteArray):
        self.serialPort.write(data)
        return
    
    def readData(self):
        data = self.serialPort.readAll()
        self.portMonitor.putData(data)
        return

    def openSerialPort(self):
        self.portSelect.updateSettings()
        _s = self.portSelect.settings
        self.serialPort.setPortName(_s['name'])
        self.serialPort.setBaudRate(_s['baudRate'])
        self.serialPort.setDataBits(_s['dataBits'])

        self.portMonitor = PortMonitor(_s['name'])
        # if (self.serialPort.open(QtCore.QIODevice.ReadWrite)):
        #     showStatusMessage(f'Connected to {_s['name']: _s['baudRate'], _s['dataBits']}')
        self.portMonitor.show()        
        # else:
        #     QtWidgets.QMessageBox().critical(self, 'Error', self.serialPort.errorString())
        #     showStatusMessage('Open error')

        return

    def closeSerialPort(self):
        if (self.serialPort.isOpen()):
            self.serialPort.close()
        showStatusMessage('Disconnected')
        return
    
    def handleError(self, error: QtSerialPort.QSerialPort.SerialPortError):
        if (error == QtSerialPort.QSerialPort.ResourceError):
            QtWidgets.QMessageBox().critical(
                self,
                'Critical Error',
                self.serialPort.errorString()
            )
            self.closeSerialPort()
        return

    def showStatusMessage(self, message: str):
        self.statusbar.showMessage(message)
        return
