# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\ormet\source\_IzmPr\svi_vs_v.0.6.7_u\forms\fmCondCalib1.ui'
#
# Created: Mon Nov 28 15:55:02 2016
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

class Ui_fmCondCalib(object):
    def setupUi(self, fmCondCalib):
        fmCondCalib.setObjectName(_fromUtf8("fmCondCalib"))
        fmCondCalib.resize(701, 495)
        fmCondCalib.setWindowOpacity(1.0)
        self.centralwidget = QtGui.QWidget(fmCondCalib)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tbSaveCalib_ = QtGui.QToolButton(self.centralwidget)
        self.tbSaveCalib_.setGeometry(QtCore.QRect(560, 433, 121, 22))
        self.tbSaveCalib_.setObjectName(_fromUtf8("tbSaveCalib_"))
        self.label_31 = QtGui.QLabel(self.centralwidget)
        self.label_31.setGeometry(QtCore.QRect(30, 10, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_31.setFont(font)
        self.label_31.setLineWidth(-5)
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.llCond_ = QtGui.QLabel(self.centralwidget)
        self.llCond_.setGeometry(QtCore.QRect(30, 70, 81, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.llCond_.setFont(font)
        self.llCond_.setFrameShape(QtGui.QFrame.Panel)
        self.llCond_.setFrameShadow(QtGui.QFrame.Sunken)
        self.llCond_.setText(_fromUtf8(""))
        self.llCond_.setObjectName(_fromUtf8("llCond_"))
        self.label_9 = QtGui.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(30, 50, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.lblCond_ed = QtGui.QLabel(self.centralwidget)
        self.lblCond_ed.setGeometry(QtCore.QRect(120, 70, 61, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblCond_ed.setFont(font)
        self.lblCond_ed.setText(_fromUtf8(""))
        self.lblCond_ed.setObjectName(_fromUtf8("lblCond_ed"))
        self.leAet_6 = QtGui.QLineEdit(self.centralwidget)
        self.leAet_6.setGeometry(QtCore.QRect(630, 840, 81, 22))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.leAet_6.setFont(font)
        self.leAet_6.setObjectName(_fromUtf8("leAet_6"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(9, 370, 461, 91))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.label_37 = QtGui.QLabel(self.groupBox)
        self.label_37.setGeometry(QtCore.QRect(10, 60, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_37.setFont(font)
        self.label_37.setLineWidth(-5)
        self.label_37.setObjectName(_fromUtf8("label_37"))
        self.leProfilName_ = QtGui.QLineEdit(self.groupBox)
        self.leProfilName_.setGeometry(QtCore.QRect(140, 20, 301, 22))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.leProfilName_.setFont(font)
        self.leProfilName_.setObjectName(_fromUtf8("leProfilName_"))
        self.leDescr_ = QtGui.QLineEdit(self.groupBox)
        self.leDescr_.setGeometry(QtCore.QRect(140, 61, 301, 22))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.leDescr_.setFont(font)
        self.leDescr_.setObjectName(_fromUtf8("leDescr_"))
        self.label_40 = QtGui.QLabel(self.groupBox)
        self.label_40.setGeometry(QtCore.QRect(10, 20, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_40.setFont(font)
        self.label_40.setLineWidth(-5)
        self.label_40.setObjectName(_fromUtf8("label_40"))
        self.gbxBKd = QtGui.QGroupBox(self.centralwidget)
        self.gbxBKd.setEnabled(False)
        self.gbxBKd.setGeometry(QtCore.QRect(0, 130, 681, 201))
        self.gbxBKd.setObjectName(_fromUtf8("gbxBKd"))
        self.lblKD4 = QtGui.QLabel(self.gbxBKd)
        self.lblKD4.setGeometry(QtCore.QRect(20, 114, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblKD4.setFont(font)
        self.lblKD4.setLineWidth(-5)
        self.lblKD4.setObjectName(_fromUtf8("lblKD4"))
        self.lblKD5 = QtGui.QLabel(self.gbxBKd)
        self.lblKD5.setGeometry(QtCore.QRect(20, 142, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblKD5.setFont(font)
        self.lblKD5.setLineWidth(-5)
        self.lblKD5.setObjectName(_fromUtf8("lblKD5"))
        self.lblKD6 = QtGui.QLabel(self.gbxBKd)
        self.lblKD6.setGeometry(QtCore.QRect(20, 172, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblKD6.setFont(font)
        self.lblKD6.setLineWidth(-5)
        self.lblKD6.setObjectName(_fromUtf8("lblKD6"))
        self.lblKD1 = QtGui.QLabel(self.gbxBKd)
        self.lblKD1.setGeometry(QtCore.QRect(20, 24, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblKD1.setFont(font)
        self.lblKD1.setLineWidth(-5)
        self.lblKD1.setObjectName(_fromUtf8("lblKD1"))
        self.lblKD3 = QtGui.QLabel(self.gbxBKd)
        self.lblKD3.setGeometry(QtCore.QRect(20, 84, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblKD3.setFont(font)
        self.lblKD3.setLineWidth(-5)
        self.lblKD3.setObjectName(_fromUtf8("lblKD3"))
        self.lblKD2 = QtGui.QLabel(self.gbxBKd)
        self.lblKD2.setGeometry(QtCore.QRect(20, 54, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblKD2.setFont(font)
        self.lblKD2.setLineWidth(-5)
        self.lblKD2.setObjectName(_fromUtf8("lblKD2"))
        self.leKu_5_ = QtGui.QDoubleSpinBox(self.gbxBKd)
        self.leKu_5_.setGeometry(QtCore.QRect(85, 137, 91, 21))
        self.leKu_5_.setDecimals(6)
        self.leKu_5_.setSingleStep(0.0001)
        self.leKu_5_.setObjectName(_fromUtf8("leKu_5_"))
        self.leKu_4_ = QtGui.QDoubleSpinBox(self.gbxBKd)
        self.leKu_4_.setGeometry(QtCore.QRect(85, 107, 91, 21))
        self.leKu_4_.setDecimals(6)
        self.leKu_4_.setSingleStep(0.0001)
        self.leKu_4_.setObjectName(_fromUtf8("leKu_4_"))
        self.leKu_6_ = QtGui.QDoubleSpinBox(self.gbxBKd)
        self.leKu_6_.setGeometry(QtCore.QRect(85, 167, 91, 21))
        self.leKu_6_.setDecimals(6)
        self.leKu_6_.setSingleStep(0.0001)
        self.leKu_6_.setObjectName(_fromUtf8("leKu_6_"))
        self.leKu_2_ = QtGui.QDoubleSpinBox(self.gbxBKd)
        self.leKu_2_.setGeometry(QtCore.QRect(85, 47, 91, 21))
        self.leKu_2_.setDecimals(6)
        self.leKu_2_.setSingleStep(0.0001)
        self.leKu_2_.setObjectName(_fromUtf8("leKu_2_"))
        self.leKu_1_ = QtGui.QDoubleSpinBox(self.gbxBKd)
        self.leKu_1_.setGeometry(QtCore.QRect(85, 19, 91, 21))
        self.leKu_1_.setDecimals(6)
        self.leKu_1_.setSingleStep(0.0001)
        self.leKu_1_.setObjectName(_fromUtf8("leKu_1_"))
        self.leKu_3_ = QtGui.QDoubleSpinBox(self.gbxBKd)
        self.leKu_3_.setGeometry(QtCore.QRect(85, 77, 91, 21))
        self.leKu_3_.setDecimals(6)
        self.leKu_3_.setSingleStep(0.0001)
        self.leKu_3_.setObjectName(_fromUtf8("leKu_3_"))
        self.label_48 = QtGui.QLabel(self.gbxBKd)
        self.label_48.setGeometry(QtCore.QRect(193, 169, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_48.setFont(font)
        self.label_48.setLineWidth(-5)
        self.label_48.setObjectName(_fromUtf8("label_48"))
        self.leB_6 = QtGui.QDoubleSpinBox(self.gbxBKd)
        self.leB_6.setGeometry(QtCore.QRect(230, 167, 181, 21))
        self.leB_6.setDecimals(16)
        self.leB_6.setMinimum(-1000000000.0)
        self.leB_6.setMaximum(1000000000.0)
        self.leB_6.setSingleStep(0.0001)
        self.leB_6.setObjectName(_fromUtf8("leB_6"))
        self.label_49 = QtGui.QLabel(self.gbxBKd)
        self.label_49.setGeometry(QtCore.QRect(192, 141, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_49.setFont(font)
        self.label_49.setLineWidth(-5)
        self.label_49.setObjectName(_fromUtf8("label_49"))
        self.leB_5 = QtGui.QDoubleSpinBox(self.gbxBKd)
        self.leB_5.setGeometry(QtCore.QRect(229, 139, 181, 21))
        self.leB_5.setDecimals(16)
        self.leB_5.setMinimum(-1000000000.0)
        self.leB_5.setMaximum(1000000000.0)
        self.leB_5.setSingleStep(0.0001)
        self.leB_5.setObjectName(_fromUtf8("leB_5"))
        self.label_50 = QtGui.QLabel(self.gbxBKd)
        self.label_50.setGeometry(QtCore.QRect(193, 112, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_50.setFont(font)
        self.label_50.setLineWidth(-5)
        self.label_50.setObjectName(_fromUtf8("label_50"))
        self.leB_4 = QtGui.QDoubleSpinBox(self.gbxBKd)
        self.leB_4.setGeometry(QtCore.QRect(230, 110, 181, 21))
        self.leB_4.setDecimals(16)
        self.leB_4.setMinimum(-1000000000.0)
        self.leB_4.setMaximum(1000000000.0)
        self.leB_4.setSingleStep(0.0001)
        self.leB_4.setObjectName(_fromUtf8("leB_4"))
        self.label_51 = QtGui.QLabel(self.gbxBKd)
        self.label_51.setGeometry(QtCore.QRect(193, 81, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_51.setFont(font)
        self.label_51.setLineWidth(-5)
        self.label_51.setObjectName(_fromUtf8("label_51"))
        self.leB_3 = QtGui.QDoubleSpinBox(self.gbxBKd)
        self.leB_3.setGeometry(QtCore.QRect(230, 79, 181, 21))
        self.leB_3.setDecimals(16)
        self.leB_3.setMinimum(-1000000000.0)
        self.leB_3.setMaximum(1000000000.0)
        self.leB_3.setSingleStep(0.0001)
        self.leB_3.setObjectName(_fromUtf8("leB_3"))
        self.label_52 = QtGui.QLabel(self.gbxBKd)
        self.label_52.setGeometry(QtCore.QRect(193, 49, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_52.setFont(font)
        self.label_52.setLineWidth(-5)
        self.label_52.setObjectName(_fromUtf8("label_52"))
        self.leB_2 = QtGui.QDoubleSpinBox(self.gbxBKd)
        self.leB_2.setGeometry(QtCore.QRect(230, 47, 181, 21))
        self.leB_2.setDecimals(16)
        self.leB_2.setMinimum(-1000000000.0)
        self.leB_2.setMaximum(1000000000.0)
        self.leB_2.setSingleStep(0.0001)
        self.leB_2.setObjectName(_fromUtf8("leB_2"))
        self.label_53 = QtGui.QLabel(self.gbxBKd)
        self.label_53.setGeometry(QtCore.QRect(193, 22, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_53.setFont(font)
        self.label_53.setLineWidth(-5)
        self.label_53.setObjectName(_fromUtf8("label_53"))
        self.leB_1 = QtGui.QDoubleSpinBox(self.gbxBKd)
        self.leB_1.setGeometry(QtCore.QRect(230, 20, 181, 21))
        self.leB_1.setDecimals(16)
        self.leB_1.setMinimum(-1000000000.0)
        self.leB_1.setMaximum(1000000000.0)
        self.leB_1.setSingleStep(0.0001)
        self.leB_1.setObjectName(_fromUtf8("leB_1"))
        self.label_54 = QtGui.QLabel(self.gbxBKd)
        self.label_54.setGeometry(QtCore.QRect(450, 169, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_54.setFont(font)
        self.label_54.setLineWidth(-5)
        self.label_54.setObjectName(_fromUtf8("label_54"))
        self.leA_1 = QtGui.QDoubleSpinBox(self.gbxBKd)
        self.leA_1.setGeometry(QtCore.QRect(487, 20, 181, 21))
        self.leA_1.setDecimals(16)
        self.leA_1.setMinimum(-1000000000.0)
        self.leA_1.setMaximum(1000000000.0)
        self.leA_1.setSingleStep(0.0001)
        self.leA_1.setObjectName(_fromUtf8("leA_1"))
        self.leA_6 = QtGui.QDoubleSpinBox(self.gbxBKd)
        self.leA_6.setGeometry(QtCore.QRect(487, 167, 181, 21))
        self.leA_6.setDecimals(16)
        self.leA_6.setMinimum(-1000000000.0)
        self.leA_6.setMaximum(1000000000.0)
        self.leA_6.setSingleStep(0.0001)
        self.leA_6.setObjectName(_fromUtf8("leA_6"))
        self.leA_2 = QtGui.QDoubleSpinBox(self.gbxBKd)
        self.leA_2.setGeometry(QtCore.QRect(487, 47, 181, 21))
        self.leA_2.setDecimals(16)
        self.leA_2.setMinimum(-1000000000.0)
        self.leA_2.setMaximum(1000000000.0)
        self.leA_2.setSingleStep(0.0001)
        self.leA_2.setObjectName(_fromUtf8("leA_2"))
        self.label_55 = QtGui.QLabel(self.gbxBKd)
        self.label_55.setGeometry(QtCore.QRect(450, 22, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_55.setFont(font)
        self.label_55.setLineWidth(-5)
        self.label_55.setObjectName(_fromUtf8("label_55"))
        self.label_56 = QtGui.QLabel(self.gbxBKd)
        self.label_56.setGeometry(QtCore.QRect(449, 141, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_56.setFont(font)
        self.label_56.setLineWidth(-5)
        self.label_56.setObjectName(_fromUtf8("label_56"))
        self.leA_5 = QtGui.QDoubleSpinBox(self.gbxBKd)
        self.leA_5.setGeometry(QtCore.QRect(486, 139, 181, 21))
        self.leA_5.setDecimals(16)
        self.leA_5.setMinimum(-1000000000.0)
        self.leA_5.setMaximum(1000000000.0)
        self.leA_5.setSingleStep(0.0001)
        self.leA_5.setObjectName(_fromUtf8("leA_5"))
        self.leA_4 = QtGui.QDoubleSpinBox(self.gbxBKd)
        self.leA_4.setGeometry(QtCore.QRect(487, 110, 181, 21))
        self.leA_4.setDecimals(16)
        self.leA_4.setMinimum(-1000000000.0)
        self.leA_4.setMaximum(1000000000.0)
        self.leA_4.setSingleStep(0.0001)
        self.leA_4.setObjectName(_fromUtf8("leA_4"))
        self.label_57 = QtGui.QLabel(self.gbxBKd)
        self.label_57.setGeometry(QtCore.QRect(450, 49, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_57.setFont(font)
        self.label_57.setLineWidth(-5)
        self.label_57.setObjectName(_fromUtf8("label_57"))
        self.label_58 = QtGui.QLabel(self.gbxBKd)
        self.label_58.setGeometry(QtCore.QRect(450, 112, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_58.setFont(font)
        self.label_58.setLineWidth(-5)
        self.label_58.setObjectName(_fromUtf8("label_58"))
        self.label_59 = QtGui.QLabel(self.gbxBKd)
        self.label_59.setGeometry(QtCore.QRect(450, 81, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_59.setFont(font)
        self.label_59.setLineWidth(-5)
        self.label_59.setObjectName(_fromUtf8("label_59"))
        self.leA_3 = QtGui.QDoubleSpinBox(self.gbxBKd)
        self.leA_3.setGeometry(QtCore.QRect(487, 79, 181, 21))
        self.leA_3.setDecimals(16)
        self.leA_3.setMinimum(-1000000000.0)
        self.leA_3.setMaximum(1000000000.0)
        self.leA_3.setSingleStep(0.0001)
        self.leA_3.setObjectName(_fromUtf8("leA_3"))
        self.chbBKd = QtGui.QCheckBox(self.centralwidget)
        self.chbBKd.setGeometry(QtCore.QRect(10, 100, 211, 21))
        self.chbBKd.setObjectName(_fromUtf8("chbBKd"))
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(130, 50, 211, 51))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.label_38 = QtGui.QLabel(self.groupBox_2)
        self.label_38.setGeometry(QtCore.QRect(46, 20, 31, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_38.setFont(font)
        self.label_38.setLineWidth(-5)
        self.label_38.setObjectName(_fromUtf8("label_38"))
        self.leKu_ = QtGui.QDoubleSpinBox(self.groupBox_2)
        self.leKu_.setGeometry(QtCore.QRect(80, 20, 91, 22))
        self.leKu_.setDecimals(3)
        self.leKu_.setSingleStep(0.001)
        self.leKu_.setObjectName(_fromUtf8("leKu_"))
        self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(350, 50, 341, 51))
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.label_39 = QtGui.QLabel(self.groupBox_3)
        self.label_39.setGeometry(QtCore.QRect(20, 20, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_39.setFont(font)
        self.label_39.setLineWidth(-5)
        self.label_39.setObjectName(_fromUtf8("label_39"))
        self.leCond_min = QtGui.QLineEdit(self.groupBox_3)
        self.leCond_min.setGeometry(QtCore.QRect(70, 20, 91, 22))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.leCond_min.setFont(font)
        self.leCond_min.setObjectName(_fromUtf8("leCond_min"))
        self.label_41 = QtGui.QLabel(self.groupBox_3)
        self.label_41.setGeometry(QtCore.QRect(190, 19, 51, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_41.setFont(font)
        self.label_41.setLineWidth(-5)
        self.label_41.setObjectName(_fromUtf8("label_41"))
        self.leCond_max = QtGui.QLineEdit(self.groupBox_3)
        self.leCond_max.setGeometry(QtCore.QRect(240, 19, 91, 22))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.leCond_max.setFont(font)
        self.leCond_max.setObjectName(_fromUtf8("leCond_max"))
        self.lblKD6_2 = QtGui.QLabel(self.centralwidget)
        self.lblKD6_2.setEnabled(False)
        self.lblKD6_2.setGeometry(QtCore.QRect(13, 343, 121, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lblKD6_2.setFont(font)
        self.lblKD6_2.setLineWidth(-5)
        self.lblKD6_2.setObjectName(_fromUtf8("lblKD6_2"))
        self.tbRecalc = QtGui.QToolButton(self.centralwidget)
        self.tbRecalc.setEnabled(False)
        self.tbRecalc.setGeometry(QtCore.QRect(270, 341, 121, 22))
        self.tbRecalc.setObjectName(_fromUtf8("tbRecalc"))
        self.leCondSet = QtGui.QLineEdit(self.centralwidget)
        self.leCondSet.setEnabled(False)
        self.leCondSet.setGeometry(QtCore.QRect(160, 340, 91, 22))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.leCondSet.setFont(font)
        self.leCondSet.setObjectName(_fromUtf8("leCondSet"))
        fmCondCalib.setCentralWidget(self.centralwidget)
        self.statusbar = QtGui.QStatusBar(fmCondCalib)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        fmCondCalib.setStatusBar(self.statusbar)
        self.actTIns = QtGui.QAction(fmCondCalib)
        self.actTIns.setObjectName(_fromUtf8("actTIns"))
        self.actTDel = QtGui.QAction(fmCondCalib)
        self.actTDel.setObjectName(_fromUtf8("actTDel"))
        self.actPrIns = QtGui.QAction(fmCondCalib)
        self.actPrIns.setObjectName(_fromUtf8("actPrIns"))
        self.actPrDel = QtGui.QAction(fmCondCalib)
        self.actPrDel.setObjectName(_fromUtf8("actPrDel"))
        self.actPrRen = QtGui.QAction(fmCondCalib)
        self.actPrRen.setObjectName(_fromUtf8("actPrRen"))

        self.retranslateUi(fmCondCalib)
        QtCore.QMetaObject.connectSlotsByName(fmCondCalib)

    def retranslateUi(self, fmCondCalib):
        fmCondCalib.setWindowTitle(_translate("fmCondCalib", "Градуировка", None))
        self.tbSaveCalib_.setText(_translate("fmCondCalib", "Сохранить", None))
        self.label_31.setText(_translate("fmCondCalib", "Профиль измерения", None))
        self.label_9.setText(_translate("fmCondCalib", "Проводимость", None))
        self.groupBox.setTitle(_translate("fmCondCalib", "Изменение наименования профиля", None))
        self.label_37.setText(_translate("fmCondCalib", " Описание профиля", None))
        self.label_40.setText(_translate("fmCondCalib", "Профиль измерения", None))
        self.gbxBKd.setTitle(_translate("fmCondCalib", "Коррекция нелинейности", None))
        self.lblKD4.setText(_translate("fmCondCalib", "Кд яч 4", None))
        self.lblKD5.setText(_translate("fmCondCalib", "Кд яч 5", None))
        self.lblKD6.setText(_translate("fmCondCalib", "Кд яч 6", None))
        self.lblKD1.setText(_translate("fmCondCalib", "<html><head/><body><p>Kд яч 1</p></body></html>", None))
        self.lblKD3.setText(_translate("fmCondCalib", "Kд яч 3", None))
        self.lblKD2.setText(_translate("fmCondCalib", "Kд яч 2", None))
        self.label_48.setText(_translate("fmCondCalib", "B 6", None))
        self.label_49.setText(_translate("fmCondCalib", "B 5", None))
        self.label_50.setText(_translate("fmCondCalib", "B 4", None))
        self.label_51.setText(_translate("fmCondCalib", "B 3", None))
        self.label_52.setText(_translate("fmCondCalib", "B 2", None))
        self.label_53.setText(_translate("fmCondCalib", "B 1", None))
        self.label_54.setText(_translate("fmCondCalib", "A 6", None))
        self.label_55.setText(_translate("fmCondCalib", "A 1", None))
        self.label_56.setText(_translate("fmCondCalib", "A 5", None))
        self.label_57.setText(_translate("fmCondCalib", "A 2", None))
        self.label_58.setText(_translate("fmCondCalib", "A 4", None))
        self.label_59.setText(_translate("fmCondCalib", "A 3", None))
        self.chbBKd.setText(_translate("fmCondCalib", "Коррекция нелинейности", None))
        self.groupBox_2.setTitle(_translate("fmCondCalib", "Изменение характеристик профиля", None))
        self.label_38.setText(_translate("fmCondCalib", "<html><head/><body><p>K яч</p></body></html>", None))
        self.groupBox_3.setTitle(_translate("fmCondCalib", "Диапазон измерения проводимости  ( мСм )", None))
        self.label_39.setText(_translate("fmCondCalib", "<html><head/><body><p>Мин.</p></body></html>", None))
        self.label_41.setText(_translate("fmCondCalib", "<html><head/><body><p>Макс.</p></body></html>", None))
        self.lblKD6_2.setText(_translate("fmCondCalib", "Ввод проводимости", None))
        self.tbRecalc.setText(_translate("fmCondCalib", "Пересчет", None))
        self.actTIns.setText(_translate("fmCondCalib", "Вставить строку", None))
        self.actTDel.setText(_translate("fmCondCalib", "Удалить строку", None))
        self.actPrIns.setText(_translate("fmCondCalib", "Новый профиль", None))
        self.actPrDel.setText(_translate("fmCondCalib", "Удалить профиль", None))
        self.actPrRen.setText(_translate("fmCondCalib", "Переименовать профиль", None))

