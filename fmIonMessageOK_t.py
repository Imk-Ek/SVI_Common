# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\__2018\NB2\svi\forms\fmIonMessageOK.ui'
#
# Created: Tue Sep 18 14:22:59 2018
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_fmIonMessageOK(object):
    def setupUi(self, fmIonMessageOK):
        fmIonMessageOK.setObjectName(_fromUtf8("fmIonMessageOK"))
        fmIonMessageOK.resize(900, 322)
        fmIonMessageOK.setMinimumSize(QtCore.QSize(900, 322))
        fmIonMessageOK.setMaximumSize(QtCore.QSize(900, 322))
        self.centralwidget = QtGui.QWidget(fmIonMessageOK)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tbSave = QtGui.QToolButton(self.centralwidget)
        self.tbSave.setGeometry(QtCore.QRect(120, 610, 361, 22))
        self.tbSave.setObjectName(_fromUtf8("tbSave"))
        self.lblMessage = QtGui.QLabel(self.centralwidget)
        self.lblMessage.setGeometry(QtCore.QRect(20, 40, 861, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblMessage.setFont(font)
        self.lblMessage.setObjectName(_fromUtf8("lblMessage"))
        self.lblMessage_1 = QtGui.QLabel(self.centralwidget)
        self.lblMessage_1.setGeometry(QtCore.QRect(20, 70, 861, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblMessage_1.setFont(font)
        self.lblMessage_1.setText(_fromUtf8(""))
        self.lblMessage_1.setObjectName(_fromUtf8("lblMessage_1"))
        self.tbOK = QtGui.QPushButton(self.centralwidget)
        self.tbOK.setGeometry(QtCore.QRect(360, 230, 115, 51))
        self.tbOK.setObjectName(_fromUtf8("tbOK"))
        fmIonMessageOK.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(fmIonMessageOK)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        fmIonMessageOK.setStatusBar(self.statusbar)

        self.retranslateUi(fmIonMessageOK)
        QtCore.QMetaObject.connectSlotsByName(fmIonMessageOK)

    def retranslateUi(self, fmIonMessageOK):
        fmIonMessageOK.setWindowTitle(_translate("fmIonMessageOK", "Результат градуировки", None))
        self.tbSave.setText(_translate("fmIonMessageOK", "Сохранить в энергонезависимой памяти", None))
        self.lblMessage.setText(_translate("fmIonMessageOK", "Другое число", None))
        self.tbOK.setText(_translate("fmIonMessageOK", "OK", None))

