# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\ormet\source\svi_meteo_19_11_2015\svi\forms\fpIon_2.ui'
#
# Created: Fri Nov 20 10:31:18 2015
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

class Ui_fpIon(object):
    def setupUi(self, fpIon):
        fpIon.setObjectName(_fromUtf8("fpIon"))
        fpIon.resize(400, 256)
        fpIon.setMinimumSize(QtCore.QSize(400, 250))
        fpIon.setMaximumSize(QtCore.QSize(400, 256))
        fpIon.setAcceptDrops(False)
        self.centralwidget = QtGui.QWidget(fpIon)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.lcdMain = QtGui.QLCDNumber(self.centralwidget)
        self.lcdMain.setGeometry(QtCore.QRect(10, 24, 261, 91))
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
        self.lcdMain.setSegmentStyle(QtGui.QLCDNumber.Filled)
        self.lcdMain.setProperty("value", -1.0)
        self.lcdMain.setProperty("intValue", -1)
        self.lcdMain.setObjectName(_fromUtf8("lcdMain"))
        self.lblProfilName = QtGui.QLabel(self.centralwidget)
        self.lblProfilName.setGeometry(QtCore.QRect(80, 0, 121, 21))
        self.lblProfilName.setMinimumSize(QtCore.QSize(121, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblProfilName.setFont(font)
        self.lblProfilName.setLineWidth(-5)
        self.lblProfilName.setObjectName(_fromUtf8("lblProfilName"))
        self.label_31 = QtGui.QLabel(self.centralwidget)
        self.label_31.setGeometry(QtCore.QRect(10, 1, 61, 21))
        self.label_31.setMinimumSize(QtCore.QSize(1, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_31.setFont(font)
        self.label_31.setLineWidth(-5)
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.lblEd = QtGui.QLabel(self.centralwidget)
        self.lblEd.setGeometry(QtCore.QRect(272, 23, 121, 31))
        self.lblEd.setMinimumSize(QtCore.QSize(20, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.lblEd.setFont(font)
        self.lblEd.setObjectName(_fromUtf8("lblEd"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(200, 120, 191, 105))
        self.groupBox.setMinimumSize(QtCore.QSize(2, 105))
        self.groupBox.setFlat(False)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.rbAutoT = QtGui.QRadioButton(self.groupBox)
        self.rbAutoT.setGeometry(QtCore.QRect(10, 26, 107, 17))
        self.rbAutoT.setMinimumSize(QtCore.QSize(107, 17))
        self.rbAutoT.setObjectName(_fromUtf8("rbAutoT"))
        self.rbManualT = QtGui.QRadioButton(self.groupBox)
        self.rbManualT.setGeometry(QtCore.QRect(10, 53, 87, 17))
        self.rbManualT.setMinimumSize(QtCore.QSize(87, 17))
        self.rbManualT.setObjectName(_fromUtf8("rbManualT"))
        self.rbOffT = QtGui.QRadioButton(self.groupBox)
        self.rbOffT.setGeometry(QtCore.QRect(10, 77, 82, 17))
        self.rbOffT.setMinimumSize(QtCore.QSize(82, 17))
        self.rbOffT.setObjectName(_fromUtf8("rbOffT"))
        self.leTemp = QtGui.QLineEdit(self.groupBox)
        self.leTemp.setGeometry(QtCore.QRect(123, 23, 41, 24))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leTemp.sizePolicy().hasHeightForWidth())
        self.leTemp.setSizePolicy(sizePolicy)
        self.leTemp.setMinimumSize(QtCore.QSize(6, 24))
        self.leTemp.setMaximumSize(QtCore.QSize(61, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(12)
        self.leTemp.setFont(font)
        self.leTemp.setFrame(True)
        self.leTemp.setObjectName(_fromUtf8("leTemp"))
        self.tbEnterT = QtGui.QToolButton(self.groupBox)
        self.tbEnterT.setGeometry(QtCore.QRect(121, 60, 61, 31))
        self.tbEnterT.setMinimumSize(QtCore.QSize(4, 4))
        self.tbEnterT.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tbEnterT.setObjectName(_fromUtf8("tbEnterT"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(167, 23, 18, 18))
        self.label.setMinimumSize(QtCore.QSize(18, 18))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.label_5 = QtGui.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(250, 0, 61, 18))
        self.label_5.setMinimumSize(QtCore.QSize(19, 18))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(12)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.lblID = QtGui.QLabel(self.centralwidget)
        self.lblID.setGeometry(QtCore.QRect(320, 0, 81, 18))
        self.lblID.setMinimumSize(QtCore.QSize(19, 18))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(12)
        self.lblID.setFont(font)
        self.lblID.setObjectName(_fromUtf8("lblID"))
        self.tbSaveToNotepad_ = QtGui.QToolButton(self.centralwidget)
        self.tbSaveToNotepad_.setGeometry(QtCore.QRect(273, 80, 121, 31))
        self.tbSaveToNotepad_.setMinimumSize(QtCore.QSize(71, 31))
        self.tbSaveToNotepad_.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tbSaveToNotepad_.setObjectName(_fromUtf8("tbSaveToNotepad_"))
        self.cbEd_3 = QtGui.QComboBox(self.centralwidget)
        self.cbEd_3.setGeometry(QtCore.QRect(100, 196, 91, 31))
        self.cbEd_3.setMinimumSize(QtCore.QSize(5, 5))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.cbEd_3.setFont(font)
        self.cbEd_3.setAutoFillBackground(True)
        self.cbEd_3.setObjectName(_fromUtf8("cbEd_3"))
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(10, 116, 111, 16))
        self.label_8.setMinimumSize(QtCore.QSize(111, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_8.setFont(font)
        self.label_8.setLineWidth(-5)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.lblEd_2 = QtGui.QLabel(self.centralwidget)
        self.lblEd_2.setGeometry(QtCore.QRect(100, 149, 61, 21))
        self.lblEd_2.setMinimumSize(QtCore.QSize(5, 5))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.lblEd_2.setFont(font)
        self.lblEd_2.setObjectName(_fromUtf8("lblEd_2"))
        self.lcdMain_2 = QtGui.QLCDNumber(self.centralwidget)
        self.lcdMain_2.setGeometry(QtCore.QRect(10, 138, 81, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdMain_2.sizePolicy().hasHeightForWidth())
        self.lcdMain_2.setSizePolicy(sizePolicy)
        self.lcdMain_2.setMinimumSize(QtCore.QSize(2, 2))
        self.lcdMain_2.setSmallDecimalPoint(True)
        self.lcdMain_2.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcdMain_2.setProperty("value", -1234.0)
        self.lcdMain_2.setProperty("intValue", -1234)
        self.lcdMain_2.setObjectName(_fromUtf8("lcdMain_2"))
        self.lcdMain_3 = QtGui.QLCDNumber(self.centralwidget)
        self.lcdMain_3.setGeometry(QtCore.QRect(10, 195, 81, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdMain_3.sizePolicy().hasHeightForWidth())
        self.lcdMain_3.setSizePolicy(sizePolicy)
        self.lcdMain_3.setMinimumSize(QtCore.QSize(2, 2))
        self.lcdMain_3.setSmallDecimalPoint(True)
        self.lcdMain_3.setSegmentStyle(QtGui.QLCDNumber.Flat)
        self.lcdMain_3.setProperty("value", 0.0)
        self.lcdMain_3.setProperty("intValue", 0)
        self.lcdMain_3.setObjectName(_fromUtf8("lcdMain_3"))
        self.lblConcentr = QtGui.QLabel(self.centralwidget)
        self.lblConcentr.setGeometry(QtCore.QRect(10, 176, 111, 21))
        self.lblConcentr.setMinimumSize(QtCore.QSize(111, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblConcentr.setFont(font)
        self.lblConcentr.setLineWidth(-5)
        self.lblConcentr.setObjectName(_fromUtf8("lblConcentr"))
        fpIon.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(fpIon)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 400, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        fpIon.setMenuBar(self.menubar)
        self.actConf = QtGui.QAction(fpIon)
        self.actConf.setObjectName(_fromUtf8("actConf"))
        self.action = QtGui.QAction(fpIon)
        self.action.setObjectName(_fromUtf8("action"))
        self.action_2 = QtGui.QAction(fpIon)
        self.action_2.setObjectName(_fromUtf8("action_2"))
        self.action_3 = QtGui.QAction(fpIon)
        self.action_3.setObjectName(_fromUtf8("action_3"))
        self.action_4 = QtGui.QAction(fpIon)
        self.action_4.setObjectName(_fromUtf8("action_4"))
        self.action_5 = QtGui.QAction(fpIon)
        self.action_5.setObjectName(_fromUtf8("action_5"))

        self.retranslateUi(fpIon)
        QtCore.QMetaObject.connectSlotsByName(fpIon)

    def retranslateUi(self, fpIon):
        fpIon.setWindowTitle(_translate("fpIon", "Иономер", None))
        self.lblProfilName.setText(_translate("fpIon", "Иономер 1", None))
        self.label_31.setText(_translate("fpIon", "Профиль", None))
        self.lblEd.setText(_translate("fpIon", "Ед.Изм<html><head/><body><p/></body></html>", None))
        self.groupBox.setTitle(_translate("fpIon", "Термокомпенсация", None))
        self.rbAutoT.setText(_translate("fpIon", "Автоматическая", None))
        self.rbManualT.setText(_translate("fpIon", "Ручной ввод", None))
        self.rbOffT.setText(_translate("fpIon", "Отключить", None))
        self.leTemp.setText(_translate("fpIon", "12", None))
        self.tbEnterT.setText(_translate("fpIon", "Ввод", None))
        self.label.setText(_translate("fpIon", "<sup>o</sup>С", None))
        self.label_5.setText(_translate("fpIon", "Проба", None))
        self.lblID.setText(_translate("fpIon", "ID", None))
        self.tbSaveToNotepad_.setText(_translate("fpIon", "Записать в блокнот", None))
        self.label_8.setText(_translate("fpIon", "Напряжение", None))
        self.lblEd_2.setText(_translate("fpIon", "<html><head/><body><p><span style=\" font-size:12pt;\">Ед.Изм</span></p><p><span style=\" font-size:12pt;\"><br/></span></p></body></html>", None))
        self.lblConcentr.setText(_translate("fpIon", "Содержание NaCl", None))
        self.actConf.setText(_translate("fpIon", "Градуировка", None))
        self.action.setText(_translate("fpIon", "Градуировка", None))
        self.action_2.setText(_translate("fpIon", "Сохранить профиль", None))
        self.action_3.setText(_translate("fpIon", "Редактировать профиль", None))
        self.action_4.setText(_translate("fpIon", "График", None))
        self.action_5.setText(_translate("fpIon", "Таблица результатов", None))
