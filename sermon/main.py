#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtCore import QCoreApplication, QMetaObject, Qt
from PyQt5.QtGui import QFont, QIcon, QPixmap
from PyQt5.QtWidgets import (QAction, QDesktopWidget, QMainWindow, QMenu,
                             QMessageBox, QSizePolicy, QWidget, QVBoxLayout, 
                             QHBoxLayout, QLabel, QDesktopWidget, QApplication)
from app import SermonApp
from about import AboutDialog


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setObjectName('MainWindow')

        self.sermonApp = SermonApp()
        self.aboutDialog = AboutDialog()

        self.initMenusAndStatusbar()
        self.bindMenuActions()
        self.attachUiEvents()
        # self.setIcon("icon.png")

        self.setCentralWidget(self.sermonApp)
        self.retranslateUi()
        QMetaObject.connectSlotsByName(self)

        self.centerWindow()
        self.show()
    
    def initMenusAndStatusbar(self):
        # statusbar
        self.statusbar = self.statusBar()
        # meunbar
        self.menubar = self.menuBar()
        self.appMenu = QMenu(self.menubar)
        self.setMenuBar(self.menubar)
        # meun actions
        self.exitAction = QAction(self)
        self.aboutAction = QAction(self)

    def setIcon(self, file_name):
        icon = QIcon()
        icon_image = self.core_ui.assets_path + file_name
        icon.addPixmap(QPixmap(icon_image), QIcon.Normal, QIcon.Off)
        self.setWindowIcon(icon)
        return

    def retranslateUi(self):
        ''' UI Text '''
        _translate = QCoreApplication.translate
        self.setWindowTitle('Sermon')
        # Menubar
        self.appMenu.setTitle(_translate('MainUI', 'Sermon'))
        self.exitAction.setText(_translate('MainUI', 'Exit'))
        self.exitAction.setShortcut(_translate('MainUI', 'Ctrl+Q'))
        self.aboutAction.setText(_translate('MainUI', 'About'))
        self.aboutAction.setShortcut(_translate('MainUI', 'Ctrl+A'))

    def bindMenuActions(self):
        # Add menu options
        self.appMenu.addAction(self.aboutAction) # about
        self.appMenu.addSeparator()
        self.appMenu.addAction(self.exitAction) # exit
        # Add menu to MainUI Window
        self.menubar.addAction(self.appMenu.menuAction())
        return

    def attachUiEvents(self):
        ''' Attach MainUI Ui events '''
        ## Menubar
        self.aboutAction.triggered.connect(self.openAboutWindow)
        self.exitAction.triggered.connect(self.close)
        return

    def centerWindow(self):
        ''' Centers the window on the screen '''
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width()-size.width())/3, (screen.height()-size.height())/4)
        return

    def closeEvent(self, event):
        ''' Close program dialog box '''
        reply = QMessageBox.question(self, 'Exit ?', "Are you sure to quit?", \
        QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()
        return

    def openAboutWindow(self):
        ''' Open about window '''
        self.aboutDialog.show()
        return

if __name__ == "__main__":
    APP = QApplication(sys.argv)
    MAIN = MainWindow()
    sys.exit(APP.exec_())
