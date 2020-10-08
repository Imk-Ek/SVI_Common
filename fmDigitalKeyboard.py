# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\ormet\source\svi_meteo_19_11_2015\svi_vs_v.0.6.4\forms\fmDigitalKeyboard.ui'
#
# Created: Thu Feb 11 15:37:10 2016
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

class Ui_fmDigitalKeyboard(object):
    def setupUi(self, fmDigitalKeyboard):
        fmDigitalKeyboard.setObjectName(_fromUtf8("fmDigitalKeyboard"))
        fmDigitalKeyboard.resize(94, 140)
        fmDigitalKeyboard.setMinimumSize(QtCore.QSize(94, 121))
        fmDigitalKeyboard.setMaximumSize(QtCore.QSize(94, 140))
        self.centralwidget = QtGui.QWidget(fmDigitalKeyboard)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tb_1 = QtGui.QToolButton(self.centralwidget)
        self.tb_1.setGeometry(QtCore.QRect(0, 20, 31, 31))
        self.tb_1.setObjectName(_fromUtf8("tb_1"))
        self.tb_2 = QtGui.QToolButton(self.centralwidget)
        self.tb_2.setGeometry(QtCore.QRect(30, 20, 31, 31))
        self.tb_2.setObjectName(_fromUtf8("tb_2"))
        self.tb_3 = QtGui.QToolButton(self.centralwidget)
        self.tb_3.setGeometry(QtCore.QRect(60, 20, 31, 31))
        self.tb_3.setObjectName(_fromUtf8("tb_3"))
        self.tb_6 = QtGui.QToolButton(self.centralwidget)
        self.tb_6.setGeometry(QtCore.QRect(60, 50, 31, 31))
        self.tb_6.setObjectName(_fromUtf8("tb_6"))
        self.tb_5 = QtGui.QToolButton(self.centralwidget)
        self.tb_5.setGeometry(QtCore.QRect(30, 50, 31, 31))
        self.tb_5.setObjectName(_fromUtf8("tb_5"))
        self.tb_4 = QtGui.QToolButton(self.centralwidget)
        self.tb_4.setGeometry(QtCore.QRect(0, 50, 31, 31))
        self.tb_4.setObjectName(_fromUtf8("tb_4"))
        self.tb_0 = QtGui.QToolButton(self.centralwidget)
        self.tb_0.setGeometry(QtCore.QRect(0, 110, 31, 31))
        self.tb_0.setObjectName(_fromUtf8("tb_0"))
        self.tb_b = QtGui.QToolButton(self.centralwidget)
        self.tb_b.setGeometry(QtCore.QRect(30, 110, 31, 31))
        self.tb_b.setObjectName(_fromUtf8("tb_b"))
        self.tb_ = QtGui.QToolButton(self.centralwidget)
        self.tb_.setGeometry(QtCore.QRect(60, 110, 31, 31))
        self.tb_.setText(_fromUtf8(""))
        self.tb_.setObjectName(_fromUtf8("tb_"))
        self.tb_9 = QtGui.QToolButton(self.centralwidget)
        self.tb_9.setGeometry(QtCore.QRect(60, 80, 31, 31))
        self.tb_9.setObjectName(_fromUtf8("tb_9"))
        self.tb_8 = QtGui.QToolButton(self.centralwidget)
        self.tb_8.setGeometry(QtCore.QRect(30, 80, 31, 31))
        self.tb_8.setObjectName(_fromUtf8("tb_8"))
        self.tb_7 = QtGui.QToolButton(self.centralwidget)
        self.tb_7.setGeometry(QtCore.QRect(0, 80, 31, 31))
        self.tb_7.setObjectName(_fromUtf8("tb_7"))
        self.leText = QtGui.QLineEdit(self.centralwidget)
        self.leText.setGeometry(QtCore.QRect(0, 0, 91, 20))
        self.leText.setObjectName(_fromUtf8("leText"))
        fmDigitalKeyboard.setCentralWidget(self.centralwidget)
        self.actConf = QtGui.QAction(fmDigitalKeyboard)
        self.actConf.setObjectName(_fromUtf8("actConf"))

        self.retranslateUi(fmDigitalKeyboard)
        QtCore.QMetaObject.connectSlotsByName(fmDigitalKeyboard)

    def retranslateUi(self, fmDigitalKeyboard):
        fmDigitalKeyboard.setWindowTitle(_translate("fmDigitalKeyboard", "Клавиатура", None))
        self.tb_1.setText(_translate("fmDigitalKeyboard", "1", None))
        self.tb_2.setText(_translate("fmDigitalKeyboard", "2", None))
        self.tb_3.setText(_translate("fmDigitalKeyboard", "3", None))
        self.tb_6.setText(_translate("fmDigitalKeyboard", "6", None))
        self.tb_5.setText(_translate("fmDigitalKeyboard", "5", None))
        self.tb_4.setText(_translate("fmDigitalKeyboard", "4", None))
        self.tb_0.setText(_translate("fmDigitalKeyboard", "0", None))
        self.tb_b.setText(_translate("fmDigitalKeyboard", ".", None))
        self.tb_9.setText(_translate("fmDigitalKeyboard", "9", None))
        self.tb_8.setText(_translate("fmDigitalKeyboard", "8", None))
        self.tb_7.setText(_translate("fmDigitalKeyboard", "7", None))
        self.actConf.setText(_translate("fmDigitalKeyboard", "Настройки", None))

