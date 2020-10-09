# -*- coding: utf-8 -*-
#Система управления виртуальными приборами
#---
__author__  = "Aleksey Bocharov <trashmbox@yandex.ru>"
__status__  = "development"
__version__ = "0.5i"
__date__    = "19 Сентября 2013"
#---
import os, sys
import atexit
import pickle
from datetime import datetime
import re
import svimb
from collections import namedtuple
import log # дополнительные возможности логирования
import logging
from sstate import *
from struct import Struct
from PyQt4 import QtCore, QtGui 
from chart_II import*
from unit import*
from Inputunit_ import*
from cond import*
from o2mer import*
from ionomer import*
from pressure import*
from amper import*
from volt import*
import copy 
from temperature import*
from notepad import*
from Lite_notepad import*
from protokol import*
from Arrow_Pr import*					 
import Results
#from svi import*
import svi
from vinstr import*

#from diagramscene import*

from common import *
import AllResults
if PCFlag==1:
  from fmChangeVirtPriborsParam import Ui_fmChangeVirtPriborsParam
  from fmChangeVirtPribors import Ui_fmChangeVirtPribors
  from fmCreateConfig import Ui_fmCreateConfig
  from fmSelectConfig import Ui_fmSelectConfig
  from fmVPPassword import Ui_fmVPPassword
  from fmWelcome import Ui_fmWelcome
  from fmProgramming_1_1 import Ui_fmProgramming_1_1
  from fmAllSearch_1_0 import Ui_fmAllSearch_1_0
  from fmDigitalKeyboard import Ui_fmDigitalKeyboard
  from fmKeyboard import Ui_fmKeyboard
if PCFlag==2:
  from fmChangeVirtPriborsParam_t import Ui_fmChangeVirtPriborsParam
  from fmChangeVirtPribors_t import Ui_fmChangeVirtPribors
  from fmCreateConfig_t import Ui_fmCreateConfig
  from fmSelectConfig_t import Ui_fmSelectConfig
  from fmVPPassword_t import Ui_fmVPPassword
  from fmWelcome_t import Ui_fmWelcome
  from fmProgramming_1_1_t import Ui_fmProgramming_1_1
  from fmAllSearch_1_0_t import Ui_fmAllSearch_1_0
  from fmDigitalKeyboard_t import Ui_fmDigitalKeyboard
  from fmKeyboard_t import Ui_fmKeyboard

import vinstr
from filtr import filtrP
import Results
global winCrChVP
global winCrChVParam
global winVPPassword
global app
global Cfg
winCrChVP = None
winCrChVPParam = None
winVPPassword = None
LL = logging.getLogger('SVI')  # сконфигурирован основным модулем
# ---------------------------------------------- 
#        Дополнительные типы
# атрибуты регистров для консоли драйвера MODBUS
regsAttr = namedtuple('regsAttr', ['DevAddr', 'RegAddr']) # адрес измерителя, адрес регистра в адресном пространстве MODBUS
# ---------------------------------------------- 
cstateD = sstate.cstateD  # словарь сохраняемых состояний общего назначения (ключ - имя типа класса)
                          #   значение: словарь параметров (например СfmMain хранит там расположение окна) 

#---
def OnDataReady_1(dataLst):
  """ обработчик callback данных от измерительных каналов 
      (вызывается в контексте отдельного потока svimb) """
  #print(globals())
  print("----------------")
  print(svi.chanD)
  #print(dataLst)  
  for ch_data in dataLst:
    ch_id = ch_data[0]
    if ch_id in svi.chanD:
      for vi_key in svi.chanD[ch_id]["Link"]:
        if vi_key in svi.vinstrD:
          if "obj" in svi.vinstrD[vi_key]:  svi.vinstrD[vi_key]["obj"].NewData({svi.chanD[ch_id]["наименование"]: ch_data}) # TODO - сгруппировать данные (возможна "пробуксовка")
 
#---      

class CfmAllSearch_1_0(QtGui.QMainWindow, Ui_fmAllSearch_1_0):
  """ Класс формы поиска измерительных модулей"""
  def __init__(self,vCE): 
    """ Инициализация класса формы поиска измерительных модулей"""   
    global vinstrD
    global cstateD
    super(CfmAllSearch_1_0, self).__init__() 
    super().__init__()    
    self.setupUi(self)
    self.vCE=vCE
    self._Counter=0
    self.on_InitTable()
    self.InitForm()
    if 'fmAllSearch_1_0' in sstate.cstateD: 
      self.dictState = sstate.cstateD['fmAllSearch_1_0'] 
      self.width=self.dictState.setdefault('width',100)
      self.height=self.dictState.setdefault('height',100)
      self.x=self.dictState.setdefault('x',100)
      self.y=self.dictState.setdefault('y',100)

    self.tbSearchModuls.clicked.connect(self.on_tbSearchModuls_clicked)
    self.twSearch.clicked.connect(self.on_twSearch_clicked)
    self.twSearch.doubleClicked.connect(self.on_twSearch_doubleCicked)
    self.twSearch.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)    
    self.twSearch.customContextMenuRequested.connect(self.on_twSearch_menu)
    self.twSearch.itemChanged.connect(self.on_twSearch_changed)
    self.on_InitTable()

  def on_tbSearchModuls_clicked(self):
      """ Событие нажатия кнопки поиска измерительных модулей"""
      self.on_InitTable()
      self.vCE.AllSearch()
      q=0


  def on_twSearch_clicked(self):
      q=0

  def on_twSearch_doubleCicked(self):
      q=0
   
  def on_twSearch_menu(self):
      q=0

  def on_twSearch_changed(self):
      q=0

  def on_InitTable(self):
      """Инициализация таблицы найденных модулей """
      self.twSearch.clear()
      try:
       CntRow=self.vCE.LocalProfil_stateD['Counter']
      except: CntRow=0
      tmpRow={}
      self.twSearch.setRowCount(CntRow)
      self.twSearch.setColumnCount(6)
      Header=['Номер','Дата','Тип','Версия платы','Версия ПО','Комментарий']
      tmpi=0
      while(tmpi<6):
        a=str(Header[tmpi])
        item = QtGui.QTableWidgetItem(a)
        self.twSearch.setHorizontalHeaderItem(tmpi, item)
        item1 = self.twSearch.horizontalHeaderItem(tmpi)
        tmpi=tmpi+1      
      tmpj=0
      while(tmpj<CntRow):

       tmpRow[0]=self.vCE.LocalProfil_stateD['S_Number'][tmpj+1]
       tmpRow[1]=self.vCE.LocalProfil_stateD['Date'][tmpj+1]
       tmpRow[2]=self.vCE.LocalProfil_stateD['Type'][tmpj+1]
       tmpRow[3]=self.vCE.LocalProfil_stateD['HW_Version'][tmpj+1]
       tmpRow[4]=self.vCE.LocalProfil_stateD['Soft_Version'][tmpj+1]
       tmpRow[5]=self.vCE.LocalProfil_stateD['Comment'][tmpj+1]
    
       tmpi=0
       while(tmpi<6):   
        
        item = QtGui.QTableWidgetItem(str(tmpRow[tmpi]))
        self.twSearch.setItem(tmpj, tmpi, item)
        tmpi=tmpi+1

       tmpj=tmpj+1
      q=0
      self.twSearch.resizeColumnsToContents()

  def InitForm(self):
      q=0
 
class CfmProgramming_1_1(QtGui.QMainWindow, Ui_fmProgramming_1_1):
  """ Форма программирования модулей (технологическая)"""

  #  vbut - список с экземплярами CIButton (кнопки вывода лицывых панелей виртуальных приборов)
  #  dictState - словарь сохраняемых при выключении переменных\параметров
  #  fFirstShow - True - первое отображение окна ("костыль" для восстановления сохраненного расположения)
  #  fRec - флаг для блокировки рекурентного вызова closeEvent 

  def __init__(self,vCE):  
    """ Инициализация формы программирования модулей """
    global vinstrD
    global cstateD
    super(CfmProgramming_1_1, self).__init__() 
    super().__init__()    
    self.setupUi(self)
    self.vCE=vCE
    self._Counter=0
    self.on_InitTable()
    self.InitForm()
    if 'CfmProgramming_1_1' in sstate.cstateD: 
      self.dictState = sstate.cstateD['CfmProgramming_1_1'] 
      self.width=self.dictState.setdefault('width',100)
      self.height=self.dictState.setdefault('height',100)
      self.x=self.dictState.setdefault('x',100)
      self.y=self.dictState.setdefault('y',100)

    self.tbReadEeprom_.clicked.connect(self.on_tbReadEeprom_clicked)
    self.tbSaveDB_.clicked.connect(self.on_tbSaveDB_clicked)

    self.cbTypeAnalog_.currentIndexChanged.connect(self.on_cbTypeAnalog_changed)
    self.leDate_.editingFinished.connect(self.on_leDate_finished_toggle)
    self.leVersion_.editingFinished.connect(self.on_leVersion_finished)
    self.tbSaveEeprom_.clicked.connect(self.on_tbSaveEeprom_clicked)
    self.tbDelDBNum_.clicked.connect(self.on_tbDelDBNum_clicked)
    self.tbAddDBNum_.clicked.connect(self.on_tbAddDBNum_clicked)
    self.tbSaveDBNum_.clicked.connect(self.on_tbSaveDBNum_clicked)
    self.tbSearchModuls.clicked.connect(self.on_tbSearchModuls)
    self.twDBNum_.clicked.connect(self.on_twDBNum_clicked)
    self.twDBNum_.doubleClicked.connect(self.on_twDBNum_doubleCicked)
    self.twDBNum_.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)    
    self.twDBNum_.customContextMenuRequested.connect(self.on_twDBNum_menu)
    self.twDBNum_.itemChanged.connect(self.on_twDBNum_changed)

 
  def on_tbSearchModuls(self):
    """Поиск подключенных модулей  """
    self.vCE.winfmAllSearch_1_0.show()

  
  def on_cbSNum_changed(self):
      q=0

  def on_cbTypeAnalog_changed(self):
      q=0

  def on_leDate_finished_toggle(self):
      q=0

  def on_leVersion_finished(self):
      q=0

  def on_tbSaveDB_clicked(self):
      self.vCE.DBEditor.Save()
  
  def on_InitTable(self):
      """ Инициализация таблицы"""
      tmpi=0
      self.twDBNum_.clear()
      try:
       CntRow=self.vCE.LocalProfil_stateD['Counter']
      except: CntRow=0
      tmpRow={}
      self.twDBNum_.setRowCount(CntRow)
      self.twDBNum_.setColumnCount(6)
      Header=['Номер','Дата','Тип','Версия платы','Версия ПО','Комментарий']
      while(tmpi<6):
        a=str(Header[tmpi])
        item = QtGui.QTableWidgetItem(a)
        self.twDBNum_.setHorizontalHeaderItem(tmpi, item)
        item1 = self.twDBNum_.horizontalHeaderItem(tmpi)
        tmpi=tmpi+1
            
      tmpj=0
      while(tmpj<CntRow):
       tmpRow[0]=self.vCE.LocalProfil_stateD['S_Number'][tmpj+1]
       tmpRow[1]=self.vCE.LocalProfil_stateD['Date'][tmpj+1]
       tmpRow[2]=self.vCE.LocalProfil_stateD['Type'][tmpj+1]
       tmpRow[3]=self.vCE.LocalProfil_stateD['HW_Version'][tmpj+1]
       tmpRow[4]=self.vCE.LocalProfil_stateD['Soft_Version'][tmpj+1]
       tmpRow[5]=self.vCE.LocalProfil_stateD['Comment'][tmpj+1]    
       tmpi=0
       while(tmpi<6):   
        
        item = QtGui.QTableWidgetItem(str(tmpRow[tmpi]))
        #item.setText('qqq')
        self.twDBNum_.setItem(tmpj, tmpi, item)
        tmpi=tmpi+1

       tmpj=tmpj+1
      q=0
      self.twDBNum_.resizeColumnsToContents()
  
  def InitForm(self):
      """ Инициализация формы"""
      self.vCE.VPriborsTypesListCounter=self.vCE.CommonProfil_stateD['VPriborsTypesListCounter']
      tmpi=0
      a=datetime.today()
      a1=a.date()
      self.leDate_.setText(str(a1))
      self.cbTypeAnalog_.clear()

      while(tmpi<self.vCE.VPriborsTypesListCounter):
          self.cbTypeAnalog_.addItem(self.vCE.CommonProfil_stateD['VPriborsTypesList'][tmpi])
          tmpi=tmpi+1
    
  def on_tbSaveEeprom_clicked(self):
      """ Запись в EEPROM """
      try:
       self.vCE.Programmer.SaveEEPROM()
      except:
       q=1
      q=3

  def on_tbReadEeprom_clicked(self):
      q=3

 
  def on_tbDelDBNum_clicked(self):
      """ Удаление записи БД"""
      self.vCE.DBEditor.delete()
      self.on_InitTable()

   
  def on_tbAddDBNum_clicked(self):
      """ Добавление записи в БД """
      SN=self.cbSNum_.value()
      self.cbSNum_.setValue(SN+1)
      Date=self.leDate_.text()
      Type=self.cbTypeAnalog_.currentText()
      HWVersion=self.leVersionHW_.text()
      SVersion=self.leVersion_.text()
      Comment=self.leComment_.text()
      self.vCE.DBEditor.Add(SN, Date, Type, HWVersion, SVersion, Comment)
      self.on_InitTable()
    
  def on_tbSaveDBNum_clicked(self):
      """ Сохранение БД """
      SN=self.cbSNum_.value()
      Date=self.leDate_.text()
      Type=self.cbTypeAnalog_.currentText()
      HWVersion=self.leVersionHW_.text()
      SVersion=self.leVersion_.text()
      Comment=self.leComment_.text()
      self.vCE.DBEditor.edit(SN, Date, Type, HWVersion, SVersion, Comment)
      self.on_InitTable()
   
  def on_twDBNum_clicked(self):
      """ Выбор строки БД"""
      i=self.twDBNum_.currentRow()
      self.vCE.DBEditor.SetCurrIndex(i+1)
      self.cbSNum_.setValue(int( self.vCE.DBEditor.Curr_SN))
      self.leDate_.setText(self.vCE.DBEditor.Curr_Date)
      self.cbTypeAnalog_.setItemText(self.cbTypeAnalog_.currentIndex(), self.vCE.DBEditor.Curr_Type)
      self.leVersionHW_.setText(self.vCE.DBEditor.Curr_HWVersion)
      self.leVersion_.setText(self.vCE.DBEditor.Curr_SVersion)
      self.leVersion_.setText(self.vCE.DBEditor.Curr_Comment)

  def on_twDBNum_doubleCicked(self):
      """ Двойной клик по таблице ДБ """
      self.on_twDBNum_clicked()
      q=0

  def on_twDBNum_menu(self):
      q=0

  def on_twDBNum_changed(self):
      q=0
  
  def ClTbl_draw(self, pr):
    """ Отрисовка таблицы БД """
    tmpi=0
    self.twDBNum_.setRowCount(5)
    self.twDBNum_.setColCount(5)
    while(tmpi<4):
      item = QtGui.QTableWidgetItem('qq')
      self.twDBNum_.setHorizontalHeaderItem(tmpi, item)
      item1 = self.twDBNum_.horizontalHeaderItem(tmpi)
      tmpi=tmpi+1
    self._col = sorted(pr)
    _size =4 # len(self.pXcol)
    if _size:


      self.fFreeze = True # "заморозка" на время заполнения таблицы    
      # извлекаем данные из профиля в таблицу
      if self.twDBNum_.rowCount() != _size:  self.twDBNum_.setRowCount(_size) #установка числа строк
      for row in range(_size): #для каждой строки
        if not self.twDBNum_.verticalHeaderItem(row):
          head = QtGui.QTableWidgetItem("")
          self.twDBNum_.setVerticalHeaderItem(row, head)
        else: 
          head = self.twDBNum_.verticalHeaderItem(row) 
        head.setText(str(row + 1))
 
        self.hint=10
        head.setData(self.hint, row) # хинт для связи с pXcol -> pXdict, независимый от вставки новых незаполненных строк
        
        if not self.twDBNum_.item(row, 0):
             self.twDBNum_.setItem(row, 0, QtGui.QTableWidgetItem(""))
        self.twDBNum_.item(row, 0).setText('qwe')#pr['col1'][row][1])  # pX


        if not self.twDBNum_.item(row, 1):  self.twDBNum_.setItem(row, 1, QtGui.QTableWidgetItem(""))
        self.twDBNum_.setItem(row, 2, QtGui.QTableWidgetItem("")) # Отклонение
      self.fFreeze = False 
    self.twDBNum_.resizeColumnsToContents()



class CfmWelcome(QtGui.QMainWindow, Ui_fmWelcome):
  """ Начальное окно программы """

  def __init__(self,vCE):
    """ Инициализация основного окна """
    global vinstrD
    global cstateD

    super().__init__()      
    self.setupUi(self)
    self.vCE=vCE
 
    self.fRec = False
    self.fFirstShow = True
    loadCstate()
    self.timer = QtCore.QTimer()
    self.timer.timeout.connect(self.on_tbSelectConfigWindow_toggle)
    self.timer.start(3000)
    #self.tbSelectConfigWindow.clicked.connect(self.on_tbSelectConfigWindow_toggle)

    
    #self.tbSetting.clicked.connect(self.on_tbSetting_toggle)
    #self.tbLoadLastConfig.clicked.connect(self.on_tbLoadLastConfig_toggle)
    #self.tbSettings.clicked.connect(self.on_tbSettings_toggle)
    #self.tbCloseConfig.clicked.connect(self.on_tbCloseConfig_toggle)

    



  
  def show(self):
    """ Показ основного окна """
    super().show()
    q=0      

  def on_tbSelectConfigWindow_toggle(self):
     """ Кнопка выбора окна выбора  конфигурации """
     try:
       self.vCE.winSelectConfig.show()
       self.close()
     except:

      print(sys.exc_info())   # TODO логирование    

  def on_tbLoadLastConfig_toggle(self):
     """ Кнопка загрузки последней конфигурации """
     self.vCE.LoadLastConfigList()
     self.vCE.ConvertCFG_1()
     self.vCE.StartCFG()

  def on_tbCloseConfig_toggle(self):
     '''Закрытие окон текущей конфигурации'''
     a=1
  

  def on_tbSetting_toggle(self):
     """ Кнопка технологическрго режима """
     try:
        self.ModeFlag= self.Cfg1["Калибровка мВ"]["ZeroA32"]																
        self.vCE.TechStart1(self.vCE.Cfg1)
     except:
      print(sys.exc_info())   # TODO логирование   DeleteConfig

  def on_tbSettings_toggle(self):
     """ Кнопка выбора баз данных модулей """
     try:
        q=1
        self.vCE.winfmProgramming_1_0.show()
     except:
      print(sys.exc_info())   # TODO логирование   DeleteConfig




class CfmSelectConfig(QtGui.QMainWindow, Ui_fmSelectConfig):
  """ Окно выбора текущей конфигурации"""

  def __init__(self,vCE):
    """ Инициализация окна выбора текущей конфигурации """
    global vinstrD
    global cstateD

    super().__init__()      
    self.setupUi(self)
    self.vCE=vCE
 
    self.fRec = False
    self.fFirstShow = True

    if 'CfmMain' in cstateD: 
      self.dictState = cstateD['CfmMain'] 
    else:
      self.dictState = {}
      cstateD['CfmMain'] = self.dictState 

    self.tbSelectConf.clicked.connect(self.on_tbSelectConf_toggle)
    self.tbChangeConf.clicked.connect(self.on_tbChangeConf_toggle)
    self.tbDelConf.clicked.connect(self.on_tbDelConf_toggle)
    self.tbUpConf.clicked.connect(self.on_tbUpConf_toggle)
    self.tbDnConf.clicked.connect(self.on_tbDnConf_toggle)
    self.tbTestModuls.clicked.connect(self.vCE.TestConfigsModuls)
    self.tbCreateConf.clicked.connect(self.on_tbCreateConf_toggle)
    self.lwConf.doubleClicked.connect(self.on_tbSelectConf_toggle)
    #self.lwConf.clicked.connect(self.on_PreSelectConf_toggle)
    self.tbSetting.clicked.connect(self.on_tbSetting_toggle)
    self.tbLoadLastConfig.clicked.connect(self.on_tbLoadLastConfig_toggle)
    self.tbSettings.clicked.connect(self.on_tbSettings_toggle)
    self.tbCloseConfig.clicked.connect(self.on_tbCloseConfig_toggle)
    #self.tbSetting.setVisible(False);
    #self.tbSettings.setVisible(False);
    #self.tbSetting.setEnabled(False);
    #self.tbSettings.setEnabled(False);
    
  def show(self):
    """ Отображение окна выбора текущей конфигурации """
    super().show()
    if self.fFirstShow: 
      self.fFirstShow = False
  
      desktop = QtGui.QApplication.desktop() 
      dh = desktop.height()
      dw = desktop.width()  
      rect = self.geometry()
      x = safeDget(self.dictState, "win.left", dw - rect.width())
      if (x > dw):  x = dw - rect.width()

      y = safeDget(self.dictState, "win.top", dh - rect.height())
      if (y > dh):  y = dh - rect.height()
      self.vCE.InitConfigList()
      a=0
      self.vCE.ModeFlag= self.vCE.Cfg1["Params"]["First"] 
      if(self.vCE.ModeFlag!='1917'):
        self.tbSetting.setVisible(False)
        self.tbSettings.setVisible(False)
        self.tbSetting.setEnabled(False)
        self.tbSettings.setEnabled(False)
      if(self.vCE.ModeFlag=='1917'):
        self.tbSetting.setVisible(True)
        self.tbSettings.setVisible(True)
        self.tbSetting.setEnabled(True)
        self.tbSettings.setEnabled(True)
      

  def on_tbSelectConf_toggle(self):
     """ Кнопка загрузки выбранной конфигурации """
     try:
       self.vCE.Close_Config_Flag=0
       a=self.lwConf.currentRow()
       self.vCE.LoadCurrConfigList(a)
       self.vCE.ConvertCFG_1()
       self.vCE.StartCFG()
       self.vCE.InitConfigList()
       self.lwConf.setEnabled(False)
       self.tbSelectConf.setEnabled(False)
       self.tbLoadLastConfig.setEnabled(False)
     except:
      print(sys.exc_info())   # TODO логирование  
      
  def on_PreSelectConf_toggle(self):
     """ Кнопка загрузки выбранной конфигурации """
     try:
       '''self.vCE.Close_Config_Flag=0
       a=self.lwConf.currentRow()
       self.vCE.LoadCurrConfigList(a)
       self.vCE.ConvertCFG_1()
       self.vCE.StartCFG()
       self.vCE.InitConfigList()
       self.lwConf.setEnabled(False)
       self.tbSelectConf.setEnabled(False)
       self.tbLoadLastConfig.setEnabled(False)'''

       tmps=self.vCE.GetConfigDescr(' ')
       self.winSelectConfig.tbDescribe.setText(tmps)
     except:
      print(sys.exc_info())   # TODO логирование   

  def on_tbChangeConf_toggle(self):
     """ Кнопка перехода к окну редактирования выбранной конфигурации """
     try:
       a=self.lwConf.currentRow()
       self.vCE.LoadCurrConfigList(a)
       self.vCE.winCrConf.show()
     except:
      print(sys.exc_info())   # TODO логирование   DeleteConfig

  def on_tbDelConf_toggle(self):
     """ Удаление выбранной конфигурации """
     try:
       CN=self.lwConf.currentRow()
       self.vCE.DeleteConfig(CN)
     except:
      print(sys.exc_info())   # TODO логирование   DeleteConfig

  def on_tbDnConf_toggle(self):
      """ Подъем выбранной конфигурации вверх по списку """
      CN=self.lwConf.currentRow()
      if (CN>0):
          self.vCE.UpConfigInList(CN)
          self.vCE.InitConfigList()
          self.lwConf.setCurrentRow(CN-1)

  def on_tbUpConf_toggle(self):
      """ Опускание выбранной конфигурации вниз по списку """
      CN=self.lwConf.currentRow()
      if (CN>=0):
          if (self.vCE.CommonProfil_stateD['Configs']>1):
            self.vCE.DownConfigInList(CN)
            self.vCE.InitConfigList()
            self.lwConf.setCurrentRow(CN+1)

  def on_tbCreateConf_toggle(self):
       """ Кнопка открытия окна редактирования конфигураций для создания новой конфигурации """
       a=-1
       self.vCE.Close_Config_Flag=0
       self.vCE.LoadCurrConfigList(a)
       self.vCE.winCrConf.show()
  def on_tbLoadLastConfig_toggle(self):
     """ Кнопка загрузки последней конфигурации """
     self.vCE.Close_Config_Flag=0
     self.vCE.LoadLastConfigList()
     self.vCE.ConvertCFG_1()
     self.vCE.StartCFG()
     self.lwConf.setEnabled(False)
     self.tbSelectConf.setEnabled(False)
     self.tbLoadLastConfig.setEnabled(False)

  def on_tbCloseConfig_toggle(self):
     '''Закрытие окон текущей конфигурации'''
     self.vCE.Close_Config_Flag=1
     self.lwConf.setEnabled(True)
     self.tbSelectConf.setEnabled(True)
     self.tbLoadLastConfig.setEnabled(True)
     #self.vinstrD1={}
     #self.DirID = svimb.CreateRTUdir(int(dirC["порт"]), 38400, 0, 100, 100)
     #self.PortOpened=1
     #LL.I("Направление MODBUS RTU COM{} [DirID={}] запущено успешно".format(dirC["порт"], DirID)) 
     #self.vCE.chanD1={}
     #self.vCE.vi={}
     #self.vinstrD1={}
     self.vCE.vinstrD1.clear()
     #Results.InitRes()

     a=1
  

  def on_tbSetting_toggle(self):
     """ Кнопка технологическрго режима """
     try:
        self.vCE.TechStart1(self.vCE.Cfg1)
     except:
      print(sys.exc_info())   # TODO логирование   DeleteConfig

  def on_tbSettings_toggle(self):
     """ Кнопка выбора баз данных модулей """
     try:
        q=1
        self.vCE.winfmProgramming_1_0.show()
     except:
      print(sys.exc_info())   # TODO логирование   DeleteConfig

  def closeEvent(self, event):
    """ Закрытие формы выбора конфигураций """
    """ событие закрытия формы """
    try:
      self.vCE.SaveConfig(self.vCE.LastConfigName) 
    except:
        q=0
    try:
      self.vCE.save_LocalProfil_state()
    except:
        q=0
    if self.fRec:
      # рекурентный вызов от closeAllWindows
      event.accept() 
    else:
      self.fRec = True
      rect = self.geometry()
      self.dictState["win.left"] = rect.left()
      self.dictState["win.top"] = rect.top()
      #app.closeAllWindows()
      event.accept()

  def closeEvent_1(self, event):
    """ событие закрытия формы """
    try:
      self.vCE.SaveConfig(self.vCE.LastConfigName) 
    except:
        q=0
    try:
      self.vCE.save_LocalProfil_state()
    except:
        q=0
    if self.fRec:
      sstate.saveCstate()
      # рекурентный вызов от closeAllWindows
      event.accept() 
    else:
      self.fRec = True
      rect = self.geometry()
      '''
      self.dictState["x"] = rect.x()
      self.dictState["y"] = rect.y()
      self.dictState["height"] = rect.height()
      self.dictState["width"] = rect.width()
      sstate.cstateD['CfmWelcome'] = self.dictState''' 
      sstate.saveCstate()
      event.accept()
 
