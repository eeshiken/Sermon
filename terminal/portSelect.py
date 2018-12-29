from PyQt5 import QtCore, QtGui, QtWidgets, QtSerialPort
from terminal.ui.uiPortSelect import Ui_PortSelect


class PortSelect(QtWidgets.QDialog, Ui_PortSelect):
    name = None
    baudRate = None
    dataBits = None

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.serialInfo = QtSerialPort.QSerialPortInfo()
        self.fillPortsInfo()
        self.fillPortsParameters()
    
    def updateSettings(self):
        pass
        return
    
    def fillPortsInfo(self):
        self.portsInfoList.clear()     
        for info in self.serialInfo.availablePorts():
            description = info.description()
            manufacturer = info.manufacturer()
            serialNumber = info.serialNumber()
            pList = [
                info.portName(),
                info.description() if info.description() else "",
                info.manufacturer() if info.manufacturer() else "",
                info.serialNumber() if info.serialNumber() else "",
                info.systemLocation(),
                int(info.vendorIdentifier()) if info.hasVendorIdentifier() else "",
                int(info.productIdentifier()) if info.hasProductIdentifier() else "",
            ]
            self.portsInfoList.addItem(pList[0], pList)
            print(pList)
        return
    
    def fillPortsParameters(self):
        stdRates = self.serialInfo.standardBaudRates()
        MIN = 9600
        MAX = 115200
        rates = stdRates[stdRates.index(MIN):stdRates.index(MAX)+1]
        
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

if __name__ == "__main__":
    import sys
    APP = QtWidgets.QApplication(sys.argv)
    MAIN = PortSelect()
    MAIN.show()
    sys.exit(APP.exec_())
