# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\ormet\source\svi_vs_v.0.3\forms\fmTPar.ui'
#
# Created: Mon Mar 31 17:00:39 2014
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

class Ui_fmTPar(object):
    def setupUi(self, fmTPar):
        fmTPar.setObjectName(_fromUtf8("fmTPar"))
        fmTPar.resize(617, 382)
        fmTPar.setMinimumSize(QtCore.QSize(617, 382))
        fmTPar.setMaximumSize(QtCore.QSize(617, 16777215))
        self.centralwidget = QtGui.QWidget(fmTPar)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.lcdDataConv = QtGui.QLCDNumber(self.centralwidget)
        self.lcdDataConv.setGeometry(QtCore.QRect(16, 150, 241, 41))
        self.lcdDataConv.setObjectName(_fromUtf8("lcdDataConv"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(15, 62, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.tbScan = QtGui.QToolButton(self.centralwidget)
        self.tbScan.setGeometry(QtCore.QRect(267, 149, 27, 22))
        self.tbScan.setObjectName(_fromUtf8("tbScan"))
        self.llData = QtGui.QLabel(self.centralwidget)
        self.llData.setGeometry(QtCore.QRect(175, 60, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.llData.setFont(font)
        self.llData.setFrameShape(QtGui.QFrame.Panel)
        self.llData.setFrameShadow(QtGui.QFrame.Sunken)
        self.llData.setText(_fromUtf8(""))
        self.llData.setObjectName(_fromUtf8("llData"))
        self.tbAutoScan = QtGui.QToolButton(self.centralwidget)
        self.tbAutoScan.setGeometry(QtCore.QRect(267, 170, 27, 22))
        self.tbAutoScan.setObjectName(_fromUtf8("tbAutoScan"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(295, 60, 20, 131))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.tbCR0Wr = QtGui.QToolButton(self.centralwidget)
        self.tbCR0Wr.setGeometry(QtCore.QRect(575, 60, 27, 22))
        self.tbCR0Wr.setObjectName(_fromUtf8("tbCR0Wr"))
        self.leCR0 = QtGui.QLineEdit(self.centralwidget)
        self.leCR0.setGeometry(QtCore.QRect(455, 61, 81, 22))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.leCR0.setFont(font)
        self.leCR0.setObjectName(_fromUtf8("leCR0"))
        self.label_14 = QtGui.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(320, 63, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_14.setFont(font)
        self.label_14.setLineWidth(-5)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.tbCR0Rd = QtGui.QToolButton(self.centralwidget)
        self.tbCR0Rd.setGeometry(QtCore.QRect(545, 60, 27, 22))
        self.tbCR0Rd.setObjectName(_fromUtf8("tbCR0Rd"))
        self.label_16 = QtGui.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(15, 15, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_16.setFont(font)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.leAddrMB = QtGui.QLineEdit(self.centralwidget)
        self.leAddrMB.setGeometry(QtCore.QRect(176, 13, 80, 22))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.leAddrMB.setFont(font)
        self.leAddrMB.setObjectName(_fromUtf8("leAddrMB"))
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(10, 40, 591, 16))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(18, 95, 241, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setFrameShape(QtGui.QFrame.Box)
        self.label_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(10, 200, 591, 16))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(15, 222, 161, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.llDataF = QtGui.QLabel(self.centralwidget)
        self.llDataF.setGeometry(QtCore.QRect(175, 220, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.llDataF.setFont(font)
        self.llDataF.setFrameShape(QtGui.QFrame.Panel)
        self.llDataF.setFrameShadow(QtGui.QFrame.Sunken)
        self.llDataF.setText(_fromUtf8(""))
        self.llDataF.setObjectName(_fromUtf8("llDataF"))
        self.lcdDataConvF = QtGui.QLCDNumber(self.centralwidget)
        self.lcdDataConvF.setGeometry(QtCore.QRect(17, 285, 241, 41))
        self.lcdDataConvF.setObjectName(_fromUtf8("lcdDataConvF"))
        self.leWSize = QtGui.QLineEdit(self.centralwidget)
        self.leWSize.setGeometry(QtCore.QRect(455, 218, 81, 22))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.leWSize.setFont(font)
        self.leWSize.setObjectName(_fromUtf8("leWSize"))
        self.label_17 = QtGui.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(320, 250, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_17.setFont(font)
        self.label_17.setLineWidth(-5)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.leMinCntS = QtGui.QLineEdit(self.centralwidget)
        self.leMinCntS.setGeometry(QtCore.QRect(455, 247, 81, 22))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.leMinCntS.setFont(font)
        self.leMinCntS.setObjectName(_fromUtf8("leMinCntS"))
        self.label_18 = QtGui.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(319, 220, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_18.setFont(font)
        self.label_18.setLineWidth(-5)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.llCntS = QtGui.QLabel(self.centralwidget)
        self.llCntS.setGeometry(QtCore.QRect(456, 278, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.llCntS.setFont(font)
        self.llCntS.setFrameShape(QtGui.QFrame.Panel)
        self.llCntS.setFrameShadow(QtGui.QFrame.Sunken)
        self.llCntS.setText(_fromUtf8(""))
        self.llCntS.setObjectName(_fromUtf8("llCntS"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(320, 280, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.llNumPass = QtGui.QLabel(self.centralwidget)
        self.llNumPass.setGeometry(QtCore.QRect(456, 308, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.llNumPass.setFont(font)
        self.llNumPass.setFrameShape(QtGui.QFrame.Panel)
        self.llNumPass.setFrameShadow(QtGui.QFrame.Sunken)
        self.llNumPass.setText(_fromUtf8(""))
        self.llNumPass.setObjectName(_fromUtf8("llNumPass"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(320, 310, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        fmTPar.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(fmTPar)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 617, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        fmTPar.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(fmTPar)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        fmTPar.setStatusBar(self.statusbar)
        self.actConf = QtGui.QAction(fmTPar)
        self.actConf.setObjectName(_fromUtf8("actConf"))

        self.retranslateUi(fmTPar)
        QtCore.QMetaObject.connectSlotsByName(fmTPar)

    def retranslateUi(self, fmTPar):
        fmTPar.setWindowTitle(_translate("fmTPar", " Термометр", None))
        self.label.setText(_translate("fmTPar", "Данные АЦП:", None))
        self.tbScan.setText(_translate("fmTPar", "Rd", None))
        self.tbAutoScan.setText(_translate("fmTPar", "A", None))
        self.tbCR0Wr.setText(_translate("fmTPar", "Wr", None))
        self.label_14.setText(_translate("fmTPar", "Код АЦП при 0<sup>o</sup>С", None))
        self.tbCR0Rd.setText(_translate("fmTPar", "Rd", None))
        self.label_16.setText(_translate("fmTPar", "Адрес MODBUS:", None))
        self.label_3.setText(_translate("fmTPar", "T =  (C<sub>АЦП</sub> - С<sub>0</sub>) / (С<sub>0</sub>&#945;)", None))
        self.label_4.setText(_translate("fmTPar", "Данные АЦП (фильтр):", None))
        self.label_17.setText(_translate("fmTPar", "Мин. отсчетов:", None))
        self.label_18.setText(_translate("fmTPar", "Размер окна:", None))
        self.label_5.setText(_translate("fmTPar", "Значащие отсчеты:", None))
        self.label_6.setText(_translate("fmTPar", "Кол-во итераций:", None))
        self.actConf.setText(_translate("fmTPar", "Настройки", None))

