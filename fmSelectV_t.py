# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\ormet\source\svi (4)\svi\forms\fmSelectV.ui'
#
# Created: Mon Sep 17 13:55:27 2018
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

class Ui_fmSelectV(object):
    def setupUi(self, fmSelectV):
        fmSelectV.setObjectName(_fromUtf8("fmSelectV"))
        fmSelectV.resize(615, 566)
        fmSelectV.setMinimumSize(QtCore.QSize(615, 566))
        fmSelectV.setMaximumSize(QtCore.QSize(615, 566))
        fmSelectV.setWindowOpacity(1.0)
        self.centralwidget = QtGui.QWidget(fmSelectV)
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
        self.lwV = QtGui.QListWidget(self.centralwidget)
        self.lwV.setGeometry(QtCore.QRect(20, 50, 571, 161))
        self.lwV.setObjectName(_fromUtf8("lwV"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 511, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(20, 300, 571, 241))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.label_11 = QtGui.QLabel(self.groupBox_3)
        self.label_11.setGeometry(QtCore.QRect(10, 90, 281, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_11.setFont(font)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.label_10 = QtGui.QLabel(self.groupBox_3)
        self.label_10.setGeometry(QtCore.QRect(10, 30, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.tbAdd = QtGui.QToolButton(self.groupBox_3)
        self.tbAdd.setGeometry(QtCore.QRect(40, 180, 125, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tbAdd.setFont(font)
        self.tbAdd.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.tbAdd.setArrowType(QtCore.Qt.NoArrow)
        self.tbAdd.setObjectName(_fromUtf8("tbAdd"))
        self.tbChange = QtGui.QToolButton(self.groupBox_3)
        self.tbChange.setGeometry(QtCore.QRect(220, 180, 125, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tbChange.setFont(font)
        self.tbChange.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.tbChange.setArrowType(QtCore.Qt.NoArrow)
        self.tbChange.setObjectName(_fromUtf8("tbChange"))
        self.leV_Name = QtGui.QLineEdit(self.groupBox_3)
        self.leV_Name.setGeometry(QtCore.QRect(320, 30, 101, 41))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leV_Name.sizePolicy().hasHeightForWidth())
        self.leV_Name.setSizePolicy(sizePolicy)
        self.leV_Name.setMinimumSize(QtCore.QSize(6, 24))
        self.leV_Name.setMaximumSize(QtCore.QSize(910, 310))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(12)
        self.leV_Name.setFont(font)
        self.leV_Name.setFrame(True)
        self.leV_Name.setObjectName(_fromUtf8("leV_Name"))
        self.leTKR = QtGui.QLineEdit(self.groupBox_3)
        self.leTKR.setGeometry(QtCore.QRect(320, 100, 101, 41))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leTKR.sizePolicy().hasHeightForWidth())
        self.leTKR.setSizePolicy(sizePolicy)
        self.leTKR.setMinimumSize(QtCore.QSize(6, 24))
        self.leTKR.setMaximumSize(QtCore.QSize(910, 310))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(12)
        self.leTKR.setFont(font)
        self.leTKR.setFrame(True)
        self.leTKR.setObjectName(_fromUtf8("leTKR"))
        self.tbDel = QtGui.QToolButton(self.groupBox_3)
        self.tbDel.setGeometry(QtCore.QRect(400, 180, 125, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tbDel.setFont(font)
        self.tbDel.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.tbDel.setArrowType(QtCore.Qt.NoArrow)
        self.tbDel.setObjectName(_fromUtf8("tbDel"))
        self.label_12 = QtGui.QLabel(self.groupBox_3)
        self.label_12.setGeometry(QtCore.QRect(20, 120, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_12.setFont(font)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.tbSelect = QtGui.QToolButton(self.centralwidget)
        self.tbSelect.setGeometry(QtCore.QRect(20, 230, 125, 51))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tbSelect.setFont(font)
        self.tbSelect.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.tbSelect.setArrowType(QtCore.Qt.NoArrow)
        self.tbSelect.setObjectName(_fromUtf8("tbSelect"))
        fmSelectV.setCentralWidget(self.centralwidget)
        self.actTIns = QtGui.QAction(fmSelectV)
        self.actTIns.setObjectName(_fromUtf8("actTIns"))
        self.actTDel = QtGui.QAction(fmSelectV)
        self.actTDel.setObjectName(_fromUtf8("actTDel"))
        self.actPrIns = QtGui.QAction(fmSelectV)
        self.actPrIns.setObjectName(_fromUtf8("actPrIns"))
        self.actPrDel = QtGui.QAction(fmSelectV)
        self.actPrDel.setObjectName(_fromUtf8("actPrDel"))
        self.actPrRen = QtGui.QAction(fmSelectV)
        self.actPrRen.setObjectName(_fromUtf8("actPrRen"))

        self.retranslateUi(fmSelectV)
        QtCore.QMetaObject.connectSlotsByName(fmSelectV)

    def retranslateUi(self, fmSelectV):
        fmSelectV.setWindowTitle(_translate("fmSelectV", "Выбор вещества", None))
        self.label_29.setText(_translate("fmSelectV", "Кд 6", None))
        self.label.setText(_translate("fmSelectV", "Таблица коэффициентов проводимости", None))
        self.groupBox_3.setTitle(_translate("fmSelectV", "Изменить", None))
        self.label_11.setText(_translate("fmSelectV", "Температурный. коэфф.", None))
        self.label_10.setText(_translate("fmSelectV", "Наименование. вещества", None))
        self.tbAdd.setText(_translate("fmSelectV", "Добавить", None))
        self.tbChange.setText(_translate("fmSelectV", "Изменить", None))
        self.leV_Name.setText(_translate("fmSelectV", "12", None))
        self.leTKR.setText(_translate("fmSelectV", "12", None))
        self.tbDel.setText(_translate("fmSelectV", "Удалить", None))
        self.label_12.setText(_translate("fmSelectV", "проводимости, %", None))
        self.tbSelect.setText(_translate("fmSelectV", "Выбрать", None))
        self.actTIns.setText(_translate("fmSelectV", "Вставить строку", None))
        self.actTDel.setText(_translate("fmSelectV", "Удалить строку", None))
        self.actPrIns.setText(_translate("fmSelectV", "Новый профиль", None))
        self.actPrDel.setText(_translate("fmSelectV", "Удалить профиль", None))
        self.actPrRen.setText(_translate("fmSelectV", "Переименовать профиль", None))

