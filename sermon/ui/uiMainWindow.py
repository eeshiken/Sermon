from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, OBJECT):
        OBJECT.setObjectName('MainWindow')
        # OBJECT.setMaximumSize(400, 225)
        OBJECT.setMinimumSize(350, 250)
        OBJECT.resize(450, 250)

        self.createActions(OBJECT)
        self.createMenu(OBJECT)
        self.statusbar = OBJECT.statusBar()

        self.retranslateUi(OBJECT)
        QtCore.QMetaObject.connectSlotsByName(OBJECT)
        return
    
    def createActions(self, OBJECT):
        self.actionAbout = QtWidgets.QAction(OBJECT)
        self.actionExit = QtWidgets.QAction(OBJECT)
        return
    
    def createMenu(self, OBJECT):
        self.menubar = OBJECT.menuBar()

        self.fileMenu = QtWidgets.QMenu(self.menubar)
        self.fileMenu.addAction(self.actionAbout)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.actionExit)

        self.menubar.addAction(self.fileMenu.menuAction())
        return

    def retranslateUi(self, OBJECT):
        _tr = QtCore.QCoreApplication.translate
        OBJECT.setWindowTitle(_tr('MainWindow', 'Sermon: Serial Monitor'))
        self.fileMenu.setTitle(_tr('MainWindow', 'File'))
        self.actionAbout.setText(_tr('MainWindow', 'About'))
        self.actionExit.setText(_tr('MainWindow', 'Exit'))
        return
    

if __name__ == "__main__":
    import sys
    APP = QtWidgets.QApplication(sys.argv)
    MAIN = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MAIN)
    MAIN.show()
    sys.exit(APP.exec_())
