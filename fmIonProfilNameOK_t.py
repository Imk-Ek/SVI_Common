# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\ormet\source\svi (4)\svi\forms\fmIonProfilNameOK.ui'
#
# Created: Mon Sep 17 14:00:11 2018
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

class Ui_fmIonProfilNameOK(object):
    def setupUi(self, fmIonProfilNameOK):
        fmIonProfilNameOK.setObjectName(_fromUtf8("fmIonProfilNameOK"))
        fmIonProfilNameOK.resize(472, 231)
        fmIonProfilNameOK.setMinimumSize(QtCore.QSize(472, 231))
        fmIonProfilNameOK.setMaximumSize(QtCore.QSize(472, 231))
        self.centralwidget = QtGui.QWidget(fmIonProfilNameOK)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tbSave = QtGui.QToolButton(self.centralwidget)
        self.tbSave.setGeometry(QtCore.QRect(120, 610, 361, 22))
        self.tbSave.setObjectName(_fromUtf8("tbSave"))
        self.tbOK = QtGui.QPushButton(self.centralwidget)
        self.tbOK.setGeometry(QtCore.QRect(180, 140, 101, 51))
        self.tbOK.setObjectName(_fromUtf8("tbOK"))
        self.leProfilName_ = QtGui.QLineEdit(self.centralwidget)
        self.leProfilName_.setGeometry(QtCore.QRect(40, 50, 381, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.leProfilName_.setFont(font)
        self.leProfilName_.setObjectName(_fromUtf8("leProfilName_"))
        fmIonProfilNameOK.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(fmIonProfilNameOK)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        fmIonProfilNameOK.setStatusBar(self.statusbar)

        self.retranslateUi(fmIonProfilNameOK)
        QtCore.QMetaObject.connectSlotsByName(fmIonProfilNameOK)

    def retranslateUi(self, fmIonProfilNameOK):
        fmIonProfilNameOK.setWindowTitle(_translate("fmIonProfilNameOK", "Ввод названия профиля", None))
        self.tbSave.setText(_translate("fmIonProfilNameOK", "Сохранить в энергонезависимой памяти", None))
        self.tbOK.setText(_translate("fmIonProfilNameOK", "OK", None))

