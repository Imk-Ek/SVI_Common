# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\__2018\NB2\svi\forms\fpVATP.ui'
#
# Created: Thu Oct 18 11:05:03 2018
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

class Ui_fpVATP(object):
    def setupUi(self, fpVATP):
        fpVATP.setObjectName(_fromUtf8("fpVATP"))
        fpVATP.resize(456, 306)
        fpVATP.setMinimumSize(QtCore.QSize(456, 306))
        fpVATP.setMaximumSize(QtCore.QSize(456, 306))
        self.centralwidget = QtGui.QWidget(fpVATP)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.lcdMain = QtGui.QLCDNumber(self.centralwidget)
        self.lcdMain.setGeometry(QtCore.QRect(10, 60, 261, 91))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdMain.sizePolicy().hasHeightForWidth())
        self.lcdMain.setSizePolicy(sizePolicy)
        self.lcdMain.setMinimumSize(QtCore.QSize(151, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.lcdMain.setPalette(palette)
        self.lcdMain.setSmallDecimalPoint(True)
        self.lcdMain.setNumDigits(5)
        self.lcdMain.setDigitCount(5)
        self.lcdMain.setProperty("value", -123.0)
        self.lcdMain.setProperty("intValue", -123)
        self.lcdMain.setObjectName(_fromUtf8("lcdMain"))
        self.lblEd = QtGui.QLabel(self.centralwidget)
        self.lblEd.setGeometry(QtCore.QRect(290, 70, 141, 71))
        self.lblEd.setMinimumSize(QtCore.QSize(141, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.lblEd.setFont(font)
        self.lblEd.setObjectName(_fromUtf8("lblEd"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(130, 7, 121, 41))
        self.label_5.setMinimumSize(QtCore.QSize(19, 18))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.lblID = QtGui.QLabel(self.centralwidget)
        self.lblID.setGeometry(QtCore.QRect(260, 10, 181, 41))
        self.lblID.setMinimumSize(QtCore.QSize(19, 18))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(12)
        self.lblID.setFont(font)
        self.lblID.setObjectName(_fromUtf8("lblID"))
        self.tbSaveToNotepad_ = QtGui.QToolButton(self.centralwidget)
        self.tbSaveToNotepad_.setGeometry(QtCore.QRect(180, 200, 251, 51))
        self.tbSaveToNotepad_.setMinimumSize(QtCore.QSize(71, 31))
        self.tbSaveToNotepad_.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tbSaveToNotepad_.setObjectName(_fromUtf8("tbSaveToNotepad_"))
        fpVATP.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(fpVATP)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 456, 38))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        fpVATP.setMenuBar(self.menubar)
        self.actConf = QtGui.QAction(fpVATP)
        self.actConf.setObjectName(_fromUtf8("actConf"))
        self.action = QtGui.QAction(fpVATP)
        self.action.setObjectName(_fromUtf8("action"))
        self.action_2 = QtGui.QAction(fpVATP)
        self.action_2.setObjectName(_fromUtf8("action_2"))
        self.action_3 = QtGui.QAction(fpVATP)
        self.action_3.setObjectName(_fromUtf8("action_3"))
        self.action_4 = QtGui.QAction(fpVATP)
        self.action_4.setObjectName(_fromUtf8("action_4"))
        self.action_5 = QtGui.QAction(fpVATP)
        self.action_5.setObjectName(_fromUtf8("action_5"))

        self.retranslateUi(fpVATP)
        QtCore.QMetaObject.connectSlotsByName(fpVATP)

    def retranslateUi(self, fpVATP):
        fpVATP.setWindowTitle(_translate("fpVATP", "Кондуктометр", None))
        self.lblEd.setText(_translate("fpVATP", "<html><head/><body><p>мкA</p></body></html>", None))
        self.label_5.setText(_translate("fpVATP", "Проба", None))
        self.lblID.setText(_translate("fpVATP", "ID", None))
        self.tbSaveToNotepad_.setText(_translate("fpVATP", "Записать в блокнот", None))
        self.actConf.setText(_translate("fpVATP", "Градуировка", None))
        self.action.setText(_translate("fpVATP", "Градуировка", None))
        self.action_2.setText(_translate("fpVATP", "Сохранить профиль", None))
        self.action_3.setText(_translate("fpVATP", "Редактировать профиль", None))
        self.action_4.setText(_translate("fpVATP", "График", None))
        self.action_5.setText(_translate("fpVATP", "Таблица результатов", None))

