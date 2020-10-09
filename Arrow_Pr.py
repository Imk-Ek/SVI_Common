
import logging
import os, sip
import subprocess
import Results
from PyQt4.QtCore import QObject, Qt
from PyQt4.QtGui import QHBoxLayout, QVBoxLayout
from ArrowPribors import ZoneWidget_4, ZoneArrowWidget
from PyQt4 import QtCore, QtGui 
from datetime import datetime
from common import PCFlag
if PCFlag==1:
  from fpArrow_Pr import Ui_fpArrow_Pr
  from Arrow_Pr_Dlg import Ui_Arrow_Pr_Dlg
if PCFlag==2:
  from fpArrow_Pr_t import Ui_fpArrow_Pr
  from Arrow_Pr_Dlg_t import Ui_Arrow_Pr_Dlg
from vinstr import CVInstr
from vp_classes import *
#LL = logging.getLogger('SVI')

class CArrow_Pr(CVInstr):
  """ Виртуальный прибор -регистратор. Записывает данные с подключенных ВП с заданным интервалом. Есть 
   возможность сохранения в файл"""

  def __init__(self,vCE,  dcfg, dstate = {}, dSize={}, fTech = False):
    """ Инициализация класса регистратора """
    super().__init__(dcfg, dstate, fTech)
    self.vCE=vCE
    
    self.closeFlag=0 
    self.StartFlag=0;
    self.dSize=dSize
    self.Name=dcfg['наименование']
    self._EdIzm="__"
    #self.vCond.ID_VP=self.vCond.dSize.setdefault('ID_VP','0')
    #self.lblID.setText(str(self.vCond.ID_VP))
    self.MidVal=float(self.dSize.setdefault('MidVal','10'))
    self.DeltaVal=float(self.dSize.setdefault('DeltaVal','2'))
    self.ArrowPrType=int(self.dSize.setdefault('ArrowPrType','0'))
    #self.MidVal=10.0
    #self.DeltaVal=2.0
    #self.ArrowPrType=0
    self.tmpVal=0
    self.tmpVal_Ed="_"
    # TODO обработку ошибок конфигурации
    self.measN ='0'# self.dictCfg["канал_"]
    self.dictCfg["meas"] = [self.measN] # фактически вносится в vinstrD
    self.ParamMess=dSize['VPParam']
    self.InputUnit=[0,0,0,0,0,0]
    self.InputVal=[0,0,0,0,0,0]
    self.InputVal_ParName=[0,0,0,0,0,0]
    self.InputVal_EdName=[0,0,0,0,0,0]
    self.OutputVal=[0,0,0]
    self.InputUnit[0]=dSize['VPChModulNameList'][0]
    #self.InputUnit[1]=dSize['VPChModulNameList'][1]
    #self.InputUnit[2]=dSize['VPChModulNameList'][2]
    self.InputVal[0]=dSize['VPChNameList'][0]
    #self.InputVal[1]=dSize['VPChNameList'][1]
    #self.InputVal[2]=dSize['VPChNameList'][2]
    self.InputVal_ParName[0]=''
    self.InputVal_EdName[0]=''
    self.InputVal_ParName[1]=''
    self.InputVal_EdName[1]=''
    self.InputVal_ParName[2]=''
    self.InputVal_EdName[2]=''
    self.InputVal_ParName[3]=''
    self.InLight_Notepad=0
    self.ID_VP='0'
    self.widthD = 7
    self.precD = 3
    self.formS = "{:"+str(self.widthD)+"."+str(self.precD)+"f}" 
    self.row_counter=0
    self.widthD = 6 # 4
    self.precD = 3  # 3
    self.formS = "{:"+str(self.widthD)+"."+str(self.precD)+"f}"

  

    self.win = CfpArrow_Pr(self.widthD + 1, self)
    self.winAboutVP =CfmAboutVP(self)
    self.dSize=dSize
    self.LoadState()
    #self.win.width=self.dSize.setdefault('width',100)
    #self.win.height=self.dSize.setdefault('height',100)
    self.win.x=self.dSize.setdefault('x',100)
    self.win.y=self.dSize.setdefault('y',100)  

    #self.InitArrowPribor()
    self.winParam  = CArrow_Pr_Dlg(self)


    self.InitDlgParam()
    #self.dSize=dSize
    #self.LoadState()

    self.tmpVal4=0
    self.tmpVal5=0
    self.tmpVal6=0
    self.tmpVal4_Ed=0
    self.tmpVal5_Ed=0
    self.tmpVal6_Ed=0
    self.InitArrowPribor()

  def LoadState(self):
    super().LoadState()
 
  def SaveState(self):
    super().SaveState()


  def NewData(self, ddata):
    q=0

  def Proceed(self):
    """Основной метод. Выполняется по таймеру с изменяемым интервалом
     Запись текущей даты и времени """
    a=datetime.today()
    a1=a.date()
    a2=a.time()
    dt1=str(a1)+"  \t"+a2.strftime("%H:%M:%S") 
    if (self.StartFlag==0):
        self.StartFlag=1
        self.InitArrowPribor()

    if(self.InputUnit[0]!='0'):
        self.tmpVal=Results.Result_Dict[self.InputUnit[0]][self.InputVal[0]]
        self.tmpVal_Ed=Results.Result_Dict[self.InputUnit[0]]['Единица '+self.InputVal[0]]
        self.win.zw4.setValue(self.tmpVal)
        self.win.zw4.ed_=self.tmpVal_Ed
        #self.win.zw4.ed_=self.vCE._EdIzm
    self.win.zw4.repaint()




  def InitDlgParam(self):
    #self.winParam.leEdIzm.setText(self._EdIzm)
    self.winParam.leMidVal.setText(str(self.MidVal))
    self.winParam.leDeltaVal.setText(str(self.DeltaVal))
    if (self.ArrowPrType==0): self.winParam.rbStripType.setChecked(1)
    if (self.ArrowPrType==1):  self.winParam.rbAngleType.setChecked(1)

    a=0

  def InitArrowPribor(self):
    if(1<2):#(self.ArrowPrType!=self.win.ArrowPrType):
      if(self.win.ArrowPrType!=-1):
         sip.delete(self.win.zw4)

      self.rect = QtCore.QRect()
      if(self.ArrowPrType==0):
        #if(self.win.ArrowPrType!=-1): sip.delete(self.win.zw4)
        self.win.zw4 = ZoneWidget_4(self.win.centralwidget)


        
        self.rect.setWidth(self.win.zw4.width()+self.win.x) 
        #self.rect.setWidth(250+self.win.x) 
        self.rect.setHeight(self.win.zw4.height()+self.win.menubar.height()+self.win.y)
        #self.rect.setHeight(500+self.win.menubar.height()+self.win.y)
        self.rect.setLeft(self.win.x)                 
        self.rect.setTop(self.win.y)    
        self.win.setGeometry(self.rect)
        self.win.ArrowPrType=0

      if(self.ArrowPrType==1):
        #if(self.win.ArrowPrType!=-1): sip.delete(self.win.zw4)
        self.win.zw4  = ZoneArrowWidget(self.win.centralwidget)
        #sip.delete(self.win.zw4)
        #self.win.zw4 = ZoneWidget_4(self.win.centralwidget)



        #self.rect.setWidth(403+self.win.x) 
        self.rect.setWidth(self.win.zw4.width()+self.win.x) 
        self.rect.setHeight(self.win.zw4.height()+self.win.menubar.height()+self.win.y)
        #self.rect.setHeight(403+self.win.menubar.height()+self.win.y)
        self.rect.setLeft(self.win.x)         
        self.rect.setTop(self.win.y)    
        self.win.setGeometry(self.rect)
        self.win.ArrowPrType=1
    a=0
    self.win.zw4.ed_=self._EdIzm
    self.win.zw4.center_value=self.MidVal
    self.win.zw4.delta_value=self.DeltaVal
    self.win.zw4.setVisible(1)
    self.win.zw4.repaint()

   