class CfmCreateConfig(QtGui.QMainWindow, Ui_fmCreateConfig):
  """ Окно создания и редактирования конфигураций """

  def __init__(self,vCE):
    global vinstrD
    global cstateD

    global winCrChVP
    global winCrChVParam
    global winVPPassword

    super().__init__()      
    self.setupUi(self)
    self.ConfName =''
    self.vCE=vCE 
    self.fRec = False
    self.fFirstShow = True
    if 'CfmCreateConfig' in cstateD: 
      self.dictState = cstateD['CfmCreateConfig'] 
    else:
      self.dictState = {}
      cstateD['CfmCreateConfig'] = self.dictState       
    self.tbTest_.clicked.connect(self.on_tbTest_clicked)
    self.tbTest_.setVisible(False)
    self.tbChangeVPList.clicked.connect(self.on_tbChangeVPList_toggle)
    self.tbAddToConfig.clicked.connect(self.on_tbAddToConfig_toggle)
    self.tbDelFromConfig.clicked.connect(self.on_tbDelFromConfig_toggle)
    self.tbChangeInConfig.clicked.connect(self.on_tbChangeInConfig_toggle)
    self.tbChangeInConfig_Off.clicked.connect(self.on_tbChangeInConfig_Off_toggle)
    self.tbSaveConfig.clicked.connect(self.on_tbSaveConfig_toggle)
    self.tbChangeVPNameInConfig.clicked.connect(self.on_tbChangeVPNameInConfig_toggle)
    self.leConfName.editingFinished.connect(self.on_leConfNameFinished)
    self.leVPName.editingFinished.connect(self.on_leVPNameFinished)
    self.cb_In_2.currentIndexChanged.connect(self.cb_In_2_Change)
    self.lwVP.currentItemChanged.connect(self.lwVP_Change)
    self.lwConf.currentItemChanged.connect(self.lwConf_Change)
    self.lwConfVPIn.currentItemChanged.connect(self.lwConfVPIn_Change)
    self.lwVP.doubleClicked.connect(self.on_tbAddToConfig_toggle)
    self.lwConf.doubleClicked.connect(self.on_tbDelFromConfig_toggle)
    self.lwConfVPIn.doubleClicked.connect(self.on_lwConfVPIn_doubleClicked_toggle)
    self.tbConfDescr.clicked.connect(self.on_tbConfDescr_toggle)
    self.tbSaveConfig.setText("Сохранить")

  def on_tbTest_clicked(self):
    """Запуск разрабатываемой версии модульного отображения """
    self.vCE.Test()
          
  def show(self):
    """ Отображение формы создания конфигурации """
    super().show()
    if self.fFirstShow: 
      self.fFirstShow = False

      desktop = QtGui.QApplication.desktop() 
      dh = desktop.height()
      dw = desktop.width()  
      rect = self.geometry()

      x = safeDget(self.dictState, "win.left", dw - rect.width())
      if (x > dw):  x = dw - rect.width()

      y = safeDget(self.dictState, "win.top", dh - rect.height())
      if (y > dh):  y = dh - rect.height()

      #self.setGeometry(QtCore.QRect(QtCore.QPoint(x, y), self.size()))
      self.vCE.InitCurrConfigList()
      self.vCE.InitVirtPriborList()
      self.vCE.InitChList()
      self.vCE.InitTypeMess()

  def on_lwConfVPIn_doubleClicked_toggle(self):
      """ отсоединение входа виртуального прибора """
      self.vCE.Reset_ConfVPIn()
 
  def on_tbChangeVPList_toggle(self):
      """ Кнопка перехода к окну ввода пароля на редактирование виртуальных приборов """

      self.vCE.winVPPassword.show()
      a=1
 
  def on_tbAddToConfig_toggle(self):
       """ Кнопка добавления прибора в конфигурацию """
       self.vCE.AddVirtPriborToConfig()

  def on_tbConfDescr_toggle(self):
       """ Кнопка добавления прибора в конфигурацию """
       self.vCE.AddDescrToConfig(self.leConfDescr.text())
 
  def on_tbDelFromConfig_toggle(self):
      """ Кнопка удаления выбранного прибора из текущенй конфигурации """
      CN=self.lwConf.currentRow()
      self.vCE.DeleteVirtPriborFromConfig(CN)
      self.vCE.InitCurrConfigList()
 
  def on_tbChangeInConfig_toggle(self):
      """ Кнопка подсоединения входа виртуального прибора к выбранному выходу другого выбранного ВП """
      self.vCE.ChangeVirtPriborInConfig()
      self.vCE.InitConfigList()

  def on_tbChangeInConfig_Off_toggle(self):
      """ Кнопка отсоединения входа виртуального прибора от предыдущего """
      self.vCE.ChangeVirtPriborInConfigOff()
      self.vCE.InitConfigList()

  def on_tbChangeVPNameInConfig_toggle(self):
      """ Кнопка сохранения изменения названия ВП в редактируемой конфигурации """
      self.vCE.ChangeVirtPriborNameInConfig()
      self.vCE.InitConfigList()
 
  def on_tbSaveConfig_toggle(self):
      """ Кнопка сохранения конфигурации """
      self.vCE.SaveConfig(self.leConfName.text())
      self.vCE.InitConfigList()

 
  def on_leConfNameFinished(self):
    """ Окончание редактирования названия конфигурации ВП """
    try:
      q=1
    except:
      LL.exception('') 
      self.leConfName.setText(str(self.ConfName))
      self.leConfName.clearFocus() 

  def on_leVPNameFinished(self):
      a=1

  
  def cb_In_1_Change(self):
      a=1
  
  def cb_In_2_Change(self):
      """ Изменение в списке подключаемых модулей """
      CN=self.cb_In_2.currentIndex()
      if(CN>=0):
         self.vCE.CurrVPAddToConfigName=self.vCE.CommonProfil_stateD['CurrCFG']['CurrCFGVPList'][CN]
         self.vCE.InitVPChListInConfig()
  
  def lwVP_Change(self):
      """ Выбор виртуального прибора в списке приборов """
      self.vCE.InitVPChInOutList()
  
  def lwConf_Change(self):
      """ Выбор виртуального прибора в списке конфигурации """
      tmpa=self.lwConf.currentRow()
      if(tmpa>=0):
        self.vCE.CurrVPCurrCfgIndex=tmpa
        self.vCE.CurrVPCurrCfgName=self.vCE.CommonProfil_stateD['CurrCFG']['CurrCFGVPList'][self.vCE.CurrVPCurrCfgIndex]
        self.leVPName.setText(self.vCE.CurrVPCurrCfgName)
        self.leVPName.clearFocus()
        tmp=self.vCE.CommonProfil_stateD['CurrCFG'][self.vCE.CurrVPCurrCfgName]['VPParam']
        if (tmp=='1'):
            self.tbChangeInConfig.setEnabled(True)
            self.cb_In_2.setEnabled(True)
            self.cb_Ch_2.setEnabled(True)
        if (tmp=='0'):
            self.tbChangeInConfig.setEnabled(False)
            self.cb_In_2.setEnabled(False)
            self.cb_Ch_2.setEnabled(False)

        self.vCE.ConfVPInList()
        self.vCE.ConfVPOutList()
  
  def lwConfVPIn_Change(self):
      a=1
  
  def closeEvent(self, event):
      """ Событие закрытия окна редактирования конфигураций """         
      self.vCE.InitConfigList()


 
class CfmChangeVirtPribors(QtGui.QMainWindow, Ui_fmChangeVirtPribors):
  """Окно редактирования виртуальных приборов """

  def __init__(self,vCE):
    """ Инициализация окна редактирования виртуальных приборов """
    super(CfmChangeVirtPribors, self).__init__()      
    self.setupUi(self)
    self.vCE=vCE
    self.lePortNum.editingFinished.connect(self.on_lePortNumFinished)
    self.leIndexVPribor.editingFinished.connect(self.on_leIndexVPriborFinished)
    self.lwCh.currentItemChanged.connect(self.lwCh_Change)
    self.lwVIns.currentItemChanged.connect(self.lwVIns_Change)
    self.lwChInMess.currentItemChanged.connect(self.lwChInMess_Change)
    self.lwChInVP.currentItemChanged.connect(self.lwChInVP_Change)
    self.cbChInVPType.currentIndexChanged.connect(self.cbChInVPType_Change)
    self.cbChInVPModul.currentIndexChanged.connect(self.cbChInVPModul_Change)#####
    self.leParamVPribor.editingFinished.connect(self.on_leVPParamFinished)
    self.tbAddChInVP.clicked.connect(self.AddChInVP)
    self.tbChangeChInVP.clicked.connect(self.ChangeChInVP)
    self.tbDelChInVP.clicked.connect(self.DelChInVP)
    self.tbAddChOutVP.clicked.connect(self.AddChOutVP)
    self.tbChangeChOutVP.clicked.connect(self.ChangeChOutVP)
    self.tbDelChOutVP.clicked.connect(self.DelChOutVP)
    self.tbAutoSearch.clicked.connect(self.AutoSearch)
    self.tbChangeCh.clicked.connect(self.ChangeCh)
    self.tbSavePortNum.clicked.connect(self.SavePortNum)
    self.tbAddVPribor.clicked.connect(self.AddVPribor)
    self.tbDelVPribor.clicked.connect(self.DelVPribor)
    self.tbChangeVPribor.clicked.connect(self.ChangeVPribor)
    self.tbParam.clicked.connect(self.Param)
    self.lwChInVP.doubleClicked.connect(self.lwChInVP_doubleClicked)

    self.tbAddAutoSearch.clicked.connect(self.AddAutoSearch)
    self.tbDelCh_2.clicked.connect(self.DelCh)
    self.tbParam.setEnabled(False);
    #self.tbParam.setVisible(False);

  def closeEvent(self, event):
      #self.vCE.winCrConf.close()
      a=21
 
  def cbTypeMess_2_Change(self):
    """ Выбор типа каналов ВП """
    curIndex=self.cbTypeMess_2.currentIndex()
    if curIndex==0:
        self.lblch_1.setText('Канал ток')
        self.lblch_2.setVisible(0)
        self.cbCh_2.setVisible(0)
    if curIndex==1:
        self.lblch_1.setText('Канал  напряжение')
        self.lblch_2.setVisible(0)
        self.cbCh_2.setVisible(0)
    if curIndex==2:
        self.lblch_1.setText('Канал температура')
        self.lblch_2.setVisible(0)
        self.cbCh_2.setVisible(0)
    if curIndex==3:
        self.lblch_1.setText('Канал напряжение')
        self.lblch_2.setText('Канал температура')
        self.lblch_2.setVisible(1)
        self.cbCh_2.setVisible(1)
    if curIndex==4:
        self.lblch_1.setText('Канал ток')
        self.lblch_2.setText('Канал температура')
        self.lblch_2.setVisible(1)
        self.cbCh_2.setVisible(1)
 
  def AddChannel(self):
    """ Добавить измерительный канал в ВП """
    self.curAdrCh=self.leModbusNum.text()
    self.curIndCh=self.leIndexMess.text()
    self.curTypeCh=self.cbTypeMess.currentText()
    self.lwVIns_3.addItem('[адрес='+self.curAdrCh+'] Измеритель '+self.curTypeCh+self.curIndCh+' 0x204')

    global cfg_stateD
    self.addPar={}
    self.addPar1=[]
    self.addPar2=[]
    self.tmp={}
    self.tmp1={}
    self.addPar['адрес']=self.curAdrCh
    self.addPar2.append(self.curTypeCh+self.curIndCh)
    self.addPar2.append('0x204')
    self.addPar1.append(self.addPar2)
    self.addPar['канал']=self.addPar1

    self.tmp=sstate.cfg_stateD['MODBUS RTU'][0]['Измеритель'][0]
    sstate.cfg_stateD['MODBUS RTU'][0]['Измеритель'].append(self.addPar)
    self.cbCh_1.AddItem('[адрес='+self.curAdrCh+'] Измеритель '+self.curTypeCh+self.curIndCh+' 0x204');
    self.cbCh_2.AddItem('[адрес='+self.curAdrCh+'] Измеритель '+self.curTypeCh+self.curIndCh+' 0x204');
    a=1

  def showEvent(self,e):
      """ Событие отображения основной формы """ 
      global cfg_stateD
      #self.cbCh_1.clear();
      #self.cbCh_2.clear();
      self.vCE.InitPortNum()
      self.vCE.winCrConf.close()
      self.vCE.winVPPassword.close()


  def SaveSettings(self):
      """ Сохранение настроек """
      global Cfg 
      global cfg_stateD
      sstate.cfg_stateD['MODBUS RTU'][0]['порт']=self.lePortNum.text();
      sstate.save_Cfg_state()



  def on_leModbusNumFinished(self):
      a=1

  def on_leVPParamFinished(self):
      a=1

  def on_leIndexMessFinished(self):
      a=1

  def on_leTypeChFinished(self):
      a=1

  def on_leAddrChFinished(self):
      a=1

  def on_lePortNumFinished(self):
      a=1

  def on_leIndexVPriborFinished(self):
      a=1

  def on_leTypeVPriborFinished(self):
      a=1

  def lwChInVP_doubleClicked(self):
      """ Сброс канала в ВП """
      self.vCE.Reset_ChInVP()

  def AddAutoSearch(self):
      """ Автопоиск подключенных модулей """
      self.vCE.AddAutoSearch()

  def cbTypeMess_Change(self):
      a=1

  def lwCh_Change(self):
    """ Выделение строки в списке измерительных модулей """
    tmpchangech=self.lwCh.currentRow()
    if(tmpchangech>=0):
     tmpName=self.vCE.CommonProfil_stateD['MessChanels']['ChMessList'][tmpchangech]
     self.vCE.CurrChName=tmpName
     self.vCE.CurrChIndex=tmpchangech
     self.leIndexMess.setText(tmpName)
     self.leIndexMess.clearFocus()
     self.vCE.InitChListCh()

  def lwVIns_Change(self):
    """ Выделение строки в списке виртуальных приборов """
    tmpchangeVP=self.lwVIns.currentRow()
    if(tmpchangeVP>=0):
     tmpVPName=self.vCE.CommonProfil_stateD['VirtPribors']['VirtPriborList'][tmpchangeVP]
     self.vCE.CurrVPName=tmpVPName
     self.vCE.CurrVPIndex=tmpchangeVP
     self.leIndexVPribor.setText(tmpVPName)
     self.leIndexVPribor.clearFocus()
     try:
       self.vCE.CurrVPParam=self.vCE.CommonProfil_stateD['VirtPribors'][tmpVPName]['VPParam']
     except: self.vCE.CurrVPParam=0
     self.leParamVPribor.setText(str(self.vCE.CurrVPParam))
     self.leParamVPribor.clearFocus()
     self.vCE.CurrVPType=self.vCE.CommonProfil_stateD['VirtPribors'][tmpVPName]['VPType']
     i=0
     while(i<self.vCE.CommonProfil_stateD['VPriborsTypesListCounter']):
      tmpVPType=self.vCE.CommonProfil_stateD['VPriborsTypesList'][i]
      if(tmpVPType==self.vCE.CurrVPType): self.cbTypeVPribor.setCurrentIndex(i)
      i=i+1
     self.vCE.InitVPChList()
     self.vCE.InitVPChOutList()

  def cbChType_Change(self):
      a=1

  def cbChAddr_Change(self):
      a=1

  def cbTypeVPribor_Change(self):
      """ Изменение типа виртуального прибора """
      if(self.cbTypeVPribor.currentIndex()>-1):
       self.leTypeVPribor.setText(self.vCE.CommonProfil_stateD['VPriborsTypesList'][self.cbTypeVPribor.currentIndex()])
       self.leTypeVPribor.clearFocus()

  def cbChVPribor_1_Change(self):
      a=1

  def cbChVPribor_2_Change(self):
      a=1

  def AddCh(self):
      """ Добавить канал виртуального прибора """
      self.vCE.AddCh()

  def DelCh(self):
      """ Удалить канал виртуального прибора """
      self.vCE.DelCh()

  def ChangeCh(self):
      """ Изменить канал виртуального прибора """
      self.vCE.ChangeCh()

  def AddChName(self):
      """ Добавить название канала виртуального прибора """
      self.vCE.AddChName()

  def DelChName(self):
      """ Удалить название канала виртуального прибора """
      self.vCE.DelChName()

  def AddChAddr(self):
      """ Добавить адрес канала виртуального прибора """
      self.vCE.AddChAddr()

  def DelChAddr(self):
      """ Удалить адрес канала виртуального прибора """
      self.vCE.DelChAddr()

  def SavePortNum(self):
      """ Сохранить номер последовательного порта """
      self.vCE.SavePortNum()

  def AddVPribor(self):
      """ Добавить  виртуальный прибор """
      self.vCE.AddVPribor()

  def DelVPribor(self):
      """ Удалить  виртуальный прибор """
      self.vCE.DelVPribor()

  def ChangeVPribor(self):
      """  Изменить виртуальный прибор """
      self.vCE.ChangeVPribor()

  def AddVPType(self):
      """  Добавить тип виртуального прибора """
      self.vCE.AddVPType()

  def DelVPType(self):
      """  Удалить тип виртуального прибора """
      self.vCE.DelVPType()

  def ChangeChName(self):
      """  Изменить имя виртуального прибора """
      self.vCE.ChangeChName()

  def ChangeChAddr(self):
      """  Изменить адрес виртуального прибора """
      self.vCE.ChangeChAddr()

  def AutoSearch(self):
      """  Автопоиск измерительных модулей """
      self.vCE.TestConfigsModuls()


  def ChangeVPType(self):
      """  Изменить тип виртуального прибора """
      self.vCE.ChangeVPType()

  def lwChInMess_Change(self):
      a=1

  def lwChInVP_Change(self):
      a=1

  def cbChInVPType_Change(self):
      a=1

  def cbChInVPModul_Change(self):
      """ Каналы в модуле ВП """
      CN=self.cbChInVPModul.currentIndex()
      if (CN>-1):
          self.vCE.CurCreatingVPMessChannelName=self.vCE.CommonProfil_stateD['MessChanels']['ChMessList'][CN]
          self.vCE.InitChInVPChannelMess()

  def AddChInMess(self):
      """ Добавить канал в измеритель """
      self.vCE.AddChInMess()

  def ChangeChInMess(self):
      """ Изменить канал в измерителе """
      self.vCE.ChangeChInMess()

  def DelChInMess(self):
      """ Удалить канал из измерителя """
      self.vCE.DelChInMess()

  def AddChInVP(self):
      """ Добавляет канал в ВП """
      self.vCE.AddChInVP()

  def ChangeChInVP(self):
      """ Изменяет канал в ВП """
      self.vCE.ChangeChInVP()

  def DelChInVP(self):
      """ Удаляет канал в ВП """
      self.vCE.DelChInVP()

  def AddChOutVP(self):      
      """ Добавляет выходной канал в ВП """
      self.vCE.AddChOutVP()

  def ChangeChOutVP(self):      
      """ изменяет выходной канал в ВП """
      self.vCE.ChangeChOutVP()

  def DelChOutVP(self):      
      """ Удаляет выходной канал в ВП """
      self.vCE.DelChOutVP()

  def on_leTypeVPChFinished(self):
      q=1

  def AddTypeVPCh(self):      
      """ Добавляет тип канала в ВП """
      self.vCE.AddTypeVPCh()

  def DelTypeVPCh(self):      
      """ Удаляет тип канала в ВП """
      self.vCE.DelTypeVPCh()

  def ChangeTypeVPCh(self):      
      """ Изменяет тип канала в ВП """
      self.vCE.ChangeTypeVPCh()

  def Param(self):      
      """ Вызывает служебное окно конфигурирования параметров каналов ВП """
      self.vCE.winCrChVPParam.show()
     

class CfmVPPassword(QtGui.QMainWindow, Ui_fmVPPassword):
  """Форма ввода пароля"""

  def __init__(self,vCE):
    """ Инициализация формы ввода пароля"""
    global vinstrD
    global cstateD

    super().__init__()      
    self.setupUi(self)


    self.vCE=vCE
    self.fRec = False
    self.fFirstShow = True

    if 'CfmVPPassword' in cstateD: 
      self.dictState = cstateD['CfmVPPassword'] 
    else:
      self.dictState = {}
      cstateD['CfmVPPassword'] = self.dictState 


    self.tbEnterPassword.clicked.connect(self.on_tbEnterPasword_toggle)
    self.lePassword.editingFinished.connect(self.on_lePasswordFinished)
  

  def on_tbEnterPasword_toggle(self):
      """ Нажатие кнопки ввод по вводу пароля"""
      a=''
      try:
         a=eval(self.lePassword.text(), {}, {})
      except: q=0
      if (a==123):
         self.vCE.winCrChVP.show()


 
  def on_lePasswordFinished(self):
      a=1

