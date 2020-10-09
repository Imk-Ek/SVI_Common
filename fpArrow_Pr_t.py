# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\MessSys\sv_new2VP\forms\fpArrow_Pr.ui'
#
# Created: Wed Mar 11 11:00:21 2020
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

class Ui_fpArrow_Pr(object):
    def setupUi(self, fpArrow_Pr):
        fpArrow_Pr.setObjectName(_fromUtf8("fpArrow_Pr"))
        fpArrow_Pr.setEnabled(True)
        fpArrow_Pr.resize(289, 342)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(fpArrow_Pr.sizePolicy().hasHeightForWidth())
        fpArrow_Pr.setSizePolicy(sizePolicy)
        self.centralwidget = QtGui.QWidget(fpArrow_Pr)
        self.centralwidget.setEnabled(True)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        fpArrow_Pr.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(fpArrow_Pr)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 289, 22))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        fpArrow_Pr.setMenuBar(self.menubar)

        self.retranslateUi(fpArrow_Pr)
        QtCore.QMetaObject.connectSlotsByName(fpArrow_Pr)

    def retranslateUi(self, fpArrow_Pr):
        fpArrow_Pr.setWindowTitle(_translate("fpArrow_Pr", "Регистратор", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    fpArrow_Pr = QtGui.QMainWindow()
    ui = Ui_fpArrow_Pr()
    ui.setupUi(fpArrow_Pr)
    fpArrow_Pr.show()
    sys.exit(app.exec_())

