# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\__2018\NB2\svi\forms\fmIonMessage.ui'
#
# Created: Tue Sep 18 14:22:53 2018
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

class Ui_fmIonMessage(object):
    def setupUi(self, fmIonMessage):
        fmIonMessage.setObjectName(_fromUtf8("fmIonMessage"))
        fmIonMessage.resize(900, 322)
        fmIonMessage.setMinimumSize(QtCore.QSize(900, 322))
        fmIonMessage.setMaximumSize(QtCore.QSize(900, 322))
        self.centralwidget = QtGui.QWidget(fmIonMessage)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tbSave = QtGui.QToolButton(self.centralwidget)
        self.tbSave.setGeometry(QtCore.QRect(120, 610, 361, 22))
        self.tbSave.setObjectName(_fromUtf8("tbSave"))
        self.lblMessage = QtGui.QLabel(self.centralwidget)
        self.lblMessage.setGeometry(QtCore.QRect(20, 30, 861, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblMessage.setFont(font)
        self.lblMessage.setObjectName(_fromUtf8("lblMessage"))
        self.lblMessage_1 = QtGui.QLabel(self.centralwidget)
        self.lblMessage_1.setGeometry(QtCore.QRect(20, 80, 861, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblMessage_1.setFont(font)
        self.lblMessage_1.setText(_fromUtf8(""))
        self.lblMessage_1.setObjectName(_fromUtf8("lblMessage_1"))
        self.btnOK = QtGui.QPushButton(self.centralwidget)
        self.btnOK.setGeometry(QtCore.QRect(290, 220, 115, 51))
        self.btnOK.setObjectName(_fromUtf8("btnOK"))
        self.btnCancel = QtGui.QPushButton(self.centralwidget)
        self.btnCancel.setGeometry(QtCore.QRect(440, 220, 115, 51))
        self.btnCancel.setObjectName(_fromUtf8("btnCancel"))
        self.lblMessage_2 = QtGui.QLabel(self.centralwidget)
        self.lblMessage_2.setGeometry(QtCore.QRect(20, 120, 861, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblMessage_2.setFont(font)
        self.lblMessage_2.setText(_fromUtf8(""))
        self.lblMessage_2.setObjectName(_fromUtf8("lblMessage_2"))
        fmIonMessage.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(fmIonMessage)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        fmIonMessage.setStatusBar(self.statusbar)

        self.retranslateUi(fmIonMessage)
        QtCore.QMetaObject.connectSlotsByName(fmIonMessage)

    def retranslateUi(self, fmIonMessage):
        fmIonMessage.setWindowTitle(_translate("fmIonMessage", "Значение буфера раствора", None))
        self.tbSave.setText(_translate("fmIonMessage", "Сохранить в энергонезависимой памяти", None))
        self.lblMessage.setText(_translate("fmIonMessage", "Другое число", None))
        self.btnOK.setText(_translate("fmIonMessage", "ОК", None))
        self.btnCancel.setText(_translate("fmIonMessage", "Отмена", None))

