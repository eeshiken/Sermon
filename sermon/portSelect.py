from PyQt5 import QtCore, QtGui, QtWidgets, QtSerialPort
from sermon.ui.uiPortSelect import Ui_PortSelect


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
        self.settings['baudRate'] = self.baudRatesList.itemData( int(self.baudRatesList.currentIndex()) )
        self.settings['dataBits'] = self.dataBitsList.itemData( int(self.dataBitsList.currentIndex()) )
        return


if __name__ == "__main__":
    import sys
    APP = QtWidgets.QApplication(sys.argv)
    MAIN = PortSelect()
    MAIN.show()
    sys.exit(APP.exec_())
