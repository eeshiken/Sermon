from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, OBJECT):
        OBJECT.setObjectName('MainWindow')
        # OBJECT.setMaximumSize(400, 225)
        OBJECT.setMinimumSize(350, 200)
        OBJECT.resize(450, 250)

        self.statusbar = OBJECT.statusBar()

        self.createActions(OBJECT)
        self.createMenu(OBJECT)

        self.retranslateUi(OBJECT)
        QtCore.QMetaObject.connectSlotsByName(OBJECT)
        return
    
    def createActions(self, OBJECT):
        self.aboutAction = QtWidgets.QAction(OBJECT)
        self.exitAction = QtWidgets.QAction(OBJECT)
        return
    
    def createMenu(self, OBJECT):
        self.menubar = OBJECT.menuBar()

        self.fileMenu = QtWidgets.QMenu(self.menubar)
        self.fileMenu.addAction(self.aboutAction)
        self.fileMenu.addSeparator()
        self.fileMenu.addAction(self.exitAction)

        self.menubar.addAction(self.fileMenu.menuAction())
        return

    def retranslateUi(self, OBJECT):
        _tr = QtCore.QCoreApplication.translate
        OBJECT.setWindowTitle(_tr('MainWindow', 'Sermon: Serial Monitor'))
        self.fileMenu.setTitle(_tr('MainWindow', 'File'))
        self.aboutAction.setText(_tr('MainWindow', 'About'))
        self.exitAction.setText(_tr('MainWindow', 'Exit'))
        return

    def closeEvent(self, event):
        reply = QtWidgets.QMessageBox.question(self, 
            'Exit ?', "Are you sure to quit?",
            QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No, QtWidgets.QMessageBox.No)

        if reply == QtWidgets.QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
        return
    

if __name__ == "__main__":
    import sys
    APP = QtWidgets.QApplication(sys.argv)
    MAIN = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MAIN)
    MAIN.show()
    sys.exit(APP.exec_())
