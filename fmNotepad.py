# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\ormet\source\svi_vs_v.0.4\forms\fmNotepad.ui'
#
# Created: Wed Feb 11 15:11:38 2015
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

class Ui_fmNotepad(object):
    def setupUi(self, fmNotepad):
        fmNotepad.setObjectName(_fromUtf8("fmNotepad"))
        fmNotepad.setEnabled(True)
        fmNotepad.resize(289, 342)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(fmNotepad.sizePolicy().hasHeightForWidth())
        fmNotepad.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(fmNotepad)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_34 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_34.setFont(font)
        self.label_34.setLineWidth(-5)
        self.label_34.setObjectName(_fromUtf8("label_34"))
        self.gridLayout.addWidget(self.label_34, 0, 0, 1, 3)
        self.lblDateTime = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblDateTime.setFont(font)
        self.lblDateTime.setLineWidth(-5)
        self.lblDateTime.setObjectName(_fromUtf8("lblDateTime"))
        self.gridLayout.addWidget(self.lblDateTime, 1, 0, 1, 3)
        self.tableW = QtGui.QTableWidget(self.centralwidget)
        self.tableW.setEnabled(True)
        self.tableW.setObjectName(_fromUtf8("tableW"))
        self.tableW.setColumnCount(0)
        self.tableW.setRowCount(0)
        self.gridLayout.addWidget(self.tableW, 2, 0, 1, 5)
        spacerItem = QtGui.QSpacerItem(8, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 3, 0, 1, 1)
        self.btnSave = QtGui.QPushButton(self.centralwidget)
        self.btnSave.setEnabled(True)
        self.btnSave.setObjectName(_fromUtf8("btnSave"))
        self.gridLayout.addWidget(self.btnSave, 3, 1, 1, 2)
        self.btnClear = QtGui.QPushButton(self.centralwidget)
        self.btnClear.setEnabled(True)
        self.btnClear.setObjectName(_fromUtf8("btnClear"))
        self.gridLayout.addWidget(self.btnClear, 3, 3, 1, 2)
        spacerItem1 = QtGui.QSpacerItem(13, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 3, 5, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(49, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 4, 0, 1, 2)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 4, 2, 1, 1)
        self.spinBox = QtGui.QSpinBox(self.centralwidget)
        self.spinBox.setEnabled(True)
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.gridLayout.addWidget(self.spinBox, 4, 3, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(30, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem3, 4, 4, 1, 1)
        fmNotepad.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(fmNotepad)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 289, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.muSetting = QtGui.QMenu(self.menubar)
        self.muSetting.setObjectName(_fromUtf8("muSetting"))
        self.muAbout = QtGui.QMenu(self.menubar)
        self.muAbout.setObjectName(_fromUtf8("muAbout"))
        fmNotepad.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(fmNotepad)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        fmNotepad.setStatusBar(self.statusbar)
        self.actPortCons = QtGui.QAction(fmNotepad)
        self.actPortCons.setObjectName(_fromUtf8("actPortCons"))
        self.actMBCons = QtGui.QAction(fmNotepad)
        self.actMBCons.setObjectName(_fromUtf8("actMBCons"))
        self.actAD779x = QtGui.QAction(fmNotepad)
        self.actAD779x.setObjectName(_fromUtf8("actAD779x"))
        self.actParV = QtGui.QAction(fmNotepad)
        self.actParV.setObjectName(_fromUtf8("actParV"))
        self.actParT = QtGui.QAction(fmNotepad)
        self.actParT.setObjectName(_fromUtf8("actParT"))
        self.actParCond = QtGui.QAction(fmNotepad)
        self.actParCond.setObjectName(_fromUtf8("actParCond"))
        self.actParTP = QtGui.QAction(fmNotepad)
        self.actParTP.setObjectName(_fromUtf8("actParTP"))
        self.actParAmper = QtGui.QAction(fmNotepad)
        self.actParAmper.setObjectName(_fromUtf8("actParAmper"))
        self.menubar.addAction(self.muSetting.menuAction())
        self.menubar.addAction(self.muAbout.menuAction())

        self.retranslateUi(fmNotepad)
        QtCore.QMetaObject.connectSlotsByName(fmNotepad)

    def retranslateUi(self, fmNotepad):
        fmNotepad.setWindowTitle(_translate("fmNotepad", "Регистратор", None))
        self.label_34.setText(_translate("fmNotepad", "Дата и время", None))
        self.lblDateTime.setText(_translate("fmNotepad", "11.11.2011 11-11-11", None))
        self.btnSave.setText(_translate("fmNotepad", "Сохранить", None))
        self.btnClear.setText(_translate("fmNotepad", "Очистить", None))
        self.label.setText(_translate("fmNotepad", "Интервал сохранения, с", None))
        self.muSetting.setTitle(_translate("fmNotepad", "Настройка", None))
        self.muAbout.setTitle(_translate("fmNotepad", "?", None))
        self.actPortCons.setText(_translate("fmNotepad", "Консоль порта...", None))
        self.actMBCons.setText(_translate("fmNotepad", "Консоль драйвера ...", None))
        self.actAD779x.setText(_translate("fmNotepad", "AD779x...", None))
        self.actParV.setText(_translate("fmNotepad", "Милливольтметр", None))
        self.actParT.setText(_translate("fmNotepad", "Термометр", None))
        self.actParCond.setText(_translate("fmNotepad", "Кондуктометр", None))
        self.actParTP.setText(_translate("fmNotepad", "Измеритель давления", None))
        self.actParAmper.setText(_translate("fmNotepad", "Микроамперметр", None))

