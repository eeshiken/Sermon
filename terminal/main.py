from PyQt5 import QtWidgets
from terminal.mainWindow import MainWindow

if __name__ == "__main__":
    import sys
    APP = QtWidgets.QApplication(sys.argv)    
    MAIN = MainWindow()
    MAIN.show()
    sys.exit(APP.exec_())
