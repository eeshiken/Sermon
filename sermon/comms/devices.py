from serial.tools.list_ports import comports

class SerialDevices(object):
    def __init__(self):
        self.devicePort = None
        self.refreshPorts()
        
    def refreshPorts(self):
        try:
            self.ports, self.descriptions, self.metas = zip(*comports())
        except ValueError: # No ports connected
            self.ports = []
            self.descriptions = []
            self.metas = []
            print("No serial ports found")
