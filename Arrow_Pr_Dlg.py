# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\MessSys\sv_new2VP\forms\Arrow_Pr_Dlg.ui'
#
# Created: Wed Mar 11 16:36:46 2020
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

class Ui_Arrow_Pr_Dlg(object):
    def setupUi(self, Arrow_Pr_Dlg):
        Arrow_Pr_Dlg.setObjectName(_fromUtf8("Arrow_Pr_Dlg"))
        Arrow_Pr_Dlg.resize(279, 249)
        self.groupBox = QtGui.QGroupBox(Arrow_Pr_Dlg)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 221, 61))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.rbStripType = QtGui.QRadioButton(self.groupBox)
        self.rbStripType.setGeometry(QtCore.QRect(10, 20, 83, 18))
        self.rbStripType.setObjectName(_fromUtf8("rbStripType"))
        self.rbAngleType = QtGui.QRadioButton(self.groupBox)
        self.rbAngleType.setGeometry(QtCore.QRect(10, 40, 83, 18))
        self.rbAngleType.setObjectName(_fromUtf8("rbAngleType"))
        self.label_2 = QtGui.QLabel(Arrow_Pr_Dlg)
        self.label_2.setGeometry(QtCore.QRect(30, 90, 111, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Arrow_Pr_Dlg)
        self.label_3.setGeometry(QtCore.QRect(30, 120, 111, 16))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.leMidVal = QtGui.QLineEdit(Arrow_Pr_Dlg)
        self.leMidVal.setGeometry(QtCore.QRect(150, 90, 71, 20))
        self.leMidVal.setObjectName(_fromUtf8("leMidVal"))
        self.leDeltaVal = QtGui.QLineEdit(Arrow_Pr_Dlg)
        self.leDeltaVal.setGeometry(QtCore.QRect(150, 120, 71, 20))
        self.leDeltaVal.setObjectName(_fromUtf8("leDeltaVal"))
        self.btnSave = QtGui.QPushButton(Arrow_Pr_Dlg)
        self.btnSave.setGeometry(QtCore.QRect(90, 190, 75, 23))
        self.btnSave.setObjectName(_fromUtf8("btnSave"))

        self.retranslateUi(Arrow_Pr_Dlg)
        QtCore.QMetaObject.connectSlotsByName(Arrow_Pr_Dlg)

    def retranslateUi(self, Arrow_Pr_Dlg):
        Arrow_Pr_Dlg.setWindowTitle(_translate("Arrow_Pr_Dlg", "Dialog", None))
        self.groupBox.setTitle(_translate("Arrow_Pr_Dlg", "Тип прибора", None))
        self.rbStripType.setText(_translate("Arrow_Pr_Dlg", "Полоса", None))
        self.rbAngleType.setText(_translate("Arrow_Pr_Dlg", "Угол", None))
        self.label_2.setText(_translate("Arrow_Pr_Dlg", "Среднее значение", None))
        self.label_3.setText(_translate("Arrow_Pr_Dlg", "Отклонение", None))
        self.btnSave.setText(_translate("Arrow_Pr_Dlg", "Сохранить", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Arrow_Pr_Dlg = QtGui.QDialog()
    ui = Ui_Arrow_Pr_Dlg()
    ui.setupUi(Arrow_Pr_Dlg)
    Arrow_Pr_Dlg.show()
    sys.exit(app.exec_())

