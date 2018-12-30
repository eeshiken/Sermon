from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, OBJECT):
        OBJECT.setObjectName('MainWindow')
        # OBJECT.setMaximumSize(400, 225)
        OBJECT.setMinimumSize(350, 250)
        OBJECT.resize(350, 250)

        self.createActions(OBJECT)
        self.createMenu(OBJECT)
        self.statusbar = OBJECT.statusBar()

        ##
        self.emojiCon()
        ##

        self.retranslateUi(OBJECT)
        QtCore.QMetaObject.connectSlotsByName(OBJECT)
        return
    
    def createActions(self, OBJECT):
        self.actionAbout = QtWidgets.QAction(OBJECT)
        self.actionAbout.setShortcuts(QtGui.QKeySequence(QtCore.Qt.CTRL + QtCore.Qt.Key_A))
        self.actionAboutQt = QtWidgets.QAction(OBJECT)
        self.actionAboutQt.setShortcuts(QtGui.QKeySequence(QtCore.Qt.CTRL + QtCore.Qt.SHIFT + QtCore.Qt.Key_A))
        self.actionExit = QtWidgets.QAction(OBJECT)
        self.actionExit.setShortcuts(QtGui.QKeySequence(QtCore.Qt.CTRL + QtCore.Qt.Key_E))
        self.actionEmojicon = QtWidgets.QAction(OBJECT)
        self.actionEmojicon.setShortcuts(QtGui.QKeySequence(QtCore.Qt.CTRL + QtCore.Qt.Key_Y))
        return
    
    def createMenu(self, OBJECT):
        self.menubar = OBJECT.menuBar()

        self.fileMenu = QtWidgets.QMenu(self.menubar)
        self.fileMenu.addAction(self.actionExit)
        # self.fileMenu.addAction(self.actionEmojicon)

        self.helpMenu = QtWidgets.QMenu(self.menubar)
        self.helpMenu.addAction(self.actionAbout)
        self.helpMenu.addAction(self.actionAboutQt)

        self.menubar.addAction(self.fileMenu.menuAction())
        self.menubar.addAction(self.helpMenu.menuAction())
    
        return

    def retranslateUi(self, OBJECT):
        _tr = QtCore.QCoreApplication.translate
        OBJECT.setWindowTitle(_tr('MainWindow', 'Sermon: Serial Monitor'))
        self.fileMenu.setTitle(_tr('MainWindow', 'File'))
        self.helpMenu.setTitle(_tr('MainWindow', 'Help'))
        self.actionAbout.setText(_tr('MainWindow', 'About'))
        self.actionAbout.setShortcut(_tr('MainWindow', 'Ctrl+A'))
        self.actionAboutQt.setText(_tr('MainWindow', 'About Qt'))
        self.actionAboutQt.setShortcut(_tr('MainWindow', 'Ctrl+Shift+A'))
        self.actionExit.setText(_tr('MainWindow', 'Exit'))
        self.actionExit.setShortcut(_tr('MainWindow', 'Ctrl+E'))
        return
    
    def emojiCon(self):
        self.emojilib = [
            "lipstick",
            "memo"
        ]
        return
    
    def getRandomEmoji(self) -> str:
        index = random.randrange(len(self.emojilib))
        return self.emojilib[index]
    

if __name__ == "__main__":
    import sys
    APP = QtWidgets.QApplication(sys.argv)
    MAIN = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MAIN)
    MAIN.show()
    sys.exit(APP.exec_())
