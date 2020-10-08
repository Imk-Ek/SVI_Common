

#import sys, traceback
import logging
from PyQt4 import QtCore, QtGui 
#import sstate

#from common import *
from vp_classes import *
import Results
#from fpPressure import Ui_fpPressure  
from fpVATP import Ui_fpVATP
from vinstr import CVInstr

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

class CPressure(CVInstr):
  """ виртуальный амперметр [В]"""
  #  measI - наименование измерительного канала, связанного с данным экземпляром амперметра
  #  widthD - суммарное кол-во выводимых знаков результата (БЕЗ учета запятой)
  #  precD  - кол-во знаков после запятой 
  #  formS  - строка форматирования для вывода результата (под НОВЫЙ метод format)

  def __init__(self,vCE, dcfg, dstate = {}, dSize={}, fTech = False):
    super().__init__(dcfg, dstate, fTech)

    self.vCE=vCE
    self.Name=dcfg['наименование']
    self.ParamMess=dSize['VPParam']
    self.InputUnit=[0,0,0]
    self.InputVal=[0,0,0]
    self.OutputVal=[0,0,0]
    self.InputUnit[0]=dSize['VPChModulNameList'][0]
    self.InputVal[0]=dSize['VPChNameList'][0]
    self.OutputVal[0]=dSize['VPChOutTypeList'][0]
    Results.Result_Dict[self.Name]={}
    Results.Result_Dict[self.Name][self.OutputVal[0]]=0
    Results.Result_Dict[self.Name]['В блокнот']=0
    self.InLight_Notepad=0
    self.ID_VP='0'
    self.LastProfil=''
    self.closeFlag=0
    # TODO обработку ошибок конфигурации
    if(self.ParamMess=='0'):
      self.measP = self.dictCfg["каналДавление"]
      self.dictCfg["meas"] = [self.measP] # фактически вносится в vinstrD
      self.Р_ed='кПа'
    if(self.ParamMess=='1'):
      self.timer = QtCore.QTimer()
      self.timer.timeout.connect(self.NewDataTimer)
      self.timer.start(1000)
    ######################################
    '''self.pStDict[(n,0)]=parts[0]
        self.pStDict[(n,1)]=parts[1]
        self.dictState['pStDict']=self.pStDict#
        # print<< self.pStDict
        # LL.I("Р".format(self.pStDict))
        #LL.I(parts[0])
        #LL.I(parts[1])
        n=n+1
    #LL.I(self.dictState['pStDict'])
    #self.pStDict1 = {}
    #self.pStDict1=self.dictState['pStDict']

    self.dictState.update'''
    ##################################
    self.widthD = 3 # 4
    self.precD = 1  # 3
    self.formS = "{:"+str(self.widthD)+"."+str(self.precD)+"f}"

    self.dSize=dSize
    self.width=self.dSize.setdefault('width',100)
    self.height=self.dSize.setdefault('height',100)
    self.x=self.dSize.setdefault('x',100)
    self.y=self.dSize.setdefault('y',100)
     
    self.winProbaID =CfmProbaID(self)
    self.winAboutVP =CfmAboutVP(self)
    self.winMessage =CfmMessage(self)
    self.win = CfpPressure(self.widthD + 1, self)

    self.LoadState()

  def LoadState(self):
    super().LoadState()


  def SaveState(self):
    super().SaveState()


  def NewData(self, ddata):
    if self.measP in ddata:
      self.win.lcdMain.display(self.formS.format(ddata[self.measP][1]))
      self.win.lblEd.setText(self.Р_ed)
      self.tmpVal=ddata[self.measP][1]
      self.timeT = ddata[self.measP][2] 
      #print(self.timeT)

    Results.Result_Dict[self.Name][self.OutputVal[0]]=self.tmpVal
    Results.Result_Dict[self.Name]['Параметр '+self.OutputVal[0]]='Давление'
    Results.Result_Dict[self.Name]['Единица '+self.OutputVal[0]]=self.Р_ed
    if(Results.Result_Dict[self.Name]['В блокнот']!=2):Results.Result_Dict[self.Name]['В блокнот']=self.InLight_Notepad
    Results.Result_Dict[self.Name]['ID_VP']=self.ID_VP
    Results.Result_Dict[self.Name]['LastProfil']=self.LastProfil
    if(Results.Result_Dict[self.Name]['В блокнот']==2):
        Results.Result_Dict[self.Name]['В блокнот']=0
        self.InLight_Notepad=0
    if (self.vCE.Close_Config_Flag==1)and(self.closeFlag==0): 
          self.closeFlag=1      
          self.win.close()

  def NewDataTimer(self):
    
   if(self.ParamMess=='1'): 
    
      self.lastP =8
      self.lastP=Results.Result_Dict[self.InputUnit[0]][self.InputVal[0]]

      self.win.lcdMain.display(self.formS.format(self.lastP))
      self.win.lblEd.setText(self.Р_ed)
      self.tmpVal=self.lastP
      self.timeT =0 #ddata[self.measI][2] 
      #print(self.timeT)

      if self.win.Reset_Flag==1:
        self.Val_min=self.tmpVal
        self.Val_max=self.tmpVal
        self.win.Reset_Flag=0
        self.win.win_Chart.Reset_Flag=0

      if self.tmpVal<self.Val_min:
        self.Val_min=self.tmpVal
      if self.tmpVal>self.Val_max:
        self.Val_max=self.tmpVal
      Results.Result_Dict[self.Name][self.OutputVal[0]]=self.tmpVal
   if (self.vCE.Close_Config_Flag==1)and(self.closeFlag==0): 
          self.closeFlag=1      
          self.win.close()

