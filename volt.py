

import logging
from PyQt4 import QtCore, QtGui 
#from fpVolt import Ui_fpVolt
from fpVATP import Ui_fpVATP
from fmOtherSettingV import Ui_fmOtherSettingV
from vinstr import *
from vp_classes import *
#LL = logging.getLogger('SVI')

class CVolt(CVInstr):
  """ виртуальный вольтметр [В]"""
  #  measN - наименование измерительного канала, связанного с данным экземпляром вольтметра
  #  widthD - суммарное кол-во выводимых знаков результата (БЕЗ учета запятой)
  #  precD  - кол-во знаков после запятой 
  #  formS  - строка форматирования для вывода результата (под НОВЫЙ метод format)

  def __init__(self,vCE, dcfg, dstate = {}, dSize={}, fTech = False):#  dSize,
    """ Инициализация вольтметра"""
    super().__init__(dcfg, dstate, fTech)
    self.Name=dcfg['наименование']
    self.vCE=vCE
    self.closeFlag=0 
    # TODO обработку ошибок конфигурации
    self.measN = self.dictCfg["каналНапряжение"]
    self.dictCfg["meas"] = [self.measN] # фактически вносится в vinstrD
    self.V_ed='В'
    self.V_ed1='мВ'
    self._fDlog=False
    #self._fDlog=True
    self.widthD = 6 # 4
    self.precD = 4  # 3
    self.formS = "{:"+str(self.widthD)+"."+str(self.precD)+"f}"
    self.InputUnit=[0,0,0]
    self.InputVal=[0,0,0]
    self.OutputVal=[0,0,0]
    self.InputUnit[0]=dSize['VPChModulNameList'][0]
    self.InputVal[0]=dSize['VPChNameList'][0]
    self.OutputVal[0]=dSize['VPChOutTypeList'][0]
    self.OutputVal[1]=dSize['VPChOutTypeList'][1]
    Results.Result_Dict[self.Name]={}
    Results.Result_Dict[self.Name][self.OutputVal[0]]=0
    Results.Result_Dict[self.Name][self.OutputVal[1]]=0
    Results.Result_Dict[self.Name]['В блокнот']=0
    self.InLight_Notepad=0
    self.ID_VP='0'
    self.LastProfil=''
    self.dSize=dSize
    self.width=self.dSize.setdefault('width',100)
    self.height=self.dSize.setdefault('height',100)
    self.x=self.dSize.setdefault('x',100)
    self.y=self.dSize.setdefault('y',100) 

    self.CountFilter_2=1
    self.CurrCountFilter_2=1
    self.U_Sum_Filter_2=0
    self.U_Filter_2=0

    self.winProbaID =CfmProbaID(self)
    self.winAboutVP =CfmAboutVP(self)
    self.winMessage =CfmMessage(self)
    self.win = CfpVolt(self.widthD + 1, self)
    self.winOtherSettingV = CfmOtherSettingV(self)

    self.LoadState()

  def LoadState(self):
    super().LoadState()
  def SaveState(self):
    super().SaveState()


  def NewData(self, ddata):
    if (self.vCE.Close_Config_Flag==1)and(self.closeFlag==0): 
          self.closeFlag=1      
          self.win.close()
    """ Основной цикл по "прерыванию" из драйвера """
    if self.measN in ddata:

      self.mV=ddata[self.measN][1]
      if(self.CurrCountFilter_2<=self.CountFilter_2):
           self.U_Sum_Filter_2=self.U_Sum_Filter_2+self.mV
           self.CurrCountFilter_2=self.CurrCountFilter_2+1
      if(self.CurrCountFilter_2>=self.CountFilter_2):
           self.U_Filter_2=self.U_Sum_Filter_2/self.CurrCountFilter_2
           self.U_Sum_Filter_2=0
           self.CurrCountFilter_2=0
      #self.U_Filter_2=1.1234567
      self.win.lcdMain.display(self.formS.format(self.U_Filter_2))
      self.win.lblEd.setText(self.V_ed)
      self.tmpVal=self.U_Filter_2
      U=self.tmpVal
      if self._fDlog: print("U = {} ".format(U))
      Results.Result_Dict[self.Name][self.OutputVal[0]]=self.tmpVal
      Results.Result_Dict[self.Name]['Параметр '+self.OutputVal[0]]='Напряжение'
      Results.Result_Dict[self.Name]['Единица '+self.OutputVal[0]]=self.V_ed

      Results.Result_Dict[self.Name][self.OutputVal[1]]=self.tmpVal*1000
      Results.Result_Dict[self.Name]['Параметр '+self.OutputVal[1]]='Напряжение'
      Results.Result_Dict[self.Name]['Единица '+self.OutputVal[1]]=self.V_ed1
    if(Results.Result_Dict[self.Name]['В блокнот']!=2):
        Results.Result_Dict[self.Name]['В блокнот']=self.InLight_Notepad
    Results.Result_Dict[self.Name]['ID_VP']=self.ID_VP
    Results.Result_Dict[self.Name]['LastProfil']=self.LastProfil
    if(Results.Result_Dict[self.Name]['В блокнот']==2):
        Results.Result_Dict[self.Name]['В блокнот']=0
        self.InLight_Notepad=0



