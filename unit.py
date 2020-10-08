

#import sys, traceback
import logging
from PyQt4 import QtCore, QtGui 
from fpUnit import Ui_fpUnit
from vinstr import CVInstr
#LL = logging.getLogger('SVI')

class CUnit(CVInstr):
  """ виртуальный """
  #  measN - наименование измерительного канала, связанного с данным экземпляром вольтметра
  #  widthD - суммарное кол-во выводимых знаков результата (БЕЗ учета запятой)
  #  precD  - кол-во знаков после запятой 
  #  formS  - строка форматирования для вывода результата (под НОВЫЙ метод format)

  def __init__(self, dcfg, dstate = {}, fTech = False):
    super().__init__(dcfg, dstate, fTech)
    self.Name=dcfg['наименование']
    # TODO обработку ошибок конфигурации
    self.measN = self.dictCfg["канал_"]
    self.dictCfg["meas"] = [self.measN] # фактически вносится в vinstrD
    self.InputUnit=['0','0','0']
    self.InputVal=['0','0','0']
    self.MessMode=0
    self.InputUnit[0]=self.dictCfg["входной_прибор_1"]
    self.InputVal[0]=self.dictCfg["входная_величина_1"]
    self.InputUnit[1]=self.dictCfg["входной_прибор_2"]
    self.InputVal[1]=self.dictCfg["входная_величина_2"]
    self.widthD = 6 # 4
    self.precD = 3  # 3
    self.tmpVal4=0
    self.tmpVal5=0
    self.formS = "{:"+str(self.widthD)+"."+str(self.precD)+"f}"
    self.win = CfpUnit(self.widthD + 1, self)
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

  def Proceed(self):
    self.tmpVal4=Results.Result_Dict[self.InputUnit[0]][self.InputVal[0]]
    self.tmpVal5=Results.Result_Dict[(self.InputUnit[1])][self.InputVal[1]]
    self.tmpVal6=Results.Result_Dict[(self.InputUnit[2])][self.InputVal[2]]
    self.win.llData_2.setText(str(self.tmpVal4))
    self.win.llData_3.setText(str(self.tmpVal5))
    Results.Result_Dict[(self.Name)][('Value')]=self.tmpVal4
    Results.Result_Dict[(self.Name)][('EdIzm')]=0
    q=1
#---
class CfpUnit(QtGui.QMainWindow, Ui_fpUnit):
  """ лицевая панель виртуального вольтметра  
        vVolt  - экземпляр виртуального вольтметра, соответствующий данной панели
        basePS - (pointSize, height) базовая связка для масштабирования наименования физ-величины (llData)  
     """
      
  def __init__(self, numDigits, vUnit):
    """ numDigits - суммарное кол-во выводимых знаков результата (C учетом запятой) """
    super(CfpUnit, self).__init__() 
    self.timer = QtCore.QTimer()    
    self.setupUi(self)
    self.vUnit = vUnit
    self.basePS = None
    self.lcdVolt.setDigitCount(numDigits)
    self.Type=2
    self.Reset_Flag=1
    self.actTech = QtGui.QAction("График", self) 
    self.actTech.triggered.connect(self.on_Chart_View)  
    self.menubar.addAction(self.actTech)
    self.timer.timeout.connect(self.on_Chart_View)
    self.timer.start(1000)
    
  def on_Chart_View(self):
    self.vUnit.Test()

  def show(self, newsize = None):
    """ newsize - экземпляр QSize для передачи новых размеров окна """
    super().show()   # важно выполнить ПЕРЕД resize - иначе resize может не пройти
    if newsize:  self.resize(newsize)

  def closeEvent(self, event):
    self.vUnit.SaveState()
    event.accept() 

  def resizeEvent(self, event):
    super().resizeEvent(event)