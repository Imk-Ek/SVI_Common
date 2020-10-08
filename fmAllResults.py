# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\ormet\source\svi_vs_v.0.4\forms\fmAllResults.ui'
#
# Created: Thu Jul 17 13:34:24 2014
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
        fmNaladka.resize(535, 313)
        self.centralwidget = QtGui.QWidget(fmNaladka)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_2 = QtGui.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 2, 1, 1)
        self.twMeas = QtGui.QTreeWidget(self.centralwidget)
        self.twMeas.setFrameShadow(QtGui.QFrame.Sunken)
        self.twMeas.setLineWidth(1)
        self.twMeas.setObjectName(_fromUtf8("twMeas"))
        self.twMeas.headerItem().setText(0, _fromUtf8("1"))
        self.twMeas.header().setVisible(False)
        self.gridLayout.addWidget(self.twMeas, 1, 0, 1, 1)
        spacerItem = QtGui.QSpacerItem(20, 50, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 1, 1, 1, 1)
        self.lwVIns = QtGui.QListWidget(self.centralwidget)
        self.lwVIns.setObjectName(_fromUtf8("lwVIns"))
        self.gridLayout.addWidget(self.lwVIns, 1, 2, 1, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.tbStart = QtGui.QToolButton(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tbStart.setFont(font)
        self.tbStart.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.tbStart.setArrowType(QtCore.Qt.NoArrow)
        self.tbStart.setObjectName(_fromUtf8("tbStart"))
        self.horizontalLayout.addWidget(self.tbStart)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 3)
        fmNaladka.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(fmNaladka)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 535, 21))
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
        self.actParAmper = QtGui.QAction(fmNaladka)
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

        self.retranslateUi(fmNaladka)
        QtCore.QMetaObject.connectSlotsByName(fmNaladka)

    def retranslateUi(self, fmNaladka):
        fmNaladka.setWindowTitle(_translate("fmNaladka", "СВП Ормет - режим наладки", None))
        self.label.setText(_translate("fmNaladka", "Измерители", None))
        self.label_2.setText(_translate("fmNaladka", "Виртуальные приборы", None))
        self.tbStart.setText(_translate("fmNaladka", "Запуск СВП", None))
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
        self.actParAmper.setText(_translate("fmNaladka", "Микроамперметр", None))

