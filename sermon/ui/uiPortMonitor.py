from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_PortMonitor(object):
    def setupUi(self, OBJECT):
        OBJECT.setObjectName("PortMonitor")
        OBJECT.resize(388, 262)
        # Layout
        self.container = QtWidgets.QVBoxLayout(self)
        self.container.setObjectName("container")

        # Top
        self.outputLayout = QtWidgets.QHBoxLayout()
        self.outputLayout.setContentsMargins(10, 10, 10, 10)
        # Output window
        self.messageOutput = QtWidgets.QTextEdit(OBJECT)
        self.messageOutput.setGeometry(QtCore.QRect(10, 40, 371, 211))
        self.messageOutput.setReadOnly(True)
        self.messageOutput.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.messageOutput.setObjectName("messageOutput")
        ### Add msg output to the output layout  
        self.outputLayout.addWidget(self.messageOutput) 

        ## Add output layout to container
        self.container.addLayout(self.outputLayout)

        # Bottom
        self.inputLayout = QtWidgets.QHBoxLayout()
        self.inputLayout.setContentsMargins(10, 10, 10, 10)
        # Input
        font = QtGui.QFont()
        font.setPointSize(12)
        self.messageInput = QtWidgets.QLineEdit()
        self.messageInput.setFont(font)
        self.messageInput.setMinimumSize(QtCore.QSize(0, 0))
        self.messageInput.setAcceptDrops(True)
        self.messageInput.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.messageInput.setText("")
        self.messageInput.setFrame(True)
        self.messageInput.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.messageInput.setObjectName("messageInput")
        ## Add input to input layout
        self.inputLayout.addWidget(self.messageInput)  

        # Send button
        self.sendButton = QtWidgets.QPushButton(OBJECT)
        self.sendButton.setGeometry(QtCore.QRect(300, 10, 85, 27))
        self.sendButton.setObjectName("sendButton")
        ### Add input to input layout
        self.inputLayout.addWidget(self.sendButton) 

        ## Add input input layout
        self.container.addLayout(self.inputLayout)

        self.retranslateUi(OBJECT)
        QtCore.QMetaObject.connectSlotsByName(OBJECT)
    
    def retranslateUi(self, OBJECT):
        _translate = QtCore.QCoreApplication.translate
        OBJECT.sendButton.setText(_translate("PortMonitor", "Send"))
        OBJECT.messageInput.setPlaceholderText(_translate("PortMonitor", "Enter message here..."))

