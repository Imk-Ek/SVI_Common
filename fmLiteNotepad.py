# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\ormet\source\svi_vs_v.0.4\forms\fmLiteNotepad.ui'
#
# Created: Mon Mar 23 10:29:53 2015
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

class Ui_fmLiteNotepad(object):
    def setupUi(self, fmLiteNotepad):
        fmLiteNotepad.setObjectName(_fromUtf8("fmLiteNotepad"))
        fmLiteNotepad.setEnabled(True)
        fmLiteNotepad.resize(255, 216)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(fmLiteNotepad.sizePolicy().hasHeightForWidth())
        fmLiteNotepad.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(fmLiteNotepad)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tableW = QtGui.QTableWidget(self.centralwidget)
        self.tableW.setEnabled(True)
        self.tableW.setObjectName(_fromUtf8("tableW"))
        self.tableW.setColumnCount(0)
        self.tableW.setRowCount(0)
        self.gridLayout.addWidget(self.tableW, 0, 0, 1, 3)
        self.btnSave = QtGui.QPushButton(self.centralwidget)
        self.btnSave.setEnabled(True)
        self.btnSave.setObjectName(_fromUtf8("btnSave"))
        self.gridLayout.addWidget(self.btnSave, 1, 0, 1, 1)
        self.btnDel = QtGui.QPushButton(self.centralwidget)
        self.btnDel.setEnabled(True)
        self.btnDel.setObjectName(_fromUtf8("btnDel"))
        self.gridLayout.addWidget(self.btnDel, 1, 1, 1, 1)
        self.btnClear = QtGui.QPushButton(self.centralwidget)
        self.btnClear.setEnabled(True)
        self.btnClear.setObjectName(_fromUtf8("btnClear"))
        self.gridLayout.addWidget(self.btnClear, 1, 2, 1, 1)
        fmLiteNotepad.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(fmLiteNotepad)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 255, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.muSetting = QtGui.QMenu(self.menubar)
        self.muSetting.setObjectName(_fromUtf8("muSetting"))
        self.muAbout = QtGui.QMenu(self.menubar)
        self.muAbout.setObjectName(_fromUtf8("muAbout"))
        fmLiteNotepad.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(fmLiteNotepad)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        fmLiteNotepad.setStatusBar(self.statusbar)
        self.actPortCons = QtGui.QAction(fmLiteNotepad)
        self.actPortCons.setObjectName(_fromUtf8("actPortCons"))
        self.actMBCons = QtGui.QAction(fmLiteNotepad)
        self.actMBCons.setObjectName(_fromUtf8("actMBCons"))
        self.actAD779x = QtGui.QAction(fmLiteNotepad)
        self.actAD779x.setObjectName(_fromUtf8("actAD779x"))
        self.actParV = QtGui.QAction(fmLiteNotepad)
        self.actParV.setObjectName(_fromUtf8("actParV"))
        self.actParT = QtGui.QAction(fmLiteNotepad)
        self.actParT.setObjectName(_fromUtf8("actParT"))
        self.actParCond = QtGui.QAction(fmLiteNotepad)
        self.actParCond.setObjectName(_fromUtf8("actParCond"))
        self.actParTP = QtGui.QAction(fmLiteNotepad)
        self.actParTP.setObjectName(_fromUtf8("actParTP"))
        self.actParAmper = QtGui.QAction(fmLiteNotepad)
        self.actParAmper.setObjectName(_fromUtf8("actParAmper"))
        self.menubar.addAction(self.muSetting.menuAction())
        self.menubar.addAction(self.muAbout.menuAction())

        self.retranslateUi(fmLiteNotepad)
        QtCore.QMetaObject.connectSlotsByName(fmLiteNotepad)

    def retranslateUi(self, fmLiteNotepad):
        fmLiteNotepad.setWindowTitle(_translate("fmLiteNotepad", "Блокнот", None))
        self.btnSave.setText(_translate("fmLiteNotepad", "Сохранить", None))
        self.btnDel.setText(_translate("fmLiteNotepad", "Удалить", None))
        self.btnClear.setText(_translate("fmLiteNotepad", "Очистить", None))
        self.muSetting.setTitle(_translate("fmLiteNotepad", "Настройка", None))
        self.muAbout.setTitle(_translate("fmLiteNotepad", "?", None))
        self.actPortCons.setText(_translate("fmLiteNotepad", "Консоль порта...", None))
        self.actMBCons.setText(_translate("fmLiteNotepad", "Консоль драйвера ...", None))
        self.actAD779x.setText(_translate("fmLiteNotepad", "AD779x...", None))
        self.actParV.setText(_translate("fmLiteNotepad", "Милливольтметр", None))
        self.actParT.setText(_translate("fmLiteNotepad", "Термометр", None))
        self.actParCond.setText(_translate("fmLiteNotepad", "Кондуктометр", None))
        self.actParTP.setText(_translate("fmLiteNotepad", "Измеритель давления", None))
        self.actParAmper.setText(_translate("fmLiteNotepad", "Микроамперметр", None))

