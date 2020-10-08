
import logging
from PyQt4 import QtCore, QtGui 

#from fpAmper import Ui_fpAmper
from fpVATP import Ui_fpVATP
from vinstr import *
from vp_classes import *
#LL = logging.getLogger('SVI')

class CAmper(CVInstr):
  """ виртуальный амперметр [В]"""
  #  measI - наименование измерительного канала, связанного с данным экземпляром амперметра
  #  widthD - суммарное кол-во выводимых знаков результата (БЕЗ учета запятой)
  #  precD  - кол-во знаков после запятой 
  #  formS  - строка форматирования для вывода результата (под НОВЫЙ метод format)

  def __init__(self,vCE,  dcfg, dstate = {}, dSize={}, fTech = False):
    super().__init__(dcfg, dstate, fTech)
    self.vCE=vCE
    self.closeFlag=0 
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
    self.I_ed='нА'
    self.InLight_Notepad=0
    self.ID_VP='0'
    self.LastProfil=''
    # TODO обработку ошибок конфигурации
    if(self.ParamMess=='0'):
      self.measI = self.dictCfg["каналТок"]
      self.dictCfg["meas"] = [self.measI] # фактически вносится в vinstrD

    if(self.ParamMess=='1'):
      self.timer = QtCore.QTimer()
      self.timer.timeout.connect(self.NewDataTimer)
      self.timer.start(1000)

    self.widthD = 6 # 4
    self.precD = 2  # 3
    self.formS = "{:"+str(self.widthD)+"."+str(self.precD)+"f}"
    self.dSize=dSize
    self.width=self.dSize.setdefault('width',100)
    self.height=self.dSize.setdefault('height',100)
    self.x=self.dSize.setdefault('x',100)
    self.y=self.dSize.setdefault('y',100) 
    self.tmpVal=0.0
    self.winProbaID =CfmProbaID(self)
    self.winAboutVP =CfmAboutVP(self)
    self.winMessage =CfmMessage(self)
    self.win = CfpAmper(self.widthD + 1, self)

    self.LoadState()

  def LoadState(self):
    super().LoadState()

  def SaveState(self):
    super().SaveState()

  def NewData(self, ddata):
    if (self.vCE.Close_Config_Flag==1)and(self.closeFlag==0): 
          self.closeFlag=1      
          self.win.close()
    if self.measI in ddata:
      self.tmpVal=ddata[self.measI][1]
      if(self.tmpVal<0): self.tmpVal=self.tmpVal*(-1)
      self.win.lcdMain.display(self.formS.format(self.tmpVal))
      #tmpa=1234.123456
      #self.win.lcdMain.display(self.formS.format(tmpa))
      self.win.lblEd.setText(self.I_ed)
      self.tmpVal=ddata[self.measI][1]
      self.timeT = ddata[self.measI][2] 
      #print(self.timeT)

    Results.Result_Dict[self.Name][self.OutputVal[0]]=self.tmpVal
    Results.Result_Dict[self.Name]['Параметр '+self.OutputVal[0]]='Ток'
    Results.Result_Dict[self.Name]['Единица '+self.OutputVal[0]]=self.I_ed
    if(Results.Result_Dict[self.Name]['В блокнот']!=2):
        Results.Result_Dict[self.Name]['В блокнот']=self.InLight_Notepad
    Results.Result_Dict[self.Name]['LastProfil']=self.LastProfil
    Results.Result_Dict[self.Name]['ID_VP']=self.ID_VP
    if(Results.Result_Dict[self.Name]['В блокнот']==2):
        Results.Result_Dict[self.Name]['В блокнот']=0
        self.InLight_Notepad=0

  def NewDataTimer(self):
   if (self.vCE.Close_Config_Flag==1)and(self.closeFlag==0): 
          self.closeFlag=1      
          self.win.close() 
   if(self.ParamMess=='1'): 
    
      self.lastI =8
      self.lastI=Results.Result_Dict[self.InputUnit[0]][self.InputVal[0]]

      self.win.lcdMain.display(self.formS.format(self.lastI))
      self.win.lblEd.setText(self.I_ed)
      self.tmpVal=self.lastI
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
#---
class CfpAmper(QtGui.QMainWindow, Ui_fpVATP):
#class CfpAmper(QtGui.QMainWindow, Ui_fpAmper):
  """ лицевая панель виртуального амперметра  
        vAmper  - экземпляр виртуального амперметра, соответствующий данной панели
        basePS - (pointSize, height) базовая связка для масштабирования наименования физ-величины (llData)  
     """
      
  def __init__(self, numDigits, vAmper):
    """ numDigits - суммарное кол-во выводимых знаков результата (C учетом запятой) """
    super(CfpAmper, self).__init__() 
    self.setupUi(self)
    self.setStyleSheet("QMainWindow {background: '#A7B5FE';}")
    self.Type=1
    self.Reset_Flag=1
    self.vAmper = vAmper
    rect = QtCore.QRect()   
    w=self.vAmper.width 
    h=self.vAmper.height
    x=self.vAmper.x         
    y=self.vAmper.y  
    rect = QtCore.QRect(x,y,w,h) 
    rect.setRect(x,y,w,h) 
    self.setGeometry(rect)  

    self.vAmper.ID_VP=self.vAmper.dSize.setdefault('ID_VP','0')
    self.lblID.setText(str(self.vAmper.ID_VP))
    self.vAmper.dSize['ID_VP']=self.vAmper.ID_VP

    

    self.basePS = None
    self.lcdMain.setDigitCount(numDigits)
    self.tbSaveToNotepad_.clicked.connect(self.on_tbSaveToNotepad_clicked)
    self.trAutoScan =None
    self.trAutoScan = self.startTimer(1000) 

    # Common menu of VP
    self.actTech = QtGui.QAction("Проба", self) 
    self.actTech.triggered.connect(self.on_Proba_toggle)  
    self.menubar.addAction(self.actTech)

    self.actTech = QtGui.QAction("О приборе", self) 
    self.actTech.triggered.connect(self.on_AboutVP_toggle)  
    self.menubar.addAction(self.actTech)
    self.lcdMain.setDigitCount(6)
    ## End of common menu of VP

  def on_tbSaveToNotepad_clicked(self):
      if(Results.Result_Dict[self.vAmper.Name]['В блокнот']==0):
        self.vAmper.ID_VP=self.lblID.text()
        self.vAmper.InLight_Notepad=1
 

  def on_Chart_View(self):
      q=0

  def show(self, newsize = None):
    """ newsize - экземпляр QSize для передачи новых размеров окна """
    super().show()   # важно выполнить ПЕРЕД resize - иначе resize может не пройти
    if newsize:  self.resize(newsize)

  def timerEvent(self, e):
  #Отображение даты по таймеру
        if (self.vAmper.vCE.Close_Config_Flag==1)and(self.vAmper.closeFlag==0): 
          self.vAmper.closeFlag=1  
          self.timer.stop()    
          self.close()


  def closeEvent(self, event):
    self.vAmper.SaveState()
    rect = self.geometry()
    self.vAmper.dSize['x'] = rect.left()
    self.vAmper.dSize['y'] = rect.top()
    self.vAmper.dSize['height'] = rect.height() 
    self.vAmper.dSize['width'] = rect.width()
    event.accept() 

  def on_Proba_toggle(self):
      self.vAmper.winProbaID.show()
      w=0

  def on_AboutVP_toggle(self):
      self.vAmper.winAboutVP.show()
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