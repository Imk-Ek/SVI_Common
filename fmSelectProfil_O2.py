# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\ormet\source\svi_vs_v.0.4\forms\fmSelectProfil_O2.ui'
#
# Created: Fri Dec  5 15:23:16 2014
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

class Ui_fmSelectProfil_O2(object):
    def setupUi(self, fmSelectProfil_O2):
        fmSelectProfil_O2.setObjectName(_fromUtf8("fmSelectProfil_O2"))
        fmSelectProfil_O2.resize(672, 309)
        self.centralwidget = QtGui.QWidget(fmSelectProfil_O2)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 292, 14))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.tbSelectProfil = QtGui.QToolButton(self.centralwidget)
        self.tbSelectProfil.setGeometry(QtCore.QRect(40, 210, 78, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tbSelectProfil.setFont(font)
        self.tbSelectProfil.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.tbSelectProfil.setArrowType(QtCore.Qt.NoArrow)
        self.tbSelectProfil.setObjectName(_fromUtf8("tbSelectProfil"))
        self.tbChangeProfil = QtGui.QToolButton(self.centralwidget)
        self.tbChangeProfil.setGeometry(QtCore.QRect(180, 210, 78, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tbChangeProfil.setFont(font)
        self.tbChangeProfil.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.tbChangeProfil.setArrowType(QtCore.Qt.NoArrow)
        self.tbChangeProfil.setObjectName(_fromUtf8("tbChangeProfil"))
        self.tbDelProfil = QtGui.QToolButton(self.centralwidget)
        self.tbDelProfil.setGeometry(QtCore.QRect(180, 240, 78, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tbDelProfil.setFont(font)
        self.tbDelProfil.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.tbDelProfil.setArrowType(QtCore.Qt.NoArrow)
        self.tbDelProfil.setObjectName(_fromUtf8("tbDelProfil"))
        self.tbAddProfil = QtGui.QToolButton(self.centralwidget)
        self.tbAddProfil.setGeometry(QtCore.QRect(40, 240, 78, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tbAddProfil.setFont(font)
        self.tbAddProfil.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.tbAddProfil.setArrowType(QtCore.Qt.NoArrow)
        self.tbAddProfil.setObjectName(_fromUtf8("tbAddProfil"))
        self.tbDescribeProfil = QtGui.QTextBrowser(self.centralwidget)
        self.tbDescribeProfil.setGeometry(QtCore.QRect(360, 30, 291, 171))
        self.tbDescribeProfil.setObjectName(_fromUtf8("tbDescribeProfil"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(360, 10, 292, 14))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.lwProfils_ = QtGui.QListWidget(self.centralwidget)
        self.lwProfils_.setGeometry(QtCore.QRect(20, 30, 311, 171))
        self.lwProfils_.setObjectName(_fromUtf8("lwProfils_"))
        fmSelectProfil_O2.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(fmSelectProfil_O2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 672, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        fmSelectProfil_O2.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(fmSelectProfil_O2)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        fmSelectProfil_O2.setStatusBar(self.statusbar)

        self.retranslateUi(fmSelectProfil_O2)
        QtCore.QMetaObject.connectSlotsByName(fmSelectProfil_O2)

    def retranslateUi(self, fmSelectProfil_O2):
        fmSelectProfil_O2.setWindowTitle(_translate("fmSelectProfil_O2", "Выбор профиля прибора", None))
        self.label.setText(_translate("fmSelectProfil_O2", "Профили", None))
        self.tbSelectProfil.setText(_translate("fmSelectProfil_O2", "Выбрать", None))
        self.tbChangeProfil.setText(_translate("fmSelectProfil_O2", "Изменить", None))
        self.tbDelProfil.setText(_translate("fmSelectProfil_O2", "Удалить", None))
        self.tbAddProfil.setText(_translate("fmSelectProfil_O2", "Добавить", None))
        self.label_2.setText(_translate("fmSelectProfil_O2", "Описание", None))

