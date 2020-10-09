# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\ormet\source\svi (4)\svi\forms\fmSelectProfil_Ion.ui'
#
# Created: Tue Sep 18 09:39:15 2018
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

class Ui_fmSelectProfil_Ion(object):
    def setupUi(self, fmSelectProfil_Ion):
        fmSelectProfil_Ion.setObjectName(_fromUtf8("fmSelectProfil_Ion"))
        fmSelectProfil_Ion.resize(1069, 422)
        fmSelectProfil_Ion.setMinimumSize(QtCore.QSize(1069, 422))
        fmSelectProfil_Ion.setMaximumSize(QtCore.QSize(1069, 422))
        self.centralwidget = QtGui.QWidget(fmSelectProfil_Ion)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 292, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.tbSelectProfil = QtGui.QToolButton(self.centralwidget)
        self.tbSelectProfil.setGeometry(QtCore.QRect(20, 270, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tbSelectProfil.setFont(font)
        self.tbSelectProfil.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.tbSelectProfil.setArrowType(QtCore.Qt.NoArrow)
        self.tbSelectProfil.setObjectName(_fromUtf8("tbSelectProfil"))
        self.tbChangeProfil = QtGui.QToolButton(self.centralwidget)
        self.tbChangeProfil.setGeometry(QtCore.QRect(180, 270, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tbChangeProfil.setFont(font)
        self.tbChangeProfil.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.tbChangeProfil.setArrowType(QtCore.Qt.NoArrow)
        self.tbChangeProfil.setObjectName(_fromUtf8("tbChangeProfil"))
        self.tbDelProfil = QtGui.QToolButton(self.centralwidget)
        self.tbDelProfil.setGeometry(QtCore.QRect(500, 270, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tbDelProfil.setFont(font)
        self.tbDelProfil.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.tbDelProfil.setArrowType(QtCore.Qt.NoArrow)
        self.tbDelProfil.setObjectName(_fromUtf8("tbDelProfil"))
        self.tbAddProfil = QtGui.QToolButton(self.centralwidget)
        self.tbAddProfil.setGeometry(QtCore.QRect(340, 270, 121, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tbAddProfil.setFont(font)
        self.tbAddProfil.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.tbAddProfil.setArrowType(QtCore.Qt.NoArrow)
        self.tbAddProfil.setObjectName(_fromUtf8("tbAddProfil"))
        self.tbDescribeProfil = QtGui.QTextBrowser(self.centralwidget)
        self.tbDescribeProfil.setGeometry(QtCore.QRect(549, 70, 501, 171))
        self.tbDescribeProfil.setObjectName(_fromUtf8("tbDescribeProfil"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(590, 20, 292, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lwProfils_ = QtGui.QListWidget(self.centralwidget)
        self.lwProfils_.setGeometry(QtCore.QRect(20, 70, 501, 171))
        self.lwProfils_.setObjectName(_fromUtf8("lwProfils_"))
        fmSelectProfil_Ion.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(fmSelectProfil_Ion)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1069, 38))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        fmSelectProfil_Ion.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(fmSelectProfil_Ion)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        fmSelectProfil_Ion.setStatusBar(self.statusbar)

        self.retranslateUi(fmSelectProfil_Ion)
        QtCore.QMetaObject.connectSlotsByName(fmSelectProfil_Ion)

    def retranslateUi(self, fmSelectProfil_Ion):
        fmSelectProfil_Ion.setWindowTitle(_translate("fmSelectProfil_Ion", "Выбор профиля прибора", None))
        self.label.setText(_translate("fmSelectProfil_Ion", "Профили", None))
        self.tbSelectProfil.setText(_translate("fmSelectProfil_Ion", "Выбрать", None))
        self.tbChangeProfil.setText(_translate("fmSelectProfil_Ion", "Изменить", None))
        self.tbDelProfil.setText(_translate("fmSelectProfil_Ion", "Удалить", None))
        self.tbAddProfil.setText(_translate("fmSelectProfil_Ion", "Добавить", None))
        self.label_2.setText(_translate("fmSelectProfil_Ion", "Описание", None))

