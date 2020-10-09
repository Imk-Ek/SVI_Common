
import logging
import os, sys
import atexit
import string
from PyQt4 import QtCore, QtGui 

from datetime import datetime
from vinstr import *

#from common import *
#для виртуальных приборов
if PCFlag==1: 
  from fmProbaID import Ui_fmProbaID
  from fmAboutVP import Ui_fmAboutVP
  from fmMessage import Ui_fmMessage
if PCFlag==2: 
  from fmProbaID_t import Ui_fmProbaID
  from fmAboutVP_t import Ui_fmAboutVP
  from fmMessage_t import Ui_fmMessage

#from vinstr import *


#LL = logging.getLogger('SVI')



class CfmProbaID(QtGui.QMainWindow, Ui_fmProbaID):
  """ Форма ввода идентификатора пробы """


  def __init__(self, vProbaID):
    super().__init__() 
    self.setupUi(self)
    self.vCE=vProbaID
    self.tbEnterPassword.clicked.connect(self.on_tbEnterPasword_toggle)
    self.lePassword.editingFinished.connect(self.on_lePasswordFinished)

  def on_tbEnterPasword_toggle(self):
      """ Нажатие кнопки ввод по вводу пароля"""
      
      a=1
      tmpstr=self.lePassword.text()
      self.vCE.ID_VP=tmpstr
      self.vCE.win.lblID.setText(tmpstr)
      self.close()

 
  def on_lePasswordFinished(self):
      a=1

  def show(self, newsize = None):
      self.lePassword.setText(str(self.vCE.ID_VP))
      super().show()


class CfmAboutVP(QtGui.QMainWindow, Ui_fmAboutVP):
  """ Форма ввода идентификатора пробы """


  def __init__(self, vAboutVP):
    super().__init__() 
    self.setupUi(self)
    self.vCE=vAboutVP

  def show(self, newsize = None):
    self.lwAbout.clear()
    tmptxt=self.vCE.vCE.CommonProfil_stateD['LastCfgName']
    self.lwAbout.addItem('Конфигурация  '+tmptxt)
    self.lwAbout.addItem('Виртуальные приборы')
    n=self.vCE.vCE.CommonProfil_stateD['CurrCFG']['CurrCFGVPListCount']
    i=0
    while (i<n) :
      tmptxt=self.vCE.vCE.CommonProfil_stateD['CurrCFG']['CurrCFGVPList'][i]
      self.lwAbout.addItem(tmptxt)
      i=i+1   
    super().show()

class CfmMessage(QtGui.QMainWindow, Ui_fmMessage):
  """ Форма вывода сообщений системы """


  def __init__(self, vMessage):
    super().__init__() 
    self.setupUi(self)
    self.vCE=vMessage

  def show(self, newsize = None):
    

    super().show()

class QLineEdit_1(QtGui.QLineEdit):

  def mouseReleaseEvent(self,event):    
  
      # Mouse Right Button Release Event #.RightButton:
      if event.button() == QtCore.Qt.LeftButton:
          #QtGui.QMessageBox.information(self,"Mouse Right Button Release Detected!","Detected Mouse Right Button Release")
          self.emit(QtCore.SIGNAL('dcEmitApp()'))

  def mouseDoubleClickEvent(self,event):
      self.emit(QtCore.SIGNAL('dcEmitApp1()'))