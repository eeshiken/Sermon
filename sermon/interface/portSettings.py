from PyQt5 import QtCore, QtGui, QtWidgets, QtSerialPort


class Ui_PortSettings(object):
    def setupUi(self, OBJECT):
        OBJECT.setObjectName('PortSettings')
        OBJECT.setMinimumSize(350, 200)

        # Baudrate
        self.baudRatesLabel = QtWidgets.QLabel()
        self.baudRatesList = QtWidgets.QComboBox()
        # Databits
        self.dataBitsLabel = QtWidgets.QLabel()
        self.dataBitsList = QtWidgets.QComboBox()
        # Parity
        self.parityLabel = QtWidgets.QLabel()
        self.parityList = QtWidgets.QComboBox()
        # StopBits
        self.stopBitsLabel = QtWidgets.QLabel()
        self.stopBitsList = QtWidgets.QComboBox()
        # FlowControl
        self.flowControlLabel = QtWidgets.QLabel()
        self.flowControlList = QtWidgets.QComboBox()

        # Buttons
        self.buttonBox = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel)

        # UI STRUCTURE
        self.container = QtWidgets.QVBoxLayout(OBJECT)
        self.container.setContentsMargins(20,20,20,20)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setColumnStretch(0,1)
        self.gridLayout.setColumnStretch(1,2)
    
        # Add widgets
        self.gridLayout.addWidget(self.baudRatesLabel,0,0)
        self.gridLayout.addWidget(self.baudRatesList,0,1)
        self.gridLayout.addWidget(self.dataBitsLabel,1,0)
        self.gridLayout.addWidget(self.dataBitsList,1,1)
        self.gridLayout.addWidget(self.parityLabel,2,0)
        self.gridLayout.addWidget(self.parityList,2,1)
        self.gridLayout.addWidget(self.stopBitsLabel,3,0)
        self.gridLayout.addWidget(self.stopBitsList,3,1)
        self.gridLayout.addWidget(self.flowControlLabel,4,0)
        self.gridLayout.addWidget(self.flowControlList,4,1)

        # Add to main Layout
        self.container.addLayout(self.gridLayout)
        self.container.addWidget(self.buttonBox)

        self.retranslateUi(OBJECT)
        QtCore.QMetaObject.connectSlotsByName(OBJECT)
        return
    
    def retranslateUi(self, OBJECT):
        _tr = QtCore.QCoreApplication.translate
        OBJECT.setWindowTitle(_tr('PortSettings', 'Port Settings'))
        self.baudRatesLabel.setText(_tr('PortSettings', 'Baudrate'))
        self.dataBitsLabel.setText(_tr('PortSettings', 'Databits'))
        self.parityLabel.setText(_tr('PortSettings', 'Parity'))
        self.stopBitsLabel.setText(_tr('PortSettings', 'Stopbits'))
        self.flowControlLabel.setText(_tr('PortSettings', 'Flow Control'))
        return


class PortSettings(QtWidgets.QDialog, Ui_PortSettings):
    settingsUpdateSignal = QtCore.pyqtSignal()

    def __init__(self, settings):
        super().__init__()
        self.setupUi(self)
        self.settings = settings
        self.serialInfo = QtSerialPort.QSerialPortInfo()
        self.fillPortsParameters()
        self.buttonBox.accepted.connect(self.updateSettings)
        self.buttonBox.rejected.connect(self.close)

    def fillPortsParameters(self):
        self.baudRatesList.addItem('9600', QtSerialPort.QSerialPort.Baud9600)
        self.baudRatesList.addItem('19200', QtSerialPort.QSerialPort.Baud19200)
        self.baudRatesList.addItem('38400', QtSerialPort.QSerialPort.Baud38400)
        self.baudRatesList.addItem('57600', QtSerialPort.QSerialPort.Baud57600)
        self.baudRatesList.addItem('115200', QtSerialPort.QSerialPort.Baud115200)
        self.baudRatesList.setCurrentIndex(0)

        self.dataBitsList.addItem('5', QtSerialPort.QSerialPort.Data5)
        self.dataBitsList.addItem('6', QtSerialPort.QSerialPort.Data6)
        self.dataBitsList.addItem('7', QtSerialPort.QSerialPort.Data7)
        self.dataBitsList.addItem('8', QtSerialPort.QSerialPort.Data8)
        self.dataBitsList.setCurrentIndex(3)

        self.parityList.addItem('No Parity', QtSerialPort.QSerialPort.NoParity)
        self.parityList.addItem('Odd Parity', QtSerialPort.QSerialPort.OddParity)
        self.parityList.addItem('Space Parity', QtSerialPort.QSerialPort.SpaceParity)
        self.parityList.addItem('Mark Parity', QtSerialPort.QSerialPort.MarkParity)
        self.parityList.setCurrentIndex(0)

        self.stopBitsList.addItem('1', QtSerialPort.QSerialPort.OneStop)
        self.stopBitsList.addItem('1.5', QtSerialPort.QSerialPort.OneAndHalfStop)
        self.stopBitsList.addItem('2', QtSerialPort.QSerialPort.TwoStop)               
        self.stopBitsList.setCurrentIndex(0)

        self.flowControlList.addItem('No Flow Control', QtSerialPort.QSerialPort.NoFlowControl)
        self.flowControlList.addItem('Hardware Control', QtSerialPort.QSerialPort.HardwareControl)
        self.flowControlList.addItem('Software Control', QtSerialPort.QSerialPort.SoftwareControl)
        self.flowControlList.setCurrentIndex(0)
        return
    
    def updateSettings(self):
        self.settings['baudRate'] = self.baudRatesList.itemData( int(self.baudRatesList.currentIndex()) )
        self.settings['dataBits'] = self.dataBitsList.itemData( int(self.dataBitsList.currentIndex()) )
        self.settings['parity'] = self.parityList.itemData( int(self.parityList.currentIndex()) )
        self.settings['stopBits'] = self.stopBitsList.itemData( int(self.stopBitsList.currentIndex()) )
        self.settings['flowControl'] = self.flowControlList.itemData( int(self.flowControlList.currentIndex()) )
        self.settingsUpdateSignal.emit()

        self.close()
        return