class CfmChangeVirtPriborsParam(QtGui.QMainWindow, Ui_fmChangeVirtPriborsParam):
  """ Класс  формы изменения параметров Виртуальных приборов """

  def __init__(self,vCE):
    """ Инициализация  формы изменения параметров Виртуальных приборов """
    super(CfmChangeVirtPriborsParam, self).__init__()      
    self.setupUi(self)
    self.vCE=vCE
    self.leTypeCh.editingFinished.connect(self.on_leTypeChFinished)
    self.leAddrCh.editingFinished.connect(self.on_leAddrChFinished)
    self.leTypeVPribor.editingFinished.connect(self.on_leTypeVPriborFinished)
    self.cbChInVPType.currentIndexChanged.connect(self.cbChInVPType_Change)
    self.cbChType.currentIndexChanged.connect(self.cbChType_Change)
    self.cbChAddr.currentIndexChanged.connect(self.cbChAddr_Change)
    self.cbTypeVPribor.currentIndexChanged.connect(self.cbTypeVPribor_Change)
    self.leTypeVPCh.editingFinished.connect(self.on_leTypeVPChFinished)
    self.tbAddTypeVPCh.clicked.connect(self.AddTypeVPCh)
    self.tbDelTypeVPCh.clicked.connect(self.DelTypeVPCh)
    self.tbChangeTypeVPCh.clicked.connect(self.ChangeTypeVPCh)
    self.tbAddChName.clicked.connect(self.AddChName)
    self.tbDelChName.clicked.connect(self.DelChName)
    self.tbAddChAddr.clicked.connect(self.AddChAddr)
    self.tbDelChAddr.clicked.connect(self.DelChAddr)
    self.tbAddVPType.clicked.connect(self.AddVPType)
    self.tbDelVPType.clicked.connect(self.DelVPType)
    self.tbChangeChName.clicked.connect(self.ChangeChName)
    self.tbChangeChAddr.clicked.connect(self.ChangeChAddr)
    self.tbChangeVPType.clicked.connect(self.ChangeVPType)
    self.tbAddChTempl.clicked.connect(self.AddChTempl)
    self.tbChangeChTempl.clicked.connect(self.ChangeChTempl)
    self.tbDelChTempl.clicked.connect(self.DelChTempl)
    self.tbAddChInMessTempl.clicked.connect(self.AddChInMessTempl)
    self.tbChangeChInMessTempl.clicked.connect(self.ChangeChInMessTempl)
    self.tbDelChInMessTempl.clicked.connect(self.DelChInMessTempl)
    self.lwChTempl.currentItemChanged.connect(self.lwChTempl_Change)
    self.lwChInMessTempl.currentItemChanged.connect(self.lwChInMessTempl_Change)
    self.leTypeMess.editingFinished.connect(self.on_leTypeMessFinished)
    self.cbChTypeTempl.currentIndexChanged.connect(self.cbChTypeTempl_Change)
    self.cbChAddrTempl.currentIndexChanged.connect(self.cbChAddrTempl_Change)

  def cbTypeMess_2_Change(self):
    """ Выбор типа канала измерителя """
    curIndex=self.cbTypeMess_2.currentIndex()
    if curIndex==0:
        self.lblch_1.setText('Канал ток')
        self.lblch_2.setVisible(0)
        self.cbCh_2.setVisible(0)
    if curIndex==1:
        self.lblch_1.setText('Канал  напряжение')
        self.lblch_2.setVisible(0)
        self.cbCh_2.setVisible(0)
    if curIndex==2:
        self.lblch_1.setText('Канал температура')
        self.lblch_2.setVisible(0)
        self.cbCh_2.setVisible(0)
    if curIndex==3:
        self.lblch_1.setText('Канал напряжение')
        self.lblch_2.setText('Канал температура')
        self.lblch_2.setVisible(1)
        self.cbCh_2.setVisible(1)
    if curIndex==4:
        self.lblch_1.setText('Канал ток')
        self.lblch_2.setText('Канал температура')
        self.lblch_2.setVisible(1)
        self.cbCh_2.setVisible(1)
 
  def AddChannel(self):
    """  Добавить канал измерителя"""
    self.curAdrCh=self.leModbusNum.text()
    self.curIndCh=self.leIndexMess.text()
    self.curTypeCh=self.cbTypeMess.currentText()
    self.lwVIns_3.addItem('[адрес='+self.curAdrCh+'] Измеритель '+self.curTypeCh+self.curIndCh+' 0x204')

    global cfg_stateD
    self.addPar={}
    self.addPar1=[]
    self.addPar2=[]
    self.tmp={}
    self.tmp1={}
    self.addPar['адрес']=self.curAdrCh
    self.addPar2.append(self.curTypeCh+self.curIndCh)
    self.addPar2.append('0x204')
    self.addPar1.append(self.addPar2)
    self.addPar['канал']=self.addPar1

    self.tmp=sstate.cfg_stateD['MODBUS RTU'][0]['Измеритель'][0]
    sstate.cfg_stateD['MODBUS RTU'][0]['Измеритель'].append(self.addPar)
    self.cbCh_1.AddItem('[адрес='+self.curAdrCh+'] Измеритель '+self.curTypeCh+self.curIndCh+' 0x204');
    self.cbCh_2.AddItem('[адрес='+self.curAdrCh+'] Измеритель '+self.curTypeCh+self.curIndCh+' 0x204');
    a=1


  def DelChannel(self):
      """ Удалить канал измерителя """
      a=self.lwVIns_3.currentRow()
      self.lwa=self.lwVIns_3.takeItem(a)
      self.lwVIns_3.removeItemWidget(self.lwa)
      self.cbCh_1.removeItem(a);
      self.cbCh_2.removeItem(a);
      del  sstate.cfg_stateD['MODBUS RTU'][0]['Измеритель'][a]

  def AddVPribor(self):
    """ Добавить виртуальный прибор"""
    self.addVPar={}
    self.addVPar1=[]
    self.addVPar2=[]
    self.tmpV={}
    self.tmpV1={}
    self.tmpCaption=' '
    curChIndex1=self.cbCh_1.currentIndex()
    curChIndex2=self.cbCh_2.currentIndex()
    curIndex=self.cbTypeMess_2.currentIndex()
    curtxt=self.cbTypeMess_2.currentText()
    indx=self.leIndexMess_2.text()
    if curIndex==0:
        self.tmpCaption='Ток'
        self.addVPar['каналТок']=sstate.cfg_stateD['MODBUS RTU'][0]['Измеритель'][curChIndex1]['канал'][0][0]
        self.addVPar['наименование']=self.tmpCaption+indx
        z= sstate.cfg_stateD['Виртуальные приборы'][curtxt].append(self.addVPar)
    if curIndex==1:
        self.tmpCaption='Напряжение'
        self.addVPar['каналН']=sstate.cfg_stateD['MODBUS RTU'][0]['Измеритель'][curChIndex1]['канал'][0][0]
        self.addVPar['наименование']=self.tmpCaption+indx
        z= sstate.cfg_stateD['Виртуальные приборы'][curtxt].append(self.addVPar)
    if curIndex==2:
        self.tmpCaption='Температура'
        self.addVPar['каналТ']=sstate.cfg_stateD['MODBUS RTU'][0]['Измеритель'][curChIndex1]['канал'][0][0]
        self.addVPar['наименование']=self.tmpCaption+indx
        z= sstate.cfg_stateD['Виртуальные приборы'][curtxt].append(self.addVPar)
    if curIndex==3:
        self.tmpCaption='Иономер'
        self.addVPar['каналН']=sstate.cfg_stateD['MODBUS RTU'][0]['Измеритель'][curChIndex1]['канал'][0][0]
        self.addVPar['каналТ']=sstate.cfg_stateD['MODBUS RTU'][0]['Измеритель'][curChIndex2]['канал'][0][0]
        self.addVPar['наименование']=self.tmpCaption+indx
        z= sstate.cfg_stateD['Виртуальные приборы'][curtxt].append(self.addVPar)
    if curIndex==4:
        self.tmpCaption='Кислородомер'
        self.addVPar['каналТок']=sstate.cfg_stateD['MODBUS RTU'][0]['Измеритель'][curChIndex1]['канал'][0][0]
        self.addVPar['каналТ']=sstate.cfg_stateD['MODBUS RTU'][0]['Измеритель'][curChIndex2]['канал'][0][0]
        self.addVPar['наименование']=self.tmpCaption+indx
        z= sstate.cfg_stateD['Виртуальные приборы'][curtxt].append(self.addVPar)

    self.lwVIns.addItem(self.tmpCaption+indx+'['+curtxt+']')

    a=1

  def DelVPribor(self):
      """ Удалить виртуальный прибор """
      del_type=0
      del_type_index=0
      del_num_index=0
      a=self.lwVIns.currentRow()
      a_str=self.lwVIns.item(a).text()
      b_=a_str
      d=b_.find('Измеритель тока')
      if b_.find('Измеритель тока')>=0:
          del_type='Измеритель тока'
          del_type_index=1
      if b_.find('Вольтметр')>=0:
          del_type='Вольтметр'
          del_type_index=2
      if b_.find('Термометр')>=0:
          del_type='Термометр'
          del_type_index=3
      if b_.find('Иономер')>=0:
          del_type='Иономер'
          del_type_index=4
      if b_.find('Кислородомер')>=0:
          del_type='Кислородомер'
          del_type_index=5
      if b_.find('0')>=0: del_num_index=0
      if b_.find('1')>=0: del_num_index=1
      if b_.find('2')>=0: del_num_index=2
      if b_.find('3')>=0: del_num_index=3
      if b_.find('4')>=0: del_num_index=4
      if b_.find('5')>=0: del_num_index=5
      self.lwa_vp=self.lwVIns.takeItem(a)
      self.lwVIns.removeItemWidget(self.lwa_vp)
      z= sstate.cfg_stateD['Виртуальные приборы'][del_type][del_num_index-1]
      del  sstate.cfg_stateD['Виртуальные приборы'][del_type][del_num_index-1]
      s=3


  def showEvent(self,e):
      """ Показ формы"""
      global cfg_stateD
      self.vCE.InitPortNum()
      self.vCE.winCrChVP.close()


  def SaveSettings(self):
      """ Сохранение параметров и номера порта """
      global Cfg 
      global cfg_stateD
      sstate.cfg_stateD['MODBUS RTU'][0]['порт']=self.lePortNum.text();
      sstate.save_Cfg_state()

  def on_leModbusNumFinished(self):
      a=1

  def on_leIndexMessFinished(self):
      a=1

  def on_leTypeChFinished(self):
      a=1

  def on_leAddrChFinished(self):
      a=1

  def on_lePortNumFinished(self):
      a=1

  def on_leIndexVPriborFinished(self):
      a=1

  def on_leTypeVPriborFinished(self):
      a=1

  def AddChTempl(self):
      """ Добавление шаблона канала"""
      self.vCE.AddChTempl()

  def ChangeChTempl(self):
      """ Изменение шаблона канала"""
      self.vCE.ChangeChTempl()

  def DelChTempl(self):
      """ Удаление шаблона канала"""
      self.vCE.DelChTempl()

  def AddChInMessTempl(self):
      """ Добавление канала в шаблон измерителя"""
      self.vCE.AddChInMessTempl()

  def ChangeChInMessTempl(self):
      """ Изменение канала в шаблоне измерителя"""
      self.vCE.ChangeChInMessTempl()

  def DelChInMessTempl(self):
      """ Удаление канала из шаблона измерителя"""
      self.vCE.DelChInMessTempl()

  def lwChTempl_Change(self):
      a=1

  def lwChInMessTempl_Change(self):
      a=1

  def on_leTypeMessFinished(self):
      a=1

  def cbChTypeTempl_Change(self):
      a=1

  def cbChAddrTempl_Change(self):
      a=1

  def lwCh_Change(self):
    """ изменение канала в списке измерительных модулей"""    
    tmpchangech=self.lwCh.currentRow()
    if(tmpchangech>=0):
     tmpName=self.vCE.CommonProfil_stateD['MessChanels']['ChMessList'][tmpchangech]
     self.vCE.CurrChName=tmpName
     self.vCE.CurrChIndex=tmpchangech
     self.leIndexMess.setText(tmpName)
     self.leIndexMess.clearFocus()
     self.leModbusNum.setText(self.vCE.CommonProfil_stateD['MessChanels'][tmpName]['AdrMODBUS'])
     self.leModbusNum.clearFocus()
     self.vCE.InitChListCh()

  def lwVIns_Change(self):
    """ изменение ВП в списке ВП"""
    tmpchangeVP=self.lwVIns.currentRow()
    if(tmpchangeVP>=0):
     tmpVPName=self.vCE.CommonProfil_stateD['VirtPribors']['VirtPriborList'][tmpchangeVP]
     self.vCE.CurrVPName=tmpVPName
     self.vCE.CurrVPIndex=tmpchangeVP
     self.leIndexVPribor.setText(tmpVPName)
     self.leIndexVPribor.clearFocus()
     self.vCE.CurrVPType=self.vCE.CommonProfil_stateD['VirtPribors'][tmpVPName]['VPType']
     i=0
     while(i<self.vCE.CommonProfil_stateD['VPriborsTypesListCounter']):
      tmpVPType=self.vCE.CommonProfil_stateD['VPriborsTypesList'][i]
      if(tmpVPType==self.vCE.CurrVPType): self.cbTypeVPribor.setCurrentIndex(i)
      i=i+1
     self.vCE.InitVPChList()
     self.vCE.InitVPChOutList()

  def cbChType_Change(self):
      """  Изменение выбора типа измерительного модуля"""
      if(self.cbChType.currentIndex()>-1):
       self.leTypeCh.setText(self.vCE.CommonProfil_stateD['MessChanels']['ChMessTypesList'][self.cbChType.currentIndex()])
       self.leTypeCh.clearFocus() 

  def cbChAddr_Change(self):
      """  Изменение выбора адреса измерительного модуля"""
      if(self.cbChAddr.currentIndex()>-1):
       self.leAddrCh.setText(self.vCE.CommonProfil_stateD['MessChanels']['ChMessAddrList'][self.cbChAddr.currentIndex()])
       self.leAddrCh.clearFocus() 

  def cbTypeVPribor_Change(self):
      """  Изменение выбора типа ВП"""
      if(self.cbTypeVPribor.currentIndex()>-1):
       self.leTypeVPribor.setText(self.vCE.CommonProfil_stateD['VPriborsTypesList'][self.cbTypeVPribor.currentIndex()])
       self.leTypeVPribor.clearFocus()

  def cbChVPribor_1_Change(self):
      a=1

  def cbChVPribor_2_Change(self):
      a=1

  def AddCh(self):
      """ Добавление канала"""
      self.vCE.AddCh()

  def DelCh(self):
      """ Удаление канала"""
      self.vCE.DelCh()

  def ChangeCh(self):
      """ Удаление канала """
      self.vCE.ChangeCh()

  def AddChName(self):
      """ Добавление имени канала"""
      self.vCE.AddChName()

  def DelChName(self):
      """ Удаление имени канала"""
      self.vCE.DelChName()

  def AddChAddr(self):
      """ Добавление адреса канала"""
      self.vCE.AddChAddr()

  def DelChAddr(self):
      """ Удаление адреса канала"""
      self.vCE.DelChAddr()

  def SavePortNum(self):
      """ Запись номера порта"""
      self.vCE.SavePortNum()

  def AddVPribor(self):
      """ Добавление ВП"""
      self.vCE.AddVPribor()

  def DelVPribor(self):
      """ Удаление ВП"""
      self.vCE.DelVPribor()

  def ChangeVPribor(self):
      """ Изменение ВП"""
      self.vCE.ChangeVPribor()

  def AddVPType(self):
      """ Добавление типа ВП"""
      self.vCE.AddVPType()

  def DelVPType(self):
      """ Удаление типа ВП"""
      self.vCE.DelVPType()

  def ChangeChName(self):
      """ Изменение имени канала"""
      self.vCE.ChangeChName()

  def ChangeChAddr(self):
      """ Изменение адреса канала"""
      self.vCE.ChangeChAddr()

  def ChangeVPType(self):
      """ Изменение типа канала"""
      self.vCE.ChangeVPType()

  def lwChInMess_Change(self):
      a=1

  def lwChInVP_Change(self):
      a=1

  def cbChInVPType_Change(self):
      """ Изменение списка типа канала  для ВП"""
      if(self.cbChInVPType.currentIndex()>-1):
       self.leTypeVPCh.setText(self.vCE.CommonProfil_stateD['VPriborsTypesChList'][self.cbChInVPType.currentIndex()])
       self.leTypeVPCh.clearFocus()

  def cbChInVPName_Change(self):
      a=1

  def AddChInMess(self):
      """ Добавление канала в измеритель"""
      self.vCE.AddChInMess()

  def ChangeChInMess(self):
      """ Изменение канала в измерителе"""
      self.vCE.ChangeChInMess()

  def DelChInMess(self):
      """ Удаление канала из измерителя"""
      self.vCE.DelChInMess()

  def AddChInVP(self):
      """ Добавление канала в ВП """
      self.vCE.AddChInVP()

  def ChangeChInVP(self):
      """ Изменение канала в ВП """
      self.vCE.ChangeChInVP()

  def DelChInVP(self):
      """ Удаление канала из ВП """
      self.vCE.DelChInVP()

  def on_leTypeVPChFinished(self):
      q=1

  def AddTypeVPCh(self):
      """ Добавление типа канала """
      self.vCE.AddTypeVPCh()

  def DelTypeVPCh(self):
      """ Удаление типа канала ВП """
      self.vCE.DelTypeVPCh()

  def ChangeTypeVPCh(self):
      """ Изменение типа канала ВП """
      self.vCE.ChangeTypeVPCh()

  def SaveAllVPSetting(self):
      a=1

class CProgrammer:
  """ Класс программирования даных в измерительные модули """
   
  def __init__(self,vCE, tmpDB1):
    """Инициализация класса """
    self.vCE=vCE
    self.tmpDB1=tmpDB1
    

  def SaveEEPROM(self):
    """Запись в EEPROM """
    self.DirID=0
    self.new_addr=0
    self.serial_num=0
    res1=svi.Programm_SN(self.DirID, 0, self.new_addr, self.serial_num)
    res=ToUns16(res1)
    q=1
    
class CDBEditor:
  """ Класс редактора базы данных"""

  def __init__(self,vCE, tmpDB1):
    """Инициализация редактора базы данных"""
    self.tmpDB1=tmpDB1
    self.vCE=vCE
    self.MaxIndex=0

    self.CurrIndex=0
    self.Curr_SN=0
    self.Curr_Date=0
    self.Curr_Type=0
    self.Curr_HWVersion=0
    self.Curr_SVersion=0
    self.Curr_Comment=0

  def SetCurrIndex(self,i):
    """Обработка текущей записи """
    self.CurrIndex=i
    self.currRow=self.CurrIndex
    self.Curr_SN=self.vCE.LocalProfil_stateD['S_Number'][self.currRow]
    self.Curr_Date=self.vCE.LocalProfil_stateD['Date'][self.currRow]
    self.Curr_Type=self.vCE.LocalProfil_stateD['Type'][self.currRow]
    self.Curr_HWVersion=self.vCE.LocalProfil_stateD['HW_Version'][self.currRow]
    self.Curr_SVersion=self.vCE.LocalProfil_stateD['Soft_Version'][self.currRow]
    self.Curr_Comment=self.vCE.LocalProfil_stateD['Comment'][self.currRow]

  def edit(self, SN, Date, Type, HWVersion, SVersion, Comment):
    """Редактирование текущей записи """
    self.vCE.LocalProfil_stateD['S_Number'][self.currRow]=SN
    self.vCE.LocalProfil_stateD['Date'][self.currRow]=Date
    self.vCE.LocalProfil_stateD['Type'][self.currRow]=Type
    self.vCE.LocalProfil_stateD['HW_Version'][self.currRow]=HWVersion
    self.vCE.LocalProfil_stateD['Soft_Version'][self.currRow]=SVersion
    self.vCE.LocalProfil_stateD['Comment'][self.currRow]=Comment

  def Add(self, SN=0, Date=0, Type=0, HWVersion=0, SVersion=0, Comment='0'):
    """Добавление записи """
    self.currRow=self.vCE.LocalProfil_stateD['Counter']+1
    self.vCE.LocalProfil_stateD['Counter']=self.currRow
    self.vCE.LocalProfil_stateD['S_Number'][self.currRow]=SN
    self.vCE.LocalProfil_stateD['Date'][self.currRow]=Date
    self.vCE.LocalProfil_stateD['Type'][self.currRow]=Type
    self.vCE.LocalProfil_stateD['HW_Version'][self.currRow]=HWVersion
    self.vCE.LocalProfil_stateD['Soft_Version'][self.currRow]=SVersion
    self.vCE.LocalProfil_stateD['Comment'][self.currRow]=Comment

  def delete(self):
    """Удаление записи """
    try:
      self.currRow=self.vCE.LocalProfil_stateD['Counter']
      del self.vCE.LocalProfil_stateD['S_Number'][self.currRow]
      del self.vCE.LocalProfil_stateD['Date'][self.currRow]
      del self.vCE.LocalProfil_stateD['Type'][self.currRow]
      del self.vCE.LocalProfil_stateD['HW_Version'][self.currRow]
      del self.vCE.LocalProfil_stateD['Soft_Version'][self.currRow]
      del self.vCE.LocalProfil_stateD['Comment'][self.currRow]
      self.currRow=self.vCE.LocalProfil_stateD['Counter']-1
      self.vCE.LocalProfil_stateD['Counter']=self.currRow
    except: r=0

  def Create(self):
    """Создание новой записи """
    self.vCE.LocalProfil_stateD={}
    self.vCE.LocalProfil_stateD['S_Number']={}
    self.vCE.LocalProfil_stateD['Date']={}
    self.vCE.LocalProfil_stateD['Type']={}
    self.vCE.LocalProfil_stateD['HW_Version']={}
    self.vCE.LocalProfil_stateD['Soft_Version']={}
    self.vCE.LocalProfil_stateD['Comment']={}
    self.vCE.LocalProfil_stateD['Counter']=0
    q=0

  def CreateSearchTable(self):
    """ Создание таблицы найденных модулей"""
    self.vCE.LocalProfil_stateD['SearchTable']={}
    self.vCE.LocalProfil_stateD['SearchTable']['S_Number']={}
    self.vCE.LocalProfil_stateD['SearchTable']['Date']={}
    self.vCE.LocalProfil_stateD['SearchTable']['Type']={}
    self.vCE.LocalProfil_stateD['SearchTable']['HW_Version']={}
    self.vCE.LocalProfil_stateD['SearchTable']['Soft_Version']={}
    self.vCE.LocalProfil_stateD['SearchTable']['Comment']={}
    self.vCE.LocalProfil_stateD['SearchTable']['Counter']=0
    q=0

  def Save(self):
    """Сохранение базы в словаре """
    self.vCE.save_LocalProfil_state()

  def Programm(self):
    """Запись данных в EEPROM """
    self.vCE.Programmer.edit
