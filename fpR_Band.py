# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\ormet\source\svi_vs_v.0.3\forms\fpR_Band.ui'
#
# Created: Thu Apr 10 14:02:20 2014
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

class Ui_fpR_Band(object):
    def setupUi(self, fpR_Band):
        fpR_Band.setObjectName(_fromUtf8("fpR_Band"))
        fpR_Band.resize(312, 111)
        self.centralwidget = QtGui.QWidget(fpR_Band)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lcdPressure = QtGui.QLCDNumber(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdPressure.sizePolicy().hasHeightForWidth())
        self.lcdPressure.setSizePolicy(sizePolicy)
        self.lcdPressure.setObjectName(_fromUtf8("lcdPressure"))
        self.horizontalLayout.addWidget(self.lcdPressure)
        self.llData = QtGui.QLabel(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.llData.sizePolicy().hasHeightForWidth())
        self.llData.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(20)
        self.llData.setFont(font)
        self.llData.setFrameShape(QtGui.QFrame.NoFrame)
        self.llData.setFrameShadow(QtGui.QFrame.Sunken)
        self.llData.setText(_fromUtf8(""))
        self.llData.setScaledContents(True)
        self.llData.setObjectName(_fromUtf8("llData"))
        self.horizontalLayout.addWidget(self.llData)
        fpR_Band.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(fpR_Band)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 312, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.muAbout = QtGui.QMenu(self.menubar)
        self.muAbout.setObjectName(_fromUtf8("muAbout"))
        fpR_Band.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(fpR_Band)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        fpR_Band.setStatusBar(self.statusbar)
        self.menubar.addAction(self.muAbout.menuAction())

        self.retranslateUi(fpR_Band)
        QtCore.QMetaObject.connectSlotsByName(fpR_Band)

    def retranslateUi(self, fpR_Band):
        fpR_Band.setWindowTitle(_translate("fpR_Band", "Сопротивление. Диапазон", None))
        self.muAbout.setTitle(_translate("fpR_Band", "?", None))

