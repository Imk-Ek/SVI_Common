# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\__2018\NB2\svi\forms\fmNotepad.ui'
#
# Created: Wed Sep 19 16:25:22 2018
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
        fmNotepad.resize(654, 622)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(fmNotepad.sizePolicy().hasHeightForWidth())
        fmNotepad.setSizePolicy(sizePolicy)
        fmNotepad.setMinimumSize(QtCore.QSize(654, 622))
        self.centralwidget = QtGui.QWidget(fmNotepad)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.formLayout = QtGui.QFormLayout(self.centralwidget)
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label_34 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_34.setFont(font)
        self.label_34.setLineWidth(-5)
        self.label_34.setObjectName(_fromUtf8("label_34"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label_34)
        self.lblDateTime = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblDateTime.setFont(font)
        self.lblDateTime.setLineWidth(-5)
        self.lblDateTime.setObjectName(_fromUtf8("lblDateTime"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.lblDateTime)
        self.tableW = QtGui.QTableWidget(self.centralwidget)
        self.tableW.setEnabled(True)
        self.tableW.setMinimumSize(QtCore.QSize(611, 321))
        self.tableW.setObjectName(_fromUtf8("tableW"))
        self.tableW.setColumnCount(0)
        self.tableW.setRowCount(0)
        self.formLayout.setWidget(2, QtGui.QFormLayout.SpanningRole, self.tableW)
        self.btnSave = QtGui.QPushButton(self.centralwidget)
        self.btnSave.setEnabled(True)
        self.btnSave.setMinimumSize(QtCore.QSize(150, 50))
        self.btnSave.setMaximumSize(QtCore.QSize(150, 50))
        self.btnSave.setObjectName(_fromUtf8("btnSave"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.btnSave)
        self.btnClear = QtGui.QPushButton(self.centralwidget)
        self.btnClear.setEnabled(True)
        self.btnClear.setMinimumSize(QtCore.QSize(150, 50))
        self.btnClear.setMaximumSize(QtCore.QSize(150, 50))
        self.btnClear.setObjectName(_fromUtf8("btnClear"))
        self.formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.btnClear)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setEnabled(True)
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.label)
        self.spinBox = QtGui.QLineEdit(self.centralwidget)
        self.spinBox.setMinimumSize(QtCore.QSize(113, 41))
        self.spinBox.setMaximumSize(QtCore.QSize(113, 41))
        self.spinBox.setObjectName(_fromUtf8("spinBox"))
        self.formLayout.setWidget(4, QtGui.QFormLayout.FieldRole, self.spinBox)
        fmNotepad.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(fmNotepad)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 654, 38))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.muSetting = QtGui.QMenu(self.menubar)
        self.muSetting.setObjectName(_fromUtf8("muSetting"))
        self.muAbout = QtGui.QMenu(self.menubar)
        self.muAbout.setObjectName(_fromUtf8("muAbout"))
        fmNotepad.setMenuBar(self.menubar)
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
        self.spinBox.setText(_translate("fmNotepad", "1", None))
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

