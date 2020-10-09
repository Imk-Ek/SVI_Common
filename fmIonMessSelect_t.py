# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\ormet\source\svi (4)\svi\forms\fmIonMessSelect.ui'
#
# Created: Mon Sep 17 14:00:33 2018
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

class Ui_fmIonMessSelect(object):
    def setupUi(self, fmIonMessSelect):
        fmIonMessSelect.setObjectName(_fromUtf8("fmIonMessSelect"))
        fmIonMessSelect.resize(508, 352)
        fmIonMessSelect.setMinimumSize(QtCore.QSize(508, 309))
        fmIonMessSelect.setMaximumSize(QtCore.QSize(5080, 3090))
        self.centralwidget = QtGui.QWidget(fmIonMessSelect)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tbSave = QtGui.QToolButton(self.centralwidget)
        self.tbSave.setGeometry(QtCore.QRect(120, 610, 361, 22))
        self.tbSave.setObjectName(_fromUtf8("tbSave"))
        self.tbSelectKolIzm = QtGui.QPushButton(self.centralwidget)
        self.tbSelectKolIzm.setGeometry(QtCore.QRect(320, 150, 121, 51))
        self.tbSelectKolIzm.setObjectName(_fromUtf8("tbSelectKolIzm"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 150, 151, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.tbSelectKolIon_1 = QtGui.QPushButton(self.centralwidget)
        self.tbSelectKolIon_1.setGeometry(QtCore.QRect(70, 51, 51, 51))
        self.tbSelectKolIon_1.setObjectName(_fromUtf8("tbSelectKolIon_1"))
        self.tbSelectKolIon_2 = QtGui.QPushButton(self.centralwidget)
        self.tbSelectKolIon_2.setGeometry(QtCore.QRect(170, 51, 51, 51))
        self.tbSelectKolIon_2.setObjectName(_fromUtf8("tbSelectKolIon_2"))
        self.tbSelectKolIon_3 = QtGui.QPushButton(self.centralwidget)
        self.tbSelectKolIon_3.setGeometry(QtCore.QRect(270, 51, 51, 51))
        self.tbSelectKolIon_3.setObjectName(_fromUtf8("tbSelectKolIon_3"))
        self.tbSelectKolIon_4 = QtGui.QPushButton(self.centralwidget)
        self.tbSelectKolIon_4.setGeometry(QtCore.QRect(370, 51, 51, 51))
        self.tbSelectKolIon_4.setObjectName(_fromUtf8("tbSelectKolIon_4"))
        self.chbAutoIzm = QtGui.QCheckBox(self.centralwidget)
        self.chbAutoIzm.setGeometry(QtCore.QRect(20, 230, 481, 41))
        self.chbAutoIzm.setObjectName(_fromUtf8("chbAutoIzm"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(16, 3, 261, 31))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.leKu_ = QtGui.QLineEdit(self.centralwidget)
        self.leKu_.setGeometry(QtCore.QRect(180, 150, 91, 41))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.leKu_.setFont(font)
        self.leKu_.setObjectName(_fromUtf8("leKu_"))
        fmIonMessSelect.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(fmIonMessSelect)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 508, 38))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu = QtGui.QMenu(self.menubar)
        self.menu.setObjectName(_fromUtf8("menu"))
        fmIonMessSelect.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(fmIonMessSelect)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        fmIonMessSelect.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(fmIonMessSelect)
        QtCore.QMetaObject.connectSlotsByName(fmIonMessSelect)

    def retranslateUi(self, fmIonMessSelect):
        fmIonMessSelect.setWindowTitle(_translate("fmIonMessSelect", "Выбор параметров измерения", None))
        self.tbSave.setText(_translate("fmIonMessSelect", "Сохранить в энергонезависимой памяти", None))
        self.tbSelectKolIzm.setText(_translate("fmIonMessSelect", "Выбрать", None))
        self.label.setText(_translate("fmIonMessSelect", "Другое число", None))
        self.tbSelectKolIon_1.setText(_translate("fmIonMessSelect", "1", None))
        self.tbSelectKolIon_2.setText(_translate("fmIonMessSelect", "2", None))
        self.tbSelectKolIon_3.setText(_translate("fmIonMessSelect", "3", None))
        self.tbSelectKolIon_4.setText(_translate("fmIonMessSelect", "4", None))
        self.chbAutoIzm.setText(_translate("fmIonMessSelect", "Автоматическое измерение напряжения", None))
        self.label_2.setText(_translate("fmIonMessSelect", "Количество измерений", None))
        self.menu.setTitle(_translate("fmIonMessSelect", "?", None))

