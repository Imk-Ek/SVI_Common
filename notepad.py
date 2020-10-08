
import logging
import os
import subprocess
import Results
from PyQt4 import QtCore, QtGui 
from datetime import datetime
from fmNotepad import Ui_fmNotepad
from vinstr import CVInstr
#LL = logging.getLogger('SVI')

class CNotepad(CVInstr):
  """ Виртуальный прибор -регистратор. Записывает данные с подключенных ВП с заданным интервалом. Есть 
   возможность сохранения в файл"""

  def __init__(self,vCE,  dcfg, dstate = {}, dSize={}, fTech = False):
    """ Инициализация класса регистратора """
    super().__init__(dcfg, dstate, fTech)
    self.vCE=vCE
    self.closeFlag=0 
    self.dSize=dSize
    self.Name=dcfg['наименование']
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
    self.InputUnit[1]=dSize['VPChModulNameList'][1]
    self.InputUnit[2]=dSize['VPChModulNameList'][2]
    self.InputVal[0]=dSize['VPChNameList'][0]
    self.InputVal[1]=dSize['VPChNameList'][1]
    self.InputVal[2]=dSize['VPChNameList'][2]
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
    self.win = CfmNotepad(self.widthD + 1, self)
    self.win.InitTable()
    self.win.StartTable()
    self.dSize=dSize
    self.LoadState()
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
    self.tmpVal4=0
    self.tmpVal5=0
    self.tmpVal6=0
    self.tmpVal4_Ed=0
    self.tmpVal5_Ed=0
    self.tmpVal6_Ed=0

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
    self.win.lblDateTime.setText(str(dt1))
    self.win.tableW.insertRow(self.row_counter)
    self.win.tableW.setItem(self.row_counter,0,QtGui.QTableWidgetItem(dt1))   
    # При наличии информации на входе 1 - запись данных
    if(self.InputUnit[0]!='0'):
        self.tmpVal4=Results.Result_Dict[self.InputUnit[0]][self.InputVal[0]]
        self.tmpVal4_Ed=Results.Result_Dict[self.InputUnit[0]]['Единица '+self.InputVal[0]]
        self.win.tableW.setItem(self.row_counter,1,QtGui.QTableWidgetItem(self.formS.format(self.tmpVal4)))
        self.win.tableW.setItem(self.row_counter,2,QtGui.QTableWidgetItem(str(self.tmpVal4_Ed)))
    # При наличии информации на входе 2 - запись данных
    if(self.InputUnit[1]!='0'): 
        self.tmpVal5=Results.Result_Dict[(self.InputUnit[1])][self.InputVal[1]]
        self.tmpVal5_Ed=Results.Result_Dict[self.InputUnit[1]]['Единица '+self.InputVal[1]]
        self.win.tableW.setItem(self.row_counter,3,QtGui.QTableWidgetItem(self.formS.format(self.tmpVal5)))
        self.win.tableW.setItem(self.row_counter,4,QtGui.QTableWidgetItem(str(self.tmpVal5_Ed)))
    # При наличии информации на входе 3 - запись данных
    if(self.InputUnit[2]!='0'): 
        self.tmpVal6=Results.Result_Dict[(self.InputUnit[2])][self.InputVal[2]]
        self.tmpVal6_Ed=Results.Result_Dict[self.InputUnit[2]]['Единица '+self.InputVal[2]]
        self.win.tableW.setItem(self.row_counter,5,QtGui.QTableWidgetItem(self.formS.format(self.tmpVal6)))
        self.win.tableW.setItem(self.row_counter,6,QtGui.QTableWidgetItem(str(self.tmpVal6_Ed)))
    # инкремент счетчика строк
    self.row_counter=self.row_counter+1 
