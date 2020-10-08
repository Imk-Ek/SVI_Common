# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\ormet\source\svi_vs_v.0.4\forms\fpPressure.ui'
#
# Created: Fri Feb 20 14:40:29 2015
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

class Ui_fpPressure(object):
    def setupUi(self, fpPressure):
        fpPressure.setObjectName(_fromUtf8("fpPressure"))
        fpPressure.resize(279, 183)
        self.centralwidget = QtGui.QWidget(fpPressure)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.lcdPressure = QtGui.QLCDNumber(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdPressure.sizePolicy().hasHeightForWidth())
        self.lcdPressure.setSizePolicy(sizePolicy)
        self.lcdPressure.setObjectName(_fromUtf8("lcdPressure"))
        self.gridLayout.addWidget(self.lcdPressure, 0, 0, 1, 1)
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
        fpPressure.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(fpPressure)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 279, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.muAbout = QtGui.QMenu(self.menubar)
        self.muAbout.setObjectName(_fromUtf8("muAbout"))
        fpPressure.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(fpPressure)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        fpPressure.setStatusBar(self.statusbar)
        self.menubar.addAction(self.muAbout.menuAction())

        self.retranslateUi(fpPressure)
        QtCore.QMetaObject.connectSlotsByName(fpPressure)

    def retranslateUi(self, fpPressure):
        fpPressure.setWindowTitle(_translate("fpPressure", "Давление", None))
        self.llData.setText(_translate("fpPressure", "кПа", None))
        self.groupBox_2.setTitle(_translate("fpPressure", "Запись в блокнот", None))
        self.leID.setText(_translate("fpPressure", "12", None))
        self.tbSaveToNotepad_.setText(_translate("fpPressure", "Записать", None))
        self.label_4.setText(_translate("fpPressure", "ID", None))
        self.muAbout.setTitle(_translate("fpPressure", "?", None))

