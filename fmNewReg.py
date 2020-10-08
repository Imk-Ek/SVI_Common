# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fmNewReg.ui'
#
# Created: Thu Dec 27 12:47:20 2012
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_dgNewReg(object):
    def setupUi(self, dgNewReg):
        dgNewReg.setObjectName(_fromUtf8("dgNewReg"))
        dgNewReg.resize(285, 129)
        self.gridLayout = QtGui.QGridLayout(dgNewReg)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(dgNewReg)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.leDevAddr = QtGui.QLineEdit(dgNewReg)
        self.leDevAddr.setObjectName(_fromUtf8("leDevAddr"))
        self.gridLayout.addWidget(self.leDevAddr, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(dgNewReg)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.leRegAddr = QtGui.QLineEdit(dgNewReg)
        self.leRegAddr.setObjectName(_fromUtf8("leRegAddr"))
        self.gridLayout.addWidget(self.leRegAddr, 1, 1, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(dgNewReg)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setCenterButtons(False)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 2)

        self.retranslateUi(dgNewReg)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), dgNewReg.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), dgNewReg.reject)
        QtCore.QMetaObject.connectSlotsByName(dgNewReg)

    def retranslateUi(self, dgNewReg):
        dgNewReg.setWindowTitle(QtGui.QApplication.translate("dgNewReg", "Новый регистр", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("dgNewReg", "Адрес измерителя на шине:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("dgNewReg", "Адрес регистра:", None, QtGui.QApplication.UnicodeUTF8))

