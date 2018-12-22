from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, OBJECT):
        OBJECT.setObjectName('MainWindow')
        OBJECT.setMaximumSize(400, 225)
        OBJECT.setMinimumSize(350, 200)
        OBJECT.resize(450, 250)

        self.statusbar = OBJECT.statusBar()
        self.menubar = OBJECT.menuBar()

        self.retranslateUi(OBJECT)
        QtCore.QMetaObject.connectSlotsByName(OBJECT)

        return

    def retranslateUi(self, OBJECT):
        _translate = QtCore.QCoreApplication.translate
        OBJECT.setWindowTitle(_translate('MainWindow', 'Sermon: Serial Monitor'))

        return

    def setIcon(self, file_name):
        icon = QtGui.QIcon()
        icon_image = file_name
        icon.addPixmap(QtGui.QPixmap(icon_image), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.setWindowIcon(icon)

        return
    
    def closeEvent(self, event):
        '''Overides the close() function, and creates a dialog to
        confirm the exit function'''
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
