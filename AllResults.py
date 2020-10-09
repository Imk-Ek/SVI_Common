

#import sys, traceback
import logging
from PyQt4 import QtCore, QtGui 
#import sstate

from common import PCFlag
if PCFlag==1:from fpUnit import Ui_fpUnit
if PCFlag==2:from fpUnit_t import Ui_fpUnit
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
    self.InputEd=['0','0','0']

    self.InputUnit[0]=self.dictCfg["прибор_1"]
    self.InputVal[0]=self.dictCfg["величина_1"]
    self.InputEd[0]=self.dictCfg["единица_1"]

    self.InputUnit[1]=self.dictCfg["прибор_2"]
    self.InputVal[1]=self.dictCfg["величина_2"]
    self.InputEd[1]=self.dictCfg["единица_2"]

    self.widthD = 6 # 4
    self.precD = 3  # 3
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

  def Test(self):

    self.tmpVal4=Results.Result_Dict[self.InputUnit[0]][self.InputVal[0]]
    #self.tmpVal4=Results.Result_Dict[(self.InputUnit[0])][('EdIzm')]
    self.tmpVal5=Results.Result_Dict[(self.InputUnit[1])][self.InputVal[1]]
    #self.tmpVal4=Results.Result_Dict[(self.InputUnit[1])][('EdIzm')]
    #self.win.lcdVolt.display(self.formS.format(str(self.tmpVal4)))
    self.win.llData_2.setText(str(self.tmpVal4))
    self.win.llData_3.setText(str(self.tmpVal5))
    #self.win.lcdVolt.display(self.formS.format(self.tmpVal5))
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
    self.win_Chart = CfpChart(self)
    self.Reset_Flag=1

    self.actTech = QtGui.QAction("График", self) 
    self.actTech.triggered.connect(self.on_Chart_View)  
    self.menubar.addAction(self.actTech)
    self.timer.timeout.connect(self.on_Chart_View)
    self.timer.start(1000)
    

  def on_Chart_View(self):
    #self.win_Chart.show()
    self.vUnit.Test()


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