#---
class CfpPressure(QtGui.QMainWindow, Ui_fpVATP):
#class CfpPressure(QtGui.QMainWindow, Ui_fpPressure):
  """ лицевая панель виртуального амперметра  
        vPressure  - экземпляр виртуального амперметра, соответствующий данной панели
        basePS - (pointSize, height) базовая связка для масштабирования наименования физ-величины (llData)  
     """
      
  def __init__(self, numDigits, vPressure):
    """ numDigits - суммарное кол-во выводимых знаков результата (C учетом запятой) """
    super(CfpPressure, self).__init__() 
    self.setupUi(self)
    self.setStyleSheet("QMainWindow {background: '#e268de';}")#969393
    self.Type=6
    self.Reset_Flag=1
    self.vPressure = vPressure

    rect = QtCore.QRect()   
    w=self.vPressure.width 
    h=self.vPressure.height
    x=self.vPressure.x         
    y=self.vPressure.y  
    rect = QtCore.QRect(x,y,w,h) 
    rect.setRect(x,y,w,h) 
    self.setGeometry(rect)
    
    self.vPressure.ID_VP=self.vPressure.dSize.setdefault('ID_VP','0')
    self.lblID.setText(str(self.vPressure.ID_VP))
     

    self.basePS = None
    #self.lcdMain.setDigitCount(numDigits)
    self.lcdMain.setDigitCount(4)
    self.tbSaveToNotepad_.clicked.connect(self.on_tbSaveToNotepad_clicked)

    # Common menu of VP
    self.actTech = QtGui.QAction("Проба", self) 
    self.actTech.triggered.connect(self.on_Proba_toggle)  
    self.menubar.addAction(self.actTech)

    self.actTech = QtGui.QAction("О приборе", self) 
    self.actTech.triggered.connect(self.on_AboutVP_toggle)  
    self.menubar.addAction(self.actTech)
    ## End of common menu of VP
    

  def on_Chart_View(self):
      self.win_Chart.show()

  def show(self, newsize = None):
    """ newsize - экземпляр QSize для передачи новых размеров окна """
    super().show()   # важно выполнить ПЕРЕД resize - иначе resize может не пройти
    if newsize:  self.resize(newsize)

  def timerEvent(self, e):
  #Отображение даты по таймеру
        if (self.vPressure.vCE.Close_Config_Flag==1)and(self.vPressure.closeFlag==0): 
          self.vPressure.closeFlag=1      
          self.close()


  def closeEvent(self, event):
    self.vPressure.SaveState()
    rect = self.geometry()
    self.vPressure.dSize['x'] = rect.left()
    self.vPressure.dSize['y'] = rect.top()
    self.vPressure.dSize['height'] = rect.height() 
    self.vPressure.dSize['width'] = rect.width()
    event.accept() 

  def on_tbSaveToNotepad_clicked(self):
      if(Results.Result_Dict[self.vPressure.Name]['В блокнот']==0):
        self.vPressure.ID_VP=self.lblID.text()
        self.vPressure.dSize['ID_VP']=self.vPressure.ID_VP
        self.vPressure.InLight_Notepad=1
      q=0 

  def on_Proba_toggle(self):
      self.vPressure.winProbaID.show()
      w=0

  def on_AboutVP_toggle(self):
      self.vPressure.winAboutVP.show()
      w=0

  def resizeEvent(self, event):
    a=1
    '''
    rect = self.centralwidget.geometry()
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
      self.basePS = (font.pointSize(), rect.height() - textH)  

    super().resizeEvent(event)'''
 
#---