#---
class CfmNotepad(QtGui.QMainWindow, Ui_fmNotepad):
  """ лицевая панель виртуального вольтметра  
        vVolt  - экземпляр виртуального вольтметра, соответствующий данной панели
        basePS - (pointSize, height) базовая связка для масштабирования наименования физ-величины (llData)  
     """
      
  def __init__(self, numDigits, vNotepad):
    """ numDigits - суммарное кол-во выводимых знаков результата (C учетом запятой) """
    super(CfmNotepad, self).__init__()     
    self.setupUi(self)
    self.setStyleSheet("QMainWindow {background: '#D8FABA';}")
    self.vNotepad = vNotepad
    self.basePS = None
    self.Type=2
    self.Reset_Flag=1
    self.timer = QtCore.QTimer()
    self.timer.timeout.connect(self.on_Timer_toggle)    
    self.spinBox.valueChanged.connect(self.on_Timer_value_Changed)
    self.spinBox.setValue(1)
    self.timer.start(1000)
    self.btnSave.clicked.connect(self.on_btnSave)
    self.btnClear.clicked.connect(self.on_btnClear)

  def InitTable(self):
      """ Инициализация таблицы блокнота  """
      tmpi=0
      self.tableW.setColumnCount(1)
      hName='Дата и время'
      self.tableW.setHorizontalHeaderItem(0,QtGui.QTableWidgetItem(hName))
      while(tmpi<3):
          if(self.vNotepad.InputVal[tmpi]!='0'):
              hName=self.vNotepad.InputUnit[tmpi]+', '+self.vNotepad.InputVal_ParName[tmpi]
              self.tableW.setColumnCount(tmpi*2+3)
              self.tableW.setHorizontalHeaderItem(tmpi*2+1,QtGui.QTableWidgetItem(hName))
              hName='Ед.изм.'
              self.tableW.setHorizontalHeaderItem(tmpi*2+2,QtGui.QTableWidgetItem(hName))
          tmpi=tmpi+1
          self.vNotepad.InputVal[0]=self.vNotepad.dSize['VPChNameList'][0]
      
  def StartTable(self):
      """  Запуск таймера обработки таблицы"""
      self.timer.start(1000)  

  def on_Timer_value_Changed(self):
      """ Событие таймера"""
      tmpi=self.spinBox.value()*1000
      self.timer.setInterval(tmpi)

  def on_btnSave(self):
      """ Нажатие кнопки сохранения таблицы """
      qq=QtGui.QFileDialog.getSaveFileName(self, "Save file", "Измерения", ".txt")
      file = open(qq, "w")
      row=0
      file.write("Отчет по измерениям")
      file.write("\n")
      a=datetime.today()
      a1=a.date()
      a2=a.time()
      dt1=str(a1)+"  \t"+a2.strftime("%H:%M:%S") 
      file.write(dt1)
      file.write("\n")
      cfg=self.vNotepad.vCE.CommonProfil_stateD['LastCfgName']
      file.write("Конфигурация"+"  \t"+cfg)
      file.write("\n")
      col=0

      while(col<=self.tableW.columnCount()-1):
           htxt=self.tableW.horizontalHeaderItem(col).text()
           file.write(htxt+"  \t")
           col=col+1
      file.write("\n")
      while(row<=self.tableW.rowCount()-1):
         col=0
         while(col<=self.tableW.columnCount()-1):
              file.write(self.tableW.item(row,col).text()+"  \t")
              col=col+1
         row=row+1
         file.write("\n")
      file.write("Конец измерений") 
      file.write("\n")
      file.close()
      cmd = 'C:/"Program Files (x86)"/"Microsoft Office"/Office12/excel.exe'
      qq1=cmd+' '+qq
      subprocess.Popen(qq1, shell = True)
      q=0

  def on_btnClear(self):
      """ кнопка стирания таблицы """
      self.tableW.clear()
      self.InitTable()
      #self.tableW.setRowCount(0)
      self.vNotepad.row_counter=0

  def show(self, newsize = None):
    """ newsize - экземпляр QSize для передачи новых размеров окна """
    super().show()   # важно выполнить ПЕРЕД resize - иначе resize может не пройти
    if newsize:  self.resize(newsize)

  def closeEvent(self, event):
    """ Событие закрытия формы """
    self.vNotepad.SaveState()
    rect = self.geometry()
    self.vNotepad.dSize['x'] = rect.left()
    self.vNotepad.dSize['y'] = rect.top()
    self.vNotepad.dSize['height'] = rect.height() 
    self.vNotepad.dSize['width'] = rect.width()
    event.accept() 

  def resizeEvent(self, event):
    """ событие изменения размера окна """
    super().resizeEvent(event)

  def on_Timer_toggle(self):
    """ событие основного таймера   """
    self.vNotepad.Proceed()
    if (self.vNotepad.vCE.Close_Config_Flag==1)and(self.vNotepad.closeFlag==0): 
          self.vNotepad.closeFlag=1      
          self.close()
          self.timer.stop()
          self.delete()
          a=0