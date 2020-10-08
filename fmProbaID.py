# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\ormet\source\svi_vs_v.0.4\forms\fmProbaID.ui'
#
# Created: Mon Jun  8 17:40:46 2015
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

class Ui_fmProbaID(object):
    def setupUi(self, fmProbaID):
        fmProbaID.setObjectName(_fromUtf8("fmProbaID"))
        fmProbaID.resize(203, 146)
        self.centralwidget = QtGui.QWidget(fmProbaID)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.lePassword = QtGui.QLineEdit(self.centralwidget)
        self.lePassword.setGeometry(QtCore.QRect(50, 10, 81, 22))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lePassword.setFont(font)
        self.lePassword.setObjectName(_fromUtf8("lePassword"))
        self.tbEnterPassword = QtGui.QToolButton(self.centralwidget)
        self.tbEnterPassword.setGeometry(QtCore.QRect(20, 60, 151, 22))
        self.tbEnterPassword.setObjectName(_fromUtf8("tbEnterPassword"))
        fmProbaID.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(fmProbaID)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        fmProbaID.setStatusBar(self.statusbar)
        self.actTIns = QtGui.QAction(fmProbaID)
        self.actTIns.setObjectName(_fromUtf8("actTIns"))
        self.actTDel = QtGui.QAction(fmProbaID)
        self.actTDel.setObjectName(_fromUtf8("actTDel"))
        self.actPrIns = QtGui.QAction(fmProbaID)
        self.actPrIns.setObjectName(_fromUtf8("actPrIns"))
        self.actPrDel = QtGui.QAction(fmProbaID)
        self.actPrDel.setObjectName(_fromUtf8("actPrDel"))
        self.actPrRen = QtGui.QAction(fmProbaID)
        self.actPrRen.setObjectName(_fromUtf8("actPrRen"))

        self.retranslateUi(fmProbaID)
        QtCore.QMetaObject.connectSlotsByName(fmProbaID)

    def retranslateUi(self, fmProbaID):
        fmProbaID.setWindowTitle(_translate("fmProbaID", "Ввод пробы", None))
        self.tbEnterPassword.setText(_translate("fmProbaID", "Ввод", None))
        self.actTIns.setText(_translate("fmProbaID", "Вставить строку", None))
        self.actTDel.setText(_translate("fmProbaID", "Удалить строку", None))
        self.actPrIns.setText(_translate("fmProbaID", "Новый профиль", None))
        self.actPrDel.setText(_translate("fmProbaID", "Удалить профиль", None))
        self.actPrRen.setText(_translate("fmProbaID", "Переименовать профиль", None))

