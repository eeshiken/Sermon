from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PortMonitor(object):
    def setupUi(self, OBJECT):
        OBJECT.setObjectName("PortMonitor")
        OBJECT.resize(388, 262)

        # Output console
        self.consoleOut = QtWidgets.QPlainTextEdit(OBJECT)
        self.consoleOut.setGeometry(QtCore.QRect(10, 40, 371, 211))
        self.consoleOut.setReadOnly(True)
        self.consoleOut.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)

        # Input
        self.dataInputBox = QtWidgets.QLineEdit(OBJECT)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dataInputBox.setFont(font)
        self.dataInputBox.setMinimumSize(QtCore.QSize(0, 0))
        self.dataInputBox.setAcceptDrops(True)
        self.dataInputBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.dataInputBox.setFrame(True)
        self.dataInputBox.setClearButtonEnabled(True)
        self.dataInputBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)

        # Send button
        self.sendButton = QtWidgets.QPushButton(OBJECT)
        self.sendButton.setGeometry(QtCore.QRect(300, 10, 85, 27))
        
        self.settingsSpacer = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)

        # Line ending
        self.lineEndLabel = QtWidgets.QLabel(OBJECT)
        self.lineEndList = QtWidgets.QComboBox(OBJECT)

        # Clear Console button
        self.clearConsoleButton = QtWidgets.QPushButton(OBJECT)

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
        self.inputLayout.addWidget(self.dataInputBox)
        self.inputLayout.addWidget(self.sendButton)
        self.settingsLayout.addWidget(self.clearConsoleButton)
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
        self.clearConsoleButton.setText(_tr('PortMonitor', 'Clear'))
        self.dataInputBox.setPlaceholderText(_tr('PortMonitor', 'Enter message here...'))
        self.lineEndLabel.setText(_tr('PortMonitor', ''))
