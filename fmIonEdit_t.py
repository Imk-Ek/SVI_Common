# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\ormet\source\svi (4)\svi\forms\fmIonEdit.ui'
#
# Created: Mon Sep 17 14:01:19 2018
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

class Ui_fmIonEdit(object):
    def setupUi(self, fmIonEdit):
        fmIonEdit.setObjectName(_fromUtf8("fmIonEdit"))
        fmIonEdit.resize(498, 410)
        self.groupBox = QtGui.QGroupBox(fmIonEdit)
        self.groupBox.setGeometry(QtCore.QRect(10, 10, 461, 301))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 240, 281, 20))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 60, 221, 21))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.leIonName = QtGui.QLineEdit(self.groupBox)
        self.leIonName.setGeometry(QtCore.QRect(300, 50, 113, 31))
        self.leIonName.setObjectName(_fromUtf8("leIonName"))
        self.label_7 = QtGui.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(10, 120, 161, 21))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.leIonVal = QtGui.QLineEdit(self.groupBox)
        self.leIonVal.setGeometry(QtCore.QRect(300, 110, 113, 31))
        self.leIonVal.setObjectName(_fromUtf8("leIonVal"))
        self.label_8 = QtGui.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(10, 180, 261, 21))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.leMolMassa = QtGui.QLineEdit(self.groupBox)
        self.leMolMassa.setGeometry(QtCore.QRect(300, 170, 113, 31))
        self.leMolMassa.setObjectName(_fromUtf8("leMolMassa"))
        self.leK = QtGui.QLineEdit(self.groupBox)
        self.leK.setGeometry(QtCore.QRect(300, 230, 113, 31))
        self.leK.setObjectName(_fromUtf8("leK"))
        self.tbSaveIon_ = QtGui.QPushButton(fmIonEdit)
        self.tbSaveIon_.setGeometry(QtCore.QRect(140, 340, 151, 51))
        self.tbSaveIon_.setObjectName(_fromUtf8("tbSaveIon_"))

        self.retranslateUi(fmIonEdit)
        QtCore.QMetaObject.connectSlotsByName(fmIonEdit)

    def retranslateUi(self, fmIonEdit):
        fmIonEdit.setWindowTitle(_translate("fmIonEdit", "Dialog", None))
        self.groupBox.setTitle(_translate("fmIonEdit", "Характеристики иона", None))
        self.label_4.setText(_translate("fmIonEdit", "Коэффициент активности", None))
        self.label_5.setText(_translate("fmIonEdit", "Наименование иона", None))
        self.label_7.setText(_translate("fmIonEdit", "Валентность", None))
        self.label_8.setText(_translate("fmIonEdit", "Молярная масса, г/моль", None))
        self.tbSaveIon_.setText(_translate("fmIonEdit", "Сохранить", None))

