# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\ormet\source\svi (4)\svi\forms\fmChangeVirtPriborsParam.ui'
#
# Created: Thu Sep 13 10:22:59 2018
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

class Ui_fmChangeVirtPriborsParam(object):
    def setupUi(self, fmChangeVirtPriborsParam):
        fmChangeVirtPriborsParam.setObjectName(_fromUtf8("fmChangeVirtPriborsParam"))
        fmChangeVirtPriborsParam.resize(1028, 889)
        fmChangeVirtPriborsParam.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        self.centralwidget = QtGui.QWidget(fmChangeVirtPriborsParam)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.twMeas = QtGui.QTreeWidget(self.centralwidget)
        self.twMeas.setGeometry(QtCore.QRect(1070, 590, 292, 221))
        self.twMeas.setFrameShadow(QtGui.QFrame.Sunken)
        self.twMeas.setLineWidth(1)
        self.twMeas.setObjectName(_fromUtf8("twMeas"))
        self.twMeas.headerItem().setText(0, _fromUtf8("1"))
        self.twMeas.header().setVisible(False)
        self.groupBox_5 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(460, 110, 441, 171))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.leTypeVPribor = QtGui.QLineEdit(self.groupBox_5)
        self.leTypeVPribor.setGeometry(QtCore.QRect(20, 48, 131, 22))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.leTypeVPribor.setFont(font)
        self.leTypeVPribor.setObjectName(_fromUtf8("leTypeVPribor"))
        self.lbl1_12 = QtGui.QLabel(self.groupBox_5)
        self.lbl1_12.setGeometry(QtCore.QRect(30, 20, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbl1_12.setFont(font)
        self.lbl1_12.setLineWidth(-5)
        self.lbl1_12.setObjectName(_fromUtf8("lbl1_12"))
        self.tbAddVPType = QtGui.QToolButton(self.groupBox_5)
        self.tbAddVPType.setGeometry(QtCore.QRect(40, 80, 78, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tbAddVPType.setFont(font)
        self.tbAddVPType.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.tbAddVPType.setArrowType(QtCore.Qt.NoArrow)
        self.tbAddVPType.setObjectName(_fromUtf8("tbAddVPType"))
        self.tbDelVPType = QtGui.QToolButton(self.groupBox_5)
        self.tbDelVPType.setGeometry(QtCore.QRect(40, 110, 78, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tbDelVPType.setFont(font)
        self.tbDelVPType.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.tbDelVPType.setArrowType(QtCore.Qt.NoArrow)
        self.tbDelVPType.setObjectName(_fromUtf8("tbDelVPType"))
        self.tbChangeVPType = QtGui.QToolButton(self.groupBox_5)
        self.tbChangeVPType.setGeometry(QtCore.QRect(40, 140, 78, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tbChangeVPType.setFont(font)
        self.tbChangeVPType.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.tbChangeVPType.setArrowType(QtCore.Qt.NoArrow)
        self.tbChangeVPType.setObjectName(_fromUtf8("tbChangeVPType"))
        self.tbChangeTypeVPCh = QtGui.QToolButton(self.groupBox_5)
        self.tbChangeTypeVPCh.setGeometry(QtCore.QRect(280, 140, 78, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tbChangeTypeVPCh.setFont(font)
        self.tbChangeTypeVPCh.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.tbChangeTypeVPCh.setArrowType(QtCore.Qt.NoArrow)
        self.tbChangeTypeVPCh.setObjectName(_fromUtf8("tbChangeTypeVPCh"))
        self.lbl1_17 = QtGui.QLabel(self.groupBox_5)
        self.lbl1_17.setGeometry(QtCore.QRect(270, 20, 121, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbl1_17.setFont(font)
        self.lbl1_17.setLineWidth(-5)
        self.lbl1_17.setObjectName(_fromUtf8("lbl1_17"))
        self.tbDelTypeVPCh = QtGui.QToolButton(self.groupBox_5)
        self.tbDelTypeVPCh.setGeometry(QtCore.QRect(280, 110, 78, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tbDelTypeVPCh.setFont(font)
        self.tbDelTypeVPCh.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.tbDelTypeVPCh.setArrowType(QtCore.Qt.NoArrow)
        self.tbDelTypeVPCh.setObjectName(_fromUtf8("tbDelTypeVPCh"))
        self.tbAddTypeVPCh = QtGui.QToolButton(self.groupBox_5)
        self.tbAddTypeVPCh.setGeometry(QtCore.QRect(280, 80, 78, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tbAddTypeVPCh.setFont(font)
        self.tbAddTypeVPCh.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.tbAddTypeVPCh.setArrowType(QtCore.Qt.NoArrow)
        self.tbAddTypeVPCh.setObjectName(_fromUtf8("tbAddTypeVPCh"))
        self.leTypeVPCh = QtGui.QLineEdit(self.groupBox_5)
        self.leTypeVPCh.setGeometry(QtCore.QRect(260, 48, 131, 22))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.leTypeVPCh.setFont(font)
        self.leTypeVPCh.setObjectName(_fromUtf8("leTypeVPCh"))
        self.groupBox_4 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(11, 109, 441, 171))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.leTypeCh = QtGui.QLineEdit(self.groupBox_4)
        self.leTypeCh.setGeometry(QtCore.QRect(7, 48, 111, 22))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.leTypeCh.setFont(font)
        self.leTypeCh.setObjectName(_fromUtf8("leTypeCh"))
        self.leAddrCh = QtGui.QLineEdit(self.groupBox_4)
        self.leAddrCh.setGeometry(QtCore.QRect(220, 50, 81, 22))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.leAddrCh.setFont(font)
        self.leAddrCh.setObjectName(_fromUtf8("leAddrCh"))
        self.lbl1_10 = QtGui.QLabel(self.groupBox_4)
        self.lbl1_10.setGeometry(QtCore.QRect(30, 20, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbl1_10.setFont(font)
        self.lbl1_10.setLineWidth(-5)
        self.lbl1_10.setObjectName(_fromUtf8("lbl1_10"))
        self.lbl1_11 = QtGui.QLabel(self.groupBox_4)
        self.lbl1_11.setGeometry(QtCore.QRect(220, 20, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbl1_11.setFont(font)
        self.lbl1_11.setLineWidth(-5)
        self.lbl1_11.setObjectName(_fromUtf8("lbl1_11"))
        self.tbAddChName = QtGui.QToolButton(self.groupBox_4)
        self.tbAddChName.setGeometry(QtCore.QRect(20, 80, 78, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tbAddChName.setFont(font)
        self.tbAddChName.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.tbAddChName.setArrowType(QtCore.Qt.NoArrow)
        self.tbAddChName.setObjectName(_fromUtf8("tbAddChName"))
        self.tbDelChAddr = QtGui.QToolButton(self.groupBox_4)
        self.tbDelChAddr.setGeometry(QtCore.QRect(220, 110, 78, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tbDelChAddr.setFont(font)
        self.tbDelChAddr.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.tbDelChAddr.setArrowType(QtCore.Qt.NoArrow)
        self.tbDelChAddr.setObjectName(_fromUtf8("tbDelChAddr"))
        self.tbDelChName = QtGui.QToolButton(self.groupBox_4)
        self.tbDelChName.setGeometry(QtCore.QRect(20, 110, 78, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tbDelChName.setFont(font)
        self.tbDelChName.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.tbDelChName.setArrowType(QtCore.Qt.NoArrow)
        self.tbDelChName.setObjectName(_fromUtf8("tbDelChName"))
        self.tbAddChAddr = QtGui.QToolButton(self.groupBox_4)
        self.tbAddChAddr.setGeometry(QtCore.QRect(220, 80, 78, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tbAddChAddr.setFont(font)
        self.tbAddChAddr.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.tbAddChAddr.setArrowType(QtCore.Qt.NoArrow)
        self.tbAddChAddr.setObjectName(_fromUtf8("tbAddChAddr"))
        self.tbChangeChAddr = QtGui.QToolButton(self.groupBox_4)
        self.tbChangeChAddr.setGeometry(QtCore.QRect(220, 140, 78, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tbChangeChAddr.setFont(font)
        self.tbChangeChAddr.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.tbChangeChAddr.setArrowType(QtCore.Qt.NoArrow)
        self.tbChangeChAddr.setObjectName(_fromUtf8("tbChangeChAddr"))
        self.tbChangeChName = QtGui.QToolButton(self.groupBox_4)
        self.tbChangeChName.setGeometry(QtCore.QRect(20, 140, 78, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tbChangeChName.setFont(font)
        self.tbChangeChName.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.tbChangeChName.setArrowType(QtCore.Qt.NoArrow)
        self.tbChangeChName.setObjectName(_fromUtf8("tbChangeChName"))
        self.groupBox_6 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_6.setGeometry(QtCore.QRect(4, 10, 891, 91))
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.cbChAddr = QtGui.QComboBox(self.groupBox_6)
        self.cbChAddr.setGeometry(QtCore.QRect(230, 46, 101, 22))
        self.cbChAddr.setEditable(False)
        self.cbChAddr.setObjectName(_fromUtf8("cbChAddr"))
        self.lbl1_6 = QtGui.QLabel(self.groupBox_6)
        self.lbl1_6.setGeometry(QtCore.QRect(240, 20, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbl1_6.setFont(font)
        self.lbl1_6.setLineWidth(-5)
        self.lbl1_6.setObjectName(_fromUtf8("lbl1_6"))
        self.cbChType = QtGui.QComboBox(self.groupBox_6)
        self.cbChType.setGeometry(QtCore.QRect(7, 46, 141, 22))
        self.cbChType.setEditable(False)
        self.cbChType.setObjectName(_fromUtf8("cbChType"))
        self.lbl1_3 = QtGui.QLabel(self.groupBox_6)
        self.lbl1_3.setGeometry(QtCore.QRect(25, 20, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbl1_3.setFont(font)
        self.lbl1_3.setLineWidth(-5)
        self.lbl1_3.setObjectName(_fromUtf8("lbl1_3"))
        self.cbTypeVPribor = QtGui.QComboBox(self.groupBox_6)
        self.cbTypeVPribor.setGeometry(QtCore.QRect(479, 47, 151, 22))
        self.cbTypeVPribor.setEditable(False)
        self.cbTypeVPribor.setObjectName(_fromUtf8("cbTypeVPribor"))
        self.lbl1_7 = QtGui.QLabel(self.groupBox_6)
        self.lbl1_7.setGeometry(QtCore.QRect(490, 21, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbl1_7.setFont(font)
        self.lbl1_7.setLineWidth(-5)
        self.lbl1_7.setObjectName(_fromUtf8("lbl1_7"))
        self.lbl1_20 = QtGui.QLabel(self.groupBox_6)
        self.lbl1_20.setGeometry(QtCore.QRect(737, 22, 131, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbl1_20.setFont(font)
        self.lbl1_20.setLineWidth(-5)
        self.lbl1_20.setObjectName(_fromUtf8("lbl1_20"))
        self.cbChInVPType = QtGui.QComboBox(self.groupBox_6)
        self.cbChInVPType.setGeometry(QtCore.QRect(719, 48, 141, 22))
        self.cbChInVPType.setEditable(False)
        self.cbChInVPType.setObjectName(_fromUtf8("cbChInVPType"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 290, 292, 14))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.lwChTempl = QtGui.QListWidget(self.centralwidget)
        self.lwChTempl.setGeometry(QtCore.QRect(15, 310, 441, 191))
        self.lwChTempl.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.lwChTempl.setObjectName(_fromUtf8("lwChTempl"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(20, 520, 441, 331))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.tbAddChTempl = QtGui.QToolButton(self.groupBox)
        self.tbAddChTempl.setGeometry(QtCore.QRect(10, 86, 78, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tbAddChTempl.setFont(font)
        self.tbAddChTempl.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.tbAddChTempl.setArrowType(QtCore.Qt.NoArrow)
        self.tbAddChTempl.setObjectName(_fromUtf8("tbAddChTempl"))
        self.tbDelChTempl = QtGui.QToolButton(self.groupBox)
        self.tbDelChTempl.setGeometry(QtCore.QRect(330, 86, 78, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tbDelChTempl.setFont(font)
        self.tbDelChTempl.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.tbDelChTempl.setArrowType(QtCore.Qt.NoArrow)
        self.tbDelChTempl.setObjectName(_fromUtf8("tbDelChTempl"))
        self.tbChangeChTempl = QtGui.QToolButton(self.groupBox)
        self.tbChangeChTempl.setGeometry(QtCore.QRect(160, 86, 78, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tbChangeChTempl.setFont(font)
        self.tbChangeChTempl.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.tbChangeChTempl.setArrowType(QtCore.Qt.NoArrow)
        self.tbChangeChTempl.setObjectName(_fromUtf8("tbChangeChTempl"))
        self.groupBox_7 = QtGui.QGroupBox(self.groupBox)
        self.groupBox_7.setGeometry(QtCore.QRect(10, 110, 421, 211))
        self.groupBox_7.setObjectName(_fromUtf8("groupBox_7"))
        self.lbl1_9 = QtGui.QLabel(self.groupBox_7)
        self.lbl1_9.setGeometry(QtCore.QRect(100, 14, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbl1_9.setFont(font)
        self.lbl1_9.setLineWidth(-5)
        self.lbl1_9.setObjectName(_fromUtf8("lbl1_9"))
        self.cbChAddrTempl = QtGui.QComboBox(self.groupBox_7)
        self.cbChAddrTempl.setGeometry(QtCore.QRect(230, 146, 101, 22))
        self.cbChAddrTempl.setEditable(False)
        self.cbChAddrTempl.setObjectName(_fromUtf8("cbChAddrTempl"))
        self.lbl1_13 = QtGui.QLabel(self.groupBox_7)
        self.lbl1_13.setGeometry(QtCore.QRect(240, 120, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbl1_13.setFont(font)
        self.lbl1_13.setLineWidth(-5)
        self.lbl1_13.setObjectName(_fromUtf8("lbl1_13"))
        self.tbDelChInMessTempl = QtGui.QToolButton(self.groupBox_7)
        self.tbDelChInMessTempl.setGeometry(QtCore.QRect(330, 180, 78, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tbDelChInMessTempl.setFont(font)
        self.tbDelChInMessTempl.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.tbDelChInMessTempl.setArrowType(QtCore.Qt.NoArrow)
        self.tbDelChInMessTempl.setObjectName(_fromUtf8("tbDelChInMessTempl"))
        self.cbChTypeTempl = QtGui.QComboBox(self.groupBox_7)
        self.cbChTypeTempl.setGeometry(QtCore.QRect(7, 146, 141, 22))
        self.cbChTypeTempl.setEditable(False)
        self.cbChTypeTempl.setObjectName(_fromUtf8("cbChTypeTempl"))
        self.lwChInMessTempl = QtGui.QListWidget(self.groupBox_7)
        self.lwChInMessTempl.setGeometry(QtCore.QRect(10, 44, 411, 71))
        self.lwChInMessTempl.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.lwChInMessTempl.setObjectName(_fromUtf8("lwChInMessTempl"))
        self.tbAddChInMessTempl = QtGui.QToolButton(self.groupBox_7)
        self.tbAddChInMessTempl.setGeometry(QtCore.QRect(10, 180, 78, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tbAddChInMessTempl.setFont(font)
        self.tbAddChInMessTempl.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.tbAddChInMessTempl.setArrowType(QtCore.Qt.NoArrow)
        self.tbAddChInMessTempl.setObjectName(_fromUtf8("tbAddChInMessTempl"))
        self.lbl1_4 = QtGui.QLabel(self.groupBox_7)
        self.lbl1_4.setGeometry(QtCore.QRect(25, 120, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbl1_4.setFont(font)
        self.lbl1_4.setLineWidth(-5)
        self.lbl1_4.setObjectName(_fromUtf8("lbl1_4"))
        self.tbChangeChInMessTempl = QtGui.QToolButton(self.groupBox_7)
        self.tbChangeChInMessTempl.setGeometry(QtCore.QRect(160, 180, 78, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tbChangeChInMessTempl.setFont(font)
        self.tbChangeChInMessTempl.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.tbChangeChInMessTempl.setArrowType(QtCore.Qt.NoArrow)
        self.tbChangeChInMessTempl.setObjectName(_fromUtf8("tbChangeChInMessTempl"))
        self.lbl1_14 = QtGui.QLabel(self.groupBox)
        self.lbl1_14.setGeometry(QtCore.QRect(10, 30, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbl1_14.setFont(font)
        self.lbl1_14.setLineWidth(-5)
        self.lbl1_14.setObjectName(_fromUtf8("lbl1_14"))
        self.leTypeMess = QtGui.QLineEdit(self.groupBox)
        self.leTypeMess.setGeometry(QtCore.QRect(10, 50, 191, 22))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.leTypeMess.setFont(font)
        self.leTypeMess.setObjectName(_fromUtf8("leTypeMess"))
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(480, 300, 441, 331))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.lbl1_2 = QtGui.QLabel(self.groupBox_2)
        self.lbl1_2.setGeometry(QtCore.QRect(4, 20, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbl1_2.setFont(font)
        self.lbl1_2.setLineWidth(-5)
        self.lbl1_2.setObjectName(_fromUtf8("lbl1_2"))
        self.leModbusNum = QtGui.QLineEdit(self.groupBox_2)
        self.leModbusNum.setGeometry(QtCore.QRect(7, 48, 81, 22))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.leModbusNum.setFont(font)
        self.leModbusNum.setObjectName(_fromUtf8("leModbusNum"))
        self.leIndexMess = QtGui.QLineEdit(self.groupBox_2)
        self.leIndexMess.setGeometry(QtCore.QRect(260, 50, 171, 22))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.leIndexMess.setFont(font)
        self.leIndexMess.setObjectName(_fromUtf8("leIndexMess"))
        self.tbAddCh = QtGui.QToolButton(self.groupBox_2)
        self.tbAddCh.setGeometry(QtCore.QRect(10, 86, 78, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tbAddCh.setFont(font)
        self.tbAddCh.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.tbAddCh.setArrowType(QtCore.Qt.NoArrow)
        self.tbAddCh.setObjectName(_fromUtf8("tbAddCh"))
        self.tbDelCh = QtGui.QToolButton(self.groupBox_2)
        self.tbDelCh.setGeometry(QtCore.QRect(330, 86, 78, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tbDelCh.setFont(font)
        self.tbDelCh.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.tbDelCh.setArrowType(QtCore.Qt.NoArrow)
        self.tbDelCh.setObjectName(_fromUtf8("tbDelCh"))
        self.tbChangeCh = QtGui.QToolButton(self.groupBox_2)
        self.tbChangeCh.setGeometry(QtCore.QRect(160, 86, 78, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tbChangeCh.setFont(font)
        self.tbChangeCh.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.tbChangeCh.setArrowType(QtCore.Qt.NoArrow)
        self.tbChangeCh.setObjectName(_fromUtf8("tbChangeCh"))
        self.lbl1_8 = QtGui.QLabel(self.groupBox_2)
        self.lbl1_8.setGeometry(QtCore.QRect(270, 20, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbl1_8.setFont(font)
        self.lbl1_8.setLineWidth(-5)
        self.lbl1_8.setObjectName(_fromUtf8("lbl1_8"))
        self.groupBox_8 = QtGui.QGroupBox(self.groupBox_2)
        self.groupBox_8.setGeometry(QtCore.QRect(10, 110, 421, 211))
        self.groupBox_8.setObjectName(_fromUtf8("groupBox_8"))
        self.lbl1_15 = QtGui.QLabel(self.groupBox_8)
        self.lbl1_15.setGeometry(QtCore.QRect(100, 14, 201, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbl1_15.setFont(font)
        self.lbl1_15.setLineWidth(-5)
        self.lbl1_15.setObjectName(_fromUtf8("lbl1_15"))
        self.cbChAddr_2 = QtGui.QComboBox(self.groupBox_8)
        self.cbChAddr_2.setGeometry(QtCore.QRect(230, 146, 101, 22))
        self.cbChAddr_2.setEditable(False)
        self.cbChAddr_2.setObjectName(_fromUtf8("cbChAddr_2"))
        self.lbl1_16 = QtGui.QLabel(self.groupBox_8)
        self.lbl1_16.setGeometry(QtCore.QRect(240, 120, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbl1_16.setFont(font)
        self.lbl1_16.setLineWidth(-5)
        self.lbl1_16.setObjectName(_fromUtf8("lbl1_16"))
        self.tbDelChInMess = QtGui.QToolButton(self.groupBox_8)
        self.tbDelChInMess.setGeometry(QtCore.QRect(330, 180, 78, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tbDelChInMess.setFont(font)
        self.tbDelChInMess.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.tbDelChInMess.setArrowType(QtCore.Qt.NoArrow)
        self.tbDelChInMess.setObjectName(_fromUtf8("tbDelChInMess"))
        self.cbChType_2 = QtGui.QComboBox(self.groupBox_8)
        self.cbChType_2.setGeometry(QtCore.QRect(7, 146, 141, 22))
        self.cbChType_2.setEditable(False)
        self.cbChType_2.setObjectName(_fromUtf8("cbChType_2"))
        self.lwChInMess = QtGui.QListWidget(self.groupBox_8)
        self.lwChInMess.setGeometry(QtCore.QRect(10, 44, 411, 71))
        self.lwChInMess.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.lwChInMess.setObjectName(_fromUtf8("lwChInMess"))
        self.tbAddChInMess = QtGui.QToolButton(self.groupBox_8)
        self.tbAddChInMess.setGeometry(QtCore.QRect(10, 180, 78, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tbAddChInMess.setFont(font)
        self.tbAddChInMess.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.tbAddChInMess.setArrowType(QtCore.Qt.NoArrow)
        self.tbAddChInMess.setObjectName(_fromUtf8("tbAddChInMess"))
        self.lbl1_5 = QtGui.QLabel(self.groupBox_8)
        self.lbl1_5.setGeometry(QtCore.QRect(25, 120, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbl1_5.setFont(font)
        self.lbl1_5.setLineWidth(-5)
        self.lbl1_5.setObjectName(_fromUtf8("lbl1_5"))
        self.tbChangeChInMess = QtGui.QToolButton(self.groupBox_8)
        self.tbChangeChInMess.setGeometry(QtCore.QRect(160, 180, 78, 20))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.tbChangeChInMess.setFont(font)
        self.tbChangeChInMess.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.tbChangeChInMess.setArrowType(QtCore.Qt.NoArrow)
        self.tbChangeChInMess.setObjectName(_fromUtf8("tbChangeChInMess"))
        self.lbl1_18 = QtGui.QLabel(self.groupBox_2)
        self.lbl1_18.setGeometry(QtCore.QRect(110, 20, 91, 21))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.lbl1_18.setFont(font)
        self.lbl1_18.setLineWidth(-5)
        self.lbl1_18.setObjectName(_fromUtf8("lbl1_18"))
        self.cbTypeMess = QtGui.QComboBox(self.groupBox_2)
        self.cbTypeMess.setGeometry(QtCore.QRect(100, 50, 151, 22))
        self.cbTypeMess.setEditable(False)
        self.cbTypeMess.setObjectName(_fromUtf8("cbTypeMess"))
        fmChangeVirtPriborsParam.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(fmChangeVirtPriborsParam)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1028, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        fmChangeVirtPriborsParam.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(fmChangeVirtPriborsParam)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        fmChangeVirtPriborsParam.setStatusBar(self.statusbar)

        self.retranslateUi(fmChangeVirtPriborsParam)
        self.cbChAddr.setCurrentIndex(-1)
        self.cbChType.setCurrentIndex(-1)
        self.cbTypeVPribor.setCurrentIndex(-1)
        self.cbChInVPType.setCurrentIndex(-1)
        self.cbChAddrTempl.setCurrentIndex(-1)
        self.cbChTypeTempl.setCurrentIndex(-1)
        self.cbChAddr_2.setCurrentIndex(-1)
        self.cbChType_2.setCurrentIndex(-1)
        self.cbTypeMess.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(fmChangeVirtPriborsParam)

    def retranslateUi(self, fmChangeVirtPriborsParam):
        fmChangeVirtPriborsParam.setWindowTitle(_translate("fmChangeVirtPriborsParam", "Изменение параметров измерительных каналов и виртуальных приборов", None))
        self.groupBox_5.setTitle(_translate("fmChangeVirtPriborsParam", "Добавление параметров виртуального прибора", None))
        self.leTypeVPribor.setText(_translate("fmChangeVirtPriborsParam", "0", None))
        self.lbl1_12.setText(_translate("fmChangeVirtPriborsParam", "Тип прибора", None))
        self.tbAddVPType.setText(_translate("fmChangeVirtPriborsParam", "Добавить", None))
        self.tbDelVPType.setText(_translate("fmChangeVirtPriborsParam", "Удалить", None))
        self.tbChangeVPType.setText(_translate("fmChangeVirtPriborsParam", "Изменить", None))
        self.tbChangeTypeVPCh.setText(_translate("fmChangeVirtPriborsParam", "Изменить", None))
        self.lbl1_17.setText(_translate("fmChangeVirtPriborsParam", "Тип канала прибора", None))
        self.tbDelTypeVPCh.setText(_translate("fmChangeVirtPriborsParam", "Удалить", None))
        self.tbAddTypeVPCh.setText(_translate("fmChangeVirtPriborsParam", "Добавить", None))
        self.leTypeVPCh.setText(_translate("fmChangeVirtPriborsParam", "0", None))
        self.groupBox_4.setTitle(_translate("fmChangeVirtPriborsParam", "Добавление параметров канала измерителя", None))
        self.leTypeCh.setText(_translate("fmChangeVirtPriborsParam", "0", None))
        self.leAddrCh.setText(_translate("fmChangeVirtPriborsParam", "0", None))
        self.lbl1_10.setText(_translate("fmChangeVirtPriborsParam", "Тип канала", None))
        self.lbl1_11.setText(_translate("fmChangeVirtPriborsParam", "Адрес канала", None))
        self.tbAddChName.setText(_translate("fmChangeVirtPriborsParam", "Добавить", None))
        self.tbDelChAddr.setText(_translate("fmChangeVirtPriborsParam", "Удалить", None))
        self.tbDelChName.setText(_translate("fmChangeVirtPriborsParam", "Удалить", None))
        self.tbAddChAddr.setText(_translate("fmChangeVirtPriborsParam", "Добавить", None))
        self.tbChangeChAddr.setText(_translate("fmChangeVirtPriborsParam", "Изменить", None))
        self.tbChangeChName.setText(_translate("fmChangeVirtPriborsParam", "Изменить", None))
        self.groupBox_6.setTitle(_translate("fmChangeVirtPriborsParam", "Параметры каналов измерения и виртуальных приборов", None))
        self.lbl1_6.setText(_translate("fmChangeVirtPriborsParam", "Адрес канала", None))
        self.lbl1_3.setText(_translate("fmChangeVirtPriborsParam", "Тип канала", None))
        self.lbl1_7.setText(_translate("fmChangeVirtPriborsParam", "Тип прибора", None))
        self.lbl1_20.setText(_translate("fmChangeVirtPriborsParam", "Тип канала прибора", None))
        self.label.setText(_translate("fmChangeVirtPriborsParam", "Шаблоны измерителей", None))
        self.groupBox.setTitle(_translate("fmChangeVirtPriborsParam", "Редактирование шаблона измерителя", None))
        self.tbAddChTempl.setText(_translate("fmChangeVirtPriborsParam", "Добавить", None))
        self.tbDelChTempl.setText(_translate("fmChangeVirtPriborsParam", "Удалить", None))
        self.tbChangeChTempl.setText(_translate("fmChangeVirtPriborsParam", "Изменить", None))
        self.groupBox_7.setTitle(_translate("fmChangeVirtPriborsParam", "Добавление канала измерителя", None))
        self.lbl1_9.setText(_translate("fmChangeVirtPriborsParam", "Наименование канала измерителя", None))
        self.lbl1_13.setText(_translate("fmChangeVirtPriborsParam", "Адрес канала", None))
        self.tbDelChInMessTempl.setText(_translate("fmChangeVirtPriborsParam", "Удалить", None))
        self.tbAddChInMessTempl.setText(_translate("fmChangeVirtPriborsParam", "Добавить", None))
        self.lbl1_4.setText(_translate("fmChangeVirtPriborsParam", "Тип канала", None))
        self.tbChangeChInMessTempl.setText(_translate("fmChangeVirtPriborsParam", "Изменить", None))
        self.lbl1_14.setText(_translate("fmChangeVirtPriborsParam", "Тип измeрителя", None))
        self.leTypeMess.setText(_translate("fmChangeVirtPriborsParam", "0", None))
        self.groupBox_2.setTitle(_translate("fmChangeVirtPriborsParam", "Добавление или изменение измерителя", None))
        self.lbl1_2.setText(_translate("fmChangeVirtPriborsParam", "Адрес MODBUS", None))
        self.leModbusNum.setText(_translate("fmChangeVirtPriborsParam", "0", None))
        self.leIndexMess.setText(_translate("fmChangeVirtPriborsParam", "0", None))
        self.tbAddCh.setText(_translate("fmChangeVirtPriborsParam", "Добавить", None))
        self.tbDelCh.setText(_translate("fmChangeVirtPriborsParam", "Удалить", None))
        self.tbChangeCh.setText(_translate("fmChangeVirtPriborsParam", "Изменить", None))
        self.lbl1_8.setText(_translate("fmChangeVirtPriborsParam", "Наименование измерителя", None))
        self.groupBox_8.setTitle(_translate("fmChangeVirtPriborsParam", "Добавление канала измерителя", None))
        self.lbl1_15.setText(_translate("fmChangeVirtPriborsParam", "Наименование канала измерителя", None))
        self.lbl1_16.setText(_translate("fmChangeVirtPriborsParam", "Адрес канала", None))
        self.tbDelChInMess.setText(_translate("fmChangeVirtPriborsParam", "Удалить", None))
        self.tbAddChInMess.setText(_translate("fmChangeVirtPriborsParam", "Добавить", None))
        self.lbl1_5.setText(_translate("fmChangeVirtPriborsParam", "Тип канала", None))
        self.tbChangeChInMess.setText(_translate("fmChangeVirtPriborsParam", "Изменить", None))
        self.lbl1_18.setText(_translate("fmChangeVirtPriborsParam", "Тип измкрителя", None))
