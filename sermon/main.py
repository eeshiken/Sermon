from PyQt5 import QtWidgets
from sermon.mainWindow import MainWindow
from sermon.stylesheet import StyleSheet

if __name__ == "__main__":
    import sys
    APP = QtWidgets.QApplication(sys.argv)    
    # APP.setStyleSheet(StyleSheet) # Uncomment when styling
    MAIN = MainWindow()
    sys.exit(APP.exec_())