class CfmOtherSettingV(QtGui.QMainWindow, Ui_fmOtherSettingV):
  """ лицевая панель формы  прочих настроек виртуального вольтметра """  
  """      vVolt  - экземпляр виртуального вольтметра, соответствующий данной панели
        basePS - (pointSize, height) базовая связка для масштабирования наименования физ-величины (llData)  
     """
      
  def __init__(self, vOs):
    """ Инициализация формы формы  прочих настроек виртуального вольтметра """
    """ numDigits - суммарное кол-во выводимых знаков результата (C учетом запятой) """
    super(CfmOtherSettingV, self).__init__() 
    self.setupUi(self)
    self.vOs = vOs
    self.tbSaveSettingV.clicked.connect(self.on_tbSaveSettingV_toggle)

  def on_tbSaveSettingV_toggle(self):
    """ сохранение настроек"""
    try:
      self.vOs.CountFilter_2 = eval(self.leCounts.text(), {}, {})
    except:
     q=0
    qq=0

#---

#class CfpVolt(QtGui.QMainWindow, Ui_fpVolt):
class CfpVolt(QtGui.QMainWindow, Ui_fpVATP):
  """ лицевая панель виртуального вольтметра  
        vVolt  - экземпляр виртуального вольтметра, соответствующий данной панели
        basePS - (pointSize, height) базовая связка для масштабирования наименования физ-величины (llData)  
     """
      
  def __init__(self, numDigits, vVolt):
    """ numDigits - суммарное кол-во выводимых знаков результата (C учетом запятой) """
    super(CfpVolt, self).__init__() 
    self.setupUi(self)
    self.setStyleSheet("QMainWindow {background: '#B0FEA7';}")
    self.vVolt = vVolt

    self.basePS = None
    self.lcdMain.setDigitCount(numDigits)
    self.lcdMain.setDigitCount(6)
    self.Type=2
    self.Reset_Flag=1
    rect = QtCore.QRect()   
    w=self.vVolt.width 
    h=self.vVolt.height
    x=self.vVolt.x         
    y=self.vVolt.y  
    rect = QtCore.QRect(x,y,w,h) 
    rect.setRect(x,y,w,h) 
    self.setGeometry(rect)  

    self.vVolt.ID_VP=self.vVolt.dSize.setdefault('ID_VP','0')
    self.lblID.setText(str(self.vVolt.ID_VP))


    self.actTech = QtGui.QAction("Настройка", self) 
    self.actTech.triggered.connect(self.on_Setting)  
    self.menubar.addAction(self.actTech)
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
    ## End of common menu of VP

  def on_tbSaveToNotepad_clicked(self):
      if(Results.Result_Dict[self.vVolt.Name]['В блокнот']==0):
        self.vVolt.ID_VP=self.lblID.text()
        self.vVolt.dSize['ID_VP']=self.vVolt.ID_VP
        self.vVolt.InLight_Notepad=1
      q=0     

  def on_Setting(self):
   self.vVolt.winOtherSettingV.show()
   q=0

  def show(self, newsize = None):
    """ newsize - экземпляр QSize для передачи новых размеров окна """
    super().show()   # важно выполнить ПЕРЕД resize - иначе resize может не пройти
    if newsize:  self.resize(newsize)

  def closeEvent(self, event):
    self.vVolt.SaveState()
    rect = self.geometry()
    self.vVolt.dSize['x'] = rect.left()
    self.vVolt.dSize['y'] = rect.top()
    self.vVolt.dSize['height'] = rect.height() 
    self.vVolt.dSize['width'] = rect.width()
    event.accept() 

  def timerEvent(self, e):
  #Отображение даты по таймеру
        if (self.vVolt.vCE.Close_Config_Flag==1)and(self.vVolt.closeFlag==0): 
          self.vVolt.closeFlag=1      
          self.close()

  def on_Proba_toggle(self):
      self.vVolt.winProbaID.show()
      w=0

  def on_AboutVP_toggle(self):
      self.vVolt.winAboutVP.show()
      w=0

  def resizeEvent(self, event):
    a=1
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
      self.basePS = (font.pointSize(), rect.height() - textH)  

    super().resizeEvent(event)'''