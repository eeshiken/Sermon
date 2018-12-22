from PyQt5 import QtCore, QtGui, QtWidgets
from sermon.ui.uiPortMonitor import Ui_PortMonitor


class PortMonitor(QtWidgets.QWidget, Ui_PortMonitor):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def btnClickedEvent(self):
        pass
