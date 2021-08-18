# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainView.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1125, 774)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.setMediaLibraryBtn = QPushButton(self.centralwidget)
        self.setMediaLibraryBtn.setObjectName(u"setMediaLibraryBtn")
        self.setMediaLibraryBtn.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_3.addWidget(self.setMediaLibraryBtn)

        self.mediaLibraryLbl = QLabel(self.centralwidget)
        self.mediaLibraryLbl.setObjectName(u"mediaLibraryLbl")

        self.horizontalLayout_3.addWidget(self.mediaLibraryLbl)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.addMediaBtn = QPushButton(self.centralwidget)
        self.addMediaBtn.setObjectName(u"addMediaBtn")

        self.horizontalLayout.addWidget(self.addMediaBtn)

        self.commitMediaBtn = QPushButton(self.centralwidget)
        self.commitMediaBtn.setObjectName(u"commitMediaBtn")

        self.horizontalLayout.addWidget(self.commitMediaBtn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.libraryViewCurrentDirLbl = QLabel(self.centralwidget)
        self.libraryViewCurrentDirLbl.setObjectName(u"libraryViewCurrentDirLbl")

        self.verticalLayout_2.addWidget(self.libraryViewCurrentDirLbl)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.libraryView = QTreeView(self.centralwidget)
        self.libraryView.setObjectName(u"libraryView")

        self.horizontalLayout_2.addWidget(self.libraryView)

        self.newMediaView = QListView(self.centralwidget)
        self.newMediaView.setObjectName(u"newMediaView")

        self.horizontalLayout_2.addWidget(self.newMediaView)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1125, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.setMediaLibraryBtn.setText(QCoreApplication.translate("MainWindow", u"Set Media Library", None))
        self.mediaLibraryLbl.setText("")
        self.addMediaBtn.setText(QCoreApplication.translate("MainWindow", u"Add Media", None))
        self.commitMediaBtn.setText(QCoreApplication.translate("MainWindow", u"Commit", None))
        self.libraryViewCurrentDirLbl.setText("")
    # retranslateUi

