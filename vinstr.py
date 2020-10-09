# -*- coding: utf-8 -*-
import sys, traceback
import logging

from PyQt4 import QtCore, QtGui 
from common import *
if PCFlag==1:from fmChangeVPribors import Ui_fmChangeVPribors
if PCFlag==2:from fmChangeVPribors_t import Ui_fmChangeVPribors
import math
import sys
import numpy
from PyQt4 import Qt
import PyQt4.Qwt5 as Qwt
import sstate

import Results

# ---------------------------------------------- 
#        Локальные ф-ии

def safeDget(d, key, a_def):
  """ ф-ия возвращает значение ключа из словаря d или
           значение a_def при отсутствии ключа в словаре """
  try:
    res = d[key]
  except:
    res = a_def
  return res 
#----------------------------------------------


class CSaveRes:
  """ базовая часть виртуального прибора """
 
  def __init__(self):
       self.DCommon[1][0]

  def Save_Value(self,x,y,val):
       self.DCommon[x][y]=val
  def Get_Value(self,x,y):
       Res=self.DCommon[x][y]


class CVInstr:
  """ базовая часть виртуального прибора """
  # win - экземпляр окна - лицевой панели (создается потомком)
  # fFirstShow - True - первое отображение лицевой панели ("костыль" для восстановления сохраненной геометрии)
  # dictCfg - словарь-дескриптор виртуального прибора (связанный с vinstrD)
  # dictState - словарь сохраняемых при выключении переменных\параметров
  # fTech - True - запуск в технологическом режиме
  
  def __init__(self, dcfg, dstate = {}, fTech = False):
    self.win = None
    self.fFirstShow = True
    self.dictCfg = dcfg
    self.dictState = dstate
    self.fTech = fTech
    #Results.InitPriborRes(dcfg['наименование'])
      


 
  def LoadState(self, dstate  = None):
    """ загрузить в словарь сохраняемых параметров dstate и применить эти параметры """
    if dstate:  self.dictState.update(dstate) 
    if self.win: 
      # восстанавливаем расположение и габариты лицевой панели с контролем выхода за границы экрана 
      desktop = QtGui.QApplication.desktop() 
      dh = desktop.height()
      dw = desktop.width() 
      winR = self.win.geometry()
      rect = QtCore.QRect()
       
      rect.setWidth(safeDget(self.dictState, "win.width", winR.width())) 
      rect.setHeight(safeDget(self.dictState, "win.height", winR.height()))

      tmp = safeDget(self.dictState, "win.left", dw << 1)
      if (tmp > dw):  tmp = (dw >> 1) - (rect.width() >> 1)
      rect.setLeft(tmp)         

      tmp = safeDget(self.dictState, "win.top", dh << 1)
      if (tmp > dh):  tmp = (dh >> 1) - (rect.height() >> 1)
      rect.setTop(tmp)  
  
      #self.win.setGeometry(rect)
      self.win.setWindowTitle(self.dictCfg["наименование"])  

    #super().LoadState()


  def SaveState(self):
    """ сохранить параметры в dictState """ 
    if self.win:
      #rect = self.win.frameGeometry()
      rect = self.win.geometry()
      self.dictState["win.left"] = rect.left()
      self.dictState["win.top"] = rect.top()
      self.dictState["win.width"] = rect.width() 
      self.dictState["win.height"] = rect.height()

    #super().SaveState()


  def ShowFP(self):
    """ отобразить лицевую панель """
    if self.fFirstShow: 
      self.fFirstShow = False
      if ("win.width" in self.dictState) and ("win.height" in  self.dictState):
        smartShow(self.win, QtCore.QSize(self.dictState["win.width"], self.dictState["win.height"]))   
      else:
        smartShow(self.win) 
    else:
      smartShow(self.win)


  def NewData(self, ddata):
    """ метод - приемник новых данных от измерителей, связанных с данным виртуальным прибором 
          ddict - словарь (key - наименование измерительного канала; значение - (ChanID, данные, время измерения))
        метод должен быть определен в классе - потомке  """
 
    pass 
#---

























