from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_PortSelect(object):
    def setupUi(self, OBJECT):
        OBJECT.setObjectName('PortSelect')
        OBJECT.setMaximumSize(400, 225)
        OBJECT.setMinimumSize(350, 200)
        OBJECT.resize(450, 250)

        # Ports label
        self.portsLabel = QtWidgets.QLabel()
        _font = QtGui.QFont()
        _font.setPointSize(12)
        self.portsLabel.setFont(_font)
        _sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        _sizePolicy.setHorizontalStretch(0)
        _sizePolicy.setVerticalStretch(0)
        _sizePolicy.setHeightForWidth(self.portsLabel.sizePolicy().hasHeightForWidth())
        self.portsLabel.setSizePolicy(_sizePolicy)

        # Port list displayed as a combobox        
        self.portsComboList = QtWidgets.QComboBox()
        _sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        _sizePolicy.setHorizontalStretch(0)
        _sizePolicy.setVerticalStretch(0)
        _sizePolicy.setHeightForWidth(self.portsComboList.sizePolicy().hasHeightForWidth())
        self.portsComboList.setSizePolicy(_sizePolicy)

        # Open button
        self.portOpenButton = QtWidgets.QPushButton()

        # Refresh button
        self.portsRefreshButton = QtWidgets.QPushButton()
        _sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        _sizePolicy.setHorizontalStretch(0)
        _sizePolicy.setVerticalStretch(0)
        _sizePolicy.setHeightForWidth(self.portsRefreshButton.sizePolicy().hasHeightForWidth())
        self.portsRefreshButton.setSizePolicy(_sizePolicy)

        # UI STRUCTURE
        self.container = QtWidgets.QVBoxLayout(OBJECT)
        self.container.setContentsMargins(30,30,30,30)
        self.portsLabelLayout = QtWidgets.QHBoxLayout()
        self.portsViewLayout = QtWidgets.QHBoxLayout()
        self.portsRefreshLayout = QtWidgets.QHBoxLayout()
        self.portsRefreshLayout.setContentsMargins(0,10,0,0) # LTRB

        # Add the created ui objects to their respective layout items
        self.portsLabelLayout.addWidget(self.portsLabel)
        self.portsViewLayout.addWidget(self.portsComboList)
        self.portsViewLayout.addWidget(self.portOpenButton)
        self.portsRefreshLayout.addWidget(self.portsRefreshButton)
        
        # Add the layouts to the container layout
        self.container.addLayout(self.portsLabelLayout)
        self.container.addLayout(self.portsViewLayout)
        self.container.addLayout(self.portsRefreshLayout)

        self.retranslateUi(OBJECT)
        QtCore.QMetaObject.connectSlotsByName(OBJECT)

        return

    def retranslateUi(self, OBJECT):
        _translate = QtCore.QCoreApplication.translate

        self.portsLabel.setText(_translate('PortSelect', 'Available Ports'))
        self.portOpenButton.setText(_translate('PortSelect', 'Open'))
        self.portsRefreshButton.setText(_translate('PortSelect', 'Refresh'))

        return


if __name__ == "__main__":
    import sys
    APP = QtWidgets.QApplication(sys.argv)
    MAIN = QtWidgets.QDialog()
    ui = Ui_PortSelect()
    ui.setupUi(MAIN)
    MAIN.show()
    sys.exit(APP.exec_())
