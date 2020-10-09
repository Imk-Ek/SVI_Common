# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\ormet\source\svi (4)\svi\forms\fmMBCons.ui'
#
# Created: Thu Sep 13 10:31:25 2018
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

class Ui_fmMBCons(object):
    def setupUi(self, fmMBCons):
        fmMBCons.setObjectName(_fromUtf8("fmMBCons"))
        fmMBCons.resize(594, 214)
        self.centralwidget = QtGui.QWidget(fmMBCons)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.cbRegs = QtGui.QComboBox(self.centralwidget)
        self.cbRegs.setGeometry(QtCore.QRect(20, 20, 211, 41))
        self.cbRegs.setObjectName(_fromUtf8("cbRegs"))
        self.lcdMeas = QtGui.QLCDNumber(self.centralwidget)
        self.lcdMeas.setGeometry(QtCore.QRect(320, 80, 161, 41))
        self.lcdMeas.setObjectName(_fromUtf8("lcdMeas"))
        self.tbRegsAdd = QtGui.QToolButton(self.centralwidget)
        self.tbRegsAdd.setGeometry(QtCore.QRect(250, 20, 41, 41))
        self.tbRegsAdd.setObjectName(_fromUtf8("tbRegsAdd"))
        self.tbRegsWr = QtGui.QToolButton(self.centralwidget)
        self.tbRegsWr.setGeometry(QtCore.QRect(250, 80, 41, 41))
        self.tbRegsWr.setObjectName(_fromUtf8("tbRegsWr"))
        self.tbRegsRd = QtGui.QToolButton(self.centralwidget)
        self.tbRegsRd.setGeometry(QtCore.QRect(200, 80, 41, 41))
        self.tbRegsRd.setObjectName(_fromUtf8("tbRegsRd"))
        self.leRegs = QtGui.QLineEdit(self.centralwidget)
        self.leRegs.setGeometry(QtCore.QRect(20, 80, 161, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.leRegs.setFont(font)
        self.leRegs.setText(_fromUtf8(""))
        self.leRegs.setObjectName(_fromUtf8("leRegs"))
        self.cbMeas = QtGui.QComboBox(self.centralwidget)
        self.cbMeas.setGeometry(QtCore.QRect(320, 20, 201, 41))
        self.cbMeas.setObjectName(_fromUtf8("cbMeas"))
        self.tbFloatAdd = QtGui.QToolButton(self.centralwidget)
        self.tbFloatAdd.setGeometry(QtCore.QRect(530, 20, 41, 41))
        self.tbFloatAdd.setObjectName(_fromUtf8("tbFloatAdd"))
        self.tbMeasRd = QtGui.QToolButton(self.centralwidget)
        self.tbMeasRd.setGeometry(QtCore.QRect(530, 80, 41, 31))
        self.tbMeasRd.setObjectName(_fromUtf8("tbMeasRd"))
        fmMBCons.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(fmMBCons)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 594, 38))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu = QtGui.QMenu(self.menubar)
        self.menu.setObjectName(_fromUtf8("menu"))
        fmMBCons.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(fmMBCons)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        fmMBCons.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(fmMBCons)
        QtCore.QMetaObject.connectSlotsByName(fmMBCons)

    def retranslateUi(self, fmMBCons):
        fmMBCons.setWindowTitle(_translate("fmMBCons", "Консоль драйвера MODBUS", None))
        self.tbRegsAdd.setText(_translate("fmMBCons", "+", None))
        self.tbRegsWr.setText(_translate("fmMBCons", "Wr", None))
        self.tbRegsRd.setText(_translate("fmMBCons", "Rd", None))
        self.tbFloatAdd.setText(_translate("fmMBCons", "+", None))
        self.tbMeasRd.setText(_translate("fmMBCons", "Rd", None))
        self.menu.setTitle(_translate("fmMBCons", "?", None))

