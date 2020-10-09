# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\ormet\source\svi (4)\svi\forms\fmProtokol.ui'
#
# Created: Thu Sep 13 10:44:09 2018
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

class Ui_fmProtokol(object):
    def setupUi(self, fmProtokol):
        fmProtokol.setObjectName(_fromUtf8("fmProtokol"))
        fmProtokol.resize(283, 270)
        self.centralwidget = QtGui.QWidget(fmProtokol)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.columnView = QtGui.QColumnView(self.centralwidget)
        self.columnView.setObjectName(_fromUtf8("columnView"))
        self.gridLayout.addWidget(self.columnView, 0, 0, 1, 5)
        spacerItem = QtGui.QSpacerItem(27, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.btnSave = QtGui.QPushButton(self.centralwidget)
        self.btnSave.setObjectName(_fromUtf8("btnSave"))
        self.gridLayout.addWidget(self.btnSave, 1, 1, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(28, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 2, 1, 1)
        self.btnPrint = QtGui.QPushButton(self.centralwidget)
        self.btnPrint.setObjectName(_fromUtf8("btnPrint"))
        self.gridLayout.addWidget(self.btnPrint, 1, 3, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(27, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 1, 4, 1, 1)
        fmProtokol.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(fmProtokol)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 283, 21))
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
        fmProtokol.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(fmProtokol)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        fmProtokol.setStatusBar(self.statusbar)
        self.actPortCons = QtGui.QAction(fmProtokol)
        self.actPortCons.setObjectName(_fromUtf8("actPortCons"))
        self.actMBCons = QtGui.QAction(fmProtokol)
        self.actMBCons.setObjectName(_fromUtf8("actMBCons"))
        self.actAD779x = QtGui.QAction(fmProtokol)
        self.actAD779x.setObjectName(_fromUtf8("actAD779x"))
        self.actParV = QtGui.QAction(fmProtokol)
        self.actParV.setObjectName(_fromUtf8("actParV"))
        self.actParT = QtGui.QAction(fmProtokol)
        self.actParT.setObjectName(_fromUtf8("actParT"))
        self.actParCond = QtGui.QAction(fmProtokol)
        self.actParCond.setObjectName(_fromUtf8("actParCond"))
        self.actParTP = QtGui.QAction(fmProtokol)
        self.actParTP.setObjectName(_fromUtf8("actParTP"))
        self.actParAmper = QtGui.QAction(fmProtokol)
        self.actParAmper.setObjectName(_fromUtf8("actParAmper"))
        self.muDebug.addAction(self.actPortCons)
        self.muDebug.addAction(self.actMBCons)
        self.muDebug.addAction(self.actAD779x)
        self.muPar.addAction(self.actParV)
        self.muPar.addAction(self.actParT)
        self.muPar.addAction(self.actParCond)
        self.muPar.addAction(self.actParTP)
        self.muPar.addAction(self.actParAmper)
        self.menubar.addAction(self.muDebug.menuAction())
        self.menubar.addAction(self.muPar.menuAction())
        self.menubar.addAction(self.muVInstr.menuAction())
        self.menubar.addAction(self.muSetting.menuAction())
        self.menubar.addAction(self.muAbout.menuAction())

        self.retranslateUi(fmProtokol)
        QtCore.QMetaObject.connectSlotsByName(fmProtokol)

    def retranslateUi(self, fmProtokol):
        fmProtokol.setWindowTitle(_translate("fmProtokol", "СВП Ормет - режим наладки", None))
        self.btnSave.setText(_translate("fmProtokol", "Сохранить", None))
        self.btnPrint.setText(_translate("fmProtokol", "Печать", None))
        self.muDebug.setTitle(_translate("fmProtokol", "Отладка", None))
        self.muSetting.setTitle(_translate("fmProtokol", "Настройка", None))
        self.muVInstr.setTitle(_translate("fmProtokol", "Виртуальные приборы", None))
        self.muPar.setTitle(_translate("fmProtokol", "Параметризация", None))
        self.muAbout.setTitle(_translate("fmProtokol", "?", None))
        self.actPortCons.setText(_translate("fmProtokol", "Консоль порта...", None))
        self.actMBCons.setText(_translate("fmProtokol", "Консоль драйвера ...", None))
        self.actAD779x.setText(_translate("fmProtokol", "AD779x...", None))
        self.actParV.setText(_translate("fmProtokol", "Милливольтметр", None))
        self.actParT.setText(_translate("fmProtokol", "Термометр", None))
        self.actParCond.setText(_translate("fmProtokol", "Кондуктометр", None))
        self.actParTP.setText(_translate("fmProtokol", "Измеритель давления", None))
        self.actParAmper.setText(_translate("fmProtokol", "Микроамперметр", None))

