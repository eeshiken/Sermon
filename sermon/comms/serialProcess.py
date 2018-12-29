from PyQt5 import QtCore
import serial


class SerialProcess(QtCore.QObject):
    alive = None
    finished = QtCore.pyqtSignal()

    def __init__(self, devicePort):
        super().__init__()
        self.alive = True
        self.databytes = 6
        
        try:
            self.conn = serial.Serial(devicePort, baudrate=115200, timeout=1)
        except serial.SerialException:
            print("Serial Error")

    def run(self):
        while self.alive:
            print(1)
            pass

        self.finished.emit()
        return

    def stop(self):
        self.alive = False
        return
    
    def isAlive(self):
        return self.alive == True
    
    def isNotAlive(self):
        return self.alive == False
