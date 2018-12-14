
from PyQt5.QtCore import QCoreApplication, QMetaObject, Qt
from PyQt5.QtGui import QFont, QIcon, QPixmap
from PyQt5.QtWidgets import (QAction, QDesktopWidget, QMainWindow, QMenu, \
                             QMessageBox, QSizePolicy, QWidget, QVBoxLayout, 
                             QHBoxLayout, QLabel)

from __version__ import __version__

class AboutDialog(QWidget):
    ''' About Interface '''
    def __init__(self):
        super().__init__()
        self.setObjectName("AboutDialog")
        self.resize(849, 472)
        self.about_box = QVBoxLayout(self)
        self.about_box.setObjectName("about_box")
        self.about_system_label = QLabel()
        self.about_system_label.setAlignment(Qt.AlignCenter)
        self.about_system_label.setObjectName("about_system_label")
        self.about_box.addWidget(self.about_system_label)

        self.retranslate_ui()
        QMetaObject.connectSlotsByName(self)

    def retranslate_ui(self):
        ''' Text content '''
        _translate = QCoreApplication.translate
        self.setWindowTitle(_translate("about_dialog", "Sermon"))
        self.about_system_label.setText(_translate("about_dialog", f"Sermon\nSerial Monitor\nv{__version__}"))
