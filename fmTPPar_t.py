# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\ormet\source\svi (4)\svi\forms\fmTPPar.ui'
#
# Created: Thu Sep 13 10:45:12 2018
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

class Ui_fmTPPar(object):
    def setupUi(self, fmTPPar):
        fmTPPar.setObjectName(_fromUtf8("fmTPPar"))
        fmTPPar.resize(874, 872)
        fmTPPar.setMinimumSize(QtCore.QSize(874, 872))
        fmTPPar.setMaximumSize(QtCore.QSize(874, 872))
        self.centralwidget = QtGui.QWidget(fmTPPar)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.line_4 = QtGui.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(0, 426, 851, 20))
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.line_5 = QtGui.QFrame(self.centralwidget)
        self.line_5.setGeometry(QtCore.QRect(15, 610, 591, 16))
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.tbP0Rd = QtGui.QToolButton(self.centralwidget)
        self.tbP0Rd.setGeometry(QtCore.QRect(730, 460, 41, 41))
        self.tbP0Rd.setObjectName(_fromUtf8("tbP0Rd"))
        self.lcdDataConv_P = QtGui.QLCDNumber(self.centralwidget)
        self.lcdDataConv_P.setGeometry(QtCore.QRect(21, 560, 241, 41))
        self.lcdDataConv_P.setObjectName(_fromUtf8("lcdDataConv_P"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(23, 505, 261, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_7.setFont(font)
        self.label_7.setFrameShape(QtGui.QFrame.Box)
        self.label_7.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_7.setAlignment(QtCore.Qt.AlignCenter)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_15 = QtGui.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(540, 460, 61, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_15.setFont(font)
        self.label_15.setLineWidth(-5)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.llData_P = QtGui.QLabel(self.centralwidget)
        self.llData_P.setGeometry(QtCore.QRect(200, 446, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.llData_P.setFont(font)
        self.llData_P.setFrameShape(QtGui.QFrame.Panel)
        self.llData_P.setFrameShadow(QtGui.QFrame.Sunken)
        self.llData_P.setText(_fromUtf8(""))
        self.llData_P.setObjectName(_fromUtf8("llData_P"))
        self.tbScan_P = QtGui.QToolButton(self.centralwidget)
        self.tbScan_P.setGeometry(QtCore.QRect(272, 559, 41, 41))
        self.tbScan_P.setObjectName(_fromUtf8("tbScan_P"))
        self.line_6 = QtGui.QFrame(self.centralwidget)
        self.line_6.setGeometry(QtCore.QRect(400, 460, 20, 131))
        self.line_6.setFrameShape(QtGui.QFrame.VLine)
        self.line_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_6.setObjectName(_fromUtf8("line_6"))
        self.leP0 = QtGui.QLineEdit(self.centralwidget)
        self.leP0.setGeometry(QtCore.QRect(630, 460, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.leP0.setFont(font)
        self.leP0.setObjectName(_fromUtf8("leP0"))
        self.tbAutoScan_P = QtGui.QToolButton(self.centralwidget)
        self.tbAutoScan_P.setGeometry(QtCore.QRect(330, 560, 41, 41))
        self.tbAutoScan_P.setObjectName(_fromUtf8("tbAutoScan_P"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 450, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.tbP0Wr = QtGui.QToolButton(self.centralwidget)
        self.tbP0Wr.setGeometry(QtCore.QRect(780, 460, 41, 41))
        self.tbP0Wr.setObjectName(_fromUtf8("tbP0Wr"))
        self.label_19 = QtGui.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(540, 510, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_19.setFont(font)
        self.label_19.setLineWidth(-5)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.tbApRd = QtGui.QToolButton(self.centralwidget)
        self.tbApRd.setGeometry(QtCore.QRect(730, 510, 41, 41))
        self.tbApRd.setObjectName(_fromUtf8("tbApRd"))
        self.leAp = QtGui.QLineEdit(self.centralwidget)
        self.leAp.setGeometry(QtCore.QRect(630, 510, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.leAp.setFont(font)
        self.leAp.setObjectName(_fromUtf8("leAp"))
        self.tbApWr = QtGui.QToolButton(self.centralwidget)
        self.tbApWr.setGeometry(QtCore.QRect(780, 510, 41, 41))
        self.tbApWr.setObjectName(_fromUtf8("tbApWr"))
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(460, 760, 221, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.line_8 = QtGui.QFrame(self.centralwidget)
        self.line_8.setGeometry(QtCore.QRect(20, 780, 591, 16))
        self.line_8.setFrameShape(QtGui.QFrame.HLine)
        self.line_8.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_8.setObjectName(_fromUtf8("line_8"))
        self.llNumPass_2 = QtGui.QLabel(self.centralwidget)
        self.llNumPass_2.setGeometry(QtCore.QRect(727, 750, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.llNumPass_2.setFont(font)
        self.llNumPass_2.setFrameShape(QtGui.QFrame.Panel)
        self.llNumPass_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.llNumPass_2.setText(_fromUtf8(""))
        self.llNumPass_2.setObjectName(_fromUtf8("llNumPass_2"))
        self.llCntS_2 = QtGui.QLabel(self.centralwidget)
        self.llCntS_2.setGeometry(QtCore.QRect(727, 710, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.llCntS_2.setFont(font)
        self.llCntS_2.setFrameShape(QtGui.QFrame.Panel)
        self.llCntS_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.llCntS_2.setText(_fromUtf8(""))
        self.llCntS_2.setObjectName(_fromUtf8("llCntS_2"))
        self.label_20 = QtGui.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(460, 680, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_20.setFont(font)
        self.label_20.setLineWidth(-5)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.leMinCntSP = QtGui.QLineEdit(self.centralwidget)
        self.leMinCntSP.setGeometry(QtCore.QRect(726, 669, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.leMinCntSP.setFont(font)
        self.leMinCntSP.setObjectName(_fromUtf8("leMinCntSP"))
        self.lcdDataConvF_P = QtGui.QLCDNumber(self.centralwidget)
        self.lcdDataConvF_P.setGeometry(QtCore.QRect(18, 695, 241, 41))
        self.lcdDataConvF_P.setObjectName(_fromUtf8("lcdDataConvF_P"))
        self.leWSizeP = QtGui.QLineEdit(self.centralwidget)
        self.leWSizeP.setGeometry(QtCore.QRect(726, 630, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.leWSizeP.setFont(font)
        self.leWSizeP.setObjectName(_fromUtf8("leWSizeP"))
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(16, 632, 281, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_10 = QtGui.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(460, 720, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.llDataF_P = QtGui.QLabel(self.centralwidget)
        self.llDataF_P.setGeometry(QtCore.QRect(310, 630, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.llDataF_P.setFont(font)
        self.llDataF_P.setFrameShape(QtGui.QFrame.Panel)
        self.llDataF_P.setFrameShadow(QtGui.QFrame.Sunken)
        self.llDataF_P.setText(_fromUtf8(""))
        self.llDataF_P.setObjectName(_fromUtf8("llDataF_P"))
        self.label_21 = QtGui.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(460, 640, 191, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_21.setFont(font)
        self.label_21.setLineWidth(-5)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(450, 390, 231, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.leWSize = QtGui.QLineEdit(self.centralwidget)
        self.leWSize.setGeometry(QtCore.QRect(720, 250, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.leWSize.setFont(font)
        self.leWSize.setObjectName(_fromUtf8("leWSize"))
        self.leMinCntS = QtGui.QLineEdit(self.centralwidget)
        self.leMinCntS.setGeometry(QtCore.QRect(720, 290, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.leMinCntS.setFont(font)
        self.leMinCntS.setObjectName(_fromUtf8("leMinCntS"))
        self.tbCR0Wr = QtGui.QToolButton(self.centralwidget)
        self.tbCR0Wr.setGeometry(QtCore.QRect(790, 70, 41, 41))
        self.tbCR0Wr.setObjectName(_fromUtf8("tbCR0Wr"))
        self.tbAutoScan = QtGui.QToolButton(self.centralwidget)
        self.tbAutoScan.setGeometry(QtCore.QRect(272, 180, 41, 41))
        self.tbAutoScan.setObjectName(_fromUtf8("tbAutoScan"))
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(20, 50, 831, 16))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.leCR0 = QtGui.QLineEdit(self.centralwidget)
        self.leCR0.setGeometry(QtCore.QRect(630, 70, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.leCR0.setFont(font)
        self.leCR0.setObjectName(_fromUtf8("leCR0"))
        self.label_16 = QtGui.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(25, 15, 181, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_16.setFont(font)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.llCntS = QtGui.QLabel(self.centralwidget)
        self.llCntS.setGeometry(QtCore.QRect(721, 340, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.llCntS.setFont(font)
        self.llCntS.setFrameShape(QtGui.QFrame.Panel)
        self.llCntS.setFrameShadow(QtGui.QFrame.Sunken)
        self.llCntS.setText(_fromUtf8(""))
        self.llCntS.setObjectName(_fromUtf8("llCntS"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(28, 120, 311, 41))
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
        self.label_18 = QtGui.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(451, 260, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_18.setFont(font)
        self.label_18.setLineWidth(-5)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.llDataF = QtGui.QLabel(self.centralwidget)
        self.llDataF.setGeometry(QtCore.QRect(300, 270, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.llDataF.setFont(font)
        self.llDataF.setFrameShape(QtGui.QFrame.Panel)
        self.llDataF.setFrameShadow(QtGui.QFrame.Sunken)
        self.llDataF.setText(_fromUtf8(""))
        self.llDataF.setObjectName(_fromUtf8("llDataF"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(25, 70, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(25, 262, 261, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.leAddrMB = QtGui.QLineEdit(self.centralwidget)
        self.leAddrMB.setGeometry(QtCore.QRect(214, 14, 80, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.leAddrMB.setFont(font)
        self.leAddrMB.setObjectName(_fromUtf8("leAddrMB"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(390, 80, 20, 131))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(450, 350, 231, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.llData = QtGui.QLabel(self.centralwidget)
        self.llData.setGeometry(QtCore.QRect(200, 70, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.llData.setFont(font)
        self.llData.setFrameShape(QtGui.QFrame.Panel)
        self.llData.setFrameShadow(QtGui.QFrame.Sunken)
        self.llData.setText(_fromUtf8(""))
        self.llData.setObjectName(_fromUtf8("llData"))
        self.llNumPass = QtGui.QLabel(self.centralwidget)
        self.llNumPass.setGeometry(QtCore.QRect(721, 390, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.llNumPass.setFont(font)
        self.llNumPass.setFrameShape(QtGui.QFrame.Panel)
        self.llNumPass.setFrameShadow(QtGui.QFrame.Sunken)
        self.llNumPass.setText(_fromUtf8(""))
        self.llNumPass.setObjectName(_fromUtf8("llNumPass"))
        self.label_17 = QtGui.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(450, 306, 191, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_17.setFont(font)
        self.label_17.setLineWidth(-5)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.tbCR0Rd = QtGui.QToolButton(self.centralwidget)
        self.tbCR0Rd.setGeometry(QtCore.QRect(730, 70, 41, 41))
        self.tbCR0Rd.setObjectName(_fromUtf8("tbCR0Rd"))
        self.lcdDataConv = QtGui.QLCDNumber(self.centralwidget)
        self.lcdDataConv.setGeometry(QtCore.QRect(26, 180, 231, 41))
        self.lcdDataConv.setObjectName(_fromUtf8("lcdDataConv"))
        self.label_14 = QtGui.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(430, 63, 211, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_14.setFont(font)
        self.label_14.setLineWidth(-5)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.tbScan = QtGui.QToolButton(self.centralwidget)
        self.tbScan.setGeometry(QtCore.QRect(332, 180, 41, 41))
        self.tbScan.setObjectName(_fromUtf8("tbScan"))
        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(20, 230, 821, 16))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.lcdDataConvF = QtGui.QLCDNumber(self.centralwidget)
        self.lcdDataConvF.setGeometry(QtCore.QRect(20, 320, 241, 41))
        self.lcdDataConvF.setObjectName(_fromUtf8("lcdDataConvF"))
        fmTPPar.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(fmTPPar)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 874, 38))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        fmTPPar.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(fmTPPar)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        fmTPPar.setStatusBar(self.statusbar)
        self.actConf = QtGui.QAction(fmTPPar)
        self.actConf.setObjectName(_fromUtf8("actConf"))

        self.retranslateUi(fmTPPar)
        QtCore.QMetaObject.connectSlotsByName(fmTPPar)

    def retranslateUi(self, fmTPPar):
        fmTPPar.setWindowTitle(_translate("fmTPPar", " Термометр и Измеритель давления", None))
        self.tbP0Rd.setText(_translate("fmTPPar", "Rd", None))
        self.label_7.setText(_translate("fmTPPar", "P =  Ap*P<sub>АЦП</sub> - P<sub>0</sub>", None))
        self.label_15.setText(_translate("fmTPPar", "P<sub>0</sub>", None))
        self.tbScan_P.setText(_translate("fmTPPar", "Rd", None))
        self.tbAutoScan_P.setText(_translate("fmTPPar", "A", None))
        self.label_2.setText(_translate("fmTPPar", "Данные АЦП P:", None))
        self.tbP0Wr.setText(_translate("fmTPPar", "Wr", None))
        self.label_19.setText(_translate("fmTPPar", "A<sub>p</sub>", None))
        self.tbApRd.setText(_translate("fmTPPar", "Rd", None))
        self.tbApWr.setText(_translate("fmTPPar", "Wr", None))
        self.label_8.setText(_translate("fmTPPar", "Кол-во итераций:", None))
        self.label_20.setText(_translate("fmTPPar", "Мин. отсчетов:", None))
        self.label_9.setText(_translate("fmTPPar", "Данные АЦП P (фильтр):", None))
        self.label_10.setText(_translate("fmTPPar", "Значащие отсчеты:", None))
        self.label_21.setText(_translate("fmTPPar", "Размер окна:", None))
        self.label_6.setText(_translate("fmTPPar", "Кол-во итераций:", None))
        self.tbCR0Wr.setText(_translate("fmTPPar", "Wr", None))
        self.tbAutoScan.setText(_translate("fmTPPar", "A", None))
        self.label_16.setText(_translate("fmTPPar", "Адрес MODBUS:", None))
        self.label_3.setText(_translate("fmTPPar", "T =  (C<sub>АЦП</sub> - С<sub>0</sub>) / (С<sub>0</sub>&#945;)", None))
        self.label_18.setText(_translate("fmTPPar", "Размер окна:", None))
        self.label.setText(_translate("fmTPPar", "Данные АЦП:", None))
        self.label_4.setText(_translate("fmTPPar", "Данные АЦП (фильтр):", None))
        self.label_5.setText(_translate("fmTPPar", "Значащие отсчеты:", None))
        self.label_17.setText(_translate("fmTPPar", "Мин. отсчетов:", None))
        self.tbCR0Rd.setText(_translate("fmTPPar", "Rd", None))
        self.label_14.setText(_translate("fmTPPar", "Код АЦП при 0<sup>o</sup>С", None))
        self.tbScan.setText(_translate("fmTPPar", "Rd", None))
        self.actConf.setText(_translate("fmTPPar", "Настройки", None))
