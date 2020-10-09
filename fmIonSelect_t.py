# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\__2018\NB2\svi\forms\fmIonSelect.ui'
#
# Created: Wed Sep 19 10:44:43 2018
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
        fmIonSelect.resize(1190, 457)
        fmIonSelect.setMinimumSize(QtCore.QSize(1190, 457))
        fmIonSelect.setMaximumSize(QtCore.QSize(1190, 457))
        fmIonSelect.setAutoFillBackground(False)
        self.centralwidget = QtGui.QWidget(fmIonSelect)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tbSave = QtGui.QToolButton(self.centralwidget)
        self.tbSave.setGeometry(QtCore.QRect(120, 610, 361, 22))
        self.tbSave.setObjectName(_fromUtf8("tbSave"))
        self.twIonSelect = QtGui.QTableWidget(self.centralwidget)
        self.twIonSelect.setGeometry(QtCore.QRect(20, 30, 655, 300))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.twIonSelect.sizePolicy().hasHeightForWidth())
        self.twIonSelect.setSizePolicy(sizePolicy)
        self.twIonSelect.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.twIonSelect.setTextElideMode(QtCore.Qt.ElideMiddle)
        self.twIonSelect.setObjectName(_fromUtf8("twIonSelect"))
        self.twIonSelect.setColumnCount(0)
        self.twIonSelect.setRowCount(0)
        self.twIonSelect.horizontalHeader().setVisible(False)
        self.twIonSelect.horizontalHeader().setHighlightSections(False)
        self.twIonSelect.verticalHeader().setVisible(False)
        self.tbSelectIon = QtGui.QPushButton(self.centralwidget)
        self.tbSelectIon.setGeometry(QtCore.QRect(20, 370, 120, 51))
        self.tbSelectIon.setObjectName(_fromUtf8("tbSelectIon"))
        self.tbAddIon_ = QtGui.QPushButton(self.centralwidget)
        self.tbAddIon_.setGeometry(QtCore.QRect(190, 370, 120, 51))
        self.tbAddIon_.setObjectName(_fromUtf8("tbAddIon_"))
        self.tbDelIon_ = QtGui.QPushButton(self.centralwidget)
        self.tbDelIon_.setGeometry(QtCore.QRect(360, 370, 120, 51))
        self.tbDelIon_.setObjectName(_fromUtf8("tbDelIon_"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(690, 36, 481, 201))
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label_4 = QtGui.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(10, 150, 271, 20))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(10, 60, 51, 16))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(10, 100, 181, 21))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.lblKIon = QtGui.QLabel(self.groupBox)
        self.lblKIon.setGeometry(QtCore.QRect(310, 140, 151, 31))
        self.lblKIon.setObjectName(_fromUtf8("lblKIon"))
        self.lblMol_Massa = QtGui.QLabel(self.groupBox)
        self.lblMol_Massa.setGeometry(QtCore.QRect(310, 100, 151, 21))
        self.lblMol_Massa.setObjectName(_fromUtf8("lblMol_Massa"))
        self.lblIon = QtGui.QLabel(self.groupBox)
        self.lblIon.setGeometry(QtCore.QRect(310, 63, 151, 20))
        self.lblIon.setObjectName(_fromUtf8("lblIon"))
        self.tbEditIon_ = QtGui.QPushButton(self.centralwidget)
        self.tbEditIon_.setGeometry(QtCore.QRect(530, 370, 120, 51))
        self.tbEditIon_.setObjectName(_fromUtf8("tbEditIon_"))
        fmIonSelect.setCentralWidget(self.centralwidget)

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

