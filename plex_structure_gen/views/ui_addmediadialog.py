# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AddMediaView.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_AddMediaDialog(object):
    def setupUi(self, AddMediaDialog):
        if not AddMediaDialog.objectName():
            AddMediaDialog.setObjectName(u"AddMediaDialog")
        AddMediaDialog.setWindowModality(Qt.WindowModal)
        AddMediaDialog.resize(535, 433)
        self.verticalLayout_2 = QVBoxLayout(AddMediaDialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.searchMovieBtn = QRadioButton(AddMediaDialog)
        self.searchMediaBtnGrp = QButtonGroup(AddMediaDialog)
        self.searchMediaBtnGrp.setObjectName(u"searchMediaBtnGrp")
        self.searchMediaBtnGrp.addButton(self.searchMovieBtn)
        self.searchMovieBtn.setObjectName(u"searchMovieBtn")
        self.searchMovieBtn.setChecked(True)

        self.horizontalLayout.addWidget(self.searchMovieBtn)

        self.searchTvShowBtn = QRadioButton(AddMediaDialog)
        self.searchMediaBtnGrp.addButton(self.searchTvShowBtn)
        self.searchTvShowBtn.setObjectName(u"searchTvShowBtn")

        self.horizontalLayout.addWidget(self.searchTvShowBtn)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.searchMediaInput = QLineEdit(AddMediaDialog)
        self.searchMediaInput.setObjectName(u"searchMediaInput")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.searchMediaInput.sizePolicy().hasHeightForWidth())
        self.searchMediaInput.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.searchMediaInput)

        self.searchBtn = QPushButton(AddMediaDialog)
        self.searchBtn.setObjectName(u"searchBtn")

        self.horizontalLayout_3.addWidget(self.searchBtn)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.groupBox = QGroupBox(AddMediaDialog)
        self.groupBox.setObjectName(u"groupBox")
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.tmdbDbBtn = QRadioButton(self.groupBox)
        self.dbBtnGrp = QButtonGroup(AddMediaDialog)
        self.dbBtnGrp.setObjectName(u"dbBtnGrp")
        self.dbBtnGrp.addButton(self.tmdbDbBtn)
        self.tmdbDbBtn.setObjectName(u"tmdbDbBtn")
        self.tmdbDbBtn.setChecked(True)

        self.horizontalLayout_2.addWidget(self.tmdbDbBtn)

        self.imdbDbBtn = QRadioButton(self.groupBox)
        self.dbBtnGrp.addButton(self.imdbDbBtn)
        self.imdbDbBtn.setObjectName(u"imdbDbBtn")

        self.horizontalLayout_2.addWidget(self.imdbDbBtn)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.foundMediaList = QListWidget(AddMediaDialog)
        self.foundMediaList.setObjectName(u"foundMediaList")
        self.foundMediaList.setSelectionMode(QAbstractItemView.MultiSelection)

        self.verticalLayout_2.addWidget(self.foundMediaList)

        self.buttonBox = QDialogButtonBox(AddMediaDialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout_2.addWidget(self.buttonBox)


        self.retranslateUi(AddMediaDialog)
        self.buttonBox.accepted.connect(AddMediaDialog.accept)
        self.buttonBox.rejected.connect(AddMediaDialog.reject)

        self.searchBtn.setDefault(True)


        QMetaObject.connectSlotsByName(AddMediaDialog)
    # setupUi

    def retranslateUi(self, AddMediaDialog):
        AddMediaDialog.setWindowTitle(QCoreApplication.translate("AddMediaDialog", u"Dialog", None))
        self.searchMovieBtn.setText(QCoreApplication.translate("AddMediaDialog", u"Movie", None))
        self.searchTvShowBtn.setText(QCoreApplication.translate("AddMediaDialog", u"TV Show", None))
        self.searchMediaInput.setPlaceholderText(QCoreApplication.translate("AddMediaDialog", u"Name of media to search for", None))
        self.searchBtn.setText(QCoreApplication.translate("AddMediaDialog", u"Search", None))
        self.groupBox.setTitle(QCoreApplication.translate("AddMediaDialog", u"Db Provider", None))
        self.tmdbDbBtn.setText(QCoreApplication.translate("AddMediaDialog", u"TMDB", None))
        self.imdbDbBtn.setText(QCoreApplication.translate("AddMediaDialog", u"IMDB", None))
    # retranslateUi

