# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\__2018\NB2\svi\forms\fmIonDigitSelect.ui'
#
# Created: Tue Sep 18 14:22:27 2018
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

class Ui_fmIonDigitSelect(object):
    def setupUi(self, fmIonDigitSelect):
        fmIonDigitSelect.setObjectName(_fromUtf8("fmIonDigitSelect"))
        fmIonDigitSelect.resize(316, 450)
        fmIonDigitSelect.setMinimumSize(QtCore.QSize(316, 450))
        fmIonDigitSelect.setMaximumSize(QtCore.QSize(316, 450))
        self.tbSelectDigitIon = QtGui.QPushButton(fmIonDigitSelect)
        self.tbSelectDigitIon.setGeometry(QtCore.QRect(88, 279, 141, 51))
        self.tbSelectDigitIon.setObjectName(_fromUtf8("tbSelectDigitIon"))
        self.leIonDigitSelect_ = QtGui.QLineEdit(fmIonDigitSelect)
        self.leIonDigitSelect_.setGeometry(QtCore.QRect(100, 210, 113, 41))
        self.leIonDigitSelect_.setObjectName(_fromUtf8("leIonDigitSelect_"))
        self.twIonDigitSelect_ = QtGui.QTableWidget(fmIonDigitSelect)
        self.twIonDigitSelect_.setGeometry(QtCore.QRect(30, 20, 250, 150))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.twIonDigitSelect_.sizePolicy().hasHeightForWidth())
        self.twIonDigitSelect_.setSizePolicy(sizePolicy)
        self.twIonDigitSelect_.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.twIonDigitSelect_.setFont(font)
        self.twIonDigitSelect_.setFrameShape(QtGui.QFrame.StyledPanel)
        self.twIonDigitSelect_.setLineWidth(1)
        self.twIonDigitSelect_.setMidLineWidth(4)
        self.twIonDigitSelect_.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.twIonDigitSelect_.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.twIonDigitSelect_.setTextElideMode(QtCore.Qt.ElideNone)
        self.twIonDigitSelect_.setShowGrid(True)
        self.twIonDigitSelect_.setGridStyle(QtCore.Qt.SolidLine)
        self.twIonDigitSelect_.setWordWrap(False)
        self.twIonDigitSelect_.setCornerButtonEnabled(False)
        self.twIonDigitSelect_.setObjectName(_fromUtf8("twIonDigitSelect_"))
        self.twIonDigitSelect_.setColumnCount(0)
        self.twIonDigitSelect_.setRowCount(1)
        item = QtGui.QTableWidgetItem()
        self.twIonDigitSelect_.setVerticalHeaderItem(0, item)
        self.twIonDigitSelect_.horizontalHeader().setVisible(False)
        self.twIonDigitSelect_.horizontalHeader().setHighlightSections(False)
        self.twIonDigitSelect_.verticalHeader().setVisible(False)

        self.retranslateUi(fmIonDigitSelect)
        QtCore.QMetaObject.connectSlotsByName(fmIonDigitSelect)

    def retranslateUi(self, fmIonDigitSelect):
        fmIonDigitSelect.setWindowTitle(_translate("fmIonDigitSelect", "Dialog", None))
        self.tbSelectDigitIon.setText(_translate("fmIonDigitSelect", "Выбрать", None))
        item = self.twIonDigitSelect_.verticalHeaderItem(0)
        item.setText(_translate("fmIonDigitSelect", "New Row", None))

