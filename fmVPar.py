# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\ormet\source\svi_vs_v.0.4\forms\fmVPar.ui'
#
# Created: Tue Feb 10 14:50:09 2015
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

class Ui_fmVPar(object):
    def setupUi(self, fmVPar):
        fmVPar.setObjectName(_fromUtf8("fmVPar"))
        fmVPar.resize(628, 540)
        self.centralwidget = QtGui.QWidget(fmVPar)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.lcdDataConv = QtGui.QLCDNumber(self.centralwidget)
        self.lcdDataConv.setGeometry(QtCore.QRect(16, 190, 241, 41))
        self.lcdDataConv.setObjectName(_fromUtf8("lcdDataConv"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(15, 72, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.tbScan = QtGui.QToolButton(self.centralwidget)
        self.tbScan.setGeometry(QtCore.QRect(267, 189, 27, 22))
        self.tbScan.setObjectName(_fromUtf8("tbScan"))
        self.llData = QtGui.QLabel(self.centralwidget)
        self.llData.setGeometry(QtCore.QRect(175, 70, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.llData.setFont(font)
        self.llData.setFrameShape(QtGui.QFrame.Panel)
        self.llData.setFrameShadow(QtGui.QFrame.Sunken)
        self.llData.setText(_fromUtf8(""))
        self.llData.setObjectName(_fromUtf8("llData"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(15, 103, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.tbAutoScan = QtGui.QToolButton(self.centralwidget)
        self.tbAutoScan.setGeometry(QtCore.QRect(267, 210, 27, 22))
        self.tbAutoScan.setObjectName(_fromUtf8("tbAutoScan"))
        self.lemK = QtGui.QLineEdit(self.centralwidget)
        self.lemK.setGeometry(QtCore.QRect(455, 160, 81, 22))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lemK.setFont(font)
        self.lemK.setObjectName(_fromUtf8("lemK"))
        self.label_12 = QtGui.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(315, 162, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_12.setFont(font)
        self.label_12.setLineWidth(-5)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.ch24b = QtGui.QCheckBox(self.centralwidget)
        self.ch24b.setGeometry(QtCore.QRect(320, 190, 181, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.ch24b.setFont(font)
        self.ch24b.setObjectName(_fromUtf8("ch24b"))
        self.chZeroComp = QtGui.QCheckBox(self.centralwidget)
        self.chZeroComp.setEnabled(False)
        self.chZeroComp.setGeometry(QtCore.QRect(320, 210, 201, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.chZeroComp.setFont(font)
        self.chZeroComp.setObjectName(_fromUtf8("chZeroComp"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(295, 70, 16, 161))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.tbIgnRd = QtGui.QToolButton(self.centralwidget)
        self.tbIgnRd.setGeometry(QtCore.QRect(545, 70, 27, 22))
        self.tbIgnRd.setObjectName(_fromUtf8("tbIgnRd"))
        self.leIgn = QtGui.QLineEdit(self.centralwidget)
        self.leIgn.setGeometry(QtCore.QRect(455, 71, 81, 22))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.leIgn.setFont(font)
        self.leIgn.setObjectName(_fromUtf8("leIgn"))
        self.label_13 = QtGui.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(320, 73, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_13.setFont(font)
        self.label_13.setLineWidth(-5)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.tbIgnWr = QtGui.QToolButton(self.centralwidget)
        self.tbIgnWr.setGeometry(QtCore.QRect(575, 70, 27, 22))
        self.tbIgnWr.setObjectName(_fromUtf8("tbIgnWr"))
        self.tbZeroWr = QtGui.QToolButton(self.centralwidget)
        self.tbZeroWr.setGeometry(QtCore.QRect(575, 100, 27, 22))
        self.tbZeroWr.setObjectName(_fromUtf8("tbZeroWr"))
        self.leZero = QtGui.QLineEdit(self.centralwidget)
        self.leZero.setGeometry(QtCore.QRect(455, 101, 81, 22))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.leZero.setFont(font)
        self.leZero.setObjectName(_fromUtf8("leZero"))
        self.label_14 = QtGui.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(320, 103, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_14.setFont(font)
        self.label_14.setLineWidth(-5)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.tbZeroRd = QtGui.QToolButton(self.centralwidget)
        self.tbZeroRd.setGeometry(QtCore.QRect(545, 100, 27, 22))
        self.tbZeroRd.setObjectName(_fromUtf8("tbZeroRd"))
        self.tbMeasWr = QtGui.QToolButton(self.centralwidget)
        self.tbMeasWr.setGeometry(QtCore.QRect(575, 130, 27, 22))
        self.tbMeasWr.setObjectName(_fromUtf8("tbMeasWr"))
        self.leMeas = QtGui.QLineEdit(self.centralwidget)
        self.leMeas.setGeometry(QtCore.QRect(455, 131, 81, 22))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.leMeas.setFont(font)
        self.leMeas.setObjectName(_fromUtf8("leMeas"))
        self.label_15 = QtGui.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(320, 133, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_15.setFont(font)
        self.label_15.setLineWidth(-5)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.tbMeasRd = QtGui.QToolButton(self.centralwidget)
        self.tbMeasRd.setGeometry(QtCore.QRect(545, 130, 27, 22))
        self.tbMeasRd.setObjectName(_fromUtf8("tbMeasRd"))
        self.label_16 = QtGui.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(15, 22, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_16.setFont(font)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.leAddrMB = QtGui.QLineEdit(self.centralwidget)
        self.leAddrMB.setGeometry(QtCore.QRect(177, 20, 81, 22))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.leAddrMB.setFont(font)
        self.leAddrMB.setObjectName(_fromUtf8("leAddrMB"))
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 50, 591, 16))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.tbmKRd = QtGui.QToolButton(self.centralwidget)
        self.tbmKRd.setGeometry(QtCore.QRect(545, 160, 27, 22))
        self.tbmKRd.setObjectName(_fromUtf8("tbmKRd"))
        self.tbmKWr = QtGui.QToolButton(self.centralwidget)
        self.tbmKWr.setGeometry(QtCore.QRect(575, 160, 27, 22))
        self.tbmKWr.setObjectName(_fromUtf8("tbmKWr"))
        self.leZeroA = QtGui.QLineEdit(self.centralwidget)
        self.leZeroA.setGeometry(QtCore.QRect(175, 100, 81, 22))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.leZeroA.setFont(font)
        self.leZeroA.setObjectName(_fromUtf8("leZeroA"))
        self.tbZeroAWr = QtGui.QToolButton(self.centralwidget)
        self.tbZeroAWr.setGeometry(QtCore.QRect(265, 100, 27, 22))
        self.tbZeroAWr.setObjectName(_fromUtf8("tbZeroAWr"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(18, 135, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setFrameShape(QtGui.QFrame.Box)
        self.label_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(10, 240, 591, 16))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(15, 262, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.llDataF = QtGui.QLabel(self.centralwidget)
        self.llDataF.setGeometry(QtCore.QRect(175, 260, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.llDataF.setFont(font)
        self.llDataF.setFrameShape(QtGui.QFrame.Panel)
        self.llDataF.setFrameShadow(QtGui.QFrame.Sunken)
        self.llDataF.setText(_fromUtf8(""))
        self.llDataF.setObjectName(_fromUtf8("llDataF"))
        self.lcdDataConvF = QtGui.QLCDNumber(self.centralwidget)
        self.lcdDataConvF.setGeometry(QtCore.QRect(17, 325, 241, 41))
        self.lcdDataConvF.setObjectName(_fromUtf8("lcdDataConvF"))
        self.leWSize = QtGui.QLineEdit(self.centralwidget)
        self.leWSize.setGeometry(QtCore.QRect(455, 258, 81, 22))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.leWSize.setFont(font)
        self.leWSize.setObjectName(_fromUtf8("leWSize"))
        self.label_17 = QtGui.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(320, 290, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_17.setFont(font)
        self.label_17.setLineWidth(-5)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.leMinCntS = QtGui.QLineEdit(self.centralwidget)
        self.leMinCntS.setGeometry(QtCore.QRect(455, 287, 81, 22))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.leMinCntS.setFont(font)
        self.leMinCntS.setObjectName(_fromUtf8("leMinCntS"))
        self.label_18 = QtGui.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(319, 260, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_18.setFont(font)
        self.label_18.setLineWidth(-5)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.llCntS = QtGui.QLabel(self.centralwidget)
        self.llCntS.setGeometry(QtCore.QRect(456, 318, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.llCntS.setFont(font)
        self.llCntS.setFrameShape(QtGui.QFrame.Panel)
        self.llCntS.setFrameShadow(QtGui.QFrame.Sunken)
        self.llCntS.setText(_fromUtf8(""))
        self.llCntS.setObjectName(_fromUtf8("llCntS"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(320, 320, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.llNumPass = QtGui.QLabel(self.centralwidget)
        self.llNumPass.setGeometry(QtCore.QRect(456, 348, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.llNumPass.setFont(font)
        self.llNumPass.setFrameShape(QtGui.QFrame.Panel)
        self.llNumPass.setFrameShadow(QtGui.QFrame.Sunken)
        self.llNumPass.setText(_fromUtf8(""))
        self.llNumPass.setObjectName(_fromUtf8("llNumPass"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(320, 350, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(10, 380, 591, 111))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(350, 20, 111, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.leCounts = QtGui.QLineEdit(self.groupBox)
        self.leCounts.setGeometry(QtCore.QRect(350, 40, 113, 20))
        self.leCounts.setObjectName(_fromUtf8("leCounts"))
        self.tbSaveSettingV = QtGui.QPushButton(self.groupBox)
        self.tbSaveSettingV.setGeometry(QtCore.QRect(370, 70, 75, 23))
        self.tbSaveSettingV.setObjectName(_fromUtf8("tbSaveSettingV"))
        self.lcdDataFilter = QtGui.QLCDNumber(self.groupBox)
        self.lcdDataFilter.setGeometry(QtCore.QRect(10, 30, 241, 41))
        self.lcdDataFilter.setObjectName(_fromUtf8("lcdDataFilter"))
        fmVPar.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(fmVPar)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 628, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        fmVPar.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(fmVPar)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        fmVPar.setStatusBar(self.statusbar)
        self.actConf = QtGui.QAction(fmVPar)
        self.actConf.setObjectName(_fromUtf8("actConf"))

        self.retranslateUi(fmVPar)
        QtCore.QMetaObject.connectSlotsByName(fmVPar)

    def retranslateUi(self, fmVPar):
        fmVPar.setWindowTitle(_translate("fmVPar", "Милливольтметр", None))
        self.label.setText(_translate("fmVPar", "Данные АЦП:", None))
        self.tbScan.setText(_translate("fmVPar", "Rd", None))
        self.label_2.setText(_translate("fmVPar", "Смещение нуля(32р):", None))
        self.tbAutoScan.setText(_translate("fmVPar", "A", None))
        self.label_12.setText(_translate("fmVPar", "Коэффициент(32р):", None))
        self.ch24b.setText(_translate("fmVPar", "24р  АЦП", None))
        self.chZeroComp.setText(_translate("fmVPar", "Автокомпенсация нуля", None))
        self.tbIgnRd.setText(_translate("fmVPar", "Rd", None))
        self.label_13.setText(_translate("fmVPar", "zcntIgn = ", None))
        self.tbIgnWr.setText(_translate("fmVPar", "Wr", None))
        self.tbZeroWr.setText(_translate("fmVPar", "Wr", None))
        self.label_14.setText(_translate("fmVPar", "zcntZero = ", None))
        self.tbZeroRd.setText(_translate("fmVPar", "Rd", None))
        self.tbMeasWr.setText(_translate("fmVPar", "Wr", None))
        self.label_15.setText(_translate("fmVPar", "mcntMeas = ", None))
        self.tbMeasRd.setText(_translate("fmVPar", "Rd", None))
        self.label_16.setText(_translate("fmVPar", "Адрес MODBUS:", None))
        self.tbmKRd.setText(_translate("fmVPar", "Rd", None))
        self.tbmKWr.setText(_translate("fmVPar", "Wr", None))
        self.tbZeroAWr.setText(_translate("fmVPar", "Wr", None))
        self.label_3.setText(_translate("fmVPar", "Выход =  (C<sub>АЦП</sub> - С<sub>0</sub>) / K", None))
        self.label_4.setText(_translate("fmVPar", "Данные АЦП (фильтр):", None))
        self.label_17.setText(_translate("fmVPar", "Мин. отсчетов:", None))
        self.label_18.setText(_translate("fmVPar", "Размер окна:", None))
        self.label_5.setText(_translate("fmVPar", "Значащие отсчеты:", None))
        self.label_6.setText(_translate("fmVPar", "Кол-во итераций:", None))
        self.groupBox.setTitle(_translate("fmVPar", "Округление", None))
        self.label_7.setText(_translate("fmVPar", "Количество отсчетов", None))
        self.leCounts.setText(_translate("fmVPar", "1", None))
        self.tbSaveSettingV.setText(_translate("fmVPar", "Применить", None))
        self.actConf.setText(_translate("fmVPar", "Настройки", None))

