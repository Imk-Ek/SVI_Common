# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\ormet\source\svi (4)\svi\forms\fmAD779x.ui'
#
# Created: Thu Sep 13 10:02:01 2018
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

class Ui_fmAD779x(object):
    def setupUi(self, fmAD779x):
        fmAD779x.setObjectName(_fromUtf8("fmAD779x"))
        fmAD779x.resize(821, 663)
        self.centralwidget = QtGui.QWidget(fmAD779x)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.twRegs = QtGui.QTabWidget(self.centralwidget)
        self.twRegs.setGeometry(QtCore.QRect(10, 190, 781, 411))
        self.twRegs.setElideMode(QtCore.Qt.ElideNone)
        self.twRegs.setObjectName(_fromUtf8("twRegs"))
        self.wtData = QtGui.QWidget()
        self.wtData.setObjectName(_fromUtf8("wtData"))
        self.label = QtGui.QLabel(self.wtData)
        self.label.setGeometry(QtCore.QRect(15, 30, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.llData = QtGui.QLabel(self.wtData)
        self.llData.setGeometry(QtCore.QRect(200, 20, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.llData.setFont(font)
        self.llData.setFrameShape(QtGui.QFrame.Panel)
        self.llData.setFrameShadow(QtGui.QFrame.Sunken)
        self.llData.setText(_fromUtf8(""))
        self.llData.setObjectName(_fromUtf8("llData"))
        self.tbDataRd = QtGui.QToolButton(self.wtData)
        self.tbDataRd.setGeometry(QtCore.QRect(340, 15, 41, 41))
        self.tbDataRd.setObjectName(_fromUtf8("tbDataRd"))
        self.label_2 = QtGui.QLabel(self.wtData)
        self.label_2.setGeometry(QtCore.QRect(460, 30, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.tbStatusRd = QtGui.QToolButton(self.wtData)
        self.tbStatusRd.setGeometry(QtCore.QRect(720, 20, 41, 41))
        self.tbStatusRd.setObjectName(_fromUtf8("tbStatusRd"))
        self.llStatus = QtGui.QLabel(self.wtData)
        self.llStatus.setGeometry(QtCore.QRect(610, 20, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.llStatus.setFont(font)
        self.llStatus.setFrameShape(QtGui.QFrame.Panel)
        self.llStatus.setFrameShadow(QtGui.QFrame.Sunken)
        self.llStatus.setText(_fromUtf8(""))
        self.llStatus.setObjectName(_fromUtf8("llStatus"))
        self.leOffset = QtGui.QLineEdit(self.wtData)
        self.leOffset.setGeometry(QtCore.QRect(200, 70, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.leOffset.setFont(font)
        self.leOffset.setObjectName(_fromUtf8("leOffset"))
        self.tbOffsetWr = QtGui.QToolButton(self.wtData)
        self.tbOffsetWr.setGeometry(QtCore.QRect(400, 70, 41, 41))
        self.tbOffsetWr.setObjectName(_fromUtf8("tbOffsetWr"))
        self.label_11 = QtGui.QLabel(self.wtData)
        self.label_11.setGeometry(QtCore.QRect(10, 70, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_11.setFont(font)
        self.label_11.setLineWidth(-5)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.tbScaleWr = QtGui.QToolButton(self.wtData)
        self.tbScaleWr.setGeometry(QtCore.QRect(400, 120, 41, 41))
        self.tbScaleWr.setObjectName(_fromUtf8("tbScaleWr"))
        self.leScale = QtGui.QLineEdit(self.wtData)
        self.leScale.setGeometry(QtCore.QRect(200, 120, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.leScale.setFont(font)
        self.leScale.setObjectName(_fromUtf8("leScale"))
        self.tbScaleRd = QtGui.QToolButton(self.wtData)
        self.tbScaleRd.setGeometry(QtCore.QRect(340, 120, 41, 41))
        self.tbScaleRd.setObjectName(_fromUtf8("tbScaleRd"))
        self.label_12 = QtGui.QLabel(self.wtData)
        self.label_12.setGeometry(QtCore.QRect(10, 130, 181, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_12.setFont(font)
        self.label_12.setLineWidth(-5)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.llID = QtGui.QLabel(self.wtData)
        self.llID.setGeometry(QtCore.QRect(610, 80, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.llID.setFont(font)
        self.llID.setFrameShape(QtGui.QFrame.Panel)
        self.llID.setFrameShadow(QtGui.QFrame.Sunken)
        self.llID.setText(_fromUtf8(""))
        self.llID.setObjectName(_fromUtf8("llID"))
        self.tbIDRd = QtGui.QToolButton(self.wtData)
        self.tbIDRd.setGeometry(QtCore.QRect(720, 80, 41, 41))
        self.tbIDRd.setObjectName(_fromUtf8("tbIDRd"))
        self.label_13 = QtGui.QLabel(self.wtData)
        self.label_13.setGeometry(QtCore.QRect(540, 82, 41, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_13.setFont(font)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.tbDataA = QtGui.QToolButton(self.wtData)
        self.tbDataA.setGeometry(QtCore.QRect(400, 17, 41, 41))
        self.tbDataA.setObjectName(_fromUtf8("tbDataA"))
        self.lcdDataConv = QtGui.QLCDNumber(self.wtData)
        self.lcdDataConv.setGeometry(QtCore.QRect(10, 180, 201, 41))
        self.lcdDataConv.setObjectName(_fromUtf8("lcdDataConv"))
        self.tbConv = QtGui.QToolButton(self.wtData)
        self.tbConv.setGeometry(QtCore.QRect(230, 180, 41, 41))
        self.tbConv.setObjectName(_fromUtf8("tbConv"))
        self.tbOffsetRd = QtGui.QToolButton(self.wtData)
        self.tbOffsetRd.setGeometry(QtCore.QRect(340, 70, 41, 41))
        self.tbOffsetRd.setObjectName(_fromUtf8("tbOffsetRd"))
        self.twRegs.addTab(self.wtData, _fromUtf8(""))
        self.wtMode = QtGui.QWidget()
        self.wtMode.setObjectName(_fromUtf8("wtMode"))
        self.label_3 = QtGui.QLabel(self.wtMode)
        self.label_3.setGeometry(QtCore.QRect(30, 20, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.tbModeRd = QtGui.QToolButton(self.wtMode)
        self.tbModeRd.setGeometry(QtCore.QRect(350, 30, 41, 41))
        self.tbModeRd.setObjectName(_fromUtf8("tbModeRd"))
        self.tbModeWr = QtGui.QToolButton(self.wtMode)
        self.tbModeWr.setGeometry(QtCore.QRect(410, 30, 41, 41))
        self.tbModeWr.setObjectName(_fromUtf8("tbModeWr"))
        self.leMode = QtGui.QLineEdit(self.wtMode)
        self.leMode.setGeometry(QtCore.QRect(250, 32, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.leMode.setFont(font)
        self.leMode.setObjectName(_fromUtf8("leMode"))
        self.cbMode = QtGui.QComboBox(self.wtMode)
        self.cbMode.setGeometry(QtCore.QRect(240, 80, 391, 41))
        self.cbMode.setObjectName(_fromUtf8("cbMode"))
        self.cbMode.addItem(_fromUtf8(""))
        self.cbMode.addItem(_fromUtf8(""))
        self.cbMode.addItem(_fromUtf8(""))
        self.cbMode.addItem(_fromUtf8(""))
        self.cbMode.addItem(_fromUtf8(""))
        self.cbMode.addItem(_fromUtf8(""))
        self.cbMode.addItem(_fromUtf8(""))
        self.cbMode.addItem(_fromUtf8(""))
        self.cbFadc = QtGui.QComboBox(self.wtMode)
        self.cbFadc.setGeometry(QtCore.QRect(240, 210, 391, 41))
        self.cbFadc.setObjectName(_fromUtf8("cbFadc"))
        self.cbFadc.addItem(_fromUtf8(""))
        self.cbFadc.addItem(_fromUtf8(""))
        self.cbFadc.addItem(_fromUtf8(""))
        self.cbFadc.addItem(_fromUtf8(""))
        self.cbFadc.addItem(_fromUtf8(""))
        self.cbFadc.addItem(_fromUtf8(""))
        self.cbFadc.addItem(_fromUtf8(""))
        self.cbFadc.addItem(_fromUtf8(""))
        self.cbFadc.addItem(_fromUtf8(""))
        self.cbFadc.addItem(_fromUtf8(""))
        self.cbFadc.addItem(_fromUtf8(""))
        self.cbFadc.addItem(_fromUtf8(""))
        self.cbFadc.addItem(_fromUtf8(""))
        self.cbFadc.addItem(_fromUtf8(""))
        self.cbFadc.addItem(_fromUtf8(""))
        self.cbFadc.addItem(_fromUtf8(""))
        self.label_4 = QtGui.QLabel(self.wtMode)
        self.label_4.setGeometry(QtCore.QRect(10, 220, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_14 = QtGui.QLabel(self.wtMode)
        self.label_14.setGeometry(QtCore.QRect(10, 150, 231, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_14.setFont(font)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.cbClock = QtGui.QComboBox(self.wtMode)
        self.cbClock.setGeometry(QtCore.QRect(240, 150, 391, 41))
        self.cbClock.setObjectName(_fromUtf8("cbClock"))
        self.cbClock.addItem(_fromUtf8(""))
        self.cbClock.addItem(_fromUtf8(""))
        self.cbClock.addItem(_fromUtf8(""))
        self.cbClock.addItem(_fromUtf8(""))
        self.twRegs.addTab(self.wtMode, _fromUtf8(""))
        self.wtConf = QtGui.QWidget()
        self.wtConf.setObjectName(_fromUtf8("wtConf"))
        self.leConf = QtGui.QLineEdit(self.wtConf)
        self.leConf.setGeometry(QtCore.QRect(225, 18, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.leConf.setFont(font)
        self.leConf.setObjectName(_fromUtf8("leConf"))
        self.tbConfRd = QtGui.QToolButton(self.wtConf)
        self.tbConfRd.setGeometry(QtCore.QRect(340, 12, 41, 41))
        self.tbConfRd.setObjectName(_fromUtf8("tbConfRd"))
        self.tbConfWr = QtGui.QToolButton(self.wtConf)
        self.tbConfWr.setGeometry(QtCore.QRect(393, 14, 41, 41))
        self.tbConfWr.setObjectName(_fromUtf8("tbConfWr"))
        self.label_5 = QtGui.QLabel(self.wtConf)
        self.label_5.setGeometry(QtCore.QRect(30, 15, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.cbBias = QtGui.QComboBox(self.wtConf)
        self.cbBias.setGeometry(QtCore.QRect(270, 170, 171, 41))
        self.cbBias.setObjectName(_fromUtf8("cbBias"))
        self.cbBias.addItem(_fromUtf8(""))
        self.cbBias.addItem(_fromUtf8(""))
        self.cbBias.addItem(_fromUtf8(""))
        self.cbBias.addItem(_fromUtf8(""))
        self.chBurnT = QtGui.QCheckBox(self.wtConf)
        self.chBurnT.setGeometry(QtCore.QRect(190, 260, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.chBurnT.setFont(font)
        self.chBurnT.setObjectName(_fromUtf8("chBurnT"))
        self.cbRef = QtGui.QComboBox(self.wtConf)
        self.cbRef.setGeometry(QtCore.QRect(260, 120, 181, 41))
        self.cbRef.setObjectName(_fromUtf8("cbRef"))
        self.cbRef.addItem(_fromUtf8(""))
        self.cbRef.addItem(_fromUtf8(""))
        self.label_7 = QtGui.QLabel(self.wtConf)
        self.label_7.setGeometry(QtCore.QRect(20, 130, 231, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.cbChan = QtGui.QComboBox(self.wtConf)
        self.cbChan.setGeometry(QtCore.QRect(120, 70, 261, 41))
        self.cbChan.setObjectName(_fromUtf8("cbChan"))
        self.cbChan.addItem(_fromUtf8(""))
        self.cbChan.addItem(_fromUtf8(""))
        self.cbChan.addItem(_fromUtf8(""))
        self.cbChan.addItem(_fromUtf8(""))
        self.cbChan.addItem(_fromUtf8(""))
        self.cbChan.addItem(_fromUtf8(""))
        self.cbChan.addItem(_fromUtf8(""))
        self.cbChan.addItem(_fromUtf8(""))
        self.label_8 = QtGui.QLabel(self.wtConf)
        self.label_8.setGeometry(QtCore.QRect(20, 80, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.label_9 = QtGui.QLabel(self.wtConf)
        self.label_9.setGeometry(QtCore.QRect(20, 180, 251, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.chABias = QtGui.QCheckBox(self.wtConf)
        self.chABias.setGeometry(QtCore.QRect(190, 310, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.chABias.setFont(font)
        self.chABias.setObjectName(_fromUtf8("chABias"))
        self.chAmp = QtGui.QCheckBox(self.wtConf)
        self.chAmp.setEnabled(True)
        self.chAmp.setGeometry(QtCore.QRect(520, 250, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(8)
        self.chAmp.setFont(font)
        self.chAmp.setObjectName(_fromUtf8("chAmp"))
        self.label_10 = QtGui.QLabel(self.wtConf)
        self.label_10.setGeometry(QtCore.QRect(480, 170, 71, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.cbCode = QtGui.QComboBox(self.wtConf)
        self.cbCode.setGeometry(QtCore.QRect(540, 161, 211, 41))
        self.cbCode.setObjectName(_fromUtf8("cbCode"))
        self.cbCode.addItem(_fromUtf8(""))
        self.cbCode.addItem(_fromUtf8(""))
        self.label_6 = QtGui.QLabel(self.wtConf)
        self.label_6.setGeometry(QtCore.QRect(470, 120, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.cbAmp = QtGui.QComboBox(self.wtConf)
        self.cbAmp.setGeometry(QtCore.QRect(590, 110, 161, 41))
        self.cbAmp.setObjectName(_fromUtf8("cbAmp"))
        self.cbAmp.addItem(_fromUtf8(""))
        self.cbAmp.addItem(_fromUtf8(""))
        self.cbAmp.addItem(_fromUtf8(""))
        self.cbAmp.addItem(_fromUtf8(""))
        self.cbAmp.addItem(_fromUtf8(""))
        self.cbAmp.addItem(_fromUtf8(""))
        self.cbAmp.addItem(_fromUtf8(""))
        self.cbAmp.addItem(_fromUtf8(""))
        self.twRegs.addTab(self.wtConf, _fromUtf8(""))
        self.wtJ = QtGui.QWidget()
        self.wtJ.setObjectName(_fromUtf8("wtJ"))
        self.label_17 = QtGui.QLabel(self.wtJ)
        self.label_17.setGeometry(QtCore.QRect(20, 20, 171, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_17.setFont(font)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.tbIOWr = QtGui.QToolButton(self.wtJ)
        self.tbIOWr.setGeometry(QtCore.QRect(360, 20, 41, 41))
        self.tbIOWr.setObjectName(_fromUtf8("tbIOWr"))
        self.leIO = QtGui.QLineEdit(self.wtJ)
        self.leIO.setGeometry(QtCore.QRect(200, 30, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.leIO.setFont(font)
        self.leIO.setObjectName(_fromUtf8("leIO"))
        self.tbIORd = QtGui.QToolButton(self.wtJ)
        self.tbIORd.setGeometry(QtCore.QRect(300, 20, 41, 41))
        self.tbIORd.setObjectName(_fromUtf8("tbIORd"))
        self.cbJDir = QtGui.QComboBox(self.wtJ)
        self.cbJDir.setGeometry(QtCore.QRect(330, 170, 401, 41))
        self.cbJDir.setObjectName(_fromUtf8("cbJDir"))
        self.cbJDir.addItem(_fromUtf8(""))
        self.cbJDir.addItem(_fromUtf8(""))
        self.cbJDir.addItem(_fromUtf8(""))
        self.cbJDir.addItem(_fromUtf8(""))
        self.label_18 = QtGui.QLabel(self.wtJ)
        self.label_18.setGeometry(QtCore.QRect(20, 160, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_18.setFont(font)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.label_19 = QtGui.QLabel(self.wtJ)
        self.label_19.setGeometry(QtCore.QRect(20, 90, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_19.setFont(font)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.cbJVal = QtGui.QComboBox(self.wtJ)
        self.cbJVal.setGeometry(QtCore.QRect(200, 90, 201, 41))
        self.cbJVal.setObjectName(_fromUtf8("cbJVal"))
        self.cbJVal.addItem(_fromUtf8(""))
        self.cbJVal.addItem(_fromUtf8(""))
        self.cbJVal.addItem(_fromUtf8(""))
        self.cbJVal.addItem(_fromUtf8(""))
        self.twRegs.addTab(self.wtJ, _fromUtf8(""))
        self.cbADC = QtGui.QComboBox(self.centralwidget)
        self.cbADC.setGeometry(QtCore.QRect(450, 16, 221, 41))
        self.cbADC.setObjectName(_fromUtf8("cbADC"))
        self.cbADC.addItem(_fromUtf8(""))
        self.cbADC.addItem(_fromUtf8(""))
        self.label_15 = QtGui.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(10, 22, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_15.setFont(font)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.leAddrMB = QtGui.QLineEdit(self.centralwidget)
        self.leAddrMB.setGeometry(QtCore.QRect(200, 20, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.leAddrMB.setFont(font)
        self.leAddrMB.setObjectName(_fromUtf8("leAddrMB"))
        self.label_16 = QtGui.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(320, 20, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_16.setFont(font)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.cbPE2 = QtGui.QCheckBox(self.centralwidget)
        self.cbPE2.setGeometry(QtCore.QRect(20, 70, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.cbPE2.setFont(font)
        self.cbPE2.setObjectName(_fromUtf8("cbPE2"))
        self.cbPE6 = QtGui.QCheckBox(self.centralwidget)
        self.cbPE6.setEnabled(False)
        self.cbPE6.setGeometry(QtCore.QRect(20, 120, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.cbPE6.setFont(font)
        self.cbPE6.setChecked(False)
        self.cbPE6.setObjectName(_fromUtf8("cbPE6"))
        self.tbSwitch = QtGui.QToolButton(self.centralwidget)
        self.tbSwitch.setGeometry(QtCore.QRect(460, 133, 164, 41))
        self.tbSwitch.setObjectName(_fromUtf8("tbSwitch"))
        self.llData_2 = QtGui.QLabel(self.centralwidget)
        self.llData_2.setGeometry(QtCore.QRect(420, 70, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.llData_2.setFont(font)
        self.llData_2.setFrameShape(QtGui.QFrame.Panel)
        self.llData_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.llData_2.setObjectName(_fromUtf8("llData_2"))
        self.cbPD5 = QtGui.QCheckBox(self.centralwidget)
        self.cbPD5.setGeometry(QtCore.QRect(180, 120, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.cbPD5.setFont(font)
        self.cbPD5.setChecked(False)
        self.cbPD5.setObjectName(_fromUtf8("cbPD5"))
        self.cbPF1 = QtGui.QCheckBox(self.centralwidget)
        self.cbPF1.setGeometry(QtCore.QRect(180, 70, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.cbPF1.setFont(font)
        self.cbPF1.setObjectName(_fromUtf8("cbPF1"))
        fmAD779x.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(fmAD779x)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 821, 38))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu = QtGui.QMenu(self.menubar)
        self.menu.setObjectName(_fromUtf8("menu"))
        fmAD779x.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(fmAD779x)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        fmAD779x.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(fmAD779x)
        self.twRegs.setCurrentIndex(1)
        self.cbMode.setCurrentIndex(5)
        self.cbFadc.setCurrentIndex(10)
        self.cbClock.setCurrentIndex(0)
        self.cbBias.setCurrentIndex(0)
        self.cbRef.setCurrentIndex(1)
        self.cbChan.setCurrentIndex(0)
        self.cbCode.setCurrentIndex(0)
        self.cbAmp.setCurrentIndex(7)
        self.cbJDir.setCurrentIndex(0)
        self.cbJVal.setCurrentIndex(0)
        self.cbADC.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(fmAD779x)

    def retranslateUi(self, fmAD779x):
        fmAD779x.setWindowTitle(_translate("fmAD779x", "Прямой доступ к AD779x", None))
        self.label.setText(_translate("fmAD779x", "Данные АЦП:", None))
        self.tbDataRd.setText(_translate("fmAD779x", "Rd", None))
        self.label_2.setText(_translate("fmAD779x", "Статус АЦП:", None))
        self.tbStatusRd.setText(_translate("fmAD779x", "Rd", None))
        self.tbOffsetWr.setText(_translate("fmAD779x", "Wr", None))
        self.label_11.setText(_translate("fmAD779x", "Смещение нуля:", None))
        self.tbScaleWr.setText(_translate("fmAD779x", "Wr", None))
        self.tbScaleRd.setText(_translate("fmAD779x", "Rd", None))
        self.label_12.setText(_translate("fmAD779x", "Коэффициент:", None))
        self.tbIDRd.setText(_translate("fmAD779x", "Rd", None))
        self.label_13.setText(_translate("fmAD779x", "ID:", None))
        self.tbDataA.setText(_translate("fmAD779x", "A", None))
        self.tbConv.setText(_translate("fmAD779x", "M", None))
        self.tbOffsetRd.setText(_translate("fmAD779x", "Rd", None))
        self.twRegs.setTabText(self.twRegs.indexOf(self.wtData), _translate("fmAD779x", "Данные", None))
        self.label_3.setText(_translate("fmAD779x", "ADC mode <b>(hex)</b>:", None))
        self.tbModeRd.setText(_translate("fmAD779x", "Rd", None))
        self.tbModeWr.setText(_translate("fmAD779x", "Wr", None))
        self.cbMode.setItemText(0, _translate("fmAD779x", "Continuos Conversion", None))
        self.cbMode.setItemText(1, _translate("fmAD779x", "Single Conversion", None))
        self.cbMode.setItemText(2, _translate("fmAD779x", "Idle Mode", None))
        self.cbMode.setItemText(3, _translate("fmAD779x", "Power Down", None))
        self.cbMode.setItemText(4, _translate("fmAD779x", "Internal Zero Calibration", None))
        self.cbMode.setItemText(5, _translate("fmAD779x", "Internal Full-Scale Calibration", None))
        self.cbMode.setItemText(6, _translate("fmAD779x", "System Zero Calibration", None))
        self.cbMode.setItemText(7, _translate("fmAD779x", "System Full-Scale Calibration", None))
        self.cbFadc.setItemText(0, _translate("fmAD779x", "недопустимое значение", None))
        self.cbFadc.setItemText(1, _translate("fmAD779x", "470 Гц", None))
        self.cbFadc.setItemText(2, _translate("fmAD779x", "242 Гц", None))
        self.cbFadc.setItemText(3, _translate("fmAD779x", "123 Гц", None))
        self.cbFadc.setItemText(4, _translate("fmAD779x", "62 Гц", None))
        self.cbFadc.setItemText(5, _translate("fmAD779x", "50 Гц", None))
        self.cbFadc.setItemText(6, _translate("fmAD779x", "39 Гц", None))
        self.cbFadc.setItemText(7, _translate("fmAD779x", "33,2  Гц", None))
        self.cbFadc.setItemText(8, _translate("fmAD779x", "19,6 Гц", None))
        self.cbFadc.setItemText(9, _translate("fmAD779x", "16,7 Гц (80 dB @ 50 Гц)", None))
        self.cbFadc.setItemText(10, _translate("fmAD779x", "16,7 Гц (65 dB @ 50 Гц и 60 Гц)", None))
        self.cbFadc.setItemText(11, _translate("fmAD779x", "12,5 Гц (66 dB @ 50 Гц и 60 Гц)", None))
        self.cbFadc.setItemText(12, _translate("fmAD779x", "10 Гц    (69 dB @ 50 Гц и 60 Гц)", None))
        self.cbFadc.setItemText(13, _translate("fmAD779x", "8,33 Гц (70 dB @ 50 Гц и 60 Гц)", None))
        self.cbFadc.setItemText(14, _translate("fmAD779x", "6,25 Гц (72 dB @ 50 Гц и 60 Гц)", None))
        self.cbFadc.setItemText(15, _translate("fmAD779x", "4,17 Гц (74 dB @ 50 Гц и 60 Гц)", None))
        self.label_4.setText(_translate("fmAD779x", " Выходная частота:", None))
        self.label_14.setText(_translate("fmAD779x", " Опорная частота:", None))
        self.cbClock.setItemText(0, _translate("fmAD779x", "Internal 64 kHz (CLK disconnected)", None))
        self.cbClock.setItemText(1, _translate("fmAD779x", "Internal 64 kHz (CLK out)", None))
        self.cbClock.setItemText(2, _translate("fmAD779x", "External 64 kHz ", None))
        self.cbClock.setItemText(3, _translate("fmAD779x", "External clock divided by 2", None))
        self.twRegs.setTabText(self.twRegs.indexOf(self.wtMode), _translate("fmAD779x", "Режим", None))
        self.tbConfRd.setText(_translate("fmAD779x", "Rd", None))
        self.tbConfWr.setText(_translate("fmAD779x", "Wr", None))
        self.label_5.setText(_translate("fmAD779x", "ADC conf <b>(hex)</b>:", None))
        self.cbBias.setItemText(0, _translate("fmAD779x", "отключен", None))
        self.cbBias.setItemText(1, _translate("fmAD779x", "к AIN1(-)", None))
        self.cbBias.setItemText(2, _translate("fmAD779x", "к AIN2(-)", None))
        self.cbBias.setItemText(3, _translate("fmAD779x", "зарезервировано", None))
        self.chBurnT.setText(_translate("fmAD779x", "Тестовый ист. тока", None))
        self.cbRef.setItemText(0, _translate("fmAD779x", "Внешний", None))
        self.cbRef.setItemText(1, _translate("fmAD779x", "Внутренний", None))
        self.label_7.setText(_translate("fmAD779x", "Опорный источник:", None))
        self.cbChan.setItemText(0, _translate("fmAD779x", "AIN1(+) - AIN1(-)", None))
        self.cbChan.setItemText(1, _translate("fmAD779x", "AIN2(+) - AIN2(-)", None))
        self.cbChan.setItemText(2, _translate("fmAD779x", "AIN3(+) - AIN3(-)", None))
        self.cbChan.setItemText(3, _translate("fmAD779x", "AIN1(-) - AIN1(-)", None))
        self.cbChan.setItemText(4, _translate("fmAD779x", "зарезервировано", None))
        self.cbChan.setItemText(5, _translate("fmAD779x", "зарезервировано", None))
        self.cbChan.setItemText(6, _translate("fmAD779x", "термодатчик", None))
        self.cbChan.setItemText(7, _translate("fmAD779x", "AVdd", None))
        self.label_8.setText(_translate("fmAD779x", "Канал:", None))
        self.label_9.setText(_translate("fmAD779x", "Источник смещения:", None))
        self.chABias.setText(_translate("fmAD779x", "Усиленный  ист. смещения", None))
        self.chAmp.setText(_translate("fmAD779x", "Усиленный вход", None))
        self.label_10.setText(_translate("fmAD779x", "Код:", None))
        self.cbCode.setItemText(0, _translate("fmAD779x", "Двухполярный", None))
        self.cbCode.setItemText(1, _translate("fmAD779x", "Однополярный", None))
        self.label_6.setText(_translate("fmAD779x", "Усиление:", None))
        self.cbAmp.setItemText(0, _translate("fmAD779x", "x1", None))
        self.cbAmp.setItemText(1, _translate("fmAD779x", "x2", None))
        self.cbAmp.setItemText(2, _translate("fmAD779x", "x4", None))
        self.cbAmp.setItemText(3, _translate("fmAD779x", "x8", None))
        self.cbAmp.setItemText(4, _translate("fmAD779x", "x16", None))
        self.cbAmp.setItemText(5, _translate("fmAD779x", "x32", None))
        self.cbAmp.setItemText(6, _translate("fmAD779x", "x64", None))
        self.cbAmp.setItemText(7, _translate("fmAD779x", "x128", None))
        self.twRegs.setTabText(self.twRegs.indexOf(self.wtConf), _translate("fmAD779x", "Конфигурация", None))
        self.label_17.setText(_translate("fmAD779x", "ADC IO <b>(hex)</b>:", None))
        self.tbIOWr.setText(_translate("fmAD779x", "Wr", None))
        self.tbIORd.setText(_translate("fmAD779x", "Rd", None))
        self.cbJDir.setItemText(0, _translate("fmAD779x", "(IEXC1 -> IOUT1)  (IEXC2 -> IOUT2)", None))
        self.cbJDir.setItemText(1, _translate("fmAD779x", "(IEXC1 -> IOUT2)  (IEXC2 -> IOUT1)", None))
        self.cbJDir.setItemText(2, _translate("fmAD779x", "Оба источника на IOUT1", None))
        self.cbJDir.setItemText(3, _translate("fmAD779x", "Оба источника на IOUT2", None))
        self.label_18.setText(_translate("fmAD779x", "Коммутация источников:", None))
        self.label_19.setText(_translate("fmAD779x", "Величина тока:", None))
        self.cbJVal.setItemText(0, _translate("fmAD779x", "откл.", None))
        self.cbJVal.setItemText(1, _translate("fmAD779x", "10 uA", None))
        self.cbJVal.setItemText(2, _translate("fmAD779x", "210 uA", None))
        self.cbJVal.setItemText(3, _translate("fmAD779x", "1 mA", None))
        self.twRegs.setTabText(self.twRegs.indexOf(self.wtJ), _translate("fmAD779x", "Источники тока", None))
        self.cbADC.setItemText(0, _translate("fmAD779x", "AD7792 (16 бит)", None))
        self.cbADC.setItemText(1, _translate("fmAD779x", "AD7793 (24  бит)", None))
        self.label_15.setText(_translate("fmAD779x", "Адрес MODBUS:", None))
        self.label_16.setText(_translate("fmAD779x", "Тип АЦП:", None))
        self.cbPE2.setText(_translate("fmAD779x", "PE2 = 1", None))
        self.cbPE6.setText(_translate("fmAD779x", "PE6 = 1", None))
        self.tbSwitch.setText(_translate("fmAD779x", "Установить", None))
        self.llData_2.setText(_translate("fmAD779x", "Входной коммутатор", None))
        self.cbPD5.setText(_translate("fmAD779x", "PD5 = 1", None))
        self.cbPF1.setText(_translate("fmAD779x", "PF1 = 1", None))
        self.menu.setTitle(_translate("fmAD779x", "?", None))
