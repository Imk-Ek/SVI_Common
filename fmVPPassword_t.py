# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\ormet\source\svi (4)\svi\forms\fmVPPassword.ui'
#
# Created: Mon Sep 17 13:56:00 2018
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

class Ui_fmVPPassword(object):
    def setupUi(self, fmVPPassword):
        fmVPPassword.setObjectName(_fromUtf8("fmVPPassword"))
        fmVPPassword.resize(384, 195)
        fmVPPassword.setMinimumSize(QtCore.QSize(384, 195))
        fmVPPassword.setMaximumSize(QtCore.QSize(384, 195))
        self.centralwidget = QtGui.QWidget(fmVPPassword)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.lePassword = QtGui.QLineEdit(self.centralwidget)
        self.lePassword.setGeometry(QtCore.QRect(92, 25, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lePassword.setFont(font)
        self.lePassword.setObjectName(_fromUtf8("lePassword"))
        self.tbEnterPassword = QtGui.QToolButton(self.centralwidget)
        self.tbEnterPassword.setGeometry(QtCore.QRect(110, 100, 151, 51))
        self.tbEnterPassword.setObjectName(_fromUtf8("tbEnterPassword"))
        fmVPPassword.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(fmVPPassword)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        fmVPPassword.setStatusBar(self.statusbar)
        self.actTIns = QtGui.QAction(fmVPPassword)
        self.actTIns.setObjectName(_fromUtf8("actTIns"))
        self.actTDel = QtGui.QAction(fmVPPassword)
        self.actTDel.setObjectName(_fromUtf8("actTDel"))
        self.actPrIns = QtGui.QAction(fmVPPassword)
        self.actPrIns.setObjectName(_fromUtf8("actPrIns"))
        self.actPrDel = QtGui.QAction(fmVPPassword)
        self.actPrDel.setObjectName(_fromUtf8("actPrDel"))
        self.actPrRen = QtGui.QAction(fmVPPassword)
        self.actPrRen.setObjectName(_fromUtf8("actPrRen"))

        self.retranslateUi(fmVPPassword)
        QtCore.QMetaObject.connectSlotsByName(fmVPPassword)

    def retranslateUi(self, fmVPPassword):
        fmVPPassword.setWindowTitle(_translate("fmVPPassword", "Ввод пароля", None))
        self.tbEnterPassword.setText(_translate("fmVPPassword", "Ввод", None))
        self.actTIns.setText(_translate("fmVPPassword", "Вставить строку", None))
        self.actTDel.setText(_translate("fmVPPassword", "Удалить строку", None))
        self.actPrIns.setText(_translate("fmVPPassword", "Новый профиль", None))
        self.actPrDel.setText(_translate("fmVPPassword", "Удалить профиль", None))
        self.actPrRen.setText(_translate("fmVPPassword", "Переименовать профиль", None))

