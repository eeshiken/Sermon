from PyQt5 import QtCore, QtGui, QtWidgets, QtSerialPort


class Ui_PortSelect(object):
    def setupUi(self, OBJECT):
        OBJECT.setObjectName('PortSelect')
        # OBJECT.setMaximumSize(400, 225)
        OBJECT.setMinimumSize(350, 200)
        # OBJECT.resize(450, 250)

        # Ports label
        self.portsLabel = QtWidgets.QLabel()
        _font = QtGui.QFont()
        _font.setPointSize(12)
        _font.setWeight(QtGui.QFont().Bold)
        self.portsLabel.setFont(_font)
        _sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        _sizePolicy.setHorizontalStretch(0)
        _sizePolicy.setVerticalStretch(0)
        _sizePolicy.setHeightForWidth(self.portsLabel.sizePolicy().hasHeightForWidth())
        self.portsLabel.setSizePolicy(_sizePolicy)

        # Port list displayed as a combobox        
        self.portsInfoList = QtWidgets.QComboBox()
        _font = QtGui.QFont()
        _font.setPointSize(24)
        _font.setWeight(QtGui.QFont().Thin)
        self.portsInfoList.setFont(_font)
        _sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        _sizePolicy.setHorizontalStretch(0)
        _sizePolicy.setVerticalStretch(0)
        _sizePolicy.setHeightForWidth(self.portsInfoList.sizePolicy().hasHeightForWidth())
        self.portsInfoList.setSizePolicy(_sizePolicy)

        # Open button
        self.portOpenButton = QtWidgets.QPushButton()
        _sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        _sizePolicy.setHorizontalStretch(0)
        _sizePolicy.setVerticalStretch(0)
        _sizePolicy.setHeightForWidth(self.portOpenButton.sizePolicy().hasHeightForWidth())
        self.portOpenButton.setSizePolicy(_sizePolicy)

        # Refresh button
        self.portsRefreshButton = QtWidgets.QPushButton()
        _sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        _sizePolicy.setHorizontalStretch(0)
        _sizePolicy.setVerticalStretch(0)
        _sizePolicy.setHeightForWidth(self.portsRefreshButton.sizePolicy().hasHeightForWidth())
        self.portsRefreshButton.setSizePolicy(_sizePolicy)

        # Spacer
        self.settingsSpacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)

        # Baudrate
        self.baudRatesLabel = QtWidgets.QLabel()
        self.baudRatesList = QtWidgets.QComboBox()

        # DataBits
        self.dataBitsLabel = QtWidgets.QLabel()
        self.dataBitsList = QtWidgets.QComboBox()

        # UI STRUCTURE
        self.container = QtWidgets.QVBoxLayout(OBJECT)
        self.container.setContentsMargins(20,20,20,20)
        self.portsLabelLayout = QtWidgets.QHBoxLayout()
        self.portsLabelLayout.setContentsMargins(0,0,0,0) # LTRB
        self.portsViewLayout = QtWidgets.QHBoxLayout()
        self.portsViewLayout.setContentsMargins(0,0,0,0) # LTRB
        self.settingsLayout = QtWidgets.QHBoxLayout()
        self.settingsLayout.setContentsMargins(0,10,0,0) # LTRB

        self.portsRefreshLayout = QtWidgets.QHBoxLayout()
        self.portsRefreshLayout.setContentsMargins(0,0,0,0) # LTRB

        # Add the created ui objects to their respective layout items
        self.portsLabelLayout.addWidget(self.portsLabel)
        self.portsViewLayout.addWidget(self.portsInfoList)
        self.portsViewLayout.addWidget(self.portOpenButton)
        self.settingsLayout.addItem(self.settingsSpacer)
        self.settingsLayout.addWidget(self.dataBitsLabel)
        self.settingsLayout.addWidget(self.dataBitsList)
        self.settingsLayout.addWidget(self.baudRatesLabel)
        self.settingsLayout.addWidget(self.baudRatesList)
        self.portsRefreshLayout.addWidget(self.portsRefreshButton)
        
        # Add the layouts to the container layout
        self.container.addLayout(self.portsLabelLayout)
        self.container.addLayout(self.portsViewLayout)
        self.container.addLayout(self.portsRefreshLayout)
        self.container.addLayout(self.settingsLayout)

        self.retranslateUi(OBJECT)
        QtCore.QMetaObject.connectSlotsByName(OBJECT)

        return

    def retranslateUi(self, OBJECT):
        _tr = QtCore.QCoreApplication.translate

        self.portsLabel.setText(_tr('PortSelect', 'Available Ports'))
        self.portOpenButton.setText(_tr('PortSelect', 'Connect'))
        self.portsRefreshButton.setText(_tr('PortSelect', 'Refresh'))
        self.baudRatesLabel.setText(_tr('PortSelect', 'Baudrate'))
        self.dataBitsLabel.setText(_tr('PortSelect', 'Databits'))

        return


class PortSelect(QtWidgets.QDialog, Ui_PortSelect):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.settings = {
            'name': None,
            'baudRate': None,
            'dataBits': None
        }
        self.serialInfo = QtSerialPort.QSerialPortInfo()
        self.fillPortsInfo()
        self.fillPortsParameters()
        self.updateSettings()
    
    def fillPortsInfo(self):
        emptyString = 'n/a'
        self.portsInfoList.clear()     
        for info in self.serialInfo.availablePorts():
            pList = [
                info.portName(),
                info.description() if info.description() else emptyString,
                info.manufacturer() if info.manufacturer() else emptyString,
                info.serialNumber() if info.serialNumber() else emptyString,
                info.systemLocation(),
                int(info.vendorIdentifier()) if info.hasVendorIdentifier() else emptyString,
                int(info.productIdentifier()) if info.hasProductIdentifier() else emptyString,
            ]
            self.portsInfoList.addItem(pList[0], pList)
        return
    
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
        return
    
    def updateSettings(self):
        self.settings['name'] = self.portsInfoList.currentText()
        self.settings['port'] = self.portsInfoList.itemData( int(self.portsInfoList.currentIndex()) )
        self.settings['baudRate'] = self.baudRatesList.itemData( int(self.baudRatesList.currentIndex()) )
        self.settings['dataBits'] = self.dataBitsList.itemData( int(self.dataBitsList.currentIndex()) )
        self.settings['parity'] = QtSerialPort.QSerialPort.NoParity
        self.settings['stopBits'] = QtSerialPort.QSerialPort.OneStop
        self.settings['flowControl'] = QtSerialPort.QSerialPort.NoFlowControl
        return
