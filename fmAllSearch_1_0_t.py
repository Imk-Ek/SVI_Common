# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\ormet\source\svi_vs_v.0.4\forms\fmAllSearch_1_0.ui'
#
# Created: Tue Nov 18 10:03:34 2014
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

class Ui_fmAllSearch_1_0(object):
    def setupUi(self, fmAllSearch_1_0):
        fmAllSearch_1_0.setObjectName(_fromUtf8("fmAllSearch_1_0"))
        fmAllSearch_1_0.resize(718, 487)
        self.centralwidget = QtGui.QWidget(fmAllSearch_1_0)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.twSearch = QtGui.QTableWidget(self.centralwidget)
        self.twSearch.setGeometry(QtCore.QRect(20, 40, 671, 331))
        self.twSearch.setObjectName(_fromUtf8("twSearch"))
        self.twSearch.setColumnCount(0)
        self.twSearch.setRowCount(0)
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(40, 10, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.tbSearchModuls = QtGui.QToolButton(self.centralwidget)
        self.tbSearchModuls.setGeometry(QtCore.QRect(230, 390, 141, 22))
        self.tbSearchModuls.setObjectName(_fromUtf8("tbSearchModuls"))
        fmAllSearch_1_0.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(fmAllSearch_1_0)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 718, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        fmAllSearch_1_0.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(fmAllSearch_1_0)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        fmAllSearch_1_0.setStatusBar(self.statusbar)

        self.retranslateUi(fmAllSearch_1_0)
        QtCore.QMetaObject.connectSlotsByName(fmAllSearch_1_0)

    def retranslateUi(self, fmAllSearch_1_0):
        fmAllSearch_1_0.setWindowTitle(_translate("fmAllSearch_1_0", "Поиск модулей", None))
        self.label_9.setText(_translate("fmAllSearch_1_0", "Список модулей", None))
        self.tbSearchModuls.setText(_translate("fmAllSearch_1_0", "Поиск", None))