#--- ------------------------------------    -----------------------------------------------------------     
class CConfigEditor:
  """ Основной класс - класс редактора конфигураций """
   

  def __init__(self, fTech1,Cfg1,chanD1,vinstrD1):
    """ Инициализация класса редактора конфигураций """
    self.state_dir1 = os.path.dirname(os.path.abspath(__file__)) 
    self.PortOpened=0
    self.DigData=''
    self.StrData=''
    self.ChannelsInit=0
    self.chNamesD = {}    # вспомогательный словарь (key - наименование канала; value - ID канала
    self.DirID=1
    self.Close_Config_Flag=0
    self.OpenProfilVP_1Flag=0
    self.OpenProfilVP_2Flag=0
    self.winSelectConfig = CfmSelectConfig(self)
    self.winCrConf = CfmCreateConfig(self)
    self.winVPPassword = CfmVPPassword(self)
    self.winCrChVP = CfmChangeVirtPribors(self)
    self.winCrChVPParam = CfmChangeVirtPriborsParam(self)
    self.winWelcome=CfmWelcome(self)
    self.winDigitalKeyboard=CfmDigitalKeyboard(self)
    self.winKeyboard=CfmKeyboard(self)
    self.tmpDB={}
    self.DBEditor=CDBEditor(self,self.tmpDB)
    self.Programmer=CProgrammer(self,self.tmpDB)
    self.LocalProfil_stateD = {}
    self.CommonProfil_stateD = {}
    self.CurrCfgName =''
    self.DelCfgName =''
    self.CurrCfgIndex =-1
    self.NumConfigs=0
    self.CurrCFGVPListCount=0
    self.load_CommonProfil_state()
    self.load_LocalProfil_state()
    self.WaitFLAG=0
    self.fTech1=fTech1
    self.Cfg1=Cfg1
    self.chanD1=chanD1
    self.vinstrD1=vinstrD1
    self.winfmProgramming_1_0=CfmProgramming_1_1(self)
    self.winfmAllSearch_1_0=CfmAllSearch_1_0(self)
    self.InitChAddrList()
    self.InitChTypeList()
    self.InitVPTypeList()
    self.InitVPChTypeList()
    self.winWelcome.show()

  def Test(self):
    """ Тест """
    self.mainWindow = MainWindow()
    self.mainWindow.setGeometry(100, 100, 800, 500)
    self.mainWindow.show()

  def TechStart1(self,Cfg1):
    """ Старт в технологическом режиме """
    global winM      # основное окно (в зависимости от режима может быть технологическим или пользовательским)
    global winPC     # консоль порта
    global winMBC    # консоль драйвера MODBUS
    global winADC    # прямой доступ к AD779x 
    global winPV     # параметризация милливольтметра
    global winCV     # конфигурирование милливольтметра
    global winPAmper     # параметризация амперметра
    global winCAmper     # конфигурирование амперметра
    global winPT     # параметризация термометра
    global winCT     # конфигурирование термометра
    global winPTP     # параметризация термометра измеритель давления
    global winCTP     # конфигурирование термометр измеритель давления
    global winPCond     # параметризация кондуктометра
    global winCCond     # конфигурирование кондуктометра
    global dgReg     # диалог определения нового регистра
    global winConv   # окно для ввода коэффициентов масштабного преобразования для окна прямого доступа к АЦП AD779x
    global gActDirID # код активного направления (пока драйвер поддерживает только одно)
        # технологический режим - подготовка дополнительных окон  
    self.winM = svi.CfmNaladka(self,Cfg1)
    self.winPC = svi.CfmPortCons(self)
    self.winMBC =svi. CfmMBCons(self,svi.main_dir)
    self.winADC = svi.CfmAD779x(self)
    self.winPV = svi.CfmVPar(self,Cfg1["Калибровка мВ"])
    self.winCV =svi. CfmVConf(self,Cfg1["Конфигурация мВ"], int(Cfg1["Калибровка мВ"]["ZeroA32"]), int(Cfg1["Калибровка мВ"]["mK32"]))
    self.winPAmper = svi.CfmAmperPar(self,Cfg1["Калибровка мкА"])
    self.winCAmper = svi.CfmAmperConf(self,Cfg1["Конфигурация мкА"], int(Cfg1["Калибровка мкА"]["ZeroA32"]), int(Cfg1["Калибровка мкА"]["mK32"]), int(Cfg1["Калибровка мкА"]["Count_Amper"]))    
    self.winPCond =svi. CfmCondPar(self,Cfg1["Калибровка Кондуктометр"])
    self.winCCond = svi.CfmCondConf(self,Cfg1["Конфигурация Кондуктометр"], int(Cfg1["Калибровка Кондуктометр"]["ZeroA32"]), int(Cfg1["Калибровка Кондуктометр"]["mK32"]))
    self.winPT = svi.CfmTPar(self,Cfg1["Калибровка T"])
    self.winCT = svi.CfmTConf(self,Cfg1["Конфигурация T"], int(Cfg1["Калибровка T"]["CR0"]))
    self.winPTP = svi.CfmTPPar(self,Cfg1["Калибровка P"])
    self.winCTP = svi.CfmTPConf(self,Cfg1["Конфигурация P"], int(Cfg1["Калибровка P"]["CR0"]),  int(Cfg1["Калибровка P"]["P0"]),  int(Cfg1["Калибровка P"]["Ap"]))
    self.dgReg = svi.CfmNewReg(self)
    self.winConv = svi.CfmNewConv(self)
    self.winM.show()
    a=1

  def InitConfigList(self):
     """ Инициализация листа существующих конфигураций """
     try:

      #self.CommonProfil_stateD['MessChanels']['ChMessList']={}
      #self.CommonProfil_stateD['MessChanels']['ChMessListCounter']=0
      #self.CommonProfil_stateD['VirtPribors']={}
      #self.CommonProfil_stateD['VirtPribors']['VirtPriborList']={}
      #self.CommonProfil_stateD['VirtPribors']['VirtPriborsListCounter']=0
      #del(self.CommonProfil_stateD['VirtPribors']['VirtPriborList'][2])
      #self.CommonProfil_stateD['MessChanels']['ChMessListCounter']=0
      #del self.CommonProfil_stateD['VirtPribors']['VirtPriborList'][9]
      #self.CommonProfil_stateD['VirtPribors']['VirtPriborsListCounter']=9
      #self.save_CommonProfil_state()

      self.NumConfigs=self.CommonProfil_stateD['Configs']
      self.winSelectConfig.lwConf.clear()
      j=0
      while (j<self.NumConfigs) :
          tmpcfg=self.CommonProfil_stateD['CFGList'][j]
          try:
            tmpYesVPCh=self.CommonProfil_stateD['CFG'][tmpcfg]['VPConfigYes']
          except:tmpYesVPCh='0'
          self.winSelectConfig.lwConf.addItem(str(tmpYesVPCh)+' '+str(tmpcfg))
          j=j+1
     except:
        q=0
     q=0

  def UpConfigInList(self,a):
     """ Перемещение выбранной конфигурации вверх по листу конфигураций """
     try:
         if (a!=0):
             tmpCnf=self.CommonProfil_stateD['CFGList'][a]
             tmpCnf2=self.CommonProfil_stateD['CFGList'][a-1]
             self.CommonProfil_stateD['CFGList'][a]=tmpCnf2
             self.CommonProfil_stateD['CFGList'][a-1]=tmpCnf             
     except:
        q=0

  def DownConfigInList(self,a):
     """ Перемещение выбранной конфигурации вниз по листу конфигураций """
     try:
         if (a!=self.CommonProfil_stateD['Configs']-1):
             tmpCnf=self.CommonProfil_stateD['CFGList'][a+1]
             tmpCnf2=self.CommonProfil_stateD['CFGList'][a]
             self.CommonProfil_stateD['CFGList'][a+1]=tmpCnf2
             self.CommonProfil_stateD['CFGList'][a]=tmpCnf
     except:
        q=0


  def LoadCurrConfigList(self,tmpi):
     Results.Result_Dict.clear()
     """ Загрузка выбранной конфигурации """
     self.CommonProfil_stateD['CurrCFG']={}
     self.CommonProfil_stateD['CurrCFG']['CurrCFGVPList']={}
     self.CommonProfil_stateD['CurrCFG']['CurrCFGVPListCount']=0
     if (tmpi>=0):
          self.CurrCfgName =self.CommonProfil_stateD['CFGList'][tmpi]
          self.CurrCfgIndex =tmpi
          tmpname=self.CommonProfil_stateD['CFGList'][tmpi]
          self.CommonProfil_stateD['LastCfgName']=tmpname
          self.LastConfigName=tmpname
          self.winCrConf.leConfName.setText(tmpname)
          self.winCrConf.leConfName.clearFocus()
          self.CommonProfil_stateD['CurrCFG']={}
          self.CommonProfil_stateD['CurrCFG']=self.CommonProfil_stateD['CFG'][tmpname]
          self.save_CommonProfil_state()
     self.InitCurrConfigList()

  def LoadLastConfigList(self):
      """ Загрузка последней выбранной конфигурации """
      self.NumConfigs=self.CommonProfil_stateD['Configs']
      j=0
      tmpi=-1
      self.LastConfigName=self.CommonProfil_stateD['LastCfgName']
      while (j<self.NumConfigs) :
          tmpName=self.CommonProfil_stateD['CFGList'][j]
          if (self.LastConfigName==tmpName): tmpi=j
          j=j+1
      #if (tmpi>=0):
      if (tmpi!=-1): self.LoadCurrConfigList(tmpi)

  def InitCurrConfigList(self):
   """ Инициализация листа текущей конфигурации """
   try:
      self.CurrCFGVPListCount=self.CommonProfil_stateD['CurrCFG']['CurrCFGVPListCount']
      self.winCrConf.lwConf.clear()
      self.winCrConf.cb_In_2.clear()
      j=0
      while (j<=self.CurrCFGVPListCount-1) :
          tmpn=self.CommonProfil_stateD['CurrCFG']['CurrCFGVPList'][j]
          try:
            tmpnyes=self.CommonProfil_stateD['CurrCFG'][tmpn]['VPYes']
          except: tmpnyes=0
          self.winCrConf.lwConf.addItem(str(tmpnyes)+' '+str(tmpn))
          self.winCrConf.cb_In_2.addItem(str(tmpnyes)+' '+str(tmpn))
          j=j+1
   except:
    LL.exception('')
   tmpd=''
   try:
     tmpd=self.CommonProfil_stateD['CurrCFG']['Descr']     
   except:
    LL.exception('')
   self.winCrConf.leConfDescr.setText(tmpd)

  def CheckCurrConfigList(self, vpname):
   """ Инициализация листа текущей конфигурации """
   Res=0
   try:
      _CurrCFGVPListCount=self.CommonProfil_stateD['CurrCFG']['CurrCFGVPListCount']
      self.winCrConf.lwConf.clear()
      self.winCrConf.cb_In_2.clear()
      j=0
      while (j<=_CurrCFGVPListCount-1) :
          tmpn=self.CommonProfil_stateD['CurrCFG']['CurrCFGVPList'][j]
          if(tmpn==vpname): Res=1
          j=j+1
   except:
    LL.exception('')
    Res=2
   return Res

  def SelectConfig(self,ConfigName):
    i=1

  def DeleteConfig(self,ConfigNum):
    """ Удаление выбранной конфигурации"""
    ii=0
    self.tmpNum=ConfigNum
    self.tmpName=self.CommonProfil_stateD['CFGList'][self.tmpNum]
    tmpDictCfg={}
    tmpDictCfg_={}    
    tmpDictCfg=self.CommonProfil_stateD['CFGList'].copy()
    while(self.tmpNum<self.NumConfigs-1):
        tmpDictCfg[self.tmpNum]=tmpDictCfg[self.tmpNum+1]
        self.tmpNum=self.tmpNum+1
    del(tmpDictCfg[self.NumConfigs-1])
    tmpDictCfg2={}
    tmpDictCfg2_={}
    tmpDictCfg2=self.CommonProfil_stateD['CFG'].copy()
    del(tmpDictCfg2[self.tmpName])
    self.NumConfigs=self.NumConfigs-1
    self.CommonProfil_stateD['Configs']=self.NumConfigs
    self.CommonProfil_stateD['CFGList']=tmpDictCfg_
    self.CommonProfil_stateD['CFG']=tmpDictCfg2_
    self.CommonProfil_stateD['CFGList'].update(tmpDictCfg)
    self.CommonProfil_stateD['CFG'].update(tmpDictCfg2)
    self.save_CommonProfil_state()
    self.InitConfigList()


  def SaveConfig(self,ConfigName):
    """ Сохранение конфигурации """
    try:
      tmpDict={}
      tmpDict2={}
      tmpDictCfg={}
      tmpDict_={}
      tmpDict2_={}
      tmpDictCfg_={}
      tmp=''
      ii=0
      cf=0
      while (ii<self.NumConfigs):
          if (ConfigName==self.CommonProfil_stateD['CFGList'][ii]): cf=1
          ii=ii+1
      if(cf==0):
        self.CurrCfgName=ConfigName
        self.NumConfigs=self.NumConfigs+1
        tmpDict2=self.CommonProfil_stateD['CFGList'].copy()
        tmp=str(self.NumConfigs-1)
        tmpDict2[(self.NumConfigs-1)]=self.CurrCfgName
        self.CommonProfil_stateD['CFGList']={}
        self.CommonProfil_stateD['CFGList'].update(tmpDict2)
      tmpDictCfg=self.CommonProfil_stateD['CFG'].copy()
      self.CommonProfil_stateD['Configs']=self.NumConfigs
      tmpDictCfg[self.CurrCfgName]={}
      tmpDictCfg[self.CurrCfgName]=self.CommonProfil_stateD['CurrCFG'].copy()
      self.CommonProfil_stateD['CFG']={}      
      self.CommonProfil_stateD['CFG'].update(tmpDictCfg.copy())
      self.save_CommonProfil_state()
      self.save_LocalProfil_state()
    except:
        LL.I("Ошибка сохранения конфигурации {} ".format(ConfigName))
        q=0

  def InitVirtPriborList(self):
      """ Инициализация листа виртуальных приборов """
      self.VirtPriborsListCounter=self.CommonProfil_stateD['VirtPribors']['VirtPriborsListCounter']
      self.winCrConf.lwVP.clear()
      self.winCrChVP.lwVIns.clear()
      j=0
      while (j<=self.VirtPriborsListCounter-1) :
          tmpname= self.CommonProfil_stateD['VirtPribors']['VirtPriborList'][j]
          try:
             tmpYes=self.CommonProfil_stateD['VirtPribors'][tmpname]['VPYes']
          except: tmpYes='0'
          self.winCrConf.lwVP.addItem(str(tmpYes)+'  '+str(tmpname))
          self.winCrChVP.lwVIns.addItem(str(tmpYes)+'  '+str(tmpname))
          j=j+1

  def CheckVirtPriborList(self,vpName=' '):
      """ Инициализация листа виртуальных приборов """
      Ret=0;
      self.VirtPriborsListCounter=self.CommonProfil_stateD['VirtPribors']['VirtPriborsListCounter']
      self.winCrConf.lwVP.clear()
      self.winCrChVP.lwVIns.clear()
      j=0
      while (j<=self.VirtPriborsListCounter-1) :
          tmpname= self.CommonProfil_stateD['VirtPribors']['VirtPriborList'][j]
          if(vpName==tmpname): Ret=1
          j=j+1
      return Ret

  def ConfVPInList(self):
      """ Инициализация списка входов вмртуальных приборов """
      self.ChVPConfigListCounter=self.CommonProfil_stateD['CurrCFG'][self.CurrVPCurrCfgName]['VPChListCounter']
      tmpi=0
      self.winCrConf.lwConfVPIn.clear()
      while(tmpi<self.ChVPConfigListCounter):
          try:
              tmpyes=self.CommonProfil_stateD['CurrCFG'][self.CurrVPCurrCfgName]['VPChModulNameYesList'][tmpi]
          except: tmpyes=0
          self.winCrConf.lwConfVPIn.addItem(str(tmpyes)+' '+self.CommonProfil_stateD['CurrCFG'][self.CurrVPCurrCfgName]['VPChTypeList'][tmpi]+" ,"+self.CommonProfil_stateD['CurrCFG'][self.CurrVPCurrCfgName]['VPChModulNameList'][tmpi]+" ,"+self.CommonProfil_stateD['CurrCFG'][self.CurrVPCurrCfgName]['VPChNameList'][tmpi])
          tmpi=tmpi+1

  def ConfVPOutList(self):
      """ Инициализация списка выходов вмртуальных приборов """
      try:
        self.ChVPOutConfigListCounter=self.CommonProfil_stateD['CurrCFG'][self.CurrVPCurrCfgName]['VPChOutListCounter']
      except: self.ChVPOutConfigListCounter=0
      tmpi=0
      self.winCrConf.lwConfVPOut.clear()
      while(tmpi<self.ChVPOutConfigListCounter):
          self.winCrConf.lwConfVPOut.addItem(self.CommonProfil_stateD['CurrCFG'][self.CurrVPCurrCfgName]['VPChOutTypeList'][tmpi])
          tmpi=tmpi+1

  def ConfVPInDataList(self):
      q=1

  def SelectVirtPriborInList(self,ConfigName):
    i=1

  def SelectVirtPriborInConfig(self,ConfigName):
    i=1

  def DeleteVirtPriborFromConfig(self,ConfigNum):
    """ Удаление вмртуальных приборов из конфигурации """
    tmpDictCfg={}
    tmpname=''
    self.tmpNum=ConfigNum
    tmpDictCfg=self.CommonProfil_stateD['CurrCFG']['CurrCFGVPList'].copy()
    tmpname=tmpDictCfg[self.tmpNum]
    while(self.tmpNum<self.CurrCFGVPListCount-1):
        tmpDictCfg[self.tmpNum]=tmpDictCfg[self.tmpNum+1]
        self.tmpNum=self.tmpNum+1
    del(tmpDictCfg[self.CurrCFGVPListCount-1])
    self.CurrCFGVPListCount=self.CurrCFGVPListCount-1
    del(self.CommonProfil_stateD['CurrCFG'][tmpname])
    self.CommonProfil_stateD['CurrCFG']['CurrCFGVPList']={}
    self.CommonProfil_stateD['CurrCFG']['CurrCFGVPList'].update(tmpDictCfg)
    self.CommonProfil_stateD['CurrCFG']['CurrCFGVPListCount']=self.CurrCFGVPListCount
    self.save_CommonProfil_state()
    self.InitCurrConfigList()

  def AddVirtPriborToConfig(self):
    """ Добавление вмртуальных приборов в конфигурации """
    i=self.winCrConf.lwVP.currentRow()
    self.CurrCFGVPListCount=self.CommonProfil_stateD['CurrCFG']['CurrCFGVPListCount']
    self.CurrCFGVPListCount=self.CurrCFGVPListCount+1
    VPName=self.CommonProfil_stateD['VirtPribors']['VirtPriborList'][i]
    tmpNewVPName=VPName
    tmpRes=0
    n=2
    tmpNewVPName=VPName+'_1'
    tmpRes=self.CheckCurrConfigList(tmpNewVPName)
    if(tmpRes==1):
        while(tmpRes==1):
           tmpNewVPName_=VPName+'_'+str(n)
           tmpRes=self.CheckCurrConfigList(tmpNewVPName_)
           n=n+1
        tmpNewVPName=tmpNewVPName_

    self.CommonProfil_stateD['CurrCFG']['CurrCFGVPListCount']=self.CurrCFGVPListCount
    self.CommonProfil_stateD['CurrCFG']['CurrCFGVPList'][self.CurrCFGVPListCount-1]=tmpNewVPName
    self.CommonProfil_stateD['CurrCFG'][tmpNewVPName]={}
    self.CommonProfil_stateD['CurrCFG'][tmpNewVPName]=copy.deepcopy(self.CommonProfil_stateD['VirtPribors'][VPName])
    self.save_CommonProfil_state()
    self.InitCurrConfigList()

  def ChangeVirtPriborNameInConfig(self):      
    """ Изменение имени вмртуального прибора в конфигурации """
    tmpRes=0
    tmpVPInCfglst=self.winCrConf.lwConf.currentRow()
    tmpVPInCfgName_New=self.winCrConf.leVPName.text()
    tmpRes=self.CheckCurrConfigList(tmpVPInCfgName_New)
    tmpVPInCfgName=self.CommonProfil_stateD['CurrCFG']['CurrCFGVPList'][tmpVPInCfglst]
    if(tmpRes==1): self.winCrConf.leVPName.setText(tmpVPInCfgName)
    if(tmpRes==0):
      tmpDict={}
      if(tmpVPInCfgName!=tmpVPInCfgName_New):
        self.CommonProfil_stateD['CurrCFG']['CurrCFGVPList'][tmpVPInCfglst]=tmpVPInCfgName_New
        tmpDict=self.CommonProfil_stateD['CurrCFG'][tmpVPInCfgName].copy()
        del(self.CommonProfil_stateD['CurrCFG'][tmpVPInCfgName])
        self.CommonProfil_stateD['CurrCFG'][tmpVPInCfgName_New]={}
        self.CommonProfil_stateD['CurrCFG'][tmpVPInCfgName_New]=tmpDict.copy()
        self.CurrVPInCfgName=tmpVPInCfgName_New
      self.CurrVPCurrCfgName=tmpVPInCfgName_New
      self.save_CommonProfil_state()
    self.InitCurrConfigList()


  def ChangeVirtPriborInConfig(self):      
    """ Изменение подключения вмртуального прибора в конфигурации """
    tmpchangech=self.winCrConf.lwConfVPIn.currentRow()
    j=self.winCrConf.cb_In_2.currentIndex()
    k=self.winCrConf.cb_Ch_2.currentIndex()
    self.CommonProfil_stateD['CurrCFG'][self.CurrVPCurrCfgName]['VPChModulNameList'][tmpchangech]=self.CommonProfil_stateD['CurrCFG']['CurrCFGVPList'][j]
    tmpName=self.CommonProfil_stateD['CurrCFG'][self.CurrVPCurrCfgName]['VPChModulNameList'][tmpchangech]
    self.CommonProfil_stateD['CurrCFG'][self.CurrVPCurrCfgName]['VPChNameList'][tmpchangech]=self.CommonProfil_stateD['CurrCFG'][tmpName]['VPChOutTypeList'][k]
    self.save_CommonProfil_state()
    self.ConfVPInList()
    self.ConfVPOutList()

  def ChangeVirtPriborInConfigOff(self):      
    """ Отключение входов вмртуального прибора в конфигурации """
    tmpchangech=self.winCrConf.lwConfVPIn.currentRow()
    j=self.winCrConf.cb_In_2.currentIndex()
    k=self.winCrConf.cb_Ch_2.currentIndex()
    self.CommonProfil_stateD['CurrCFG'][self.CurrVPCurrCfgName]['VPChModulNameList'][tmpchangech]='0'
    tmpName=self.CommonProfil_stateD['CurrCFG'][self.CurrVPCurrCfgName]['VPChModulNameList'][tmpchangech]
    self.CommonProfil_stateD['CurrCFG'][self.CurrVPCurrCfgName]['VPChNameList'][tmpchangech]='0'
    self.save_CommonProfil_state()
    self.ConfVPInList()
    self.ConfVPOutList()

  def DeleteVirtPriborFromList(self,ConfigNum):      
    """ Удаление  вмртуального прибора из конфигурации """
    tmpDictCfg={}
    self.CommonProfilLst.pop(ConfigNum)
    self.NumConfigs=self.NumConfigs-1
    tmpDictCfg['CFGList']=self.CommonProfilLst
    self.CommonProfil_stateD.update(tmpDictCfg)
    self.save_CommonProfil_state()
    self.InitConfigList()

  def load_CommonProfil_state(self):
   """ Загрузка и сохранение профилей АРМ.
   загрузка словаря таблиц данных """ 
   try:    
    fname = self.state_dir1+'/CommonProfil_state.pk'
    if os.path.isfile(fname):
      with open(fname, 'rb') as pfile:
        self.CommonProfil_stateD.update(pickle.load(pfile))
      LL.I("Загрузка {} выполнена успешно".format(fname))
    else:
      LL.I("Отсутствует {} - словарь CommonProfil_stateD пустой".format(fname)) 
   except:
    LL.E("Ошибка при загрузке {}".format(fname))
    LL.exception('')   

  def save_CommonProfil_state(self):
    """ сохранение словаря таблиц данных (CommonProfil_state) """
    try: 
      fname = self.state_dir1+'/CommonProfil_state.pk'
      if self.CommonProfil_stateD:
        with open(fname, 'wb') as pfile:
          pickle.dump(self.CommonProfil_stateD, pfile)
        LL.I("Сохранение {} выполнено успешно".format(fname)) 
      else:
        LL.I("Словарь CommonProfil_stateD пустой - сохранять в файл нечего")  
    except:
      LL.E("Ошибка при сохранении {}".format(fname))   
      LL.exception('')

  def load_LocalProfil_state(self):
    """ Загрузка и сохранение профилей локальных приборов.
    загрузка словаря таблиц данных """ 
    try:
      fname = self.state_dir1+'/LocalProfil_state.pk'
      if os.path.isfile(fname):
        with open(fname, 'rb') as pfile:
          self.LocalProfil_stateD.update(pickle.load(pfile))
        LL.I("Загрузка {} выполнена успешно".format(fname))
      else:
        LL.I("Отсутствует {} - словарь LocalProfil_stateD пустой".format(fname)) 
    except:
      LL.E("Ошибка при загрузке {}".format(fname))
      LL.exception('')   

  def save_LocalProfil_state(self):
    """ сохранение словаря таблиц данных (LocalProfil_state) """
    try: 
      fname = self.state_dir1+'/LocalProfil_state.pk'
      if self.LocalProfil_stateD:
        with open(fname, 'wb') as pfile:
          pickle.dump(self.LocalProfil_stateD, pfile)
        LL.I("Сохранение {} выполнено успешно".format(fname)) 
      else:
        LL.I("Словарь LocalProfil_stateD пустой - сохранять в файл нечего")  
    except:
      LL.E("Ошибка при сохранении {}".format(fname))   
      LL.exception('')

  def AddDescrToConfig(self,Descr):
      self.CommonProfil_stateD['CurrCFG']['Descr']=Descr

  def GetConfigDescr(self,Name):
      Descr=''
      Descr=self.CommonProfil_stateD['CurrCFG']['Descr']
      return Descr 

  def on_leModbusNumFinished(self):
      a=1

  def on_leIndexMessFinished(self):
      a=1

  def on_leTypeChFinished(self):
      a=1

  def on_leAddrChFinished(self):
      a=1

  def on_lePortNumFinished(self):
      a=1

  def on_leIndexVPriborFinished(self):
      a=1

  def on_leTypeVPriborFinished(self):
      a=1

  def lwCh_Change(self):
      a=1

  def lwVIns_Change(self):
      a=1

  def cbChType_Change(self):
      a=1

  def cbChAddr_Change(self):
      a=1

  def cbTypeVPribor_Change(self):
      a=1

  def cbChVPribor_1_Change(self):
      a=1

  def cbChVPribor_2_Change(self):
      a=1

  def AutoSearch(self):
      """ Автопоиск измерительных модулей """
      self.DirID=1
      self.BaseCopy=384
      self.offs_addr=0
      self.offs_SerNum=52
      self.offs_TypeID=57
      self.offs_Descr=58
      self.addrMB=1
      NumPort=int(self.CommonProfil_stateD['PortNumber'])
      if(self.PortOpened!=1): self.OpenPort_1(NumPort)
      self.PortOpened=1
      tmpAdr=0
      while(tmpAdr<255):
       self.addrMB=tmpAdr
       try:   
         tmp_Par = svimb.ReadRegs16(self.DirID, self.addrMB, self.BaseCopy + self.offs_addr, 1) 
         tmp_addr = svi.ToUns16(tmp_Par[0]) 
         tmp_Par = svimb.ReadRegs16(self.DirID, self.addrMB, self.BaseCopy + self.offs_SerNum, 1)
         tmp_SerNum = svi.ToUns16(tmp_Par[0])
         tmp_Par = svimb.ReadRegs16(self.DirID, self.addrMB, self.BaseCopy + self.offs_TypeID, 1)
         tmp_TypeID = svi.ToUns16(tmp_Par[0])

         i=0
         j=0
         tmpt=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
         tmptxt=''
         try:
           tmpt=svimb.ReadRegs16(self.DirID, self.addrMB, self.BaseCopy + self.offs_Descr+i, 70)
           while(i<70):
            tmptxt=tmptxt+chr( tmpt[i])
            i=i+1
         except: q=0
         tmp_Descr = tmptxt
         k=len(tmp_Descr)
         tmp_namemod=''
         namemod=''
         tmp_namech1=''
         namech1=''
         tmp_namech2=''
         namech2=''
         par2=0
         i=0
         while(i<70):
             if(namemod==''):
                 if(tmp_Descr[i]!=':'):
                     tmp_namemod=tmp_namemod+tmp_Descr[i]
                 else: 
                     namemod=tmp_namemod

             if((namemod!='')&(namech1=='')):
                 if((tmp_Descr[i]!=',')&(tmp_Descr[i]!=';')):
                     if((tmp_Descr[i]!=' ')&(tmp_Descr[i]!=':')):tmp_namech1=tmp_namech1+tmp_Descr[i]
                 else: 
                     namech1=tmp_namech1
                     if (tmp_Descr[i]!=';'):par2=1
             if((namemod!='')&(namech1!='')&(namech2=='')&(par2==1)):
                 if(tmp_Descr[i]!=';'):
                     if((tmp_Descr[i]!=' ')&(tmp_Descr[i]!=',')):tmp_namech2=tmp_namech2+tmp_Descr[i]
                 else: 
                     namech2=tmp_namech2
             i=i+1

         self.ChMessListCounter=self.CommonProfil_stateD['MessChanels']['ChMessListCounter']
         i=0
         k=1
         tmpn=namemod
         while (i<self.ChMessListCounter):
             if(self.CommonProfil_stateD['MessChanels']['ChMessList'][i]==tmpn+str(k)):
                 i=-1
                 k=k+1
             i=i+1
         tmpchn=namemod+str(k)
         self.tmpChName=tmpchn
         self.CurrChName=tmpchn
         tmpmbch=str(tmp_addr)
         self.CommonProfil_stateD['MessChanels']['ChMessList'][self.ChMessListCounter]=tmpchn
         self.CommonProfil_stateD['MessChanels'][tmpchn]={}
         self.CommonProfil_stateD['MessChanels'][tmpchn]['AdrMODBUS']=tmpmbch
         self.CommonProfil_stateD['MessChanels'][tmpchn]['Serial_Number']=tmp_SerNum
         self.CommonProfil_stateD['MessChanels'][tmpchn]['Type_ID']=tmp_TypeID
         self.CommonProfil_stateD['MessChanels'][tmpchn]['ChMessChListCounter']=0
         self.CommonProfil_stateD['MessChanels'][tmpchn]['ChMessChTypeList']={}
         self.CommonProfil_stateD['MessChanels'][tmpchn]['ChMessChAdrList']={}
         tmpmbch=self.winCrChVP.lwCh.addItem(tmpchn+',  MODBUS  '+str(tmp_addr)+',  Зав.номер  '+ str(tmp_SerNum))
         self.ChMessListCounter=self.ChMessListCounter+1
         self.CommonProfil_stateD['MessChanels']['ChMessListCounter']=self.ChMessListCounter

         if(namech1!=''):
           self.ChMessChListCounter=self.CommonProfil_stateD['MessChanels'][self.CurrChName]['ChMessChListCounter']
           self.CommonProfil_stateD['MessChanels'][self.CurrChName]['ChMessChTypeList'][self.ChMessChListCounter]=namech1
           
           if(namech1=='давление'):
               self.CommonProfil_stateD['MessChanels'][self.CurrChName]['ChMessChAdrList'][self.ChMessChListCounter]='0x206' 
               self.winCrChVP.lwChInMess.addItem(namech1+" ,"+'0x206')
           else:
               self.CommonProfil_stateD['MessChanels'][self.CurrChName]['ChMessChAdrList'][self.ChMessChListCounter]='0x204'
               self.winCrChVP.lwChInMess.addItem(namech1+" ,"+'0x204') 

           self.ChMessChListCounter=self.ChMessChListCounter+1
           self.CommonProfil_stateD['MessChanels'][self.CurrChName]['ChMessChListCounter']=self.ChMessChListCounter

         if(namech2!=''):
           self.ChMessChListCounter=self.CommonProfil_stateD['MessChanels'][self.CurrChName]['ChMessChListCounter']
           self.CommonProfil_stateD['MessChanels'][self.CurrChName]['ChMessChTypeList'][self.ChMessChListCounter]=namech2
           self.CommonProfil_stateD['MessChanels'][self.CurrChName]['ChMessChAdrList'][self.ChMessChListCounter]='0x208'
           self.winCrChVP.lwChInMess.addItem(namech2+" ,"+'0x208')
           self.ChMessChListCounter=self.ChMessChListCounter+1
           self.CommonProfil_stateD['MessChanels'][self.CurrChName]['ChMessChListCounter']=self.ChMessChListCounter
         self.save_CommonProfil_state()       
       except:q=0
       tmpAdr=tmpAdr+1
      q=2

  def AllSearch(self):
      """ Автопоиск измерительных модулей_2 """
      self.DirID=1
      self.BaseCopy=384
      self.offs_addr=0
      self.offs_SerNum=52
      self.offs_TypeID=57
      self.offs_Descr=58
      self.addrMB=1
      NumPort=int(self.CommonProfil_stateD['PortNumber'])
      if(self.PortOpened!=1): self.OpenPort_1(NumPort)
      self.PortOpened=1
      tmpAdr=0
      while(tmpAdr<255):
       self.addrMB=tmpAdr
       try:   
         tmp_Par = svimb.ReadRegs16(self.DirID, self.addrMB, self.BaseCopy + self.offs_addr, 1) 
         tmp_addr = svi.ToUns16(tmp_Par[0]) 
         tmp_Par = svimb.ReadRegs16(self.DirID, self.addrMB, self.BaseCopy + self.offs_SerNum, 1)
         tmp_SerNum = svi.ToUns16(tmp_Par[0])
         tmp_Par = svimb.ReadRegs16(self.DirID, self.addrMB, self.BaseCopy + self.offs_TypeID, 1)
         tmp_TypeID = svi.ToUns16(tmp_Par[0])

         i=0
         j=0
         tmpt=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
         tmptxt=''
         try:
          tmpt=svimb.ReadRegs16(self.DirID, self.addrMB, self.BaseCopy + self.offs_Descr+i, 70)
          while(i<70):
            tmptxt=tmptxt+chr( tmpt[i])
            i=i+1
         except: q=0
         tmp_Descr = tmptxt
         k=len(tmp_Descr)
         tmp_namemod=''
         namemod=''
         tmp_namech1=''
         namech1=''
         tmp_namech2=''
         namech2=''
         par2=0
         i=0
         while(i<70):
             if(namemod==''):
                 if(tmp_Descr[i]!=':'):
                     tmp_namemod=tmp_namemod+tmp_Descr[i]
                 else: 
                     namemod=tmp_namemod

             if((namemod!='')&(namech1=='')):
                 if((tmp_Descr[i]!=',')&(tmp_Descr[i]!=';')):
                     if((tmp_Descr[i]!=' ')&(tmp_Descr[i]!=':')):tmp_namech1=tmp_namech1+tmp_Descr[i]
                 else: 
                     namech1=tmp_namech1
                     if (tmp_Descr[i]!=';'):par2=1
             if((namemod!='')&(namech1!='')&(namech2=='')&(par2==1)):
                 if(tmp_Descr[i]!=';'):
                     if((tmp_Descr[i]!=' ')&(tmp_Descr[i]!=',')):tmp_namech2=tmp_namech2+tmp_Descr[i]
                 else: 
                     namech2=tmp_namech2
             i=i+1

         self.ChMessListCounter=self.CommonProfil_stateD['MessChanels']['ChMessListCounter']
         i=0
         k=1
         tmpn=namemod
         while (i<self.ChMessListCounter):
             if(self.CommonProfil_stateD['MessChanels']['ChMessList'][i]==tmpn+str(k)):
                 i=-1
                 k=k+1
             i=i+1
         tmpchn=namemod+str(k)
         self.tmpChName=tmpchn
         self.CurrChName=tmpchn
         tmpmbch=str(tmp_addr)
         self.CommonProfil_stateD['MessChanels']['ChMessList'][self.ChMessListCounter]=tmpchn
         self.CommonProfil_stateD['MessChanels'][tmpchn]={}
         self.CommonProfil_stateD['MessChanels'][tmpchn]['AdrMODBUS']=tmpmbch
         self.CommonProfil_stateD['MessChanels'][tmpchn]['Serial_Number']=tmp_SerNum
         self.CommonProfil_stateD['MessChanels'][tmpchn]['Type_ID']=tmp_TypeID
         self.CommonProfil_stateD['MessChanels'][tmpchn]['ChMessChListCounter']=0
         self.CommonProfil_stateD['MessChanels'][tmpchn]['ChMessChTypeList']={}
         self.CommonProfil_stateD['MessChanels'][tmpchn]['ChMessChAdrList']={}
         tmpmbch=self.winCrChVP.lwCh.addItem(tmpchn+',  MODBUS  '+str(tmp_addr)+',  Зав.номер  '+ str(tmp_SerNum))

         self.ChMessListCounter=self.ChMessListCounter+1
         self.CommonProfil_stateD['MessChanels']['ChMessListCounter']=self.ChMessListCounter
         if(namech1!=''):
           self.ChMessChListCounter=self.CommonProfil_stateD['MessChanels'][self.CurrChName]['ChMessChListCounter']
           self.CommonProfil_stateD['MessChanels'][self.CurrChName]['ChMessChTypeList'][self.ChMessChListCounter]=namech1
           
           if(namech1=='давление'):
               self.CommonProfil_stateD['MessChanels'][self.CurrChName]['ChMessChAdrList'][self.ChMessChListCounter]='0x206' 
           else:
               self.CommonProfil_stateD['MessChanels'][self.CurrChName]['ChMessChAdrList'][self.ChMessChListCounter]='0x204'
           self.ChMessChListCounter=self.ChMessChListCounter+1
           self.CommonProfil_stateD['MessChanels'][self.CurrChName]['ChMessChListCounter']=self.ChMessChListCounter

         if(namech2!=''):

           self.ChMessChListCounter=self.CommonProfil_stateD['MessChanels'][self.CurrChName]['ChMessChListCounter']
           self.CommonProfil_stateD['MessChanels'][self.CurrChName]['ChMessChTypeList'][self.ChMessChListCounter]=namech2
           self.CommonProfil_stateD['MessChanels'][self.CurrChName]['ChMessChAdrList'][self.ChMessChListCounter]='0x208'
           self.ChMessChListCounter=self.ChMessChListCounter+1
           self.CommonProfil_stateD['MessChanels'][self.CurrChName]['ChMessChListCounter']=self.ChMessChListCounter
         self.save_CommonProfil_state()       
       except:q=0
       tmpAdr=tmpAdr+1
      q=2

  def TestConfigsModuls(self):
      """ Тестирование измерительных модулей"""
      self.DirID=1
      self.BaseCopy=384
      self.offs_addr=0
      self.offs_SerNum=52
      self.offs_TypeID=57
      self.offs_Descr=58
      self.addrMB=1
      NumPort=int(self.CommonProfil_stateD['PortNumber'])
      if(self.PortOpened!=1): self.OpenPort_1(NumPort)
      self.PortOpened=1

      self.ChMessListCounter=self.CommonProfil_stateD['MessChanels']['ChMessListCounter']
      tmpi=0
      tmpYes=0
      self.tmpadrtst=0
      while(tmpi<self.ChMessListCounter):
          tmpch=self.CommonProfil_stateD['MessChanels']['ChMessList'][tmpi]
          self.tmpadrtst=self.CommonProfil_stateD['MessChanels'][tmpch]['AdrMODBUS']
          try:
            tmpsn=self.CommonProfil_stateD['MessChanels'][tmpch]['Serial_Number']
          except:
            tmpsn=0  
            self.CommonProfil_stateD['MessChanels'][tmpch]['Serial_Number']=tmpsn
          if(tmpsn!=0):
              try:
                tmp_Par = svimb.ReadRegs16(self.DirID, int(self.tmpadrtst), self.BaseCopy + self.offs_SerNum, 1)
                tmp_SerNum = svi.ToUns16(tmp_Par[0])
                if(tmp_SerNum==tmpsn):
                    tmpYes='+'
                else:
                    tmpYes='*'
              except:  tmpYes='-' 
              
          else: 
              tmpYes='0'
          self.CommonProfil_stateD['MessChanels'][tmpch]['Present']=tmpYes
          tmpi=tmpi+1
      self.save_CommonProfil_state()
      self.InitChList()
      self.InitChInVPModulMess()
      self.TestVPribors()
      self.TestCurrConfigVPribors()
      self.TestAllConfigsVPribors()

  def TestVPribors(self):
      """ Тестирование виртуальных приборов """
      q=1
      self.VirtPriborsListCounter=self.CommonProfil_stateD['VirtPribors']['VirtPriborsListCounter']
      j=0
      #Проверка всех виртуальных приборов
      while (j<=self.VirtPriborsListCounter-1) :
          tmpname=self.CommonProfil_stateD['VirtPribors']['VirtPriborList'][j]
          try:
             tmpVPYes=self.CommonProfil_stateD['VirtPribors'][tmpname]['VPYes']
          except:tmpVPYes=0

          self.ChVPListCounter=self.CommonProfil_stateD['VirtPribors'][tmpname]['VPChListCounter']
          tmpi=0
          tmpYesVPCh='+'
          while(tmpi<self.ChVPListCounter):
             
              tmpchtype=self.CommonProfil_stateD['VirtPribors'][tmpname]['VPChTypeList'][tmpi]
              tmpvpchmname=self.CommonProfil_stateD['VirtPribors'][tmpname]['VPChModulNameList'][tmpi]
              try:
                vpchmsn=self.CommonProfil_stateD['VirtPribors'][tmpname]['VPChModulSerialNumbersList'][tmpi]
              except:vpchmsn=0
              vpchname=self.CommonProfil_stateD['VirtPribors'][tmpname]['VPChNameList'][tmpi]
              try:
                vpchmsnyes=self.CommonProfil_stateD['VirtPribors'][tmpname]['VPChModulNameYesList'][tmpi]
              except:vpchmsnyes=0

              self.ChMessListCounter=self.CommonProfil_stateD['MessChanels']['ChMessListCounter']
              tmpi2=0
              tmpYes=0
              self.tmpadrtst=0
              while(tmpi2<self.ChMessListCounter):
                  tmpch=self.CommonProfil_stateD['MessChanels']['ChMessList'][tmpi2]
                  try:
                    tmpsn=self.CommonProfil_stateD['MessChanels'][tmpch]['Serial_Number']
                  except:
                    tmpsn=0 

                  try:
                    tmpYes=self.CommonProfil_stateD['MessChanels'][tmpch]['Present'] 
                  except: 
                    tmpYes='0'
                     
                          
                  if(tmpsn!=0):
                      #Если номер мизмерительного модкля равен номеру модуля в ВП
                      if(tmpsn==vpchmsn):
                           #Признак работоспособности канала передается в ВП
                           self.CommonProfil_stateD['VirtPribors'][tmpname]['VPChModulNameYesList'][tmpi]=tmpYes
                           if(tmpYes!='+'):tmpYesVPCh='-'
                           if(tmpch!=tmpvpchmname):
                               #Если наименование канала изменилось то в ВП оноизменяется тоже
                               self.CommonProfil_stateD['VirtPribors'][tmpname]['VPChModulNameList'][tmpi2]=tmpch
                              
                  tmpi2=tmpi2+1
              tmpi=tmpi+1
              self.CommonProfil_stateD['VirtPribors'][tmpname]['VPYes']=tmpYesVPCh

          j=j+1
      self.InitVirtPriborList()

  def TestCurrConfigVPribors(self):
      """ Проверка ВП текущей конфигурации """
      tmpYesVPConfig='+'
      tmpYesVPCh='+'
      q=1
      self.VirtPriborsListCounter=self.CommonProfil_stateD['CurrCFG']['CurrCFGVPListCount']
      j=0
      #Проверка всех виртуальных приборов
      while (j<=self.VirtPriborsListCounter-1) :
          tmpname=self.CommonProfil_stateD['CurrCFG']['CurrCFGVPList'][j]
          try:
             tmpVPYes=self.CommonProfil_stateD['CurrCFG'][tmpname]['VPYes']
          except:tmpVPYes=0

          self.ChVPListCounter=self.CommonProfil_stateD['CurrCFG'][tmpname]['VPChListCounter']
          tmpi=0
          tmpYesVPCh='+'
          while(tmpi<self.ChVPListCounter):
             
              tmpchtype=self.CommonProfil_stateD['CurrCFG'][tmpname]['VPChTypeList'][tmpi]
              tmpvpchmname=self.CommonProfil_stateD['CurrCFG'][tmpname]['VPChModulNameList'][tmpi]
              try:
                vpchmsn=self.CommonProfil_stateD['CurrCFG'][tmpname]['VPChModulSerialNumbersList'][tmpi]
              except:vpchmsn=0
              vpchname=self.CommonProfil_stateD['CurrCFG'][tmpname]['VPChNameList'][tmpi]
              try:
                vpchmsnyes=self.CommonProfil_stateD['CurrCFG'][tmpname]['VPChModulNameYesList'][tmpi]
              except:vpchmsnyes=0

              self.ChMessListCounter=self.CommonProfil_stateD['MessChanels']['ChMessListCounter']
              tmpi2=0
              tmpYes=0
              self.tmpadrtst=0
              while(tmpi2<self.ChMessListCounter):
                  tmpch=self.CommonProfil_stateD['MessChanels']['ChMessList'][tmpi2]
                  try:
                    tmpsn=self.CommonProfil_stateD['MessChanels'][tmpch]['Serial_Number']
                  except:
                    tmpsn=0 

                  try:
                    tmpYes=self.CommonProfil_stateD['MessChanels'][tmpch]['Present'] 
                  except: 
                    tmpYes='0'
                     
                          
                  if(tmpsn!=0):
                      #Если номер мизмерительного модкля равен номеру модуля в ВП
                      if(tmpsn==vpchmsn):
                           #Признак работоспособности канала передается в ВП
                           self.CommonProfil_stateD['CurrCFG'][tmpname]['VPChModulNameYesList'][tmpi]=tmpYes
                           if(tmpYes!='+'):tmpYesVPCh='-'
                           if(tmpch!=tmpvpchmname):
                               #Если наименование канала изменилось то в ВП оноизменяется тоже
                               self.CommonProfil_stateD['CurrCFG'][tmpname]['VPChModulNameList'][tmpi2]=tmpch
                              
                  tmpi2=tmpi2+1
              tmpi=tmpi+1
              self.CommonProfil_stateD['CurrCFG'][tmpname]['VPYes']=tmpYesVPCh
          if(tmpYesVPCh!='+'):tmpYesVPConfig='-' 
          j=j+1

      tmps=self.winCrConf.windowTitle()
      self.winCrConf.setWindowTitle(tmps+ '  '+str(tmpYesVPCh))

  def TestAllConfigsVPribors(self):
      """Проверка ВП всех конфигураций """
      self.NumConfigs=self.CommonProfil_stateD['Configs']
      jcfg=0
      #Проверка всех существующих конфигураций приборов
      while (jcfg<self.NumConfigs) :
        cfgname=self.CommonProfil_stateD['CFGList'][jcfg]

        tmpYesVPConfig='+'
        q=1
        self.VirtPriborsListCounter=self.CommonProfil_stateD['CFG'][cfgname]['CurrCFGVPListCount']
        j=0
        #Проверка всех виртуальных приборов
        while (j<=self.VirtPriborsListCounter-1) :
          tmpname=self.CommonProfil_stateD['CFG'][cfgname]['CurrCFGVPList'][j]
          try:
             tmpVPYes=self.CommonProfil_stateD['CFG'][cfgname][tmpname]['VPYes']
          except:tmpVPYes=0

          tmpChVPListCounter=self.CommonProfil_stateD['CFG'][cfgname][tmpname]['VPChListCounter']
          tmpi=0
          tmpYesVPCh='+'
          while(tmpi<tmpChVPListCounter):
             
              tmpchtype=self.CommonProfil_stateD['CFG'][cfgname][tmpname]['VPChTypeList'][tmpi]
              try:
               tmpvpchmname=self.CommonProfil_stateD['CFG'][cfgname][tmpname]['VPChModulNameList'][tmpi]
              except:
               tmpvpchmname=''
              try:
                vpchmsn=self.CommonProfil_stateD['CFG'][cfgname][tmpname]['VPChModulSerialNumbersList'][tmpi]
              except:vpchmsn=0
              vpchname=self.CommonProfil_stateD['CFG'][cfgname][tmpname]['VPChNameList'][tmpi]
              try:
                vpchmsnyes=self.CommonProfil_stateD['CFG'][cfgname][tmpname]['VPChModulNameYesList'][tmpi]
              except:vpchmsnyes=0

              self.ChMessListCounter=self.CommonProfil_stateD['MessChanels']['ChMessListCounter']
              tmpi2=0
              tmpYes=0
              self.tmpadrtst=0
              while(tmpi2<self.ChMessListCounter):
                  tmpch=self.CommonProfil_stateD['MessChanels']['ChMessList'][tmpi2]
                  try:
                    tmpsn=self.CommonProfil_stateD['MessChanels'][tmpch]['Serial_Number']
                  except:
                    tmpsn=0 

                  try:
                    tmpYes=self.CommonProfil_stateD['MessChanels'][tmpch]['Present'] 
                  except: 
                    tmpYes='0'
                                               
                  if(tmpsn!=0):
                      #Если номер мизмерительного модкля равен номеру модуля в ВП
                      if(tmpsn==vpchmsn):
                           #Признак работоспособности канала передается в ВП
                           self.CommonProfil_stateD['CFG'][cfgname][tmpname]['VPChModulNameYesList'][tmpi]=tmpYes
                           if(tmpYes!='+'):tmpYesVPCh='-'
                           if(tmpch!=tmpvpchmname):
                               #Если наименование канала изменилось то в ВП оноизменяется тоже
                               self.CommonProfil_stateD['CFG'][cfgname][tmpname]['VPChModulNameList'][tmpi2]=tmpch
                              
                  tmpi2=tmpi2+1
              tmpi=tmpi+1
              self.CommonProfil_stateD['CFG'][cfgname][tmpname]['VPYes']=tmpYesVPCh
          if(tmpYesVPCh!='+'):tmpYesVPConfig='-' 
          j=j+1
        try:
          self.CommonProfil_stateD['CFG'][cfgname]['VPConfigYes']=tmpYesVPConfig
        except:q=0
        jcfg=jcfg+1
      self.InitConfigList()
      qq=1



  def AddAutoSearch(self):
      """ Автопоиск измерительных модулей -добавление"""
      self.DirID=1
      self.BaseCopy=384
      self.offs_addr=0
      self.offs_SerNum=52
      self.offs_TypeID=57
      self.offs_Descr=58
      self.addrMB=1
      NumPort=int(self.CommonProfil_stateD['PortNumber'])
      NewAddrList={}
      i_NewAddrList=0
      if(self.PortOpened!=1): self.OpenPort_1(int(NumPort))
      self.PortOpened=1
      tmpAdr=0
      i_sn=0
      tmp_adr_free=0
      tmpYes_addr=0
      #проверка адресов
      self.ChMessListCounter=self.CommonProfil_stateD['MessChanels']['ChMessListCounter']
      tmpi3=0
      while(tmpi3<256):
              NewAddrList[int(tmpi3)]=0
              tmpi3=tmpi3+1
      tmpi3=0
      while(tmpi3<self.ChMessListCounter):
              tmpch=self.CommonProfil_stateD['MessChanels']['ChMessList'][tmpi3]
              tmp_adr=self.CommonProfil_stateD['MessChanels'][tmpch]['AdrMODBUS']
              NewAddrList[int(tmp_adr)]=1
              tmpi3=tmpi3+1
      while(i_sn<1000):
        res = 0
        try:
          res = svi.ToUns16(svimb.WriteReg16(self.DirID, 0, 0, i_sn))
        except: q=0 
        if((res==i_sn)&(i_sn!=0)):
            #найден модуль
            #проверка: есть ли такой модуль
            self.ChMessListCounter=self.CommonProfil_stateD['MessChanels']['ChMessListCounter']
            tmpi=0
            tmpYes=0
            
            #проверка: есть ли модуль с данным серийником в списке
            while(tmpi<self.ChMessListCounter):
              tmpch=self.CommonProfil_stateD['MessChanels']['ChMessList'][tmpi]
              tmp_sn=self.CommonProfil_stateD['MessChanels'][tmpch]['Serial_Number']
              if(tmp_sn==i_sn):tmpYes=1
              tmpi=tmpi+1
            #если нет в списке то поиск свободного адреса
            if(tmpYes==0):
                  tmpi3=1
                  while(tmpi3<256):
                        if(NewAddrList[tmpi3]==0):
                            tmp_adr_free=tmpi3
                            tmpi3=256
                        tmpi3=tmpi3+1
                  #программирование нового адреса   
                  try:
                    NewAddrList[int(tmp_adr_free)]=2
                    svimb.WriteReg16(self.DirID, 0, tmp_adr_free, i_sn)

                  except:svi.time.sleep(2)
                  #окончание цикла

        i_sn=i_sn+1        
      q=2
      tmpi2=1
      while(tmpi2<256):
            #добавление в список 
            tmpi2=tmpi2+1
            if(NewAddrList[tmpi2-1]==2):
                  self.addrMB=tmpi2-1
                  
                  try:   
                    tmp_Par = svimb.ReadRegs16(self.DirID, self.addrMB, self.BaseCopy + self.offs_addr, 1) 
                    tmp_addr = svi.ToUns16(tmp_Par[0]) 
                    tmp_Par = svimb.ReadRegs16(self.DirID, self.addrMB, self.BaseCopy + self.offs_SerNum, 1)
                    tmp_SerNum = svi.ToUns16(tmp_Par[0])
                    tmp_Par = svimb.ReadRegs16(self.DirID, self.addrMB, self.BaseCopy + self.offs_TypeID, 1)
                    tmp_TypeID = svi.ToUns16(tmp_Par[0])

                    i=0
                    j=0
                    tmpt=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
                    tmptxt=''
                    try:
 
                      while(i<70):
                       j=svimb.ReadRegs16(self.DirID, self.addrMB, self.BaseCopy + self.offs_Descr+i, 1)
                       tmpt[i]=j[0]
                       tmptxt=tmptxt+chr( tmpt[i])
                       i=i+1
                    except: q=0
                    tmp_Descr = tmptxt
                    k=len(tmp_Descr)
                    tmp_namemod=''
                    namemod=''
                    tmp_namech1=''
                    namech1=''
                    tmp_namech2=''
                    namech2=''
                    par2=0
                    i=0
                    while(i<70):
                        if(namemod==''):
                            if(tmp_Descr[i]!=':'):
                                tmp_namemod=tmp_namemod+tmp_Descr[i]
                            else: 
                                namemod=tmp_namemod

                        if((namemod!='')&(namech1=='')):
                            if((tmp_Descr[i]!=',')&(tmp_Descr[i]!=';')):
                                if((tmp_Descr[i]!=' ')&(tmp_Descr[i]!=':')):tmp_namech1=tmp_namech1+tmp_Descr[i]
                            else: 
                                namech1=tmp_namech1
                                if (tmp_Descr[i]!=';'):par2=1
                        if((namemod!='')&(namech1!='')&(namech2=='')&(par2==1)):
                            if(tmp_Descr[i]!=';'):
                                if((tmp_Descr[i]!=' ')&(tmp_Descr[i]!=',')):tmp_namech2=tmp_namech2+tmp_Descr[i]
                            else: 
                                namech2=tmp_namech2
                        i=i+1

                    self.ChMessListCounter=self.CommonProfil_stateD['MessChanels']['ChMessListCounter']
                    i=0
                    k=1
                    tmpn=namemod
                    while (i<self.ChMessListCounter):
                        if(self.CommonProfil_stateD['MessChanels']['ChMessList'][i]==tmpn+str(k)):
                            i=-1
                            k=k+1
                        i=i+1
                    tmpchn=namemod+str(k)
                    self.tmpChName=tmpchn
                    self.CurrChName=tmpchn
                    tmpmbch=str(tmp_addr)
                    self.CommonProfil_stateD['MessChanels']['ChMessList'][self.ChMessListCounter]=tmpchn
                    self.CommonProfil_stateD['MessChanels'][tmpchn]={}
                    self.CommonProfil_stateD['MessChanels'][tmpchn]['AdrMODBUS']=tmpmbch
                    self.CommonProfil_stateD['MessChanels'][tmpchn]['Serial_Number']=tmp_SerNum
                    self.CommonProfil_stateD['MessChanels'][tmpchn]['Type_ID']=tmp_TypeID
                    self.CommonProfil_stateD['MessChanels'][tmpchn]['ChMessChListCounter']=0
                    self.CommonProfil_stateD['MessChanels'][tmpchn]['ChMessChTypeList']={}
                    self.CommonProfil_stateD['MessChanels'][tmpchn]['ChMessChAdrList']={}
                    self.CommonProfil_stateD['MessChanels'][tmpchn]['Present']='+'
                    self.ChMessListCounter=self.ChMessListCounter+1
                    self.CommonProfil_stateD['MessChanels']['ChMessListCounter']=self.ChMessListCounter
                    #self.save_CommonProfil_state()

                    if(namech1!=''):
                      self.ChMessChListCounter=self.CommonProfil_stateD['MessChanels'][self.CurrChName]['ChMessChListCounter']
                      self.CommonProfil_stateD['MessChanels'][self.CurrChName]['ChMessChTypeList'][self.ChMessChListCounter]=namech1
           
                      if(namech1=='давление'):
                          self.CommonProfil_stateD['MessChanels'][self.CurrChName]['ChMessChAdrList'][self.ChMessChListCounter]='0x206' 
                          self.winCrChVP.lwChInMess.addItem(namech1+" ,"+'0x206')
                      else:
                          self.CommonProfil_stateD['MessChanels'][self.CurrChName]['ChMessChAdrList'][self.ChMessChListCounter]='0x204'
                          self.winCrChVP.lwChInMess.addItem(namech1+" ,"+'0x204') 

                      self.ChMessChListCounter=self.ChMessChListCounter+1
                      self.CommonProfil_stateD['MessChanels'][self.CurrChName]['ChMessChListCounter']=self.ChMessChListCounter
 
                    if(namech2!=''):

                      self.ChMessChListCounter=self.CommonProfil_stateD['MessChanels'][self.CurrChName]['ChMessChListCounter']
                      self.CommonProfil_stateD['MessChanels'][self.CurrChName]['ChMessChTypeList'][self.ChMessChListCounter]=namech2
                      self.CommonProfil_stateD['MessChanels'][self.CurrChName]['ChMessChAdrList'][self.ChMessChListCounter]='0x208'
                      self.ChMessChListCounter=self.ChMessChListCounter+1
                      self.CommonProfil_stateD['MessChanels'][self.CurrChName]['ChMessChListCounter']=self.ChMessChListCounter

                    self.save_CommonProfil_state()
                    
       
                  except:q=0
                  self.InitChList()
                  self.InitChInVPModulMess()
                  #конец добавления в список

  def AddCh(self):
    """ Добавление канала измерительного модуля в лист """
    self.ChMessListCounter=self.CommonProfil_stateD['MessChanels']['ChMessListCounter']
    tmpchn=self.winCrChVP.leIndexMess.text()
    self.tmpChName=tmpchn
    self.CurrChName=tmpchn
    #if(self.ChMessListCounter>0): self.CurrChIndex=self.CommonProfil_stateD['MessChanels']['ChMessList'][self.ChMessListCounter]
    #else: self.CurrChIndex=-1
    tmpmbch=self.winCrChVP.leModbusNum.text()
    self.CommonProfil_stateD['MessChanels']['ChMessList'][self.ChMessListCounter]=tmpchn
    self.CommonProfil_stateD['MessChanels'][tmpchn]={}
    self.CommonProfil_stateD['MessChanels'][tmpchn]['AdrMODBUS']=tmpmbch
    self.CommonProfil_stateD['MessChanels'][tmpchn]['ChMessChListCounter']=0
    self.CommonProfil_stateD['MessChanels'][tmpchn]['ChMessChTypeList']={}
    self.CommonProfil_stateD['MessChanels'][tmpchn]['ChMessChAdrList']={}
    tmpmbch=self.winCrChVP.lwCh.addItem(tmpchn)
    self.ChMessListCounter=self.ChMessListCounter+1
    self.CommonProfil_stateD['MessChanels']['ChMessListCounter']=self.ChMessListCounter
    self.save_CommonProfil_state()

  def DelCh(self):
      """ удаление канала измерительного модуля из листа """
      self.ChMessListCounter=self.CommonProfil_stateD['MessChanels']['ChMessListCounter']
      self.tmpChMess=self.winCrChVP.lwCh.currentRow()
      self.tmpChMessName=self.CommonProfil_stateD['MessChanels']['ChMessList'][self.tmpChMess]
      while(self.tmpChMess<self.ChMessListCounter-1):
        self.CommonProfil_stateD['MessChanels']['ChMessList'][self.tmpChMess]=self.CommonProfil_stateD['MessChanels']['ChMessList'][self.tmpChMess+1]
        self.tmpChMess=self.tmpChMess+1
      del(self.CommonProfil_stateD['MessChanels']['ChMessList'][self.ChMessListCounter-1])
      del(self.CommonProfil_stateD['MessChanels'][self.tmpChMessName])
      self.ChMessListCounter=self.ChMessListCounter-1
      self.CommonProfil_stateD['MessChanels']['ChMessListCounter']=self.ChMessListCounter
      self.save_CommonProfil_state()
      self.InitChList()

  def ChangeCh(self):
    """ Изменение канала измерительного модуля в листе """
    tmpchn=self.winCrChVP.leIndexMess.text()
    tmpchangech=self.winCrChVP.lwCh.currentRow()
    self.CurrChName=self.CommonProfil_stateD['MessChanels']['ChMessList'][tmpchangech]
    self.tmpChName=tmpchn
    if(self.CurrChName!=self.tmpChName):
        self.CommonProfil_stateD['MessChanels']['ChMessList'][tmpchangech]=tmpchn
        tmpDict=self.CommonProfil_stateD['MessChanels'][self.CurrChName].copy()
        del(self.CommonProfil_stateD['MessChanels'][self.CurrChName])
        self.CommonProfil_stateD['MessChanels'][self.tmpChName]={}
        self.CommonProfil_stateD['MessChanels'][self.tmpChName]=tmpDict.copy()
        self.CurrChName=self.tmpChName
    self.save_CommonProfil_state()
    self.InitChList()

  def InitTypeMess(self):
      a=1

  def InitChList(self):
      """ Инициализация листа измерительных модулей """
      self.ChMessListCounter=self.CommonProfil_stateD['MessChanels']['ChMessListCounter']
      tmpi=0
      tmp_SerNum=0
      tmp_TypeID=0
      tmpmbch=0
      tmpYes=' '
      self.winCrChVP.lwCh.clear()
      while(tmpi<self.ChMessListCounter):
          tmpchn=self.CommonProfil_stateD['MessChanels']['ChMessList'][tmpi]
          try:   
            tmp_addr=self.CommonProfil_stateD['MessChanels'][tmpchn]['AdrMODBUS']        
            tmp_SerNum=self.CommonProfil_stateD['MessChanels'][tmpchn]['Serial_Number']
            try:
              tmp_TypeID=self.CommonProfil_stateD['MessChanels'][tmpchn]['Type_ID']
            except:q=0
            try:
              tmpYes=self.CommonProfil_stateD['MessChanels'][tmpchn]['Present']
            except:tmpYes='_'
          except:q=0
          self.winCrChVP.lwCh.addItem(str(tmpYes)+'  '+str(tmpchn)+',  MODBUS  '+str(tmp_addr)+',  Зав.номер  '+ str(tmp_SerNum))
          tmpi=tmpi+1
      self.InitChInVPModulMess()

  def InitPortNum(self):
      """ выгрузка номера порта """
      tmpN=self.CommonProfil_stateD['PortNumber']
      self.winCrChVP.lePortNum.setText(tmpN)
    
  def AddChName(self):
      """ Добавить имя измерительного канала """
      self.ChMessTypesListCounter=self.CommonProfil_stateD['MessChanels']['ChMessTypesListCounter']
      ChType=self.winCrChVPParam.leTypeCh.text()
      self.CommonProfil_stateD['MessChanels']['ChMessTypesList'][self.ChMessTypesListCounter]=ChType
      self.ChMessTypesListCounter=self.ChMessTypesListCounter+1
      self.CommonProfil_stateD['MessChanels']['ChMessTypesListCounter']=self.ChMessTypesListCounter
      self.save_CommonProfil_state()
      self.InitChTypeList()

  def DelChName(self):
      """ Удалить имя измерительного канала """
      self.ChMessTypesListCounter=self.CommonProfil_stateD['MessChanels']['ChMessTypesListCounter']
      ChType=self.winCrChVPParam.cbChType.currentIndex()
      tmpi=ChType
      while(tmpi<self.ChMessTypesListCounter-1):
        self.CommonProfil_stateD['MessChanels']['ChMessTypesList'][tmpi]=self.CommonProfil_stateD['MessChanels']['ChMessTypesList'][tmpi+1]
        tmpi=tmpi+1
      del(self.CommonProfil_stateD['MessChanels']['ChMessTypesList'][self.ChMessTypesListCounter-1])
      self.ChMessTypesListCounter=self.ChMessTypesListCounter-1
      self.CommonProfil_stateD['MessChanels']['ChMessTypesListCounter']=self.ChMessTypesListCounter
      self.save_CommonProfil_state()
      self.InitChTypeList()

  def ChangeChName(self):
      """ Изменить имя измерительного канала """
      self.ChMessTypesListCounter=self.CommonProfil_stateD['MessChanels']['ChMessTypesListCounter']
      ChType=self.winCrChVPParam.cbChType.currentIndex()
      newChType=self.winCrChVPParam.leTypeCh.text()
      self.CommonProfil_stateD['MessChanels']['ChMessTypesList'][ChType]=newChType
      self.save_CommonProfil_state()
      self.InitChTypeList()

  def InitChTypeList(self):
      """ Инициализация списка типов измерительных каналов """
      self.ChMessTypesListCounter=self.CommonProfil_stateD['MessChanels']['ChMessTypesListCounter']
      tmpi=0
      self.winCrChVPParam.cbChType.clear()
      self.winCrChVP.cbChInVPChannel.clear()
      while(tmpi<self.ChMessTypesListCounter):
          self.winCrChVPParam.cbChType.addItem(self.CommonProfil_stateD['MessChanels']['ChMessTypesList'][tmpi])
          self.winCrChVP.cbChInVPChannel.addItem(self.CommonProfil_stateD['MessChanels']['ChMessTypesList'][tmpi])
          tmpi=tmpi+1
      if(self.winCrChVPParam.cbChType.currentIndex()<0): self.winCrChVPParam.cbChType.setCurrentIndex(0)
      try:
       self.winCrChVPParam.leTypeCh.setText(self.CommonProfil_stateD['MessChanels']['ChMessTypesList'][self.winCrChVPParam.cbChType.currentIndex()])
       self.winCrChVPParam.leTypeCh.clearFocus() 
      except:
           q=0

  def SavePortNum(self):
      """ Сохранение номера порта """
      tmpN=self.winCrChVP.lePortNum.text()
      self.CommonProfil_stateD['PortNumber']=tmpN
      self.save_CommonProfil_state()

  def AddChAddr(self):
      """ Добавление адреса измерительного канала  """
      self.ChMessAddrListCounter=self.CommonProfil_stateD['MessChanels']['ChMessAddrListCounter']
      ChAddr=self.winCrChVPParam.leAddrCh.text()
      self.CommonProfil_stateD['MessChanels']['ChMessAddrList'][self.ChMessAddrListCounter]=ChAddr
      self.ChMessAddrListCounter=self.ChMessAddrListCounter+1
      self.CommonProfil_stateD['MessChanels']['ChMessAddrListCounter']=self.ChMessAddrListCounter
      self.save_CommonProfil_state()
      self.InitChAddrList()

  def DelChAddr(self):
      """ Удаление адреса измерительного канала """
      self.ChMessAddrListCounter=self.CommonProfil_stateD['MessChanels']['ChMessAddrListCounter']
      ChAddr=self.winCrChVPParam.cbChAddr.currentIndex()
      tmpi=ChAddr
      while(tmpi<self.ChMessAddrListCounter-1):
        self.CommonProfil_stateD['MessChanels']['ChMessAddrList'][tmpi]=self.CommonProfil_stateD['MessChanels']['ChMessAddrList'][tmpi+1]
        tmpi=tmpi+1
      del(self.CommonProfil_stateD['MessChanels']['ChMessAddrList'][self.ChMessAddrListCounter-1])
      self.ChMessAddrListCounter=self.ChMessAddrListCounter-1
      self.CommonProfil_stateD['MessChanels']['ChMessAddrListCounter']=self.ChMessAddrListCounter
      self.save_CommonProfil_state()
      self.InitChAddrList()

  def ChangeChAddr(self):
      """ Изменение адреса измерительного канала """
      self.ChMessAddrListCounter=self.CommonProfil_stateD['MessChanels']['ChMessAddrListCounter']
      ChAddr=self.winCrChVPParam.cbChAddr.currentIndex()
      newChName=self.winCrChVPParam.leAddrCh.text()
      self.CommonProfil_stateD['MessChanels']['ChMessAddrList'][ChAddr]=newChName
      self.save_CommonProfil_state()
      self.InitChAddrList()

  def InitChAddrList(self):
      """ Инициализация списка адресов измерительных каналов """
      self.ChMessAddrListCounter=self.CommonProfil_stateD['MessChanels']['ChMessAddrListCounter']
      tmpi=0
      self.winCrChVPParam.cbChAddr.clear()
      while(tmpi<self.ChMessAddrListCounter):
          self.winCrChVPParam.cbChAddr.addItem(self.CommonProfil_stateD['MessChanels']['ChMessAddrList'][tmpi])
          tmpi=tmpi+1
      self.winCrChVPParam.leAddrCh.setText(self.CommonProfil_stateD['MessChanels']['ChMessAddrList'][self.winCrChVPParam.cbChAddr.currentIndex()])
      self.winCrChVPParam.leAddrCh.clearFocus() 

  def AddVPribor(self):
    """ Создание нового виртуального прибора  """
    self.VirtPriborsListCounter=self.CommonProfil_stateD['VirtPribors']['VirtPriborsListCounter']
    tmpVPName=self.winCrChVP.leIndexVPribor.text()
    tmpVPParam=self.winCrChVP.leParamVPribor.text()
    tmpVPIndex=self.CommonProfil_stateD['VirtPribors']['VirtPriborsListCounter']
    tmpVPType=self.CommonProfil_stateD['VPriborsTypesList'][self.winCrChVP.cbTypeVPribor.currentIndex()]
    self.CommonProfil_stateD['VirtPribors']['VirtPriborList'][self.VirtPriborsListCounter]=tmpVPName
    self.CommonProfil_stateD['VirtPribors'][tmpVPName]={}
    self.CommonProfil_stateD['VirtPribors'][tmpVPName]['VPType']=tmpVPType
    self.CommonProfil_stateD['VirtPribors'][tmpVPName]['VPYes']=0
    self.CommonProfil_stateD['VirtPribors'][tmpVPName]['VPParam']=tmpVPParam
    self.CommonProfil_stateD['VirtPribors'][tmpVPName]['VPChListCounter']=0
    self.CommonProfil_stateD['VirtPribors'][tmpVPName]['VPChTypeList']={}
    self.CommonProfil_stateD['VirtPribors'][tmpVPName]['VPChModulNameList']={}
    self.CommonProfil_stateD['VirtPribors'][tmpVPName]['VPChModulNameYesList']={}
    self.CommonProfil_stateD['VirtPribors'][tmpVPName]['VPChModulSerialNumbersList']={}
    self.CommonProfil_stateD['VirtPribors'][tmpVPName]['VPChNameList']={}
    self.CommonProfil_stateD['VirtPribors'][tmpVPName]['VPChOutListCounter']=0
    self.CommonProfil_stateD['VirtPribors'][tmpVPName]['VPChOutTypeList']={}
    self.CommonProfil_stateD['VirtPribors'][tmpVPName]['VPChOutNameList']={}
    self.winCrChVP.lwVIns.addItem(tmpVPName)
    self.VirtPriborsListCounter=self.VirtPriborsListCounter+1
    self.CommonProfil_stateD['VirtPribors']['VirtPriborsListCounter']=self.VirtPriborsListCounter
    self.CurrVPName=tmpVPName
    self.CurrVPIndex=tmpVPIndex
    self.CurrVPType=tmpVPType
    self.save_CommonProfil_state()
    self.InitVirtPriborList()

  def DelVPribor(self):
      """Удаление виртуального прибора"""
      self.VirtPriborsListCounter=self.CommonProfil_stateD['VirtPribors']['VirtPriborsListCounter']
      self.tmpVPlst=self.winCrChVP.lwVIns.currentRow()
      self.tmpVPName=self.CommonProfil_stateD['VirtPribors']['VirtPriborList'][self.tmpVPlst]
      while(self.tmpVPlst<self.VirtPriborsListCounter-1):
        self.CommonProfil_stateD['VirtPribors']['VirtPriborList'][self.tmpVPlst]=self.CommonProfil_stateD['VirtPribors']['VirtPriborList'][self.tmpVPlst+1]
        self.tmpVPlst=self.tmpVPlst+1
      del(self.CommonProfil_stateD['VirtPribors']['VirtPriborList'][self.VirtPriborsListCounter-1])
      del(self.CommonProfil_stateD['VirtPribors'][self.tmpVPName])
      self.VirtPriborsListCounter=self.VirtPriborsListCounter-1
      self.CommonProfil_stateD['VirtPribors']['VirtPriborsListCounter']=self.VirtPriborsListCounter
      self.save_CommonProfil_state()
      self.InitVirtPriborList()

  def ChangeVPribor(self):
    """ Изменение виртуального прибора"""
    tmpVPlst=self.winCrChVP.lwVIns.currentRow()
    tmpVPType_New=self.CommonProfil_stateD['VPriborsTypesList'][self.winCrChVP.cbTypeVPribor.currentIndex()]
    tmpVPName_New=self.winCrChVP.leIndexVPribor.text()
    tmpVPParam_New=self.winCrChVP.leParamVPribor.text()
    tmpVPName=self.CommonProfil_stateD['VirtPribors']['VirtPriborList'][tmpVPlst]
    tmpVPType=self.CommonProfil_stateD['VirtPribors'][tmpVPName]['VPType']
    self.CommonProfil_stateD['VirtPribors'][tmpVPName].setdefault('VPParam',0)
    tmpVPParam=self.CommonProfil_stateD['VirtPribors'][tmpVPName]['VPParam']
    if(tmpVPType_New!=tmpVPType): self.CommonProfil_stateD['VirtPribors'][tmpVPName]['VPType']=tmpVPType_New
    if(tmpVPParam_New!=tmpVPParam): self.CommonProfil_stateD['VirtPribors'][tmpVPName]['VPParam']=tmpVPParam_New
    tmpDict={}
    if(tmpVPName!=tmpVPName_New):
        self.CommonProfil_stateD['VirtPribors']['VirtPriborList'][tmpVPlst]=tmpVPName_New
        tmpDict=self.CommonProfil_stateD['VirtPribors'][tmpVPName].copy()
        del(self.CommonProfil_stateD['VirtPribors'][tmpVPName])
        self.CommonProfil_stateD['VirtPribors'][tmpVPName_New]={}
        self.CommonProfil_stateD['VirtPribors'][tmpVPName_New]=tmpDict.copy()
        self.CurrVPName=tmpVPName_New
    self.save_CommonProfil_state()
    self.InitVirtPriborList()

  def AddVPType(self):
      """ Добавить тип ВП """
      self.VPriborsTypesListCounter=self.CommonProfil_stateD['VPriborsTypesListCounter']
      VPType=self.winCrChVPParam.leTypeVPribor.text()
      self.CommonProfil_stateD['VPriborsTypesList'][self.VPriborsTypesListCounter]=VPType
      self.VPriborsTypesListCounter=self.VPriborsTypesListCounter+1
      self.CommonProfil_stateD['VPriborsTypesListCounter']=self.VPriborsTypesListCounter
      self.save_CommonProfil_state()
      self.InitVPTypeList()

  def DelVPType(self):
      """ Удалить тип ВП """
      self.VPriborsTypesListCounter=self.CommonProfil_stateD['VPriborsTypesListCounter']
      VPType=self.winCrChVPParam.cbTypeVPribor.currentIndex()
      tmpi=VPType
      while(tmpi<self.VPriborsTypesListCounter-1):
        self.CommonProfil_stateD['VPriborsTypesList'][tmpi]=self.CommonProfil_stateD['VPriborsTypesList'][tmpi+1]
        tmpi=tmpi+1
      del(self.CommonProfil_stateD['VPriborsTypesList'][self.VPriborsTypesListCounter-1])
      self.VPriborsTypesListCounter=self.VPriborsTypesListCounter-1
      self.CommonProfil_stateD['VPriborsTypesListCounter']=self.VPriborsTypesListCounter
      self.save_CommonProfil_state()
      self.InitVPTypeList()

  def ChangeVPType(self):
      """ Изменить тип ВП """
      self.VPriborsTypesListCounter=self.CommonProfil_stateD['VPriborsTypesListCounter']
      VPType=self.winCrChVPParam.cbTypeVPribor.currentIndex()
      newVPType=self.winCrChVPParam.leTypeVPribor.text()
      self.CommonProfil_stateD['VPriborsTypesList'][VPType]=newVPType
      self.save_CommonProfil_state()
      self.InitVPTypeList()

  def InitVPTypeList(self):
      """ Инициализация списка типов ВП """
      self.VPriborsTypesListCounter=self.CommonProfil_stateD['VPriborsTypesListCounter']
      tmpi=0
      self.winCrChVPParam.cbTypeVPribor.clear()
      self.winCrChVP.cbTypeVPribor.clear()
      while(tmpi<self.VPriborsTypesListCounter):
          self.winCrChVP.cbTypeVPribor.addItem(self.CommonProfil_stateD['VPriborsTypesList'][tmpi])
          self.winCrChVPParam.cbTypeVPribor.addItem(self.CommonProfil_stateD['VPriborsTypesList'][tmpi])
          tmpi=tmpi+1
      if(self.winCrChVP.cbTypeVPribor.currentIndex()<0): self.winCrChVP.cbTypeVPribor.setCurrentIndex(0)
      if(self.winCrChVPParam.cbTypeVPribor.currentIndex()<0): self.winCrChVPParam.cbTypeVPribor.setCurrentIndex(0)
      try:
       self.winCrChVPParam.leTypeVPribor.setText(self.CommonProfil_stateD['VPriborsTypesList'][self.winCrChVPParam.cbTypeVPribor.currentIndex()])
       self.winCrChVPParam.leTypeVPribor.clearFocus() 
      except:
       q=0

  def InitChInVPModulMess(self):
      """ Инициализация списка измерительных модулей """
      self.ChMessListCounter=self.CommonProfil_stateD['MessChanels']['ChMessListCounter']
      tmpi=0
      self.winCrChVP.cbChInVPModul.clear()
      while(tmpi<self.ChMessListCounter):
          tmpchn=self.CommonProfil_stateD['MessChanels']['ChMessList'][tmpi]
          try:
             tmpsn=self.CommonProfil_stateD['MessChanels'][tmpchn]['Serial_Number']
          except: tmpsn=0
          try:
             tmpYes=self.CommonProfil_stateD['MessChanels'][tmpchn]['Present']
          except: tmpYes=0
          self.winCrChVP.cbChInVPModul.addItem(str(tmpYes)+'  '+str(tmpchn)+', '+str(tmpsn))
          tmpi=tmpi+1



  def InitChInVPChannelMess(self):
      """ Инициализация списка каналов измерительных модулей """
      self.ChMessListChCounter=self.CommonProfil_stateD['MessChanels'][self.CurCreatingVPMessChannelName]['ChMessChListCounter']
      tmpi=0
      self.winCrChVP.cbChInVPChannel.clear()
      while(tmpi<self.ChMessListChCounter):
          tmpn=self.CommonProfil_stateD['MessChanels'][self.CurCreatingVPMessChannelName]['ChMessChTypeList'][tmpi]
          tmpadr=self.CommonProfil_stateD['MessChanels'][self.CurCreatingVPMessChannelName]['ChMessChAdrList'][tmpi]
          self.winCrChVP.cbChInVPChannel.addItem(tmpn+" ,"+tmpadr)
          tmpi=tmpi+1

  def AddChTempl(self):
    """ Добавление шаблона канала """
    self.ChMessListTemplCounter=self.CommonProfil_stateD['MessChanelsTempl']['ChMessTemplListCounter']
    tmpchn=self.winCrChVPParam.leTypeMess.text()
    self.tmpChTemplName=tmpchn
    self.CurrChTemplName=tmpchn
    tmpmbch='0'
    self.CommonProfil_stateD['MessChanelsTempl']['ChMessTemplList'][self.ChMessListTemplCounter]=tmpchn
    self.CommonProfil_stateD['MessChanelsTempl'][tmpchn]={}
    self.CommonProfil_stateD['MessChanelsTempl'][tmpchn]['AdrMODBUS']=tmpmbch
    self.CommonProfil_stateD['MessChanelsTempl'][tmpchn]['MessType']=tmpchn
    self.CommonProfil_stateD['MessChanelsTempl'][tmpchn]['ChMessChListCounter']=0
    self.CommonProfil_stateD['MessChanelsTempl'][tmpchn]['ChMessChTypeList']={}
    self.CommonProfil_stateD['MessChanelsTempl'][tmpchn]['ChMessChAdrList']={}
    tmpmbch=self.winCrChVPParam.lwChTempl.addItem(tmpchn)
    self.ChMessListTemplCounter=self.ChMessListTemplCounter+1
    self.CommonProfil_stateD['MessChanelsTempl']['ChMessListTemplCounter']=self.ChMessListTemplCounter
    self.save_CommonProfil_state()

  def ChangeChTempl(self):
    """ Изменение шаблона канала """
    tmpchn=self.winCrChVPParam.leTypeMess.text()
    tmpchangech=self.winCrChVPParam.lwChTempl.currentRow()
    self.CurrChTemplName=self.CommonProfil_stateD['MessChanelsTempl']['ChMessTemplList'][tmpchangech]
    self.tmpChTemplName=tmpchn
    tmpDict={}    
    if(self.CurrChTemplName!=self.tmpChTemplName):
        self.CommonProfil_stateD['MessChanelsTempl']['ChMessList'][tmpchangech]=tmpchn
        tmpDict=self.CommonProfil_stateD['MessChanelsTempl'][self.CurrChTemplName].copy()
        del(self.CommonProfil_stateD['MessChanelsTempl'][self.CurrChTemplName])
        self.CommonProfil_stateD['MessChanelsTempl'][self.tmpChTemplName]={}
        self.CommonProfil_stateD['MessChanelsTempl'][self.tmpChTemplName]=tmpDict.copy()
        self.CurrChTemplName=self.tmpChTemplName
    self.save_CommonProfil_state()
    self.InitTypeMess()

  def DelChTempl(self):
      """ Удаление шаблона канала """
      self.ChMessListTemplCounter=self.CommonProfil_stateD['MessChanelsTempl']['ChMessTemplListCounter']
      self.tmpChMessTempl=self.winCrChVP.lwCh.currentRow()
      self.tmpChMessNameTempl=self.CommonProfil_stateD['MessChanelsTempl']['ChMessTemplList'][self.tmpChMessTempl]
      while(self.tmpChMessTempl<self.ChMessListTemplCounter-1):
        self.CommonProfil_stateD['MessChanelsTempl']['ChMessTemplList'][self.tmpChMesTempls]=self.CommonProfil_stateD['MessChanelsTempl']['ChMessTemplList'][self.tmpChMesTempls+1]
        self.tmpChMessTempl=self.tmpChMessTempl+1
      del(self.CommonProfil_stateD['MessChanelsTempl']['ChMessTemplList'][self.ChMessListTemplCounter-1])
      del(self.CommonProfil_stateD['MessChanelsTempl'][self.tmpChMessNamTemple])
      self.ChMessListTemplCounter=self.ChMessListTemplCounter-1
      self.CommonProfil_stateD['MessChanelsTempl']['ChMessListCounter']=self.ChMessListTemplCounter
      self.save_CommonProfil_state()
      self.InitTypeMess()

  def AddChInMessTempl(self):
     """ Добавление канала в шаблон измерителя """
     i=self.winCrChVPParam.cbChTypeTempl.currentIndex()
     j=self.winCrChVPParam.cbChAddrTempl.currentIndex()
     self.ChMessChListCounter=self.CommonProfil_stateD['MessChanelsTempl'][self.CurrChName]['ChMessChListCounter']
     self.CommonProfil_stateD['MessChanelsTempl'][self.CurrChName]['ChMessChTypeList'][self.ChMessChListCounter]=self.CommonProfil_stateD['MessChanels']['ChMessTypesList'][i]
     self.CommonProfil_stateD['MessChanelsTempl'][self.CurrChName]['ChMessChAdrList'][self.ChMessChListCounter]=self.CommonProfil_stateD['MessChanels']['ChMessAddrList'][j]
     self.winCrChVPParam.lwChInMessTempl.addItem(self.CommonProfil_stateD['MessChanelsTempl'][self.CurrChName]['ChMessChTypeList'][self.ChMessChListCounter]+" ,"+self.CommonProfil_stateD['MessChanels'][self.CurrChName]['ChMessChAdrList'][self.ChMessChListCounter])
     self.ChMessChListCounter=self.ChMessChListCounter+1
     self.CommonProfil_stateD['MessChanelsTempl'][self.CurrChName]['ChMessChListCounter']=self.ChMessChListCounter
     self.save_CommonProfil_state()

  def ChangeChInMessTempl(self):
    """ Изменение канала в шаблоне измерителя """
    tmpchangech=self.winCrChVPParam.lwChInMessTempl.currentRow()
    i=self.winCrChVP.winCrChVPParam.currentIndex()
    j=self.winCrChVP.winCrChVPParam.currentIndex()
    self.CommonProfil_stateD['MessChanelsTempl'][self.CurrChName]['ChMessChTypeList'][tmpchangech]=self.CommonProfil_stateD['MessChanels']['ChMessTypesList'][i]
    self.CommonProfil_stateD['MessChanelsTempl'][self.CurrChName]['ChMessChAdrList'][tmpchangech]=self.CommonProfil_stateD['MessChanels']['ChMessAddrList'][j]
    self.save_CommonProfil_state()
    self.InitChListChTempl()

  def DelChInMessTempl(self):
      """ Удаление канала из шаблона измерителя """
      self.ChMessChListCounter=self.CommonProfil_stateD['MessChanelsTempl'][self.CurrChName]['ChMessChListCounter']
      self.tmpChMessCh=self.winCrChVP.winCrChVPParam.currentRow()
      while(self.tmpChMessCh<self.ChMessChListCounter-1):
        self.CommonProfil_stateD['MessChanelsTempl'][self.CurrChName]['ChMessChTypeList'][self.tmpChMessCh]=self.CommonProfil_stateD['MessChanels'][self.CurrChName]['ChMessChTypeList'][self.tmpChMessCh+1]
        self.CommonProfil_stateD['MessChanelsTempl'][self.CurrChName]['ChMessChAdrList'][self.tmpChMessCh]=self.CommonProfil_stateD['MessChanels'][self.CurrChName]['ChMessChAdrList'][self.tmpChMessCh+1]
        self.tmpChMessCh=self.tmpChMessCh+1
      del(self.CommonProfil_stateD['MessChanelsTempl'][self.CurrChName]['ChMessChTypeList'][self.ChMessChListCounter-1])
      del(self.CommonProfil_stateD['MessChanelsTempl'][self.CurrChName]['ChMessChAdrList'][self.ChMessChListCounter-1])
      self.ChMessChListCounter=self.ChMessChListCounter-1
      self.CommonProfil_stateD['MessChanelsTempl'][self.CurrChName]['ChMessChListCounter']=self.ChMessChListCounter
      self.save_CommonProfil_state()
      self.InitChListChTempl()

  def InitChListChTempl(self):
      """ Инициализация листа шаблона каналов """
      self.ChMessListChTemplCounter=self.CommonProfil_stateD['MessChanelsTempl'][self.CurrChName]['ChMessChListCounter']
      tmpi=0
      self.winCrChVPParam.lwChInMessTempl.clear()
      while(tmpi<self.ChMessListChCounter):
          self.winCrChVPParam.lwChInMessTempl.addItem(self.CommonProfil_stateD['MessChanelsTempl'][self.CurrChName]['ChMessChTypeList'][tmpi]+" ,"+self.CommonProfil_stateD['MessChanelsTempl'][self.CurrChName]['ChMessChAdrList'][tmpi])
          tmpi=tmpi+1

  def AddChInMess(self):
     """ Добавление канала в измеритель """
     i=self.winCrChVP.cbChType.currentIndex()
     j=self.winCrChVP.cbChAddr.currentIndex()
     self.ChMessChListCounter=self.CommonProfil_stateD['MessChanels'][self.CurrChName]['ChMessChListCounter']
     self.CommonProfil_stateD['MessChanels'][self.CurrChName]['ChMessChTypeList'][self.ChMessChListCounter]=self.CommonProfil_stateD['MessChanels']['ChMessTypesList'][i]
     self.CommonProfil_stateD['MessChanels'][self.CurrChName]['ChMessChAdrList'][self.ChMessChListCounter]=self.CommonProfil_stateD['MessChanels']['ChMessAddrList'][j]
     self.winCrChVP.lwChInMess.addItem(self.CommonProfil_stateD['MessChanels'][self.CurrChName]['ChMessChTypeList'][self.ChMessChListCounter]+" ,"+self.CommonProfil_stateD['MessChanels'][self.CurrChName]['ChMessChAdrList'][self.ChMessChListCounter])
     self.ChMessChListCounter=self.ChMessChListCounter+1
     self.CommonProfil_stateD['MessChanels'][self.CurrChName]['ChMessChListCounter']=self.ChMessChListCounter
     self.save_CommonProfil_state()

  def ChangeChInMess(self):
    """ Изменение канала в измерителе """
    tmpchangech=self.winCrChVP.lwChInMess.currentRow()
    i=self.winCrChVP.cbChType.currentIndex()
    j=self.winCrChVP.cbChAddr.currentIndex()
    self.CommonProfil_stateD['MessChanels'][self.CurrChName]['ChMessChTypeList'][tmpchangech]=self.CommonProfil_stateD['MessChanels']['ChMessTypesList'][i]
    self.CommonProfil_stateD['MessChanels'][self.CurrChName]['ChMessChAdrList'][tmpchangech]=self.CommonProfil_stateD['MessChanels']['ChMessAddrList'][j]
    self.save_CommonProfil_state()
    self.InitChListCh()

  def DelChInMess(self):
      """ Удаление канала из измерителя """
      self.ChMessChListCounter=self.CommonProfil_stateD['MessChanels'][self.CurrChName]['ChMessChListCounter']
      self.tmpChMessCh=self.winCrChVP.lwChInMess.currentRow()
      while(self.tmpChMessCh<self.ChMessChListCounter-1):
        self.CommonProfil_stateD['MessChanels'][self.CurrChName]['ChMessChTypeList'][self.tmpChMessCh]=self.CommonProfil_stateD['MessChanels'][self.CurrChName]['ChMessChTypeList'][self.tmpChMessCh+1]
        self.CommonProfil_stateD['MessChanels'][self.CurrChName]['ChMessChAdrList'][self.tmpChMessCh]=self.CommonProfil_stateD['MessChanels'][self.CurrChName]['ChMessChAdrList'][self.tmpChMessCh+1]
        self.tmpChMessCh=self.tmpChMessCh+1
      del(self.CommonProfil_stateD['MessChanels'][self.CurrChName]['ChMessChTypeList'][self.ChMessChListCounter-1])
      del(self.CommonProfil_stateD['MessChanels'][self.CurrChName]['ChMessChAdrList'][self.ChMessChListCounter-1])
      self.ChMessChListCounter=self.ChMessChListCounter-1
      self.CommonProfil_stateD['MessChanels'][self.CurrChName]['ChMessChListCounter']=self.ChMessChListCounter
      self.save_CommonProfil_state()
      self.InitChListCh()

  def InitChListCh(self):
      """ Инициализация листа каналов в измерительном модуле """
      self.ChMessListChCounter=self.CommonProfil_stateD['MessChanels'][self.CurrChName]['ChMessChListCounter']
      tmpi=0
      self.winCrChVP.lwChInMess.clear()
      while(tmpi<self.ChMessListChCounter):
          self.winCrChVP.lwChInMess.addItem(self.CommonProfil_stateD['MessChanels'][self.CurrChName]['ChMessChTypeList'][tmpi]+" ,"+self.CommonProfil_stateD['MessChanels'][self.CurrChName]['ChMessChAdrList'][tmpi])
          tmpi=tmpi+1

  def AddChInVP(self):
     """ Добавить канал в ВП """
     i=self.winCrChVP.cbChInVPType.currentIndex()
     j=self.winCrChVP.cbChInVPModul.currentIndex()
     k=self.winCrChVP.cbChInVPChannel.currentIndex()
     self.ChVPListCounter=self.CommonProfil_stateD['VirtPribors'][self.CurrVPName]['VPChListCounter']
     self.CommonProfil_stateD['VirtPribors'][self.CurrVPName]['VPChTypeList'][self.ChVPListCounter]=self.CommonProfil_stateD['VPriborsTypesChList'][i]
     
     
     tmpPar=self.CommonProfil_stateD['VirtPribors'][self.CurrVPName]['VPParam']
     if(tmpPar=='0'):
       tmpModulName=self.CommonProfil_stateD['MessChanels']['ChMessList'][j]
       self.CommonProfil_stateD['VirtPribors'][self.CurrVPName]['VPChModulNameList'][self.ChVPListCounter]=self.CommonProfil_stateD['MessChanels']['ChMessList'][j]
       self.CommonProfil_stateD['VirtPribors'][self.CurrVPName]['VPChModulSerialNumbersList'][self.ChVPListCounter]=self.CommonProfil_stateD['MessChanels'][tmpModulName]['Serial_Number']     
       self.CommonProfil_stateD['VirtPribors'][self.CurrVPName]['VPChModulNameYesList'][self.ChVPListCounter]=self.CommonProfil_stateD['MessChanels'][tmpModulName]['Present']
       self.CommonProfil_stateD['VirtPribors'][self.CurrVPName]['VPChNameList'][self.ChVPListCounter]=self.CommonProfil_stateD['MessChanels'][tmpModulName]['ChMessChTypeList'][k]
     if(tmpPar=='1'):
       tmpModulName='0'
       self.CommonProfil_stateD['VirtPribors'][self.CurrVPName]['VPChModulNameList'][self.ChVPListCounter]='0'
       self.CommonProfil_stateD['VirtPribors'][self.CurrVPName]['VPChModulSerialNumbersList'][self.ChVPListCounter]='0'    
       self.CommonProfil_stateD['VirtPribors'][self.CurrVPName]['VPChModulNameYesList'][self.ChVPListCounter]='0' 
       self.CommonProfil_stateD['VirtPribors'][self.CurrVPName]['VPChNameList'][self.ChVPListCounter]='0' 
     self.winCrChVP.lwChInVP.addItem(self.CommonProfil_stateD['VirtPribors'][self.CurrVPName]['VPChTypeList'][self.ChVPListCounter]+" ,"+tmpModulName +" ,"+self.CommonProfil_stateD['VirtPribors'][self.CurrVPName]['VPChNameList'][self.ChVPListCounter])
     self.ChVPListCounter=self.ChVPListCounter+1
     self.CommonProfil_stateD['VirtPribors'][self.CurrVPName]['VPChListCounter']=self.ChVPListCounter
     self.save_CommonProfil_state()

  def ChangeChInVP(self):
    """ Изменить канал в ВП """
    tmpchangech=self.winCrChVP.lwChInVP.currentRow()
    i=self.winCrChVP.cbChInVPType.currentIndex()
    j=self.winCrChVP.cbChInVPModul.currentIndex()
    k=self.winCrChVP.cbChInVPChannel.currentIndex()
    tmpModulName=self.CommonProfil_stateD['MessChanels']['ChMessList'][j]
    self.CommonProfil_stateD['VirtPribors'][self.CurrVPName]['VPChTypeList'][tmpchangech]=self.CommonProfil_stateD['VPriborsTypesChList'][i]
    self.CommonProfil_stateD['VirtPribors'][self.CurrVPName]['VPChNameList'][tmpchangech]=self.CommonProfil_stateD['MessChanels'][tmpModulName]['ChMessChTypeList'][k]
    self.CommonProfil_stateD['VirtPribors'][self.CurrVPName]['VPChModulNameList'][tmpchangech]=self.CommonProfil_stateD['MessChanels']['ChMessList'][j]
    try:
      self.CommonProfil_stateD['VirtPribors'][self.CurrVPName]['VPChModulSerialNumbersList'][tmpchangech]=self.CommonProfil_stateD['MessChanels'][tmpModulName]['Serial_Number']    
    except: q=0
    self.save_CommonProfil_state()
    self.InitVPChList()

  def DelChInVP(self):
      """ Удалить канал из ВП """
      self.ChVPListCounter=self.CommonProfil_stateD['VirtPribors'][self.CurrVPName]['VPChListCounter']
      self.tmpChVP=self.winCrChVP.lwChInVP.currentRow()
      while(self.tmpChVP<self.ChVPListCounter-1):
        self.CommonProfil_stateD['VirtPribors'][self.CurrVPName]['VPChTypeList'][self.tmpChVP]=self.CommonProfil_stateD['VirtPribors'][self.CurrVPName]['VPChTypeList'][self.tmpChVP+1]
        self.CommonProfil_stateD['VirtPribors'][self.CurrVPName]['VPChNameList'][self.tmpChVP]=self.CommonProfil_stateD['VirtPribors'][self.CurrVPName]['VPChNameList'][self.tmpChVP+1]
        self.CommonProfil_stateD['VirtPribors'][self.CurrVPName]['VPChModulNameList'][self.tmpChVP]=self.CommonProfil_stateD['VirtPribors'][self.CurrVPName]['VPChModulNameList'][self.tmpChVP+1]
        try:
           self.CommonProfil_stateD['VirtPribors'][self.CurrVPName]['VPChModulSerialNumbersList'][self.tmpChVP]=self.CommonProfil_stateD['VirtPribors'][self.CurrVPName]['VPChModulSerialNumbersList'][self.tmpChVP+1]
           self.CommonProfil_stateD['VirtPribors'][self.CurrVPName]['VPChModulPresentList'][self.tmpChVP]=self.CommonProfil_stateD['VirtPribors'][self.CurrVPName]['VPChModulPresentList'][self.tmpChVP+1]
        except: q=0
        self.tmpChVP=self.tmpChVP+1
      del(self.CommonProfil_stateD['VirtPribors'][self.CurrVPName]['VPChTypeList'][self.ChVPListCounter-1])
      del(self.CommonProfil_stateD['VirtPribors'][self.CurrVPName]['VPChNameList'][self.ChVPListCounter-1])
      del(self.CommonProfil_stateD['VirtPribors'][self.CurrVPName]['VPChModulNameList'][self.ChVPListCounter-1])
      try:
        del(self.CommonProfil_stateD['VirtPribors'][self.CurrVPName]['VPChModulSerialNumbersList'][self.ChVPListCounter-1])
        del(self.CommonProfil_stateD['VirtPribors'][self.CurrVPName]['VPChModulPresentList'][self.ChVPListCounter-1])
      except: q=0
      self.ChVPListCounter=self.ChVPListCounter-1
      self.CommonProfil_stateD['VirtPribors'][self.CurrVPName]['VPChListCounter']=self.ChVPListCounter
      self.save_CommonProfil_state()
      self.InitVPChList()

  def InitVPChList(self):
      """ Инициализация листа входных каналов ВП """
      self.ChVPListCounter=self.CommonProfil_stateD['VirtPribors'][self.CurrVPName]['VPChListCounter']
      tmpi=0
      self.winCrChVP.lwChInVP.clear()
      while(tmpi<self.ChVPListCounter):
          tmpchtype=self.CommonProfil_stateD['VirtPribors'][self.CurrVPName]['VPChTypeList'][tmpi]
          tmpvpchmname=self.CommonProfil_stateD['VirtPribors'][self.CurrVPName]['VPChModulNameList'][tmpi]
          try:
            vpchmsn=self.CommonProfil_stateD['VirtPribors'][self.CurrVPName]['VPChModulSerialNumbersList'][tmpi]
          except:vpchmsn=0
          vpchname=self.CommonProfil_stateD['VirtPribors'][self.CurrVPName]['VPChNameList'][tmpi]

          try:
            tmpsn=self.CommonProfil_stateD['VirtPribors'][self.CurrVPName]['Serial_Number']
          except:tmpsn=0
          try:
            tmpYes=self.CommonProfil_stateD['VirtPribors'][self.CurrVPName]['VPChModulNameYesList'][tmpi]
          except:tmpYes=0
          self.winCrChVP.lwChInVP.addItem(str(tmpYes)+'  '+str(tmpchtype)+', '+str(tmpvpchmname)+" ,"+str(vpchmsn)+" ,"+str(vpchname))
          tmpi=tmpi+1

  def InitVPChListInConfig(self):
      """ Инициализация листа выходных каналов ВП """
      tmpName=self.CurrVPAddToConfigName
      #self.ChVPListCounter=self.CommonProfil_stateD['VirtPribors'][tmpName]['VPChOutListCounter']
      self.ChVPListCounter=self.CommonProfil_stateD['CurrCFG'][tmpName]['VPChOutListCounter']
      tmpi=0
      self.winCrConf.cb_Ch_2.clear()
      while(tmpi<self.ChVPListCounter):
          #self.winCrConf.cb_Ch_2.addItem(self.CommonProfil_stateD['VirtPribors'][tmpName]['VPChOutTypeList'][tmpi])
          self.winCrConf.cb_Ch_2.addItem(self.CommonProfil_stateD['CurrCFG'][tmpName]['VPChOutTypeList'][tmpi])

          tmpi=tmpi+1



