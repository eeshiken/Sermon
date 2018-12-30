from PyQt5 import QtCore, QtGui, QtWidgets, QtSerialPort
from sermon.ui.uiMainWindow import Ui_MainWindow
from sermon.portSelect import PortSelect
from sermon.portMonitor import PortMonitor
from emoji import emojize
import os
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.portSelect = PortSelect()
        self.serialPort = QtSerialPort.QSerialPort()
        self.setCentralWidget(self.portSelect)
        self.initActionsConnections()

        self.serialPort.errorOccurred.connect(self.handleSerialError)
        self.serialPort.readyRead.connect(self.readData)

        scriptDir = os.path.dirname(os.path.realpath(__file__))
        iconsPath = scriptDir+os.path.sep+'ui'+os.path.sep+'icons'+os.path.sep

        appIcon = QtGui.QIcon()
        appIcon.addFile(iconsPath+'128x128.png', QtCore.QSize(128,128))
        appIcon.addFile(iconsPath+'256x256.png', QtCore.QSize(256,256))
        self.setWindowIcon(appIcon)

        self.showStatusMessage("...", 1000)
    
    def about(self):
        QtWidgets.QMessageBox.information(self, 
            'About Sermon',
            '<b>Sermon</b> is a serial communication tool for embedded development'
        )
        return
    
    def aboutQt(self):
        QtWidgets.QMessageBox.aboutQt(self, "About Qt")
        return
    
    def handleEmojicon(self):
        moj = f':{self.getRandomEmoji()}:'
        self.showStatusMessage(moj)
        return
    
    def initActionsConnections(self):
        self.actionAbout.triggered.connect(self.about)
        self.actionAboutQt.triggered.connect(self.aboutQt)
        self.actionEmojicon.triggered.connect(self.handleEmojicon)
        self.actionExit.triggered.connect(self.close)
        
        self.portSelect.portsRefreshButton.clicked.connect(self.portSelect.fillPortsInfo)
        self.portSelect.portOpenButton.clicked.connect(self.openSerialPort)
        return

    def openSerialPort(self):
        self.portSelect.updateSettings()
        _s = self.portSelect.settings
        self.serialPort.setPortName(_s['name'])
        self.serialPort.setBaudRate(_s['baudRate'])
        self.serialPort.setDataBits(_s['dataBits'])

        self.portMonitor = PortMonitor(f"{_s['name']} | {_s['baudRate']}")
        self.portMonitor.sendButton.clicked.connect(self.writeData)
        self.portMonitor.enterPressed.connect(self.writeData)
        self.portMonitor.windowClosed.connect(self.closeSerialPort)

        # if (self.serialPort.open(QtCore.QIODevice.ReadWrite)):
        #     self.showStatusMessage(f"Connected to {_s['name']}: {_s['baudRate']}, {_s['dataBits']}")
        self.portMonitor.show()        
        # else:
        #     QtWidgets.QMessageBox().critical(self, 'Error', self.serialPort.errorString())
        #     self.showStatusMessage('Open error')

        return

    def closeSerialPort(self):
        if (self.serialPort.isOpen()):
            self.serialPort.close()
        self.showStatusMessage('Disconnected')
        return
    
    def writeData(self):
        # Modify input with appropriate line ending
        leo = self.portMonitor.lineEndingOption
        if leo == 1:
            le = "\n"
        elif leo == 2:
            le = "\n\r"
        else:
            le = ""

        inData = self.portMonitor.dataInputBox.text() + le
        # Write data to port
        # self.serialPort.write(inData)
        self.portMonitor.dataInputBox.clear()
        return
    
    def readData(self):
        outData = self.serialPort.readAll()
        self.portMonitor.putData(outData)
        return
    
    def handleSerialError(self, error: QtSerialPort.QSerialPort.SerialPortError):
        if (error == QtSerialPort.QSerialPort.ResourceError):
            QtWidgets.QMessageBox().critical(
                self,
                'Critical Error',
                self.serialPort.errorString()
            )
            self.closeSerialPort()
        return

    def showStatusMessage(self, message: str, timeout: int = 2000):
        self.statusbar.showMessage(message, timeout)
        return
    
    def closeEvent(self, event: QtGui.QCloseEvent):

        reply = QtWidgets.QMessageBox.question(self, 
            'Exit ?', "Are you sure to quit?",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            try:
                if (self.portMonitor.isVisible()):
                    self.portMonitor.close()
                    self.closeSerialPort()
            except AttributeError:
                pass
            event.accept()
        else:
            event.ignore()
        return
