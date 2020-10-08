# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\ormet\source\svi_vs_v.0.4\forms\fmIonSelect.ui'
#
# Created: Mon Jan 26 17:20:41 2015
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

class Ui_fmIonSelect(object):
    def setupUi(self, fmIonSelect):
        fmIonSelect.setObjectName(_fromUtf8("fmIonSelect"))
        fmIonSelect.resize(763, 293)
        self.centralwidget = QtGui.QWidget(fmIonSelect)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tbSave = QtGui.QToolButton(self.centralwidget)
        self.tbSave.setGeometry(QtCore.QRect(120, 610, 361, 22))
        self.tbSave.setObjectName(_fromUtf8("tbSave"))
        self.twIonSelect = QtGui.QTableWidget(self.centralwidget)
        self.twIonSelect.setGeometry(QtCore.QRect(20, 0, 511, 192))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.twIonSelect.sizePolicy().hasHeightForWidth())
        self.twIonSelect.setSizePolicy(sizePolicy)
        self.twIonSelect.setObjectName(_fromUtf8("twIonSelect"))
        self.twIonSelect.setColumnCount(0)
        self.twIonSelect.setRowCount(0)
        self.tbSelectIon = QtGui.QPushButton(self.centralwidget)
        self.tbSelectIon.setGeometry(QtCore.QRect(30, 210, 75, 23))
        self.tbSelectIon.setObjectName(_fromUtf8("tbSelectIon"))
        self.tbAddIon_ = QtGui.QPushButton(self.centralwidget)
        self.tbAddIon_.setGeometry(QtCore.QRect(150, 210, 75, 23))
        self.tbAddIon_.setObjectName(_fromUtf8("tbAddIon_"))
        self.tbDelIon_ = QtGui.QPushButton(self.centralwidget)
        self.tbDelIon_.setGeometry(QtCore.QRect(270, 210, 75, 23))
        self.tbDelIon_.setObjectName(_fromUtf8("tbDelIon_"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(540, 0, 211, 111))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 70, 141, 20))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 20, 46, 13))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(10, 40, 91, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.lblKIon = QtGui.QLabel(self.groupBox)
        self.lblKIon.setGeometry(QtCore.QRect(160, 70, 41, 20))
        self.lblKIon.setObjectName(_fromUtf8("lblKIon"))
        self.lblMol_Massa = QtGui.QLabel(self.groupBox)
        self.lblMol_Massa.setGeometry(QtCore.QRect(160, 40, 41, 16))
        self.lblMol_Massa.setObjectName(_fromUtf8("lblMol_Massa"))
        self.lblIon = QtGui.QLabel(self.groupBox)
        self.lblIon.setGeometry(QtCore.QRect(160, 20, 46, 13))
        self.lblIon.setObjectName(_fromUtf8("lblIon"))
        self.tbEditIon_ = QtGui.QPushButton(self.centralwidget)
        self.tbEditIon_.setGeometry(QtCore.QRect(380, 210, 75, 23))
        self.tbEditIon_.setObjectName(_fromUtf8("tbEditIon_"))
        fmIonSelect.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(fmIonSelect)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 763, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu = QtGui.QMenu(self.menubar)
        self.menu.setObjectName(_fromUtf8("menu"))
        fmIonSelect.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(fmIonSelect)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        fmIonSelect.setStatusBar(self.statusbar)
        self.menubar.addAction(self.menu.menuAction())

        self.retranslateUi(fmIonSelect)
        QtCore.QMetaObject.connectSlotsByName(fmIonSelect)

    def retranslateUi(self, fmIonSelect):
        fmIonSelect.setWindowTitle(_translate("fmIonSelect", "Выбор иона", None))
        self.tbSave.setText(_translate("fmIonSelect", "Сохранить в энергонезависимой памяти", None))
        self.tbSelectIon.setText(_translate("fmIonSelect", "Выбрать", None))
        self.tbAddIon_.setText(_translate("fmIonSelect", "Добавить", None))
        self.tbDelIon_.setText(_translate("fmIonSelect", "Удалить", None))
        self.groupBox.setTitle(_translate("fmIonSelect", "Характеристики иона", None))
        self.label_4.setText(_translate("fmIonSelect", "Коэффициент активности", None))
        self.label_5.setText(_translate("fmIonSelect", "Ион", None))
        self.label_6.setText(_translate("fmIonSelect", "Молярная масса", None))
        self.lblKIon.setText(_translate("fmIonSelect", "-", None))
        self.lblMol_Massa.setText(_translate("fmIonSelect", "-", None))
        self.lblIon.setText(_translate("fmIonSelect", "-", None))
        self.tbEditIon_.setText(_translate("fmIonSelect", "Изменить", None))
        self.menu.setTitle(_translate("fmIonSelect", "?", None))

