# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\ormet\source\svi_meteo_19_11_2015\svi_vs_v.0.6.5\forms\fmIonDigitSelect.ui'
#
# Created: Fri Jul  1 16:23:06 2016
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

class Ui_fmIonDigitSelect(object):
    def setupUi(self, fmIonDigitSelect):
        fmIonDigitSelect.setObjectName(_fromUtf8("fmIonDigitSelect"))
        fmIonDigitSelect.resize(283, 315)
        fmIonDigitSelect.setMinimumSize(QtCore.QSize(283, 315))
        fmIonDigitSelect.setMaximumSize(QtCore.QSize(283, 315))
        self.tbSelectDigitIon = QtGui.QPushButton(fmIonDigitSelect)
        self.tbSelectDigitIon.setGeometry(QtCore.QRect(100, 240, 75, 23))
        self.tbSelectDigitIon.setObjectName(_fromUtf8("tbSelectDigitIon"))
        self.leIonDigitSelect_ = QtGui.QLineEdit(fmIonDigitSelect)
        self.leIonDigitSelect_.setGeometry(QtCore.QRect(80, 210, 113, 20))
        self.leIonDigitSelect_.setObjectName(_fromUtf8("leIonDigitSelect_"))
        self.twIonDigitSelect_ = QtGui.QTableWidget(fmIonDigitSelect)
        self.twIonDigitSelect_.setGeometry(QtCore.QRect(10, 0, 241, 192))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.twIonDigitSelect_.sizePolicy().hasHeightForWidth())
        self.twIonDigitSelect_.setSizePolicy(sizePolicy)
        self.twIonDigitSelect_.setObjectName(_fromUtf8("twIonDigitSelect_"))
        self.twIonDigitSelect_.setColumnCount(0)
        self.twIonDigitSelect_.setRowCount(0)

        self.retranslateUi(fmIonDigitSelect)
        QtCore.QMetaObject.connectSlotsByName(fmIonDigitSelect)

    def retranslateUi(self, fmIonDigitSelect):
        fmIonDigitSelect.setWindowTitle(_translate("fmIonDigitSelect", "Dialog", None))
        self.tbSelectDigitIon.setText(_translate("fmIonDigitSelect", "Выбрать", None))

