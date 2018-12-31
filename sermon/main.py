from PyQt5 import QtCore, QtWidgets
from sermon.mainWindow import MainWindow

if __name__ == "__main__":
    import sys
    QtCore.QCoreApplication.setApplicationName('Sermon')
    APP = QtWidgets.QApplication(sys.argv)
    # APP.setStyleSheet(stylesheet)
    MAIN = MainWindow()
    MAIN.show()
    sys.exit(APP.exec_())
