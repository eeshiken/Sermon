from PyQt5 import QtWidgets
from mainWindow import MainWindow


if __name__ == "__main__":
    import sys
    APP = QtWidgets.QApplication(sys.argv)    
    MAIN = MainWindow()
    sys.exit(APP.exec_())
