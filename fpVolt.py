# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\ormet\source\svi_vs_v.0.4\forms\fpVolt.ui'
#
# Created: Fri Feb 20 14:40:06 2015
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

class Ui_fpVolt(object):
    def setupUi(self, fpVolt):
        fpVolt.setObjectName(_fromUtf8("fpVolt"))
        fpVolt.resize(247, 170)
        self.centralwidget = QtGui.QWidget(fpVolt)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lcdVolt = QtGui.QLCDNumber(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdVolt.sizePolicy().hasHeightForWidth())
        self.lcdVolt.setSizePolicy(sizePolicy)
        self.lcdVolt.setObjectName(_fromUtf8("lcdVolt"))
        self.gridLayout.addWidget(self.lcdVolt, 0, 0, 1, 1)
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
        self.llData.setScaledContents(True)
        self.llData.setObjectName(_fromUtf8("llData"))
        self.gridLayout.addWidget(self.llData, 0, 1, 1, 1)
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.leID = QtGui.QLineEdit(self.groupBox_2)
        self.leID.setGeometry(QtCore.QRect(40, 20, 81, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leID.sizePolicy().hasHeightForWidth())
        self.leID.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(12)
        self.leID.setFont(font)
        self.leID.setFrame(True)
        self.leID.setObjectName(_fromUtf8("leID"))
        self.tbSaveToNotepad_ = QtGui.QToolButton(self.groupBox_2)
        self.tbSaveToNotepad_.setGeometry(QtCore.QRect(140, 20, 81, 31))
        self.tbSaveToNotepad_.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tbSaveToNotepad_.setObjectName(_fromUtf8("tbSaveToNotepad_"))
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(10, 20, 31, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.groupBox_2, 1, 0, 1, 2)
        fpVolt.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(fpVolt)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 247, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.muAbout = QtGui.QMenu(self.menubar)
        self.muAbout.setObjectName(_fromUtf8("muAbout"))
        fpVolt.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(fpVolt)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        fpVolt.setStatusBar(self.statusbar)
        self.menubar.addAction(self.muAbout.menuAction())

        self.retranslateUi(fpVolt)
        QtCore.QMetaObject.connectSlotsByName(fpVolt)

    def retranslateUi(self, fpVolt):
        fpVolt.setWindowTitle(_translate("fpVolt", "Напряжение", None))
        self.llData.setText(_translate("fpVolt", "В", None))
        self.groupBox_2.setTitle(_translate("fpVolt", "Запись в блокнот", None))
        self.leID.setText(_translate("fpVolt", "12", None))
        self.tbSaveToNotepad_.setText(_translate("fpVolt", "Записать", None))
        self.label_4.setText(_translate("fpVolt", "ID", None))
        self.muAbout.setTitle(_translate("fpVolt", "?", None))

