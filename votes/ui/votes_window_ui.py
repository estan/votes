# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/estan/Projekt/votes/votes/ui/votes_window.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_VotesWindow(object):
    def setupUi(self, VotesWindow):
        VotesWindow.setObjectName("VotesWindow")
        VotesWindow.setEnabled(False)
        VotesWindow.resize(540, 331)
        self.centralwidget = QtWidgets.QWidget(VotesWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName("gridLayout")
        self.bananaVotes = QtWidgets.QLabel(self.centralwidget)
        self.bananaVotes.setMinimumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.bananaVotes.setFont(font)
        self.bananaVotes.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.bananaVotes.setObjectName("bananaVotes")
        self.gridLayout.addWidget(self.bananaVotes, 2, 0, 1, 1)
        self.chocolateVotes = QtWidgets.QLabel(self.centralwidget)
        self.chocolateVotes.setMinimumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.chocolateVotes.setFont(font)
        self.chocolateVotes.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.chocolateVotes.setObjectName("chocolateVotes")
        self.gridLayout.addWidget(self.chocolateVotes, 2, 1, 1, 1)
        self.lemonVotes = QtWidgets.QLabel(self.centralwidget)
        self.lemonVotes.setMinimumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lemonVotes.setFont(font)
        self.lemonVotes.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.lemonVotes.setObjectName("lemonVotes")
        self.gridLayout.addWidget(self.lemonVotes, 2, 2, 1, 1)
        self.resetButton = QtWidgets.QPushButton(self.centralwidget)
        self.resetButton.setObjectName("resetButton")
        self.gridLayout.addWidget(self.resetButton, 3, 0, 1, 3)
        self.bananaLabel = QtWidgets.QLabel(self.centralwidget)
        self.bananaLabel.setMinimumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.bananaLabel.setFont(font)
        self.bananaLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.bananaLabel.setObjectName("bananaLabel")
        self.gridLayout.addWidget(self.bananaLabel, 1, 0, 1, 1)
        self.chocolateLabel = QtWidgets.QLabel(self.centralwidget)
        self.chocolateLabel.setMinimumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.chocolateLabel.setFont(font)
        self.chocolateLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.chocolateLabel.setObjectName("chocolateLabel")
        self.gridLayout.addWidget(self.chocolateLabel, 1, 1, 1, 1)
        self.lemonLabel = QtWidgets.QLabel(self.centralwidget)
        self.lemonLabel.setMinimumSize(QtCore.QSize(50, 50))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lemonLabel.setFont(font)
        self.lemonLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.lemonLabel.setObjectName("lemonLabel")
        self.gridLayout.addWidget(self.lemonLabel, 1, 2, 1, 1)
        self.chocolateButton = QtWidgets.QPushButton(self.centralwidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/votes/images/chocolate_small.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.chocolateButton.setIcon(icon)
        self.chocolateButton.setIconSize(QtCore.QSize(160, 160))
        self.chocolateButton.setObjectName("chocolateButton")
        self.gridLayout.addWidget(self.chocolateButton, 0, 1, 1, 1)
        self.lemonButton = QtWidgets.QPushButton(self.centralwidget)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/votes/images/lemon_small.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.lemonButton.setIcon(icon1)
        self.lemonButton.setIconSize(QtCore.QSize(160, 160))
        self.lemonButton.setObjectName("lemonButton")
        self.gridLayout.addWidget(self.lemonButton, 0, 2, 1, 1)
        self.bananaButton = QtWidgets.QPushButton(self.centralwidget)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/votes/images/banana_small.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.bananaButton.setIcon(icon2)
        self.bananaButton.setIconSize(QtCore.QSize(160, 160))
        self.bananaButton.setObjectName("bananaButton")
        self.gridLayout.addWidget(self.bananaButton, 0, 0, 1, 1)
        VotesWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(VotesWindow)
        self.statusbar.setObjectName("statusbar")
        VotesWindow.setStatusBar(self.statusbar)

        self.retranslateUi(VotesWindow)
        QtCore.QMetaObject.connectSlotsByName(VotesWindow)

    def retranslateUi(self, VotesWindow):
        _translate = QtCore.QCoreApplication.translate
        VotesWindow.setWindowTitle(_translate("VotesWindow", "Votes Demo"))
        self.bananaVotes.setText(_translate("VotesWindow", "0"))
        self.chocolateVotes.setText(_translate("VotesWindow", "0"))
        self.lemonVotes.setText(_translate("VotesWindow", "0"))
        self.resetButton.setToolTip(_translate("VotesWindow", "Reset all vote counters"))
        self.resetButton.setText(_translate("VotesWindow", "Reset"))
        self.bananaLabel.setText(_translate("VotesWindow", "Banana"))
        self.chocolateLabel.setText(_translate("VotesWindow", "Chocolate"))
        self.lemonLabel.setText(_translate("VotesWindow", "Lemon"))
        self.chocolateButton.setToolTip(_translate("VotesWindow", "Vote for Chocolate"))
        self.lemonButton.setToolTip(_translate("VotesWindow", "Vote for Lemon"))
        self.bananaButton.setToolTip(_translate("VotesWindow", "Vote for Banana"))

from . import votes_rc
