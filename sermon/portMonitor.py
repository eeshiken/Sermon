from PyQt5 import QtCore, QtGui, QtWidgets
from sermon.ui.uiPortMonitor import Ui_PortMonitor
import time

class PortMonitor(QtWidgets.QWidget, Ui_PortMonitor):
    closed = QtCore.pyqtSignal()
    devicePort = None

    def __init__(self, port):
        super().__init__()
        self.setupUi(self)
        self.devicePort = port
        self.setWindowTitle(self.devicePort)

        self.setupSerialProcess()
        # Start serial
        # self.serialThread.start()

    def setupSerialProcess(self):
        self.serialThread = QtCore.QThread()
        self.serialProcess = SerialProcess(self.devicePort)
        self.serialProcess.moveToThread(self.serialThread)
        self.serialThread.started.connect(self.serialProcess.run)
        self.serialProcess.finished.connect(self.serialThread.quit)
        self.serialThread.finished.connect(self.close)
        return

    def closeEvent(self, event):
        self.serialProcess.stop()
        while self.serialProcess.alive == True:
            pass
        self.closed.emit()
        return
