

import logging
from PyQt4 import QtCore, QtGui 
import Results
from common import PCFlag
if PCFlag==1: from fpInputUnit import Ui_fpInputUnit
if PCFlag==2: from fpInputUnit_t import Ui_fpInputUnit
from vinstr import CVInstr
#LL = logging.getLogger('SVI')


class CInputUnit_(CVInstr):
  """ виртуальный """
  #  measN - наименование измерительного канала, связанного с данным экземпляром вольтметра
  #  widthD - суммарное кол-во выводимых знаков результата (БЕЗ учета запятой)
  #  precD  - кол-во знаков после запятой 
  #  formS  - строка форматирования для вывода результата (под НОВЫЙ метод format)

  #def __init__(self, dcfg, dstate = {}, fTech = False):
  def __init__(self,vCE,  dcfg, dstate = {}, dSize={}, fTech = False):
    super().__init__(dcfg, dstate, fTech)
    self.vCE=vCE
    self.closeFlag=0 
    self.Name=dcfg['наименование']
    self.ParamMess=dSize['VPParam']
    self.OutputVal=[0,0,0,0]
    self.tmpVal1=0
    self.tmpVal2=0
    self.tmpVal3=0
    self.OutputVal[0]=dSize['VPChOutTypeList'][0]
    self.OutputVal[1]=dSize['VPChOutTypeList'][1]
    self.OutputVal[2]=dSize['VPChOutTypeList'][2]
    Results.Result_Dict[self.Name]={}
    Results.Result_Dict[self.Name][self.OutputVal[0]]=0
    Results.Result_Dict[self.Name][self.OutputVal[1]]=0
    Results.Result_Dict[self.Name][self.OutputVal[2]]=0
    self.widthD = 6 # 4
    self.precD = 3  # 3
    self.tmpVal4=0
    self.tmpVal5=0
    self.formS = "{:"+str(self.widthD)+"."+str(self.precD)+"f}"
    self.dSize=dSize
    self.win = CfpInputUnit(self.widthD + 1, self)
    self.LoadState()
    self.win.tmpVal1=self.win.leVal1.setText('0')
    self.win.tmpVal2=self.win.leVal2.setText('0')
    self.win.tmpVal3=self.win.leVal3.setText('0')				 
    rect = QtCore.QRect()
    self.win.width=self.dSize.setdefault('width',100)
    self.win.height=self.dSize.setdefault('height',100)
    self.win.x=self.dSize.setdefault('x',100)
    self.win.y=self.dSize.setdefault('y',100)       
    rect.setWidth(self.win.width) 
    rect.setHeight(self.win.height)
    rect.setLeft(self.win.x)         
    rect.setTop(self.win.y)    
    self.win.setGeometry(rect)
    self.trAutoScan =None
    #self.trAutoScan = self.startTimer(1000)
        
  def LoadState(self):
    super().LoadState()

  def SaveState(self):
    super().SaveState()

  def NewData(self, ddata):
    self.tmpVal4=Results.Result_Dict
    if self.measN in ddata:
      #self.win.lcdVolt.display(self.formS.format(ddata[self.measN][1]))
      self.tmpVal=ddata[self.measN][1]

  def Proceed(self):
    Results.Result_Dict[self.Name][self.OutputVal[0]]=float(self.tmpVal1)
    Results.Result_Dict[self.Name][self.OutputVal[1]]=int(self.tmpVal2)
    Results.Result_Dict[self.Name][self.OutputVal[2]]=int(self.tmpVal3)

    Results.Result_Dict[self.Name]['Параметр '+self.OutputVal[0]]='П.1'
    Results.Result_Dict[self.Name]['Единица '+self.OutputVal[0]]='ед.1.'

    Results.Result_Dict[self.Name]['Параметр '+self.OutputVal[1]]='П.2'
    Results.Result_Dict[self.Name]['Единица '+self.OutputVal[1]]='ед.2.'

    Results.Result_Dict[self.Name]['Параметр '+self.OutputVal[2]]='П.3'
    Results.Result_Dict[self.Name]['Единица '+self.OutputVal[2]]='ед.3.'	 
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
    self.Type=2
    self.Reset_Flag=1
    self.actTech = QtGui.QAction("График", self) 
    self.tbEnter.clicked.connect(self.on_tbEnter)  
    self.menubar.addAction(self.actTech)
    self.timer = QtCore.QTimer()
    self.timer.timeout.connect(self.on_timer)
    self.timer.start(1000)
    

  def on_timer(self):
    self.vUnit.Proceed()
    if (self.vUnit.vCE.Close_Config_Flag==1)and(self.vUnit.closeFlag==0): 
          self.vUnit.closeFlag=1      
          self.close()

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
    rect = self.geometry()
    self.vUnit.dSize['x'] = rect.left()
    self.vUnit.dSize['y'] = rect.top()
    self.vUnit.dSize['height'] = rect.height() 
    self.vUnit.dSize['width'] = rect.width()
    event.accept() 


  def resizeEvent(self, event):

    super().resizeEvent(event)