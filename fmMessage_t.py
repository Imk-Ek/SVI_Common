# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\ormet\source\svi (4)\svi\forms\fmMessage.ui'
#
# Created: Thu Sep 13 10:41:08 2018
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

class Ui_fmMessage(object):
    def setupUi(self, fmMessage):
        fmMessage.setObjectName(_fromUtf8("fmMessage"))
        fmMessage.resize(492, 247)
        fmMessage.setMinimumSize(QtCore.QSize(492, 247))
        fmMessage.setMaximumSize(QtCore.QSize(492, 247))
        self.centralwidget = QtGui.QWidget(fmMessage)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tbMessage = QtGui.QTextBrowser(self.centralwidget)
        self.tbMessage.setGeometry(QtCore.QRect(20, 10, 451, 201))
        self.tbMessage.setObjectName(_fromUtf8("tbMessage"))
        fmMessage.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(fmMessage)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        fmMessage.setStatusBar(self.statusbar)
        self.actTIns = QtGui.QAction(fmMessage)
        self.actTIns.setObjectName(_fromUtf8("actTIns"))
        self.actTDel = QtGui.QAction(fmMessage)
        self.actTDel.setObjectName(_fromUtf8("actTDel"))
        self.actPrIns = QtGui.QAction(fmMessage)
        self.actPrIns.setObjectName(_fromUtf8("actPrIns"))
        self.actPrDel = QtGui.QAction(fmMessage)
        self.actPrDel.setObjectName(_fromUtf8("actPrDel"))
        self.actPrRen = QtGui.QAction(fmMessage)
        self.actPrRen.setObjectName(_fromUtf8("actPrRen"))

        self.retranslateUi(fmMessage)
        QtCore.QMetaObject.connectSlotsByName(fmMessage)

    def retranslateUi(self, fmMessage):
        fmMessage.setWindowTitle(_translate("fmMessage", "Сообщение", None))
        self.actTIns.setText(_translate("fmMessage", "Вставить строку", None))
        self.actTDel.setText(_translate("fmMessage", "Удалить строку", None))
        self.actPrIns.setText(_translate("fmMessage", "Новый профиль", None))
        self.actPrDel.setText(_translate("fmMessage", "Удалить профиль", None))
        self.actPrRen.setText(_translate("fmMessage", "Переименовать профиль", None))

