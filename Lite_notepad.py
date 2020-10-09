
import logging
import os
import subprocess
from PyQt4 import QtCore, QtGui 
from datetime import datetime
from common import PCFlag
if PCFlag==1: from fmLiteNotepad import Ui_fmLiteNotepad
if PCFlag==2: from fmLiteNotepad_t import Ui_fmLiteNotepad
from vinstr import CVInstr
import Results
#LL = logging.getLogger('SVI')

class CLiteNotepad(CVInstr):
  """ виртуальный блокнот 
    Блокнот, сохраняющий текущее значение показаний прибора в таблице """

  def __init__(self,vCE,  dcfg, dstate = {}, dSize={}, fTech = False):
    """ Инициализация виртуального блокнота"""
    super().__init__(dcfg, dstate, fTech)
    self.vCE=vCE
    self.closeFlag=0  
    self.dSize=dSize
    self.Name=dcfg['наименование']
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
    self.widthD = 7
    self.precD = 3
    self.formS = "{:"+str(self.widthD)+"."+str(self.precD)+"f}" 
    self.row_counter=0
    self.widthD = 6 # 4
    self.precD = 3  # 3
    self.formS = "{:"+str(self.widthD)+"."+str(self.precD)+"f}"
    self.win = CfmLiteNotepad(self.widthD + 1, self)
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
    self.tmpVal4_Id=0
    self.tmpVal4=0
    self.tmpVal4_Ed=0
    self.tmpVal4_VP=''
    self.tmpVal4_VPProfil=''
    self.tmpVal5_Id=0
    self.tmpVal5=0
    self.tmpVal5_Ed=0
    self.tmpVal5_VP=''
    self.tmpVal5_VPProfil=''
    self.tmpVal6_Id=0
    self.tmpVal6=0
    self.tmpVal6_Ed=0
    self.tmpVal4_VP=''
    self.tmpVal4_VPProfil=''

  def LoadState(self):
    super().LoadState()
 
  def SaveState(self):
    super().SaveState()

  def NewData(self, ddata):
      q=0

  def Proceed(self):
    """ Обновление содержания блокнота по таймеру """

    #Запись даты и времени
    a=datetime.today()
    a1=a.date()
    a2=a.time()
    dt1=str(a1)+"  \t"+a2.strftime("%H:%M:%S")
    d1=0
    d3=0
    d3=0
    try:
       d1=Results.Result_Dict[self.InputUnit[0]]['В блокнот']

    except: d1=0

    try:
       d2=Results.Result_Dict[self.InputUnit[1]]['В блокнот']

    except: d2=0

    try:
       d3=Results.Result_Dict[self.InputUnit[2]]['В блокнот']

    except: d3=0

     
    #Создание новой строки в таблице
    if(d1==1)|(d2==1)|(d3==1):
        self.cnt1=self.win.tableW.rowCount()
        self.row_counter=self.cnt1
        self.win.tableW.insertRow(self.row_counter)
        self.win.tableW.setItem(self.row_counter,1,QtGui.QTableWidgetItem(dt1))
    
    #Проверка наличия данных на первом входе и сигнала на их запись
    if(d1==1):
        self.tmpVal4=Results.Result_Dict[self.InputUnit[0]][self.InputVal[0]]
        self.tmpVal4_VP=str(self.InputUnit[0])
        self.tmpVal4_VPProfil=Results.Result_Dict[self.InputUnit[0]]['LastProfil']
        self.tmpVal4_Ed=Results.Result_Dict[self.InputUnit[0]]['Единица '+self.InputVal[0]]
        self.tmpVal4_Id=Results.Result_Dict[self.InputUnit[0]]['ID_VP']
        self.win.tableW.setItem(self.row_counter,0,QtGui.QTableWidgetItem(str(self.tmpVal4_Id)))
        self.win.tableW.setItem(self.row_counter,2,QtGui.QTableWidgetItem(str(self.tmpVal4_VP)))
        self.win.tableW.setItem(self.row_counter,3,QtGui.QTableWidgetItem(str(self.tmpVal4_VPProfil)))
        self.win.tableW.setItem(self.row_counter,4,QtGui.QTableWidgetItem(self.formS.format(self.tmpVal4)))
        self.win.tableW.setItem(self.row_counter,5,QtGui.QTableWidgetItem(str(self.tmpVal4_Ed)))
        Results.Result_Dict[self.InputUnit[0]]['В блокнот']=2
        self.row_counter=self.row_counter+1 

    #Проверка наличия данных на втором входе и сигнала на их запись
    if(d2==1): 
        self.tmpVal5=Results.Result_Dict[self.InputUnit[1]][self.InputVal[1]]
        self.tmpVal5_VP=str(self.InputUnit[1])
        self.tmpVal5_VPProfil=Results.Result_Dict[self.InputUnit[1]]['LastProfil']
        self.tmpVal5_Ed=Results.Result_Dict[self.InputUnit[1]]['Единица '+self.InputVal[1]]
        self.tmpVal5_Id=Results.Result_Dict[self.InputUnit[1]]['ID_VP']
        self.win.tableW.setItem(self.row_counter,0,QtGui.QTableWidgetItem(str(self.tmpVal5_Id)))
        self.win.tableW.setItem(self.row_counter,2,QtGui.QTableWidgetItem(str(self.tmpVal5_VP)))
        self.win.tableW.setItem(self.row_counter,3,QtGui.QTableWidgetItem(str(self.tmpVal5_VPProfil)))
        self.win.tableW.setItem(self.row_counter,4,QtGui.QTableWidgetItem(self.formS.format(self.tmpVal5)))
        self.win.tableW.setItem(self.row_counter,5,QtGui.QTableWidgetItem(str(self.tmpVal5_Ed)))
        Results.Result_Dict[self.InputUnit[1]]['В блокнот']=2
        self.row_counter=self.row_counter+1 

    #Проверка наличия данных на третьем входе и сигнала на их запись
    if(d3==1): 
        self.tmpVal6=Results.Result_Dict[self.InputUnit[2]][self.InputVal[2]]
        self.tmpVal6_VP=str(self.InputUnit[2])
        self.tmpVal6_VPProfil=Results.Result_Dict[self.InputUnit[2]]['LastProfil']
        self.tmpVal6_Ed=Results.Result_Dict[self.InputUnit[2]]['Единица '+self.InputVal[2]]
        self.tmpVal6_Id=Results.Result_Dict[self.InputUnit[2]]['ID_VP']
        self.win.tableW.setItem(self.row_counter,0,QtGui.QTableWidgetItem(str(self.tmpVal6_Id)))
        self.win.tableW.setItem(self.row_counter,2,QtGui.QTableWidgetItem(str(self.tmpVal6_VP)))
        self.win.tableW.setItem(self.row_counter,3,QtGui.QTableWidgetItem(str(self.tmpVal6_VPProfil)))
        self.win.tableW.setItem(self.row_counter,4,QtGui.QTableWidgetItem(self.formS.format(self.tmpVal6)))
        self.win.tableW.setItem(self.row_counter,5,QtGui.QTableWidgetItem(str(self.tmpVal6_Ed)))
        Results.Result_Dict[self.InputUnit[2]]['В блокнот']=2
        self.row_counter=self.row_counter+1 

    d1=0
    d3=0
    d3=0