################################VP Ch OUT#######################################################
  def AddChOutVP(self):
     """ Добавить выходной канал ВП """
     i=self.winCrChVP.cbChOutVPType.currentIndex()
     self.ChVPOutListCounter=self.CommonProfil_stateD['VirtPribors'][self.CurrVPName]['VPChOutListCounter']
     self.CommonProfil_stateD['VirtPribors'][self.CurrVPName]['VPChOutTypeList'][self.ChVPOutListCounter]=self.CommonProfil_stateD['VPriborsTypesChList'][i]
     self.winCrChVP.lwChOutVP.addItem(self.CommonProfil_stateD['VirtPribors'][self.CurrVPName]['VPChOutTypeList'][self.ChVPOutListCounter])
     self.ChVPOutListCounter=self.ChVPOutListCounter+1
     self.CommonProfil_stateD['VirtPribors'][self.CurrVPName]['VPChOutListCounter']=self.ChVPOutListCounter
     self.save_CommonProfil_state()

  def ChangeChOutVP(self):
    """ Изменить выходной канал ВП """
    tmpchangech=self.winCrChVP.lwChOutVP.currentRow()
    i=self.winCrChVP.cbChOutVPType.currentIndex()
    self.CommonProfil_stateD['VirtPribors'][self.CurrVPName]['VPChOutTypeList'][tmpchangech]=self.CommonProfil_stateD['VPriborsTypesChList'][i]
    self.save_CommonProfil_state()
    self.InitVPChOutList()

  def DelChOutVP(self):
      """ Удалить выходной канал ВП """
      self.ChVPOutListCounter=self.CommonProfil_stateD['VirtPribors'][self.CurrVPName]['VPChOutListCounter']
      self.tmpChOutVP=self.winCrChVP.lwChOutVP.currentRow()
      while(self.tmpChOutVP<self.ChVPOutListCounter-1):
        self.CommonProfil_stateD['VirtPribors'][self.CurrVPName]['VPChOutTypeList'][self.tmpChOutVP]=self.CommonProfil_stateD['VirtPribors'][self.CurrVPName]['VPChOutTypeList'][self.tmpChOutVP+1]
        self.tmpChOutVP=self.tmpChOutVP+1
      del(self.CommonProfil_stateD['VirtPribors'][self.CurrVPName]['VPChOutTypeList'][self.ChVPOutListCounter-1])
      self.ChVPOutListCounter=self.ChVPOutListCounter-1
      self.CommonProfil_stateD['VirtPribors'][self.CurrVPName]['VPChOutListCounter']=self.ChVPOutListCounter
      self.save_CommonProfil_state()
      self.InitVPChOutList()

  def InitVPChOutList(self):
      """ Инициализация списка выходных каналов ВП """
      try:
       self.ChVPOutListCounter=self.CommonProfil_stateD['VirtPribors'][self.CurrVPName]['VPChOutListCounter']
      except: self.ChVPOutListCounter=0
      tmpi=0
      self.winCrChVP.lwChOutVP.clear()
      while(tmpi<self.ChVPOutListCounter):
          self.winCrChVP.lwChOutVP.addItem(self.CommonProfil_stateD['VirtPribors'][self.CurrVPName]['VPChOutTypeList'][tmpi])
          tmpi=tmpi+1

  def Reset_ConfVPIn(self):
    """ Сброс соединений входных каналов ВП текущей конфигурации"""
    tmpchangech=self.winCrConf.lwConfVPIn.currentRow()
    self.CommonProfil_stateD['CurrCFG'][self.CurrVPCurrCfgName]['VPChModulNameList'][tmpchangech]='0'
    self.CommonProfil_stateD['CurrCFG'][self.CurrVPCurrCfgName]['VPChNameList'][tmpchangech]='0'
    self.save_CommonProfil_state()
    self.ConfVPInList()

  def Reset_ChInVP(self):
    """ Сброс соединений входных каналов ВП"""
    tmpchangech=self.winCrChVP.lwChInVP.currentRow()
    self.CommonProfil_stateD['VirtPribors'][self.CurrVPName]['VPChNameList'][tmpchangech]='0'
    self.CommonProfil_stateD['VirtPribors'][self.CurrVPName]['VPChModulNameList'][tmpchangech]='0'
    self.save_CommonProfil_state()
    self.InitVPChList()

  def InitVPChInOutList(self):
      """ Инициализация списка выходных каналов ВП"""
      i=self.winCrConf.lwVP.currentRow()
      if(i>=0):
        tmpNewVPName=self.CommonProfil_stateD['VirtPribors']['VirtPriborList'][i]
        try:
         self.ChVPOutListCounter=self.CommonProfil_stateD['VirtPribors'][tmpNewVPName]['VPChOutListCounter']
        except:self.ChVPOutListCounter=0
        tmpi=0
        self.winCrConf.lwVPOut.clear()
        while(tmpi<self.ChVPOutListCounter):
          self.winCrConf.lwVPOut.addItem(self.CommonProfil_stateD['VirtPribors'][tmpNewVPName]['VPChOutTypeList'][tmpi])
          tmpi=tmpi+1
        self.ChVPListCounter=self.CommonProfil_stateD['VirtPribors'][tmpNewVPName]['VPChListCounter']
        tmpi=0
        self.winCrConf.lwVPIn.clear()
        while(tmpi<self.ChVPListCounter):
          try:
             tmpYes=self.CommonProfil_stateD['VirtPribors'][tmpNewVPName]['VPChModulNameYesList'][tmpi]
          except: tmpYes=0
          self.winCrConf.lwVPIn.addItem(str(tmpYes)+' '+self.CommonProfil_stateD['VirtPribors'][tmpNewVPName]['VPChTypeList'][tmpi]+" ,"+self.CommonProfil_stateD['VirtPribors'][tmpNewVPName]['VPChModulNameList'][tmpi]+" ,"+self.CommonProfil_stateD['VirtPribors'][tmpNewVPName]['VPChNameList'][tmpi])
          tmpi=tmpi+1

  def AddTypeVPCh(self):
      """ Добавление типа канала ВП в список возможных"""
      self.VPriborsTypesChListCounter=self.CommonProfil_stateD['VPriborsTypesChListCounter']
      VPChType=self.winCrChVPParam.leTypeVPCh.text()
      self.CommonProfil_stateD['VPriborsTypesChList'][self.VPriborsTypesChListCounter]=VPChType
      self.VPriborsTypesChListCounter=self.VPriborsTypesChListCounter+1
      self.CommonProfil_stateD['VPriborsTypesChListCounter']=self.VPriborsTypesChListCounter
      self.save_CommonProfil_state()
      self.InitVPChTypeList()

  def DelTypeVPCh(self):
      """ Удаление типа канала ВП из списка возможных"""
      self.VPriborsTypesChListCounter=self.CommonProfil_stateD['VPriborsTypesChListCounter']
      VPChType=self.winCrChVPParam.cbChInVPType.currentIndex()
      tmpi=VPChType
      while(tmpi<self.VPriborsTypesChListCounter-1):
        self.CommonProfil_stateD['VPriborsTypesChList'][tmpi]=self.CommonProfil_stateD['VPriborsTypesChList'][tmpi+1]
        tmpi=tmpi+1
      del(self.CommonProfil_stateD['VPriborsTypesChList'][self.VPriborsTypesChListCounter-1])
      self.VPriborsTypesChListCounter=self.VPriborsTypesChListCounter-1
      self.CommonProfil_stateD['VPriborsTypesChListCounter']=self.VPriborsTypesChListCounter
      self.save_CommonProfil_state()
      self.InitVPChTypeList()

  def ChangeTypeVPCh(self):
      """ Изменение названия типа канала ВП в списке возможных типов"""
      self.VPriborsTypesChListCounter=self.CommonProfil_stateD['VPriborsTypesChListCounter']
      VPChType=self.winCrChVPParam.cbChInVPType.currentIndex()
      newVPChType=self.winCrChVPParam.leTypeVPCh.text()
      self.CommonProfil_stateD['VPriborsTypesChList'][VPChType]=newVPChType
      self.save_CommonProfil_state()
      self.InitVPChTypeList()

  def InitVPChTypeList(self):
      """ Инициализация списка типов каналов ВП """
      self.VPriborsTypesChListCounter=self.CommonProfil_stateD['VPriborsTypesChListCounter']
      tmpi=0
      self.winCrChVP.cbChInVPType.clear()
      self.winCrChVPParam.cbChInVPType.clear()
      self.winCrChVP.cbChOutVPType.clear()
      while(tmpi<self.VPriborsTypesChListCounter):
          self.winCrChVPParam.cbChInVPType.addItem(self.CommonProfil_stateD['VPriborsTypesChList'][tmpi])
          self.winCrChVP.cbChOutVPType.addItem(self.CommonProfil_stateD['VPriborsTypesChList'][tmpi])
          self.winCrChVP.cbChInVPType.addItem(self.CommonProfil_stateD['VPriborsTypesChList'][tmpi])
          tmpi=tmpi+1
      if(self.winCrChVPParam.cbChInVPType.currentIndex()<0): self.winCrChVPParam.cbChInVPType.setCurrentIndex(0)
      if(self.winCrChVP.cbChInVPType.currentIndex()<0): self.winCrChVP.cbChInVPType.setCurrentIndex(0)
      try:
       self.winCrChVPParam.leTypeVPCh.setText(self.CommonProfil_stateD['VPriborsTypesChList'][self.winCrChVPParam.cbChInVPType.currentIndex()])
       self.winCrChVPParam.leTypeVPCh.clearFocus() 
      except:
       q=0

  def SaveAllVPSetting(self):
      a=1

  def ConvertCFG(self):
      """ Перобразование конфигурации """
      self.CommonProfil_stateD['ConvCFG']={}
      self.CommonProfil_stateD['ConvCFG']['MODBUS RTU']={}
      self.CommonProfil_stateD['ConvCFG']['MODBUS RTU']['Измеритель']={}
      self.CommonProfil_stateD['ConvCFG']['MODBUS RTU']['порт']=self.CommonProfil_stateD['PortNumber']
      tmpi=self.CommonProfil_stateD['MessChanels']['ChMessListCounter']
      i=0
      while(i<tmpi):
          self.CommonProfil_stateD['ConvCFG']['MODBUS RTU']['Измеритель'][i]={}
          tmpiname=self.CommonProfil_stateD['MessChanels']['ChMessList'][i]
          self.CommonProfil_stateD['ConvCFG']['MODBUS RTU']['Измеритель'][i]['адрес']=self.CommonProfil_stateD['MessChanels'][tmpiname]['AdrMODBUS']

          tmpj=self.CommonProfil_stateD['MessChanels'][tmpiname]['ChMessChListCounter']
          j=0
          while(j<tmpj):
              self.CommonProfil_stateD['ConvCFG']['MODBUS RTU']['Измеритель'][i]['канал']={}
              tmpport=self.CommonProfil_stateD['MessChanels'][tmpiname]['ChMessChTypeList'][j]
              tmpportadr = self.CommonProfil_stateD['MessChanels'][tmpiname]['ChMessChAdrList'][j]
              self.CommonProfil_stateD['ConvCFG']['MODBUS RTU']['Измеритель'][i]['канал'][j]={}
              self.CommonProfil_stateD['ConvCFG']['MODBUS RTU']['Измеритель'][i]['канал'][j][0]=tmpport
              self.CommonProfil_stateD['ConvCFG']['MODBUS RTU']['Измеритель'][i]['канал'][j][1]=tmpportadr
              j=j+1
          #while(j<tmpj)
          i=i+1
      #while(i<tmpi)

      self.CommonProfil_stateD['ConvCFG']['Виртуальные приборы']={}
      tmpk=self.CommonProfil_stateD['CurrCFG']['CurrCFGVPListCount']
      k=0      
      VPNT={}
      VPNT[0,0]=1
      VPNT[0,1]=2
      vptypecounter=0
      while(k<tmpk):
          tmpVPname=self.CommonProfil_stateD['CurrCFG']['CurrCFGVPList'][k]
          tmptype=self.CommonProfil_stateD['CurrCFG'][tmpVPname]['VPType']

          tmpres=self.CommonProfil_stateD['ConvCFG']['Виртуальные приборы'].get(tmptype)
          if(tmpres==None):
              k1=0
              self.CommonProfil_stateD['ConvCFG']['Виртуальные приборы'][tmptype]={}
              self.CommonProfil_stateD['ConvCFG']['Виртуальные приборы'][tmptype][0]={}
              self.CommonProfil_stateD['ConvCFG']['Виртуальные приборы'][tmptype][0]['наименование']=tmpVPname
          if(tmpres!=None):
            k1=1
            resk1=0
            while(resk1!=None):
                resk1=self.CommonProfil_stateD['ConvCFG']['Виртуальные приборы'][tmptype].get(k1)
                k1=k1+1
                #VPNT[k,0]=tmpres
            self.CommonProfil_stateD['ConvCFG']['Виртуальные приборы'][tmptype][k1-1]={}
            self.CommonProfil_stateD['ConvCFG']['Виртуальные приборы'][tmptype][k1-1]['наименование']=tmpVPname
          k2=0
          tmpk2=self.CommonProfil_stateD['CurrCFG'][tmpVPname]['VPChListCounter']
          while(k2<tmpk2):
               tmpvpchname=self.CommonProfil_stateD['CurrCFG'][tmpVPname]['VPChNameList'][k2]
               tmpvpchtype=self.CommonProfil_stateD['CurrCFG'][tmpVPname]['VPChTypeList'][k2]
               if(k1==0): self.CommonProfil_stateD['ConvCFG']['Виртуальные приборы'][tmptype][k1][tmpvpchtype]=tmpvpchname
               else: self.CommonProfil_stateD['ConvCFG']['Виртуальные приборы'][tmptype][k1-1][tmpvpchtype]=tmpvpchname
               k2=k2+1
          k=k+1
      ttt=0

  def ConvertCFG_1(self):
      """ Перобразование конфигурации 1 """
      self.CommonProfil_stateD['ConvCFG']={}
      self.CommonProfil_stateD['ConvCFG']['MODBUS RTU']=[]      
      tmpd={}
      tmpd['порт']=self.CommonProfil_stateD['PortNumber']
      tmpd['Измеритель']=[]
      tmpdct1={}
      tmpdct2={}
      tmpi=self.CommonProfil_stateD['MessChanels']['ChMessListCounter']
      i=0
      while(i<tmpi):
          tmpiname=self.CommonProfil_stateD['MessChanels']['ChMessList'][i]
          tmpdct1['адрес']=self.CommonProfil_stateD['MessChanels'][tmpiname]['AdrMODBUS']

          tmpj=self.CommonProfil_stateD['MessChanels'][tmpiname]['ChMessChListCounter']
          j=0
          tmpdct1['канал']=[]
          while(j<tmpj):
              tmpport=tmpiname+self.CommonProfil_stateD['MessChanels'][tmpiname]['ChMessChTypeList'][j]#####
              tmpportadr = self.CommonProfil_stateD['MessChanels'][tmpiname]['ChMessChAdrList'][j]
              tmpdct3={}
              tmpdct3[0]=tmpport
              tmpdct3[1]=tmpportadr
              tmpdct1['канал'].append(tmpdct3.copy())
              j=j+1
          #while(j<tmpj)
          
          tmpd['Измеритель'].append(tmpdct1.copy())          
          i=i+1
      #while(i<tmpi)
      self.CommonProfil_stateD['ConvCFG']['MODBUS RTU'].append(tmpd.copy())
      self.CommonProfil_stateD['ConvCFG']['Виртуальные приборы']={}
      tmpdVP={}
      tmpk=self.CommonProfil_stateD['CurrCFG']['CurrCFGVPListCount']
      k=0
      
      VPNT={}
      VPNT[0,0]=1
      VPNT[0,1]=2

      vptypecounter=0
      while(k<tmpk):
          tmpVPname=self.CommonProfil_stateD['CurrCFG']['CurrCFGVPList'][k]
          tmptype=self.CommonProfil_stateD['CurrCFG'][tmpVPname]['VPType']

          tmpres=tmpdVP.get(tmptype)
          if(tmpres==None):
              k1=0
              tmpdVP[tmptype]=[]
              tmpdctVP={}
              tmpdctVP['наименование']=tmpVPname
          if(tmpres!=None):
            k1=1
            resk1=0
            while(resk1!=None):
                resk1=tmpdctVP.get(k1)
                k1=k1+1
                #VPNT[k,0]=tmpres
            tmpdctVP={}
            tmpdctVP['наименование']=tmpVPname
          k2=0
          tmpk2=self.CommonProfil_stateD['CurrCFG'][tmpVPname]['VPChListCounter']
          while(k2<tmpk2):
               tmpvpchname=self.CommonProfil_stateD['CurrCFG'][tmpVPname]['VPChModulNameList'][k2]+self.CommonProfil_stateD['CurrCFG'][tmpVPname]['VPChNameList'][k2]
               tmpvpchtype=self.CommonProfil_stateD['CurrCFG'][tmpVPname]['VPChTypeList'][k2]
               if(k1==0): tmpdctVP[tmpvpchtype]=tmpvpchname
               else: tmpdctVP[tmpvpchtype]=tmpvpchname
               k2=k2+1
          tmpdVP[tmptype].append(tmpdctVP)
          self.CommonProfil_stateD['ConvCFG']['Виртуальные приборы'].update(tmpdVP.copy())
          k=k+1
      ttt=0

  def StartCFG(self):
     """ Запуск конфигурации """
     global fTech     # флаг технологического режима      
     global chanD     # словарь дескрипторов измерительных каналов
     global vstateD   # словарь сохраняемых состояний виртуальных приборов 
     global Cfg       # конфигурация
     from svi import vinstrD
     aa=0
     a=self.winSelectConfig.lwConf.currentRow()
     self.Cfg1['MODBUS RTU']={}
     self.Cfg1['Виртуальные приборы']={}
     self.Cfg1['MODBUS RTU']=copy.deepcopy(self.CommonProfil_stateD['ConvCFG']['MODBUS RTU'])
     self.Cfg1['Виртуальные приборы']=copy.deepcopy(self.CommonProfil_stateD['ConvCFG']['Виртуальные приборы'])
     self.SVIstart_3(self.CommonProfil_stateD,self.fTech1,self.Cfg1,self.chanD1,self.vinstrD1,self.LocalProfil_stateD)
     tmpk=self.CommonProfil_stateD['CurrCFG']['CurrCFGVPListCount']
     k=0 
     while(k<tmpk):
         tmpVPname=self.CommonProfil_stateD['CurrCFG']['CurrCFGVPList'][k]
         self.vinstrD1[tmpVPname]['obj'].ShowFP()
         k=k+1

  def SVIstart_3(self,cfg2,fTech1,Cfg1,chanD1,vinstrD1,cfgLocalProfil):
    """ подготовка и запуск системы виртуальных приборов 
      (вызывать ПОСЛЕ создания  QtGui.QApplication) """

    global vstateD   # словарь сохраняемых состояний виртуальных приборов  
    DirID=1
    if(self.ChannelsInit==0):
      for dirC in Cfg1["MODBUS RTU"]:
          a=1
      #--- запуск активных направлений
      for dirC in Cfg1["MODBUS RTU"]:
        #tmpD = renameDK(dirC, {"скорость":"Speed", "четность":"Parity", "таймаут":"Timeout", "пауза":"ReqPause"})
        if(self.PortOpened!=1):   
          self.DirID = svimb.CreateRTUdir(int(dirC["порт"]), 38400, 0, 100, 100)
          self.PortOpened=1
          LL.I("Направление MODBUS RTU COM{} [DirID={}] запущено успешно".format(dirC["порт"], DirID)) 
        #DirID = svimb.CreateRTUdir(int(dirC["порт"]), **tmpD)

        
 
        #--- перечисление измерителей на направлении
        for instC in dirC["Измеритель"]:
     
          if "канал" in instC:
            #---- запуск опроса каналов измерения в формате float
            for chL in instC["канал"]:
              chD = {}  # дескриптор канала
              chD['DirID'] = DirID         # код направления на котором находится измеритель
              chD['DevAddr'] = eval(instC["адрес"], {}, {}) # адрес измерителя на направлении (шине MODBUS)
              chD['RegAddr'] = eval(chL[1], {}, {})  # адрес сканируемого измерительного регистра (в регистровом поле MODBUS измерителя) 
              chD['наименование'] = chL[0] # уникальное наименование измерительного канала (по нему идет связка с вирт. приборами)  
              chD['Link'] = [] # список заполняется уже после создания виртуальных приборов
              ChID = svimb.AddChan(chD['DirID'], chD['DevAddr'], chD['RegAddr'], -1)   

              self.chanD1[ChID] = chD
              self.chNamesD[chD['наименование']] = ChID
              LL.I("Измерительный канал '{}' в устройстве c адресом {} [RegAddr={:x}h DirID={}] запущен успешно".format(
                    chD['наименование'], chD['DevAddr'],  chD['RegAddr'], chD['DirID'])) 

          if "канал04" in instC:
            #---- запуск опроса каналов измерения по ф-ии 04h MODBUS
            for chL in instC["канал04"]:
              chD = {}  # дескриптор канала
              chD['DirID'] = DirID         # код направления на котором находится измеритель
              chD['DevAddr'] = eval(instC["адрес"], {}, {}) # адрес измерителя на направлении (шине MODBUS)
              chD['RegAddr'] = eval(chL[1], {}, {}) # адрес сканируемого измерительного регистра (в регистровом поле MODBUS измерителя) 
              chD['наименование'] = chL[0] # уникальное наименование измерительного канала (по нему идет связка с вирт. приборами)  
              ChID = svimb.AddChan(chD['DirID'], chD['DevAddr'], chD['RegAddr'], -1)   

              self.chanD1[ChID] = chD
              LL.I("Измерительный канал '{}' в устройстве c адресом {} [RegAddr={:x}h DirID={}] запущен успешно".format(
                  chD['наименование'], chD['DevAddr'],  chD['RegAddr'], chD['DirID'])) 

               #--- строим словарь доступных виртуальных приборов на основании конфигурации
      for vkey in Cfg1["Виртуальные приборы"]:
       for self.vi in Cfg1["Виртуальные приборы"][vkey]:
        self.vinstrD1[self.vi["наименование"]] = {"vtype": vkey } 
        self.vinstrD1[self.vi["наименование"]].update(self.vi) # переносим все ключи - экземпляр виртуального прибора потом сам разберется 
      
    # конец self.ChannelsInit==0
    if(self.ChannelsInit==1): 
        self.vinstrD1.clear()
        self.vi.clear()
        for vkey in Cfg1["Виртуальные приборы"]:
         for self.vi in Cfg1["Виртуальные приборы"][vkey]:
          self.vinstrD1[self.vi["наименование"]] = {"vtype": vkey } 
          self.vinstrD1[self.vi["наименование"]].update(self.vi) # переносим все ключи - экземпляр виртуального прибора потом сам разберется 
          for tmpi in self.chanD1:
           self.chanD1[tmpi]['Link']=[]

  #--- cоздаем набор виртуальных приборов на основании разобранной конфигурации

    self.ChannelsInit=1
    for vikey, self.vi in self.vinstrD1.items():
      if vikey not in vstateD:  vstateD[vikey] = {}  # виртуальный прибор сам заполнит свой словарь состояний
      vtype = self.vi["vtype"]
      if vtype == "Вольтметр":
        self.vi["obj"] = CVolt(self,self.vi, vstateD[vikey], cfg2['CurrCFG'][vikey], fTech = fTech1)
      if vtype == "Термометр":
        self.vi["obj"] = CTemp(self,self.vi, vstateD[vikey], cfg2['CurrCFG'][vikey], fTech = fTech1)
      if vtype == "Иономер":
        self.vi["obj"] = CIon(self, self.vi, vstateD[vikey], cfg2['CurrCFG'][vikey], cfgLocalProfil,  fTech = fTech1)
      if vtype == "Измеритель тока":
        self.vi["obj"] = CAmper(self,self.vi, vstateD[vikey], cfg2['CurrCFG'][vikey], fTech = fTech1)
      if vtype == "Кислородомер":
        self.vi["obj"] = CO_2(self, self.vi,table_stateD, vstateD[vikey], cfg2['CurrCFG'][vikey], cfgLocalProfil, fTech = fTech1)
      if vtype == "Измеритель сопротивления":
        self.vi["obj"] = CCond(self,self.vi, vstateD[vikey], cfg2['CurrCFG'][vikey],cfgLocalProfil, fTech = fTech1)
      if vtype == "Сопротивление.Диапазон":
        self.vi["obj"] = CR_Band(self,self.vi, vstateD[vikey], cfg2['CurrCFG'][vikey], fTech = fTech1)
      if vtype == "Измеритель давления":
        self.vi["obj"] = CPressure(self,self.vi, vstateD[vikey], cfg2['CurrCFG'][vikey], fTech = fTech1)
      if vtype == "Модуль":
        self.vi["obj"] = CUnit(self,self.vi, vstateD[vikey], cfg2['CurrCFG'][vikey], fTech = fTech1)
      if vtype == "График":
        self.vi["obj"] = CChart_II(self,self.vi, vstateD[vikey], cfg2['CurrCFG'][vikey], fTech = fTech1)
      if vtype == "Регистратор":
        self.vi["obj"] = CNotepad(self,self.vi, vstateD[vikey], cfg2['CurrCFG'][vikey], fTech = fTech1)
      if vtype == "Блокнот":
        self.vi["obj"] = CLiteNotepad(self,self.vi, vstateD[vikey], cfg2['CurrCFG'][vikey], fTech = fTech1)
      if vtype == "Протокол":
        self.vi["obj"] = CProtokol(self,self.vi, vstateD[vikey], cfg2['CurrCFG'][vikey], fTech = fTech1)
      if vtype == "Ввод данных":
        a=False  
        self.vi["obj"] = CInputUnit_(self,self.vi, vstateD[vikey], cfg2['CurrCFG'][vikey], fTech = fTech1)

      if vtype == "Стрелочный прибор":
        self.vi["obj"] = CArrow_Pr(self,self.vi, vstateD[vikey], cfg2['CurrCFG'][vikey], fTech = fTech1)												  
    #--- связка каналов с виртуальными приборами TODO - обработка ошибок 
    for vikey, self.vi in self.vinstrD1.items():
      if ("obj" in self.vi) and ("meas" in self.vi):
        for chN in self.vi["meas"]:
          tmpVPParam=cfg2['CurrCFG'][vikey]['VPParam']
          if(tmpVPParam!='1'):
              if(chN!='0'):
                  '''if(self.chanD1[self.chNamesD[chN]]['Link']==[]):'''
                  self.chanD1[self.chNamesD[chN]]['Link'].append(vikey)

    #--- установка Callback ф-ии в драйвер
    #svimb.SetDSCallback(OnDataReady_1)

    q=1 
    
  def OpenPort_1(self, NumPort):
    #import svimb
    self.DirID = svimb.CreateRTUdir(NumPort, 38400, 0, 100, 100)
    self.PortOpened=1
    LL.I("Направление MODBUS RTU COM{} [DirID={}] запущено успешно".format(NumPort, self.DirID))



