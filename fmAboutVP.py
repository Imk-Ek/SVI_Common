# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\ormet\source\svi_vs_v.0.4\forms\fmAboutVP.ui'
#
# Created: Tue Jun  9 13:41:18 2015
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

class Ui_fmAboutVP(object):
    def setupUi(self, fmAboutVP):
        fmAboutVP.setObjectName(_fromUtf8("fmAboutVP"))
        fmAboutVP.resize(306, 268)
        self.centralwidget = QtGui.QWidget(fmAboutVP)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.lwAbout = QtGui.QListWidget(self.centralwidget)
        self.lwAbout.setGeometry(QtCore.QRect(10, 10, 281, 231))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lwAbout.sizePolicy().hasHeightForWidth())
        self.lwAbout.setSizePolicy(sizePolicy)
        self.lwAbout.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.lwAbout.setObjectName(_fromUtf8("lwAbout"))
        fmAboutVP.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(fmAboutVP)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        fmAboutVP.setStatusBar(self.statusbar)
        self.actTIns = QtGui.QAction(fmAboutVP)
        self.actTIns.setObjectName(_fromUtf8("actTIns"))
        self.actTDel = QtGui.QAction(fmAboutVP)
        self.actTDel.setObjectName(_fromUtf8("actTDel"))
        self.actPrIns = QtGui.QAction(fmAboutVP)
        self.actPrIns.setObjectName(_fromUtf8("actPrIns"))
        self.actPrDel = QtGui.QAction(fmAboutVP)
        self.actPrDel.setObjectName(_fromUtf8("actPrDel"))
        self.actPrRen = QtGui.QAction(fmAboutVP)
        self.actPrRen.setObjectName(_fromUtf8("actPrRen"))

        self.retranslateUi(fmAboutVP)
        QtCore.QMetaObject.connectSlotsByName(fmAboutVP)

    def retranslateUi(self, fmAboutVP):
        fmAboutVP.setWindowTitle(_translate("fmAboutVP", "О программе", None))
        self.actTIns.setText(_translate("fmAboutVP", "Вставить строку", None))
        self.actTDel.setText(_translate("fmAboutVP", "Удалить строку", None))
        self.actPrIns.setText(_translate("fmAboutVP", "Новый профиль", None))
        self.actPrDel.setText(_translate("fmAboutVP", "Удалить профиль", None))
        self.actPrRen.setText(_translate("fmAboutVP", "Переименовать профиль", None))

