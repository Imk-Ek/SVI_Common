# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\ormet\source\svi_vs_v.0.5.1\forms\fpO_2.ui'
#
# Created: Fri Sep 25 14:17:11 2015
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

class Ui_fpO_2(object):
    def setupUi(self, fpO_2):
        fpO_2.setObjectName(_fromUtf8("fpO_2"))
        fpO_2.resize(400, 397)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(fpO_2.sizePolicy().hasHeightForWidth())
        fpO_2.setSizePolicy(sizePolicy)
        fpO_2.setMinimumSize(QtCore.QSize(400, 1))
        fpO_2.setMaximumSize(QtCore.QSize(400, 397))
        self.centralwidget = QtGui.QWidget(fpO_2)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(10, 264, 111, 21))
        self.label_5.setMinimumSize(QtCore.QSize(111, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setLineWidth(-5)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_3 = QtGui.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(225, 44, 81, 41))
        self.label_3.setMinimumSize(QtCore.QSize(81, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lblProfilName = QtGui.QLabel(self.centralwidget)
        self.lblProfilName.setGeometry(QtCore.QRect(10, 20, 121, 21))
        self.lblProfilName.setMinimumSize(QtCore.QSize(121, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblProfilName.setFont(font)
        self.lblProfilName.setLineWidth(-5)
        self.lblProfilName.setObjectName(_fromUtf8("lblProfilName"))
        self.label_31 = QtGui.QLabel(self.centralwidget)
        self.label_31.setGeometry(QtCore.QRect(10, 0, 121, 21))
        self.label_31.setMinimumSize(QtCore.QSize(121, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_31.setFont(font)
        self.label_31.setLineWidth(-5)
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.lcdMain = QtGui.QLCDNumber(self.centralwidget)
        self.lcdMain.setGeometry(QtCore.QRect(10, 44, 211, 41))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdMain.sizePolicy().hasHeightForWidth())
        self.lcdMain.setSizePolicy(sizePolicy)
        self.lcdMain.setMinimumSize(QtCore.QSize(211, 41))
        self.lcdMain.setSmallDecimalPoint(True)
        self.lcdMain.setProperty("value", 0.0)
        self.lcdMain.setProperty("intValue", 0)
        self.lcdMain.setObjectName(_fromUtf8("lcdMain"))
        self.lcdMain_2 = QtGui.QLCDNumber(self.centralwidget)
        self.lcdMain_2.setGeometry(QtCore.QRect(10, 91, 211, 41))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdMain_2.sizePolicy().hasHeightForWidth())
        self.lcdMain_2.setSizePolicy(sizePolicy)
        self.lcdMain_2.setMinimumSize(QtCore.QSize(211, 41))
        self.lcdMain_2.setSmallDecimalPoint(True)
        self.lcdMain_2.setProperty("value", 0.0)
        self.lcdMain_2.setProperty("intValue", 0)
        self.lcdMain_2.setObjectName(_fromUtf8("lcdMain_2"))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(225, 91, 81, 41))
        self.label_6.setMinimumSize(QtCore.QSize(81, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(12)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(3, 138, 201, 121))
        self.groupBox.setMinimumSize(QtCore.QSize(2, 121))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.rbAutoT = QtGui.QRadioButton(self.groupBox)
        self.rbAutoT.setGeometry(QtCore.QRect(10, 24, 111, 17))
        self.rbAutoT.setMinimumSize(QtCore.QSize(111, 17))
        self.rbAutoT.setObjectName(_fromUtf8("rbAutoT"))
        self.rbManualT = QtGui.QRadioButton(self.groupBox)
        self.rbManualT.setGeometry(QtCore.QRect(10, 54, 82, 17))
        self.rbManualT.setMinimumSize(QtCore.QSize(82, 17))
        self.rbManualT.setObjectName(_fromUtf8("rbManualT"))
        self.rbOffT = QtGui.QRadioButton(self.groupBox)
        self.rbOffT.setGeometry(QtCore.QRect(10, 84, 82, 17))
        self.rbOffT.setMinimumSize(QtCore.QSize(82, 17))
        self.rbOffT.setObjectName(_fromUtf8("rbOffT"))
        self.leTemp = QtGui.QLineEdit(self.groupBox)
        self.leTemp.setGeometry(QtCore.QRect(130, 24, 41, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leTemp.sizePolicy().hasHeightForWidth())
        self.leTemp.setSizePolicy(sizePolicy)
        self.leTemp.setMinimumSize(QtCore.QSize(6, 3))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(12)
        self.leTemp.setFont(font)
        self.leTemp.setFrame(True)
        self.leTemp.setObjectName(_fromUtf8("leTemp"))
        self.tbEnterT = QtGui.QToolButton(self.groupBox)
        self.tbEnterT.setGeometry(QtCore.QRect(120, 74, 71, 31))
        self.tbEnterT.setMinimumSize(QtCore.QSize(8, 31))
        self.tbEnterT.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tbEnterT.setObjectName(_fromUtf8("tbEnterT"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(175, 24, 31, 31))
        self.label.setMinimumSize(QtCore.QSize(8, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(200, 139, 201, 121))
        self.groupBox_2.setMinimumSize(QtCore.QSize(2, 121))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.rbAutoP = QtGui.QRadioButton(self.groupBox_2)
        self.rbAutoP.setGeometry(QtCore.QRect(10, 24, 111, 17))
        self.rbAutoP.setMinimumSize(QtCore.QSize(111, 17))
        self.rbAutoP.setObjectName(_fromUtf8("rbAutoP"))
        self.rbManualP = QtGui.QRadioButton(self.groupBox_2)
        self.rbManualP.setGeometry(QtCore.QRect(10, 54, 82, 17))
        self.rbManualP.setMinimumSize(QtCore.QSize(82, 17))
        self.rbManualP.setObjectName(_fromUtf8("rbManualP"))
        self.rbOffP = QtGui.QRadioButton(self.groupBox_2)
        self.rbOffP.setGeometry(QtCore.QRect(10, 84, 82, 17))
        self.rbOffP.setMinimumSize(QtCore.QSize(82, 17))
        self.rbOffP.setObjectName(_fromUtf8("rbOffP"))
        self.lePressure = QtGui.QLineEdit(self.groupBox_2)
        self.lePressure.setGeometry(QtCore.QRect(119, 24, 41, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lePressure.sizePolicy().hasHeightForWidth())
        self.lePressure.setSizePolicy(sizePolicy)
        self.lePressure.setMinimumSize(QtCore.QSize(6, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(12)
        self.lePressure.setFont(font)
        self.lePressure.setFrame(True)
        self.lePressure.setObjectName(_fromUtf8("lePressure"))
        self.tbEnterP = QtGui.QToolButton(self.groupBox_2)
        self.tbEnterP.setGeometry(QtCore.QRect(122, 74, 71, 31))
        self.tbEnterP.setMinimumSize(QtCore.QSize(8, 31))
        self.tbEnterP.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tbEnterP.setObjectName(_fromUtf8("tbEnterP"))
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setGeometry(QtCore.QRect(160, 24, 31, 31))
        self.label_2.setMinimumSize(QtCore.QSize(31, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(12)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.leSalt = QtGui.QLineEdit(self.centralwidget)
        self.leSalt.setGeometry(QtCore.QRect(135, 264, 84, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leSalt.sizePolicy().hasHeightForWidth())
        self.leSalt.setSizePolicy(sizePolicy)
        self.leSalt.setMinimumSize(QtCore.QSize(81, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(12)
        self.leSalt.setFont(font)
        self.leSalt.setFrame(True)
        self.leSalt.setReadOnly(True)
        self.leSalt.setObjectName(_fromUtf8("leSalt"))
        self.label_4 = QtGui.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(225, 264, 61, 31))
        self.label_4.setMinimumSize(QtCore.QSize(61, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 301, 296, 61))
        self.groupBox_3.setMinimumSize(QtCore.QSize(281, 61))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.leID = QtGui.QLineEdit(self.groupBox_3)
        self.leID.setGeometry(QtCore.QRect(40, 20, 81, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leID.sizePolicy().hasHeightForWidth())
        self.leID.setSizePolicy(sizePolicy)
        self.leID.setMinimumSize(QtCore.QSize(81, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(12)
        self.leID.setFont(font)
        self.leID.setFrame(True)
        self.leID.setObjectName(_fromUtf8("leID"))
        self.tbSaveToNotepad_ = QtGui.QToolButton(self.groupBox_3)
        self.tbSaveToNotepad_.setGeometry(QtCore.QRect(140, 20, 81, 31))
        self.tbSaveToNotepad_.setMinimumSize(QtCore.QSize(81, 31))
        self.tbSaveToNotepad_.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tbSaveToNotepad_.setObjectName(_fromUtf8("tbSaveToNotepad_"))
        self.label_7 = QtGui.QLabel(self.groupBox_3)
        self.label_7.setGeometry(QtCore.QRect(10, 20, 31, 31))
        self.label_7.setMinimumSize(QtCore.QSize(31, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(12)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.tbSelectProfil = QtGui.QToolButton(self.centralwidget)
        self.tbSelectProfil.setGeometry(QtCore.QRect(230, 5, 121, 31))
        self.tbSelectProfil.setMinimumSize(QtCore.QSize(121, 31))
        self.tbSelectProfil.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tbSelectProfil.setObjectName(_fromUtf8("tbSelectProfil"))
        fpO_2.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(fpO_2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.muAbout = QtGui.QMenu(self.menubar)
        self.muAbout.setObjectName(_fromUtf8("muAbout"))
        fpO_2.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(fpO_2)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        fpO_2.setStatusBar(self.statusbar)
        self.actConf = QtGui.QAction(fpO_2)
        self.actConf.setObjectName(_fromUtf8("actConf"))
        self.menubar.addAction(self.muAbout.menuAction())

        self.retranslateUi(fpO_2)
        QtCore.QMetaObject.connectSlotsByName(fpO_2)

    def retranslateUi(self, fpO_2):
        fpO_2.setWindowTitle(_translate("fpO_2", "Кислородомер", None))
        self.label_5.setText(_translate("fpO_2", "Содержание соли", None))
        self.label_3.setText(_translate("fpO_2", "<html><head/><body><p>мг/дм<span style=\" vertical-align:super;\">3</span></p></body></html>", None))
        self.lblProfilName.setText(_translate("fpO_2", "КИСЛОРОДОМЕТР 1", None))
        self.label_31.setText(_translate("fpO_2", "Профиль измерения", None))
        self.label_6.setText(_translate("fpO_2", "<html><head/><body><p>%</p></body></html>", None))
        self.groupBox.setTitle(_translate("fpO_2", "Термокомпенсация", None))
        self.rbAutoT.setText(_translate("fpO_2", "Автоматическая", None))
        self.rbManualT.setText(_translate("fpO_2", "Ручной ввод", None))
        self.rbOffT.setText(_translate("fpO_2", "Отключить", None))
        self.leTemp.setText(_translate("fpO_2", "12", None))
        self.tbEnterT.setText(_translate("fpO_2", "Ввод", None))
        self.label.setText(_translate("fpO_2", "<sup>o</sup>С", None))
        self.groupBox_2.setTitle(_translate("fpO_2", "Компенсация давления", None))
        self.rbAutoP.setText(_translate("fpO_2", "Автоматическая", None))
        self.rbManualP.setText(_translate("fpO_2", "Ручной ввод", None))
        self.rbOffP.setText(_translate("fpO_2", "Отключить", None))
        self.lePressure.setText(_translate("fpO_2", "12", None))
        self.tbEnterP.setText(_translate("fpO_2", "Ввод", None))
        self.label_2.setText(_translate("fpO_2", "<html><head/><body><p>кПа</p></body></html>", None))
        self.leSalt.setText(_translate("fpO_2", "0", None))
        self.label_4.setText(_translate("fpO_2", "<html><head/><body><p>мг/дм<span style=\" vertical-align:super;\">3</span></p></body></html>", None))
        self.groupBox_3.setTitle(_translate("fpO_2", "Запись в блокнот", None))
        self.leID.setText(_translate("fpO_2", "12", None))
        self.tbSaveToNotepad_.setText(_translate("fpO_2", "Записать", None))
        self.label_7.setText(_translate("fpO_2", "ID", None))
        self.tbSelectProfil.setText(_translate("fpO_2", " К Выбору профиля", None))
        self.muAbout.setTitle(_translate("fpO_2", "?", None))
        self.actConf.setText(_translate("fpO_2", "Градуировка", None))

