# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\ormet\source\svi_meteo_19_11_2015\svi_vs_v.0.6.5\forms\fmIonMessage.ui'
#
# Created: Fri Jul  1 16:23:11 2016
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
        fmIonMessage.resize(686, 186)
        fmIonMessage.setMinimumSize(QtCore.QSize(686, 186))
        fmIonMessage.setMaximumSize(QtCore.QSize(686, 186))
        self.centralwidget = QtGui.QWidget(fmIonMessage)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tbSave = QtGui.QToolButton(self.centralwidget)
        self.tbSave.setGeometry(QtCore.QRect(120, 610, 361, 22))
        self.tbSave.setObjectName(_fromUtf8("tbSave"))
        self.lblMessage = QtGui.QLabel(self.centralwidget)
        self.lblMessage.setGeometry(QtCore.QRect(10, 10, 631, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblMessage.setFont(font)
        self.lblMessage.setObjectName(_fromUtf8("lblMessage"))
        self.lblMessage_1 = QtGui.QLabel(self.centralwidget)
        self.lblMessage_1.setGeometry(QtCore.QRect(10, 40, 631, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblMessage_1.setFont(font)
        self.lblMessage_1.setText(_fromUtf8(""))
        self.lblMessage_1.setObjectName(_fromUtf8("lblMessage_1"))
        self.btnOK = QtGui.QPushButton(self.centralwidget)
        self.btnOK.setGeometry(QtCore.QRect(230, 120, 75, 23))
        self.btnOK.setObjectName(_fromUtf8("btnOK"))
        self.btnCancel = QtGui.QPushButton(self.centralwidget)
        self.btnCancel.setGeometry(QtCore.QRect(320, 120, 75, 23))
        self.btnCancel.setObjectName(_fromUtf8("btnCancel"))
        self.lblMessage_2 = QtGui.QLabel(self.centralwidget)
        self.lblMessage_2.setGeometry(QtCore.QRect(10, 80, 631, 20))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.lblMessage_2.setFont(font)
        self.lblMessage_2.setText(_fromUtf8(""))
        self.lblMessage_2.setObjectName(_fromUtf8("lblMessage_2"))
        fmIonMessage.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(fmIonMessage)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 686, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu = QtGui.QMenu(self.menubar)
        self.menu.setObjectName(_fromUtf8("menu"))
        fmIonMessage.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(fmIonMessage)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        fmIonMessage.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(fmIonMessage)
        QtCore.QMetaObject.connectSlotsByName(fmIonMessage)

    def retranslateUi(self, fmIonMessage):
        fmIonMessage.setWindowTitle(_translate("fmIonMessage", "Значение буфера раствора", None))
        self.tbSave.setText(_translate("fmIonMessage", "Сохранить в энергонезависимой памяти", None))
        self.lblMessage.setText(_translate("fmIonMessage", "Другое число", None))
        self.btnOK.setText(_translate("fmIonMessage", "ОК", None))
        self.btnCancel.setText(_translate("fmIonMessage", "Отмена", None))
        self.menu.setTitle(_translate("fmIonMessage", "?", None))

