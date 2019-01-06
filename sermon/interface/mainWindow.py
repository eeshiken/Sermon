import os
from random import randrange

from PyQt5 import QtCore, QtGui, QtWidgets, QtSerialPort
from sermon.resources import resourcePath
from sermon.interface.portSettings import PortSettings
from sermon.interface.portSelect import PortSelect
from sermon.interface.portMonitor import PortMonitor


class StatusBar(QtWidgets.QStatusBar):
    def __init__(self):
        super().__init__()
        # Baudrates
        self.baudRateLabel = QtWidgets.QLabel()
        self.baudRateLabel.setToolTip('Baudrate')
        self.addPermanentWidget(self.baudRateLabel)
        # Databits
        self.dataBitsLabel = QtWidgets.QLabel()
        self.dataBitsLabel.setToolTip('Databits')
        self.addPermanentWidget(self.dataBitsLabel)

    def setBaudRate(self, baudrate: str):
        self.baudRateLabel.setText(str(baudrate))
    
    def setDataBits(self, databits: str):
        self.dataBitsLabel.setText(str(databits))


class Ui_MainWindow(object):
    def setupUi(self, OBJECT):
        OBJECT.setObjectName('MainWindow')
        OBJECT.setMinimumSize(350, 250)
        OBJECT.resize(450, 300)

        self.createActions(OBJECT)
        self.createMenu(OBJECT)

        self.retranslateUi(OBJECT)
        QtCore.QMetaObject.connectSlotsByName(OBJECT)
        return
    
    def retranslateUi(self, OBJECT):
        _tr = QtCore.QCoreApplication.translate
        OBJECT.setWindowTitle(_tr('MainWindow', 'Sermon: Serial Monitor'))
        self.fileMenu.setTitle(_tr('MainWindow', 'File'))
        self.helpMenu.setTitle(_tr('MainWindow', 'Help'))
        self.actionAbout.setText(_tr('MainWindow', 'About'))
        self.actionAboutQt.setText(_tr('MainWindow', 'About Qt'))
        self.actionExit.setText(_tr('MainWindow', 'Exit'))
        self.actionUnicode.setText(_tr('MainWindow', 'Unicode'))
        return
    
    def createActions(self, OBJECT):
        self.actionAbout = QtWidgets.QAction(OBJECT)
        self.actionAbout.setShortcuts(QtGui.QKeySequence(QtCore.Qt.CTRL + QtCore.Qt.Key_A))
        self.actionAboutQt = QtWidgets.QAction(OBJECT)
        self.actionAboutQt.setShortcuts(QtGui.QKeySequence(QtCore.Qt.CTRL + QtCore.Qt.SHIFT + QtCore.Qt.Key_A))
        self.actionExit = QtWidgets.QAction(OBJECT)
        self.actionExit.setShortcuts(QtGui.QKeySequence(QtCore.Qt.CTRL + QtCore.Qt.Key_E))
        self.actionUnicode = QtWidgets.QAction(OBJECT)
        self.actionUnicode.setShortcuts(QtGui.QKeySequence(QtCore.Qt.CTRL + QtCore.Qt.Key_Y))
        return
    
    def createMenu(self, OBJECT):
        self.menubar = OBJECT.menuBar()

        self.fileMenu = QtWidgets.QMenu(self.menubar)
        self.fileMenu.addAction(self.actionExit)
        self.fileMenu.addAction(self.actionUnicode)

        self.helpMenu = QtWidgets.QMenu(self.menubar)
        self.helpMenu.addAction(self.actionAbout)
        self.helpMenu.addAction(self.actionAboutQt)

        self.menubar.addAction(self.fileMenu.menuAction())
        self.menubar.addAction(self.helpMenu.menuAction())
    
        return

    def getRandomUnicode(self) -> str:
        CODE_LENGTH = randrange(10)
        hexCode = [chr(randrange(945,975)) for code in range(CODE_LENGTH)]
        return ''.join(hexCode)


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.portSelect = PortSelect()
        self.setCentralWidget(self.portSelect)

        self.statusbar = StatusBar()
        self.setStatusBar(self.statusbar)
    
        self.initActionsConnections()
        
        self.setAppIcon()
        self.showStatusMessage("...", 1000)

        # Populate on statrtup
        self.portSelect.settingsDialog = PortSettings(self.portSelect.settings)
        self.portSelect.settingsDialog.settingsUpdateSignal.connect(self.portSelect.onSettingsUpdate)
        self.portSelect.settingsDialog.updateSettings()

    def setAppIcon(self):
        appIcon = QtGui.QIcon()
        appIcon.addFile(resourcePath('128x128'), QtCore.QSize(128,128))
        appIcon.addFile(resourcePath('256x256'), QtCore.QSize(256,256))
        self.setWindowIcon(appIcon)
    
    def about(self):
        QtWidgets.QMessageBox.information(self, 
            'About Sermon',
            '<b>Sermon</b> is a serial communication tool for embedded development'
        )
        return
    
    def aboutQt(self):
        QtWidgets.QMessageBox.aboutQt(self, "About Qt")
        return
    
    def handleUnicode(self):
        code = self.getRandomUnicode()
        self.showStatusMessage(code)
        return
    
    def initActionsConnections(self):
        self.actionAbout.triggered.connect(self.about)
        self.actionAboutQt.triggered.connect(self.aboutQt)
        self.actionUnicode.triggered.connect(self.handleUnicode)
        self.actionExit.triggered.connect(self.close)
        
        self.portSelect.portsRefreshButton.clicked.connect(self.portSelect.fillPortsInfo)
        self.portSelect.portOpenButton.clicked.connect(self.openSerialPort)
        self.portSelect.settingsButton.clicked.connect(self.portSelect.showSettingsDialog)
        self.portSelect.settingsUpdateSignal.connect(self.onSettingsUpdate)
        return
    
    def onSettingsUpdate(self):
        _s = self.portSelect.settings
        self.statusbar.setBaudRate(_s['baudRate'])
        self.statusbar.setDataBits(_s['dataBits'])
        return

    def openSerialPort(self):
        self.portSelect.selectPortSettings()
        _p = self.portSelect.portInfo
        _s = self.portSelect.settings

        # Fast check if no devices are connected
        if _p['name'] == 'n/a':
            QtWidgets.QMessageBox.information(self,
                'Port Info',
                'No devices found!'
            )
            return

        self.serialPort = QtSerialPort.QSerialPort()
        self.serialPort.setPortName(_p['name'])
        self.serialPort.setBaudRate(_s['baudRate'])
        self.serialPort.setDataBits(_s['dataBits'])
        self.serialPort.setParity(_s['parity'])
        self.serialPort.setStopBits(_s['stopBits'])
        self.serialPort.setFlowControl(_s['flowControl'])

        # Create communication window and connect signals
        self.portMonitor = PortMonitor(f"{_p['name']} | {_s['baudRate']}")
        self.portMonitor.sendButton.clicked.connect(self.onSerialWriteData)
        self.portMonitor.enterPressed.connect(self.onSerialWriteData)
        self.portMonitor.windowClosed.connect(self.closeSerialPort)

        if self.serialPort.open(QtCore.QIODevice.ReadWrite):
            self.serialPort.readyRead.connect(self.onSerialReadData)
            self.portMonitor.consoleOut.clear()
            self.portMonitor.show()
            self.serialPort.errorOccurred.connect(self.handleSerialError)
            self.showStatusMessage(f"Connected to {_p['name']}: {_s['baudRate']}, {_s['dataBits']}")
        else:
            msg = f"Cannot connect to device on port {_p['name']}"
            self.handleSerialError(msg)
        return

    def closeSerialPort(self):
        if (self.serialPort.isOpen()):
            self.serialPort.close()
            self.showStatusMessage('Disconnected')
        self.portMonitor.consoleOut.clear()
        return
    
    def onSerialWriteData(self):
        # Modify input with appropriate line ending
        leo = self.portMonitor.lineEndingOption
        if leo == 1:
            le = "\n"
        elif leo == 2:
            le = "\r\n"
        else:
            le = ""

        inData = self.portMonitor.dataInputBox.text() + le
        # Write data to port
        self.serialPort.write(inData.encode('utf-8'))
        self.portMonitor.dataInputBox.clear()
        return
    
    def onSerialReadData(self):
        outData = bytes(self.serialPort.readAll())
        strData = outData.decode('utf-8')
        self.portMonitor.putData(strData)
        return
    
    def handleSerialError(self, error: QtSerialPort.QSerialPort.SerialPortError):
        QtWidgets.QMessageBox().critical(
            self,
            'Serial Error',
            f'{error}\nError Code: {self.serialPort.error()}'
        )
        self.closeSerialPort()
        return

    def showStatusMessage(self, message: str, timeout: int = 3000):
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
