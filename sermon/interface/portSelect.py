from PyQt5 import QtCore, QtGui, QtWidgets
from serial.tools.list_ports import comports
from sermon.interface.portSettings import PortSettings

class Ui_PortSelect(object):
    def setupUi(self, OBJECT):
        OBJECT.setObjectName('PortSelect')
        OBJECT.setMinimumSize(350, 200)

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
        self.settingsButton = QtWidgets.QPushButton()

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
        self.portsRefreshLayout.addWidget(self.portsRefreshButton)
        self.settingsLayout.addItem(self.settingsSpacer)
        self.settingsLayout.addWidget(self.settingsButton)
        
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
        self.settingsButton.setText(_tr('PortSelect', 'Settings'))
        return


class PortSelect(QtWidgets.QDialog, Ui_PortSelect):
    settingsUpdateSignal = QtCore.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.portInfo = {
            'all': None,
            'name': None,
        }
        self.settings = {
            'name': None,
            'portInfo': None,
            'baudRate': None,
            'dataBits': None,
            'parity': None,
            'stopBits': None,
            'flowControl': None
        }
        self.fillPortsInfo()

    def fillPortsInfo(self):
        self.portsInfoList.clear()
        try:
            ports, descriptions, hwid = zip(*comports())
            for i in range(len(ports)):
                portInfo = [ports[i], descriptions[i], hwid[i]]
                self.portsInfoList.addItem(descriptions[i], portInfo)
        except ValueError:
            emptyPorts = ['n/a','n/a','n/a']
            self.portsInfoList.addItem('NADA', emptyPorts)
            
        return
    
    def showSettingsDialog(self):
        self.settingsDialog = PortSettings(self.settings)
        self.settingsDialog.settingsUpdateSignal.connect(self.onSettingsUpdate)
        self.settingsDialog.exec()
        return
    
    def selectPortSettings(self):
        self.portInfo['all'] = self.portsInfoList.itemData( int(self.portsInfoList.currentIndex()) )
        self.portInfo['name'] = self.portInfo['all'][0]

    def onSettingsUpdate(self):
        self.settingsUpdateSignal.emit()
        return