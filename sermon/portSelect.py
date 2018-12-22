from PyQt5 import QtCore, QtGui, QtWidgets
from sermon.ui.uiPortSelect import Ui_PortSelect
from sermon.comms.devices import SerialDevices


class PortSelect(QtWidgets.QDialog, Ui_PortSelect):
    serialDevices = None

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.serialDevices = SerialDevices()
        self.updatePortList()
        self.__bindEventHandlers()

    def __bindEventHandlers(self):
        self.portOpenButton.clicked.connect(self.__openBtnClickedEvent)
        self.portsRefreshButton.clicked.connect(self.__refreshBtnClickedEvent)
        return

    def __openBtnClickedEvent(self):
        print('Open')
        # Selct port from combolist
        # open port on the serial thread
        # Show thread window
        return
    
    def __refreshBtnClickedEvent(self):
        print('refresh')
        self.serialDevices.refreshPorts()
        self.updatePortList()
        return

    def updatePortList(self):
        self.portsComboList.clear()
        for portDescription in self.serialDevices.descriptions:
            self.portsComboList.addItems([portDescription])
        return


if __name__ == "__main__":
    import sys
    APP = QtWidgets.QApplication(sys.argv)
    MAIN = PortSelect()
    MAIN.show()
    sys.exit(APP.exec_())
