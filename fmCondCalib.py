# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\ormet\source\svi_vs_v.0.3\forms\fmCondCalib.ui'
#
# Created: Wed May 21 17:57:49 2014
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

class Ui_fmCondCalib(object):
    def setupUi(self, fmCondCalib):
        fmCondCalib.setObjectName(_fromUtf8("fmCondCalib"))
        fmCondCalib.resize(403, 208)
        self.centralwidget = QtGui.QWidget(fmCondCalib)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tbCalib = QtGui.QToolButton(self.centralwidget)
        self.tbCalib.setGeometry(QtCore.QRect(20, 62, 341, 22))
        self.tbCalib.setObjectName(_fromUtf8("tbCalib"))
        self.tbElecAdd = QtGui.QToolButton(self.centralwidget)
        self.tbElecAdd.setGeometry(QtCore.QRect(340, 122, 27, 22))
        self.tbElecAdd.setObjectName(_fromUtf8("tbElecAdd"))
        self.cbElec = QtGui.QComboBox(self.centralwidget)
        self.cbElec.setGeometry(QtCore.QRect(18, 128, 311, 22))
        self.cbElec.setObjectName(_fromUtf8("cbElec"))
        self.leElec = QtGui.QLineEdit(self.centralwidget)
        self.leElec.setEnabled(False)
        self.leElec.setGeometry(QtCore.QRect(20, 122, 311, 22))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.leElec.setFont(font)
        self.leElec.setObjectName(_fromUtf8("leElec"))
        self.label_31 = QtGui.QLabel(self.centralwidget)
        self.label_31.setGeometry(QtCore.QRect(20, 94, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_31.setFont(font)
        self.label_31.setLineWidth(-5)
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.label_28 = QtGui.QLabel(self.centralwidget)
        self.label_28.setGeometry(QtCore.QRect(26, 12, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_28.setFont(font)
        self.label_28.setLineWidth(-5)
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.leKu = QtGui.QDoubleSpinBox(self.centralwidget)
        self.leKu.setGeometry(QtCore.QRect(60, 10, 91, 21))
        self.leKu.setSingleStep(0.01)
        self.leKu.setObjectName(_fromUtf8("leKu"))
        fmCondCalib.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(fmCondCalib)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 403, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.muProf = QtGui.QMenu(self.menubar)
        self.muProf.setObjectName(_fromUtf8("muProf"))
        self.muTabl = QtGui.QMenu(self.menubar)
        self.muTabl.setObjectName(_fromUtf8("muTabl"))
        fmCondCalib.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(fmCondCalib)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        fmCondCalib.setStatusBar(self.statusbar)
        self.actTIns = QtGui.QAction(fmCondCalib)
        self.actTIns.setObjectName(_fromUtf8("actTIns"))
        self.actTDel = QtGui.QAction(fmCondCalib)
        self.actTDel.setObjectName(_fromUtf8("actTDel"))
        self.actPrIns = QtGui.QAction(fmCondCalib)
        self.actPrIns.setObjectName(_fromUtf8("actPrIns"))
        self.actPrDel = QtGui.QAction(fmCondCalib)
        self.actPrDel.setObjectName(_fromUtf8("actPrDel"))
        self.actPrRen = QtGui.QAction(fmCondCalib)
        self.actPrRen.setObjectName(_fromUtf8("actPrRen"))
        self.menubar.addAction(self.muProf.menuAction())
        self.menubar.addAction(self.muTabl.menuAction())

        self.retranslateUi(fmCondCalib)
        QtCore.QMetaObject.connectSlotsByName(fmCondCalib)

    def retranslateUi(self, fmCondCalib):
        fmCondCalib.setWindowTitle(_translate("fmCondCalib", "Градуировка", None))
        self.tbCalib.setText(_translate("fmCondCalib", "Сохранить", None))
        self.tbElecAdd.setText(_translate("fmCondCalib", "+", None))
        self.label_31.setText(_translate("fmCondCalib", "Профиль измерения", None))
        self.label_28.setText(_translate("fmCondCalib", "К<sub>яч</sub>=", None))
        self.muProf.setTitle(_translate("fmCondCalib", "Профиль", None))
        self.muTabl.setTitle(_translate("fmCondCalib", "Таблица", None))
        self.actTIns.setText(_translate("fmCondCalib", "Вставить строку", None))
        self.actTDel.setText(_translate("fmCondCalib", "Удалить строку", None))
        self.actPrIns.setText(_translate("fmCondCalib", "Новый профиль", None))
        self.actPrDel.setText(_translate("fmCondCalib", "Удалить профиль", None))
        self.actPrRen.setText(_translate("fmCondCalib", "Переименовать профиль", None))

