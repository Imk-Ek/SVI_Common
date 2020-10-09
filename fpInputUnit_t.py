# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\ormet\source\svi_vs_v.0.4\forms\fpInputUnit.ui'
#
# Created: Fri Aug 29 15:43:01 2014
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

class Ui_fpInputUnit(object):
    def setupUi(self, fpInputUnit):
        fpInputUnit.setObjectName(_fromUtf8("fpInputUnit"))
        fpInputUnit.resize(294, 187)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(fpInputUnit.sizePolicy().hasHeightForWidth())
        fpInputUnit.setSizePolicy(sizePolicy)
        fpInputUnit.setMinimumSize(QtCore.QSize(294, 187))
        fpInputUnit.setSizeIncrement(QtCore.QSize(1, 1))
        fpInputUnit.setDockOptions(QtGui.QMainWindow.AllowTabbedDocks|QtGui.QMainWindow.AnimatedDocks)
        self.centralwidget = QtGui.QWidget(fpInputUnit)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tbEnter = QtGui.QPushButton(self.centralwidget)
        self.tbEnter.setGeometry(QtCore.QRect(110, 110, 75, 23))
        self.tbEnter.setObjectName(_fromUtf8("tbEnter"))
        self.leVal1 = QtGui.QLineEdit(self.centralwidget)
        self.leVal1.setGeometry(QtCore.QRect(90, 10, 113, 20))
        self.leVal1.setObjectName(_fromUtf8("leVal1"))
        self.leVal2 = QtGui.QLineEdit(self.centralwidget)
        self.leVal2.setGeometry(QtCore.QRect(90, 40, 113, 20))
        self.leVal2.setObjectName(_fromUtf8("leVal2"))
        self.leVal3 = QtGui.QLineEdit(self.centralwidget)
        self.leVal3.setGeometry(QtCore.QRect(90, 70, 113, 20))
        self.leVal3.setObjectName(_fromUtf8("leVal3"))
        self.Dtk = QtGui.QLabel(self.centralwidget)
        self.Dtk.setGeometry(QtCore.QRect(10, 10, 61, 16))
        self.Dtk.setObjectName(_fromUtf8("Dtk"))
        self.Dtk_2 = QtGui.QLabel(self.centralwidget)
        self.Dtk_2.setGeometry(QtCore.QRect(10, 40, 61, 16))
        self.Dtk_2.setObjectName(_fromUtf8("Dtk_2"))
        self.Dtk_3 = QtGui.QLabel(self.centralwidget)
        self.Dtk_3.setGeometry(QtCore.QRect(10, 70, 61, 16))
        self.Dtk_3.setObjectName(_fromUtf8("Dtk_3"))
        fpInputUnit.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(fpInputUnit)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 294, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.muAbout = QtGui.QMenu(self.menubar)
        self.muAbout.setObjectName(_fromUtf8("muAbout"))
        fpInputUnit.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(fpInputUnit)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        fpInputUnit.setStatusBar(self.statusbar)
        self.menubar.addAction(self.muAbout.menuAction())

        self.retranslateUi(fpInputUnit)
        QtCore.QMetaObject.connectSlotsByName(fpInputUnit)

    def retranslateUi(self, fpInputUnit):
        fpInputUnit.setWindowTitle(_translate("fpInputUnit", "Напряжение", None))
        self.tbEnter.setText(_translate("fpInputUnit", "Ввод", None))
        self.Dtk.setText(_translate("fpInputUnit", "Величина 1", None))
        self.Dtk_2.setText(_translate("fpInputUnit", "Величина 2", None))
        self.Dtk_3.setText(_translate("fpInputUnit", "Величина 3", None))
        self.muAbout.setTitle(_translate("fpInputUnit", "?", None))

