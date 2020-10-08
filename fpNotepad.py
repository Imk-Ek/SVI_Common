# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\ormet\source\svi_vs_v.0.4\forms\fpNotepad.ui'
#
# Created: Thu Aug 28 15:16:09 2014
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

class Ui_fpUnit(object):
    def setupUi(self, fpUnit):
        fpUnit.setObjectName(_fromUtf8("fpUnit"))
        fpUnit.resize(315, 297)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(fpUnit.sizePolicy().hasHeightForWidth())
        fpUnit.setSizePolicy(sizePolicy)
        fpUnit.setDockOptions(QtGui.QMainWindow.AllowTabbedDocks|QtGui.QMainWindow.AnimatedDocks)
        self.centralwidget = QtGui.QWidget(fpUnit)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tableView = QtGui.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(20, 10, 256, 192))
        self.tableView.setObjectName(_fromUtf8("tableView"))
        fpUnit.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(fpUnit)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 315, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.muAbout = QtGui.QMenu(self.menubar)
        self.muAbout.setObjectName(_fromUtf8("muAbout"))
        fpUnit.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(fpUnit)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        fpUnit.setStatusBar(self.statusbar)
        self.menubar.addAction(self.muAbout.menuAction())

        self.retranslateUi(fpUnit)
        QtCore.QMetaObject.connectSlotsByName(fpUnit)

    def retranslateUi(self, fpUnit):
        fpUnit.setWindowTitle(_translate("fpUnit", "Напряжение", None))
        self.muAbout.setTitle(_translate("fpUnit", "?", None))