#---
class CfmLiteNotepad(QtGui.QMainWindow, Ui_fmLiteNotepad):
  """ лицевая панель виртуального"""
      
  def __init__(self, numDigits, vNotepad):
    """ Инициализация формы блокнота """
    super(CfmLiteNotepad, self).__init__() 
    self.setupUi(self)
    self.setStyleSheet("QMainWindow {background: '#FED0FC';}")
    self.vNotepad = vNotepad
    self.basePS = None
    self.Type=2
    self.Reset_Flag=1
    self.InLight_Notepad=0
    self.ID_VP='0'
    self.timer = QtCore.QTimer()
    self.timer.timeout.connect(self.on_Timer_toggle)    
    self.btnSave.clicked.connect(self.on_btnSave)
    self.btnClear.clicked.connect(self.on_btnClear)
    self.btnDel.clicked.connect(self.on_btnDel)
    self.trAutoScan =None
    self.trAutoScan = self.startTimer(1000) 


  def timerEvent(self, e):
  #Отображение даты по таймеру
        if (self.vNotepad.vCE.Close_Config_Flag==1)and(self.vNotepad.closeFlag==0): 
          self.vNotepad.closeFlag=1  
          self.timer.stop()    
          self.close()
          self.delete()
          a=1

  def InitTable(self):
      """ Иницализация таблицы на форме ВП """
      tmpi=0
      self.tableW.setColumnCount(6)
      if PCFlag==2:								   
        self.tableW.setColumnCount(6)
        self.tableW.setColumnWidth(0,190)
        self.tableW.setColumnWidth(1,190)
        self.tableW.setColumnWidth(2,190)
        self.tableW.setColumnWidth(3,190)
        self.tableW.setColumnWidth(4,190)
        self.tableW.setColumnWidth(5,190)
      
        hName='Идентификатор'+'     '
        self.tableW.setHorizontalHeaderItem(0,QtGui.QTableWidgetItem(hName))
        hName='Дата и время'+'     '
        self.tableW.setHorizontalHeaderItem(1,QtGui.QTableWidgetItem(hName))
        hName='Вирт. прибор'+'     '
        self.tableW.setHorizontalHeaderItem(2,QtGui.QTableWidgetItem(hName))
        hName='Профиль'+'     '
        self.tableW.setHorizontalHeaderItem(3,QtGui.QTableWidgetItem(hName))
        hName='Значение'+'     '
        self.tableW.setHorizontalHeaderItem(4,QtGui.QTableWidgetItem(hName))
        hName='Ед. измерения'+'     '
        self.tableW.setHorizontalHeaderItem(5,QtGui.QTableWidgetItem(hName))							   
      if PCFlag==1:
        hName='Идентификатор'
        self.tableW.setHorizontalHeaderItem(0,QtGui.QTableWidgetItem(hName))
        hName='Дата и время'
        self.tableW.setHorizontalHeaderItem(1,QtGui.QTableWidgetItem(hName))
        hName='Вирт. прибор'
        self.tableW.setHorizontalHeaderItem(2,QtGui.QTableWidgetItem(hName))
        hName='Профиль'
        self.tableW.setHorizontalHeaderItem(3,QtGui.QTableWidgetItem(hName))
        hName='Значение'
        self.tableW.setHorizontalHeaderItem(4,QtGui.QTableWidgetItem(hName))
        hName='Ед. измерения'
        self.tableW.setHorizontalHeaderItem(5,QtGui.QTableWidgetItem(hName))
      
  def StartTable(self):
      """ Запуск таймера блокнота """
      self.timer.start(1000)  
    
  def on_btnSave(self):
      """ Сохранение в файл содержимого блокнота """
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
      #Открытие файла в Excel
      cmd = 'C:/"Program Files (x86)"/"Microsoft Office"/Office12/excel.exe'
      qq1=cmd+' '+qq
      subprocess.Popen(qq1, shell = True)
      q=0

  def on_btnClear(self):
      """ Очистка таблицы блокнота """
      self.tableW.clear()
      self.tableW.setRowCount(0)
      self.vNotepad.row_counter=0
      self.InitTable()

  def on_btnDel(self):
      """ Удаление выделенной строки в фороме таблице блокнота """
      tmprow=self.tableW.currentRow()
      self.tableW.removeRow(tmprow)
      self.vNotepad.row_counter=self.vNotepad.row_counter-1

  def show(self, newsize = None):
    """ newsize - экземпляр QSize для передачи новых размеров окна """
    super().show()   # важно выполнить ПЕРЕД resize - иначе resize может не пройти
    if newsize:  self.resize(newsize)

  def closeEvent(self, event):
    """ Закрытие формы """
    self.vNotepad.SaveState()
    rect = self.geometry()
    self.vNotepad.dSize['x'] = rect.left()
    self.vNotepad.dSize['y'] = rect.top()
    self.vNotepad.dSize['height'] = rect.height() 
    self.vNotepad.dSize['width'] = rect.width()
    event.accept() 

  def resizeEvent(self, event):
    """ изменение размера формы """
    super().resizeEvent(event)

  def on_Timer_toggle(self):
    """ Событие по таймеру """
    self.vNotepad.Proceed()