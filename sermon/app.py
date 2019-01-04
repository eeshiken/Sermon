import sys
from PyQt5 import QtCore, QtWidgets
from sermon import __version__
from sermon.interface.mainWindow import MainWindow


def run():
    APP = QtWidgets.QApplication(sys.argv)
    APP.setApplicationName('Sermon')
    APP.setApplicationVersion(__version__)

    MAIN = MainWindow()

    MAIN.show()
    sys.exit(APP.exec_())

if __name__ == "__main__":
    run()
