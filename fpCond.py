# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\ormet\source\svi_vs_v.0.3\forms\fpCond.ui'
#
# Created: Thu May 22 10:52:56 2014
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
        fpCond.resize(415, 629)
        fpCond.setMinimumSize(QtCore.QSize(308, 193))
        self.centralwidget = QtGui.QWidget(fpCond)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.lcdMain = QtGui.QLCDNumber(self.centralwidget)
        self.lcdMain.setGeometry(QtCore.QRect(11, 41, 211, 41))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdMain.sizePolicy().hasHeightForWidth())
        self.lcdMain.setSizePolicy(sizePolicy)
        self.lcdMain.setSmallDecimalPoint(True)
        self.lcdMain.setProperty("value", 0.0)
        self.lcdMain.setProperty("intValue", 0)
        self.lcdMain.setObjectName(_fromUtf8("lcdMain"))
        self.leMain = QtGui.QLineEdit(self.centralwidget)
        self.leMain.setGeometry(QtCore.QRect(10, 700, 51, 21))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leMain.sizePolicy().hasHeightForWidth())
        self.leMain.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(12)
        self.leMain.setFont(font)
        self.leMain.setFrame(True)
        self.leMain.setReadOnly(True)
        self.leMain.setObjectName(_fromUtf8("leMain"))
        self.leTemp = QtGui.QLineEdit(self.centralwidget)
        self.leTemp.setGeometry(QtCore.QRect(141, 264, 81, 31))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.leTemp.sizePolicy().hasHeightForWidth())
        self.leTemp.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(12)
        self.leTemp.setFont(font)
        self.leTemp.setFrame(True)
        self.leTemp.setReadOnly(True)
        self.leTemp.setObjectName(_fromUtf8("leTemp"))
        self.tbTComp = QtGui.QToolButton(self.centralwidget)
        self.tbTComp.setGeometry(QtCore.QRect(10, 264, 121, 31))
        self.tbTComp.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tbTComp.setObjectName(_fromUtf8("tbTComp"))
        self.tbAutoT = QtGui.QToolButton(self.centralwidget)
        self.tbAutoT.setGeometry(QtCore.QRect(270, 264, 51, 31))
        self.tbAutoT.setFocusPolicy(QtCore.Qt.NoFocus)
        self.tbAutoT.setObjectName(_fromUtf8("tbAutoT"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(229, 264, 31, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.cbElec = QtGui.QComboBox(self.centralwidget)
        self.cbElec.setGeometry(QtCore.QRect(50, 510, 311, 22))
        self.cbElec.setObjectName(_fromUtf8("cbElec"))
        self.cbElec.addItem(_fromUtf8(""))
        self.label_6 = QtGui.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(40, 450, 61, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_6.setFont(font)
        self.label_6.setLineWidth(-5)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.llBand = QtGui.QLabel(self.centralwidget)
        self.llBand.setGeometry(QtCore.QRect(150, 450, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.llBand.setFont(font)
        self.llBand.setFrameShape(QtGui.QFrame.Panel)
        self.llBand.setFrameShadow(QtGui.QFrame.Sunken)
        self.llBand.setText(_fromUtf8(""))
        self.llBand.setObjectName(_fromUtf8("llBand"))
        self.lblEd = QtGui.QLabel(self.centralwidget)
        self.lblEd.setGeometry(QtCore.QRect(240, 40, 91, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.lblEd.setFont(font)
        self.lblEd.setObjectName(_fromUtf8("lblEd"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(10, 10, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_7.setFont(font)
        self.label_7.setLineWidth(-5)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(10, 87, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_8.setFont(font)
        self.label_8.setLineWidth(-5)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.lblEd_2 = QtGui.QLabel(self.centralwidget)
        self.lblEd_2.setGeometry(QtCore.QRect(240, 116, 91, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.lblEd_2.setFont(font)
        self.lblEd_2.setObjectName(_fromUtf8("lblEd_2"))
        self.lcdMain_2 = QtGui.QLCDNumber(self.centralwidget)
        self.lcdMain_2.setGeometry(QtCore.QRect(11, 118, 211, 41))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdMain_2.sizePolicy().hasHeightForWidth())
        self.lcdMain_2.setSizePolicy(sizePolicy)
        self.lcdMain_2.setSmallDecimalPoint(True)
        self.lcdMain_2.setProperty("value", 0.0)
        self.lcdMain_2.setProperty("intValue", 0)
        self.lcdMain_2.setObjectName(_fromUtf8("lcdMain_2"))
        self.lblEd_3 = QtGui.QLabel(self.centralwidget)
        self.lblEd_3.setGeometry(QtCore.QRect(240, 199, 91, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Verdana"))
        font.setPointSize(18)
        font.setBold(False)
        font.setWeight(50)
        self.lblEd_3.setFont(font)
        self.lblEd_3.setObjectName(_fromUtf8("lblEd_3"))
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(10, 169, 111, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_9.setFont(font)
        self.label_9.setLineWidth(-5)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.lcdMain_3 = QtGui.QLCDNumber(self.centralwidget)
        self.lcdMain_3.setGeometry(QtCore.QRect(11, 200, 211, 41))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcdMain_3.sizePolicy().hasHeightForWidth())
        self.lcdMain_3.setSizePolicy(sizePolicy)
        self.lcdMain_3.setSmallDecimalPoint(True)
        self.lcdMain_3.setProperty("value", 0.0)
        self.lcdMain_3.setProperty("intValue", 0)
        self.lcdMain_3.setObjectName(_fromUtf8("lcdMain_3"))
        self.leKu = QtGui.QDoubleSpinBox(self.centralwidget)
        self.leKu.setGeometry(QtCore.QRect(54, 368, 91, 21))
        self.leKu.setSingleStep(0.01)
        self.leKu.setObjectName(_fromUtf8("leKu"))
        self.leElec = QtGui.QLineEdit(self.centralwidget)
        self.leElec.setEnabled(False)
        self.leElec.setGeometry(QtCore.QRect(10, 330, 311, 22))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.leElec.setFont(font)
        self.leElec.setObjectName(_fromUtf8("leElec"))
        self.tbElecAdd = QtGui.QToolButton(self.centralwidget)
        self.tbElecAdd.setGeometry(QtCore.QRect(330, 330, 27, 22))
        self.tbElecAdd.setObjectName(_fromUtf8("tbElecAdd"))
        self.label_31 = QtGui.QLabel(self.centralwidget)
        self.label_31.setGeometry(QtCore.QRect(10, 302, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_31.setFont(font)
        self.label_31.setLineWidth(-5)
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.label_28 = QtGui.QLabel(self.centralwidget)
        self.label_28.setGeometry(QtCore.QRect(20, 370, 41, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_28.setFont(font)
        self.label_28.setLineWidth(-5)
        self.label_28.setObjectName(_fromUtf8("label_28"))
        self.tbCalib = QtGui.QToolButton(self.centralwidget)
        self.tbCalib.setGeometry(QtCore.QRect(10, 410, 341, 22))
        self.tbCalib.setObjectName(_fromUtf8("tbCalib"))
        self.cbElec_2 = QtGui.QComboBox(self.centralwidget)
        self.cbElec_2.setGeometry(QtCore.QRect(10, 340, 311, 22))
        self.cbElec_2.setObjectName(_fromUtf8("cbElec_2"))
        fpCond.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(fpCond)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 415, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.muAbout = QtGui.QMenu(self.menubar)
        self.muAbout.setObjectName(_fromUtf8("muAbout"))
        fpCond.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(fpCond)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        fpCond.setStatusBar(self.statusbar)
        self.actConf = QtGui.QAction(fpCond)
        self.actConf.setObjectName(_fromUtf8("actConf"))
        self.menubar.addAction(self.muAbout.menuAction())

        self.retranslateUi(fpCond)
        self.cbElec.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(fpCond)

    def retranslateUi(self, fpCond):
        fpCond.setWindowTitle(_translate("fpCond", "Кондуктометр", None))
        self.leMain.setText(_translate("fpCond", "12", None))
        self.leTemp.setText(_translate("fpCond", "12", None))
        self.tbTComp.setText(_translate("fpCond", "Термокомпенсация", None))
        self.tbAutoT.setText(_translate("fpCond", "АТК", None))
        self.label.setText(_translate("fpCond", "<sup>o</sup>С", None))
        self.cbElec.setItemText(0, _translate("fpCond", "Электрод1", None))
        self.label_6.setText(_translate("fpCond", "Диапазон", None))
        self.lblEd.setText(_translate("fpCond", "<html><head/><body><p/></body></html>", None))
        self.label_7.setText(_translate("fpCond", "Проводимость", None))
        self.label_8.setText(_translate("fpCond", "Содержание соли", None))
        self.lblEd_2.setText(_translate("fpCond", "<html><head/><body><p/></body></html>", None))
        self.lblEd_3.setText(_translate("fpCond", "<html><head/><body><p/></body></html>", None))
        self.label_9.setText(_translate("fpCond", "Сопротивление", None))
        self.tbElecAdd.setText(_translate("fpCond", "+", None))
        self.label_31.setText(_translate("fpCond", "Профиль измерения", None))
        self.label_28.setText(_translate("fpCond", "К<sub>яч</sub>=", None))
        self.tbCalib.setText(_translate("fpCond", "Сохранить", None))
        self.muAbout.setTitle(_translate("fpCond", "?", None))
        self.actConf.setText(_translate("fpCond", "Градуировка", None))

