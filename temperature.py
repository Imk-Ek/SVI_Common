

import logging
from PyQt4 import QtCore, QtGui 

#from fpTemp import Ui_fpTemp
from fpVATP import Ui_fpVATP
from vinstr import *
from vp_classes import *
#LL = logging.getLogger('SVI')

class CTemp(CVInstr):
  """ виртуальный термометр [°C] """
  #  measT - наименование измерительного канала, связанного с данным экземпляром термометра
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
    Results.Result_Dict[self.Name]['В блокнот']=0
    self.Temp_ed='oC'
    self.InLight_Notepad=0
    self.ID_VP='0'
    self.LastProfil=''
    Results.Result_Dict[self.Name][self.OutputVal[0]]=0
    # TODO обработку ошибок конфигурации
    if(self.ParamMess=='0'):
      self.measT = self.dictCfg["каналТемпература"]
      self.dictCfg["meas"] = [self.measT] # фактически вносится в vinstrD

    if(self.ParamMess=='1'):
      self.timer = QtCore.QTimer()
      self.timer.timeout.connect(self.NewDataTimer)
      self.timer.start(1000)

    self.widthD = 4
    self.precD = 1
    self.formS = "{:"+str(self.widthD)+"."+str(self.precD)+"f}"


    self.dSize=dSize
    self.width=self.dSize.setdefault('width',100)
    self.height=self.dSize.setdefault('height',100)
    self.x=self.dSize.setdefault('x',100)
    self.y=self.dSize.setdefault('y',100) 
    

    self.winProbaID =CfmProbaID(self)
    self.winAboutVP =CfmAboutVP(self)
    self.winMessage =CfmMessage(self)
    self.win = CfpTemp(self.widthD + 1, self)
    self.win.lcdMain.display('888')
    self.LoadState()
    

  def LoadState(self):
    super().LoadState()

  def SaveState(self):
    super().SaveState()

  def NewData(self, ddata):
    self.win.lcdMain.display('999')
    if self.measT in ddata:
      self.win.lcdMain.display(self.formS.format(ddata[self.measT][1]))
      self.win.lblEd.setText(self.Temp_ed)
      self.tmpVal=ddata[self.measT][1]

    Results.Result_Dict[self.Name][self.OutputVal[0]]=self.tmpVal
    Results.Result_Dict[self.Name]['Параметр '+self.OutputVal[0]]='Температура'
    Results.Result_Dict[self.Name]['Единица '+self.OutputVal[0]]=self.Temp_ed
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
   if (self.vCE.Close_Config_Flag==1)and(self.closeFlag==0): 
          self.closeFlag=1      
          self.win.close() 
   if(self.ParamMess=='1'): 
    
      self.lastT =8
      self.lastT=Results.Result_Dict[self.InputUnit[0]][self.InputVal[0]]

      self.win.lcdMain.display(self.formS.format(self.lastT))
      self.win.lblEd.setText(self.Temp_ed)
      self.tmpVal=self.lastT
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
class CfpTemp(QtGui.QMainWindow, Ui_fpVATP):
#class CfpTemp(QtGui.QMainWindow, Ui_fpTemp):
  """ лицевая панель виртуального термометра  
       vTemp  - экземпляр виртуального термометра, соответствующий данной панели 
       basePS - (pointSize, height) базовая связка для масштабирования наименования физ-величины (llData)  """

  def __init__(self, numDigits, vTemp):
    """ numDigits - суммарное кол-во выводимых знаков результата (C учетом запятой) """
    super(CfpTemp, self).__init__() 
    self.setupUi(self)
    self.setStyleSheet("QMainWindow {background: '#F8FEA7';}")
    self.vTemp = vTemp  
    rect = QtCore.QRect()   
    w=self.vTemp.width 
    h=self.vTemp.height
    x=self.vTemp.x         
    y=self.vTemp.y  
    rect = QtCore.QRect(x,y,w,h) 
    rect.setRect(x,y,w,h) 
    self.setGeometry(rect)
    self.basePS = None
    self.lcdMain.setDigitCount(numDigits)
    self.tbSaveToNotepad_.clicked.connect(self.on_tbSaveToNotepad_clicked) 
    self.Type=3
    self.Reset_Flag=1

    self.vTemp.ID_VP=self.vTemp.dSize.setdefault('ID_VP','0')
    self.lblID.setText(str(self.vTemp.ID_VP))
    self.trAutoScan =None
    self.trAutoScan = self.startTimer(1000)

    # Common menu of VP
    self.actTech = QtGui.QAction("Проба", self) 
    self.actTech.triggered.connect(self.on_Proba_toggle)  
    self.menubar.addAction(self.actTech)

    self.actTech = QtGui.QAction("О приборе", self) 
    self.actTech.triggered.connect(self.on_AboutVP_toggle)  
    self.menubar.addAction(self.actTech)
    ## End of common menu of VP

    
  def on_tbSaveToNotepad_clicked(self):
     if(Results.Result_Dict[self.vTemp.Name]['В блокнот']==0):
        self.vTemp.ID_VP=self.lblID.text()
        self.vTemp.dSize['ID_VP']=self.vTemp.ID_VP
        self.vTemp.InLight_Notepad=1
     q=0 

  def show(self, newsize = None):
    """ newsize - экземпляр QSize для передачи новых размеров окна """
    super().show()   # важно выполнить ПЕРЕД resize - иначе resize может не пройти
    if newsize:  self.resize(newsize)

  def timerEvent(self, e):
  #Отображение даты по таймеру
        if (self.vTemp.vCE.Close_Config_Flag==1)and(self.vTemp.closeFlag==0): 
          self.vTemp.closeFlag=1      
          self.close()

  def closeEvent(self, event):
    self.vTemp.SaveState()
    rect = self.geometry()
    self.vTemp.dSize['x'] = rect.left()
    self.vTemp.dSize['y'] = rect.top()
    self.vTemp.dSize['height'] = rect.height() 
    self.vTemp.dSize['width'] = rect.width()
    event.accept() 

  def on_Proba_toggle(self):
      self.vTemp.winProbaID.show()
      w=0

  def on_AboutVP_toggle(self):
      self.vTemp.winAboutVP.show()
      w=0

  def resizeEvent(self, event):
    a=1
    '''
    rect = self.centralwidget.geometry()
    font = self.llData.font()
    fm = QtGui.QFontMetrics(font) 
    textH = fm.boundingRect(self.llData.text()).height()

    #print("layout.height = {} text.height = {} pointS = {}".format(rect.height(), textH, font.pointSize()))

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