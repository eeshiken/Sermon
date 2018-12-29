from PyQt5 import QtCore, QtGui, QtWidgets
from terminal.ui.uiPortMonitor import Ui_PortMonitor


class PortMonitor(QtWidgets.QDialog, Ui_PortMonitor):
    def __init__(self, NAME):
        super().__init__()
        self.setupUi(self)
        self.fillLineEndings()
        _tr = QtCore.QCoreApplication.translate
        self.setWindowTitle(_tr('PortMonitor', NAME))
    
    def fillLineEndings(self):
        self.lineEndList.addItem('No line ending')
        self.lineEndList.addItem('Newline \\n')
        self.lineEndList.addItem('Newline & Return \\n\\r')
        self.lineEndList.setCurrentIndex(1)
        return


if __name__ == "__main__":
    import sys
    APP = QtWidgets.QApplication(sys.argv)
    MAIN = PortSelect()
    MAIN.show()
    sys.exit(APP.exec_())
