# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\ormet\source\svi_vs_v.0.4\forms\SelectConfig.ui'
#
# Created: Mon Jul 21 15:52:24 2014
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

class Ui_fmSelectConfig(object):
    def setupUi(self, fmSelectConfig):
        fmSelectConfig.setObjectName(_fromUtf8("fmSelectConfig"))
        fmSelectConfig.resize(397, 305)
        self.centralwidget = QtGui.QWidget(fmSelectConfig)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.twMeas = QtGui.QTreeWidget(self.centralwidget)
        self.twMeas.setGeometry(QtCore.QRect(790, 450, 292, 221))
        self.twMeas.setFrameShadow(QtGui.QFrame.Sunken)
        self.twMeas.setLineWidth(1)
        self.twMeas.setObjectName(_fromUtf8("twMeas"))
        self.twMeas.headerItem().setText(0, _fromUtf8("1"))
        self.twMeas.header().setVisible(False)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 10, 292, 14))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.tbDelCh = QtGui.QToolButton(self.centralwidget)
        self.tbDelCh.setGeometry(QtCore.QRect(240, 240, 78, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tbDelCh.setFont(font)
        self.tbDelCh.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.tbDelCh.setArrowType(QtCore.Qt.NoArrow)
        self.tbDelCh.setObjectName(_fromUtf8("tbDelCh"))
        self.lwVIns_3 = QtGui.QListWidget(self.centralwidget)
        self.lwVIns_3.setGeometry(QtCore.QRect(35, 30, 311, 191))
        self.lwVIns_3.setSelectionMode(QtGui.QAbstractItemView.MultiSelection)
        self.lwVIns_3.setObjectName(_fromUtf8("lwVIns_3"))
        self.tbSave = QtGui.QToolButton(self.centralwidget)
        self.tbSave.setGeometry(QtCore.QRect(50, 240, 78, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tbSave.setFont(font)
        self.tbSave.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.tbSave.setArrowType(QtCore.Qt.NoArrow)
        self.tbSave.setObjectName(_fromUtf8("tbSave"))
        fmSelectConfig.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(fmSelectConfig)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 397, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        fmSelectConfig.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(fmSelectConfig)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        fmSelectConfig.setStatusBar(self.statusbar)

        self.retranslateUi(fmSelectConfig)
        QtCore.QMetaObject.connectSlotsByName(fmSelectConfig)

    def retranslateUi(self, fmSelectConfig):
        fmSelectConfig.setWindowTitle(_translate("fmSelectConfig", "MainWindow", None))
        self.label.setText(_translate("fmSelectConfig", "Выбор конфигурации", None))
        self.tbDelCh.setText(_translate("fmSelectConfig", "Изменить", None))
        self.tbSave.setText(_translate("fmSelectConfig", "Выбрать", None))

