# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\ormet\source\svi_meteo_19_11_2015\svi_vs_v.0.6.5\forms\fmIonMessSelect3.ui'
#
# Created: Fri Jul  1 16:23:30 2016
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
        fmIonMessSelect.resize(270, 195)
        fmIonMessSelect.setMinimumSize(QtCore.QSize(270, 195))
        fmIonMessSelect.setMaximumSize(QtCore.QSize(270, 195))
        self.centralwidget = QtGui.QWidget(fmIonMessSelect)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tbSave = QtGui.QToolButton(self.centralwidget)
        self.tbSave.setGeometry(QtCore.QRect(120, 610, 361, 22))
        self.tbSave.setObjectName(_fromUtf8("tbSave"))
        self.tbSelectKolIzm = QtGui.QPushButton(self.centralwidget)
        self.tbSelectKolIzm.setGeometry(QtCore.QRect(170, 80, 75, 23))
        self.tbSelectKolIzm.setObjectName(_fromUtf8("tbSelectKolIzm"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(19, 85, 71, 16))
        self.label.setObjectName(_fromUtf8("label"))
        self.tbSelectKolIon_1 = QtGui.QPushButton(self.centralwidget)
        self.tbSelectKolIon_1.setGeometry(QtCore.QRect(20, 26, 41, 41))
        self.tbSelectKolIon_1.setObjectName(_fromUtf8("tbSelectKolIon_1"))
        self.tbSelectKolIon_2 = QtGui.QPushButton(self.centralwidget)
        self.tbSelectKolIon_2.setGeometry(QtCore.QRect(80, 26, 41, 41))
        self.tbSelectKolIon_2.setObjectName(_fromUtf8("tbSelectKolIon_2"))
        self.tbSelectKolIon_3 = QtGui.QPushButton(self.centralwidget)
        self.tbSelectKolIon_3.setGeometry(QtCore.QRect(140, 26, 41, 41))
        self.tbSelectKolIon_3.setObjectName(_fromUtf8("tbSelectKolIon_3"))
        self.tbSelectKolIon_4 = QtGui.QPushButton(self.centralwidget)
        self.tbSelectKolIon_4.setGeometry(QtCore.QRect(200, 26, 41, 41))
        self.tbSelectKolIon_4.setObjectName(_fromUtf8("tbSelectKolIon_4"))
        self.chbAutoIzm = QtGui.QCheckBox(self.centralwidget)
        self.chbAutoIzm.setGeometry(QtCore.QRect(20, 120, 241, 21))
        self.chbAutoIzm.setObjectName(_fromUtf8("chbAutoIzm"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(16, 3, 231, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.spinBox = QtGui.QLineEdit(self.centralwidget)
        self.spinBox.setGeometry(QtCore.QRect(100, 80, 61, 20))
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        fmIonMessSelect.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(fmIonMessSelect)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 270, 21))
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
        self.label.setText(_translate("fmIonMessSelect", "Другое", None))
        self.tbSelectKolIon_1.setText(_translate("fmIonMessSelect", "1", None))
        self.tbSelectKolIon_2.setText(_translate("fmIonMessSelect", "2", None))
        self.tbSelectKolIon_3.setText(_translate("fmIonMessSelect", "3", None))
        self.tbSelectKolIon_4.setText(_translate("fmIonMessSelect", "4", None))
        self.chbAutoIzm.setText(_translate("fmIonMessSelect", "Авт. измерение напряжения", None))
        self.label_2.setText(_translate("fmIonMessSelect", "Количество измерений", None))
        self.menu.setTitle(_translate("fmIonMessSelect", "?", None))

