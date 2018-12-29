from PyQt5 import QtCore, QtGui, QtWidgets
from sermon.ui.uiPortSelect import Ui_PortSelect
from sermon.comms.devices import SerialDevices
from sermon.portMonitor import PortMonitor


class PortSelect(QtWidgets.QDialog, Ui_PortSelect):
    serialDevices = None
    selectedPort = None
    portOpen = False

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
        self.serialDevices.refreshPorts()

        try:
            selectedPortDescription = self.portsComboList.itemText(self.portsComboList.currentIndex())
            indexOfSelected = self.serialDevices.descriptions.index(selectedPortDescription)
            self.serialDevices.devicePort = self.serialDevices.ports[indexOfSelected]
        except ValueError:
            print("Port selection error")
            return

        print(f'Open: {self.serialDevices.devicePort}, Index: {indexOfSelected}')

        if self.portNotOpen():
            self.portOpen = True
            self.portMonitor = PortMonitor(self.serialDevices.devicePort)
            self.portMonitor.show()
            self.portMonitor.closed.connect(self.portMonitorClosed)
        else:
            print("Port already open")
        return
    
    def closeEvent(self, event):
        self.portMonitor.serialProcess.stop()

    def portMonitorClosed(self):
        self.portOpen = False
        return
    
    def __refreshBtnClickedEvent(self):
        print('Refresh')
        self.serialDevices.refreshPorts()
        self.updatePortList()
        return

    def updatePortList(self):
        self.portsComboList.clear()
        for portDescription in self.serialDevices.descriptions:
            self.portsComboList.addItems([portDescription])
        return

    def portIsOpen(self):
        return self.portOpen == True
    
    def portNotOpen(self):
        return self.portOpen == False


if __name__ == "__main__":
    import sys
    APP = QtWidgets.QApplication(sys.argv)
    MAIN = PortSelect()
    MAIN.show()
    sys.exit(APP.exec_())
