# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fmMain.ui'
#
# Created: Wed Jul 31 17:27:48 2013
#      by: PyQt4 UI code generator 4.9.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_fmMain(object):
    def setupUi(self, fmMain):
        fmMain.setObjectName(_fromUtf8("fmMain"))
        fmMain.resize(446, 293)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(fmMain.sizePolicy().hasHeightForWidth())
        fmMain.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(fmMain)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.gridLayout.setSpacing(4)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        fmMain.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(fmMain)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 446, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.muAbout = QtGui.QMenu(self.menubar)
        self.muAbout.setObjectName(_fromUtf8("muAbout"))
        fmMain.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(fmMain)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        fmMain.setStatusBar(self.statusbar)
        self.menubar.addAction(self.muAbout.menuAction())

        self.retranslateUi(fmMain)
        QtCore.QMetaObject.connectSlotsByName(fmMain)

    def retranslateUi(self, fmMain):
        fmMain.setWindowTitle(QtGui.QApplication.translate("fmMain", "СВП Ормет", None, QtGui.QApplication.UnicodeUTF8))
        self.muAbout.setTitle(QtGui.QApplication.translate("fmMain", "?", None, QtGui.QApplication.UnicodeUTF8))

