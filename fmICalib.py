# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\ormet\source\svi_meteo_19_11_2015\svi\forms\fmICalib.ui'
#
# Created: Fri Nov 20 13:54:42 2015
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

class Ui_fmICalib(object):
    def setupUi(self, fmICalib):
        fmICalib.setObjectName(_fromUtf8("fmICalib"))
        fmICalib.resize(581, 484)
        self.centralwidget = QtGui.QWidget(fmICalib)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.teCalib = QtGui.QTableWidget(self.centralwidget)
        self.teCalib.setGeometry(QtCore.QRect(10, 110, 341, 192))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.teCalib.setFont(font)
        self.teCalib.setObjectName(_fromUtf8("teCalib"))
        self.teCalib.setColumnCount(3)
        self.teCalib.setRowCount(3)
        item = QtGui.QTableWidgetItem()
        self.teCalib.setVerticalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.teCalib.setVerticalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.teCalib.setVerticalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.teCalib.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.teCalib.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.teCalib.setHorizontalHeaderItem(2, item)
        self.leZero = QtGui.QLineEdit(self.centralwidget)
        self.leZero.setGeometry(QtCore.QRect(230, 78, 81, 22))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.leZero.setFont(font)
        self.leZero.setObjectName(_fromUtf8("leZero"))
        self.label_13 = QtGui.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(10, 79, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_13.setFont(font)
        self.label_13.setLineWidth(-5)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.lepXu = QtGui.QLineEdit(self.centralwidget)
        self.lepXu.setGeometry(QtCore.QRect(50, 78, 81, 22))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lepXu.setFont(font)
        self.lepXu.setObjectName(_fromUtf8("lepXu"))
        self.label_14 = QtGui.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(190, 79, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_14.setFont(font)
        self.label_14.setLineWidth(-5)
        self.label_14.setObjectName(_fromUtf8("label_14"))
        self.label_15 = QtGui.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(317, 79, 31, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_15.setFont(font)
        self.label_15.setLineWidth(-5)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(0, 367, 341, 81))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label_37 = QtGui.QLabel(self.groupBox)
        self.label_37.setGeometry(QtCore.QRect(10, 60, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_37.setFont(font)
        self.label_37.setLineWidth(-5)
        self.label_37.setObjectName(_fromUtf8("label_37"))
        self.leProfilName_ = QtGui.QLineEdit(self.groupBox)
        self.leProfilName_.setEnabled(False)
        self.leProfilName_.setGeometry(QtCore.QRect(140, 20, 191, 22))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.leProfilName_.setFont(font)
        self.leProfilName_.setObjectName(_fromUtf8("leProfilName_"))
        self.label_40 = QtGui.QLabel(self.groupBox)
        self.label_40.setGeometry(QtCore.QRect(10, 20, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_40.setFont(font)
        self.label_40.setLineWidth(-5)
        self.label_40.setObjectName(_fromUtf8("label_40"))
        self.leDescr_ = QtGui.QLineEdit(self.groupBox)
        self.leDescr_.setGeometry(QtCore.QRect(140, 50, 191, 22))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.leDescr_.setFont(font)
        self.leDescr_.setObjectName(_fromUtf8("leDescr_"))
        self.tbSaveProfilIon = QtGui.QToolButton(self.centralwidget)
        self.tbSaveProfilIon.setGeometry(QtCore.QRect(10, 337, 341, 22))
        self.tbSaveProfilIon.setObjectName(_fromUtf8("tbSaveProfilIon"))
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 0, 341, 51))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.tbSelectIon = QtGui.QToolButton(self.groupBox_2)
        self.tbSelectIon.setGeometry(QtCore.QRect(10, 19, 151, 22))
        self.tbSelectIon.setObjectName(_fromUtf8("tbSelectIon"))
        self.tbGrad = QtGui.QToolButton(self.groupBox_2)
        self.tbGrad.setGeometry(QtCore.QRect(180, 19, 151, 22))
        self.tbGrad.setObjectName(_fromUtf8("tbGrad"))
        self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(360, 0, 211, 111))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.label_4 = QtGui.QLabel(self.groupBox_3)
        self.label_4.setGeometry(QtCore.QRect(10, 70, 141, 20))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(self.groupBox_3)
        self.label_5.setGeometry(QtCore.QRect(10, 20, 46, 13))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(self.groupBox_3)
        self.label_6.setGeometry(QtCore.QRect(10, 40, 91, 16))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.lblKIon = QtGui.QLabel(self.groupBox_3)
        self.lblKIon.setGeometry(QtCore.QRect(160, 70, 41, 20))
        self.lblKIon.setObjectName(_fromUtf8("lblKIon"))
        self.lblMol_Massa = QtGui.QLabel(self.groupBox_3)
        self.lblMol_Massa.setGeometry(QtCore.QRect(160, 40, 41, 16))
        self.lblMol_Massa.setObjectName(_fromUtf8("lblMol_Massa"))
        self.lblIon = QtGui.QLabel(self.groupBox_3)
        self.lblIon.setGeometry(QtCore.QRect(160, 20, 46, 13))
        self.lblIon.setObjectName(_fromUtf8("lblIon"))
        self.lblS = QtGui.QLabel(self.centralwidget)
        self.lblS.setGeometry(QtCore.QRect(448, 140, 31, 16))
        self.lblS.setObjectName(_fromUtf8("lblS"))
        self.label_7 = QtGui.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(370, 140, 81, 16))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.lblIon_3 = QtGui.QLabel(self.centralwidget)
        self.lblIon_3.setGeometry(QtCore.QRect(490, 140, 31, 16))
        self.lblIon_3.setObjectName(_fromUtf8("lblIon_3"))
        self.label_8 = QtGui.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(10, 56, 151, 16))
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.leS_min = QtGui.QLineEdit(self.centralwidget)
        self.leS_min.setGeometry(QtCore.QRect(410, 202, 81, 22))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.leS_min.setFont(font)
        self.leS_min.setObjectName(_fromUtf8("leS_min"))
        self.label_16 = QtGui.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(370, 203, 51, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_16.setFont(font)
        self.label_16.setLineWidth(-5)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(370, 180, 151, 16))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.tbAddRow = QtGui.QToolButton(self.centralwidget)
        self.tbAddRow.setGeometry(QtCore.QRect(10, 310, 101, 22))
        self.tbAddRow.setObjectName(_fromUtf8("tbAddRow"))
        self.tbDelRow = QtGui.QToolButton(self.centralwidget)
        self.tbDelRow.setGeometry(QtCore.QRect(120, 310, 101, 22))
        self.tbDelRow.setObjectName(_fromUtf8("tbDelRow"))
        fmICalib.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(fmICalib)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 581, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.muProf = QtGui.QMenu(self.menubar)
        self.muProf.setObjectName(_fromUtf8("muProf"))
        self.muTabl = QtGui.QMenu(self.menubar)
        self.muTabl.setObjectName(_fromUtf8("muTabl"))
        fmICalib.setMenuBar(self.menubar)
        self.actTIns = QtGui.QAction(fmICalib)
        self.actTIns.setObjectName(_fromUtf8("actTIns"))
        self.actTDel = QtGui.QAction(fmICalib)
        self.actTDel.setObjectName(_fromUtf8("actTDel"))
        self.actPrIns = QtGui.QAction(fmICalib)
        self.actPrIns.setObjectName(_fromUtf8("actPrIns"))
        self.actPrDel = QtGui.QAction(fmICalib)
        self.actPrDel.setObjectName(_fromUtf8("actPrDel"))
        self.actPrRen = QtGui.QAction(fmICalib)
        self.actPrRen.setObjectName(_fromUtf8("actPrRen"))
        self.menubar.addAction(self.muProf.menuAction())
        self.menubar.addAction(self.muTabl.menuAction())

        self.retranslateUi(fmICalib)
        QtCore.QMetaObject.connectSlotsByName(fmICalib)

    def retranslateUi(self, fmICalib):
        fmICalib.setWindowTitle(_translate("fmICalib", "Градуировка", None))
        item = self.teCalib.verticalHeaderItem(0)
        item.setText(_translate("fmICalib", "1", None))
        item = self.teCalib.verticalHeaderItem(1)
        item.setText(_translate("fmICalib", "2", None))
        item = self.teCalib.verticalHeaderItem(2)
        item.setText(_translate("fmICalib", "3", None))
        item = self.teCalib.horizontalHeaderItem(0)
        item.setText(_translate("fmICalib", "pX", None))
        item = self.teCalib.horizontalHeaderItem(1)
        item.setText(_translate("fmICalib", "Напряжение [мВ]", None))
        item = self.teCalib.horizontalHeaderItem(2)
        item.setText(_translate("fmICalib", "Отклонение [мВ]", None))
        self.label_13.setText(_translate("fmICalib", "pH<sub>и</sub>=", None))
        self.label_14.setText(_translate("fmICalib", "E<sub>и</sub>=", None))
        self.label_15.setText(_translate("fmICalib", "[мВ]", None))
        self.groupBox.setTitle(_translate("fmICalib", "Изменение наименования профиля", None))
        self.label_37.setText(_translate("fmICalib", " Описание профиля", None))
        self.label_40.setText(_translate("fmICalib", "Профиль измерения", None))
        self.tbSaveProfilIon.setText(_translate("fmICalib", "Сохранить профиль", None))
        self.groupBox_2.setTitle(_translate("fmICalib", "Автоматическая градуировка", None))
        self.tbSelectIon.setText(_translate("fmICalib", "Выбор иона", None))
        self.tbGrad.setText(_translate("fmICalib", "Градуировка", None))
        self.groupBox_3.setTitle(_translate("fmICalib", "Характеристики иона", None))
        self.label_4.setText(_translate("fmICalib", "Коэффициент активности", None))
        self.label_5.setText(_translate("fmICalib", "Ион", None))
        self.label_6.setText(_translate("fmICalib", "Молярная масса", None))
        self.lblKIon.setText(_translate("fmICalib", "-", None))
        self.lblMol_Massa.setText(_translate("fmICalib", "-", None))
        self.lblIon.setText(_translate("fmICalib", "-", None))
        self.lblS.setText(_translate("fmICalib", "_", None))
        self.label_7.setText(_translate("fmICalib", "Крутизна S=", None))
        self.lblIon_3.setText(_translate("fmICalib", "мВ/pH", None))
        self.label_8.setText(_translate("fmICalib", "Изопотенциальная  точка:", None))
        self.label_16.setText(_translate("fmICalib", "<html><head/><body><p>S<span style=\" vertical-align:sub;\">min</span>=</p></body></html>", None))
        self.label_9.setText(_translate("fmICalib", "Минимальная крутизна", None))
        self.tbAddRow.setText(_translate("fmICalib", "Добавить строку", None))
        self.tbDelRow.setText(_translate("fmICalib", "Удалить строку", None))
        self.muProf.setTitle(_translate("fmICalib", "Профиль", None))
        self.muTabl.setTitle(_translate("fmICalib", "Таблица", None))
        self.actTIns.setText(_translate("fmICalib", "Вставить строку", None))
        self.actTDel.setText(_translate("fmICalib", "Удалить строку", None))
        self.actPrIns.setText(_translate("fmICalib", "Новый профиль", None))
        self.actPrDel.setText(_translate("fmICalib", "Удалить профиль", None))
        self.actPrRen.setText(_translate("fmICalib", "Переименовать профиль", None))

