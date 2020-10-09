# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\ormet\source\svi (4)\svi\forms\fmNewConv.ui'
#
# Created: Thu Sep 13 10:41:41 2018
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

class Ui_fmNewConv(object):
    def setupUi(self, fmNewConv):
        fmNewConv.setObjectName(_fromUtf8("fmNewConv"))
        fmNewConv.resize(447, 258)
        self.label_3 = QtGui.QLabel(fmNewConv)
        self.label_3.setGeometry(QtCore.QRect(140, 10, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_3.setFont(font)
        self.label_3.setFrameShape(QtGui.QFrame.Box)
        self.label_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_6 = QtGui.QLabel(fmNewConv)
        self.label_6.setGeometry(QtCore.QRect(170, 140, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_6.setFont(font)
        self.label_6.setFrameShape(QtGui.QFrame.Box)
        self.label_6.setFrameShadow(QtGui.QFrame.Sunken)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.leCm_K = QtGui.QLineEdit(fmNewConv)
        self.leCm_K.setGeometry(QtCore.QRect(240, 184, 101, 22))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.leCm_K.setFont(font)
        self.leCm_K.setObjectName(_fromUtf8("leCm_K"))
        self.leK = QtGui.QLineEdit(fmNewConv)
        self.leK.setGeometry(QtCore.QRect(240, 90, 101, 22))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.leK.setFont(font)
        self.leK.setObjectName(_fromUtf8("leK"))
        self.tbSampleC_K = QtGui.QToolButton(fmNewConv)
        self.tbSampleC_K.setGeometry(QtCore.QRect(350, 184, 81, 22))
        self.tbSampleC_K.setObjectName(_fromUtf8("tbSampleC_K"))
        self.tbSampleC0 = QtGui.QToolButton(fmNewConv)
        self.tbSampleC0.setGeometry(QtCore.QRect(350, 54, 81, 22))
        self.tbSampleC0.setObjectName(_fromUtf8("tbSampleC0"))
        self.label = QtGui.QLabel(fmNewConv)
        self.label.setGeometry(QtCore.QRect(21, 54, 141, 18))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.leAref_K = QtGui.QLineEdit(fmNewConv)
        self.leAref_K.setGeometry(QtCore.QRect(240, 220, 101, 22))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.leAref_K.setFont(font)
        self.leAref_K.setObjectName(_fromUtf8("leAref_K"))
        self.label_4 = QtGui.QLabel(fmNewConv)
        self.label_4.setGeometry(QtCore.QRect(21, 184, 201, 18))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(fmNewConv)
        self.label_5.setGeometry(QtCore.QRect(21, 220, 221, 18))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.leC0 = QtGui.QLineEdit(fmNewConv)
        self.leC0.setGeometry(QtCore.QRect(240, 54, 101, 22))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.leC0.setFont(font)
        self.leC0.setObjectName(_fromUtf8("leC0"))
        self.label_2 = QtGui.QLabel(fmNewConv)
        self.label_2.setGeometry(QtCore.QRect(21, 90, 201, 18))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.tbCalcK = QtGui.QToolButton(fmNewConv)
        self.tbCalcK.setGeometry(QtCore.QRect(350, 90, 81, 22))
        self.tbCalcK.setObjectName(_fromUtf8("tbCalcK"))

        self.retranslateUi(fmNewConv)
        QtCore.QMetaObject.connectSlotsByName(fmNewConv)

    def retranslateUi(self, fmNewConv):
        fmNewConv.setWindowTitle(_translate("fmNewConv", "Масштабирование", None))
        self.label_3.setText(_translate("fmNewConv", "Выход =  <b>К</b>*(<b>C</b><sub>АЦП</sub> - <b>С</b><sub>0</sub>)", None))
        self.label_6.setText(_translate("fmNewConv", "<b>К</b> =  <b>A</b><sub>Э</sub> / <b>С</b><sub>И ЗМ</sub>", None))
        self.tbSampleC_K.setText(_translate("fmNewConv", "Загрузить", None))
        self.tbSampleC0.setText(_translate("fmNewConv", "Загрузить", None))
        self.label.setText(_translate("fmNewConv", "<b>С</b><sub>0</sub> - поправка ноля:", None))
        self.label_4.setText(_translate("fmNewConv", "<b>С</b><sub>И ЗМ</sub> -  измеренный код АЦП:", None))
        self.label_5.setText(_translate("fmNewConv", "<b>A</b><sub>Э</sub> - эталон, соотв. коду <b>С</b><sub>И ЗМ</sub>:", None))
        self.label_2.setText(_translate("fmNewConv", "<b>К</b> - коэффициент пересчета:", None))
        self.tbCalcK.setText(_translate("fmNewConv", "Рассчитать", None))