class CfmDigitalKeyboard(QtGui.QMainWindow, Ui_fmDigitalKeyboard):
  """ Класс формы поиска измерительных модулей"""
  def __init__(self,vCE): 
    """ Инициализация класса формы поиска измерительных модулей"""   
    global vinstrD
    global cstateD
    super(CfmDigitalKeyboard, self).__init__() 
    super().__init__()    
    self.setupUi(self)
    self.vCE=vCE
    self.stackUnder=''
    self.tb_1.clicked.connect(self.on_tb_1)
    self.tb_2.clicked.connect(self.on_tb_2)
    self.tb_3.clicked.connect(self.on_tb_3)
    self.tb_4.clicked.connect(self.on_tb_4)
    self.tb_5.clicked.connect(self.on_tb_5)
    self.tb_6.clicked.connect(self.on_tb_6)
    self.tb_7.clicked.connect(self.on_tb_7)
    self.tb_8.clicked.connect(self.on_tb_8)
    self.tb_9.clicked.connect(self.on_tb_9)
    self.tb_0.clicked.connect(self.on_tb_0)
    self.tb_b.clicked.connect(self.on_tb_b)
    self.tb_.clicked.connect(self.on_tb_)


  def on_tb_1(self):
      """ Событие нажатия кнопки"""
      self.Str='1'
      self.Add();
      q=0

  def on_tb_2(self):
      """ Событие нажатия кнопки"""
      self.Str='2'
      self.Add();
      q=0

  def on_tb_3(self):
      """ Событие нажатия кнопки"""
      self.Str='3'
      self.Add();
      q=0

  def on_tb_4(self):
      """ Событие нажатия кнопки"""
      self.Str='4'
      self.Add();
      q=0

  def on_tb_5(self):
      """ Событие нажатия кнопки"""
      self.Str='5'
      self.Add();
      q=0

  def on_tb_6(self):
      """ Событие нажатия кнопки"""
      self.Str='6'
      self.Add();
      q=0

  def on_tb_7(self):
      """ Событие нажатия кнопки"""
      self.Str='7'
      self.Add();
      q=0

  def on_tb_8(self):
      """ Событие нажатия кнопки"""
      self.Str='8'
      self.Add();
      q=0

  def on_tb_9(self):
      """ Событие нажатия кнопки"""
      self.Str='9'
      self.Add();
      q=0

  def on_tb_0(self):
      """ Событие нажатия кнопки"""
      self.Str='0'
      self.Add();
      q=0

  def on_tb_b(self):
      """ Событие нажатия кнопки"""
      self.Str='.'
      self.Add();
      q=0

  def on_tb_(self):
      """ закрытие формы"""
      self.leText.clear()
      self.vCE.DigData=''
      q=0

  def Add(self):
      """ Событие нажатия кнопки"""
      self.leText.setText(self.leText.text() +self.Str)
      self.vCE.DigData=self.leText.text()
      q=0


