# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\ormet\source\svi_meteo_19_11_2015\svi_vs_v.0.6.5\forms\fmIonMessageOK.ui'
#
# Created: Fri Jul  1 16:23:17 2016
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
        fmIonMessageOK.resize(409, 186)
        fmIonMessageOK.setMinimumSize(QtCore.QSize(409, 186))
        fmIonMessageOK.setMaximumSize(QtCore.QSize(409, 186))
        self.centralwidget = QtGui.QWidget(fmIonMessageOK)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tbSave = QtGui.QToolButton(self.centralwidget)
        self.tbSave.setGeometry(QtCore.QRect(120, 610, 361, 22))
        self.tbSave.setObjectName(_fromUtf8("tbSave"))
        self.lblMessage = QtGui.QLabel(self.centralwidget)
        self.lblMessage.setGeometry(QtCore.QRect(10, 40, 391, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblMessage.setFont(font)
        self.lblMessage.setObjectName(_fromUtf8("lblMessage"))
        self.lblMessage_1 = QtGui.QLabel(self.centralwidget)
        self.lblMessage_1.setGeometry(QtCore.QRect(10, 70, 391, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblMessage_1.setFont(font)
        self.lblMessage_1.setText(_fromUtf8(""))
        self.lblMessage_1.setObjectName(_fromUtf8("lblMessage_1"))
        self.tbOK = QtGui.QPushButton(self.centralwidget)
        self.tbOK.setGeometry(QtCore.QRect(160, 110, 75, 23))
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

