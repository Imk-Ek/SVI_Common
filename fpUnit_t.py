# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\ormet\source\svi_vs_v.0.4\forms\fpUnit.ui'
#
# Created: Wed Jun  4 16:50:59 2014
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
        fpUnit.resize(300, 177)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(fpUnit.sizePolicy().hasHeightForWidth())
        fpUnit.setSizePolicy(sizePolicy)
        fpUnit.setDockOptions(QtGui.QMainWindow.AllowTabbedDocks|QtGui.QMainWindow.AnimatedDocks)
        self.centralwidget = QtGui.QWidget(fpUnit)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.lcdVolt = QtGui.QLCDNumber(self.centralwidget)
        self.lcdVolt.setGeometry(QtCore.QRect(9, 9, 64, 23))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdVolt.sizePolicy().hasHeightForWidth())
        self.lcdVolt.setSizePolicy(sizePolicy)
        self.lcdVolt.setObjectName(_fromUtf8("lcdVolt"))
        self.llData_2 = QtGui.QLabel(self.centralwidget)
        self.llData_2.setGeometry(QtCore.QRect(10, 40, 281, 32))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.llData_2.sizePolicy().hasHeightForWidth())
        self.llData_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(20)
        self.llData_2.setFont(font)
        self.llData_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.llData_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.llData_2.setScaledContents(True)
        self.llData_2.setObjectName(_fromUtf8("llData_2"))
        self.llData_3 = QtGui.QLabel(self.centralwidget)
        self.llData_3.setGeometry(QtCore.QRect(10, 80, 281, 32))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.llData_3.sizePolicy().hasHeightForWidth())
        self.llData_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(20)
        self.llData_3.setFont(font)
        self.llData_3.setFrameShape(QtGui.QFrame.NoFrame)
        self.llData_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.llData_3.setScaledContents(True)
        self.llData_3.setObjectName(_fromUtf8("llData_3"))
        fpUnit.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(fpUnit)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 300, 21))
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
        self.llData_2.setText(_translate("fpUnit", "В", None))
        self.llData_3.setText(_translate("fpUnit", "В", None))
        self.muAbout.setTitle(_translate("fpUnit", "?", None))

