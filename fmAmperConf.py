# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\ormet\source\svi_vs_v.0.4\forms\fmAmperConf.ui'
#
# Created: Thu Feb 12 11:27:31 2015
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

class Ui_fmAmperConf(object):
    def setupUi(self, fmAmperConf):
        fmAmperConf.setObjectName(_fromUtf8("fmAmperConf"))
        fmAmperConf.resize(783, 449)
        self.centralwidget = QtGui.QWidget(fmAmperConf)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.leAddrMB = QtGui.QLineEdit(self.centralwidget)
        self.leAddrMB.setGeometry(QtCore.QRect(192, 18, 81, 22))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.leAddrMB.setFont(font)
        self.leAddrMB.setObjectName(_fromUtf8("leAddrMB"))
        self.label_16 = QtGui.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(10, 20, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_16.setFont(font)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.tbAddrMBWr = QtGui.QToolButton(self.centralwidget)
        self.tbAddrMBWr.setGeometry(QtCore.QRect(310, 17, 27, 22))
        self.tbAddrMBWr.setObjectName(_fromUtf8("tbAddrMBWr"))
        self.tbAddrMBRd = QtGui.QToolButton(self.centralwidget)
        self.tbAddrMBRd.setGeometry(QtCore.QRect(280, 17, 27, 22))
        self.tbAddrMBRd.setObjectName(_fromUtf8("tbAddrMBRd"))
        self.tbthrATRd = QtGui.QToolButton(self.centralwidget)
        self.tbthrATRd.setGeometry(QtCore.QRect(280, 47, 27, 22))
        self.tbthrATRd.setObjectName(_fromUtf8("tbthrATRd"))
        self.tbthrATWr = QtGui.QToolButton(self.centralwidget)
        self.tbthrATWr.setGeometry(QtCore.QRect(310, 47, 27, 22))
        self.tbthrATWr.setObjectName(_fromUtf8("tbthrATWr"))
        self.lethrAT = QtGui.QLineEdit(self.centralwidget)
        self.lethrAT.setGeometry(QtCore.QRect(192, 48, 81, 22))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lethrAT.setFont(font)
        self.lethrAT.setObjectName(_fromUtf8("lethrAT"))
        self.label_17 = QtGui.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(10, 50, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_17.setFont(font)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.tbConfRd = QtGui.QToolButton(self.centralwidget)
        self.tbConfRd.setGeometry(QtCore.QRect(280, 240, 27, 22))
        self.tbConfRd.setObjectName(_fromUtf8("tbConfRd"))
        self.tbConfWr = QtGui.QToolButton(self.centralwidget)
        self.tbConfWr.setGeometry(QtCore.QRect(310, 240, 27, 22))
        self.tbConfWr.setObjectName(_fromUtf8("tbConfWr"))
        self.leConf = QtGui.QLineEdit(self.centralwidget)
        self.leConf.setGeometry(QtCore.QRect(192, 241, 81, 22))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.leConf.setFont(font)
        self.leConf.setObjectName(_fromUtf8("leConf"))
        self.label_18 = QtGui.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(10, 244, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_18.setFont(font)
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.label_19 = QtGui.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(10, 324, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_19.setFont(font)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.leSerNum = QtGui.QLineEdit(self.centralwidget)
        self.leSerNum.setGeometry(QtCore.QRect(192, 322, 81, 22))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.leSerNum.setFont(font)
        self.leSerNum.setObjectName(_fromUtf8("leSerNum"))
        self.tbSerNumWr = QtGui.QToolButton(self.centralwidget)
        self.tbSerNumWr.setGeometry(QtCore.QRect(310, 321, 27, 22))
        self.tbSerNumWr.setObjectName(_fromUtf8("tbSerNumWr"))
        self.tbSerNumRd = QtGui.QToolButton(self.centralwidget)
        self.tbSerNumRd.setGeometry(QtCore.QRect(280, 321, 27, 22))
        self.tbSerNumRd.setObjectName(_fromUtf8("tbSerNumRd"))
        self.leZeroA = QtGui.QLineEdit(self.centralwidget)
        self.leZeroA.setGeometry(QtCore.QRect(191, 97, 81, 22))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.leZeroA.setFont(font)
        self.leZeroA.setObjectName(_fromUtf8("leZeroA"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(11, 100, 151, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lemK = QtGui.QLineEdit(self.centralwidget)
        self.lemK.setGeometry(QtCore.QRect(190, 129, 81, 22))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lemK.setFont(font)
        self.lemK.setObjectName(_fromUtf8("lemK"))
        self.label_12 = QtGui.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(12, 130, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_12.setFont(font)
        self.label_12.setLineWidth(-5)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.tbZeroARd = QtGui.QToolButton(self.centralwidget)
        self.tbZeroARd.setGeometry(QtCore.QRect(340, 96, 27, 22))
        self.tbZeroARd.setObjectName(_fromUtf8("tbZeroARd"))
        self.tbZeroAWr = QtGui.QToolButton(self.centralwidget)
        self.tbZeroAWr.setGeometry(QtCore.QRect(370, 96, 27, 22))
        self.tbZeroAWr.setObjectName(_fromUtf8("tbZeroAWr"))
        self.tbZeroARdVar = QtGui.QToolButton(self.centralwidget)
        self.tbZeroARdVar.setGeometry(QtCore.QRect(282, 96, 51, 22))
        self.tbZeroARdVar.setObjectName(_fromUtf8("tbZeroARdVar"))
        self.tbmKRdVar = QtGui.QToolButton(self.centralwidget)
        self.tbmKRdVar.setGeometry(QtCore.QRect(282, 128, 51, 22))
        self.tbmKRdVar.setObjectName(_fromUtf8("tbmKRdVar"))
        self.tbmKRd = QtGui.QToolButton(self.centralwidget)
        self.tbmKRd.setGeometry(QtCore.QRect(340, 128, 27, 22))
        self.tbmKRd.setObjectName(_fromUtf8("tbmKRd"))
        self.tbmKWr = QtGui.QToolButton(self.centralwidget)
        self.tbmKWr.setGeometry(QtCore.QRect(370, 128, 27, 22))
        self.tbmKWr.setObjectName(_fromUtf8("tbmKWr"))
        self.tbModeRd = QtGui.QToolButton(self.centralwidget)
        self.tbModeRd.setGeometry(QtCore.QRect(279, 208, 27, 22))
        self.tbModeRd.setObjectName(_fromUtf8("tbModeRd"))
        self.tbModeWr = QtGui.QToolButton(self.centralwidget)
        self.tbModeWr.setGeometry(QtCore.QRect(309, 208, 27, 22))
        self.tbModeWr.setObjectName(_fromUtf8("tbModeWr"))
        self.leMode = QtGui.QLineEdit(self.centralwidget)
        self.leMode.setGeometry(QtCore.QRect(191, 209, 81, 22))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.leMode.setFont(font)
        self.leMode.setObjectName(_fromUtf8("leMode"))
        self.label_20 = QtGui.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(10, 212, 131, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_20.setFont(font)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.label_21 = QtGui.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(10, 276, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_21.setFont(font)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.leIO = QtGui.QLineEdit(self.centralwidget)
        self.leIO.setGeometry(QtCore.QRect(191, 274, 81, 22))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.leIO.setFont(font)
        self.leIO.setObjectName(_fromUtf8("leIO"))
        self.tbIOWr = QtGui.QToolButton(self.centralwidget)
        self.tbIOWr.setGeometry(QtCore.QRect(309, 273, 27, 22))
        self.tbIOWr.setObjectName(_fromUtf8("tbIOWr"))
        self.tbIORd = QtGui.QToolButton(self.centralwidget)
        self.tbIORd.setGeometry(QtCore.QRect(279, 273, 27, 22))
        self.tbIORd.setObjectName(_fromUtf8("tbIORd"))
        self.tbSave = QtGui.QToolButton(self.centralwidget)
        self.tbSave.setGeometry(QtCore.QRect(11, 367, 361, 22))
        self.tbSave.setObjectName(_fromUtf8("tbSave"))
        self.line_3 = QtGui.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(11, 346, 381, 20))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.label_22 = QtGui.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(10, 160, 171, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_22.setFont(font)
        self.label_22.setObjectName(_fromUtf8("label_22"))
        self.leCount_Amper = QtGui.QLineEdit(self.centralwidget)
        self.leCount_Amper.setGeometry(QtCore.QRect(192, 158, 81, 22))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.leCount_Amper.setFont(font)
        self.leCount_Amper.setObjectName(_fromUtf8("leCount_Amper"))
        self.tbCount_AmperWr = QtGui.QToolButton(self.centralwidget)
        self.tbCount_AmperWr.setGeometry(QtCore.QRect(369, 157, 27, 22))
        self.tbCount_AmperWr.setObjectName(_fromUtf8("tbCount_AmperWr"))
        self.tbCount_AmperRd = QtGui.QToolButton(self.centralwidget)
        self.tbCount_AmperRd.setGeometry(QtCore.QRect(339, 157, 27, 22))
        self.tbCount_AmperRd.setObjectName(_fromUtf8("tbCount_AmperRd"))
        self.tbCount_AmpeRdVar = QtGui.QToolButton(self.centralwidget)
        self.tbCount_AmpeRdVar.setGeometry(QtCore.QRect(282, 157, 51, 22))
        self.tbCount_AmpeRdVar.setObjectName(_fromUtf8("tbCount_AmpeRdVar"))
        self.tbDescribeWr = QtGui.QToolButton(self.centralwidget)
        self.tbDescribeWr.setGeometry(QtCore.QRect(720, 77, 27, 22))
        self.tbDescribeWr.setObjectName(_fromUtf8("tbDescribeWr"))
        self.label_34 = QtGui.QLabel(self.centralwidget)
        self.label_34.setGeometry(QtCore.QRect(450, 107, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_34.setFont(font)
        self.label_34.setObjectName(_fromUtf8("label_34"))
        self.tbTypeIDRd = QtGui.QToolButton(self.centralwidget)
        self.tbTypeIDRd.setGeometry(QtCore.QRect(690, 104, 27, 22))
        self.tbTypeIDRd.setObjectName(_fromUtf8("tbTypeIDRd"))
        self.leTypeID = QtGui.QLineEdit(self.centralwidget)
        self.leTypeID.setGeometry(QtCore.QRect(602, 105, 81, 22))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.leTypeID.setFont(font)
        self.leTypeID.setObjectName(_fromUtf8("leTypeID"))
        self.label_33 = QtGui.QLabel(self.centralwidget)
        self.label_33.setGeometry(QtCore.QRect(450, 10, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_33.setFont(font)
        self.label_33.setObjectName(_fromUtf8("label_33"))
        self.tbTypeIDWr = QtGui.QToolButton(self.centralwidget)
        self.tbTypeIDWr.setGeometry(QtCore.QRect(720, 104, 27, 22))
        self.tbTypeIDWr.setObjectName(_fromUtf8("tbTypeIDWr"))
        self.teDescribe = QtGui.QLineEdit(self.centralwidget)
        self.teDescribe.setGeometry(QtCore.QRect(450, 40, 311, 22))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.teDescribe.setFont(font)
        self.teDescribe.setObjectName(_fromUtf8("teDescribe"))
        self.tbDescribeRd = QtGui.QToolButton(self.centralwidget)
        self.tbDescribeRd.setGeometry(QtCore.QRect(690, 77, 27, 22))
        self.tbDescribeRd.setObjectName(_fromUtf8("tbDescribeRd"))
        fmAmperConf.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(fmAmperConf)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 783, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu = QtGui.QMenu(self.menubar)
        self.menu.setObjectName(_fromUtf8("menu"))
        fmAmperConf.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(fmAmperConf)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        fmAmperConf.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(fmAmperConf)
        QtCore.QMetaObject.connectSlotsByName(fmAmperConf)

    def retranslateUi(self, fmAmperConf):
        fmAmperConf.setWindowTitle(_translate("fmAmperConf", "Настройки микроамперметра ", None))
        self.label_16.setText(_translate("fmAmperConf", "Адрес MODBUS:", None))
        self.tbAddrMBWr.setText(_translate("fmAmperConf", "Wr", None))
        self.tbAddrMBRd.setText(_translate("fmAmperConf", "Rd", None))
        self.tbthrATRd.setText(_translate("fmAmperConf", "Rd", None))
        self.tbthrATWr.setText(_translate("fmAmperConf", "Wr", None))
        self.label_17.setText(_translate("fmAmperConf", "Пауза во фрейме:", None))
        self.tbConfRd.setText(_translate("fmAmperConf", "Rd", None))
        self.tbConfWr.setText(_translate("fmAmperConf", "Wr", None))
        self.label_18.setText(_translate("fmAmperConf", "ADC conf <b>(hex)</b>:", None))
        self.label_19.setText(_translate("fmAmperConf", "Серийный номер:", None))
        self.tbSerNumWr.setText(_translate("fmAmperConf", "Wr", None))
        self.tbSerNumRd.setText(_translate("fmAmperConf", "Rd", None))
        self.label_2.setText(_translate("fmAmperConf", "Смещение нуля(32р):", None))
        self.label_12.setText(_translate("fmAmperConf", "Коэффициент(32р):", None))
        self.tbZeroARd.setText(_translate("fmAmperConf", "Rd", None))
        self.tbZeroAWr.setText(_translate("fmAmperConf", "Wr", None))
        self.tbZeroARdVar.setText(_translate("fmAmperConf", "RdVar", None))
        self.tbmKRdVar.setText(_translate("fmAmperConf", "RdVar", None))
        self.tbmKRd.setText(_translate("fmAmperConf", "Rd", None))
        self.tbmKWr.setText(_translate("fmAmperConf", "Wr", None))
        self.tbModeRd.setText(_translate("fmAmperConf", "Rd", None))
        self.tbModeWr.setText(_translate("fmAmperConf", "Wr", None))
        self.label_20.setText(_translate("fmAmperConf", "ADC mode <b>(hex)</b>:", None))
        self.label_21.setText(_translate("fmAmperConf", "ADC IO <b>(hex)</b>:", None))
        self.tbIOWr.setText(_translate("fmAmperConf", "Wr", None))
        self.tbIORd.setText(_translate("fmAmperConf", "Rd", None))
        self.tbSave.setText(_translate("fmAmperConf", "Сохранить в энергонезависимой памяти", None))
        self.label_22.setText(_translate("fmAmperConf", "Кол-во отсчетов для усред.", None))
        self.tbCount_AmperWr.setText(_translate("fmAmperConf", "Wr", None))
        self.tbCount_AmperRd.setText(_translate("fmAmperConf", "Rd", None))
        self.tbCount_AmpeRdVar.setText(_translate("fmAmperConf", "RdVar", None))
        self.tbDescribeWr.setText(_translate("fmAmperConf", "Wr", None))
        self.label_34.setText(_translate("fmAmperConf", "Тип модуля", None))
        self.tbTypeIDRd.setText(_translate("fmAmperConf", "Rd", None))
        self.label_33.setText(_translate("fmAmperConf", "Описание", None))
        self.tbTypeIDWr.setText(_translate("fmAmperConf", "Wr", None))
        self.tbDescribeRd.setText(_translate("fmAmperConf", "Rd", None))
        self.menu.setTitle(_translate("fmAmperConf", "?", None))