class CfmKeyboard(QtGui.QMainWindow, Ui_fmKeyboard):
  """ Класс формы поиска измерительных модулей"""
  def __init__(self,vCE): 
    """ Инициализация класса формы поиска измерительных модулей"""   
    global vinstrD
    global cstateD
    super(CfmKeyboard, self).__init__() 
    super().__init__()    
    self.setupUi(self)
    self.vCE=vCE
    self.Caps=0
    self.Shift=0
    self.EngRus=0
    self.tb_1.clicked.connect(self.on_tb_1)
    self.tb_2.clicked.connect(self.on_tb_2)
    self.tb_3.clicked.connect(self.on_tb_3)
    self.tb_4.clicked.connect(self.on_tb_4)
    self.tb_5.clicked.connect(self.on_tb_5)
    self.tb_6.clicked.connect(self.on_tb_6)
    self.tb_7.clicked.connect(self.on_tb_7)
    self.tb_8.clicked.connect(self.on_tb_8)
    self.tb_9.clicked.connect(self.on_tb_9)
    self.tb_0.clicked.connect(self.on_tb_0)
    self.tb_b.clicked.connect(self.on_tb_b)
    self.tb_.clicked.connect(self.on_tb_)

    self.tb_minus.clicked.connect(self.on_tb_minus)
    self.tb_eq.clicked.connect(self.on_tb_eq)
    self.tb_d2.clicked.connect(self.on_tb_d2)

    self.tb_tilda.clicked.connect(self.on_tb_tilda)


    self.tb_q.clicked.connect(self.on_tb_q)
    self.tb_w.clicked.connect(self.on_tb_w)
    self.tb_e.clicked.connect(self.on_tb_e)
    self.tb_r.clicked.connect(self.on_tb_r)
    self.tb_t.clicked.connect(self.on_tb_t)
    self.tb_y.clicked.connect(self.on_tb_y)
    self.tb_u.clicked.connect(self.on_tb_u)
    self.tb_o.clicked.connect(self.on_tb_o)
    self.tb_p.clicked.connect(self.on_tb_p)
    self.tb_sq1.clicked.connect(self.on_tb_sq1)
    self.tb_sq2.clicked.connect(self.on_tb_sq2)
    self.tb_a.clicked.connect(self.on_tb_a)
    self.tb_s.clicked.connect(self.on_tb_s)
    self.tb_d.clicked.connect(self.on_tb_d)
    self.tb_f.clicked.connect(self.on_tb_f)
    self.tb_g.clicked.connect(self.on_tb_g)
    self.tb_h.clicked.connect(self.on_tb_h)
    self.tb_j.clicked.connect(self.on_tb_j)
    self.tb_k.clicked.connect(self.on_tb_k)
    self.tb_l.clicked.connect(self.on_tb_l)
    self.tb_tz.clicked.connect(self.on_tb_tz)
    self.tb_ap.clicked.connect(self.on_tb_ap)
    self.tb_z.clicked.connect(self.on_tb_z)
    self.tb_x.clicked.connect(self.on_tb_x)
    self.tb_c.clicked.connect(self.on_tb_c)
    self.tb_v.clicked.connect(self.on_tb_v)
    self.tb_b.clicked.connect(self.on_tb_b)
    self.tb_n.clicked.connect(self.on_tb_n)
    self.tb_m.clicked.connect(self.on_tb_m)
    self.tb_z1.clicked.connect(self.on_tb_z1)
    self.tb_t1.clicked.connect(self.on_tb_t1)
    self.tb_d1.clicked.connect(self.on_tb_d1)
    self.tb_Space.clicked.connect(self.on_tb_Space)
    self.tb_Del.clicked.connect(self.on_tb_Del)
    self.tb_Caps.clicked.connect(self.on_tb_Caps)
    self.tb_Shift.clicked.connect(self.on_tb_Shift)
    self.tb_Ru_En.clicked.connect(self.on_tb_Ru_En)



  def on_tb_1(self):
      """ Событие нажатия кнопки"""
      self.Str=self.tb_1.text()
      self.Add();
      q=0

  def on_tb_2(self):
      """ Событие нажатия кнопки"""
      self.Str=self.tb_2.text()
      self.Add();
      q=0

  def on_tb_3(self):
      """ Событие нажатия кнопки"""
      self.Str=self.tb_3.text()
      self.Add();
      q=0

  def on_tb_4(self):
      """ Событие нажатия кнопки"""
      self.Str=self.tb_4.text()
      self.Add();
      q=0

  def on_tb_5(self):
      """ Событие нажатия кнопки"""
      self.Str=self.tb_5.text()
      self.Add();
      q=0

  def on_tb_6(self):
      """ Событие нажатия кнопки"""
      self.Str=self.tb_6.text()
      self.Add();
      q=0

  def on_tb_7(self):
      """ Событие нажатия кнопки"""
      self.Str=self.tb_7.text()
      self.Add();
      q=0

  def on_tb_8(self):
      """ Событие нажатия кнопки"""
      self.Str=self.tb_8.text()
      self.Add();
      q=0

  def on_tb_9(self):
      """ Событие нажатия кнопки"""
      self.Str=self.tb_9.text()
      self.Add();
      q=0
      q=0

  def on_tb_0(self):
      """ Событие нажатия кнопки"""
      self.Str=self.tb_0.text()
      self.Add();
      q=0

  def on_tb_b(self):
      """ Событие нажатия кнопки"""
      self.Str='.'
      self.Add();
      q=0

  def on_tb_(self):
      """ закрытие формы"""
      self.leText.clear()
      self.vCE.StrData=''
      q=0

      
  def on_tb_q(self):
      """ Событие нажатия кнопки"""
      self.Str= self.tb_q.text()
      self.Add();      
      q=0

  def on_tb_w(self):
      """ Событие нажатия кнопки"""
      self.Str=self.tb_w.text()
      self.Add();
      q=0

  def on_tb_e(self):
      """ Событие нажатия кнопки"""
      self.Str=self.tb_e.text()
      self.Add();
      q=0

  def on_tb_r(self):
      """ Событие нажатия кнопки"""
      self.Str=self.tb_r.text()
      self.Add();
      q=0

  def on_tb_t(self):
      """ Событие нажатия кнопки"""
      self.Str=self.tb_t.text()
      self.Add();
      q=0

  def on_tb_y(self):
      """ Событие нажатия кнопки"""
      self.Str=self.tb_y.text()
      self.Add();
      q=0

  def on_tb_u(self):
      """ Событие нажатия кнопки"""
      self.Str=self.tb_u.text()
      self.Add();
      q=0

  def on_tb_i(self):
      """ Событие нажатия кнопки"""
      self.Str=self.tb_i.text()
      self.Add();
      q=0

  def on_tb_o(self):
      """ Событие нажатия кнопки"""
      self.Str=self.tb_o.text()
      self.Add();
      q=0

  def on_tb_p(self):
      """ Событие нажатия кнопки"""
      self.Str=self.tb_p.text()
      self.Add();
      q=0

  def on_tb_sq1(self):
      """ Событие нажатия кнопки"""
      self.Str=self.tb_sq1.text()
      self.Add();
      q=0

  def on_tb_sq2(self):
      """ Событие нажатия кнопки"""
      self.Str=self.tb_sq2.text()
      self.Add();
      q=0

  def on_tb_a(self):
      """ Событие нажатия кнопки"""
      self.Str=self.tb_a.text()
      self.Add();
      q=0

  def on_tb_s(self):
      """ Событие нажатия кнопки"""
      self.Str=self.tb_s.text()
      self.Add();
      q=0

  def on_tb_d(self):
      """ Событие нажатия кнопки"""
      self.Str=self.tb_d.text()
      self.Add();
      q=0

  def on_tb_f(self):
      """ Событие нажатия кнопки"""
      self.Str=self.tb_f.text()
      self.Add();
      q=0

  def on_tb_g(self):
      """ Событие нажатия кнопки"""
      self.Str=self.tb_g.text()
      self.Add();
      q=0

  def on_tb_h(self):
      """ Событие нажатия кнопки"""
      self.Str=self.tb_h.text()
      self.Add();
      q=0

  def on_tb_j(self):
      """ Событие нажатия кнопки"""
      self.Str=self.tb_j.text()
      self.Add();
      q=0

  def on_tb_k(self):
      """ Событие нажатия кнопки"""
      self.Str=self.tb_k.text()
      self.Add();
      q=0

  def on_tb_l(self):
      """ Событие нажатия кнопки"""
      self.Str=self.tb_l.text()
      self.Add();
      q=0

  def on_tb_tz(self):
      """ Событие нажатия кнопки"""
      self.Str=self.tb_tz.text()
      self.Add();
      q=0

  def on_tb_ap(self):
      """ Событие нажатия кнопки"""
      self.Str=self.tb_ap.text()
      self.Add();
      q=0

  def on_tb_z(self):
      """ Событие нажатия кнопки"""
      self.Str=self.tb_z.text()
      self.Add();
      q=0

  def on_tb_x(self):
      """ Событие нажатия кнопки"""
      self.Str=self.tb_x.text()
      self.Add();
      q=0

  def on_tb_c(self):
      """ Событие нажатия кнопки"""
      self.Str=self.tb_c.text()
      self.Add();
      q=0

  def on_tb_v(self):
      """ Событие нажатия кнопки"""
      self.Str=self.tb_v.text()
      self.Add();
      q=0

  def on_tb_b(self):
      """ Событие нажатия кнопки"""
      self.Str=self.tb_b.text()
      self.Add();
      q=0

  def on_tb_n(self):
      """ Событие нажатия кнопки"""
      self.Str=self.tb_n.text()
      self.Add();
      q=0

  def on_tb_m(self):
      """ Событие нажатия кнопки"""
      self.Str=self.tb_m.text()
      self.Add();
      q=0

  def on_tb_z1(self):
      """ Событие нажатия кнопки"""
      self.Str=self.tb_z1.text()
      self.Add();
      q=0

  def on_tb_t1(self):
      """ Событие нажатия кнопки"""
      self.Str=self.tb_t1.text()
      self.Add();
      q=0

  def on_tb_d1(self):
      """ Событие нажатия кнопки"""
      self.Str=self.tb_d1.text()
      self.Add();
      q=0

  def on_tb_minus(self):
      """ Событие нажатия кнопки"""
      self.Str=self.tb_minus.text()
      self.Add();
      q=0

  def on_tb_eq(self):
      """ Событие нажатия кнопки"""
      self.Str=self.tb_eq.text()
      self.Add();
      q=0

  def on_tb_d2(self):
      """ Событие нажатия кнопки"""
      self.Str=self.tb_d2.text()
      self.Add();
      q=0


  def on_tb_tilda(self):
      """ Событие нажатия кнопки"""
      self.Str=self.tb_tilda.text()
      self.Add();
      q=0


  def on_tb_Space(self):
      """ Событие нажатия кнопки"""
      self.Str=' '
      self.Add();
      q=0

  def on_tb_Del(self):
      """ Событие нажатия кнопки"""
      self.Str='9'
      self.Add();
      q=0

  def on_tb_Caps(self):
      """ Событие нажатия кнопки"""
      if((self.Caps==0)&(self.Shift==0)):
          self.Caps=1
      else:
          self.Caps=0
      self.SelectLetter()
      q=0

  def on_tb_Shift(self):
      """ Событие нажатия кнопки"""
      if(self.Shift==0):
          self.Shift=1
      else:
          self.Shift=0
      self.SelectLetter()
      q=0

  def on_tb_Ru_En(self):
      if(self.EngRus==0):
          self.EngRus=1
      else:
          self.EngRus=0
      self.SelectLetter()
      q=0



  def Add(self):
      """ Событие нажатия кнопки"""
      self.leText.setText(self.leText.text() +self.Str)
      self.vCE.StrData=self.leText.text()
      if(self.Shift==1):
          self.Caps=0
          self.Shift=0
          self.SelectLetter()
      q=0

  def ShowEvent(self,event):
      self.Shift=0
      self.Caps=0
      self.EngRus=0
      self.show()
      q=0

  def SelectLetter(self):
      """ Событие нажатия кнопки"""
      if(self.Shift==1):self.Caps=1
      if(self.Caps==0)&(self.EngRus==0):
          self.tb_q.setText('q')
          self.tb_w.setText('w')
          self.tb_e.setText('e')
          self.tb_r.setText('r')
          self.tb_t.setText('t')
          self.tb_y.setText('y')
          self.tb_u.setText('u')
          self.tb_i.setText('i')
          self.tb_o.setText('i')
          self.tb_p.setText('o')
          self.tb_sq1.setText('[')
          self.tb_sq2.setText(']')
          self.tb_a.setText('a')
          self.tb_s.setText('s')
          self.tb_d.setText('d')
          self.tb_f.setText('f')
          self.tb_g.setText('g')
          self.tb_h.setText('h')
          self.tb_j.setText('j')
          self.tb_k.setText('k')
          self.tb_l.setText('l')
          self.tb_tz.setText(';')
          self.tb_ap.setText("'")
          self.tb_z.setText('z')
          self.tb_x.setText('x')
          self.tb_c.setText('c')
          self.tb_v.setText('v')
          self.tb_b.setText('b')
          self.tb_n.setText('n')
          self.tb_m.setText('m')
          self.tb_z1.setText(',')
          self.tb_t1.setText('.')
          self.tb_d1.setText('/')
          if(self.Shift==1):
              self.tb_Shift.setText('SHIFT')
              self.tb_Caps.setText('Caps') 

              self.tb_1.setText('!')
              self.tb_2.setText('@')
              self.tb_3.setText('#')
              self.tb_4.setText('$')
              self.tb_5.setText('%')
              self.tb_6.setText('^')
              self.tb_7.setText('&')
              self.tb_8.setText('*')
              self.tb_9.setText('(')
              self.tb_0.setText(')')


              self.tb_minus.setText('_')
              self.tb_eq.setText('+')
              self.tb_d2.setText('|')

              self.tb_tilda.setText('~')

          else:
              self.tb_Shift.setText('Shift')
              self.tb_Caps.setText('CAPS')
              self.tb_1.setText('1')
              self.tb_2.setText('2')
              self.tb_3.setText('3')
              self.tb_4.setText('4')
              self.tb_5.setText('5')
              self.tb_6.setText('6')
              self.tb_7.setText('7')
              self.tb_8.setText('8')
              self.tb_9.setText('9')
              self.tb_0.setText('0')


              self.tb_minus.setText('-')
              self.tb_eq.setText('=')
              self.tb_d2.setText('/')

              self.tb_tilda.setText('`')
          self.tb_Ru_En.setText('Rus')
      if(self.Caps==1)&(self.EngRus==0):
          self.tb_q.setText('Q')
          self.tb_w.setText('W')
          self.tb_e.setText('E')
          self.tb_r.setText('R')
          self.tb_t.setText('T')
          self.tb_y.setText('Y')
          self.tb_u.setText('U')
          self.tb_i.setText('I')
          self.tb_o.setText('O')
          self.tb_p.setText('P')
          self.tb_sq1.setText('[')
          self.tb_sq2.setText(']')
          self.tb_a.setText('A')
          self.tb_s.setText('S')
          self.tb_d.setText('D')
          self.tb_f.setText('F')
          self.tb_g.setText('G')
          self.tb_h.setText('H')
          self.tb_j.setText('J')
          self.tb_k.setText('K')
          self.tb_l.setText('L')
          self.tb_tz.setText(';')
          self.tb_ap.setText("'")
          self.tb_z.setText('Z')
          self.tb_x.setText('X')
          self.tb_c.setText('C')
          self.tb_v.setText('V')
          self.tb_b.setText('B')
          self.tb_n.setText('N')
          self.tb_m.setText('M')
          self.tb_z1.setText(',')
          self.tb_t1.setText('.')
          self.tb_d1.setText('/')
          if(self.Shift==1):
              self.tb_Shift.setText('SHIFT')
              self.tb_Caps.setText('Caps') 

              self.tb_1.setText('!')
              self.tb_2.setText('@')
              self.tb_3.setText('#')
              self.tb_4.setText('$')
              self.tb_5.setText('%')
              self.tb_6.setText('^')
              self.tb_7.setText('&')
              self.tb_8.setText('*')
              self.tb_9.setText('(')
              self.tb_0.setText(')')


              self.tb_minus.setText('_')
              self.tb_eq.setText('+')
              self.tb_d2.setText('|')

              self.tb_tilda.setText('~')

          else:
              self.tb_Shift.setText('Shift')
              self.tb_Caps.setText('CAPS')
              self.tb_1.setText('1')
              self.tb_2.setText('2')
              self.tb_3.setText('3')
              self.tb_4.setText('4')
              self.tb_5.setText('5')
              self.tb_6.setText('6')
              self.tb_7.setText('7')
              self.tb_8.setText('8')
              self.tb_9.setText('9')
              self.tb_0.setText('0')


              self.tb_minus.setText('-')
              self.tb_eq.setText('=')
              self.tb_d2.setText('/')

              self.tb_tilda.setText('`')
          self.tb_Ru_En.setText('Rus')
      if(self.Caps==0)&(self.EngRus==1):
          self.tb_q.setText('й')
          self.tb_w.setText('ц')
          self.tb_e.setText('у')
          self.tb_r.setText('к')
          self.tb_t.setText('е')
          self.tb_y.setText('н')
          self.tb_u.setText('г')
          self.tb_i.setText('ш')
          self.tb_o.setText('щ')
          self.tb_p.setText('з')
          self.tb_sq1.setText('х')
          self.tb_sq2.setText('ъ')
          self.tb_a.setText('ф')
          self.tb_s.setText('ы')
          self.tb_d.setText('в')
          self.tb_f.setText('а')
          self.tb_g.setText('п')
          self.tb_h.setText('р')
          self.tb_j.setText('о')
          self.tb_k.setText('л')
          self.tb_l.setText('д')
          self.tb_tz.setText('ж')
          self.tb_ap.setText("э")
          self.tb_z.setText('я')
          self.tb_x.setText('ч')
          self.tb_c.setText('с')
          self.tb_v.setText('м')
          self.tb_b.setText('и')
          self.tb_n.setText('т')
          self.tb_m.setText('ь')
          self.tb_z1.setText('б')
          self.tb_t1.setText('ю')
          self.tb_d1.setText('.')
          if(self.Shift==1):
              self.tb_Shift.setText('SHIFT')
              self.tb_Caps.setText('Caps') 

              self.tb_1.setText('!')
              self.tb_2.setText('"')
              self.tb_3.setText('№')
              self.tb_4.setText(';')
              self.tb_5.setText('%')
              self.tb_6.setText(':')
              self.tb_7.setText('?')
              self.tb_8.setText('*')
              self.tb_9.setText('(')
              self.tb_0.setText(')')


              self.tb_minus.setText('_')
              self.tb_eq.setText('+')
              self.tb_d2.setText('/')

              self.tb_tilda.setText('ё')

          else:
              self.tb_Shift.setText('Shift')
              self.tb_Caps.setText('CAPS')
              self.tb_1.setText('1')
              self.tb_2.setText('2')
              self.tb_3.setText('3')
              self.tb_4.setText('4')
              self.tb_5.setText('5')
              self.tb_6.setText('6')
              self.tb_7.setText('7')
              self.tb_8.setText('8')
              self.tb_9.setText('9')
              self.tb_0.setText('0')


              self.tb_minus.setText('-')
              self.tb_eq.setText('=')
              self.tb_d2.setText('/')

              self.tb_tilda.setText('ё')
          self.tb_Ru_En.setText('Eng')
      if(self.Caps==1)&(self.EngRus==1):
          self.tb_q.setText('Й')
          self.tb_w.setText('Ц')
          self.tb_e.setText('У')
          self.tb_r.setText('К')
          self.tb_t.setText('Е')
          self.tb_y.setText('Н')
          self.tb_u.setText('Г')
          self.tb_i.setText('Ш')
          self.tb_o.setText('Щ')
          self.tb_p.setText('З')
          self.tb_sq1.setText('Х')
          self.tb_sq2.setText('Ъ')
          self.tb_a.setText('Ф')
          self.tb_s.setText('Ы')
          self.tb_d.setText('В')
          self.tb_f.setText('А')
          self.tb_g.setText('П')
          self.tb_h.setText('Р')
          self.tb_j.setText('О')
          self.tb_k.setText('Л')
          self.tb_l.setText('Д')
          self.tb_tz.setText('Ж')
          self.tb_ap.setText("Э")
          self.tb_z.setText('Я')
          self.tb_x.setText('Ч')
          self.tb_c.setText('С')
          self.tb_v.setText('М')
          self.tb_b.setText('И')
          self.tb_n.setText('Т')
          self.tb_m.setText('Ь')
          self.tb_z1.setText('Б')
          self.tb_t1.setText('Ю')
          self.tb_d1.setText('.')
          if(self.Shift==1):
              self.tb_Shift.setText('SHIFT')
              self.tb_Caps.setText('Caps') 

              self.tb_1.setText('!')
              self.tb_2.setText('"')
              self.tb_3.setText('№')
              self.tb_4.setText(';')
              self.tb_5.setText('%')
              self.tb_6.setText(':')
              self.tb_7.setText('?')
              self.tb_8.setText('*')
              self.tb_9.setText('(')
              self.tb_0.setText(')')


              self.tb_minus.setText('_')
              self.tb_eq.setText('+')
              self.tb_d2.setText('/')

              self.tb_tilda.setText('Ё')

          else:
              self.tb_Shift.setText('Shift')
              self.tb_Caps.setText('CAPS')
              self.tb_1.setText('1')
              self.tb_2.setText('2')
              self.tb_3.setText('3')
              self.tb_4.setText('4')
              self.tb_5.setText('5')
              self.tb_6.setText('6')
              self.tb_7.setText('7')
              self.tb_8.setText('8')
              self.tb_9.setText('9')
              self.tb_0.setText('0')


              self.tb_minus.setText('-')
              self.tb_eq.setText('=')
              self.tb_d2.setText('/')

              self.tb_tilda.setText('ё')
          self.tb_Ru_En.setText('Eng')




 
 

     