#---
class CfpArrow_Pr(QtGui.QMainWindow, Ui_fpArrow_Pr):
  """ лицевая панель виртуального вольтметра  
        vVolt  - экземпляр виртуального вольтметра, соответствующий данной панели
        basePS - (pointSize, height) базовая связка для масштабирования наименования физ-величины (llData)  
     """
      
  def __init__(self, numDigits, vNotepad):
    """ numDigits - суммарное кол-во выводимых знаков результата (C учетом запятой) """
    super(CfpArrow_Pr, self).__init__()     
    self.setupUi(self)
    self.ArrowPrType=-1

            # Common menu of VP
    self.actTech = QtGui.QAction("Параметры", self) 
    self.actTech.triggered.connect(self.on_btnParam)  
    self.menubar.addAction(self.actTech)

    self.actTech = QtGui.QAction("О приборе", self) 
    self.actTech.triggered.connect(self.on_AboutVP_toggle)  
    self.menubar.addAction(self.actTech)

    ## End of common menu of VP
    self.setStyleSheet("QMainWindow {background: '#D8FABA';}")
    self.vCE = vNotepad
    self.basePS = None
    self.Type=2
    self.Reset_Flag=1
    self.timer = QtCore.QTimer()
    self.timer.timeout.connect(self.on_Timer_toggle)    
    self.timer.start(1000)
      
  def StartTable(self):
      """  Запуск таймера обработки таблицы"""
      self.timer.start(1000)  

  def on_Timer_value_Changed(self):
      """ Событие таймера"""
      tmpi=self.spinBox.value()*1000
      self.timer.setInterval(tmpi)

  def on_btnParam(self):
      self.vCE.InitDlgParam()
      self.vCE.winParam.show() 
      q=0



  def show(self, newsize = None):
    """ newsize - экземпляр QSize для передачи новых размеров окна """
    super().show()   # важно выполнить ПЕРЕД resize - иначе resize может не пройти
    if newsize:  self.resize(newsize)

  def closeEvent(self, event):
    """ Событие закрытия формы """
    rect = self.geometry()
    self.vCE.dSize['x'] = rect.left()
    self.vCE.dSize['y'] = rect.top()
    self.vCE.dSize['height'] = rect.height() 
    self.vCE.dSize['width'] = rect.width()
    self.vCE.SaveState()
    if(self.vCE .winParam.close()==0):self.vCE .winParam.close()
    event.accept() 
    

  def resizeEvent(self, event):
    """ событие изменения размера окна """
    super().resizeEvent(event)
    self.zw4.setGeometry(QtCore.QRect(0, 0, self.width, self.height))

  def on_Timer_toggle(self):
    """ событие основного таймера   """
    self.vCE.Proceed()
    if (self.vCE.vCE.Close_Config_Flag==1)and(self.vCE.closeFlag==0): 
          self.vCE.closeFlag=1      
          self.close()
          self.timer.stop()
          self.delete()
          a=0

  def on_AboutVP_toggle(self):
      self.vCE.winAboutVP.show()
      w=0

class CArrow_Pr_Dlg(QtGui.QMainWindow, Ui_Arrow_Pr_Dlg):

  def __init__(self, win):     
    super().__init__()
    self.setupUi(self)
    self.win = win
    self.ShowFlag=0
    #self.tbSaveIon_.clicked.connect(self.on_tbSaveIon_clicked)
    self.setWindowTitle("Настройка прибора");
    self.btnSave.clicked.connect(self.on_btnSave)

  def on_btnSave(self):
      q=""
      #self.win._EdIzm=self.leEdIzm.text()
      self.win.MidVal=float(self.leMidVal.text())
      self.win.DeltaVal=float(self.leDeltaVal.text())
      if (self.rbStripType.isChecked()):
          self.win.ArrowPrType=0 
          self.win.InitArrowPribor()
      if (self.rbAngleType.isChecked()):
          self.win.ArrowPrType=1 
          self.win.InitArrowPribor()
      self.win.dSize['MidVal']=str(self.win.MidVal)
      self.win.dSize['DeltaVal']=str(self.win.DeltaVal)
      self.win.dSize['ArrowPrType']=str(self.win.ArrowPrType)
      self.win.SaveState()

      q=0