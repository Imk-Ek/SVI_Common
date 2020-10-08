

#import sys, traceback
import logging
from PyQt4 import QtCore, QtGui 
#import sstate

#from common import *
#import Results
from fpInputUnit import Ui_fpInputUnit
from vinstr import CVInstr
from chart import*
#LL = logging.getLogger('SVI')


#####################################
#import math
#import numpy
#from PyQt4 import Qt
#import PyQt4.Qwt5 as Qwt
#from PyQt4.Qt import *
#from PyQt4.Qwt5 import *
#import pyqtSlot,SIGNAL,SLOT
#####################################

class CInputUnit_(CVInstr):
  """ виртуальный """
  #  measN - наименование измерительного канала, связанного с данным экземпляром вольтметра
  #  widthD - суммарное кол-во выводимых знаков результата (БЕЗ учета запятой)
  #  precD  - кол-во знаков после запятой 
  #  formS  - строка форматирования для вывода результата (под НОВЫЙ метод format)

  def __init__(self, dcfg, dstate = {}, fTech = False):
    super().__init__(dcfg, dstate, fTech)
    self.Name=dcfg['наименование']
    self.ParamMess=dSize['VPParam']
    self.OutputVal=[0,0,0,0]
    self.tmpVal1=0
    self.tmpVal2=0
    self.tmpVal3=0
    self.OutputVal[0]=dSize['VPChOutTypeList'][0]
    self.OutputVal[1]=dSize['VPChOutTypeList'][1]
    self.OutputVal[2]=dSize['VPChOutTypeList'][2]
    #self.OutputVal[3]=dSize['VPChOutTypeList'][3]
    Results.Result_Dict[self.Name]={}
    Results.Result_Dict[self.Name][self.OutputVal[0]]=0
    Results.Result_Dict[self.Name][self.OutputVal[1]]=0
    Results.Result_Dict[self.Name][self.OutputVal[2]]=0

    self.widthD = 6 # 4
    self.precD = 3  # 3
    self.tmpVal4=0
    self.tmpVal5=0
    self.formS = "{:"+str(self.widthD)+"."+str(self.precD)+"f}"

    self.win = CfpInputUnit(self.widthD + 1, self)
    self.LoadState()
    
    

  def LoadState(self):
    super().LoadState()


  def SaveState(self):
    super().SaveState()


  def NewData(self, ddata):
    #global Result_Dict
    self.tmpVal4=Results.Result_Dict
    if self.measN in ddata:
      #self.win.lcdVolt.display(self.formS.format(ddata[self.measN][1]))
      self.tmpVal=ddata[self.measN][1]

    if self.win.Reset_Flag==1:
        self.Val_min=self.tmpVal
        self.Val_max=self.tmpVal
        self.win.Reset_Flag=0
        self.win.win_Chart.Reset_Flag=0
        self.win.win_Chart.Count_draw=0

    if self.tmpVal<self.Val_min:
        self.Val_min=self.tmpVal
    if self.tmpVal>self.Val_max:
        self.Val_max=self.tmpVal

        self.win.win_Chart.Sens_1.show()
        self.win.win_Chart.Sens_2.hide()
    self.win.win_Chart.lcdMain_mg.display(self.formS.format(self.tmpVal))
    self.win.win_Chart.lcdMain_mg_min.display(self.formS.format(self.Val_min))
    self.win.win_Chart.lcdMain_mg_max.display(self.formS.format(self.Val_max))
    self.win.win_Chart.y_draw=numpy.append(self.win.win_Chart.y_draw,self.tmpVal)
    self.win.win_Chart.x_draw=numpy.append(self.win.win_Chart.x_draw,self.win.win_Chart.Count_draw)
    self.win.win_Chart.Count_draw=self.win.win_Chart.Count_draw+1
    self.win.win_Chart.Sens_1.setData(self.win.win_Chart.x_draw,self.win.win_Chart.y_draw)
    #Results.Result_Dict[(self.Name)][('Value')]=self.tmpVal
    #Results.Result_Dict[(self.Name)][('EdIzm')]=0

  def Proceed(self):
    Results.Result_Dict[self.Name][self.OutputVal[0]]=self.tmpVal1
    Results.Result_Dict[self.Name][self.OutputVal[1]]=self.tmpVal2
    Results.Result_Dict[self.Name][self.OutputVal[2]]=self.tmpVal3
    q=1

#---
class CfpInputUnit(QtGui.QMainWindow, Ui_fpInputUnit):
  """ лицевая панель виртуального вольтметра  
        vVolt  - экземпляр виртуального вольтметра, соответствующий данной панели
        basePS - (pointSize, height) базовая связка для масштабирования наименования физ-величины (llData)  
     """
      
  def __init__(self, numDigits, vUnit):
    """ numDigits - суммарное кол-во выводимых знаков результата (C учетом запятой) """
    super(CfpInputUnit, self).__init__() 
    
    
    self.setupUi(self)
    self.vUnit = vUnit

    self.basePS = None
    self.lcdVolt.setDigitCount(numDigits)
    self.Type=2
    self.win_Chart = CfpChart(self)
    self.Reset_Flag=1

    self.actTech = QtGui.QAction("График", self) 
    self.tbEnter.clicked.connect(self.on_tbEnter)  
    self.menubar.addAction(self.actTech)
    self.timer = QtCore.QTimer()
    self.timer.timeout.connect(self.on_timer)
    self.timer.start(1000)
    

  def on_timer(self):

    self.vUnit.Proceed()

  def on_tbEnter(self):

    self.vUnit.tmpVal1=self.leVal1.text()
    self.vUnit.tmpVal2=self.leVal2.text()
    self.vUnit.tmpVal3=self.leVal3.text()


  def show(self, newsize = None):
    """ newsize - экземпляр QSize для передачи новых размеров окна """
    super().show()   # важно выполнить ПЕРЕД resize - иначе resize может не пройти
    if newsize:  self.resize(newsize)


  def closeEvent(self, event):
    self.vUnit.SaveState()
    event.accept() 


  def resizeEvent(self, event):
    '''rect = self.centralwidget.geometry()
    font = self.llData.font()
    fm = QtGui.QFontMetrics(font) 
    textH = fm.boundingRect(self.llData.text()).height()

    # print("layout.height = {} text.height = {} pointS = {}".format(rect.height(), textH, font.pointSize()))

    if self.basePS:
      # базовое значение уже зафиксировано - масштабируем 
      delta = rect.height() - textH
      if delta > 2 * self.basePS[1]:   deltaPS = 1
      elif delta < 1.5 * self.basePS[1]: deltaPS = -1  
      else:                              deltaPS = 0

      if deltaPS:
        font.setPointSize(font.pointSize() + deltaPS)
        self.llData.setFont(font)               

    else:    
      # первая отрисовка лицевой панели - захватываем базовые размеры для последующего масштабирования
      # TODO - проверить не повлияет ли стартовое восстановление прошлой геометрии окна
      self.basePS = (font.pointSize(), rect.height() - textH)'''  

    super().resizeEvent(event)