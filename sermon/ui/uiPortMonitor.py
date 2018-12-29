from PyQt5 import QtCore, QtGui, QtWidgets

class Console(QtWidgets.QPlainTextEdit):
    def __init__(self, OBJECT):
        super().__init__(OBJECT)
        self.document().setMaximumBlockCount(1000)

    def putData(self, data: QtCore.QByteArray):
        self.insertPlainText(data)
        self.bar = QtWidgets.QScrollBar().verticalScrollBar()
        self.bar.setValue(self.bar.maximum())
    
    def setLocalEchoEnabled(self, set: bool):
        self.localEchoEnabled = set
    
    def keyPressEvent(self, event):
        print(event.key())
    
    def mousePressEvent(self, event):
        self.setFocus()


class Ui_PortMonitor(object):
    def setupUi(self, OBJECT):
        OBJECT.setObjectName("PortMonitor")
        OBJECT.resize(388, 262)

        # Output console
        self.consoleOut = Console(OBJECT)
        self.consoleOut.setGeometry(QtCore.QRect(10, 40, 371, 211))
        self.consoleOut.setReadOnly(True)
        self.consoleOut.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        # Input
        self.dataIn = QtWidgets.QLineEdit()
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dataIn.setFont(font)
        self.dataIn.setMinimumSize(QtCore.QSize(0, 0))
        self.dataIn.setAcceptDrops(True)
        self.dataIn.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.dataIn.setFrame(True)
        self.dataIn.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)

        # Send button
        self.sendButton = QtWidgets.QPushButton(OBJECT)
        self.sendButton.setGeometry(QtCore.QRect(300, 10, 85, 27))
        
        self.settingsSpacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)

        # Line ending
        self.lineEndLabel = QtWidgets.QLabel(OBJECT)
        self.lineEndList = QtWidgets.QComboBox(OBJECT)

        # UI STRUCTURE
        # Layouts
        self.container = QtWidgets.QVBoxLayout(OBJECT)

        self.outputLayout = QtWidgets.QHBoxLayout()
        self.outputLayout.setContentsMargins(0, 0, 0, 0)
        self.inputLayout = QtWidgets.QHBoxLayout()
        self.inputLayout.setContentsMargins(0, 0, 0, 0)
        self.settingsLayout = QtWidgets.QHBoxLayout()
        self.settingsLayout.setContentsMargins(0, 0, 0, 0)

        # Add elements to layouts
        self.outputLayout.addWidget(self.consoleOut)
        self.inputLayout.addWidget(self.dataIn)
        self.inputLayout.addWidget(self.sendButton)
        self.settingsLayout.addItem(self.settingsSpacer)
        self.settingsLayout.addWidget(self.lineEndLabel)
        self.settingsLayout.addWidget(self.lineEndList)

        # Add layouts to main layout
        self.container.addLayout(self.inputLayout)
        self.container.addLayout(self.outputLayout)
        self.container.addLayout(self.settingsLayout)

        self.retranslateUi(OBJECT)
        QtCore.QMetaObject.connectSlotsByName(OBJECT)
    
    def retranslateUi(self, OBJECT):
        _tr = QtCore.QCoreApplication.translate
        self.sendButton.setText(_tr('PortMonitor', 'Send'))
        self.dataIn.setPlaceholderText(_tr('PortMonitor', 'Enter message here...'))
        self.lineEndLabel.setText(_tr('PortMonitor', ''))
