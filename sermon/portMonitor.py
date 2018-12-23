from PyQt5 import QtCore, QtGui, QtWidgets
from sermon.ui.uiPortMonitor import Ui_PortMonitor
import time

class PortMonitor(QtWidgets.QWidget, Ui_PortMonitor):
    closed = QtCore.pyqtSignal()

    def __init__(self, port):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle(port)
        self.setupSerialProcess()
        self.serialThread.start()

    def setupSerialProcess(self):
        self.serialThread = QtCore.QThread()
        self.serialProcess = SerialProcess()
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

class SerialProcess(QtCore.QObject):
    alive = None
    finished = QtCore.pyqtSignal()

    def run(self):
        self.alive = True

        while self.alive:
            print(1)
            pass

        self.finished.emit()
        return
    
    def isAlive(self):
        return self.alive == True
    
    def isNotAlive(self):
        return self.alive == False
    
    def stop(self):
        self.alive = False
        return
