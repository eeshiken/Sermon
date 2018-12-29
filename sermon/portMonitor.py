from PyQt5 import QtCore, QtGui, QtWidgets
from sermon.ui.uiPortMonitor import Ui_PortMonitor


class PortMonitor(QtWidgets.QDialog, Ui_PortMonitor):
    windowClosed = QtCore.pyqtSignal()
    enterPressed = QtCore.pyqtSignal()
    lineEndingOption = None

    def __init__(self, NAME):
        super().__init__()
        self.setupUi(self)

        self.consoleOut.document().setMaximumBlockCount(1000)

        _tr = QtCore.QCoreApplication.translate
        self.setWindowTitle(_tr('PortMonitor', NAME))

        self.fillLineEndings()
        self.updateLineEnding()

        self.lineEndList.currentIndexChanged.connect(self.updateLineEnding)
        self.clearConsoleButton.clicked.connect(self.consoleOut.clear)
    
    def fillLineEndings(self):
        self.lineEndList.addItem('No line ending', 0)
        self.lineEndList.addItem('Newline \\n', 1)
        self.lineEndList.addItem('Newline & Return \\n\\r', 2)
        self.lineEndList.setCurrentIndex(1)
        return
    
    def updateLineEnding(self):
        self.lineEndingOption = self.lineEndList.itemData(int(self.lineEndList.currentData()))
        return

    def putData(self, data: QtCore.QByteArray):
        self.consoleOut.insertPlainText(data)
        self.bar = self.consoleOut.verticalScrollBar()
        self.bar.setValue(self.bar.maximum())
    
    def keyPressEvent(self, event: QtGui.QKeyEvent):
        if (event.key() == QtCore.Qt.Key_Return):
            self.enterPressed.emit()
        return
    
    def closeEvent(self, event: QtGui.QCloseEvent):
        self.windowClosed.emit()
        return


if __name__ == "__main__":
    import sys
    APP = QtWidgets.QApplication(sys.argv)
    MAIN = PortSelect()
    MAIN.show()
    sys.exit(APP.exec_())
