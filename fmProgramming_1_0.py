# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\ormet\source\svi_vs_v.0.4\forms\fmProgramming_1_0.ui'
#
# Created: Fri Nov 14 11:09:27 2014
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

class Ui_fmProgramming_1_0(object):
    def setupUi(self, fmProgramming_1_0):
        fmProgramming_1_0.setObjectName(_fromUtf8("fmProgramming_1_0"))
        fmProgramming_1_0.resize(701, 447)
        self.centralwidget = QtGui.QWidget(fmProgramming_1_0)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label_31 = QtGui.QLabel(self.centralwidget)
        self.label_31.setGeometry(QtCore.QRect(10, 10, 121, 21))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_31.sizePolicy().hasHeightForWidth())
        self.label_31.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_31.setFont(font)
        self.label_31.setLineWidth(-5)
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(400, 10, 141, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.label_29 = QtGui.QLabel(self.centralwidget)
        self.label_29.setGeometry(QtCore.QRect(590, 840, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_29.setFont(font)
        self.label_29.setLineWidth(-5)
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.cbSNum = QtGui.QComboBox(self.centralwidget)
        self.cbSNum.setGeometry(QtCore.QRect(10, 40, 201, 22))
        self.cbSNum.setEditable(False)
        self.cbSNum.setObjectName(_fromUtf8("cbSNum"))
        self.cbTypeAnalog = QtGui.QComboBox(self.centralwidget)
        self.cbTypeAnalog.setGeometry(QtCore.QRect(10, 100, 201, 22))
        self.cbTypeAnalog.setEditable(False)
        self.cbTypeAnalog.setObjectName(_fromUtf8("cbTypeAnalog"))
        self.label_41 = QtGui.QLabel(self.centralwidget)
        self.label_41.setGeometry(QtCore.QRect(10, 70, 171, 21))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_41.sizePolicy().hasHeightForWidth())
        self.label_41.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_41.setFont(font)
        self.label_41.setLineWidth(-5)
        self.label_41.setObjectName(_fromUtf8("label_41"))
        self.twDBNum = QtGui.QTableWidget(self.centralwidget)
        self.twDBNum.setGeometry(QtCore.QRect(230, 40, 461, 311))
        self.twDBNum.setObjectName(_fromUtf8("twDBNum"))
        self.twDBNum.setColumnCount(0)
        self.twDBNum.setRowCount(0)
        self.label_42 = QtGui.QLabel(self.centralwidget)
        self.label_42.setGeometry(QtCore.QRect(20, 160, 51, 21))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_42.sizePolicy().hasHeightForWidth())
        self.label_42.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_42.setFont(font)
        self.label_42.setLineWidth(-5)
        self.label_42.setObjectName(_fromUtf8("label_42"))
        self.label_43 = QtGui.QLabel(self.centralwidget)
        self.label_43.setGeometry(QtCore.QRect(20, 230, 71, 21))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_43.sizePolicy().hasHeightForWidth())
        self.label_43.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_43.setFont(font)
        self.label_43.setLineWidth(-5)
        self.label_43.setObjectName(_fromUtf8("label_43"))
        self.leDate = QtGui.QLineEdit(self.centralwidget)
        self.leDate.setGeometry(QtCore.QRect(10, 190, 171, 22))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.leDate.setFont(font)
        self.leDate.setObjectName(_fromUtf8("leDate"))
        self.leVersion = QtGui.QLineEdit(self.centralwidget)
        self.leVersion.setGeometry(QtCore.QRect(10, 260, 171, 22))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.leVersion.setFont(font)
        self.leVersion.setObjectName(_fromUtf8("leVersion"))
        self.tbDelDBNum = QtGui.QToolButton(self.centralwidget)
        self.tbDelDBNum.setGeometry(QtCore.QRect(230, 370, 141, 22))
        self.tbDelDBNum.setObjectName(_fromUtf8("tbDelDBNum"))
        self.tbAddDBNum = QtGui.QToolButton(self.centralwidget)
        self.tbAddDBNum.setGeometry(QtCore.QRect(380, 370, 141, 22))
        self.tbAddDBNum.setObjectName(_fromUtf8("tbAddDBNum"))
        self.tbSaveDBNum = QtGui.QToolButton(self.centralwidget)
        self.tbSaveDBNum.setGeometry(QtCore.QRect(530, 370, 141, 22))
        self.tbSaveDBNum.setObjectName(_fromUtf8("tbSaveDBNum"))
        self.tbSaveEeprom = QtGui.QPushButton(self.centralwidget)
        self.tbSaveEeprom.setGeometry(QtCore.QRect(10, 300, 211, 23))
        self.tbSaveEeprom.setObjectName(_fromUtf8("tbSaveEeprom"))
        fmProgramming_1_0.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(fmProgramming_1_0)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        fmProgramming_1_0.setStatusBar(self.statusbar)
        self.actTIns = QtGui.QAction(fmProgramming_1_0)
        self.actTIns.setObjectName(_fromUtf8("actTIns"))
        self.actTDel = QtGui.QAction(fmProgramming_1_0)
        self.actTDel.setObjectName(_fromUtf8("actTDel"))
        self.actPrIns = QtGui.QAction(fmProgramming_1_0)
        self.actPrIns.setObjectName(_fromUtf8("actPrIns"))
        self.actPrDel = QtGui.QAction(fmProgramming_1_0)
        self.actPrDel.setObjectName(_fromUtf8("actPrDel"))
        self.actPrRen = QtGui.QAction(fmProgramming_1_0)
        self.actPrRen.setObjectName(_fromUtf8("actPrRen"))

        self.retranslateUi(fmProgramming_1_0)
        self.cbSNum.setCurrentIndex(-1)
        self.cbTypeAnalog.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(fmProgramming_1_0)

    def retranslateUi(self, fmProgramming_1_0):
        fmProgramming_1_0.setWindowTitle(_translate("fmProgramming_1_0", "Программирование адреса устройств", None))
        self.label_31.setText(_translate("fmProgramming_1_0", "Заводской номер", None))
        self.label_9.setText(_translate("fmProgramming_1_0", "База номеров приборов", None))
        self.label_29.setText(_translate("fmProgramming_1_0", "Кд 6", None))
        self.label_41.setText(_translate("fmProgramming_1_0", "Тип аналогового устройства", None))
        self.label_42.setText(_translate("fmProgramming_1_0", "Дата", None))
        self.label_43.setText(_translate("fmProgramming_1_0", "Версия ПО", None))
        self.leDate.setText(_translate("fmProgramming_1_0", "0", None))
        self.leVersion.setText(_translate("fmProgramming_1_0", "0", None))
        self.tbDelDBNum.setText(_translate("fmProgramming_1_0", "Удалить запись", None))
        self.tbAddDBNum.setText(_translate("fmProgramming_1_0", "Добавить запись", None))
        self.tbSaveDBNum.setText(_translate("fmProgramming_1_0", "Сохранить запись", None))
        self.tbSaveEeprom.setText(_translate("fmProgramming_1_0", "Запмсь в EEPROM", None))
        self.actTIns.setText(_translate("fmProgramming_1_0", "Вставить строку", None))
        self.actTDel.setText(_translate("fmProgramming_1_0", "Удалить строку", None))
        self.actPrIns.setText(_translate("fmProgramming_1_0", "Новый профиль", None))
        self.actPrDel.setText(_translate("fmProgramming_1_0", "Удалить профиль", None))
        self.actPrRen.setText(_translate("fmProgramming_1_0", "Переименовать профиль", None))

