# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\ormet\source\svi (4)\svi\forms\fmTKR.ui'
#
# Created: Mon Sep 17 13:55:46 2018
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

class Ui_fmTKR(object):
    def setupUi(self, fmTKR):
        fmTKR.setObjectName(_fromUtf8("fmTKR"))
        fmTKR.resize(451, 418)
        fmTKR.setMinimumSize(QtCore.QSize(451, 418))
        fmTKR.setMaximumSize(QtCore.QSize(451, 418))
        fmTKR.setWindowOpacity(1.0)
        self.centralwidget = QtGui.QWidget(fmTKR)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.lblCond_ed = QtGui.QLabel(self.centralwidget)
        self.lblCond_ed.setGeometry(QtCore.QRect(540, 70, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblCond_ed.setFont(font)
        self.lblCond_ed.setText(_fromUtf8(""))
        self.lblCond_ed.setObjectName(_fromUtf8("lblCond_ed"))
        self.leAet_6 = QtGui.QLineEdit(self.centralwidget)
        self.leAet_6.setGeometry(QtCore.QRect(630, 840, 81, 22))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.leAet_6.setFont(font)
        self.leAet_6.setObjectName(_fromUtf8("leAet_6"))
        self.label_29 = QtGui.QLabel(self.centralwidget)
        self.label_29.setGeometry(QtCore.QRect(590, 840, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_29.setFont(font)
        self.label_29.setLineWidth(-5)
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(250, 280, 41, 31))
        self.label_4.setMinimumSize(QtCore.QSize(18, 18))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.leTemp = QtGui.QLineEdit(self.centralwidget)
        self.leTemp.setGeometry(QtCore.QRect(154, 280, 91, 41))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leTemp.sizePolicy().hasHeightForWidth())
        self.leTemp.setSizePolicy(sizePolicy)
        self.leTemp.setMinimumSize(QtCore.QSize(6, 24))
        self.leTemp.setMaximumSize(QtCore.QSize(610, 310))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(12)
        self.leTemp.setFont(font)
        self.leTemp.setFrame(True)
        self.leTemp.setObjectName(_fromUtf8("leTemp"))
        self.label_10 = QtGui.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(60, 230, 311, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.groupBox_4 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(0, 10, 301, 201))
        self.groupBox_4.setMinimumSize(QtCore.QSize(2, 105))
        self.groupBox_4.setFlat(False)
        self.groupBox_4.setCheckable(False)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.rb_R = QtGui.QRadioButton(self.groupBox_4)
        self.rb_R.setGeometry(QtCore.QRect(10, 140, 201, 41))
        self.rb_R.setMinimumSize(QtCore.QSize(107, 17))
        self.rb_R.setObjectName(_fromUtf8("rb_R"))
        self.rb_25 = QtGui.QRadioButton(self.groupBox_4)
        self.rb_25.setGeometry(QtCore.QRect(10, 30, 281, 41))
        self.rb_25.setMinimumSize(QtCore.QSize(87, 17))
        self.rb_25.setObjectName(_fromUtf8("rb_25"))
        self.rb_20 = QtGui.QRadioButton(self.groupBox_4)
        self.rb_20.setGeometry(QtCore.QRect(10, 82, 281, 41))
        self.rb_20.setMinimumSize(QtCore.QSize(82, 17))
        self.rb_20.setObjectName(_fromUtf8("rb_20"))
        self.tbSave = QtGui.QToolButton(self.centralwidget)
        self.tbSave.setGeometry(QtCore.QRect(140, 350, 141, 51))
        self.tbSave.setObjectName(_fromUtf8("tbSave"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(310, 150, 41, 41))
        self.label_3.setMinimumSize(QtCore.QSize(18, 18))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.leTemp_R = QtGui.QLineEdit(self.centralwidget)
        self.leTemp_R.setGeometry(QtCore.QRect(210, 150, 81, 41))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leTemp_R.sizePolicy().hasHeightForWidth())
        self.leTemp_R.setSizePolicy(sizePolicy)
        self.leTemp_R.setMinimumSize(QtCore.QSize(6, 24))
        self.leTemp_R.setMaximumSize(QtCore.QSize(610, 310))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(12)
        self.leTemp_R.setFont(font)
        self.leTemp_R.setFrame(True)
        self.leTemp_R.setObjectName(_fromUtf8("leTemp_R"))
        fmTKR.setCentralWidget(self.centralwidget)
        self.actTIns = QtGui.QAction(fmTKR)
        self.actTIns.setObjectName(_fromUtf8("actTIns"))
        self.actTDel = QtGui.QAction(fmTKR)
        self.actTDel.setObjectName(_fromUtf8("actTDel"))
        self.actPrIns = QtGui.QAction(fmTKR)
        self.actPrIns.setObjectName(_fromUtf8("actPrIns"))
        self.actPrDel = QtGui.QAction(fmTKR)
        self.actPrDel.setObjectName(_fromUtf8("actPrDel"))
        self.actPrRen = QtGui.QAction(fmTKR)
        self.actPrRen.setObjectName(_fromUtf8("actPrRen"))

        self.retranslateUi(fmTKR)
        QtCore.QMetaObject.connectSlotsByName(fmTKR)

    def retranslateUi(self, fmTKR):
        fmTKR.setWindowTitle(_translate("fmTKR", "Тип АТК", None))
        self.label_29.setText(_translate("fmTKR", "Кд 6", None))
        self.label_4.setText(_translate("fmTKR", "<sup>o</sup>С", None))
        self.leTemp.setText(_translate("fmTKR", "25.0", None))
        self.label_10.setText(_translate("fmTKR", "Температура градуировки", None))
        self.groupBox_4.setTitle(_translate("fmTKR", "Тип АТК", None))
        self.rb_R.setText(_translate("fmTKR", "Приведенная к", None))
        self.rb_25.setText(_translate("fmTKR", "Приведенная к 25  оС", None))
        self.rb_20.setText(_translate("fmTKR", "Приведенная к 20  оС", None))
        self.tbSave.setText(_translate("fmTKR", "Сохранить", None))
        self.label_3.setText(_translate("fmTKR", "<sup>o</sup>С", None))
        self.leTemp_R.setText(_translate("fmTKR", "24.0", None))
        self.actTIns.setText(_translate("fmTKR", "Вставить строку", None))
        self.actTDel.setText(_translate("fmTKR", "Удалить строку", None))
        self.actPrIns.setText(_translate("fmTKR", "Новый профиль", None))
        self.actPrDel.setText(_translate("fmTKR", "Удалить профиль", None))
        self.actPrRen.setText(_translate("fmTKR", "Переименовать профиль", None))

