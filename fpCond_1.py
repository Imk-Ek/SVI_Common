# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\ormet\source\svi_vs_v.0.4\forms\fpCond_1.ui'
#
# Created: Fri Mar  6 15:02:08 2015
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

class Ui_fpCond(object):
    def setupUi(self, fpCond):
        fpCond.setObjectName(_fromUtf8("fpCond"))
        fpCond.resize(368, 522)
        fpCond.setMinimumSize(QtCore.QSize(368, 522))
        self.centralwidget = QtGui.QWidget(fpCond)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_31 = QtGui.QLabel(self.centralwidget)
        self.label_31.setMinimumSize(QtCore.QSize(121, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_31.setFont(font)
        self.label_31.setLineWidth(-5)
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.gridLayout.addWidget(self.label_31, 0, 0, 1, 1)
        self.label_34 = QtGui.QLabel(self.centralwidget)
        self.label_34.setMinimumSize(QtCore.QSize(121, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_34.setFont(font)
        self.label_34.setLineWidth(-5)
        self.label_34.setObjectName(_fromUtf8("label_34"))
        self.gridLayout.addWidget(self.label_34, 0, 1, 1, 3)
        self.lblProfilName = QtGui.QLabel(self.centralwidget)
        self.lblProfilName.setMinimumSize(QtCore.QSize(121, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblProfilName.setFont(font)
        self.lblProfilName.setLineWidth(-5)
        self.lblProfilName.setObjectName(_fromUtf8("lblProfilName"))
        self.gridLayout.addWidget(self.lblProfilName, 1, 0, 1, 1)
        self.lblDateTime = QtGui.QLabel(self.centralwidget)
        self.lblDateTime.setMinimumSize(QtCore.QSize(121, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblDateTime.setFont(font)
        self.lblDateTime.setLineWidth(-5)
        self.lblDateTime.setObjectName(_fromUtf8("lblDateTime"))
        self.gridLayout.addWidget(self.lblDateTime, 1, 1, 1, 3)
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setMinimumSize(QtCore.QSize(111, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_7.setFont(font)
        self.label_7.setLineWidth(-5)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout.addWidget(self.label_7, 2, 0, 1, 1)
        self.lcdMain = QtGui.QLCDNumber(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdMain.sizePolicy().hasHeightForWidth())
        self.lcdMain.setSizePolicy(sizePolicy)
        self.lcdMain.setMinimumSize(QtCore.QSize(151, 41))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        self.lcdMain.setPalette(palette)
        self.lcdMain.setSmallDecimalPoint(True)
        self.lcdMain.setProperty("value", 0.0)
        self.lcdMain.setProperty("intValue", 0)
        self.lcdMain.setObjectName(_fromUtf8("lcdMain"))
        self.gridLayout.addWidget(self.lcdMain, 3, 0, 1, 2)
        self.lblEd = QtGui.QLabel(self.centralwidget)
        self.lblEd.setMinimumSize(QtCore.QSize(161, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.lblEd.setFont(font)
        self.lblEd.setObjectName(_fromUtf8("lblEd"))
        self.gridLayout.addWidget(self.lblEd, 3, 2, 1, 2)
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setMinimumSize(QtCore.QSize(111, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_8.setFont(font)
        self.label_8.setLineWidth(-5)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.gridLayout.addWidget(self.label_8, 4, 0, 1, 1)
        self.lcdMain_2 = QtGui.QLCDNumber(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdMain_2.sizePolicy().hasHeightForWidth())
        self.lcdMain_2.setSizePolicy(sizePolicy)
        self.lcdMain_2.setMinimumSize(QtCore.QSize(151, 41))
        self.lcdMain_2.setSmallDecimalPoint(True)
        self.lcdMain_2.setProperty("value", 0.0)
        self.lcdMain_2.setProperty("intValue", 0)
        self.lcdMain_2.setObjectName(_fromUtf8("lcdMain_2"))
        self.gridLayout.addWidget(self.lcdMain_2, 5, 0, 1, 2)
        self.lblEd_2 = QtGui.QLabel(self.centralwidget)
        self.lblEd_2.setMinimumSize(QtCore.QSize(101, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.lblEd_2.setFont(font)
        self.lblEd_2.setObjectName(_fromUtf8("lblEd_2"))
        self.gridLayout.addWidget(self.lblEd_2, 5, 3, 1, 1)
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setMinimumSize(QtCore.QSize(111, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_9.setFont(font)
        self.label_9.setLineWidth(-5)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.gridLayout.addWidget(self.label_9, 6, 0, 1, 1)
        self.lcdMain_3 = QtGui.QLCDNumber(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdMain_3.sizePolicy().hasHeightForWidth())
        self.lcdMain_3.setSizePolicy(sizePolicy)
        self.lcdMain_3.setMinimumSize(QtCore.QSize(211, 41))
        self.lcdMain_3.setSmallDecimalPoint(True)
        self.lcdMain_3.setProperty("value", 0.0)
        self.lcdMain_3.setProperty("intValue", 0)
        self.lcdMain_3.setObjectName(_fromUtf8("lcdMain_3"))
        self.gridLayout.addWidget(self.lcdMain_3, 7, 0, 1, 3)
        self.lblEd_3 = QtGui.QLabel(self.centralwidget)
        self.lblEd_3.setMinimumSize(QtCore.QSize(91, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.lblEd_3.setFont(font)
        self.lblEd_3.setObjectName(_fromUtf8("lblEd_3"))
        self.gridLayout.addWidget(self.lblEd_3, 7, 3, 1, 1)
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setMinimumSize(QtCore.QSize(218, 105))
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
        self.leTemp.setGeometry(QtCore.QRect(123, 23, 61, 24))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leTemp.sizePolicy().hasHeightForWidth())
        self.leTemp.setSizePolicy(sizePolicy)
        self.leTemp.setMinimumSize(QtCore.QSize(61, 24))
        self.leTemp.setMaximumSize(QtCore.QSize(61, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(12)
        self.leTemp.setFont(font)
        self.leTemp.setFrame(True)
        self.leTemp.setObjectName(_fromUtf8("leTemp"))
        self.tbEnterT = QtGui.QToolButton(self.groupBox)
        self.tbEnterT.setGeometry(QtCore.QRect(130, 60, 71, 31))
        self.tbEnterT.setMinimumSize(QtCore.QSize(71, 31))
        self.tbEnterT.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tbEnterT.setObjectName(_fromUtf8("tbEnterT"))
        self.label = QtGui.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(190, 23, 18, 18))
        self.label.setMinimumSize(QtCore.QSize(18, 18))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.groupBox, 8, 0, 1, 3)
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setMinimumSize(QtCore.QSize(231, 57))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.leID = QtGui.QLineEdit(self.groupBox_2)
        self.leID.setGeometry(QtCore.QRect(49, 23, 81, 24))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leID.sizePolicy().hasHeightForWidth())
        self.leID.setSizePolicy(sizePolicy)
        self.leID.setMinimumSize(QtCore.QSize(81, 24))
        self.leID.setMaximumSize(QtCore.QSize(81, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(12)
        self.leID.setFont(font)
        self.leID.setFrame(True)
        self.leID.setObjectName(_fromUtf8("leID"))
        self.tbSaveToNotepad_ = QtGui.QToolButton(self.groupBox_2)
        self.tbSaveToNotepad_.setGeometry(QtCore.QRect(142, 20, 71, 31))
        self.tbSaveToNotepad_.setMinimumSize(QtCore.QSize(71, 31))
        self.tbSaveToNotepad_.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tbSaveToNotepad_.setObjectName(_fromUtf8("tbSaveToNotepad_"))
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setGeometry(QtCore.QRect(17, 23, 19, 18))
        self.label_4.setMinimumSize(QtCore.QSize(19, 18))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.groupBox_2, 9, 0, 1, 3)
        self.tbSelectProfil = QtGui.QToolButton(self.centralwidget)
        self.tbSelectProfil.setMinimumSize(QtCore.QSize(121, 31))
        self.tbSelectProfil.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tbSelectProfil.setObjectName(_fromUtf8("tbSelectProfil"))
        self.gridLayout.addWidget(self.tbSelectProfil, 10, 0, 1, 3)
        self.horizontalLayout.addLayout(self.gridLayout)
        fpCond.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(fpCond)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 368, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        fpCond.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(fpCond)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        fpCond.setStatusBar(self.statusbar)
        self.actConf = QtGui.QAction(fpCond)
        self.actConf.setObjectName(_fromUtf8("actConf"))
        self.action = QtGui.QAction(fpCond)
        self.action.setObjectName(_fromUtf8("action"))
        self.action_2 = QtGui.QAction(fpCond)
        self.action_2.setObjectName(_fromUtf8("action_2"))
        self.action_3 = QtGui.QAction(fpCond)
        self.action_3.setObjectName(_fromUtf8("action_3"))
        self.action_4 = QtGui.QAction(fpCond)
        self.action_4.setObjectName(_fromUtf8("action_4"))
        self.action_5 = QtGui.QAction(fpCond)
        self.action_5.setObjectName(_fromUtf8("action_5"))

        self.retranslateUi(fpCond)
        QtCore.QMetaObject.connectSlotsByName(fpCond)

    def retranslateUi(self, fpCond):
        fpCond.setWindowTitle(_translate("fpCond", "Кондуктометр", None))
        self.label_31.setText(_translate("fpCond", "Профиль измерения", None))
        self.label_34.setText(_translate("fpCond", "Дата и время", None))
        self.lblProfilName.setText(_translate("fpCond", "КОНДУКТОМЕТР 1", None))
        self.lblDateTime.setText(_translate("fpCond", "11.11.2011 11-11-11", None))
        self.label_7.setText(_translate("fpCond", "Проводимость", None))
        self.lblEd.setText(_translate("fpCond", "<html><head/><body><p/></body></html>", None))
        self.label_8.setText(_translate("fpCond", "Содержание NaCl", None))
        self.lblEd_2.setText(_translate("fpCond", "<html><head/><body><p/></body></html>", None))
        self.label_9.setText(_translate("fpCond", "Сопротивление", None))
        self.lblEd_3.setText(_translate("fpCond", "<html><head/><body><p/></body></html>", None))
        self.groupBox.setTitle(_translate("fpCond", "Термокомпенсация", None))
        self.rbAutoT.setText(_translate("fpCond", "Автоматическая", None))
        self.rbManualT.setText(_translate("fpCond", "Ручной ввод", None))
        self.rbOffT.setText(_translate("fpCond", "Отключить", None))
        self.leTemp.setText(_translate("fpCond", "12", None))
        self.tbEnterT.setText(_translate("fpCond", "Ввод", None))
        self.label.setText(_translate("fpCond", "<sup>o</sup>С", None))
        self.groupBox_2.setTitle(_translate("fpCond", "Запись в блокнот", None))
        self.leID.setText(_translate("fpCond", "12", None))
        self.tbSaveToNotepad_.setText(_translate("fpCond", "Записать", None))
        self.label_4.setText(_translate("fpCond", "ID", None))
        self.tbSelectProfil.setText(_translate("fpCond", " К Выбору профиля", None))
        self.actConf.setText(_translate("fpCond", "Градуировка", None))
        self.action.setText(_translate("fpCond", "Градуировка", None))
        self.action_2.setText(_translate("fpCond", "Сохранить профиль", None))
        self.action_3.setText(_translate("fpCond", "Редактировать профиль", None))
        self.action_4.setText(_translate("fpCond", "График", None))
        self.action_5.setText(_translate("fpCond", "Таблица результатов", None))

