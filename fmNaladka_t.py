# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\ormet\source\svi (4)\svi\forms\fmNaladka.ui'
#
# Created: Thu Sep 13 10:41:19 2018
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

class Ui_fmNaladka(object):
    def setupUi(self, fmNaladka):
        fmNaladka.setObjectName(_fromUtf8("fmNaladka"))
        fmNaladka.resize(788, 446)
        fmNaladka.setMinimumSize(QtCore.QSize(788, 446))
        fmNaladka.setDockOptions(QtGui.QMainWindow.AnimatedDocks)
        self.centralwidget = QtGui.QWidget(fmNaladka)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tbPort = QtGui.QPushButton(self.centralwidget)
        self.tbPort.setGeometry(QtCore.QRect(40, 20, 261, 41))
        self.tbPort.setObjectName(_fromUtf8("tbPort"))
        self.tbDataBase = QtGui.QPushButton(self.centralwidget)
        self.tbDataBase.setGeometry(QtCore.QRect(40, 90, 261, 41))
        self.tbDataBase.setObjectName(_fromUtf8("tbDataBase"))
        self.spbPortNumber = QtGui.QSpinBox(self.centralwidget)
        self.spbPortNumber.setGeometry(QtCore.QRect(320, 20, 81, 41))
        self.spbPortNumber.setObjectName(_fromUtf8("spbPortNumber"))
        self.tbSearchModuls = QtGui.QPushButton(self.centralwidget)
        self.tbSearchModuls.setGeometry(QtCore.QRect(40, 160, 261, 41))
        self.tbSearchModuls.setObjectName(_fromUtf8("tbSearchModuls"))
        self.tbV = QtGui.QPushButton(self.centralwidget)
        self.tbV.setGeometry(QtCore.QRect(460, 20, 261, 41))
        self.tbV.setObjectName(_fromUtf8("tbV"))
        self.tbT = QtGui.QPushButton(self.centralwidget)
        self.tbT.setGeometry(QtCore.QRect(460, 90, 261, 41))
        self.tbT.setObjectName(_fromUtf8("tbT"))
        self.tbA = QtGui.QPushButton(self.centralwidget)
        self.tbA.setGeometry(QtCore.QRect(460, 160, 261, 41))
        self.tbA.setObjectName(_fromUtf8("tbA"))
        self.tbP = QtGui.QPushButton(self.centralwidget)
        self.tbP.setGeometry(QtCore.QRect(460, 230, 261, 41))
        self.tbP.setObjectName(_fromUtf8("tbP"))
        self.tbC = QtGui.QPushButton(self.centralwidget)
        self.tbC.setGeometry(QtCore.QRect(460, 300, 261, 41))
        self.tbC.setObjectName(_fromUtf8("tbC"))
        self.tbADC = QtGui.QPushButton(self.centralwidget)
        self.tbADC.setGeometry(QtCore.QRect(40, 230, 261, 41))
        self.tbADC.setObjectName(_fromUtf8("tbADC"))
        self.tbWinb = QtGui.QPushButton(self.centralwidget)
        self.tbWinb.setGeometry(QtCore.QRect(40, 300, 261, 41))
        self.tbWinb.setObjectName(_fromUtf8("tbWinb"))
        fmNaladka.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(fmNaladka)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 788, 38))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.muDebug = QtGui.QMenu(self.menubar)
        self.muDebug.setObjectName(_fromUtf8("muDebug"))
        self.muSetting = QtGui.QMenu(self.menubar)
        self.muSetting.setObjectName(_fromUtf8("muSetting"))
        self.muVInstr = QtGui.QMenu(self.menubar)
        self.muVInstr.setObjectName(_fromUtf8("muVInstr"))
        self.muPar = QtGui.QMenu(self.menubar)
        self.muPar.setObjectName(_fromUtf8("muPar"))
        self.muAbout = QtGui.QMenu(self.menubar)
        self.muAbout.setObjectName(_fromUtf8("muAbout"))
        fmNaladka.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(fmNaladka)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        fmNaladka.setStatusBar(self.statusbar)
        self.actPortCons = QtGui.QAction(fmNaladka)
        self.actPortCons.setObjectName(_fromUtf8("actPortCons"))
        self.actMBCons = QtGui.QAction(fmNaladka)
        self.actMBCons.setObjectName(_fromUtf8("actMBCons"))
        self.actAD779x = QtGui.QAction(fmNaladka)
        self.actAD779x.setObjectName(_fromUtf8("actAD779x"))
        self.actParV = QtGui.QAction(fmNaladka)
        self.actParV.setObjectName(_fromUtf8("actParV"))
        self.actParT = QtGui.QAction(fmNaladka)
        self.actParT.setObjectName(_fromUtf8("actParT"))
        self.actParCond = QtGui.QAction(fmNaladka)
        self.actParCond.setObjectName(_fromUtf8("actParCond"))
        self.actParTP = QtGui.QAction(fmNaladka)
        self.actParTP.setObjectName(_fromUtf8("actParTP"))
        self.muDebug.addAction(self.actPortCons)
        self.muDebug.addAction(self.actMBCons)
        self.muDebug.addAction(self.actAD779x)
        self.muPar.addAction(self.actParV)
        self.muPar.addAction(self.actParT)
        self.muPar.addAction(self.actParCond)
        self.muPar.addAction(self.actParTP)
        self.menubar.addAction(self.muDebug.menuAction())
        self.menubar.addAction(self.muPar.menuAction())
        self.menubar.addAction(self.muVInstr.menuAction())
        self.menubar.addAction(self.muSetting.menuAction())
        self.menubar.addAction(self.muAbout.menuAction())

        self.retranslateUi(fmNaladka)
        QtCore.QMetaObject.connectSlotsByName(fmNaladka)

    def retranslateUi(self, fmNaladka):
        fmNaladka.setWindowTitle(_translate("fmNaladka", "СВП Ормет - режим наладки", None))
        self.tbPort.setText(_translate("fmNaladka", "Открыть порт", None))
        self.tbDataBase.setText(_translate("fmNaladka", "База номеров модулей", None))
        self.tbSearchModuls.setText(_translate("fmNaladka", "Поиск модулей", None))
        self.tbV.setText(_translate("fmNaladka", "Вольтметр", None))
        self.tbT.setText(_translate("fmNaladka", "Термометр", None))
        self.tbA.setText(_translate("fmNaladka", "Амперметр", None))
        self.tbP.setText(_translate("fmNaladka", "Измеритель давления", None))
        self.tbC.setText(_translate("fmNaladka", "Кондуктометр", None))
        self.tbADC.setText(_translate("fmNaladka", "АЦП", None))
        self.tbWinb.setText(_translate("fmNaladka", "Winb", None))
        self.muDebug.setTitle(_translate("fmNaladka", "Отладка", None))
        self.muSetting.setTitle(_translate("fmNaladka", "Настройка", None))
        self.muVInstr.setTitle(_translate("fmNaladka", "Виртуальные приборы", None))
        self.muPar.setTitle(_translate("fmNaladka", "Параметризация", None))
        self.muAbout.setTitle(_translate("fmNaladka", "?", None))
        self.actPortCons.setText(_translate("fmNaladka", "Консоль порта...", None))
        self.actMBCons.setText(_translate("fmNaladka", "Консоль драйвера ...", None))
        self.actAD779x.setText(_translate("fmNaladka", "AD779x...", None))
        self.actParV.setText(_translate("fmNaladka", "Милливольтметр", None))
        self.actParT.setText(_translate("fmNaladka", "Термометр", None))
        self.actParCond.setText(_translate("fmNaladka", "Кондуктометр", None))
        self.actParTP.setText(_translate("fmNaladka", "Измеритель давления", None))

