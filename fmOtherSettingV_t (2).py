# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\ormet\source\svi_vs_v.0.4\forms\fmOtherSettingV.ui'
#
# Created: Tue Feb 10 15:56:00 2015
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

class Ui_fmOtherSettingV(object):
    def setupUi(self, fmOtherSettingV):
        fmOtherSettingV.setObjectName(_fromUtf8("fmOtherSettingV"))
        fmOtherSettingV.resize(302, 127)
        self.groupBox = QtGui.QGroupBox(fmOtherSettingV)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 281, 111))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 20, 111, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.leCounts = QtGui.QLineEdit(self.groupBox)
        self.leCounts.setGeometry(QtCore.QRect(160, 18, 113, 20))
        self.leCounts.setObjectName(_fromUtf8("leCounts"))
        self.tbSaveSettingV = QtGui.QPushButton(self.groupBox)
        self.tbSaveSettingV.setGeometry(QtCore.QRect(100, 70, 75, 23))
        self.tbSaveSettingV.setObjectName(_fromUtf8("tbSaveSettingV"))

        self.retranslateUi(fmOtherSettingV)
        QtCore.QMetaObject.connectSlotsByName(fmOtherSettingV)

    def retranslateUi(self, fmOtherSettingV):
        fmOtherSettingV.setWindowTitle(_translate("fmOtherSettingV", "Параметры", None))
        self.groupBox.setTitle(_translate("fmOtherSettingV", "Округление", None))
        self.label_5.setText(_translate("fmOtherSettingV", "Количество отсчетов", None))
        self.leCounts.setText(_translate("fmOtherSettingV", "1", None))
        self.tbSaveSettingV.setText(_translate("fmOtherSettingV", "Сохранить", None))

