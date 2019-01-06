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
        self.dataInputBox.setFrame(False)
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
        # self.sendButton.setFlat(True)
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


class PortMonitor(QtWidgets.QDialog, Ui_PortMonitor):
    windowClosed = QtCore.pyqtSignal()
    enterPressed = QtCore.pyqtSignal()
    lineEndingOption = None

    def __init__(self, NAME):
        super().__init__()
        self.setupUi(self)

        self.consoleOut.document().setMaximumBlockCount(1000)

        _tr = QtCore.QCoreApplication.translate
        self.setWindowTitle(_tr('PortMonitor', NAME))

        self.fillLineEndings()
        self.updateLineEnding()

        self.lineEndList.currentIndexChanged.connect(self.updateLineEnding)
        self.clearConsoleButton.clicked.connect(self.consoleOut.clear)
    
    def fillLineEndings(self):
        self.lineEndList.addItem('No line ending', 0)
        self.lineEndList.addItem('Newline \\n', 1)
        self.lineEndList.addItem('Newline & Return \\r\\n', 2)
        self.lineEndList.setCurrentIndex(1)
        return
    
    def updateLineEnding(self):
        self.lineEndingOption = self.lineEndList.itemData(int(self.lineEndList.currentData()))
        return

    def putData(self, data: str):
        self.consoleOut.insertPlainText(data)
        self.bar = self.consoleOut.verticalScrollBar()
        self.bar.setValue(self.bar.maximum())
    
    def keyPressEvent(self, event: QtGui.QKeyEvent):
        if (event.key() == QtCore.Qt.Key_Return):
            self.enterPressed.emit()
        return
    
    def closeEvent(self, event: QtGui.QCloseEvent):
        self.windowClosed.emit()
        return
