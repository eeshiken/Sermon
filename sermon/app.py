#!/usr/bin/python3
# -*- coding: utf-8 -*-

from PyQt5.QtCore import QCoreApplication, QMetaObject, Qt
from PyQt5.QtGui import QFont, QIcon, QPixmap
from PyQt5.QtWidgets import (QAction, QDesktopWidget, QMainWindow, QMenu, \
                             QMessageBox, QSizePolicy, QWidget, QVBoxLayout, 
                             QHBoxLayout, QLabel)
from gui import Ui_Sermon


class SermonApp(QWidget, Ui_Sermon):
    ''' Main UI class '''
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.sendButton.clicked.connect(self.btnClickedEvent)

    def btnClickedEvent(self):
        pass
