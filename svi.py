# -*- coding: utf-8 -*-
#---
__author__  = "Aleksey Bocharov <trashmbox@yandex.ru>"
__status__  = "development"
__version__ = "0.5i"
__date__    = "19 Сентября 2013"
#---
from common import *
import os, sys
import atexit
import pickle
from datetime import datetime
import re
import svimb
from collections import namedtuple
import log # дополнительные возможности логирования
import logging
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
from temperature import*
from notepad import*
from protokol import*
from config_edit import*
import Results
import AllResults
import time

from fmNaladka import Ui_fmNaladka
from fmPortCons import Ui_fmPortCons
from fmMBCons import Ui_fmMBCons
from fmNewReg import Ui_dgNewReg
from fmAD779x import Ui_fmAD779x
from fmVPar import Ui_fmVPar
from fmNewConv import Ui_fmNewConv
from fmVConf import Ui_fmVConf
from fmTPar import Ui_fmTPar
from fmTConf import Ui_fmTConf 
from fmTPPar import Ui_fmTPPar
from fmTPConf import Ui_fmTPConf 
from fmCondPar import Ui_fmCondPar
from fmCondConf import Ui_fmCondConf 
from fmAmperPar import Ui_fmAmperPar
from fmAmperConf import Ui_fmAmperConf 
from fmMain import Ui_fmMain
from fmChangeVPribors import Ui_fmChangeVPribors
from fmSelectProfil import Ui_fmSelectProfil
from vinstr import *
from filtr import filtrP
import Results

LL = logging.getLogger('SVI')  # сконфигурирован основным модулем
winCrConf=None
global Cfg
Cfg={}
# ---------------------------------------------- 
#        Дополнительные типы

# атрибуты регистров для консоли драйвера MODBUS
regsAttr = namedtuple('regsAttr', ['DevAddr', 'RegAddr']) # адрес измерителя, адрес регистра в адресном пространстве MODBUS
# ---------------------------------------------- 
#        Локальные ф-ии

def LoadCfg(fname, cdict = {}, tpl = None):
  """ чтение и разбор файла конфигурации fname по шаблону tpl, если задан словарь cdict - то к разобранной 
      конфигурации на выходе добавляется cdict (то есть можно собрать словарь из разных файлов) 
        * секции в квадратных скобках
        * комментарии с символа #
        * имя параметра от значения отделяется символом =
          параметр может получать список значений, отделенных запятыми
        * допускается иерархическая структура секций - вложенные секции имеют большее кол-во квадратных скобок
        * допускаются одинаковые имена вложенных секций - даже если вложенная секция одна, она помещается в 
          список. таким образом словарь секции верхнего уровня получает ключ равный имени вложенной секции а
          значение - список словарей значений вложенных секций 
      В итоге на выходе получается словарь словарей
      Замечания:
        Если секция не обозначена, то словарь параметров помещается в значение ключа "Default"   
        Если параметр присутствует без знака равенства, или после знака равенства СРАЗУ стоит перевод строки,
        то за значение параметра принимается ''    
        Ключ "Default" в выходном словаре размещается всегда (даже если нет параметров без секций)"""

  rgSect = re.compile(r'(\[+)([^\]]+)(\]+)') 
  lvl = 0    # текущий уровень вложения  
  sdict = {} # накапливаемый словарь значений текущей обрабатываеамой секции
  cntLine = 0
  Sections = ['Default', ] # список секций текущего уровня вложения
  pLst = None    # связанный с result список для вставки текущей накопленной мультисекции

  if Sections[-1] not in cdict:
    result = { Sections[-1]: {} }
  else:
    result = cdict.copy()

  try:
    CfgFile = open(fname, 'rt', encoding = 'utf_8')
  except:                                 
    CfgFile = None 

  #--- ВРЕМЕННО !!!
  #print("tpl = {}".format(tpl))
  #print("-------------------------------------------------")
  #--- ВРЕМЕННО !!!

  if CfgFile: 
    for line in CfgFile:
      cntLine += 1
      temp = line.split('#')[0]   # "срезаем" комментарии
      temp = temp.strip()
      if temp:
        sm = rgSect.match(temp)
        if sm:
          # найден заголовок новой секции - переносим накопленную секцию
          if pLst != None :  
            # накопленная секция является мультисекцией (или вложенной)
            pLst.append(sdict)  # связка с result уже выполнена
          else:
            result[Sections[-1]].update(sdict) 

          #--- ВРЕМЕННО !!!
          #print("result = {}".format(result))
          #--- ВРЕМЕННО !!!          

          sdict = {}
          new_lvl = len(sm.group(1))
          if (new_lvl - lvl) > 1:  raise Exception("Недопустимый уровень вложения в строке {} файла {}".format(cntLine, fname))
      
          if new_lvl > lvl:
            Sections.append(sm.group(2))  
          elif new_lvl < lvl:
            Sections = Sections[0: new_lvl+1] 
            Sections[-1] = sm.group(2)
          else: 
            Sections[-1] = sm.group(2)

          #--- ВРЕМЕННО !!!
          #print("new_lv = {}  Sections = {}".format(new_lvl, Sections))
          #--- ВРЕМЕННО !!!

          lvl = new_lvl 
          pLst = None
          # ищем точку вставки будущей накопленной секции 
          # (т.е. инициализируем pLst при помощи "ссылочного" на result словаря pd)
          pd = result 
          for i in range(1, lvl):
            if isinstance(pd[Sections[i]], list):  pd = pd[Sections[i]][-1] 
            else:                                  pd = pd[Sections[i]]  

          if (lvl > 1) or (tpl and (Sections[-1] in tpl["мультисекции"])):
            # допускается несколько экземпляров секции 
            if Sections[-1] not in pd:
              pLst = []
              pd[Sections[-1]] = pLst
            else:
              pLst = pd[Sections[-1]]
          else:
            pLst = None
            result[Sections[-1]] = {}

          #--- ВРЕМЕННО !!!
          #print("result_tmp = {}".format(result))
          ##print("pLst = {}".format(pLst)) 
          #print("-------------------------------------------------")
          #--- ВРЕМЕННО !!!   

        else:
          # найден параметр
          parDsc = temp.partition('=')
          parLst = parDsc[2].split(',')
          parName = parDsc[0].strip()

          if len(parLst) > 1:
            # параметр представляет собой список значений
            tmpLst = []
            for value in parLst:
              tmpLst.append(value.strip())  
            parData = tmpLst

          else:  parData = parLst[0].strip()

          if tpl and (parName in tpl["мультипараметры"]):
            # допускается несколько экземпляров параметра
            if parName not in sdict:  sdict[parName] = [] # значения такого параметра собираются в список    
            sdict[parName].append(parData) # замечание: если мультипараметр - список, то получится список списков
          else: 
            sdict[parName] = parData

    # обработка файла завершена - добавляем последнюю накопленную секцию
    if pLst != None:  
      # накопленная секция является мультисекцией (или вложенной)
      pLst.append(sdict)  # связка с result уже выполнена
    else:
      result[Sections[-1]].update(sdict) 

    CfgFile.close()
  return result

def SaveCfg(fname, cdict = {}, tpl = None):
  """ чтение и разбор файла конфигурации fname по шаблону tpl, если задан словарь cdict - то к разобранной 
      конфигурации на выходе добавляется cdict (то есть можно собрать словарь из разных файлов) 
        * секции в квадратных скобках
        * комментарии с символа #
        * имя параметра от значения отделяется символом =
          параметр может получать список значений, отделенных запятыми
        * допускается иерархическая структура секций - вложенные секции имеют большее кол-во квадратных скобок
        * допускаются одинаковые имена вложенных секций - даже если вложенная секция одна, она помещается в 
          список. таким образом словарь секции верхнего уровня получает ключ равный имени вложенной секции а
          значение - список словарей значений вложенных секций 
      В итоге на выходе получается словарь словарей
      Замечания:
        Если секция не обозначена, то словарь параметров помещается в значение ключа "Default"   
        Если параметр присутствует без знака равенства, или после знака равенства СРАЗУ стоит перевод строки,
        то за значение параметра принимается ''    
        Ключ "Default" в выходном словаре размещается всегда (даже если нет параметров без секций)"""

  rgSect = re.compile(r'(\[+)([^\]]+)(\]+)') 
  lvl = 0    # текущий уровень вложения  
  sdict = {} # накапливаемый словарь значений текущей обрабатываеамой секции
  cntLine = 0
  Sections = ['Default', ] # список секций текущего уровня вложения
  pLst = None    # связанный с result список для вставки текущей накопленной мультисекции

  if Sections[-1] not in cdict:
    result = { Sections[-1]: {} }
  else:
    result = cdict.copy()

  try:
    CfgFile = open(fname, 'rt', encoding = 'utf_8')
  except:                                 
    CfgFile = None 

  #--- ВРЕМЕННО !!!
  #print("tpl = {}".format(tpl))
  #print("-------------------------------------------------")
  #--- ВРЕМЕННО !!!

  if CfgFile: 
    for line in CfgFile:
      cntLine += 1
      temp = line.split('#')[0]   # "срезаем" комментарии
      temp = temp.strip()
      if temp:
        sm = rgSect.match(temp)
        if sm:
          # найден заголовок новой секции - переносим накопленную секцию
          if pLst != None :  
            # накопленная секция является мультисекцией (или вложенной)
            pLst.append(sdict)  # связка с result уже выполнена
          else:
            result[Sections[-1]].update(sdict) 

          #--- ВРЕМЕННО !!!
          #print("result = {}".format(result))
          #--- ВРЕМЕННО !!!          

          sdict = {}
          new_lvl = len(sm.group(1))
          if (new_lvl - lvl) > 1:  raise Exception("Недопустимый уровень вложения в строке {} файла {}".format(cntLine, fname))
      
          if new_lvl > lvl:
            Sections.append(sm.group(2))  
          elif new_lvl < lvl:
            Sections = Sections[0: new_lvl+1] 
            Sections[-1] = sm.group(2)
          else: 
            Sections[-1] = sm.group(2)

          #--- ВРЕМЕННО !!!
          #print("new_lv = {}  Sections = {}".format(new_lvl, Sections))
          #--- ВРЕМЕННО !!!

          lvl = new_lvl 
          pLst = None
          # ищем точку вставки будущей накопленной секции 
          # (т.е. инициализируем pLst при помощи "ссылочного" на result словаря pd)
          pd = result 
          for i in range(1, lvl):
            if isinstance(pd[Sections[i]], list):  pd = pd[Sections[i]][-1] 
            else:                                  pd = pd[Sections[i]]  

          if (lvl > 1) or (tpl and (Sections[-1] in tpl["мультисекции"])):
            # допускается несколько экземпляров секции 
            if Sections[-1] not in pd:
              pLst = []
              pd[Sections[-1]] = pLst
            else:
              pLst = pd[Sections[-1]]
          else:
            pLst = None
            result[Sections[-1]] = {}

          #--- ВРЕМЕННО !!!
          #print("result_tmp = {}".format(result))
          ##print("pLst = {}".format(pLst)) 
          #print("-------------------------------------------------")
          #--- ВРЕМЕННО !!!   

        else:
          # найден параметр
          parDsc = temp.partition('=')
          parLst = parDsc[2].split(',')
          parName = parDsc[0].strip()

          if len(parLst) > 1:
            # параметр представляет собой список значений
            tmpLst = []
            for value in parLst:
              tmpLst.append(value.strip())  
            parData = tmpLst

          else:  parData = parLst[0].strip()

          if tpl and (parName in tpl["мультипараметры"]):
            # допускается несколько экземпляров параметра
            if parName not in sdict:  sdict[parName] = [] # значения такого параметра собираются в список    
            sdict[parName].append(parData) # замечание: если мультипараметр - список, то получится список списков
          else: 
            sdict[parName] = parData

    # обработка файла завершена - добавляем последнюю накопленную секцию
    if pLst != None:  
      # накопленная секция является мультисекцией (или вложенной)
      pLst.append(sdict)  # связка с result уже выполнена
    else:
      result[Sections[-1]].update(sdict) 

    CfgFile.close()
  return result


def BytesToHex(arr):
  """  ф-ия формирует на выходе строку Hex значений элементов массива arr """
  res = ""
  try:
    for b in arr:
      res += "{:02X}".format(b) 
  except(TypeError):
    pass       # TODO - логирование 
  return res


def ToUns16(data):
  """ преобразование int16_t в uint16_t """
  return int.from_bytes(data.to_bytes(2, 'little', signed = True), 'little')


def ToUns32(dlow, dhigh):
  """ преобразование двух int16_t в uint32_t """
  return int.from_bytes(dlow.to_bytes(2, 'little', signed = True) + dhigh.to_bytes(2, 'little', signed = True), 'little')
 
     
def ToSig32(dlow, dhigh):
  """ преобразование двух int16_t в int32_t """
  return int.from_bytes(dlow.to_bytes(2, 'little', signed = True) + dhigh.to_bytes(2, 'little', signed = True), 'little', signed = True)
 
# ---------------------------------------------- 
#        Классы

class CAD779x:
  """ работа с регистрами АЦП AD7792\AD7793, установленным в устройстве на шине MODBUS
      (пример необходимой карты MODBUS см. в OrmID(sysdef.h)) """
  # AddrMB - адрес устройства на шине MODBUS
  # f24b       - True - 24 разрядный АЦП (т.е. AD7793) - иначе 16 разрядов (т.е. AD7792)
  # раскладка карты MODBUS для доступа к АЦП:
  # mbaAddrReg  - адрес регистра AD7792\93, в который будет производится запись\чтение 
  # mbaWriteReg - записываемые в регистр AD7792\93 данные
  # mbaReadReg  - считанные из регистра AD7792\93 данные
  # mba92_Write - выполнить запись регистра AD7792
  # mba92_Read  - выполнить чтение регистра AD7792
  # mba93_Write - выполнить запись регистра AD7793 
  # mba93_Read  - выполнить чтение регистра AD7793

  def __init__(self, dirID, addrMB, confMB, f24b_ = False):
    """ dirID  - код направления на котором подключено устройство, поддерживающее MODBUS       
        addrMB - адрес устройства на шине MODBUS
        confMB - словарь с картой в регистровом\битовом поле MODBUS
        f24b_  - выбор типа АЦП (можно поменять и после создания класса)
    """
    self.DirID = dirID
    self.AddrMB = addrMB
    self.f24b = f24b_

    self.mbaAddrReg = int(confMB["AddrReg"])
    self.mbaWriteReg = int(confMB["WriteReg"])
    self.mbaReadReg = int(confMB["ReadReg"])
    self.mba92_Write = int(confMB["f92Write"]) 
    self.mba92_Read = int(confMB["f92Read"])
    self.mba93_Write = int(confMB["f93Write"])
    self.mba93_Read = int(confMB["f93Read"])


  def SelectAD7792(self):
    self.f24b = False


  def SelectAD7793(self):
    self.f24b = True


  def _Read8(self):
    """  чтение 8-разрядного регистра 
         (адрес регистра должен быть загружен заранее) """
    if (self.f24b):  svimb.WriteBit(self.DirID, self.AddrMB, self.mba93_Read, 1)
    else:            svimb.WriteBit(self.DirID, self.AddrMB, self.mba92_Read, 1) 

    tmpT = svimb.ReadRegs16(self.DirID, self.AddrMB, self.mbaReadReg, 1) 
    return (tmpT[0] & 0xff) 


  def _Read16(self):
    """  чтение 16-разрядного регистра
         (адрес регистра должен быть загружен заранее) """
    if (self.f24b):  svimb.WriteBit(self.DirID, self.AddrMB, self.mba93_Read, 1)
    else:            svimb.WriteBit(self.DirID, self.AddrMB, self.mba92_Read, 1) 
 
    tmpT = svimb.ReadRegs16(self.DirID, self.AddrMB, self.mbaReadReg, 1)
    return tmpT[0]


  def _Write16(self, data):
    """ запись 16-разрядного регистра
        (адрес регистра должен быть загружен заранее) """
    svimb.WriteReg16(self.DirID, self.AddrMB, self.mbaWriteReg, data & 0xffff) 
    if (self.f24b):  svimb.WriteBit(self.DirID, self.AddrMB, self.mba93_Write, 1) 
    else:            svimb.WriteBit(self.DirID, self.AddrMB, self.mba92_Write, 1)


  def _Read16_24(self):  
    """  чтение 16-разрядного регистра или 24-разрядного в зависимости от типа АЦП
         (адрес регистра должен быть загружен заранее) """
    res = 0
    if (self.f24b): 
      svimb.WriteBit(self.DirID, self.AddrMB, self.mba93_Read, 1)  
      (rlow, rhigh) = svimb.ReadRegs16(self.DirID, self.AddrMB, self.mbaReadReg, 2)
      blow = rlow.to_bytes(2, 'little', signed = True)
      bhigh = bytearray(rhigh.to_bytes(2, 'little', signed = True))
      bhigh[1] = 0  # "урезаем" до 24 разрядов 
      res = int.from_bytes(blow + bhigh, 'little')
 
    else:
      svimb.WriteBit(self.DirID, self.AddrMB, self.mba92_Read, 1)
      tmpT = svimb.ReadRegs16(self.DirID, self.AddrMB, self.mbaReadReg, 1)
      res = tmpT[0]

    return res 


  def _Write16_24(self, data):  
    """  запись 16-разрядного регистра или 24-разрядного в зависимости от типа АЦП
         (адрес регистра должен быть загружен заранее) """
    if (self.f24b): 
      svimb.WriteReg16(self.DirID, self.AddrMB, self.mbaWriteReg, data & 0xffff)
      svimb.WriteReg16(self.DirID, self.AddrMB, self.mbaWriteReg+1, (data & 0xff0000) >> 16)
      svimb.WriteBit(self.DirID, self.AddrMB, self.mba93_Write, 1)

    else:
      svimb.WriteReg16(self.DirID, self.AddrMB, self.mbaWriteReg, data & 0xffff)      
      svimb.WriteBit(self.DirID, self.AddrMB, self.mba92_Write, 1)
 

  def ReadStatus(self):
    """ чтение регистра статуса """
    svimb.WriteReg16(self.DirID, self.AddrMB, self.mbaAddrReg, 0)
   
    return self._Read8()

  def ReadID(self):
    """ чтение регистра идентификации """
    svimb.WriteReg16(self.DirID, self.AddrMB, self.mbaAddrReg, 4)

    return self._Read8() 

  def ReadData(self):
    """ чтение регистра данных (результат преобразования)  
        (возвращается всегда unsigned) """
    svimb.WriteReg16(self.DirID, self.AddrMB, self.mbaAddrReg, 3)
    data = self._Read16_24() 
    if (self.f24b): 
      # 24 бита 
      res = int.from_bytes(data.to_bytes(4, 'little', signed = True), 'little') 
    else:
      # 16 бит  
      res = int.from_bytes(data.to_bytes(2, 'little', signed = True), 'little')  

    return  res 


  def ReadOffset(self): 
    """ чтение регистра смещения нуля """
    svimb.WriteReg16(self.DirID, self.AddrMB, self.mbaAddrReg, 6)

    return self._Read16_24()


  def WriteOffset(self, data):
    """ запись регистра смещения нуля """
    svimb.WriteReg16(self.DirID, self.AddrMB, self.mbaAddrReg, 6)

    return self._Write16_24(data)


  def ReadScale(self): 
    """ чтение регистра коэффициента """
    svimb.WriteReg16(self.DirID, self.AddrMB, self.mbaAddrReg, 7)

    return self._Read16_24()


  def WriteScale(self, data):
    """ запись регистра коэффициента """
    svimb.WriteReg16(self.DirID, self.AddrMB, self.mbaAddrReg, 7)

    return self._Write16_24(data)

  
  def ReadMode(self):
    """ чтение регистра режима """
    svimb.WriteReg16(self.DirID, self.AddrMB, self.mbaAddrReg, 1)
 
    return self._Read16()


  def WriteMode(self, data):
    """ запись регистра режима """
    svimb.WriteReg16(self.DirID, self.AddrMB, self.mbaAddrReg, 1)

    return self._Write16(data)


  def ReadConf(self):
    """ чтение регистра конфигурации """
    svimb.WriteReg16(self.DirID, self.AddrMB, self.mbaAddrReg, 2)
 
    return self._Read16()


  def WriteConf(self, data):
    """ запись регистра конфигурации """
    svimb.WriteReg16(self.DirID, self.AddrMB, self.mbaAddrReg, 2)

    return self._Write16(data)


  def ReadIO(self):
    """ чтение регистра источников тока """
    svimb.WriteReg16(self.DirID, self.AddrMB, self.mbaAddrReg, 5)

    return self._Read8()


  def WriteIO(self ,data):
    """ запись регистра источников тока """
    svimb.WriteReg16(self.DirID, self.AddrMB, self.mbaAddrReg, 5)
    self._Write16(data & 0xff)


class CTechSwitch:
  """ управление входным коммутатором на отладочной плате милливольтметра\кондуктометра """
  # mbaSwitchReg - адрес управляющего регистра
  # mbaSwitch -    выполнить команду загруженую в регистр SwitchReg     
  
  def __init__(self, dirID, addrMB, confMB):
    """ dirID  - код направления на котором подключено устройство, поддерживающее MODBUS       
        addrMB - адрес устройства на шине MODBUS
        confMB - словарь с картой в регистровом\битовом поле MODBUS
    """
    self.DirID = dirID
    self.AddrMB = addrMB

    self.mbaSwitchReg = int(confMB["SwitchReg"])
    self.mbaSwitch = int(confMB["fSwitch"]) 


  def Set(self, pe2, pe6, pf1, pd5):
    """ атомарная установка битов PE2 PE6 PF1 PD5 (см. схему цифрового модуля)
        pe2, pe6, pf1, pd5  типа boolean или int (true - установить в 1, false - сбросить в 0) """
    sreg = 0 
    if pe2:  sreg |= (1 << 0)  
    if pe6:  sreg |= (1 << 1)   
    if pf1:  sreg |= (1 << 2)
    if pd5:  sreg |= (1 << 3)
    svimb.WriteReg16(self.DirID, self.AddrMB, self.mbaSwitchReg, sreg)
    svimb.WriteBit(self.DirID, self.AddrMB, self.mbaSwitch, 1)


class CMConv:
  """ масштабное преобразование вида Вых = K*(Вх - C0) """

  def __init__(self, K = 1.0, C0 = 0):
    self.K = K
    self.C0 = C0 

  def Convert(self, data):
    """ выполнить масштабное преобразование data """
    return (self.K * (data - self.C0))

#---
class CfmNaladka(QtGui.QMainWindow, Ui_fmNaladka):
  # fRec - флаг для блокировки рекурентного вызова closeEvent

  def __init__(self,vCE,Cfg1):
    super(CfmNaladka, self).__init__()      
    self.setupUi(self)

    self.fRec = False
    self.fStarted = False  # True - запущена СВП
    self.vCE=vCE
    self.actTech = QtGui.QAction("Настройка", self) 
    self.actTech.triggered.connect(self.on_muSetting)  
    self.menubar.addAction(self.actTech)

    self.tbPort.clicked.connect(self.on_tbPort_clicked)
    #self.spbPortNumber
    self.tbDataBase.clicked.connect(self.on_tbDataBase_clicked)
    self.tbSearchModuls.clicked.connect(self.on_tbSearchModuls_clicked)
    self.tbV.clicked.connect(self.on_tbV_clicked)
    self.tbT.clicked.connect(self.on_tbT_clicked)
    self.tbA.clicked.connect(self.on_tbA_clicked)
    self.tbP.clicked.connect(self.on_tbP_clicked)
    self.tbC.clicked.connect(self.on_tbC_clicked)
    self.tbADC.clicked.connect(self.on_tbADC_clicked)
    self.tbWinb.clicked.connect(self.on_tbWinb_clicked)

    self.show()
    b=2

  def on_tbPort_clicked(self):
      self.vCE.winPC.show()#


  def on_tbDataBase_clicked(self):
      self.vCE.winfmProgramming_1_0.show()

  def on_tbSearchModuls_clicked(self):
      self.vCE.winfmAllSearch_1_0.show()

  def on_tbV_clicked(self):
      self.vCE.winPV.show()#

  def on_tbT_clicked(self):
      self.vCE.winPT.show()#

  def on_tbA_clicked(self):
      self.vCE.winPAmper.show()#
      q=1

  def on_tbP_clicked(self):
      self.vCE.winPTP.show()#

  def on_tbC_clicked(self):
      self.vCE.winPCond.show()#

  def on_tbADC_clicked(self):
      self.vCE.winADC.show()#

  def on_tbWinb_clicked(self):
      self.vCE.winMBC.show()#



  def closeEvent(self, event):
    #print("closeEvent = {}".format(event))
    if self.fRec:
      # рекурентный вызов от closeAllWindows
      event.accept() 
    else:
      self.fRec = True
      app.closeAllWindows()
      event.accept() 


  def on_miPortCons(self):
    winPC.show()#


  def on_miMBCons(self):
    winMBC.show()#


  def on_miAD779x(self):
    winADC.show()#


  def on_miParV(self):
    winPV.show()#


  def on_miParT(self):
    winPT.show()#

  def on_miParCond(self):
    winPCond.show()#

  def on_miParTP(self):
    winPTP.show()#


  @QtCore.pyqtSlot(QtGui.QAction)  
  def on_muVInstr(self, source):
    source.data().ShowFP()


  def on_muSetting(self, source):
    winSetting.show()


  def on_Starttoggle(self):
    global vinstrD

    if not self.fStarted:
      # запуск СВП
      SVIstart()
      for vi in vinstrD: 
        tmpAct = self.muVInstr.addAction("{}".format(vi))
        if "obj" in vinstrD[vi]:  tmpAct.setData(vinstrD[vi]["obj"]) 
      self.fStarted = True
    self.tbStart.setDown(self.fStarted)
 #---  
class CfmPortCons(QtGui.QMainWindow, Ui_fmPortCons):
  def __init__(self,vCE):
    super(CfmPortCons, self).__init__() 
    self.setupUi(self)
    self.vCE=vCE
    self.fAddCRC = False # True - добавлять к введенным строкам CRC (MODBUS) 
 
    for i in range(0, 10):
      tmpAct = self.qmPort.addAction("COM{}".format(i))
      tmpAct.setData(i)
      tmpAct.setCheckable(True) 
      #self.menubar.addAction() 
   
    self.qmPort.triggered.connect(self.on_actPort)
    self.leHex.returnPressed.connect(self.on_HexEnter)  
    self.leASCII.returnPressed.connect(self.on_ASCIIEnter) 
    self.tbCRC.clicked.connect(self.on_CRCtoggle)

  def SendRecv(self, outArr, fHex, fCRC=False):
      """передача массива outArr (bytes\bytearray) через открытое направление 
         с логированием ответа в шестнадцатеричном (fHex = True) или в ASCII виде. 
         fCRC = True  - опциональная добавка CRC (MODBUS) """
      if (gActDirID):
        if (fCRC):
          crc = svimb.CRC16_MODBUS(outArr)
          sendArr = outArr + crc.to_bytes(2, byteorder = 'little')
        else:
          sendArr = outArr 

        if (fHex):
          self.teLog.append("<b>Tx(hex):</b> {}\n".format(BytesToHex(sendArr)))
        else:
          self.teLog.append("<b>Tx(ascii):</b> {}\n".format(sendArr)) 

        inArr = svimb.DirectSend(gActDirID, sendArr)

        if (fHex):
          self.teLog.append("<b>Rx(hex):</b> {}\n".format(BytesToHex(inArr))) 
        else:
          self.teLog.append("<b>Rx(ascii):</b> {}\n".format(inArr))  
       

  @QtCore.pyqtSlot(QtGui.QAction)      
  def on_actPort(self, source):
    global gActDirID
    global dirD
   
    #print("clicked {} [isChecked={}] ".format(source.data(), source.isChecked())) # ВРЕМЕННО !!!

    if not source.isChecked():
      # порт уже активирован ранее
      source.setChecked(True)
      return
   
    DirID = 0 
    try:
      DirID = svimb.CreateRTUdir(source.data()) 
    except:
      gActDirID = 0
      source.setChecked(False)
      print(sys.exc_info())   # TODO логирование

    if DirID:
      ddsc = {"cmnt": "COM{}".format(source.data())} # пока дескриптор направления чисто формальный
      dirD[DirID] = ddsc
      source.setText("COM{} [DirID={}]".format(source.data(), DirID))


  def on_HexEnter(self):
    outArr = bytes.fromhex(self.leHex.text())  
    #print(outArr)
    self.SendRecv(outArr, True, self.fAddCRC) 

    
  def on_ASCIIEnter(self):    
    outArr = self.leASCII.text().encode()  # TODO конвертер в ASCII - сейчас utf-8  
    self.SendRecv(outArr, False) 

  
  def on_CRCtoggle(self):
    self.fAddCRC = not self.fAddCRC
    self.tbCRC.setDown(self.fAddCRC) 

#---
class CfmMBCons(QtGui.QMainWindow, Ui_fmMBCons):
  # DirID    - активное направление обмена (пока извлекается первое из словаря дескрипторов dirD) TODO 
  # oldTitle - сохраненный заголовок окна

  def __init__(self,vCE, fdir):
    super(CfmMBCons, self).__init__() 
    self.setupUi(self)
    self.vCE=vCE
    self.oldTitle = self.windowTitle()
    self.lstRegs = [] # список именованных кортежей с реквизитами регистров
    self.lstMeas = [] # список именованных кортежей с реквизитами измерительных каналов
    self.RegData = 0; # значение введенное в поле leRegs 
    #--
    self.fname = fdir+'/test.pk'
    if os.path.isfile(self.fname):
      with open(self.fname, 'rb') as pfile:
        self.lstRegs = pickle.load(pfile)

    for reg in self.lstRegs:
      self.cbRegs.addItem("[{}] адрес={:04X}h".format(reg[0], reg[1]))  

    """#--
    for meas in Cfg["MODBUS RTU"]["Измеритель"]:
      for dk in meas:
        if  (dk == "канал04") or (dk == "канал03"):
          self.cbMeas.addItem("[адрес={}] {} [{:04X}h]".format(meas["адрес"], meas[dk][0], eval(meas[dk][1], {}, {})))    
    #-- """

    self.tbRegsAdd.clicked.connect(self.on_RegsAdd_toggle)
    self.tbRegsRd.clicked.connect(self.on_RegsRd_toggle) 
    self.tbRegsWr.clicked.connect(self.on_RegsWr_toggle)
    self.cbRegs.currentIndexChanged.connect(self.on_cbRegs_changed) 
    self.leRegs.editingFinished.connect(self.on_leRegsFinish)

  
  def showEvent(self, e):
    global dirD 

    tmpL = [k for k in dirD.keys()]
    try:
      self.DirID = tmpL[0]  # пока за активное направление принимается первое TODO
      self.setWindowTitle("{} [{}]".format(self.oldTitle, dirD[self.DirID]["cmnt"]))
    except:
      self.DirID = 0
      print(sys.exc_info())   # TODO логирование   
    super().showEvent(e)


  def closeEvent(self, event):
    with open(self.fname, 'wb') as pfile:
      pickle.dump(self.lstRegs, pfile)
    event.accept()

  
  def on_RegsAdd_toggle(self):
    self.vCE.dgReg.show(self.on_RegsAdd_result)


  def on_RegsAdd_result(self, res):
    """ метод вызывается напрямую из обработчика finished диалогового окна """     
    #print(res)
    if res:  
      self.lstRegs.append(regsAttr._make(res))
      self.cbRegs.addItem("[{}] адрес={:04X}h".format(res[0], res[1]))   

   
  def on_RegsRd_toggle(self):
    try:
      tmpT = svimb.ReadRegs16(self.DirID, self.lstRegs[self.cbRegs.currentIndex()].DevAddr, self.lstRegs[self.cbRegs.currentIndex()].RegAddr)
      self.leRegs.setText(str(tmpT[0]))
    except:
      self.leRegs.setText('?')
      print(sys.exc_info())   # TODO логирование


  def on_RegsWr_toggle(self):
    try:
      self.leRegs.clearFocus() 
      tmp = svimb.WriteReg16(self.DirID, self.lstRegs[self.cbRegs.currentIndex()].DevAddr, self.lstRegs[self.cbRegs.currentIndex()].RegAddr, self.RegData)
      self.leRegs.setText(str(tmp))
      self.RegData = tmp
    except:
      self.leRegs.setText('?')
      print(sys.exc_info())   # TODO логирование


  @QtCore.pyqtSlot(int)
  def on_cbRegs_changed(self, ind):
    self.leRegs.setText('')


  def on_leRegsFinish(self):
    try:
      #print(self.leRegs.text())   # ВРЕМЕННО !!!

      self.RegData = eval(self.leRegs.text(), {}, {})
    except:
      self.leRegs.setText(str(self.RegData))  
      print(sys.exc_info())  # TODO логирование 
    self.leRegs.clearFocus() 

#---
class CfmNewReg(QtGui.QDialog, Ui_dgNewReg):
  def __init__(self,vCE):
    super(CfmNewReg, self).__init__() 
    self.setupUi(self)
    self.vCE=vCE
    self.on_result = None # метод-приемник результатов, вызываемый по закрытию окна   
    self.DevAddr = 0
    self.RegAddr = 0 
    self.leDevAddr.setText(str(self.DevAddr))
    self.leRegAddr.setText(str(self.RegAddr))

    self.setWindowModality(QtCore.Qt.ApplicationModal)

    self.finished.connect(self.on_finished)
    self.leDevAddr.editingFinished.connect(self.on_DevAddrFinish) 
    self.leRegAddr.editingFinished.connect(self.on_RegAddrFinish)


  def show(self,vCE, on_res):
    """  on_res - метод-приемник кортежа (адрес измерителя, адрес регистра)
         если пользователь отменил ввод, в метод-приемник передается None  """ 
    self.on_result = on_res
    super(CfmNewReg, self).show()  


  def on_DevAddrFinish(self):
    try:
      self.DevAddr = eval(self.leDevAddr.text(), {}, {})
      #print("DevAddr={}".format(self.DevAddr)) 
    except:
      print(sys.exc_info())  # TODO логирование


  def on_RegAddrFinish(self):
    try:
      self.RegAddr = eval(self.leRegAddr.text(), {}, {})
      #print("RegAddr={}".format(self.RegAddr)) 
    except:
      print(sys.exc_info())  # TODO логирование


  @QtCore.pyqtSlot(int)
  def on_finished(self, res_code):
    if (res_code == QtGui.QDialog.Accepted):  self.on_result((self.DevAddr, self.RegAddr)) 
    else:                                     self.on_result(None) 

#---
class CfmAD779x(QtGui.QMainWindow, Ui_fmAD779x):
  # adc     - экземпляр класса CAD779x для абстрагирования технологического канала доступа к АЦП
  # t_switch- экземпляр класса CTechSwitch для абстрагирования управления входным коммутатором на отладочной плате милливольтметра\кондуктометра  
  # addrMB  - адрес устройства MODBUS, в котором расположен АЦП
  # aData   - регистр данных (выходной код) АЦП
  # aOffset - регистр смещения 0 АЦП
  # aScale  - регистр коэффициента АЦП
  # aMode   - регистр режима АЦП
  # aConf   - регистр конфигурации АЦП
  # aIO     - регистр источников тока
  # fAuto   - True - запущен автоматический опрос АЦП по таймеру
  # trAutoA - ID таймера автоматического опроса АЦП
  # mconv   - экземпляр класса CMConv для масштабирования выходного кода АЦП
  # DirID    - активное направление обмена (пока извлекается первое из словаря дескрипторов dirD) TODO 
  # oldTitle - сохраненный заголовок окна 

  def __init__(self,vCE):

    super(CfmAD779x, self).__init__() 
    self.setupUi(self) 
    self.vCE=vCE
    self.adc = None      # экземпляр создается во время вызова show() при выбранном направлении обмена (gActDirID)
    self.t_switch = None # экземпляр создается во время вызова show() при выбранном направлении обмена (gActDirID)
    self.addrMB = 1 
    self.aData = 0
    self.aOffset = 0
    self.aScale = 0
    self.aMode = 0x000a
    self.aConf = 0x0710 
    self.aIO = 0
    self.fAuto = False  
    self.trAutoA = None
    self.mconv = CMConv()
    self.lcdDataConv.setDigitCount(9)
    self.oldTitle = self.windowTitle()
 
    self.leAddrMB.setText(str(self.addrMB)) 
    self.UnPackMode(self.aMode, True)
    self.UnPackConf(self.aConf, True)
    self.UnPackIO(self.aIO, True)

    self.cbADC.currentIndexChanged.connect(self.on_cbADC_changed) 
    self.leAddrMB.editingFinished.connect(self.on_leAddrMBFinish)
    self.tbSwitch.clicked.connect(self.on_tbSwitch_toggle)

    self.tbDataA.clicked.connect(self.on_DataAuto_toggle)
    self.tbStatusRd.clicked.connect(self.on_StatusRd_toggle)
    self.tbIDRd.clicked.connect(self.on_IDRd_toggle)
    self.tbDataRd.clicked.connect(self.on_DataRd_toggle)
    self.tbOffsetRd.clicked.connect(self.on_OffsetRd_toggle)
    self.tbOffsetWr.clicked.connect(self.on_OffsetWr_toggle)
    self.leOffset.editingFinished.connect(self.on_leOffsetFinish)
    self.tbScaleRd.clicked.connect(self.on_ScaleRd_toggle)
    self.tbScaleWr.clicked.connect(self.on_ScaleWr_toggle)
    self.leScale.editingFinished.connect(self.on_leScaleFinish)
    self.tbConv.clicked.connect(self.on_tbConv_toggle)

    self.leMode.editingFinished.connect(self.on_leModeFinish)
    self.cbMode.currentIndexChanged.connect(self.on_cbMode_changed)
    self.cbClock.currentIndexChanged.connect(self.on_cbClock_changed)
    self.cbFadc.currentIndexChanged.connect(self.on_cbFadc_changed)
    self.tbModeRd.clicked.connect(self.on_ModeRd_toggle)
    self.tbModeWr.clicked.connect(self.on_ModeWr_toggle)

    self.leConf.editingFinished.connect(self.on_leConfFinish)
    self.cbChan.currentIndexChanged.connect(self.on_cbChan_changed)
    self.cbAmp.currentIndexChanged.connect(self.on_cbAmp_changed)
    self.cbRef.currentIndexChanged.connect(self.on_cbRef_changed)
    self.cbCode.currentIndexChanged.connect(self.on_cbCode_changed)
    self.cbBias.currentIndexChanged.connect(self.on_cbBias_changed)
    self.chBurnT.stateChanged.connect(self.on_chBurnT_changed)    
    self.chABias.stateChanged.connect(self.on_chABias_changed) 
    self.chAmp.stateChanged.connect(self.on_chAmp_changed)
    self.tbConfRd.clicked.connect(self.on_ConfRd_toggle)
    self.tbConfWr.clicked.connect(self.on_ConfWr_toggle)
 
    self.leIO.editingFinished.connect(self.on_leIOFinish)    
    self.cbJVal.currentIndexChanged.connect(self.on_cbJVal_changed)
    self.cbJDir.currentIndexChanged.connect(self.on_cbJDir_changed)
    self.tbIORd.clicked.connect(self.on_IORd_toggle)
    self.tbIOWr.clicked.connect(self.on_IOWr_toggle)


  def showEvent(self, e):
    global dirD 

    if (self.adc == None):
      tmpL = [k for k in dirD.keys()]
      try:
        self.DirID = tmpL[0]  # пока за активное направление принимается первое TODO
        self.setWindowTitle("{} [{}]".format(self.oldTitle, dirD[self.DirID]["cmnt"]))
        self.adc = CAD779x(self.DirID, self.addrMB, self.vCE.Cfg1["AD779x"], self.cbADC.currentIndex()) 
      except:
        self.DirID = 0
        print(sys.exc_info())   # TODO логирование

    #if ((self.t_switch == None) and gActDirID):
    #  self.t_switch = CTechSwitch(gActDirID, self.addrMB, Cfg["Макет мВ"])
    super().showEvent(e)


  def timerEvent(self, e):
    # print("timerEvent ID = {}".format(e.timerId())) # ВРЕМЕННО !!!
    self.tbDataRd.click()    
    self.UpdateConv()
    self.llData.update()
    print("aData = {} \t aConv = {}".format(self.aData, self.lcdDataConv.value()))    # ВРЕМЕННО !!!


  @QtCore.pyqtSlot(int)
  def on_cbADC_changed(self, ind):
    if ind:  self.adc.SelectAD7793()
    else:    self.adc.SelectAD7792()      


  def on_leAddrMBFinish(self):
    try:
      self.addrMB = eval(self.leAddrMB.text(), {}, {})
      self.adc.AddrMB = self.addrMB
    except:
      self.leAddrMB.setText(str(self.addrMB))   
    self.leAddrMB.clearFocus()    


  def on_tbSwitch_toggle(self):
    self.t_switch.Set(self.cbPE2.isChecked(), self.cbPE6.isChecked(), self.cbPF1.isChecked(), self.cbPD5.isChecked())


  def on_DataAuto_toggle(self):
    self.fAuto = not self.fAuto
    self.tbDataA.setDown(self.fAuto)    
    if (self.fAuto):
      self.trAutoA = self.startTimer(2000)  
      print("trAutoA = {}".format(self.trAutoA))      

    else:
      self.killTimer(self.trAutoA) 


  def on_StatusRd_toggle(self):
    try:
      self.llStatus.setText(str(self.adc.ReadStatus()))
    except:
      self.llStatus.setText('?')
      print(sys.exc_info())   # TODO логирование


  def on_IDRd_toggle(self):
    try:
      self.llID.setText(str(self.adc.ReadID()))
    except:
      self.llID.setText('?')
      print(sys.exc_info())   # TODO логирование


  def on_DataRd_toggle(self):  
    try:
      self.aData = self.adc.ReadData() # конвертер в unsigned включен в состав метода

      self.llData.setText(str(self.aData)) 
    except:
      self.llData.setText('?')
      print(sys.exc_info())   # TODO логирование


  def on_OffsetRd_toggle(self):  
    try:
      self.aOffset = self.adc.ReadOffset()
      # конвертер в unsigned    
      if self.cbADC.currentIndex(): 
        # 24 бита 
        self.leOffset.setText(str(int.from_bytes(self.aOffset.to_bytes(4, 'little', signed = True), 'little'))) 
      else:
        # 16 бит  
        self.leOffset.setText(str(int.from_bytes(self.aOffset.to_bytes(2, 'little', signed = True), 'little'))) 
    except:
      self.leOffset.setText('?') 
      print(sys.exc_info())   # TODO логирование


  def on_OffsetWr_toggle(self):  
    try:
      self.leOffset.clearFocus()
      self.adc.WriteOffset(self.aOffset)  
    except:
      self.leOffset.setText('?') 
      print(sys.exc_info())   # TODO логирование


  def on_leOffsetFinish(self):
    try:
      self.aOffset = eval(self.leOffset.text(), {}, {})
    except:
      self.leOffset.setText(str(self.aOffset))
      print(sys.exc_info())   # TODO логирование
    self.leOffset.clearFocus()    


  def on_ScaleRd_toggle(self):
    try:
      self.aScale = self.adc.ReadScale()
      # конвертер в unsigned   
      if self.cbADC.currentIndex(): 
        # 24 бита 
        self.leScale.setText(str(int.from_bytes(self.aScale.to_bytes(4, 'little', signed = True), 'little')))
      else:
        # 16 бит
        self.leScale.setText(str(int.from_bytes(self.aScale.to_bytes(2, 'little', signed = True), 'little')))     
    except:
      self.leScale.setText('?') 
      print(sys.exc_info())   # TODO логирование


  def on_ScaleWr_toggle(self):
    try:
      self.leScale.clearFocus()
      self.adc.WriteScale(self.aScale)  
    except: 
      self.leScale.setText('?')
      print(sys.exc_info())   # TODO логирование


  def on_leScaleFinish(self):
    try:
      self.aScale = eval(self.leScale.text(), {}, {})  
    except:
      self.leScale.setText(str(self.aScale)) 
      print(sys.exc_info())   # TODO логирование
    self.leScale.clearFocus()


  def on_tbConv_toggle(self):
    self.vCE.winConv.show(self.mconv)    


  def on_leModeFinish(self):
    try:
      self.aMode = int(self.leMode.text(), 16)
      self.UnPackMode(self.aMode) 
    except:
      self.leMode.setText("{:04X}".format(self.aMode))
      print(sys.exc_info())   # TODO логирование
    self.leMode.clearFocus()    


  @QtCore.pyqtSlot(int)
  def on_cbMode_changed(self, ind):
    self.PackMode(True)
 

  @QtCore.pyqtSlot(int)
  def on_cbClock_changed(self, ind):
    self.PackMode(True)
 

  @QtCore.pyqtSlot(int)
  def on_cbFadc_changed(self, ind):
    self.PackMode(True)


  def on_ModeRd_toggle(self):  
    try:
      self.UnPackMode(self.adc.ReadMode(), True)
    except:
      self.leMode.setText('?') 
      print(sys.exc_info())   # TODO логирование


  def on_ModeWr_toggle(self):
    try:
      self.leMode.clearFocus()
      self.adc.WriteMode(self.aMode)  
    except: 
      self.leMode.setText('?')
      print(sys.exc_info())   # TODO логирование


  def on_leConfFinish(self):
    try:
      self.aConf = int(self.leConf.text(), 16)
      self.UnPackConf(self.aConf) 
    except:
      self.leConf.setText("{:04X}".format(self.aConf))
      print(sys.exc_info())   # TODO логирование
    self.leConf.clearFocus()  


  @QtCore.pyqtSlot(int)
  def on_cbChan_changed(self, ind):
    self.PackConf(True)


  @QtCore.pyqtSlot(int)
  def on_cbAmp_changed(self, ind):
    self.PackConf(True) 
    self.chAmp.setEnabled(ind < 2)   
 

  @QtCore.pyqtSlot(int)
  def on_cbRef_changed(self, ind):
    self.PackConf(True)


  @QtCore.pyqtSlot(int)
  def on_cbCode_changed(self, ind):
    self.PackConf(True)


  @QtCore.pyqtSlot(int)
  def on_cbBias_changed(self, ind):
    self.PackConf(True)


  @QtCore.pyqtSlot(int) 
  def on_chBurnT_changed(self, ind):
    self.PackConf(True) 


  @QtCore.pyqtSlot(int) 
  def on_chABias_changed(self, ind): 
    self.PackConf(True) 


  @QtCore.pyqtSlot(int) 
  def on_chAmp_changed(self, ind):
    self.PackConf(True) 


  def on_ConfRd_toggle(self):  
    try:
      self.UnPackConf(self.adc.ReadConf(), True)
    except:
      self.leConf.setText('?') 
      print(sys.exc_info())   # TODO логирование


  def on_ConfWr_toggle(self):
    try:
      self.leConf.clearFocus()
      self.adc.WriteConf(self.aConf)  
    except: 
      self.leConf.setText('?')
      print(sys.exc_info())   # TODO логирование


  def on_leIOFinish(self):
    try:
      self.aIO = int(self.leIO.text(), 16)
      self.UnPackIO(self.aIO) 
    except:
      self.leIO.setText("{:04X}".format(self.aIO))
      print(sys.exc_info())   # TODO логирование
    self.leIO.clearFocus()
 
   
  @QtCore.pyqtSlot(int)
  def on_cbJVal_changed(self, ind):
    self.PackIO(True)


  @QtCore.pyqtSlot(int)
  def on_cbJDir_changed(self, ind):
    self.PackIO(True)


  def on_IORd_toggle(self):
    try:
      self.UnPackIO(self.adc.ReadIO(), True)
    except:
      self.leIO.setText('?') 
      print(sys.exc_info())   # TODO логирование


  def on_IOWr_toggle(self):
    try:
      self.leIO.clearFocus()
      self.adc.WriteIO(self.aIO)  
    except: 
      self.leIO.setText('?')
      print(sys.exc_info())   # TODO логирование


  def PackMode(self, fUpdate = False):
    """ метод возвращает код режима АЦП на основании текущего состояния вкладки 'Режим'
        если fUpdate = True, код режима переносится в aMode и отображается в leMode """
    res = 0
    res |= ((self.cbMode.currentIndex() & 0x07) << 13) | ((self.cbClock.currentIndex() & 0x03) << 6) 
    res |= (self.cbFadc.currentIndex() & 0x0f)
    if (fUpdate):
      self.aMode = res 
      self.leMode.setText("{:04X}".format(self.aMode))
      
    return res


  def UnPackMode(self, mode, fUpdate = False):
    """ метод выставляет состояние вкладки 'Режим' на основании кода режима АЦП (mode)
        если fUpdate = True, код режима (mode) переносится в aMode и отображается в leMode """  
    self.cbMode.setCurrentIndex((mode >> 13) & 0x07)
    self.cbClock.setCurrentIndex((mode >> 6) & 0x03)
    self.cbFadc.setCurrentIndex(mode & 0x0f)
    if (fUpdate):
      # конвертер в unsigned 
      self.aMode = int.from_bytes(mode.to_bytes(2, 'little', signed = True), 'little')
      self.leMode.setText("{:04X}".format(self.aMode))

  
  def PackConf(self, fUpdate = False):
    """ метод возвращает код конфигурации АЦП на основании текущего состояния вкладки 'Конфигурация'
        если fUpdate = True, код конфигурации переносится в aConf и отображается в leConf """
    res = 0
    res |= ((self.cbBias.currentIndex() & 0x03) << 14) | ((int(self.chBurnT.isChecked()) & 0x01) << 13)
    res |= ((self.cbCode.currentIndex() & 0x01) << 12) | ((int(self.chABias.isChecked()) & 0x01) << 11)
    res |= ((self.cbAmp.currentIndex() & 0x07) << 8) | ((self.cbRef.currentIndex() & 0x01) << 7)
    res |= ((int(self.chAmp.isChecked()) & 0x01) << 4) | (self.cbChan.currentIndex() & 0x07) 
    if (fUpdate):
      self.aConf = res 
      self.leConf.setText("{:04X}".format(self.aConf))
    return res 

  
  def UnPackConf(self, conf, fUpdate = False):
    """ метод выставляет состояние вкладки 'Конфигурация' на основании кода конфигурации АЦП
        если fUpdate = True, код конфигурации переносится в aConf и отображается в leConf """  
    self.cbBias.setCurrentIndex((conf >> 14) & 0x03)
    self.chBurnT.setChecked(bool(conf & (1 << 13))) 
    self.cbCode.setCurrentIndex((conf >> 12) & 0x01)
    self.chABias.setChecked(bool(conf & (1 << 11)))
    tmp = (conf >> 8) & 0x07 
    self.cbAmp.setCurrentIndex(tmp) 
    self.chAmp.setEnabled(tmp < 2)   
    self.cbRef.setCurrentIndex((conf >> 7) & 0x01) 
    self.chAmp.setChecked(bool(conf & (1 << 4)))
    self.cbChan.setCurrentIndex(conf & 0x07)
    if (fUpdate):
      # конвертер в unsigned 
      self.aConf = int.from_bytes(conf.to_bytes(2, 'little', signed = True), 'little')
      self.leConf.setText("{:04X}".format(self.aConf))


  def PackIO(self, fUpdate = False):
    """ метод возвращает управляющий код источников тока АЦП (IO) на основании текущего состояния вкладки 'Источники тока'
        если fUpdate = True, код переносится в aIO и отображается в leIO """
    res = 0
    res |= ((self.cbJDir.currentIndex() & 0x03) << 2) | (self.cbJVal.currentIndex() & 0x03)
    if (fUpdate):
      self.aIO = res 
      self.leIO.setText("{:02X}".format(self.aIO))
    return res 


  def UnPackIO(self, cio, fUpdate = False):
    """ метод выставляет состояние вкладки 'Источники тока' на основании управляющего кода источников тока АЦП
        если fUpdate = True, код переносится в aIO и отображается в leIO """ 
    self.cbJDir.setCurrentIndex((cio >> 2) & 0x03)
    self.cbJVal.setCurrentIndex(cio & 0x03)
    if (fUpdate):
      self.aIO = cio 
      self.leIO.setText("{:02X}".format(self.aIO))


  def UpdateConv(self):
    """ пересчитать и обновить индикатор масштабированного вывода   """
    self.lcdDataConv.display(self.mconv.Convert(self.aData))

#---
class CfmVPar(QtGui.QMainWindow, Ui_fmVPar): 
  # addrMB   - адрес милливольтметра в сети MODBUS
  # scanS    - структура для разбора технологического скана
  # ntScan   - namedtuple для упрощения именования полей на выходе scanF
  # scan     - экземпляр ntScan c данными последнего скана 
  # ADCF     - выход фильтра отсчетов АЦП 
  # mVF      - выход милливольтметра на основании отфильтрованных остчетов АЦП
  # fAuto    - True - запущен автоматическое сканирование по таймеру
  # trAutoScan - ID таймера сканирования
  # filtr    - экземпляр filtrP для фильтрации отсчетов АЦП 
  # wSize    - размер окна filtrP (параметр filtrP)
  # min_cntS - минимально приемлимое значение оставшихся в окне сэмплов для формирования результата (параметр filtrP)
  # раскладка карты MODBUS для параметризации милливольтметра:
  #  mba_zcntIgn   -  кол-во игнорируемых отсчетов с АЦП после переключения ключа 
  #  mba_zcntZero  -  кол-во отсчетов АЦП, усредняемых для получения ноля аналогового тракта 
  #  mba_mcntMeas  -  кол-во отсчетов АЦП, снимаемых в режиме штатных измерений до следующей калибровки ноля 
  #  mba_ZeroA32   -  периодически измеряемый ноль аналогового тракта
  #  mba_mK32      -  коэф-т пересчета кодов АЦП в [В]  - на эту величину ДЕЛЯТСЯ коды 
  #  mba_f24b      -  управляющий флаг - 1 - работа с 24х разрядным АЦП
  #  mba_fZeroComp -  управляющий флаг - 1 - режим автоматической компенсации нуля
  #  mba_tsStart   -  стартовый адрес скана в регистровом поле MODBUS
  #  mbq_tsQnt     -  кол-во регистров MODBUS в технологическом скане
  #  DirID    - активное направление обмена (пока извлекается первое из словаря дескрипторов dirD) TODO 
  #  oldTitle - сохраненный заголовок окна

  def __init__(self,vCE, confMB):
    """ confMB - словарь с картой в регистровом\битовом поле MODBUS """
       
    super(CfmVPar, self).__init__()
    self.setupUi(self)

    self.vCE=vCE
    self.addrMB = 1
    self.zcntIgn = 0
    self.zcntZero = 1
    self.mcntMeas = 1000
    self.ZeroA = 0
    self.mK = 1
    self.fAuto = False
    self.trAutoScan = None
    self.scan = None
    self.ADCF = 0
    self.mVF = 0
    self.oldTitle = self.windowTitle()
    self.lcdDataConv.setDigitCount(9)
    self.lcdDataConvF.setDigitCount(9)
    self.lcdDataFilter.setDigitCount(9)
    self.wSize = 30
    self.min_cntS = 20
    self.CountFilter_2=1
    self.CurrCountFilter_2=1
    self.U_Sum_Filter_2=0
    self.U_Filter_2=0
    self.filtr = filtrP(self.wSize, self.min_cntS)
    self.filtr1 = filtrP(self.wSize, self.min_cntS)

    self.mba_zcntIgn = int(confMB["zcntIgn"])
    self.mba_zcntZero = int(confMB["zcntZero"])
    self.mba_mcntMeas = int(confMB["mcntMeas"])
    self.mba_ZeroA32 = int(confMB["ZeroA32"])
    self.mba_mK32 = int(confMB["mK32"])
    self.mba_f24b = int(confMB["f24b"])
    self.mba_fZeroComp = int(confMB["fZeroComp"])
    self.scanS = Struct(confMB["techStr"])
    self.ntScan = namedtuple('ntScan', confMB["techLst"])
    self.mba_tsStart = int(confMB["techStart"])
    self.mbq_tsQnt = int(confMB["techQnt"])

    self.leAddrMB.setText(str(self.addrMB)) 
    self.leIgn.setText(str(self.zcntIgn))
    self.leZero.setText(str(self.zcntZero))
    self.leMeas.setText(str(self.mcntMeas))
    self.leZeroA.setText(str(self.ZeroA))
    self.lemK.setText(str(self.mK))
    self.leWSize.setText(str(self.wSize))
    self.leMinCntS.setText(str(self.min_cntS))

    self.actConf.triggered.connect(self.on_muConf_toggle)
    self.menubar.addAction(self.actConf)

    self.leAddrMB.editingFinished.connect(self.on_leAddrMBFinish)

    self.leIgn.editingFinished.connect(self.on_leIgnFinish)
    self.tbIgnRd.clicked.connect(self.on_IgnRd_toggle)
    self.tbIgnWr.clicked.connect(self.on_IgnWr_toggle)
    self.leZero.editingFinished.connect(self.on_leZeroFinish)
    self.tbZeroRd.clicked.connect(self.on_ZeroRd_toggle)
    self.tbZeroWr.clicked.connect(self.on_ZeroWr_toggle)
    self.leMeas.editingFinished.connect(self.on_leMeasFinish)
    self.tbMeasRd.clicked.connect(self.on_MeasRd_toggle)
    self.tbMeasWr.clicked.connect(self.on_MeasWr_toggle)
    self.lemK.editingFinished.connect(self.on_lemKFinish)
    self.tbmKRd.clicked.connect(self.on_mKRd_toggle)
    self.tbmKWr.clicked.connect(self.on_mKWr_toggle) 
    self.leZeroA.editingFinished.connect(self.on_leZeroAFinish)
    self.tbZeroAWr.clicked.connect(self.on_ZeroAWr_toggle)
    self.tbSaveSettingV.clicked.connect(self.on_tbSaveSettingV_toggle)

    self.ch24b.stateChanged.connect(self.on_ch24b_changed)
    self.chZeroComp.stateChanged.connect(self.on_chZeroComp_changed)
    self.tbScan.clicked.connect(self.on_Scan_toggle)
    self.tbAutoScan.clicked.connect(self.on_AutoScan_toggle)

    self.leWSize.editingFinished.connect(self.on_leWSizeFinish)
    self.leMinCntS.editingFinished.connect(self.on_leMinCntSFinish)


  def showEvent(self, e):
    global dirD 

    tmpL = [k for k in dirD.keys()]
    try:
      self.DirID = tmpL[0]  # пока за активное направление принимается первое TODO
      self.setWindowTitle("{} [{}]".format(self.oldTitle, dirD[self.DirID]["cmnt"]))
    except:
      self.DirID = 0
      print(sys.exc_info())   # TODO логирование
    super().showEvent(e)

  
  def timerEvent(self, e):
    # print("timerEvent ID = {}".format(e.timerId())) # ВРЕМЕННО !!!
    self.tbScan.click()    

    self.llData.update()
    self.leZeroA.update()
    if (self.scan):
      self.ADCF = self.filtr.newS(self.scan.ADCcode) 
      self.mVF = (self.ADCF - self.scan.ZeroA) / self.mK  
      self.llDataF.setText(str(self.ADCF))
      self.llCntS.setText(str(self.filtr.cntS))
      self.llNumPass.setText(str(self.filtr.NumPass))
      self.lcdDataConvF.display(self.mVF)
      ####################################
      if(self.CurrCountFilter_2<=self.CountFilter_2):
           self.U_Sum_Filter_2=self.U_Sum_Filter_2+self.scan.mV
           self.CurrCountFilter_2=self.CurrCountFilter_2+1
      if(self.CurrCountFilter_2>=self.CountFilter_2):
           self.U_Filter_2=self.U_Sum_Filter_2/self.CurrCountFilter_2
           self.U_Sum_Filter_2=0
           self.CurrCountFilter_2=0
      self.lcdDataFilter.display(self.U_Filter_2)
      #####################################
      self.llDataF.update()
      self.llCntS.update()  
      self.llNumPass.update() 
      #print("adc = {} \t mV = {} \t adcF = {} \t mVF = {}".format(self.scan.ADCcode, self.scan.mV, self.ADCF, self.mVF))               
      print("adc = {} \t adcF = {} \t mVF = {}".format(self.scan.ADCcode, self.ADCF, self.U_Filter_2))               


  def on_muConf_toggle(self):
    self.vCE.winCV.show(self.DirID, self.addrMB)


  def on_leAddrMBFinish(self):
    try:
      self.addrMB = eval(self.leAddrMB.text(), {}, {})
    except:
      print(sys.exc_info())   # TODO логирование
    self.leAddrMB.setText(str(self.addrMB))
    self.leAddrMB.clearFocus()    

  def on_tbSaveSettingV_toggle(self):
    try:
      self.CountFilter_2 = eval(self.leCounts.text(), {}, {})
    except:
     q=0
    qq=0

  def on_leIgnFinish(self):
    try:
      self.zcntIgn = eval(self.leIgn.text(), {}, {})
    except:
      print(sys.exc_info())   # TODO логирование
    self.leIgn.setText(str(self.zcntIgn))
    self.leIgn.clearFocus()  


  def on_IgnRd_toggle(self):
    try: 
      tmpL = svimb.ReadRegs16(self.DirID , self.addrMB, self.mba_zcntIgn, 1)
       # конвертер в unsigned 
      self.zcntIgn = int.from_bytes(tmpL[0].to_bytes(2, 'little', signed = True), 'little')
      self.leIgn.setText(str(self.zcntIgn))
    except:
      self.leIgn.setText('?')
      print(sys.exc_info())   # TODO логирование 


  def on_IgnWr_toggle(self):
    try:
      self.leIgn.clearFocus()
      svimb.WriteReg16(self.DirID, self.addrMB, self.mba_zcntIgn, self.zcntIgn & 0xffff) 
    except:
      self.leIgn.setText('?')
      print(sys.exc_info())   # TODO логирование 


  def on_leZeroFinish(self):
    try:
      self.zcntZero = eval(self.leZero.text(), {}, {})
    except:
      print(sys.exc_info())   # TODO логирование
    self.leZero.setText(str(self.zcntZero))
    self.leZero.clearFocus()  


  def on_ZeroRd_toggle(self):
    try:
      tmpL = svimb.ReadRegs16(self.DirID, self.addrMB, self.mba_zcntZero, 1)
      # конвертер в unsigned 
      self.zcntZero = int.from_bytes(tmpL[0].to_bytes(2, 'little', signed = True), 'little')
      self.leZero.setText(str(self.zcntZero))
    except:
      self.leZero.setText('?')
      print(sys.exc_info())   # TODO логирование 


  def on_ZeroWr_toggle(self):
    try:
      self.leZero.clearFocus()
      svimb.WriteReg16(self.DirID, self.addrMB, self.mba_zcntZero, self.zcntZero & 0xffff)
    except:
      self.leZero.setText('?')
      print(sys.exc_info())   # TODO логирование 


  def on_leMeasFinish(self):
    try:
      self.mcntMeas = eval(self.leMeas.text(), {}, {})
    except:
      print(sys.exc_info())   # TODO логирование
    self.leMeas.setText(str(self.mcntMeas))
    self.leMeas.clearFocus()


  def on_MeasRd_toggle(self): 
     try:
       tmpL = svimb.ReadRegs16(self.DirID, self.addrMB, self.mba_mcntMeas, 1)
       # конвертер в unsigned 
       self.mcntMeas = int.from_bytes(tmpL[0].to_bytes(2, 'little', signed = True), 'little')
       self.leMeas.setText(str(self.mcntMeas))
     except:
      self.leMeas.setText('?')
      print(sys.exc_info())   # TODO логирование 

    
  def  on_MeasWr_toggle(self):
    try:
      self.leMeas.clearFocus()
      svimb.WriteReg16(self.DirID, self.addrMB, self.mba_mcntMeas, self.mcntMeas & 0xffff)
    except:
      self.leMeas.setText('?')
      print(sys.exc_info())   # TODO логирование 


  def on_lemKFinish(self):
    try:
      self.mK = eval(self.lemK.text(), {}, {})
    except:
      print(sys.exc_info())   # TODO логирование
    self.lemK.setText(str(self.mK))
    self.lemK.clearFocus()


  def on_mKRd_toggle(self):
    try:
      (rlow, rhigh) = svimb.ReadRegs16(self.DirID, self.addrMB, self.mba_mK32, 2)
      self.mK = ToSig32(rlow, rhigh)
      self.lemK.setText(str(self.mK))
    except:
      self.lemK.setText('?')
      print(sys.exc_info())   # TODO логирование 


  def on_mKWr_toggle(self):
    try:
      self.lemK.clearFocus()
      svimb.WriteReg16(self.DirID, self.addrMB, self.mba_mK32, self.mK & 0xffff)
      svimb.WriteReg16(self.DirID, self.addrMB, self.mba_mK32+1, (self.mK & 0xffff0000) >> 16)
    except:
      self.lemK.setText('?')
      print(sys.exc_info())   # TODO логирование 

 
  def on_leZeroAFinish(self):
    try:
      self.ZeroA = eval(self.leZeroA.text(), {}, {})
    except:
      print(sys.exc_info())   # TODO логирование
    self.leZeroA.setText(str(self.ZeroA))
    self.leZeroA.clearFocus()


  def on_ZeroAWr_toggle(self):
    try:
      self.leZeroA.clearFocus()
      svimb.WriteReg16(self.DirID, self.addrMB, self.mba_ZeroA32, self.ZeroA & 0xffff)
      svimb.WriteReg16(self.DirID, self.addrMB, self.mba_ZeroA32+1, (self.ZeroA & 0xffff0000) >> 16)
    except:
      self.leZeroA.setText('?')
      print(sys.exc_info())   # TODO логирование 
 
  @QtCore.pyqtSlot(int) 
  def on_ch24b_changed(self, ind):
    try:
      svimb.WriteBit(self.DirID, self.addrMB, self.mba_f24b, self.ch24b.isChecked())
    except:
      self.ch24b.setCheckState(QtCore.Qt.PartiallyChecked)
      print(sys.exc_info())   # TODO логирование 


  @QtCore.pyqtSlot(int)
  def on_chZeroComp_changed(self, ind):
    try:
      svimb.WriteBit(self.DirID, self.addrMB, self.mba_fZeroComp, self.chZeroComp.isChecked())
    except:
      self.chZeroComp.setCheckState(QtCore.Qt.PartiallyChecked)
      print(sys.exc_info())   # TODO логирование  


  def on_Scan_toggle(self):
    try:
      tmpL = svimb.ReadRegs16(self.DirID, self.addrMB, self.mba_tsStart, self.mbq_tsQnt)
      #print(tmpL)               
      ba = bytearray()
      for reg in tmpL:
        ba += reg.to_bytes(2, 'little', signed = True)
      #print("ba={}".format(ba)) 
      self.scan = self.ntScan._make(self.scanS.unpack(ba))
      #print(self.scan)               
      self.llData.setText(str(self.scan.ADCcode)) 
      self.leZeroA.setText(str(self.scan.ZeroA))
      self.lcdDataConv.display(self.scan.mV)
    except:
      print(sys.exc_info())   # TODO логирование 


  def on_AutoScan_toggle(self):
    self.fAuto = not self.fAuto
    self.tbAutoScan.setDown(self.fAuto)    
    if (self.fAuto):
      self.trAutoScan = self.startTimer(1000)  
      print("trAutoScan = {}".format(self.trAutoScan))      

    else:
      self.killTimer(self.trAutoScan) 


  def on_leWSizeFinish(self):
    try:
      self.wSize = eval(self.leWSize.text(), {}, {})
      self.filtr = filtrP(self.wSize, self.min_cntS) 
    except:
      print(sys.exc_info())   # TODO логирование
    self.leWSize.setText(str(self.wSize))
    self.leWSize.clearFocus()


  def on_leMinCntSFinish(self):
    try:
      self.min_cntS = eval(self.leMinCntS.text(), {}, {})
      self.filtr = filtrP(self.wSize, self.min_cntS) 
    except:
      print(sys.exc_info())   # TODO логирование
    self.leMinCntS.setText(str(self.min_cntS))
    self.leMinCntS.clearFocus()

#---
class CfmVConf(QtGui.QMainWindow, Ui_fmVConf): 
  # DirID - активное направление MODBUS 
  # addrMB - адрес конфигурируемого милливольтметра на направлении DirID
  # wnCaption - заголовок окна
  
  # новые параметры в редактируемой копии конфигурации милливольтметра
  #  n_addrMB - адрес в сети MODBUS
  #  n_thrAT  - предельно допустимая распределенная пауза в приемном пакете 
  #  n_ZeroA  - cмещение нуля(32р) [unsigned]
  #  n_mK     - коэф-т пересчета кодов АЦП в [В] (32р) [signed]
  #  n_ADC_mode - загружаемое значение в регистр mode AЦП
  #  n_ADC_conf - загружаемое значение в регистр configuration AЦП
  #  n_ADC_IO   - загружаемое значение в регистр IO AЦП (младший байт)
  #  n_SerNum   - серийный номер узла

  # раскладка карты MODBUS для параметризации милливольтметра:
  #  mbv_ZeroA32    - cмещение нуля(32р) в SysVar (параметр используется в рилтайм рассчетах)
  #  mbv_mK32       - коэф-т пересчета кодов АЦП в [В] (32р) в SysVar (параметр используется в рилтайм рассчетах)
  #  fUpdConf       - дискретная команда на запись редактируемой копии в энергонезависимую память
  # следующие поля заданы в виде регистровых смещений относительно Base
  #  BaseMain      - начало активной конфигурации (доступна только для чтения)
  #  BaseCopy      - начало редактируемой копии конфигурации
  #  offs_addr     - адрес данного устройства в сети MODBUS 
  #  offs_thrAT    - предельно допустимая распределенная пауза в приемном пакете 
  #  offs_ZeroA32  - cмещение нуля(32р)
  #  offs_mK32     - коэф-т пересчета кодов АЦП в [В] (32р)
  #  offs_ADC_mode - загружаемое значение в регистр mode AЦП
  #  offs_ADC_conf - загружаемое значение в регистр configuration AЦП
  #  offs_ADC_IO   - загружаемое значение в регистр IO AЦП (младший байт)
  #  offs_SerNum   - серийный номер узла 

  def __init__(self,vCE, confMB, mbv_ZeroA32, mbv_mK32):
    """ confMB - словарь с картой в регистровом\битовом поле MODBUS 
        mbv_ZeroA32, mbv_mK32 - адреса в структуре системных переманных SysVar """
       
    super(CfmVConf, self).__init__()
    self.setupUi(self)
    self.vCE=vCE
    self.addrMB = 1
    self.wnCaption = self.windowTitle()
       
    self.mbv_ZeroA32 = mbv_ZeroA32
    self.mbv_mK32 = mbv_mK32
    self.fUpdConf = int(confMB["fUpdConf"])
    self.BaseMain = int(confMB["BaseMain"])
    self.BaseCopy = int(confMB["BaseCopy"])
    self.offs_addr = int(confMB["offs_addr"])
    self.offs_thrAT = int(confMB["offs_thrAT"])
    self.offs_ZeroA32 = int(confMB["offs_ZeroA32"])
    self.offs_mK32 = int(confMB["offs_mK32"])
    self.offs_ADC_mode = int(confMB["offs_ADC_mode"])
    self.offs_ADC_conf = int(confMB["offs_ADC_conf"])
    self.offs_ADC_IO = int(confMB["offs_ADC_IO"])
    self.offs_SerNum = int(confMB["offs_SerNum"])
    try:
      self.offs_Descr = int(confMB["offs_Descr"])
      self.offs_TypeID = int(confMB["offs_TypeID"])
    except:q=0

    self.leAddrMB.editingFinished.connect(self.on_leAddrMBFinished)
    self.tbAddrMBRd.clicked.connect(self.on_tbAddrMBRd_toggle)
    self.tbAddrMBWr.clicked.connect(self.on_tbAddrMBWr_toggle)
    self.lethrAT.editingFinished.connect(self.on_lethrATFinished)
    self.tbthrATRd.clicked.connect(self.on_tbthrATRd_toggle)
    self.tbthrATWr.clicked.connect(self.on_tbthrATWr_toggle)
    self.leZeroA.editingFinished.connect(self.on_leZeroAFinished)
    self.tbZeroARdVar.clicked.connect(self.on_tbZeroARdVar_toggle)
    self.tbZeroARd.clicked.connect(self.on_tbZeroARd_toggle)
    self.tbZeroAWr.clicked.connect(self.on_tbZeroAWr_toggle)
    self.lemK.editingFinished.connect(self.on_lemKFinished)
    self.tbmKRdVar.clicked.connect(self.on_tbmKRdVar_toggle)
    self.tbmKRd.clicked.connect(self.on_tbmKRd_toggle)
    self.tbmKWr.clicked.connect(self.on_tbmKWr_toggle)    
    self.leMode.editingFinished.connect(self.on_leModeFinished)
    self.tbModeRd.clicked.connect(self.on_tbModeRd_toggle)
    self.tbModeWr.clicked.connect(self.on_tbModeWr_toggle)
    self.leConf.editingFinished.connect(self.on_leConfFinished)
    self.tbConfRd.clicked.connect(self.on_tbConfRd_toggle)
    self.tbConfWr.clicked.connect(self.on_tbConfWr_toggle)
    self.leIO.editingFinished.connect(self.on_leIOFinished)
    self.tbIORd.clicked.connect(self.on_tbIORd_toggle)
    self.tbIOWr.clicked.connect(self.on_tbIOWr_toggle)
    self.leSerNum.editingFinished.connect(self.on_leSerNumFinished)
    self.tbSerNumRd.clicked.connect(self.on_tbSerNumRd_toggle)
    self.tbSerNumWr.clicked.connect(self.on_tbSerNumWr_toggle)

    self.teDescribe.cursorPositionChanged.connect(self.on_teDescribeFinished)
    self.tbDescribeRd.clicked.connect(self.on_tbDescribeRd_toggle)
    self.tbDescribeWr.clicked.connect(self.on_tbDescribemWr_toggle)
    self.leTypeID.editingFinished.connect(self.on_leTypeIDFinished)
    self.tbTypeIDRd.clicked.connect(self.on_tbTypeIDRd_toggle)
    self.tbTypeIDWr.clicked.connect(self.on_tbTypeIDWr_toggle)


    self.tbSave.clicked.connect(self.on_tbSave_toggle)


  def show(self, DirID, addrMB):
    """ DirID - активное направление MODBUS 
        addrMB - адрес конфигурируемого милливольтметра на направлении DirID """
    self.DirID = DirID
    self.addrMB = addrMB
    self.setWindowTitle(self.wnCaption + " [{:02X}h]".format(self.addrMB))
    super().show()


  def on_leAddrMBFinished(self):
    try:
      self.n_addrMB = eval(self.leAddrMB.text(), {}, {})
    except:
      self.leAddrMB.setText(str(ToUns16(self.n_addrMB)))
      print(sys.exc_info())   # TODO логирование
    self.leAddrMB.clearFocus()    


  def on_tbAddrMBRd_toggle(self):
    try:
      tmpT = svimb.ReadRegs16(self.DirID, self.addrMB, self.BaseCopy + self.offs_addr, 1) 
      self.n_addrMB = tmpT[0]
      self.leAddrMB.setText(str(ToUns16(self.n_addrMB)))    
    except:
      self.leAddrMB.setText('?') 
      print(sys.exc_info())   # TODO логирование


  def on_tbAddrMBWr_toggle(self):
    try:
      self.leAddrMB.clearFocus() 
      self.n_addrMB = svimb.WriteReg16(self.DirID, self.addrMB, self.BaseCopy + self.offs_addr, self.n_addrMB)
      self.leAddrMB.setText(str(ToUns16(self.n_addrMB)))
    except:
      self.leAddrMB.setText('?')
      print(sys.exc_info())   # TODO логирование
    

  def on_lethrATFinished(self):
    try:
      self.n_thrAT = eval(self.lethrAT.text(), {}, {})
    except:
      self.lethrAT.setText(str(ToUns16(self.n_thrAT)))
      print(sys.exc_info())   # TODO логирование
    self.lethrAT.clearFocus() 


  def on_tbthrATRd_toggle(self):
    try:
      tmpT = svimb.ReadRegs16(self.DirID, self.addrMB, self.BaseCopy + self.offs_thrAT, 1) 
      self.n_thrAT = tmpT[0]
      self.lethrAT.setText(str(ToUns16(self.n_thrAT)))    
    except:
      self.lethrAT.setText('?') 
      print(sys.exc_info())   # TODO логирование


  def on_tbthrATWr_toggle(self):
    try:
      self.lethrAT.clearFocus() 
      self.n_thrAT = svimb.WriteReg16(self.DirID, self.addrMB, self.BaseCopy + self.offs_thrAT, self.n_thrAT)
      self.lethrAT.setText(str(ToUns16(self.n_thrAT))) 
    except:
      self.lethrAT.setText('?')
      print(sys.exc_info())   # TODO логирование

 
  def on_leZeroAFinished(self):
    try:
      self.n_ZeroA = eval(self.leZeroA.text(), {}, {})
    except:
      self.leZeroA.setText(str(self.n_ZeroA))
      print(sys.exc_info())   # TODO логирование
    self.leZeroA.clearFocus() 

  
  def on_tbZeroARdVar_toggle(self):
    try:
      (rlow, rhigh) = svimb.ReadRegs16(self.DirID, self.addrMB, self.mbv_ZeroA32, 2)
      self.n_ZeroA = ToUns32(rlow, rhigh)
      self.leZeroA.setText(str(self.n_ZeroA ))    
    except:
      self.leZeroA.setText('?') 
      print(sys.exc_info())   # TODO логирование


  def on_tbZeroARd_toggle(self):
    try:
      (rlow, rhigh) = svimb.ReadRegs16(self.DirID, self.addrMB, self.BaseCopy + self.offs_ZeroA32, 2)
      self.n_ZeroA = ToUns32(rlow, rhigh)
      self.leZeroA.setText(str(self.n_ZeroA ))    
    except:
      self.leZeroA.setText('?') 
      print(sys.exc_info())   # TODO логирование


  def on_tbZeroAWr_toggle(self):
    try:
      self.leZeroA.clearFocus()
      svimb.WriteReg16(self.DirID, self.addrMB, self.BaseCopy + self.offs_ZeroA32, self.n_ZeroA & 0xffff)
      svimb.WriteReg16(self.DirID, self.addrMB, self.BaseCopy + self.offs_ZeroA32 + 1, (self.n_ZeroA & 0xffff0000) >> 16)
    except:
      self.leZeroA.setText('?')
      print(sys.exc_info())   # TODO логирование 


  def on_lemKFinished(self):
    try:
      self.n_mK = eval(self.lemK.text(), {}, {})
    except:
      self.lemK.setText(str(self.n_mK))
      print(sys.exc_info())   # TODO логирование
    self.lemK.clearFocus() 


  def on_tbmKRdVar_toggle(self):
    try:
      (rlow, rhigh) = svimb.ReadRegs16(self.DirID, self.addrMB, self.mbv_mK32, 2)
      self.n_mK = ToSig32(rlow, rhigh)
      self.lemK.setText(str(self.n_mK))    
    except:
      self.lemK.setText('?') 
      print(sys.exc_info())   # TODO логирование


  def on_tbmKRd_toggle(self):
    try:
      (rlow, rhigh) = svimb.ReadRegs16(self.DirID, self.addrMB, self.BaseCopy + self.offs_mK32, 2)
      self.n_mK = ToSig32(rlow, rhigh)
      self.lemK.setText(str(self.n_mK))    
    except:
      self.lemK.setText('?') 
      print(sys.exc_info())   # TODO логирование


  def on_tbmKWr_toggle(self):
    try:
      self.lemK.clearFocus()
      svimb.WriteReg16(self.DirID, self.addrMB, self.BaseCopy + self.offs_mK32, self.n_mK & 0xffff)
      svimb.WriteReg16(self.DirID, self.addrMB, self.BaseCopy + self.offs_mK32 + 1, (self.n_mK & 0xffff0000) >> 16)
    except:
      self.lemK.setText('?')
      print(sys.exc_info())   # TODO логирование


  def on_leModeFinished(self):
    try:
      self.n_ADC_mode = int(self.leMode.text(), 16)
    except:
      self.leMode.setText("{:04X}".format(self.n_ADC_mode))
      print(sys.exc_info())   # TODO логирование
    self.leMode.clearFocus()  


  def on_tbModeRd_toggle(self):
    try:
      tmpT = svimb.ReadRegs16(self.DirID, self.addrMB, self.BaseCopy + self.offs_ADC_mode, 1) 
      self.n_ADC_mode = ToUns16(tmpT[0])
      self.leMode.setText("{:04X}".format(self.n_ADC_mode))    
    except:
      self.leMode.setText('?') 
      print(sys.exc_info())   # TODO логирование


  def on_tbModeWr_toggle(self):
    try:
      self.leMode.clearFocus() 
      self.n_ADC_mode = ToUns16(svimb.WriteReg16(self.DirID, self.addrMB, self.BaseCopy + self.offs_ADC_mode, self.n_ADC_mode))
      self.leMode.setText("{:04X}".format(self.n_ADC_mode)) 
    except:
      self.leMode.setText('?')
      print(sys.exc_info())   # TODO логирование
 

  def on_leConfFinished(self):
    try:
      self.n_ADC_conf = int(self.leConf.text(), 16)
    except:
      self.leConf.setText("{:04X}".format(self.n_ADC_conf))
      print(sys.exc_info())   # TODO логирование
    self.leConf.clearFocus() 


  def on_tbConfRd_toggle(self):
    try:
      tmpT = svimb.ReadRegs16(self.DirID, self.addrMB, self.BaseCopy + self.offs_ADC_conf, 1) 
      self.n_ADC_conf = ToUns16(tmpT[0])
      self.leConf.setText("{:04X}".format(self.n_ADC_conf))    
    except:
      self.leConf.setText('?') 
      print(sys.exc_info())   # TODO логирование


  def on_tbConfWr_toggle(self):
    try:
      self.leConf.clearFocus() 
      self.n_ADC_conf = ToUns16(svimb.WriteReg16(self.DirID, self.addrMB, self.BaseCopy + self.offs_ADC_conf, self.n_ADC_conf))
      self.leConf.setText("{:04X}".format(self.n_ADC_conf)) 
    except:
      self.leConf.setText('?')
      print(sys.exc_info())   # TODO логирование


  def on_leIOFinished(self):
    try:
      self.n_ADC_IO = int(self.leIO.text(), 16) & 0xff
    except:
      self.leIO.setText("{:02X}".format(self.n_ADC_IO))
      print(sys.exc_info())   # TODO логирование
    self.leIO.clearFocus() 


  def on_tbIORd_toggle(self):
    try:
      tmpT = svimb.ReadRegs16(self.DirID, self.addrMB, self.BaseCopy + self.offs_ADC_IO, 1) 
      self.n_ADC_IO = (ToUns16(tmpT[0])) & 0xff
      self.leIO.setText("{:02X}".format(self.n_ADC_IO))    
    except:
      self.leIO.setText('?') 
      print(sys.exc_info())   # TODO логирование


  def on_tbIOWr_toggle(self):
    try:
      self.leIO.clearFocus() 
      self.n_ADC_IO = (ToUns16(svimb.WriteReg16(self.DirID, self.addrMB, self.BaseCopy + self.offs_ADC_IO, self.n_ADC_IO))) & 0xff
      self.leIO.setText("{:02X}".format(self.n_ADC_IO))   
    except:
      self.leIO.setText('?')
      print(sys.exc_info())   # TODO логирование


  def on_leSerNumFinished(self):
    try:
      self.n_SerNum = eval(self.leSerNum.text(), {}, {})
    except:
      self.leSerNum.setText(str(self.n_SerNum))
      LL.exception('')
    self.leSerNum.clearFocus() 


  def on_tbSerNumRd_toggle(self):
    try:
      tmpT = svimb.ReadRegs16(self.DirID, self.addrMB, self.BaseCopy + self.offs_SerNum, 1) 
      self.n_SerNum = ToUns16(tmpT[0])
      self.leSerNum.setText(str(self.n_SerNum))    
    except:
      self.leSerNum.setText('?') 
      LL.exception('')


  def on_tbSerNumWr_toggle(self):
    try:
      self.leSerNum.clearFocus() 
      self.n_SerNum = ToUns16(svimb.WriteReg16(self.DirID, self.addrMB, self.BaseCopy + self.offs_SerNum, self.n_SerNum))
      self.leSerNum.setText(str(self.n_SerNum))  
    except:
      self.leSerNum.setText('?') 
      LL.exception('')

################################################


  def on_teDescribeFinished(self):
    a=1

  def on_tbDescribeRd_toggle(self):
    try:
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
      except: a=0
      self.n_Describe=tmptxt
      self.teDescribe.setText(str(self.n_Describe))    
    except:
      self.teDescribe.setText('?') 
      LL.exception('')


  def on_tbDescribemWr_toggle(self):
    try:
      self.n_Describe = self.teDescribe.toPlainText()
      Tmpt=[ord(c) for c in self.n_Describe]
      ltxt=len(self.n_Describe)


      self.teDescribe.clearFocus() 
      i=0
      while(i<ltxt):
       svimb.WriteReg16(self.DirID, self.addrMB, self.BaseCopy + self.offs_Descr+i, Tmpt[i])
       i=i+1
      self.teDescribe.setText(str(self.n_Describe))  
    except:
      self.teDescribe.setText('?') 
      LL.exception('')


  def on_leTypeIDFinished(self):
    try:
      self.n_TypeID = eval(self.leTypeID.text(), {}, {})
    except:
      self.leTypeID.setText(str(self.n_TypeID))
      LL.exception('')
    self.leSerNum.clearFocus() 


  def on_tbTypeIDRd_toggle(self):
    try:
      tmpT = svimb.ReadRegs16(self.DirID, self.addrMB, self.BaseCopy + self.offs_TypeID, 1) 
      self.n_TypeID = ToUns16(tmpT[0])
      self.leTypeID.setText(str(self.n_TypeID))    
    except:
      self.leTypeID.setText('?') 
      LL.exception('')


  def on_tbTypeIDWr_toggle(self):
    try:
      self.leTypeID.clearFocus() 
      self.n_TypeID = ToUns16(svimb.WriteReg16(self.DirID, self.addrMB, self.BaseCopy + self.offs_TypeID, self.n_TypeID))
      self.leTypeID.setText(str(self.n_TypeID))  
    except:
      self.leTypeID.setText('?') 
      LL.exception('')
################################################

  def on_tbSave_toggle(self):
    try:
      svimb.WriteBit(self.DirID, self.addrMB, self.fUpdConf, 1)
    except:
      LL.exception('')

#---
#//////////////////////////////////////////////////
class CfmCondPar(QtGui.QMainWindow, Ui_fmCondPar): 
  # addrMB   - адрес милливольтметра в сети MODBUS
  # scanS    - структура для разбора технологического скана
  # ntScan   - namedtuple для упрощения именования полей на выходе scanF
  # scan     - экземпляр ntScan c данными последнего скана 
  # ADCF     - выход фильтра отсчетов АЦП 
  # mVF      - выход милливольтметра на основании отфильтрованных остчетов АЦП
  # fAuto    - True - запущен автоматическое сканирование по таймеру
  # trAutoScan - ID таймера сканирования
  # filtr    - экземпляр filtrP для фильтрации отсчетов АЦП 
  # wSize    - размер окна filtrP (параметр filtrP)
  # min_cntS - минимально приемлимое значение оставшихся в окне сэмплов для формирования результата (параметр filtrP)
  # раскладка карты MODBUS для параметризации милливольтметра:
  #  mba_zcntIgn   -  кол-во игнорируемых отсчетов с АЦП после переключения ключа 
  #  mba_zcntZero  -  кол-во отсчетов АЦП, усредняемых для получения ноля аналогового тракта 
  #  mba_mcntMeas  -  кол-во отсчетов АЦП, снимаемых в режиме штатных измерений до следующей калибровки ноля 
  #  mba_ZeroA32   -  периодически измеряемый ноль аналогового тракта
  #  mba_mK32      -  коэф-т пересчета кодов АЦП в [В]  - на эту величину ДЕЛЯТСЯ коды 
  #  mba_f24b      -  управляющий флаг - 1 - работа с 24х разрядным АЦП
  #  mba_fZeroComp -  управляющий флаг - 1 - режим автоматической компенсации нуля
  #  mba_tsStart   -  стартовый адрес скана в регистровом поле MODBUS
  #  mbq_tsQnt     -  кол-во регистров MODBUS в технологическом скане
  #  DirID    - активное направление обмена (пока извлекается первое из словаря дескрипторов dirD) TODO 
  #  oldTitle - сохраненный заголовок окна

  def __init__(self,vCE, confMB):
    """ confMB - словарь с картой в регистровом\битовом поле MODBUS """
    global Naladka_stateD    
    super(CfmCondPar, self).__init__()
    self.setupUi(self)
    self.vCE=vCE
    self.addrMB = 1
    self.zcntIgn = 0
    self.zcntZero = 1
    self.mcntMeas = 1000
    self.ZeroA = 0
    self.mK = 1
    self.fAuto = False
    self.trAutoScan = None
    self.scan = None
    self.ADCF = 0
    self.mVF = 0
    self.oldTitle = self.windowTitle()

    self.wSize = 30
    self.min_cntS = 20
    self.filtr = filtrP(self.wSize, self.min_cntS)
    self.filtr1 = filtrP(self.wSize, self.min_cntS)

    self.PD47 = 1
    self.PB5 = 1
    self.Ku = 1.0
    self.B = 0.0
    self.B_ = 0.0
    self.tmpB = 0.0
    try:
      load_Naladka_state()
    except: q=0
    self.mba_zcntIgn = int(confMB["zcntIgn"])
    self.mba_zcntZero = int(confMB["zcntZero"])
    self.mba_mcntMeas = int(confMB["mcntMeas"])
    self.mba_ZeroA32 = int(confMB["ZeroA32"])
    self.mba_mK32 = int(confMB["mK32"])
    self.mba_f24b = int(confMB["f24b"])
    self.mba_fZeroComp = int(confMB["fZeroComp"])
    self.scanS = Struct(confMB["techStr"])
    self.ntScan = namedtuple('ntScan', confMB["techLst"])
    self.mba_tsStart = int(confMB["techStart"])
    self.mbq_tsQnt = int(confMB["techQnt"])

    self.mba_PD47 = int(confMB["PD47_OUTPUT"])
    self.mba_PB5 = int(confMB["PB5_Meandr"])
    self.mba_Aet_1 = int(confMB["Aet_1"])
    self.mba_Aet_2 = int(confMB["Aet_2"])
    self.mba_Aet_3 = int(confMB["Aet_3"])
    self.mba_Aet_4 = int(confMB["Aet_4"])
    self.mba_Aet_5 = int(confMB["Aet_5"])
    self.mba_Aet_6 = int(confMB["Aet_6"])

    self.mba_B_ = int(confMB["B_"])
    self.mba_Nt_1 = int(confMB["Nt_1"])
    self.mba_Nt_2 = int(confMB["Nt_2"])
    self.mba_Nt_3 = int(confMB["Nt_3"])

    self.Aetu_1=sstate.Naladka_stateD['Conductomer']['Aetu_1']
    self.Aetu_2=sstate.Naladka_stateD['Conductomer']['Aetu_2']
    self.Aetu_3=sstate.Naladka_stateD['Conductomer']['Aetu_3']
    self.Aetu_4=sstate.Naladka_stateD['Conductomer']['Aetu_4']
    self.Aetu_5=sstate.Naladka_stateD['Conductomer']['Aetu_5']
    self.Aetu_6=sstate.Naladka_stateD['Conductomer']['Aetu_6']
    try:
     self.B_6=sstate.Naladka_stateD['Conductomer']['B_6']
    except: self.B_6=0.0

    self.leAetu_1.setText(str(self.Aetu_1))
    self.leAetu_2.setText(str(self.Aetu_2))
    self.leAetu_3.setText(str(self.Aetu_3))
    self.leAetu_4.setText(str(self.Aetu_4))
    self.leAetu_5.setText(str(self.Aetu_5))
    self.leAetu_6.setText(str(self.Aetu_6))
    self.leB_6.setText(str(self.B_6))
    self.leB.setText(str(self.B))

    self.leAddrMB.setText(str(self.addrMB)) 
    self.leIgn.setText(str(self.zcntIgn))
    self.leZero.setText(str(self.zcntZero))
    self.leMeas.setText(str(self.mcntMeas))
    self.leKu.setText(str(self.Ku))
    self.lemK.setText(str(self.mK))
    self.leWSize.setText(str(self.wSize))
    self.leMinCntS.setText(str(self.min_cntS))

    self.lePD47.setText(str(self.PD47)) 
    self.leFreqMeandr.setText(str(self.PB5))

    self.actConf.triggered.connect(self.on_muConf_toggle)
    self.menubar.addAction(self.actConf)

    self.leAddrMB.editingFinished.connect(self.on_leAddrMBFinish)

    self.leIgn.editingFinished.connect(self.on_leIgnFinish)
    self.tbIgnRd.clicked.connect(self.on_IgnRd_toggle)
    self.tbIgnWr.clicked.connect(self.on_IgnWr_toggle)
    self.leZero.editingFinished.connect(self.on_leZeroFinish)
    self.tbZeroRd.clicked.connect(self.on_ZeroRd_toggle)
    self.tbZeroWr.clicked.connect(self.on_ZeroWr_toggle)
    self.leMeas.editingFinished.connect(self.on_leMeasFinish)
    self.tbMeasRd.clicked.connect(self.on_MeasRd_toggle)
    self.tbMeasWr.clicked.connect(self.on_MeasWr_toggle)
    self.lemK.editingFinished.connect(self.on_lemKFinish)
    self.tbmKRd.clicked.connect(self.on_mKRd_toggle)
    self.tbmKWr.clicked.connect(self.on_mKWr_toggle) 

    self.lePD47.editingFinished.connect(self.on_lePD47Finish)
    self.tbPD47Rd.clicked.connect(self.on_PD47Rd_toggle)
    self.tbPD47Wr.clicked.connect(self.on_PD47Wr_toggle)
    self.leFreqMeandr.editingFinished.connect(self.on_leFreqMeandrFinish)
    self.tbFreqMeandrRd.clicked.connect(self.on_FreqMeandrRd_toggle)
    self.tbFreqMeandrWr.clicked.connect(self.on_FreqMeandrWr_toggle)
    self.rbOff.setChecked(True)
    self.cbPD1.stateChanged.connect(self.on_PD47Select_toggle)
    self.cbPD2.stateChanged.connect(self.on_PD47Select_toggle)
    self.cbPD3.stateChanged.connect(self.on_PD47Select_toggle)
    self.cbPD4.stateChanged.connect(self.on_PD47Select_toggle)
    self.cbPD5.stateChanged.connect(self.on_PD47Select_toggle)
    self.cbPD6.stateChanged.connect(self.on_PD47Select_toggle)
    self.cbPD7.stateChanged.connect(self.on_PD47Select_toggle)
    self.cbPDXx10.stateChanged.connect(self.on_PD47Select_toggle)
    self.cbPDAuto.stateChanged.connect(self.on_PD47Select_toggle)

    self.rb500.clicked.connect(self.on_PB5Select_toggle)
    self.rb5000.clicked.connect(self.on_PB5Select_toggle)
    self.rbOff.clicked.connect(self.on_PB5Select_toggle)
    self.rbOn.clicked.connect(self.on_PB5Select_toggle)
    self.rbAuto.clicked.connect(self.on_PB5Select_toggle)


    self.leAetu_1.editingFinished.connect(self.on_leAetu_1Finished)
    self.leAetu_2.editingFinished.connect(self.on_leAetu_2Finished)
    self.leAetu_3.editingFinished.connect(self.on_leAetu_3Finished)
    self.leAetu_4.editingFinished.connect(self.on_leAetu_4Finished)
    self.leAetu_5.editingFinished.connect(self.on_leAetu_5Finished)
    self.leAetu_6.editingFinished.connect(self.on_leAetu_6Finished)
    self.leB_6.editingFinished.connect(self.on_leB_6Finished)

    self.leAet_1.editingFinished.connect(self.on_leAet_1Finished)
    self.tbAetRd_1.clicked.connect(self.on_tbAetRd_1_toggle)
    self.tbAetWr_1.clicked.connect(self.on_tbAetWr_1_toggle)
    self.leAet_2.editingFinished.connect(self.on_leAet_2Finished)
    self.tbAetRd_2.clicked.connect(self.on_tbAetRd_2_toggle)
    self.tbAetWr_2.clicked.connect(self.on_tbAetWr_2_toggle)
    self.leAet_3.editingFinished.connect(self.on_leAet_3Finished)
    self.tbAetRd_3.clicked.connect(self.on_tbAetRd_3_toggle)
    self.tbAetWr_3.clicked.connect(self.on_tbAetWr_3_toggle)
    self.leAet_4.editingFinished.connect(self.on_leAet_4Finished)
    self.tbAetRd_4.clicked.connect(self.on_tbAetRd_4_toggle)
    self.tbAetWr_4.clicked.connect(self.on_tbAetWr_4_toggle)
    self.leAet_5.editingFinished.connect(self.on_leAet_5Finished)
    self.tbAetRd_5.clicked.connect(self.on_tbAetRd_5_toggle)
    self.tbAetWr_5.clicked.connect(self.on_tbAetWr_5_toggle)
    self.leAet_6.editingFinished.connect(self.on_leAet_6Finished)
    self.tbAetRd_6.clicked.connect(self.on_tbAetRd_6_toggle)
    self.tbAetWr_6.clicked.connect(self.on_tbAetWr_6_toggle)

    self.leB_.editingFinished.connect(self.on_leB_Finished)
    self.tbmB_Rd.clicked.connect(self.on_tbmB_Rd_toggle)
    self.tbmB_Wr.clicked.connect(self.on_tbmB_Wr_toggle)

    self.leNt_1.editingFinished.connect(self.on_leNt_1Finished)
    self.tbNtRd_1.clicked.connect(self.on_tbNtRd_1_toggle)
    self.tbNtWr_1.clicked.connect(self.on_tbNtWr_1_toggle)
    self.leNt_2.editingFinished.connect(self.on_leNt_2Finished)
    self.tbNtRd_2.clicked.connect(self.on_tbNtRd_2_toggle)
    self.tbNtWr_2.clicked.connect(self.on_tbNtWr_2_toggle)
    self.leNt_3.editingFinished.connect(self.on_leNt_3Finished)
    self.tbNtRd_3.clicked.connect(self.on_tbNtRd_3_toggle)
    self.tbNtWr_3.clicked.connect(self.on_tbNtWr_3_toggle)

    self.ch24b.stateChanged.connect(self.on_ch24b_changed)
    self.chZeroComp.stateChanged.connect(self.on_chZeroComp_changed)
    self.tbScan.clicked.connect(self.on_Scan_toggle)
    self.tbAutoScan.clicked.connect(self.on_AutoScan_toggle)

    self.leWSize.editingFinished.connect(self.on_leWSizeFinish)
    self.leMinCntS.editingFinished.connect(self.on_leMinCntSFinish)

    self.leKu.editingFinished.connect(self.on_leKuFinish)
    self.tbAetuWr.clicked.connect(self.on_tbAetuWr_toggle)
    self.leB.editingFinished.connect(self.on_leBFinish)

    self.lcdDataConv_cond.setDigitCount(13)
    self.lcdDataConvF_cond.setDigitCount(13)
    self.lcdDataConv_cond_1.setDigitCount(13)
    self.lcdDataConvF_cond_1.setDigitCount(9)

    self.widthD = 9 # 4
    self.precD = 4  # 3
    self.widthD1 = 6 # 4
    self.precD1 = 4  # 3
    self.formS = "{:"+str(self.widthD)+"."+str(self.precD)+"f}"
    self.formS1 = "{:"+str(self.widthD1)+"."+str(self.precD1)+"f}"
    self.formS2 = "{:"+str(8)+"."+str(5)+"f}"


  def closeEvent(self, event):
    try:
      save_Naladka_state()
    except:
      
        q=0

  def showEvent(self, e):
    global dirD 

    tmpL = [k for k in dirD.keys()]
    try:
      self.DirID = tmpL[0]  # пока за активное направление принимается первое TODO
      self.setWindowTitle("{} [{}]".format(self.oldTitle, dirD[self.DirID]["cmnt"]))
    except:
      self.DirID = 0
      print(sys.exc_info())   # TODO логирование
    super().showEvent(e)

  
  def timerEvent(self, e):
    self.tmpR=0.0
    self.tmpX=0.0
    self.C=1.956947E-6
    #self.C=1.956947
    self.tmpC=0.0
    self.tmpB6=0.0
    # print("timerEvent ID = {}".format(e.timerId())) # ВРЕМЕННО !!!
    self.tbScan.click()  
    ######################################################
    '''self.Aetu=self.Aetu_1
    self.tmp_R=500000
    if (self.tmp_R!=0):
              self.tmpX=self.B_-self.tmpC+self.Ku/(float(self.tmp_R)*self.Aetu)#См
              self.lcdDataConvF_cond.display(self.formS.format(self.tmp_R))
              self.lcdDataConv_cond_1.display(self.formS.format(self.tmpX*(10**6))) #мкСм
    else : self.lcdDataConv_cond_1.display('-')

    if(self.tmpX!=0):
              self.tmpR=1/self.tmpX
              self.lcdDataConv_cond.display(self.formS2.format(self.tmpR))#Сопротивление """
    else : 
        self.lcdDataConv_cond.display('-')
        self.lcdDataConvF_cond.display(self.formS.format(self.tmp_R))'''
    #######################################################  

    if (self.scan):
      self.llData_cond.setText(str(self.scan.ZeroA1))
      self.llDataBand.setText(str(int(self.scan.Band)))
      #if(self.scan.Band==0): self.llDataBand_2.setText('мкСм/см    МОм')
      #if (self.scan.Band==1)or(self.scan.Band==2)or(self.scan.Band==3)or(self.scan.Band==4): self.llDataBand_2.setText('мкСм/см    МОм')
      self.llDataBand_2.setText('мкСм/см    Ом')
      self.B_=self.B

      self.ADCF = self.filtr1.newS(self.scan.ZeroA1)
      if (self.ADCF<1000000) : 
          #self.lcdDataConv_cond.display(self.formS2.format(self.scan.mV/100000000.0))
          #if (self.scan.Band<=2):
              #self.tmpX=1/self.scan.mV-1.956947E-6
              #self.tmpR=1/self.tmpX
              #self.lcdDataConv_cond.display(self.formS2.format(self.tmpR))#Сопротивление """

          #if (self.scan.Band>=3):
              #self.lcdDataConv_cond.display(self.formS2.format(self.scan.mV))#Сопротивление """
          self.Aetu=1
          if(self.scan.Band==1):self.Aetu=self.Aetu_1
          if(self.scan.Band==2):self.Aetu=self.Aetu_2
          if(self.scan.Band==3):self.Aetu=self.Aetu_3
          if(self.scan.Band==4):self.Aetu=self.Aetu_4
          if(self.scan.Band==5):self.Aetu=self.Aetu_5
          if(self.scan.Band==6):self.Aetu=self.Aetu_6

          self.tmpC=self.C
          self.tmp_R=self.scan.mV
          if(self.scan.Band<=2):
            self.tmpB=self.B_/1000000.0 
          else:
            self.tmpB=0.0

          if(self.scan.Band==6):
              self.tmpB6=self.B_6 
          else:
              self.tmpB6=0.0

          if (self.tmp_R!=0):
              self.tmpX=self.tmpB-self.Ku*self.tmpC+ self.tmpB6/1000 +self.Ku/(float(self.tmp_R)*self.Aetu)#См
              self.lcdDataConvF_cond.display(self.formS.format(self.tmp_R))
              self.lcdDataConv_cond_1.display(self.formS.format(self.tmpX*(10**6))) #мкСм
          else : self.lcdDataConv_cond_1.display('-')

          if(self.tmpX!=0):
              self.tmpR=1/self.tmpX
              self.lcdDataConv_cond.display(self.formS2.format(self.tmpR))#Сопротивление """
          else : 
              self.lcdDataConv_cond.display('-')
              self.lcdDataConvF_cond.display(self.formS.format(self.tmp_R))
      self.tmpmV=self.tmpR

      self.mVF = self.filtr.newS(self.tmpmV)
       
      self.llDataF_cond.setText(str(self.ADCF))
      if (self.ADCF<1000000) :
          a=0
          ###self.lcdDataConvF_cond.display(self.formS1.format(self.mVF))
          if (self.mVF!=0):self.lcdDataConvF_cond_1.display(self.formS.format(self.B_+(10**6)*self.Ku/float(self.mVF*self.Aetu)))
          else : self.lcdDataConvF_cond_1.display('-')

      self.llCntS.setText(str(self.filtr.cntS))
      self.llNumPass.setText(str(self.filtr.NumPass))

      self.llData_cond.update()
      self.llDataF_cond.update()
      self.llCntS.update()  
      self.llNumPass.update()
      #self.lt = time.localtime()
      #print (strftime("%H:%M:%S.%f"))
      now = datetime.now()
      #print (now.strftime("%H:%M:%S.%f"))
      #print("adc = {} \t mV = {} \t adcF = {} \t mVF = {}".format(self.scan.ADCcode, self.scan.mV, self.ADCF, self.mVF))               
      #print("adc = {} \t adcF = {} \t mVF = {}".format(self.scan.ADCcode, self.ADCF, self.mVF))  
      print( " {} \t adc1 = {} \t adc2 = {} \t Adc_rez = {}  \t Adc_rezf = {}\t A = {} \t A_f = {} \t Band = {}".format(now.strftime("%H:%M:%S.%f"), self.scan.ADCcode, self.scan.ZeroA, self.scan.ZeroA1, self.ADCF, self.scan.mV/100000000.0, self.mVF/100000000.0, int(self.scan.Band)))    
      #print("adc1 = {} \t adc2 = {} \t ACd_rez = {}".format(self.scan.ADCcode, self.scan.ZeroA, self.scan.mV ))            
            

  def on_tbAetuWr_toggle(self):
    try:
      sstate.Naladka_stateD['Conductomer']['Aetu_1']=self.Aetu_1
      sstate.Naladka_stateD['Conductomer']['Aetu_2']=self.Aetu_2
      sstate.Naladka_stateD['Conductomer']['Aetu_3']=self.Aetu_3
      sstate.Naladka_stateD['Conductomer']['Aetu_4']=self.Aetu_4
      sstate.Naladka_stateD['Conductomer']['Aetu_5']=self.Aetu_5
      sstate.Naladka_stateD['Conductomer']['Aetu_6']=self.Aetu_6
      sstate.Naladka_stateD['Conductomer']['B_6']=self.B_6

    except:

      LL.exception('')

  def on_leBFinish(self):
    try:
      self.B = eval(self.leB.text(), {}, {})
    except:
      print(sys.exc_info())   # TODO логирование
    self.leB.setText(str(self.B))
    self.leB.clearFocus()

  def on_muConf_toggle(self):
    self.vCE.winCCond.show(self.DirID, self.addrMB)


  def on_leAddrMBFinish(self):
    try:
      self.addrMB = eval(self.leAddrMB.text(), {}, {})
    except:
      print(sys.exc_info())   # TODO логирование
    self.leAddrMB.setText(str(self.addrMB))
    self.leAddrMB.clearFocus()    


  def on_leIgnFinish(self):
    try:
      self.zcntIgn = eval(self.leIgn.text(), {}, {})
    except:
      print(sys.exc_info())   # TODO логирование
    self.leIgn.setText(str(self.zcntIgn))
    self.leIgn.clearFocus()  


  def on_IgnRd_toggle(self):
    try: 
      tmpL = svimb.ReadRegs16(self.DirID , self.addrMB, self.mba_zcntIgn, 1)
       # конвертер в unsigned 
      self.zcntIgn = int.from_bytes(tmpL[0].to_bytes(2, 'little', signed = True), 'little')
      self.leIgn.setText(str(self.zcntIgn))
    except:
      self.leIgn.setText('?')
      print(sys.exc_info())   # TODO логирование 


  def on_IgnWr_toggle(self):
    try:
      self.leIgn.clearFocus()
      svimb.WriteReg16(self.DirID, self.addrMB, self.mba_zcntIgn, self.zcntIgn & 0xffff) 
    except:
      self.leIgn.setText('?')
      print(sys.exc_info())   # TODO логирование 


  def on_leZeroFinish(self):
    try:
      self.zcntZero = eval(self.leZero.text(), {}, {})
    except:
      print(sys.exc_info())   # TODO логирование
    self.leZero.setText(str(self.zcntZero))
    self.leZero.clearFocus()  


  def on_ZeroRd_toggle(self):
    try:
      tmpL = svimb.ReadRegs16(self.DirID, self.addrMB, self.mba_zcntZero, 1)
      # конвертер в unsigned 
      self.zcntZero = int.from_bytes(tmpL[0].to_bytes(2, 'little', signed = True), 'little')
      self.leZero.setText(str(self.zcntZero))
    except:
      self.leZero.setText('?')
      print(sys.exc_info())   # TODO логирование 


  def on_ZeroWr_toggle(self):
    try:
      self.leZero.clearFocus()
      svimb.WriteReg16(self.DirID, self.addrMB, self.mba_zcntZero, self.zcntZero & 0xffff)
    except:
      self.leZero.setText('?')
      print(sys.exc_info())   # TODO логирование 


  def on_leMeasFinish(self):
    try:
      self.mcntMeas = eval(self.leMeas.text(), {}, {})
    except:
      print(sys.exc_info())   # TODO логирование
    self.leMeas.setText(str(self.mcntMeas))
    self.leMeas.clearFocus()


  def on_MeasRd_toggle(self): 
     try:
       tmpL = svimb.ReadRegs16(self.DirID, self.addrMB, self.mba_mcntMeas, 1)
       # конвертер в unsigned 
       self.mcntMeas = int.from_bytes(tmpL[0].to_bytes(2, 'little', signed = True), 'little')
       self.leMeas.setText(str(self.mcntMeas))
     except:
      self.leMeas.setText('?')
      print(sys.exc_info())   # TODO логирование 

    
  def  on_MeasWr_toggle(self):
    try:
      self.leMeas.clearFocus()
      svimb.WriteReg16(self.DirID, self.addrMB, self.mba_mcntMeas, self.mcntMeas & 0xffff)
    except:
      self.leMeas.setText('?')
      print(sys.exc_info())   # TODO логирование 


  def on_lemKFinish(self):
    try:
      self.mK = eval(self.lemK.text(), {}, {})
    except:
      print(sys.exc_info())   # TODO логирование
    self.lemK.setText(str(self.mK))
    self.lemK.clearFocus()


  def on_mKRd_toggle(self):
    try:
      (rlow, rhigh) = svimb.ReadRegs16(self.DirID, self.addrMB, self.mba_mK32, 2)
      self.mK = ToSig32(rlow, rhigh)
      self.lemK.setText(str(self.mK))
    except:
      self.lemK.setText('?')
      print(sys.exc_info())   # TODO логирование 


  def on_mKWr_toggle(self):
    try:
      self.lemK.clearFocus()
      svimb.WriteReg16(self.DirID, self.addrMB, self.mba_mK32, self.mK & 0xffff)
      svimb.WriteReg16(self.DirID, self.addrMB, self.mba_mK32+1, (self.mK & 0xffff0000) >> 16)
    except:
      self.lemK.setText('?')
      print(sys.exc_info())   # TODO логирование 

 
  def on_leZeroAFinish(self):
    try:
      self.ZeroA = eval(self.leZeroA.text(), {}, {})
    except:
      print(sys.exc_info())   # TODO логирование
    self.leZeroA.setText(str(self.ZeroA))
    self.leZeroA.clearFocus()


  def on_ZeroAWr_toggle(self):
    try:
      self.leZeroA.clearFocus()
      svimb.WriteReg16(self.DirID, self.addrMB, self.mba_ZeroA32, self.ZeroA & 0xffff)
      svimb.WriteReg16(self.DirID, self.addrMB, self.mba_ZeroA32+1, (self.ZeroA & 0xffff0000) >> 16)
    except:
      self.leZeroA.setText('?')
      print(sys.exc_info())   # TODO логирование 
 
  @QtCore.pyqtSlot(int) 
  def on_ch24b_changed(self, ind):
    try:
      svimb.WriteBit(self.DirID, self.addrMB, self.mba_f24b, self.ch24b.isChecked())
    except:
      self.ch24b.setCheckState(QtCore.Qt.PartiallyChecked)
      print(sys.exc_info())   # TODO логирование 


  @QtCore.pyqtSlot(int)
  def on_chZeroComp_changed(self, ind):
    try:
      svimb.WriteBit(self.DirID, self.addrMB, self.mba_fZeroComp, self.chZeroComp.isChecked())
    except:
      self.chZeroComp.setCheckState(QtCore.Qt.PartiallyChecked)
      print(sys.exc_info())   # TODO логирование  


  def on_Scan_toggle(self):
    try:
      tmpL = svimb.ReadRegs16(self.DirID, self.addrMB, self.mba_tsStart, self.mbq_tsQnt)
      #print(tmpL)               
      ba = bytearray()
      for reg in tmpL:
        ba += reg.to_bytes(2, 'little', signed = True)
      #print("ba={}".format(ba)) 
      self.scan = self.ntScan._make(self.scanS.unpack(ba))
    except:
      print(sys.exc_info())   # TODO логирование 


  def on_AutoScan_toggle(self):
    self.fAuto = not self.fAuto
    self.tbAutoScan.setDown(self.fAuto)    
    if (self.fAuto):
      self.trAutoScan = self.startTimer(500)  
      print("trAutoScan = {}".format(self.trAutoScan))      

    else:
      self.killTimer(self.trAutoScan) 


  def on_leWSizeFinish(self):
    try:
      self.wSize = eval(self.leWSize.text(), {}, {})
      self.filtr = filtrP(self.wSize, self.min_cntS) 
      self.filtr1 = filtrP(self.wSize, self.min_cntS) 
    except:
      print(sys.exc_info())   # TODO логирование
    self.leWSize.setText(str(self.wSize))
    self.leWSize.clearFocus()

  def on_leKuFinish(self):
    try:
      self.Ku = eval(self.leKu.text(), {}, {})
    except:
      print(sys.exc_info())   # TODO логирование
    self.leWSize.setText(str(self.Ku))
    self.leWSize.clearFocus()
##############################################################
  def on_lePD47Finish(self):
    try:
      self.PD47 = eval(self.lePD47.text(), {}, {})
    except:
      print(sys.exc_info())   # TODO логирование
    self.lePD47.setText(str(self.PD47))
    self.lePD47.clearFocus()


  def on_PD47Rd_toggle(self): 
     try:
       tmpL = svimb.ReadRegs16(self.DirID, self.addrMB, self.mba_PD47, 1)
       # конвертер в unsigned 
       self.PD47 = int.from_bytes(tmpL[0].to_bytes(2, 'little', signed = True), 'little')
       self.lePD47.setText(str(self.PD47))
     except:
      self.lePD47.setText('?')
      print(sys.exc_info())   # TODO логирование 

    
  def  on_PD47Wr_toggle(self):
    try:
      self.lePD47.clearFocus()
      svimb.WriteReg16(self.DirID, self.addrMB, self.mba_PD47, self.PD47 & 0xffff)
    except:
      self.lePD47.setText('?')
      print(sys.exc_info())   # TODO логирование 

##
  def on_leFreqMeandrFinish(self):
    try:
      self.PB5 = eval(self.leFreqMeandr.text(), {}, {})
    except:
      print(sys.exc_info())   # TODO логирование
    self.leFreqMeandr.setText(str(self.PB5))
    self.leFreqMeandr.clearFocus()


  def on_FreqMeandrRd_toggle(self): 
     try:
       tmpL = svimb.ReadRegs16(self.DirID, self.addrMB, self.mba_PB5, 1)
       # конвертер в unsigned 
       self.PB5 = int.from_bytes(tmpL[0].to_bytes(2, 'little', signed = True), 'little')
       self.leFreqMeandr.setText(str(self.PB5))
     except:
      self.leFreqMeandr.setText('?')
      print(sys.exc_info())   # TODO логирование 

  def on_PD47Select_toggle(self): 
     tmp=0
     if self.cbPD1.isChecked()==1:
         tmp=1

     if self.cbPD2.isChecked()==1:
         tmp=2

     if self.cbPD3.isChecked()==1:
         tmp=3

     if self.cbPD4.isChecked()==1:
         tmp=4

     if self.cbPD5.isChecked()==1:
         tmp=5

     if self.cbPD6.isChecked()==1:
         tmp=6

     if self.cbPD7.isChecked()==1:
         tmp=7
     if self.cbPDXx10.isChecked()==1:
         tmp=tmp+10
  
     if self.cbPDAuto.isChecked()==1:
         tmp=9

     self.lePD47.setText(str(tmp))
     self.on_lePD47Finish() 

  def on_PB5Select_toggle(self): 
     tmp=0
     if self.rb500.isChecked()==1:
         tmp=1

     if self.rb5000.isChecked()==1:
         tmp=2
     
     if self.rbOff.isChecked()==1:
         tmp=0

     if self.rbOn.isChecked()==1:
         tmp=3
     if self.rbAuto.isChecked()==1:
         tmp=9

     self.leFreqMeandr.setText(str(tmp))
     self.on_leFreqMeandrFinish() 
        
  def  on_FreqMeandrWr_toggle(self):
    try:
      self.leFreqMeandr.clearFocus()
      svimb.WriteReg16(self.DirID, self.addrMB, self.mba_PB5, self.PB5 & 0xffff)
    except:
      self.leFreqMeandr.setText('?')
      print(sys.exc_info())   # TODO логирование 

##############################################################
  def on_leAet_1Finished(self):
    try:
      self.n_Aet_1 = eval(self.leAet_1.text(), {}, {})
    except:
      self.leAet_1.setText(str(self.n_Aet_1))
      LL.exception('')
    self.leAet_1.clearFocus() 

  def on_tbAetRd_1_toggle(self):
    try:
      (rlow, rhigh) = svimb.ReadRegs16(self.DirID, self.addrMB, self.mba_Aet_1, 2) 
      self.n_Aet_1 = ToUns32(rlow, rhigh)/10**3
      self.leAet_1.setText(str(self.n_Aet_1))    
    except:
      self.leAet_1.setText('?') 
      LL.exception('')




  def on_tbAetWr_1_toggle(self):
    try:
      self.leAet_1.clearFocus() 
      svimb.WriteReg16(self.DirID, self.addrMB, self.mba_Aet_1, (int)(self.n_Aet_1*10**3) & 0xffff)#2
      svimb.WriteReg16(self.DirID, self.addrMB, self.mba_Aet_1+1, ((int)(self.n_Aet_1*10**3) & 0xffff0000) >> 16)
      self.leAet_1.setText(str(self.n_Aet_1))  
    except:
      self.leAet_1.setText('?') 
      LL.exception('')

  def on_leAet_2Finished(self):
    try:
      self.n_Aet_2 = eval(self.leAet_2.text(), {}, {})
    except:
      self.leAet_2.setText(str(self.n_Aet_2))
      LL.exception('')
    self.leAet_2.clearFocus() 

  def on_tbAetRd_2_toggle(self):
    try:
      (rlow, rhigh) = svimb.ReadRegs16(self.DirID, self.addrMB, self.mba_Aet_2, 2) 
      self.n_Aet_2 = ToUns32(rlow, rhigh)/10**3##3
      self.leAet_2.setText(str(self.n_Aet_2))    
    except:
      self.leAet_2.setText('?') 
      LL.exception('')

  def on_tbAetWr_2_toggle(self):
    try:
      self.leAet_2.clearFocus() 
      svimb.WriteReg16(self.DirID, self.addrMB, self.mba_Aet_2, round(self.n_Aet_2*10**3) & 0xffff)##3
      svimb.WriteReg16(self.DirID, self.addrMB, self.mba_Aet_2+1, (round(self.n_Aet_2*10**3) & 0xffff0000) >> 16)##3
      self.leAet_2.setText(str(self.n_Aet_2))  
    except:
      self.leAet_2.setText('?') 
      LL.exception('')

  def on_leAet_3Finished(self):
    try:
      self.n_Aet_3 = eval(self.leAet_3.text(), {}, {})
    except:
      self.leAet_3.setText(str(self.n_Aet_3))
      LL.exception('')
    self.leAet_3.clearFocus() 

  def on_tbAetRd_3_toggle(self):
    try:
      (rlow, rhigh) = svimb.ReadRegs16(self.DirID, self.addrMB, self.mba_Aet_3, 2) 
      self.n_Aet_3 = ToUns32(rlow, rhigh)/10**4
      self.leAet_3.setText(str(self.n_Aet_3))    
    except:
      self.leAet_3.setText('?') 
      LL.exception('')

  def on_tbAetWr_3_toggle(self):
    try:
      self.leAet_3.clearFocus() 
      svimb.WriteReg16(self.DirID, self.addrMB, self.mba_Aet_3, round(self.n_Aet_3*10**4) & 0xffff)
      svimb.WriteReg16(self.DirID, self.addrMB, self.mba_Aet_3+1, (round(self.n_Aet_3*10**4) & 0xffff0000) >> 16)
      self.leAet_3.setText(str(self.n_Aet_3))  
    except:
      self.leAet_3.setText('?') 
      LL.exception('')

  def on_leAet_4Finished(self):
    try:
      self.n_Aet_4 = eval(self.leAet_4.text(), {}, {})
    except:
      self.leAet_4.setText(str(self.n_Aet_4))
      LL.exception('')
    self.leAet_4.clearFocus() 

  def on_tbAetRd_4_toggle(self):
    try:
      (rlow, rhigh) = svimb.ReadRegs16(self.DirID, self.addrMB, self.mba_Aet_4, 2) 
      self.n_Aet_4 = ToUns32(rlow, rhigh)/10**5
      self.leAet_4.setText(str(self.n_Aet_4))    
    except:
      self.leAet_4.setText('?') 
      LL.exception('')

  def on_tbAetWr_4_toggle(self):
    try:
      self.leAet_4.clearFocus() 
      svimb.WriteReg16(self.DirID, self.addrMB, self.mba_Aet_4, round(self.n_Aet_4*10**5) & 0xffff)
      svimb.WriteReg16(self.DirID, self.addrMB, self.mba_Aet_4+1, (round(self.n_Aet_4*10**5) & 0xffff0000) >> 16)
      self.leAet_4.setText(str(self.n_Aet_4))  
    except:
      self.leAet_4.setText('?') 
      LL.exception('')

  def on_leAet_5Finished(self):
    try:
      self.n_Aet_5 = eval(self.leAet_5.text(), {}, {})
    except:
      self.leAet_5.setText(str(self.n_Aet_5))
      LL.exception('')
    self.leAet_5.clearFocus() 

  def on_tbAetRd_5_toggle(self):
    try:
      (rlow, rhigh) = svimb.ReadRegs16(self.DirID, self.addrMB, self.mba_Aet_5, 2) 
      self.n_Aet_5 = ToUns32(rlow, rhigh)/10**6
      self.leAet_5.setText(str(self.n_Aet_5))    
    except:
      self.leAet_5.setText('?') 
      LL.exception('')

  def on_tbAetWr_5_toggle(self):
    try:
      self.leAet_5.clearFocus() 
      svimb.WriteReg16(self.DirID, self.addrMB, self.mba_Aet_5, round(self.n_Aet_5*10**6) & 0xffff)
      svimb.WriteReg16(self.DirID, self.addrMB, self.mba_Aet_5+1, (round(self.n_Aet_5*10**6) & 0xffff0000) >> 16)
      self.leAet_5.setText(str(self.n_Aet_5))  
    except:
      self.leAet_5.setText('?') 
      LL.exception('')

  def on_leAet_6Finished(self):
    try:
      self.n_Aet_6 = eval(self.leAet_6.text(), {}, {})
    except:
      self.leAet_6.setText(str(self.n_Aet_6))
      LL.exception('')
    self.leAet_6.clearFocus() 

  def on_tbAetRd_6_toggle(self):
    try:
      
      (rlow, rhigh) = svimb.ReadRegs16(self.DirID, self.addrMB, self.mba_Aet_6, 2) 
      self.n_Aet_6 = ToUns32(rlow, rhigh)/10**7
      self.leAet_6.setText(str(self.n_Aet_6))    
    except:
      self.leAet_6.setText('?') 
      LL.exception('')

  def on_tbAetWr_6_toggle(self):
    try:
      self.leAet_6.clearFocus() 
      svimb.WriteReg16(self.DirID, self.addrMB, self.mba_Aet_6, round(self.n_Aet_6*10**7) & 0xffff)
      svimb.WriteReg16(self.DirID, self.addrMB, self.mba_Aet_6+1, (round(self.n_Aet_6*10**7) & 0xffff0000) >> 16)
      self.leAet_6.setText(str(self.n_Aet_6))  
    except:
      self.leAet_6.setText('?') 
      LL.exception('')

  def on_leB_Finished(self):
    try:
      self.n_B_ = eval(self.leB_.text(), {}, {})
    except:
      self.leB_.setText(str(self.n_B_))
      LL.exception('')
    self.leB_.clearFocus() 

  def on_tbmB_Rd_toggle(self):
    try:
      (rlow, rhigh) = svimb.ReadRegs16(self.DirID, self.addrMB, self.mba_B_, 2) 
      self.n_B_ = ToSig32(rlow, rhigh)/10**7
      self.leB_.setText(str(self.n_B_))    
    except:
      self.leB_.setText('?') 
      LL.exception('')

  def on_tbmB_Wr_toggle(self):
    try:
      self.leB_.clearFocus() 
      svimb.WriteReg16(self.DirID, self.addrMB, self.mba_B_, round(self.n_B_*10**7) & 0xffff)
      svimb.WriteReg16(self.DirID, self.addrMB, self.mba_B_+1, (round(self.n_B_*10**7) & 0xffff0000) >> 16)
      self.leB_.setText(str(self.n_B_))  
    except:
      self.leB_.setText('?') 
      LL.exception('')

  def on_leNt_1Finished(self):
    try:
      self.n_Nt_1 = eval(self.leNt_1.text(), {}, {})
    except:
      self.leNt_1.setText(str(self.n_Nt_1))
      LL.exception('')
    self.leNt_1.clearFocus() 

  def on_tbNtRd_1_toggle(self):
    try:
      tmpL= svimb.ReadRegs16(self.DirID, self.addrMB, self.mba_Nt_1, 1) 
      self.n_Nt_1 = int.from_bytes(tmpL[0].to_bytes(2, 'little', signed = True), 'little')
      self.leNt_1.setText(str(self.n_Nt_1))    
    except:
      self.leNt_1.setText('?') 
      LL.exception('')

  def on_tbNtWr_1_toggle(self):
    try:
      self.leNt_1.clearFocus() 
      svimb.WriteReg16(self.DirID, self.addrMB, self.mba_Nt_1, self.n_Nt_1 & 0xffff)
      self.leNt_1.setText(str(self.n_Nt_1))  
    except:
      self.leNt_1.setText('?') 
      LL.exception('')

  def on_leNt_2Finished(self):
    try:
      self.n_Nt_2 = eval(self.leNt_2.text(), {}, {})
    except:
      self.leNt_2.setText(str(self.n_Nt_2))
      LL.exception('')
    self.leNt_2.clearFocus() 

  def on_tbNtRd_2_toggle(self):
    try:
      tmpL = svimb.ReadRegs16(self.DirID, self.addrMB, self.mba_Nt_2, 2) 
      self.n_Nt_2 =  int.from_bytes(tmpL[0].to_bytes(2, 'little', signed = True), 'little')
      self.leNt_2.setText(str(self.n_Nt_2))    
    except:
      self.leNt_2.setText('?') 
      LL.exception('')

  def on_tbNtWr_2_toggle(self):
    try:
      self.leNt_2.clearFocus() 
      svimb.WriteReg16(self.DirID, self.addrMB, self.mba_Nt_2, self.n_Nt_2 & 0xffff)
      self.leNt_2.setText(str(self.n_Nt_2))  
    except:
      self.leNt_2.setText('?') 
      LL.exception('')

  def on_leNt_3Finished(self):
    try:
      self.n_Nt_3 = eval(self.leNt_3.text(), {}, {})
    except:
      self.leNt_3.setText(str(self.n_Nt_3))
      LL.exception('')
    self.leNt_3.clearFocus() 

  def on_tbNtRd_3_toggle(self):
    try:
      tmpL= svimb.ReadRegs16(self.DirID, self.addrMB, self.mba_Nt_3, 2) 
      self.n_Nt_3 =  int.from_bytes(tmpL[0].to_bytes(2, 'little', signed = True), 'little')
      self.leNt_3.setText(str(self.n_Nt_3))    
    except:
      self.leNt_3.setText('?') 
      LL.exception('')

  def on_tbNtWr_3_toggle(self):
    try:
      self.leNt_3.clearFocus() 
      svimb.WriteReg16(self.DirID, self.addrMB, self.mba_Nt_3, self.n_Nt_3 & 0xffff)
      self.leNt_3.setText(str(self.n_Nt_3))  
    except:
      self.leNt_3.setText('?') 
      LL.exception('')

  def on_leMinCntSFinish(self):
    try:
      self.min_cntS = eval(self.leMinCntS.text(), {}, {})
      self.filtr = filtrP(self.wSize, self.min_cntS)
      self.filtr1 = filtrP(self.wSize, self.min_cntS) 
    except:
      print(sys.exc_info())   # TODO логирование
    self.leMinCntS.setText(str(self.min_cntS))
    self.leMinCntS.clearFocus()

  def on_leAetu_1Finished(self):
    try:
      self.Aetu_1 = eval(self.leAetu_1.text(), {}, {})
    except:
      self.leAetu_1.setText(str(self.Aetu_1))
      LL.exception('')
    self.leAetu_1.clearFocus() 

  def on_leAetu_2Finished(self):
    try:
      self.Aetu_2 = eval(self.leAetu_2.text(), {}, {})
    except:
      self.leAetu_2.setText(str(self.Aetu_2))
      LL.exception('')
    self.leAetu_2.clearFocus() 

  def on_leAetu_3Finished(self):
    try:
      self.Aetu_3 = eval(self.leAetu_3.text(), {}, {})
    except:
      self.leAetu_3.setText(str(self.Aetu_3))
      LL.exception('')
    self.leAetu_3.clearFocus() 

  def on_leAetu_4Finished(self):
    try:
      self.Aetu_4 = eval(self.leAetu_4.text(), {}, {})
    except:
      self.leAetu_4.setText(str(self.Aetu_4))
      LL.exception('')
    self.leAetu_4.clearFocus() 

  def on_leAetu_5Finished(self):
    try:
      self.Aetu_5 = eval(self.leAetu_5.text(), {}, {})
    except:
      self.leAetu_5.setText(str(self.Aetu_5))
      LL.exception('')
    self.leAetu_5.clearFocus() 

  def on_leAetu_6Finished(self):
    try:
      self.Aetu_6 = eval(self.leAetu_6.text(), {}, {})
    except:
      self.leAetu_6.setText(str(self.Aetu_6))
      LL.exception('')
    self.leAetu_6.clearFocus() 

  def on_leB_6Finished(self):
    try:
      self.B_6 = eval(self.leB_6.text(), {}, {})
    except:
      self.leB_6.setText(str(self.Aetu_6))
      LL.exception('')
    self.leB_6.clearFocus() 

#---
class CfmCondConf(QtGui.QMainWindow, Ui_fmCondConf): 
  # DirID - активное направление MODBUS 
  # addrMB - адрес конфигурируемого милливольтметра на направлении DirID
  # wnCaption - заголовок окна
  
  # новые параметры в редактируемой копии конфигурации милливольтметра
  #  n_addrMB - адрес в сети MODBUS
  #  n_thrAT  - предельно допустимая распределенная пауза в приемном пакете 
  #  n_ZeroA  - cмещение нуля(32р) [unsigned]
  #  n_mK     - коэф-т пересчета кодов АЦП в [В] (32р) [signed]
  #  n_ADC_mode - загружаемое значение в регистр mode AЦП
  #  n_ADC_conf - загружаемое значение в регистр configuration AЦП
  #  n_ADC_IO   - загружаемое значение в регистр IO AЦП (младший байт)
  #  n_SerNum   - серийный номер узла

  # раскладка карты MODBUS для параметризации милливольтметра:
  #  mbv_ZeroA32    - cмещение нуля(32р) в SysVar (параметр используется в рилтайм рассчетах)
  #  mbv_mK32       - коэф-т пересчета кодов АЦП в [В] (32р) в SysVar (параметр используется в рилтайм рассчетах)
  #  fUpdConf       - дискретная команда на запись редактируемой копии в энергонезависимую память
  # следующие поля заданы в виде регистровых смещений относительно Base
  #  BaseMain      - начало активной конфигурации (доступна только для чтения)
  #  BaseCopy      - начало редактируемой копии конфигурации
  #  offs_addr     - адрес данного устройства в сети MODBUS 
  #  offs_thrAT    - предельно допустимая распределенная пауза в приемном пакете 
  #  offs_ZeroA32  - cмещение нуля(32р)
  #  offs_mK32     - коэф-т пересчета кодов АЦП в [В] (32р)
  #  offs_ADC_mode - загружаемое значение в регистр mode AЦП
  #  offs_ADC_conf - загружаемое значение в регистр configuration AЦП
  #  offs_ADC_IO   - загружаемое значение в регистр IO AЦП (младший байт)
  #  offs_SerNum   - серийный номер узла 

  def __init__(self,vCE, confMB, mbv_ZeroA32, mbv_mK32):
    """ confMB - словарь с картой в регистровом\битовом поле MODBUS 
        mbv_ZeroA32, mbv_mK32 - адреса в структуре системных переманных SysVar """
       
    super(CfmCondConf, self).__init__()
    self.setupUi(self)
    self.vCE=vCE
    self.addrMB = 1
    self.wnCaption = self.windowTitle()
       
    self.mbv_ZeroA32 = mbv_ZeroA32
    self.mbv_mK32 = mbv_mK32
    self.fUpdConf = int(confMB["fUpdConf"])
    self.BaseMain = int(confMB["BaseMain"])
    self.BaseCopy = int(confMB["BaseCopy"])
    self.offs_addr = int(confMB["offs_addr"])
    self.offs_thrAT = int(confMB["offs_thrAT"])
    self.offs_ZeroA32 = int(confMB["offs_ZeroA32"])
    self.offs_mK32 = int(confMB["offs_mK32"])
    self.offs_ADC_mode = int(confMB["offs_ADC_mode"])
    self.offs_ADC_conf = int(confMB["offs_ADC_conf"])
    self.offs_ADC_IO = int(confMB["offs_ADC_IO"])
    self.offs_SerNum = int(confMB["offs_SerNum"])
    self.offs_B_ = int(confMB["offs_B_"])
    try:
      self.offs_Descr = int(confMB["offs_Descr"])
      self.offs_TypeID = int(confMB["offs_TypeID"])
    except:q=0

    
    self.offs_PD47_OUTPUT = int(confMB["offs_PD47_OUTPUT"])
    self.offs_PB5_Meandr = int(confMB["offs_PB5_Meandr"])

    self.offs_Aet_1 = int(confMB["offs_Aet_1"])
    self.offs_Aet_2 = int(confMB["offs_Aet_2"])
    self.offs_Aet_3 = int(confMB["offs_Aet_3"])
    self.offs_Aet_4 = int(confMB["offs_Aet_4"])
    self.offs_Aet_5 = int(confMB["offs_Aet_5"])
    self.offs_Aet_6 = int(confMB["offs_Aet_6"])
    self.offs_Nt_1 = int(confMB["offs_Nt_1"])
    self.offs_Nt_2 = int(confMB["offs_Nt_2"])
    self.offs_Nt_3 = int(confMB["offs_Nt_3"])
    self.mba_PD47 = int(confMB["PD47_OUTPUT"])
    self.mba_PB5 = int(confMB["PB5_Meandr"])
    self.mba_Aet_1 = int(confMB["Aet_1"])
    self.mba_Aet_2 = int(confMB["Aet_2"])
    self.mba_Aet_3 = int(confMB["Aet_3"])
    self.mba_Aet_4 = int(confMB["Aet_4"])
    self.mba_Aet_5 = int(confMB["Aet_5"])
    self.mba_Aet_6 = int(confMB["Aet_6"])
    self.mba_B_ = int(confMB["B_"])
    self.mba_Nt_1 = int(confMB["Nt_1"])
    self.mba_Nt_2 = int(confMB["Nt_2"])
    self.mba_Nt_3 = int(confMB["Nt_3"])

    self.leAddrMB.editingFinished.connect(self.on_leAddrMBFinished)
    self.tbAddrMBRd.clicked.connect(self.on_tbAddrMBRd_toggle)
    self.tbAddrMBWr.clicked.connect(self.on_tbAddrMBWr_toggle)
    self.lethrAT.editingFinished.connect(self.on_lethrATFinished)
    self.tbthrATRd.clicked.connect(self.on_tbthrATRd_toggle)
    self.tbthrATWr.clicked.connect(self.on_tbthrATWr_toggle)
    self.leZeroA.editingFinished.connect(self.on_leZeroAFinished)
    self.tbZeroARdVar.clicked.connect(self.on_tbZeroARdVar_toggle)
    self.tbZeroARd.clicked.connect(self.on_tbZeroARd_toggle)
    self.tbZeroAWr.clicked.connect(self.on_tbZeroAWr_toggle)
    self.lemK.editingFinished.connect(self.on_lemKFinished)
    self.tbmKRdVar.clicked.connect(self.on_tbmKRdVar_toggle)
    self.tbmKRd.clicked.connect(self.on_tbmKRd_toggle)
    self.tbmKWr.clicked.connect(self.on_tbmKWr_toggle)    
    self.leMode.editingFinished.connect(self.on_leModeFinished)
    self.tbModeRd.clicked.connect(self.on_tbModeRd_toggle)
    self.tbModeWr.clicked.connect(self.on_tbModeWr_toggle)
    self.leConf.editingFinished.connect(self.on_leConfFinished)
    self.tbConfRd.clicked.connect(self.on_tbConfRd_toggle)
    self.tbConfWr.clicked.connect(self.on_tbConfWr_toggle)
    self.leIO.editingFinished.connect(self.on_leIOFinished)
    self.tbIORd.clicked.connect(self.on_tbIORd_toggle)
    self.tbIOWr.clicked.connect(self.on_tbIOWr_toggle)
    self.leSerNum.editingFinished.connect(self.on_leSerNumFinished)
    self.tbSerNumRd.clicked.connect(self.on_tbSerNumRd_toggle)
    self.tbSerNumWr.clicked.connect(self.on_tbSerNumWr_toggle)
    self.teDescribe.cursorPositionChanged.connect(self.on_teDescribeFinished)
    self.tbDescribeRd.clicked.connect(self.on_tbDescribeRd_toggle)
    self.tbDescribeWr.clicked.connect(self.on_tbDescribemWr_toggle)
    self.leTypeID.editingFinished.connect(self.on_leTypeIDFinished)
    self.tbTypeIDRd.clicked.connect(self.on_tbTypeIDRd_toggle)
    self.tbTypeIDWr.clicked.connect(self.on_tbTypeIDWr_toggle)

    self.lePD47.editingFinished.connect(self.on_lePD47Finished)
    self.tbPD47Rd.clicked.connect(self.on_tbPD47Rd_toggle)
    self.tbPD47Var.clicked.connect(self.on_tbPD47Var_toggle)
    self.tbPD47Wr.clicked.connect(self.on_tbPD47Wr_toggle)
    self.lePB5.editingFinished.connect(self.on_lePB5Finished)
    self.tbPB5Rd.clicked.connect(self.on_tbPB5Rd_toggle)
    self.tbPB5Var.clicked.connect(self.on_tbPB5Var_toggle)
    self.tbPB5Wr.clicked.connect(self.on_tbPB5Wr_toggle)

    self.leAet_1.editingFinished.connect(self.on_leAet_1Finished)
    self.tbAetRd_1.clicked.connect(self.on_tbAetRd_1_toggle)
    self.tbAetVar_1.clicked.connect(self.on_tbAetVar_1_toggle)
    self.tbAetWr_1.clicked.connect(self.on_tbAetWr_1_toggle)
    self.leAet_2.editingFinished.connect(self.on_leAet_2Finished)
    self.tbAetRd_2.clicked.connect(self.on_tbAetRd_2_toggle)
    self.tbAetVar_2.clicked.connect(self.on_tbAetVar_2_toggle)
    self.tbAetWr_2.clicked.connect(self.on_tbAetWr_2_toggle)
    self.leAet_3.editingFinished.connect(self.on_leAet_3Finished)
    self.tbAetRd_3.clicked.connect(self.on_tbAetRd_3_toggle)
    self.tbAetVar_3.clicked.connect(self.on_tbAetVar_3_toggle)
    self.tbAetWr_3.clicked.connect(self.on_tbAetWr_3_toggle)
    self.leAet_4.editingFinished.connect(self.on_leAet_4Finished)
    self.tbAetRd_4.clicked.connect(self.on_tbAetRd_4_toggle)
    self.tbAetVar_4.clicked.connect(self.on_tbAetVar_4_toggle)
    self.tbAetWr_4.clicked.connect(self.on_tbAetWr_4_toggle)
    self.leAet_5.editingFinished.connect(self.on_leAet_5Finished)
    self.tbAetRd_5.clicked.connect(self.on_tbAetRd_5_toggle)
    self.tbAetVar_5.clicked.connect(self.on_tbAetVar_5_toggle)
    self.tbAetWr_5.clicked.connect(self.on_tbAetWr_5_toggle)
    self.leAet_6.editingFinished.connect(self.on_leAet_6Finished)
    self.tbAetRd_6.clicked.connect(self.on_tbAetRd_6_toggle)
    self.tbAetVar_6.clicked.connect(self.on_tbAetVar_6_toggle)
    self.tbAetWr_6.clicked.connect(self.on_tbAetWr_6_toggle)

    self.leB_.editingFinished.connect(self.on_leB_Finished)
    self.tbB_Rd.clicked.connect(self.on_tbB_Rd_toggle)
    self.tbB_Var.clicked.connect(self.on_tbB_Var_toggle)
    self.tbB_Wr.clicked.connect(self.on_tbB_Wr_toggle)

    self.leNt_1.editingFinished.connect(self.on_leNt_1Finished)
    self.tbNtRd_1.clicked.connect(self.on_tbNtRd_1_toggle)
    self.tbNtVar_1.clicked.connect(self.on_tbNtVar_1_toggle)
    self.tbNtWr_1.clicked.connect(self.on_tbNtWr_1_toggle)
    self.leNt_2.editingFinished.connect(self.on_leNt_2Finished)
    self.tbNtRd_2.clicked.connect(self.on_tbNtRd_2_toggle)
    self.tbNtVar_2.clicked.connect(self.on_tbNtVar_2_toggle)
    self.tbNtWr_2.clicked.connect(self.on_tbNtWr_2_toggle)
    self.leNt_3.editingFinished.connect(self.on_leNt_3Finished)
    self.tbNtRd_3.clicked.connect(self.on_tbNtRd_3_toggle)
    self.tbNtVar_3.clicked.connect(self.on_tbNtVar_3_toggle)
    self.tbNtWr_3.clicked.connect(self.on_tbNtWr_3_toggle)

    self.leSerNum_S.editingFinished.connect(self.on_leSerNum_SFinished)
    self.leAddrMB_S.editingFinished.connect(self.on_leAddrMB_SFinished)
    self.tbNewAddr_Wr.clicked.connect(self.on_tbNewAddr_Wr_toggle)

    self.tbSave.clicked.connect(self.on_tbSave_toggle)

    self.n_Describe=''


  def show(self, DirID, addrMB):
    """ DirID - активное направление MODBUS 
        addrMB - адрес конфигурируемого милливольтметра на направлении DirID """
    self.DirID = DirID
    self.addrMB = addrMB
    self.setWindowTitle(self.wnCaption + " [{:02X}h]".format(self.addrMB))
    super().show()


  def on_leAddrMBFinished(self):
    try:
      self.n_addrMB = eval(self.leAddrMB.text(), {}, {})
    except:
      self.leAddrMB.setText(str(ToUns16(self.n_addrMB)))
      print(sys.exc_info())   # TODO логирование
    self.leAddrMB.clearFocus()    


  def on_tbAddrMBRd_toggle(self):
    try:
      tmpT = svimb.ReadRegs16(self.DirID, self.addrMB, self.BaseCopy + self.offs_addr, 1) 
      self.n_addrMB = tmpT[0]
      self.leAddrMB.setText(str(ToUns16(self.n_addrMB)))    
    except:
      self.leAddrMB.setText('?') 
      print(sys.exc_info())   # TODO логирование


  def on_tbAddrMBWr_toggle(self):
    try:
      self.leAddrMB.clearFocus() 
      self.n_addrMB = svimb.WriteReg16(self.DirID, self.addrMB, self.BaseCopy + self.offs_addr, self.n_addrMB)
      self.leAddrMB.setText(str(ToUns16(self.n_addrMB)))
    except:
      self.leAddrMB.setText('?')
      print(sys.exc_info())   # TODO логирование
    

  def on_lethrATFinished(self):
    try:
      self.n_thrAT = eval(self.lethrAT.text(), {}, {})
    except:
      self.lethrAT.setText(str(ToUns16(self.n_thrAT)))
      print(sys.exc_info())   # TODO логирование
    self.lethrAT.clearFocus() 


  def on_tbthrATRd_toggle(self):
    try:
      tmpT = svimb.ReadRegs16(self.DirID, self.addrMB, self.BaseCopy + self.offs_thrAT, 1) 
      self.n_thrAT = tmpT[0]
      self.lethrAT.setText(str(ToUns16(self.n_thrAT)))    
    except:
      self.lethrAT.setText('?') 
      print(sys.exc_info())   # TODO логирование


  def on_tbthrATWr_toggle(self):
    try:
      self.lethrAT.clearFocus() 
      self.n_thrAT = svimb.WriteReg16(self.DirID, self.addrMB, self.BaseCopy + self.offs_thrAT, self.n_thrAT)
      self.lethrAT.setText(str(ToUns16(self.n_thrAT))) 
    except:
      self.lethrAT.setText('?')
      print(sys.exc_info())   # TODO логирование

 
  def on_leZeroAFinished(self):
    try:
      self.n_ZeroA = eval(self.leZeroA.text(), {}, {})
    except:
      self.leZeroA.setText(str(self.n_ZeroA))
      print(sys.exc_info())   # TODO логирование
    self.leZeroA.clearFocus() 

  
  def on_tbZeroARdVar_toggle(self):
    try:
      (rlow, rhigh) = svimb.ReadRegs16(self.DirID, self.addrMB, self.mbv_ZeroA32, 2)
      self.n_ZeroA = ToUns32(rlow, rhigh)
      self.leZeroA.setText(str(self.n_ZeroA ))    
    except:
      self.leZeroA.setText('?') 
      print(sys.exc_info())   # TODO логирование


  def on_tbZeroARd_toggle(self):
    try:
      (rlow, rhigh) = svimb.ReadRegs16(self.DirID, self.addrMB, self.BaseCopy + self.offs_ZeroA32, 2)
      self.n_ZeroA = ToUns32(rlow, rhigh)
      self.leZeroA.setText(str(self.n_ZeroA ))    
    except:
      self.leZeroA.setText('?') 
      print(sys.exc_info())   # TODO логирование


  def on_tbZeroAWr_toggle(self):
    try:
      self.leZeroA.clearFocus()
      svimb.WriteReg16(self.DirID, self.addrMB, self.BaseCopy + self.offs_ZeroA32, self.n_ZeroA & 0xffff)
      svimb.WriteReg16(self.DirID, self.addrMB, self.BaseCopy + self.offs_ZeroA32 + 1, (self.n_ZeroA & 0xffff0000) >> 16)
    except:
      self.leZeroA.setText('?')
      print(sys.exc_info())   # TODO логирование 


  def on_lemKFinished(self):
    try:
      self.n_mK = eval(self.lemK.text(), {}, {})
    except:
      self.lemK.setText(str(self.n_mK))
      print(sys.exc_info())   # TODO логирование
    self.lemK.clearFocus() 


  def on_tbmKRdVar_toggle(self):
    try:
      (rlow, rhigh) = svimb.ReadRegs16(self.DirID, self.addrMB, self.mbv_mK32, 2)
      self.n_mK = ToSig32(rlow, rhigh)
      self.lemK.setText(str(self.n_mK))    
    except:
      self.lemK.setText('?') 
      print(sys.exc_info())   # TODO логирование


  def on_tbmKRd_toggle(self):
    try:
      (rlow, rhigh) = svimb.ReadRegs16(self.DirID, self.addrMB, self.BaseCopy + self.offs_mK32, 2)
      self.n_mK = ToSig32(rlow, rhigh)
      self.lemK.setText(str(self.n_mK))    
    except:
      self.lemK.setText('?') 
      print(sys.exc_info())   # TODO логирование


  def on_tbmKWr_toggle(self):
    try:
      self.lemK.clearFocus()
      svimb.WriteReg16(self.DirID, self.addrMB, self.BaseCopy + self.offs_mK32, self.n_mK & 0xffff)
      svimb.WriteReg16(self.DirID, self.addrMB, self.BaseCopy + self.offs_mK32 + 1, (self.n_mK & 0xffff0000) >> 16)
    except:
      self.lemK.setText('?')
      print(sys.exc_info())   # TODO логирование


  def on_leModeFinished(self):
    try:
      self.n_ADC_mode = int(self.leMode.text(), 16)
    except:
      self.leMode.setText("{:04X}".format(self.n_ADC_mode))
      print(sys.exc_info())   # TODO логирование
    self.leMode.clearFocus()  


  def on_tbModeRd_toggle(self):
    try:
      tmpT = svimb.ReadRegs16(self.DirID, self.addrMB, self.BaseCopy + self.offs_ADC_mode, 1) 
      self.n_ADC_mode = ToUns16(tmpT[0])
      self.leMode.setText("{:04X}".format(self.n_ADC_mode))    
    except:
      self.leMode.setText('?') 
      print(sys.exc_info())   # TODO логирование


  def on_tbModeWr_toggle(self):
    try:
      self.leMode.clearFocus() 
      self.n_ADC_mode = ToUns16(svimb.WriteReg16(self.DirID, self.addrMB, self.BaseCopy + self.offs_ADC_mode, self.n_ADC_mode))
      self.leMode.setText("{:04X}".format(self.n_ADC_mode)) 
    except:
      self.leMode.setText('?')
      print(sys.exc_info())   # TODO логирование
 

  def on_leConfFinished(self):
    try:
      self.n_ADC_conf = int(self.leConf.text(), 16)
    except:
      self.leConf.setText("{:04X}".format(self.n_ADC_conf))
      print(sys.exc_info())   # TODO логирование
    self.leConf.clearFocus() 


  def on_tbConfRd_toggle(self):
    try:
      tmpT = svimb.ReadRegs16(self.DirID, self.addrMB, self.BaseCopy + self.offs_ADC_conf, 1) 
      self.n_ADC_conf = ToUns16(tmpT[0])
      self.leConf.setText("{:04X}".format(self.n_ADC_conf))    
    except:
      self.leConf.setText('?') 
      print(sys.exc_info())   # TODO логирование


  def on_tbConfWr_toggle(self):
    try:
      self.leConf.clearFocus() 
      self.n_ADC_conf = ToUns16(svimb.WriteReg16(self.DirID, self.addrMB, self.BaseCopy + self.offs_ADC_conf, self.n_ADC_conf))
      self.leConf.setText("{:04X}".format(self.n_ADC_conf)) 
    except:
      self.leConf.setText('?')
      print(sys.exc_info())   # TODO логирование


  def on_leIOFinished(self):
    try:
      self.n_ADC_IO = int(self.leIO.text(), 16) & 0xff
    except:
      self.leIO.setText("{:02X}".format(self.n_ADC_IO))
      print(sys.exc_info())   # TODO логирование
    self.leIO.clearFocus() 


  def on_tbIORd_toggle(self):
    try:
      tmpT = svimb.ReadRegs16(self.DirID, self.addrMB, self.BaseCopy + self.offs_ADC_IO, 1) 
      self.n_ADC_IO = (ToUns16(tmpT[0])) & 0xff
      self.leIO.setText("{:02X}".format(self.n_ADC_IO))    
    except:
      self.leIO.setText('?') 
      print(sys.exc_info())   # TODO логирование


  def on_tbIOWr_toggle(self):
    try:
      self.leIO.clearFocus() 
      self.n_ADC_IO = (ToUns16(svimb.WriteReg16(self.DirID, self.addrMB, self.BaseCopy + self.offs_ADC_IO, self.n_ADC_IO))) & 0xff
      self.leIO.setText("{:02X}".format(self.n_ADC_IO))   
    except:
      self.leIO.setText('?')
      print(sys.exc_info())   # TODO логирование


  def on_leSerNumFinished(self):
    try:
      self.n_SerNum = eval(self.leSerNum.text(), {}, {})
    except:
      self.leSerNum.setText(str(self.n_SerNum))
      LL.exception('')
    self.leSerNum.clearFocus() 


  def on_tbSerNumRd_toggle(self):
    try:
      tmpT = svimb.ReadRegs16(self.DirID, self.addrMB, self.BaseCopy + self.offs_SerNum, 1) 
      self.n_SerNum = ToUns16(tmpT[0])
      self.leSerNum.setText(str(self.n_SerNum))    
    except:
      self.leSerNum.setText('?') 
      LL.exception('')


  def on_tbSerNumWr_toggle(self):
    try:
      self.leSerNum.clearFocus() 
      self.n_SerNum = ToUns16(svimb.WriteReg16(self.DirID, self.addrMB, self.BaseCopy + self.offs_SerNum, self.n_SerNum))
      self.leSerNum.setText(str(self.n_SerNum))  
    except:
      self.leSerNum.setText('?') 
      LL.exception('')

  def on_teDescribeFinished(self):
    a=1
    '''try:
      #self.n_Describe = eval(self.teDescribe.text(), {}, {})
      a=1
    except:
      self.teDescribe.setText(str(self.n_Describe))
      LL.exception('')
    self.teDescribe.clearFocus()''' 


  def on_tbDescribeRd_toggle(self):
    try:
      i=0
      j=0
      tmpt=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
      tmptxt=''

      try:
       tmpt=svimb.ReadRegs16(self.DirID, self.addrMB, self.BaseCopy + self.offs_Descr+i, 70)
       while(i<66):
        tmptxt=tmptxt+chr( tmpt[i])
        i=i+1
      except: a=0
      self.n_Describe=tmptxt
      
      self.teDescribe.setText(str(self.n_Describe))    
    except:
      self.teDescribe.setText('?') 
      LL.exception('')


  def on_tbDescribemWr_toggle(self):
    try:
      self.n_Describe = self.teDescribe.text()

      Tmpt=[ord(c) for c in self.n_Describe]
      ltxt=len(self.n_Describe)


      self.teDescribe.clearFocus() 
      i=0
      while(i<ltxt):
       svimb.WriteReg16(self.DirID, self.addrMB, self.BaseCopy + self.offs_Descr+i, Tmpt[i])
       i=i+1
      self.teDescribe.setText(str(self.n_Describe))  
    except:
      self.teDescribe.setText('?') 
      LL.exception('')


  def on_leTypeIDFinished(self):
    try:
      self.n_TypeID = eval(self.leTypeID.text(), {}, {})
    except:
      self.leTypeID.setText(str(self.n_TypeID))
      LL.exception('')
    self.leSerNum.clearFocus() 


  def on_tbTypeIDRd_toggle(self):
    try:
      tmpT = svimb.ReadRegs16(self.DirID, self.addrMB, self.BaseCopy + self.offs_TypeID, 1) 
      self.n_TypeID = ToUns16(tmpT[0])
      self.leTypeID.setText(str(self.n_TypeID))    
    except:
      self.leTypeID.setText('?') 
      LL.exception('')


  def on_tbTypeIDWr_toggle(self):
    try:
      self.leTypeID.clearFocus() 
      self.n_TypeID = ToUns16(svimb.WriteReg16(self.DirID, self.addrMB, self.BaseCopy + self.offs_TypeID, self.n_TypeID))
      self.leTypeID.setText(str(self.n_TypeID))  
    except:
      self.leTypeID.setText('?') 
      LL.exception('')

  def on_lePD47Finished(self):
    try:
      self.n_PD47 = eval(self.lePD47.text(), {}, {})
    except:
      self.lePD47.setText(str(self.n_PD47))
      LL.exception('')
    self.lePD47.clearFocus() 


  def on_tbPD47Rd_toggle(self):
    try:
      tmpT = svimb.ReadRegs16(self.DirID, self.addrMB, self.BaseCopy + self.offs_PD47_OUTPUT, 1) 
      self.n_PD47 = ToUns16(tmpT[0])
      self.lePD47.setText(str(self.n_PD47))    
    except:
      self.lePD47.setText('?') 
      LL.exception('')

  def on_tbPD47Var_toggle(self):
    try:

      tmpT = svimb.ReadRegs16(self.DirID, self.addrMB, self.mba_PD47, 1)
      self.n_PD47_ = ToUns16(tmpT[0])
      self.lePD47.setText(str(self.n_PD47_))    
    except:
      self.lemK.setText('?') 
      print(sys.exc_info())   # TODO логирование

  def on_tbPD47Wr_toggle(self):
    try:
      self.leSerNum.clearFocus() 
      self.n_PD47 = ToUns16(svimb.WriteReg16(self.DirID, self.addrMB, self.BaseCopy + self.offs_PD47_OUTPUT, self.n_PD47))
      self.lePD47.setText(str(self.n_PD47))  
    except:
      self.lePD47.setText('?') 
      LL.exception('')

  def on_lePB5Finished(self):
    try:
      self.n_PB5 = eval(self.lePB5.text(), {}, {})
    except:
      self.lePB5.setText(str(self.n_PB5))
      LL.exception('')
    self.lePB5.clearFocus() 


  def on_tbPB5Rd_toggle(self):
    try:
      tmpT = svimb.ReadRegs16(self.DirID, self.addrMB, self.BaseCopy + self.offs_PB5_Meandr, 1) 
      self.n_PB5 = ToUns16(tmpT[0])
      self.lePB5.setText(str(self.n_PB5))    
    except:
      self.lePB5.setText('?') 
      LL.exception('')

  def on_tbPB5Var_toggle(self):
    try:

      tmpT = svimb.ReadRegs16(self.DirID, self.addrMB, self.mba_PB5, 1)
      self.n_PB5_= ToUns16(tmpT[0]) 
      self.lePB5.setText(str(self.n_PB5_))    
    except:
      self.lePB5.setText('?') 
      print(sys.exc_info())   # TODO логирование

  def on_tbPB5Wr_toggle(self):
    try:
      self.lePB5.clearFocus() 
      self.n_PB5 = ToUns16(svimb.WriteReg16(self.DirID, self.addrMB, self.BaseCopy + self.offs_PB5_Meandr, self.n_PB5))
      self.lePB5.setText(str(self.n_PB5))  
    except:
      self.lePB5.setText('?') 
      LL.exception('')

  def on_leAet_1Finished(self):
    try:
      self.n_Aet_1 = eval(self.leAet_1.text(), {}, {})
    except:
      self.leAet_1.setText(str(self.n_Aet_1))
      LL.exception('')
    self.leAet_1.clearFocus() 

  def on_tbAetRd_1_toggle(self):
    try:

      (rlow, rhigh) = svimb.ReadRegs16(self.DirID, self.addrMB, self.BaseCopy + self.offs_Aet_1, 2) 
      self.n_Aet_1 = ToUns32(rlow, rhigh)/10**3
      self.leAet_1.setText(str(self.n_Aet_1))    
    except:
      self.leAet_1.setText('?') 
      LL.exception('')

  def on_tbAetVar_1_toggle(self):
    try:
      (rlow, rhigh)  = svimb.ReadRegs16(self.DirID, self.addrMB, self.mba_Aet_1, 2)
      self.n_Aet_1= ToUns32(rlow, rhigh)/10**3
      self.leAet_1.setText(str(self.n_Aet_1))    
    except:
      self.leAet_1.setText('?') 
      print(sys.exc_info())   # TODO логирование

  def on_tbAetWr_1_toggle(self):
    try:
      self.leAet_1.clearFocus() 
      svimb.WriteReg16(self.DirID, self.addrMB, self.BaseCopy + self.offs_Aet_1, round(self.n_Aet_1*10**3) & 0xffff)
      svimb.WriteReg16(self.DirID, self.addrMB, self.BaseCopy + self.offs_Aet_1+1, (round(self.n_Aet_1*10**3) & 0xffff0000) >> 16)
      self.leAet_1.setText(str(self.n_Aet_1))  
    except:
      self.leAet_1.setText('?') 
      LL.exception('')

  def on_leAet_2Finished(self):
    try:
      self.n_Aet_2 = eval(self.leAet_2.text(), {}, {})
    except:
      self.leAet_2.setText(str(self.n_Aet_2))
      LL.exception('')
    self.leAet_2.clearFocus() 

  def on_tbAetRd_2_toggle(self):
    try:
      (rlow, rhigh) = svimb.ReadRegs16(self.DirID, self.addrMB, self.BaseCopy + self.offs_Aet_2, 2) 
      self.n_Aet_2 = ToUns32(rlow, rhigh)/10**3
      self.leAet_2.setText(str(self.n_Aet_2))    
    except:
      self.leAet_2.setText('?') 
      LL.exception('')

  def on_tbAetVar_2_toggle(self):
    try:
      (rlow, rhigh)  = svimb.ReadRegs16(self.DirID, self.addrMB, self.mba_Aet_2, 2)
      self.n_Aet_2= ToUns32(rlow, rhigh)/10**3
      self.leAet_2.setText(str(self.n_Aet_2))    
    except:
      self.leAet_2.setText('?') 
      print(sys.exc_info())   # TODO логирование

  def on_tbAetWr_2_toggle(self):
    try:
      self.leAet_2.clearFocus() 
      svimb.WriteReg16(self.DirID, self.addrMB, self.BaseCopy + self.offs_Aet_2, round(self.n_Aet_2*10**3) & 0xffff)##3
      svimb.WriteReg16(self.DirID, self.addrMB, self.BaseCopy + self.offs_Aet_2+1, (round(self.n_Aet_2*10**3) & 0xffff0000) >> 16)##3
      self.leAet_2.setText(str(self.n_Aet_2))  
    except:
      self.leAet_2.setText('?') 
      LL.exception('')

  def on_leAet_3Finished(self):
    try:
      self.n_Aet_3 = eval(self.leAet_3.text(), {}, {})
    except:
      self.leAet_3.setText(str(self.n_Aet_3))
      LL.exception('')
    self.leAet_3.clearFocus() 

  def on_tbAetRd_3_toggle(self):
    try:
      (rlow, rhigh) = svimb.ReadRegs16(self.DirID, self.addrMB, self.BaseCopy + self.offs_Aet_3, 2) 
      self.n_Aet_3 = ToUns32(rlow, rhigh)/10**47
      self.leAet_3.setText(str(self.n_Aet_3))    
    except:
      self.leAet_3.setText('?') 
      LL.exception('')

  def on_tbAetVar_3_toggle(self):
    try:
      (rlow, rhigh)  = svimb.ReadRegs16(self.DirID, self.addrMB, self.mba_Aet_3, 2)
      self.n_Aet_3= ToUns32(rlow, rhigh)/10**4
      self.leAet_3.setText(str(self.n_Aet_3))    
    except:
      self.leAet_3.setText('?') 
      print(sys.exc_info())   # TODO логирование

  def on_tbAetWr_3_toggle(self):
    try:
      self.leAet_3.clearFocus() 
      svimb.WriteReg16(self.DirID, self.addrMB, self.BaseCopy + self.offs_Aet_3, round(self.n_Aet_3*10**4) & 0xffff)
      svimb.WriteReg16(self.DirID, self.addrMB, self.BaseCopy + self.offs_Aet_3+1, (round(self.n_Aet_3*10**4) & 0xffff0000) >> 16)
      self.leAet_3.setText(str(self.n_Aet_3))  
    except:
      self.leAet_3.setText('?') 
      LL.exception('')

  def on_leAet_4Finished(self):
    try:
      self.n_Aet_4 = eval(self.leAet_4.text(), {}, {})
    except:
      self.leAet_4.setText(str(self.n_Aet_4))
      LL.exception('')
    self.leAet_4.clearFocus() 

  def on_tbAetRd_4_toggle(self):
    try:
      (rlow, rhigh) = svimb.ReadRegs16(self.DirID, self.addrMB, self.BaseCopy + self.offs_Aet_4, 2) 
      self.n_Aet_4 = ToUns32(rlow, rhigh)/10**5
      self.leAet_4.setText(str(self.n_Aet_4))    
    except:
      self.leAet_4.setText('?') 
      LL.exception('')

  def on_tbAetVar_4_toggle(self):
    try:
      (rlow, rhigh)  = svimb.ReadRegs16(self.DirID, self.addrMB, self.mba_Aet_4, 2)
      self.n_Aet_4= ToUns32(rlow, rhigh)/10**5
      self.leAet_4.setText(str(self.n_Aet_4))    
    except:
      self.leAet_4.setText('?') 
      print(sys.exc_info())   # TODO логирование

  def on_tbAetWr_4_toggle(self):
    try:
      self.leAet_4.clearFocus() 
      svimb.WriteReg16(self.DirID, self.addrMB, self.BaseCopy + self.offs_Aet_4, round(self.n_Aet_4*10**5) & 0xffff)
      svimb.WriteReg16(self.DirID, self.addrMB, self.BaseCopy + self.offs_Aet_4+1, (round(self.n_Aet_4*10**5) & 0xffff0000) >> 16)
      self.leAet_4.setText(str(self.n_Aet_4))  
    except:
      self.leAet_4.setText('?') 
      LL.exception('')

  def on_leAet_5Finished(self):
    try:
      self.n_Aet_5 = eval(self.leAet_5.text(), {}, {})
    except:
      self.leAet_5.setText(str(self.n_Aet_5))
      LL.exception('')
    self.leAet_5.clearFocus() 

  def on_tbAetRd_5_toggle(self):
    try:
      (rlow, rhigh) = svimb.ReadRegs16(self.DirID, self.addrMB, self.BaseCopy + self.offs_Aet_5, 2) 
      self.n_Aet_5 = ToUns32(rlow, rhigh)/10**6
      self.leAet_5.setText(str(self.n_Aet_5))    
    except:
      self.leAet_5.setText('?') 
      LL.exception('')

  def on_tbAetVar_5_toggle(self):
    try:
      (rlow, rhigh)  = svimb.ReadRegs16(self.DirID, self.addrMB, self.mba_Aet_5, 2)
      self.n_Aet_5= ToUns32(rlow, rhigh)/10**6
      self.leAet_5.setText(str(self.n_Aet_5))    
    except:
      self.leAet_5.setText('?') 
      print(sys.exc_info())   # TODO логирование

  def on_tbAetWr_5_toggle(self):
    try:
      self.leAet_5.clearFocus() 
      svimb.WriteReg16(self.DirID, self.addrMB, self.BaseCopy + self.offs_Aet_5, round(self.n_Aet_5*10**6) & 0xffff)
      svimb.WriteReg16(self.DirID, self.addrMB, self.BaseCopy + self.offs_Aet_5+1, (round(self.n_Aet_5*10**6) & 0xffff0000) >> 16)
      self.leAet_5.setText(str(self.n_Aet_5))  
    except:
      self.leAet_5.setText('?') 
      LL.exception('')

  def on_leAet_6Finished(self):
    try:
      self.n_Aet_6 = eval(self.leAet_6.text(), {}, {})
    except:
      self.leAet_6.setText(str(self.n_Aet_6))
      LL.exception('')
    self.leAet_6.clearFocus() 

  def on_tbAetRd_6_toggle(self):
    try:
      (rlow, rhigh) = svimb.ReadRegs16(self.DirID, self.addrMB, self.BaseCopy + self.offs_Aet_6, 2) 
      self.n_Aet_6 = ToUns32(rlow, rhigh)/10**7
      self.leAet_6.setText(str(self.n_Aet_6))    
    except:
      self.leAet_6.setText('?') 
      LL.exception('')

  def on_tbAetVar_6_toggle(self):
    try:
      (rlow, rhigh)  = svimb.ReadRegs16(self.DirID, self.addrMB, self.mba_Aet_6, 2)
      self.n_Aet_6= ToUns32(rlow, rhigh)/10**7
      self.leAet_6.setText(str(self.n_Aet_6))    
    except:
      self.leAet_6.setText('?') 
      print(sys.exc_info())   # TODO логирование

  def on_tbAetWr_6_toggle(self):
    try:
      self.leAet_6.clearFocus() 
      svimb.WriteReg16(self.DirID, self.addrMB, self.BaseCopy + self.offs_Aet_6, round(self.n_Aet_6*10**7) & 0xffff)
      svimb.WriteReg16(self.DirID, self.addrMB, self.BaseCopy + self.offs_Aet_6+1, (round(self.n_Aet_6*10**7) & 0xffff0000) >> 16)
      self.leAet_6.setText(str(self.n_Aet_6))  
    except:
      self.leAet_6.setText('?') 
      LL.exception('')

#######################################################
  def on_leB_Finished(self):
    try:
      self.n_leB_ = eval(self.leB_.text(), {}, {})
    except:
      self.leB_.setText(str(self.n_leB_))
      LL.exception('')
    self.leB_.clearFocus() 

  def on_tbB_Rd_toggle(self):
    try:

      (rlow, rhigh) = svimb.ReadRegs16(self.DirID, self.addrMB, self.BaseCopy + self.offs_B_, 2) 
      self.n_B_ = ToSig32(rlow, rhigh)/10**7
      self.leB_.setText(str(self.n_B_))    
    except:
      self.leB_.setText('?') 
      LL.exception('')

  def on_tbB_Var_toggle(self):
    try:
      (rlow, rhigh)  = svimb.ReadRegs16(self.DirID, self.addrMB, self.mba_B_, 2)
      self.n_B_= ToSig32(rlow, rhigh)/10**7
      self.leB_.setText(str(self.n_B_))    
    except:
      self.leB_.setText('?') 
      print(sys.exc_info())   # TODO логирование

  def on_tbB_Wr_toggle(self):
    try:
      self.leB_.clearFocus() 
      svimb.WriteReg16(self.DirID, self.addrMB, self.BaseCopy + self.offs_B_, round(self.n_B_*10**7) & 0xffff)
      svimb.WriteReg16(self.DirID, self.addrMB, self.BaseCopy + self.offs_B_+1, (round(self.n_B_*10**7) & 0xffff0000) >> 16)
      self.leB_.setText(str(self.n_B_))  
    except:
      self.leB_.setText('?') 
      LL.exception('')

#######################################################

  def on_leNt_1Finished(self):
    try:
      self.n_Nt_1 = eval(self.leNt_1.text(), {}, {})
    except:
      self.leNt_1.setText(str(self.n_Nt_1))
      LL.exception('')
    self.leNt_1.clearFocus() 

  def on_tbNtRd_1_toggle(self):
    try:
      tmpT = svimb.ReadRegs16(self.DirID, self.addrMB, self.BaseCopy + self.offs_Nt_1, 2) 
      self.n_Nt_1 =  ToUns16(tmpT[0])
      self.leNt_1.setText(str(self.n_Nt_1))    
    except:
      self.leNt_1.setText('?') 
      LL.exception('')

  def on_tbNtVar_1_toggle(self):
    try:
      tmpT= svimb.ReadRegs16(self.DirID, self.addrMB, self.mba_Nt_1, 2)
      self.n_Nt_1_= ToUns16(tmpT[0])
      self.leNt_1.setText(str(self.n_Nt_1_))    
    except:
      self.leNt_1.setText('?') 
      print(sys.exc_info())   # TODO логирование

  def on_tbNtWr_1_toggle(self):
    try:
      self.leNt_1.clearFocus() 
      svimb.WriteReg16(self.DirID, self.addrMB, self.BaseCopy + self.offs_Nt_1, self.n_Nt_1 & 0xffff)
      self.leNt_1.setText(str(self.n_Nt_1))  
    except:
      self.leNt_1.setText('?') 
      LL.exception('')

  def on_leNt_2Finished(self):
    try:
      self.n_Nt_2 = eval(self.leNt_2.text(), {}, {})
    except:
      self.leNt_2.setText(str(self.n_Nt_2))
      LL.exception('')
    self.leNt_2.clearFocus() 

  def on_tbNtRd_2_toggle(self):
    try:
      tmpT = svimb.ReadRegs16(self.DirID, self.addrMB, self.BaseCopy + self.offs_Nt_2, 2) 
      self.n_Nt_2 =  ToUns16(tmpT[0])
      self.leNt_2.setText(str(self.n_Nt_2))    
    except:
      self.leNt_2.setText('?') 
      LL.exception('')

  def on_tbNtVar_2_toggle(self):
    try:
      tmpT = svimb.ReadRegs16(self.DirID, self.addrMB, self.mba_Nt_2, 2)
      self.n_Nt_2_= ToUns16(tmpT[0])
      self.leNt_2.setText(str(self.n_Nt_2_))    
    except:
      self.leNt_2.setText('?') 
      print(sys.exc_info())   # TODO логирование

  def on_tbNtWr_2_toggle(self):
    try:
      self.leNt_2.clearFocus() 
      svimb.WriteReg16(self.DirID, self.addrMB, self.BaseCopy + self.offs_Nt_2, self.n_Nt_2 & 0xffff)
      self.leNt_2.setText(str(self.n_Nt_2))  
    except:
      self.leNt_2.setText('?') 
      LL.exception('')

  def on_leNt_3Finished(self):
    try:
      self.n_Nt_3 = eval(self.leNt_3.text(), {}, {})
    except:
      self.leNt_3.setText(str(self.n_Nt_3))
      LL.exception('')
    self.leNt_3.clearFocus() 

  def on_tbNtRd_3_toggle(self):
    try:
      tmpT = svimb.ReadRegs16(self.DirID, self.addrMB, self.BaseCopy + self.offs_Nt_3, 2) 
      self.n_Nt_3 = ToUns16(tmpT[0])
      self.leNt_3.setText(str(self.n_Nt_3))    
    except:
      self.leNt_3.setText('?') 
      LL.exception('')

  def on_tbNtVar_3_toggle(self):
    try:
      tmpT = svimb.ReadRegs16(self.DirID, self.addrMB, self.mba_Nt_3, 2)
      self.n_Nt_3_= ToUns16(tmpT[0]) 
      self.leNt_3.setText(str(self.n_Nt_3_))    
    except:
      self.leNt_3.setText('?') 
      print(sys.exc_info())   # TODO логирование

  def on_tbNtWr_3_toggle(self):
    try:
      self.leNt_3.clearFocus() 
      svimb.WriteReg16(self.DirID, self.addrMB, self.BaseCopy + self.offs_Nt_3, self.n_Nt_3 & 0xffff)
      self.leNt_3.setText(str(self.n_Nt_3))  
    except:
      self.leNt_3.setText('?') 
      LL.exception('')

  def on_leSerNum_SFinished(self):
      a=1

  def on_leAddrMB_SFinished(self):
      a=1

  def on_tbNewAddr_Wr_toggle(self):
      
      self.new_addr=int(self.leAddrMB_S.text())
      self.serial_num=int(self.leSerNum_S.text())
      res=0
      res = ToUns16(svimb.WriteReg16(self.DirID, 0, self.new_addr, self.serial_num))
      q=1

  def on_tbSave_toggle(self):
    try:
      svimb.WriteBit(self.DirID, self.addrMB, self.fUpdConf, 1)
    except:
      LL.exception('')

#---
################################################AMPER
#---
class CfmAmperPar(QtGui.QMainWindow, Ui_fmAmperPar): 
  # addrMB   - адрес милливольтметра в сети MODBUS
  # scanS    - структура для разбора технологического скана
  # ntScan   - namedtuple для упрощения именования полей на выходе scanF
  # scan     - экземпляр ntScan c данными последнего скана 
  # ADCF     - выход фильтра отсчетов АЦП 
  # mVF      - выход милливольтметра на основании отфильтрованных остчетов АЦП
  # fAuto    - True - запущен автоматическое сканирование по таймеру
  # trAutoScan - ID таймера сканирования
  # filtr    - экземпляр filtrP для фильтрации отсчетов АЦП 
  # wSize    - размер окна filtrP (параметр filtrP)
  # min_cntS - минимально приемлимое значение оставшихся в окне сэмплов для формирования результата (параметр filtrP)
  # раскладка карты MODBUS для параметризации милливольтметра:
  #  mba_zcntIgn   -  кол-во игнорируемых отсчетов с АЦП после переключения ключа 
  #  mba_zcntZero  -  кол-во отсчетов АЦП, усредняемых для получения ноля аналогового тракта 
  #  mba_mcntMeas  -  кол-во отсчетов АЦП, снимаемых в режиме штатных измерений до следующей калибровки ноля 
  #  mba_ZeroA32   -  периодически измеряемый ноль аналогового тракта
  #  mba_mK32      -  коэф-т пересчета кодов АЦП в [В]  - на эту величину ДЕЛЯТСЯ коды 
  #  mba_f24b      -  управляющий флаг - 1 - работа с 24х разрядным АЦП
  #  mba_fZeroComp -  управляющий флаг - 1 - режим автоматической компенсации нуля
  #  mba_tsStart   -  стартовый адрес скана в регистровом поле MODBUS
  #  mbq_tsQnt     -  кол-во регистров MODBUS в технологическом скане
  #  DirID    - активное направление обмена (пока извлекается первое из словаря дескрипторов dirD) TODO 
  #  oldTitle - сохраненный заголовок окна

  def __init__(self,vCE, confMB):
    """ confMB - словарь с картой в регистровом\битовом поле MODBUS """
       
    super(CfmAmperPar, self).__init__()
    self.setupUi(self)
    self.vCE=vCE
    self.addrMB = 1
    self.zcntIgn = 0
    self.zcntZero = 1
    self.mcntMeas = 1000
    self.ZeroA = 0
    self.mK = 1
    self.fAuto = False
    self.trAutoScan = None
    self.scan = None
    self.ADCF = 0
    self.mVF = 0
    self.Count_Amper=1
    self.oldTitle = self.windowTitle()
    self.lcdDataConv.setDigitCount(9)
    self.lcdDataConvF.setDigitCount(9)
    self.wSize = 30
    self.min_cntS = 20
    self.filtr = filtrP(self.wSize, self.min_cntS)
    self.filtr1 = filtrP(self.wSize, self.min_cntS)

    self.mba_zcntIgn = int(confMB["zcntIgn"])
    self.mba_zcntZero = int(confMB["zcntZero"])
    self.mba_mcntMeas = int(confMB["mcntMeas"])
    self.mba_ZeroA32 = int(confMB["ZeroA32"])
    self.mba_mK32 = int(confMB["mK32"])
    self.mba_Count_Amper = int(confMB["Count_Amper"])
    self.mba_f24b = int(confMB["f24b"])
    self.mba_fZeroComp = int(confMB["fZeroComp"])
    self.scanS = Struct(confMB["techStr"])
    self.ntScan = namedtuple('ntScan', confMB["techLst"])
    self.mba_tsStart = int(confMB["techStart"])
    self.mbq_tsQnt = int(confMB["techQnt"])

    self.leAddrMB.setText(str(self.addrMB)) 
    self.leIgn.setText(str(self.zcntIgn))
    self.leZero.setText(str(self.zcntZero))
    self.leMeas.setText(str(self.mcntMeas))
    self.leZeroA.setText(str(self.ZeroA))
    self.lemK.setText(str(self.mK))
    self.leCount_Amper.setText(str(self.Count_Amper))
    self.leWSize.setText(str(self.wSize))
    self.leMinCntS.setText(str(self.min_cntS))

    self.actConf.triggered.connect(self.on_muConf_toggle)
    self.menubar.addAction(self.actConf)

    self.leAddrMB.editingFinished.connect(self.on_leAddrMBFinish)

    self.leIgn.editingFinished.connect(self.on_leIgnFinish)
    self.tbIgnRd.clicked.connect(self.on_IgnRd_toggle)
    self.tbIgnWr.clicked.connect(self.on_IgnWr_toggle)
    self.leZero.editingFinished.connect(self.on_leZeroFinish)
    self.tbZeroRd.clicked.connect(self.on_ZeroRd_toggle)
    self.tbZeroWr.clicked.connect(self.on_ZeroWr_toggle)
    self.leMeas.editingFinished.connect(self.on_leMeasFinish)
    self.tbMeasRd.clicked.connect(self.on_MeasRd_toggle)
    self.tbMeasWr.clicked.connect(self.on_MeasWr_toggle)
    self.lemK.editingFinished.connect(self.on_lemKFinish)
    self.tbmKRd.clicked.connect(self.on_mKRd_toggle)
    self.tbmKWr.clicked.connect(self.on_mKWr_toggle)
    self.leCount_Amper.editingFinished.connect(self.on_leCount_AmperFinish)
    self.tbCount_AmperRd.clicked.connect(self.on_Count_AmperRd_toggle)
    self.tbCount_AmperWr.clicked.connect(self.on_Count_AmperWr_toggle) 
    self.leZeroA.editingFinished.connect(self.on_leZeroAFinish)
    self.tbZeroAWr.clicked.connect(self.on_ZeroAWr_toggle)

    self.ch24b.stateChanged.connect(self.on_ch24b_changed)
    self.chZeroComp.stateChanged.connect(self.on_chZeroComp_changed)
    self.tbScan.clicked.connect(self.on_Scan_toggle)
    self.tbAutoScan.clicked.connect(self.on_AutoScan_toggle)

    self.leWSize.editingFinished.connect(self.on_leWSizeFinish)
    self.leMinCntS.editingFinished.connect(self.on_leMinCntSFinish)


  def showEvent(self, e):
    global dirD 

    tmpL = [k for k in dirD.keys()]
    try:
      self.DirID = tmpL[0]  # пока за активное направление принимается первое TODO
      self.setWindowTitle("{} [{}]".format(self.oldTitle, dirD[self.DirID]["cmnt"]))
    except:
      self.DirID = 0
      print(sys.exc_info())   # TODO логирование
    super().showEvent(e)

  
  def timerEvent(self, e):
    # print("timerEvent ID = {}".format(e.timerId())) # ВРЕМЕННО !!!
    self.tbScan.click()    
    self.llData.update()
    self.leZeroA.update()
    if (self.scan):
      self.ADCF = self.filtr.newS(self.scan.ADCcode) 
      self.mVF = (self.ADCF - self.scan.ZeroA) / self.mK  
      self.llDataF.setText(str(self.ADCF))
      self.llCntS.setText(str(self.filtr.cntS))
      self.llNumPass.setText(str(self.filtr.NumPass))
      self.lcdDataConvF.display(self.mVF)

      self.llDataF.update()
      self.llCntS.update()  
      self.llNumPass.update() 
      #print("adc = {} \t mV = {} \t adcF = {} \t mVF = {}".format(self.scan.ADCcode, self.scan.mV, self.ADCF, self.mVF))               
      print("adc = {} \t adcF = {} \t mVF = {}".format(self.scan.ADCcode, self.ADCF, self.mVF))               


  def on_muConf_toggle(self):
    self.vCE.winCAmper.show(self.DirID, self.addrMB)


  def on_leAddrMBFinish(self):
    try:
      self.addrMB = eval(self.leAddrMB.text(), {}, {})
    except:
      print(sys.exc_info())   # TODO логирование
    self.leAddrMB.setText(str(self.addrMB))
    self.leAddrMB.clearFocus()    


  def on_leIgnFinish(self):
    try:
      self.zcntIgn = eval(self.leIgn.text(), {}, {})
    except:
      print(sys.exc_info())   # TODO логирование
    self.leIgn.setText(str(self.zcntIgn))
    self.leIgn.clearFocus()  


  def on_IgnRd_toggle(self):
    try: 
      tmpL = svimb.ReadRegs16(self.DirID , self.addrMB, self.mba_zcntIgn, 1)
       # конвертер в unsigned 
      self.zcntIgn = int.from_bytes(tmpL[0].to_bytes(2, 'little', signed = True), 'little')
      self.leIgn.setText(str(self.zcntIgn))
    except:
      self.leIgn.setText('?')
      print(sys.exc_info())   # TODO логирование 


  def on_IgnWr_toggle(self):
    try:
      self.leIgn.clearFocus()
      svimb.WriteReg16(self.DirID, self.addrMB, self.mba_zcntIgn, self.zcntIgn & 0xffff) 
    except:
      self.leIgn.setText('?')
      print(sys.exc_info())   # TODO логирование 


  def on_leZeroFinish(self):
    try:
      self.zcntZero = eval(self.leZero.text(), {}, {})
    except:
      print(sys.exc_info())   # TODO логирование
    self.leZero.setText(str(self.zcntZero))
    self.leZero.clearFocus()  


  def on_ZeroRd_toggle(self):
    try:
      tmpL = svimb.ReadRegs16(self.DirID, self.addrMB, self.mba_zcntZero, 1)
      # конвертер в unsigned 
      self.zcntZero = int.from_bytes(tmpL[0].to_bytes(2, 'little', signed = True), 'little')
      self.leZero.setText(str(self.zcntZero))
    except:
      self.leZero.setText('?')
      print(sys.exc_info())   # TODO логирование 


  def on_ZeroWr_toggle(self):
    try:
      self.leZero.clearFocus()
      svimb.WriteReg16(self.DirID, self.addrMB, self.mba_zcntZero, self.zcntZero & 0xffff)
    except:
      self.leZero.setText('?')
      print(sys.exc_info())   # TODO логирование 


  def on_leMeasFinish(self):
    try:
      self.mcntMeas = eval(self.leMeas.text(), {}, {})
    except:
      print(sys.exc_info())   # TODO логирование
    self.leMeas.setText(str(self.mcntMeas))
    self.leMeas.clearFocus()


  def on_MeasRd_toggle(self): 
     try:
       tmpL = svimb.ReadRegs16(self.DirID, self.addrMB, self.mba_mcntMeas, 1)
       # конвертер в unsigned 
       self.mcntMeas = int.from_bytes(tmpL[0].to_bytes(2, 'little', signed = True), 'little')
       self.leMeas.setText(str(self.mcntMeas))
     except:
      self.leMeas.setText('?')
      print(sys.exc_info())   # TODO логирование 

    
  def  on_MeasWr_toggle(self):
    try:
      self.leMeas.clearFocus()
      svimb.WriteReg16(self.DirID, self.addrMB, self.mba_mcntMeas, self.mcntMeas & 0xffff)
    except:
      self.leMeas.setText('?')
      print(sys.exc_info())   # TODO логирование 


  def on_lemKFinish(self):
    try:
      self.mK = eval(self.lemK.text(), {}, {})
    except:
      print(sys.exc_info())   # TODO логирование
    self.lemK.setText(str(self.mK))
    self.lemK.clearFocus()


  def on_mKRd_toggle(self):
    try:
      (rlow, rhigh) = svimb.ReadRegs16(self.DirID, self.addrMB, self.mba_mK32, 2)
      self.mK = ToSig32(rlow, rhigh)
      self.lemK.setText(str(self.mK))
    except:
      self.lemK.setText('?')
      print(sys.exc_info())   # TODO логирование 


  def on_mKWr_toggle(self):
    try:
      self.lemK.clearFocus()
      svimb.WriteReg16(self.DirID, self.addrMB, self.mba_mK32, self.mK & 0xffff)
      svimb.WriteReg16(self.DirID, self.addrMB, self.mba_mK32+1, (self.mK & 0xffff0000) >> 16)
    except:
      self.lemK.setText('?')
      print(sys.exc_info())   # TODO логирование 

  def on_leCount_AmperFinish(self):
    try:
      self.Count_Amper = eval(self.leCount_Amper.text(), {}, {})
    except:
      print(sys.exc_info())   # TODO логирование
    self.leCount_Amper.setText(str(self.Count_Amper))
    self.leCount_Amper.clearFocus()


  def on_Count_AmperRd_toggle(self):
    try:
      (rlow, rhigh) = svimb.ReadRegs16(self.DirID, self.addrMB, self.mba_Count_Amper, 2)
      self.Count_Amper = ToSig32(rlow, rhigh)
      self.leCount_Amper.setText(str(self.Count_Amper))
    except:
      self.leCount_Amper.setText('?')
      print(sys.exc_info())   # TODO логирование 


  def on_Count_AmperWr_toggle(self):
    try:
      self.leCount_Amper.clearFocus()
      svimb.WriteReg16(self.DirID, self.addrMB, self.mba_Count_Amper, self.Count_Amper & 0xffff)
      svimb.WriteReg16(self.DirID, self.addrMB, self.mba_Count_Amper+1, (self.Count_Amper & 0xffff0000) >> 16)
    except:
      self.leCount_Amper.setText('?')
      print(sys.exc_info())   # TODO логирование 

 
  def on_leZeroAFinish(self):
    try:
      self.ZeroA = eval(self.leZeroA.text(), {}, {})
    except:
      print(sys.exc_info())   # TODO логирование
    self.leZeroA.setText(str(self.ZeroA))
    self.leZeroA.clearFocus()


  def on_ZeroAWr_toggle(self):
    try:
      self.leZeroA.clearFocus()
      svimb.WriteReg16(self.DirID, self.addrMB, self.mba_ZeroA32, self.ZeroA & 0xffff)
      svimb.WriteReg16(self.DirID, self.addrMB, self.mba_ZeroA32+1, (self.ZeroA & 0xffff0000) >> 16)
    except:
      self.leZeroA.setText('?')
      print(sys.exc_info())   # TODO логирование 
 
  @QtCore.pyqtSlot(int) 
  def on_ch24b_changed(self, ind):
    try:
      svimb.WriteBit(self.DirID, self.addrMB, self.mba_f24b, self.ch24b.isChecked())
    except:
      self.ch24b.setCheckState(QtCore.Qt.PartiallyChecked)
      print(sys.exc_info())   # TODO логирование 


  @QtCore.pyqtSlot(int)
  def on_chZeroComp_changed(self, ind):
    try:
      svimb.WriteBit(self.DirID, self.addrMB, self.mba_fZeroComp, self.chZeroComp.isChecked())
    except:
      self.chZeroComp.setCheckState(QtCore.Qt.PartiallyChecked)
      print(sys.exc_info())   # TODO логирование  


  def on_Scan_toggle(self):
    try:
      tmpL = svimb.ReadRegs16(self.DirID, self.addrMB, self.mba_tsStart, self.mbq_tsQnt)
      #print(tmpL)               
      ba = bytearray()
      for reg in tmpL:
        ba += reg.to_bytes(2, 'little', signed = True)
      #print("ba={}".format(ba)) 
      self.scan = self.ntScan._make(self.scanS.unpack(ba))
      #print(self.scan)               
      self.llData.setText(str(self.scan.ADCcode)) 
      self.leZeroA.setText(str(self.scan.ZeroA))
      self.lcdDataConv.display(self.scan.mV)
    except:
      print(sys.exc_info())   # TODO логирование 


  def on_AutoScan_toggle(self):
    self.fAuto = not self.fAuto
    self.tbAutoScan.setDown(self.fAuto)    
    if (self.fAuto):
      self.trAutoScan = self.startTimer(500)  
      print("trAutoScan = {}".format(self.trAutoScan))      

    else:
      self.killTimer(self.trAutoScan) 

  def on_leWSizeFinish(self):
    try:
      self.wSize = eval(self.leWSize.text(), {}, {})
      self.filtr = filtrP(self.wSize, self.min_cntS) 
    except:
      print(sys.exc_info())   # TODO логирование
    self.leWSize.setText(str(self.wSize))
    self.leWSize.clearFocus()


  def on_leMinCntSFinish(self):
    try:
      self.min_cntS = eval(self.leMinCntS.text(), {}, {})
      self.filtr = filtrP(self.wSize, self.min_cntS) 
    except:
      print(sys.exc_info())   # TODO логирование
    self.leMinCntS.setText(str(self.min_cntS))
    self.leMinCntS.clearFocus()

#---
class CfmAmperConf(QtGui.QMainWindow, Ui_fmAmperConf): 
  # DirID - активное направление MODBUS 
  # addrMB - адрес конфигурируемого милливольтметра на направлении DirID
  # wnCaption - заголовок окна
  
  # новые параметры в редактируемой копии конфигурации милливольтметра
  #  n_addrMB - адрес в сети MODBUS
  #  n_thrAT  - предельно допустимая распределенная пауза в приемном пакете 
  #  n_ZeroA  - cмещение нуля(32р) [unsigned]
  #  n_mK     - коэф-т пересчета кодов АЦП в [В] (32р) [signed]
  #  n_ADC_mode - загружаемое значение в регистр mode AЦП
  #  n_ADC_conf - загружаемое значение в регистр configuration AЦП
  #  n_ADC_IO   - загружаемое значение в регистр IO AЦП (младший байт)
  #  n_SerNum   - серийный номер узла

  # раскладка карты MODBUS для параметризации милливольтметра:
  #  mbv_ZeroA32    - cмещение нуля(32р) в SysVar (параметр используется в рилтайм рассчетах)
  #  mbv_mK32       - коэф-т пересчета кодов АЦП в [В] (32р) в SysVar (параметр используется в рилтайм рассчетах)
  #  fUpdConf       - дискретная команда на запись редактируемой копии в энергонезависимую память
  # следующие поля заданы в виде регистровых смещений относительно Base
  #  BaseMain      - начало активной конфигурации (доступна только для чтения)
  #  BaseCopy      - начало редактируемой копии конфигурации
  #  offs_addr     - адрес данного устройства в сети MODBUS 
  #  offs_thrAT    - предельно допустимая распределенная пауза в приемном пакете 
  #  offs_ZeroA32  - cмещение нуля(32р)
  #  offs_mK32     - коэф-т пересчета кодов АЦП в [В] (32р)
  #  offs_ADC_mode - загружаемое значение в регистр mode AЦП
  #  offs_ADC_conf - загружаемое значение в регистр configuration AЦП
  #  offs_ADC_IO   - загружаемое значение в регистр IO AЦП (младший байт)
  #  offs_SerNum   - серийный номер узла 

  def __init__(self,vCE,confMB, mbv_ZeroA32, mbv_mK32, mbv_Count_Amper):
    """ confMB - словарь с картой в регистровом\битовом поле MODBUS 
        mbv_ZeroA32, mbv_mK32 - адреса в структуре системных переманных SysVar """
       
    super(CfmAmperConf, self).__init__()
    self.setupUi(self)
    self.vCE=vCE

    self.addrMB = 1
    self.wnCaption = self.windowTitle()
       
    self.mbv_ZeroA32 = mbv_ZeroA32
    self.mbv_mK32 = mbv_mK32
    self.mbv_Count_Amper = mbv_Count_Amper

    self.fUpdConf = int(confMB["fUpdConf"])
    self.BaseMain = int(confMB["BaseMain"])
    self.BaseCopy = int(confMB["BaseCopy"])
    self.offs_addr = int(confMB["offs_addr"])
    self.offs_thrAT = int(confMB["offs_thrAT"])
    self.offs_ZeroA32 = int(confMB["offs_ZeroA32"])
    self.offs_mK32 = int(confMB["offs_mK32"])
    self.offs_Count_Amper = int(confMB["offs_Count_Amper"])
    self.offs_ADC_mode = int(confMB["offs_ADC_mode"])
    self.offs_ADC_conf = int(confMB["offs_ADC_conf"])
    self.offs_ADC_IO = int(confMB["offs_ADC_IO"])
    self.offs_SerNum = int(confMB["offs_SerNum"])
    try:
      self.offs_Descr = int(confMB["offs_Descr"])
      self.offs_TypeID = int(confMB["offs_TypeID"])
    except:q=0

    self.leAddrMB.editingFinished.connect(self.on_leAddrMBFinished)
    self.tbAddrMBRd.clicked.connect(self.on_tbAddrMBRd_toggle)
    self.tbAddrMBWr.clicked.connect(self.on_tbAddrMBWr_toggle)
    self.lethrAT.editingFinished.connect(self.on_lethrATFinished)
    self.tbthrATRd.clicked.connect(self.on_tbthrATRd_toggle)
    self.tbthrATWr.clicked.connect(self.on_tbthrATWr_toggle)
    self.leZeroA.editingFinished.connect(self.on_leZeroAFinished)
    self.tbZeroARdVar.clicked.connect(self.on_tbZeroARdVar_toggle)
    self.tbZeroARd.clicked.connect(self.on_tbZeroARd_toggle)
    self.tbZeroAWr.clicked.connect(self.on_tbZeroAWr_toggle)
    self.lemK.editingFinished.connect(self.on_lemKFinished)
    self.tbmKRdVar.clicked.connect(self.on_tbmKRdVar_toggle)
    self.tbmKRd.clicked.connect(self.on_tbmKRd_toggle)
    self.tbmKWr.clicked.connect(self.on_tbmKWr_toggle)    
    self.leCount_Amper.editingFinished.connect(self.on_leCount_AmperFinished)
    self.tbCount_AmpeRdVar.clicked.connect(self.on_Count_AmperRdVar_toggle)
    self.tbCount_AmperRd.clicked.connect(self.on_tbCount_AmperRd_toggle)
    self.tbCount_AmperWr.clicked.connect(self.on_tbCount_AmperWr_toggle)  
    self.leMode.editingFinished.connect(self.on_leModeFinished)
    self.tbModeRd.clicked.connect(self.on_tbModeRd_toggle)
    self.tbModeWr.clicked.connect(self.on_tbModeWr_toggle)
    self.leConf.editingFinished.connect(self.on_leConfFinished)
    self.tbConfRd.clicked.connect(self.on_tbConfRd_toggle)
    self.tbConfWr.clicked.connect(self.on_tbConfWr_toggle)
    self.leIO.editingFinished.connect(self.on_leIOFinished)
    self.tbIORd.clicked.connect(self.on_tbIORd_toggle)
    self.tbIOWr.clicked.connect(self.on_tbIOWr_toggle)
    self.leSerNum.editingFinished.connect(self.on_leSerNumFinished)
    self.tbSerNumRd.clicked.connect(self.on_tbSerNumRd_toggle)
    self.tbSerNumWr.clicked.connect(self.on_tbSerNumWr_toggle)
    self.teDescribe.cursorPositionChanged.connect(self.on_teDescribeFinished)
    self.tbDescribeRd.clicked.connect(self.on_tbDescribeRd_toggle)
    self.tbDescribeWr.clicked.connect(self.on_tbDescribemWr_toggle)
    self.leTypeID.editingFinished.connect(self.on_leTypeIDFinished)
    self.tbTypeIDRd.clicked.connect(self.on_tbTypeIDRd_toggle)
    self.tbTypeIDWr.clicked.connect(self.on_tbTypeIDWr_toggle)
    self.tbSave.clicked.connect(self.on_tbSave_toggle)


  def show(self, DirID, addrMB):
    """ DirID - активное направление MODBUS 
        addrMB - адрес конфигурируемого милливольтметра на направлении DirID """
    self.DirID = DirID
    self.addrMB = addrMB
    self.setWindowTitle(self.wnCaption + " [{:02X}h]".format(self.addrMB))
    super().show()


  def on_leAddrMBFinished(self):
    try:
      self.n_addrMB = eval(self.leAddrMB.text(), {}, {})
    except:
      self.leAddrMB.setText(str(ToUns16(self.n_addrMB)))
      print(sys.exc_info())   # TODO логирование
    self.leAddrMB.clearFocus()    


  def on_tbAddrMBRd_toggle(self):
    try:
      tmpT = svimb.ReadRegs16(self.DirID, self.addrMB, self.BaseCopy + self.offs_addr, 1) 
      self.n_addrMB = tmpT[0]
      self.leAddrMB.setText(str(ToUns16(self.n_addrMB)))    
    except:
      self.leAddrMB.setText('?') 
      print(sys.exc_info())   # TODO логирование


  def on_tbAddrMBWr_toggle(self):
    try:
      self.leAddrMB.clearFocus() 
      self.n_addrMB = svimb.WriteReg16(self.DirID, self.addrMB, self.BaseCopy + self.offs_addr, self.n_addrMB)
      self.leAddrMB.setText(str(ToUns16(self.n_addrMB)))
    except:
      self.leAddrMB.setText('?')
      print(sys.exc_info())   # TODO логирование
    

  def on_lethrATFinished(self):
    try:
      self.n_thrAT = eval(self.lethrAT.text(), {}, {})
    except:
      self.lethrAT.setText(str(ToUns16(self.n_thrAT)))
      print(sys.exc_info())   # TODO логирование
    self.lethrAT.clearFocus() 


  def on_tbthrATRd_toggle(self):
    try:
      tmpT = svimb.ReadRegs16(self.DirID, self.addrMB, self.BaseCopy + self.offs_thrAT, 1) 
      self.n_thrAT = tmpT[0]
      self.lethrAT.setText(str(ToUns16(self.n_thrAT)))    
    except:
      self.lethrAT.setText('?') 
      print(sys.exc_info())   # TODO логирование


  def on_tbthrATWr_toggle(self):
    try:
      self.lethrAT.clearFocus() 
      self.n_thrAT = svimb.WriteReg16(self.DirID, self.addrMB, self.BaseCopy + self.offs_thrAT, self.n_thrAT)
      self.lethrAT.setText(str(ToUns16(self.n_thrAT))) 
    except:
      self.lethrAT.setText('?')
      print(sys.exc_info())   # TODO логирование

 
  def on_leZeroAFinished(self):
    try:
      self.n_ZeroA = eval(self.leZeroA.text(), {}, {})
    except:
      self.leZeroA.setText(str(self.n_ZeroA))
      print(sys.exc_info())   # TODO логирование
    self.leZeroA.clearFocus() 

  
  def on_tbZeroARdVar_toggle(self):
    try:
      (rlow, rhigh) = svimb.ReadRegs16(self.DirID, self.addrMB, self.mbv_ZeroA32, 2)
      self.n_ZeroA = ToUns32(rlow, rhigh)
      self.leZeroA.setText(str(self.n_ZeroA ))    
    except:
      self.leZeroA.setText('?') 
      print(sys.exc_info())   # TODO логирование


  def on_tbZeroARd_toggle(self):
    try:
      (rlow, rhigh) = svimb.ReadRegs16(self.DirID, self.addrMB, self.BaseCopy + self.offs_ZeroA32, 2)
      self.n_ZeroA = ToUns32(rlow, rhigh)
      self.leZeroA.setText(str(self.n_ZeroA ))    
    except:
      self.leZeroA.setText('?') 
      print(sys.exc_info())   # TODO логирование


  def on_tbZeroAWr_toggle(self):
    try:
      self.leZeroA.clearFocus()
      svimb.WriteReg16(self.DirID, self.addrMB, self.BaseCopy + self.offs_ZeroA32, self.n_ZeroA & 0xffff)
      svimb.WriteReg16(self.DirID, self.addrMB, self.BaseCopy + self.offs_ZeroA32 + 1, (self.n_ZeroA & 0xffff0000) >> 16)
    except:
      self.leZeroA.setText('?')
      print(sys.exc_info())   # TODO логирование 


  def on_lemKFinished(self):
    try:
      self.n_mK = eval(self.lemK.text(), {}, {})
    except:
      self.lemK.setText(str(self.n_mK))
      print(sys.exc_info())   # TODO логирование
    self.lemK.clearFocus() 


  def on_tbmKRdVar_toggle(self):
    try:
      (rlow, rhigh) = svimb.ReadRegs16(self.DirID, self.addrMB, self.mbv_mK32, 2)
      self.n_mK = ToSig32(rlow, rhigh)
      self.lemK.setText(str(self.n_mK))    
    except:
      self.lemK.setText('?') 
      print(sys.exc_info())   # TODO логирование


  def on_tbmKRd_toggle(self):
    try:
      (rlow, rhigh) = svimb.ReadRegs16(self.DirID, self.addrMB, self.BaseCopy + self.offs_mK32, 2)
      self.n_mK = ToSig32(rlow, rhigh)
      self.lemK.setText(str(self.n_mK))    
    except:
      self.lemK.setText('?') 
      print(sys.exc_info())   # TODO логирование


  def on_tbmKWr_toggle(self):
    try:
      self.lemK.clearFocus()
      svimb.WriteReg16(self.DirID, self.addrMB, self.BaseCopy + self.offs_mK32, self.n_mK & 0xffff)
      svimb.WriteReg16(self.DirID, self.addrMB, self.BaseCopy + self.offs_mK32 + 1, (self.n_mK & 0xffff0000) >> 16)
    except:
      self.lemK.setText('?')
      print(sys.exc_info())   # TODO логирование

  def on_leCount_AmperFinished(self):
    try:
      self.n_Count_Amper = eval(self.leCount_Amper.text(), {}, {})
    except:
      self.lemK.setText(str(self.n_Count_Amper))
      print(sys.exc_info())   # TODO логирование
    self.leCount_Amper.clearFocus() 


  def on_Count_AmperRdVar_toggle(self):
    try:
      (rlow, rhigh) = svimb.ReadRegs16(self.DirID, self.addrMB, self.mbv_Count_Amper, 2)
      self.n_Count_Amper = ToSig32(rlow, rhigh)
      self.leCount_Amper.setText(str(self.n_Count_Amper))    
    except:
      self.lemK.setText('?') 
      print(sys.exc_info())   # TODO логирование


  def on_tbCount_AmperRd_toggle(self):
    try:
      (rlow, rhigh) = svimb.ReadRegs16(self.DirID, self.addrMB, self.BaseCopy + self.offs_Count_Amper, 2)
      self.n_Count_Amper = ToSig32(rlow, rhigh)
      self.leCount_Amper.setText(str(self.n_Count_Amper))    
    except:
      self.leCount_Amper.setText('?') 
      print(sys.exc_info())   # TODO логирование


  def on_tbCount_AmperWr_toggle(self):
    try:
      self.lemK.clearFocus()
      svimb.WriteReg16(self.DirID, self.addrMB, self.BaseCopy + self.offs_Count_Amper, self.n_Count_Amper & 0xffff)
      svimb.WriteReg16(self.DirID, self.addrMB, self.BaseCopy + self.offs_Count_Amper + 1, (self.n_Count_Amper & 0xffff0000) >> 16)
    except:
      self.lemK.setText('?')
      print(sys.exc_info())   # TODO логирование


  def on_leModeFinished(self):
    try:
      self.n_ADC_mode = int(self.leMode.text(), 16)
    except:
      self.leMode.setText("{:04X}".format(self.n_ADC_mode))
      print(sys.exc_info())   # TODO логирование
    self.leMode.clearFocus()  


  def on_tbModeRd_toggle(self):
    try:
      tmpT = svimb.ReadRegs16(self.DirID, self.addrMB, self.BaseCopy + self.offs_ADC_mode, 1) 
      self.n_ADC_mode = ToUns16(tmpT[0])
      self.leMode.setText("{:04X}".format(self.n_ADC_mode))    
    except:
      self.leMode.setText('?') 
      print(sys.exc_info())   # TODO логирование


  def on_tbModeWr_toggle(self):
    try:
      self.leMode.clearFocus() 
      self.n_ADC_mode = ToUns16(svimb.WriteReg16(self.DirID, self.addrMB, self.BaseCopy + self.offs_ADC_mode, self.n_ADC_mode))
      self.leMode.setText("{:04X}".format(self.n_ADC_mode)) 
    except:
      self.leMode.setText('?')
      print(sys.exc_info())   # TODO логирование
 

  def on_leConfFinished(self):
    try:
      self.n_ADC_conf = int(self.leConf.text(), 16)
    except:
      self.leConf.setText("{:04X}".format(self.n_ADC_conf))
      print(sys.exc_info())   # TODO логирование
    self.leConf.clearFocus() 


  def on_tbConfRd_toggle(self):
    try:
      tmpT = svimb.ReadRegs16(self.DirID, self.addrMB, self.BaseCopy + self.offs_ADC_conf, 1) 
      self.n_ADC_conf = ToUns16(tmpT[0])
      self.leConf.setText("{:04X}".format(self.n_ADC_conf))    
    except:
      self.leConf.setText('?') 
      print(sys.exc_info())   # TODO логирование


  def on_tbConfWr_toggle(self):
    try:
      self.leConf.clearFocus() 
      self.n_ADC_conf = ToUns16(svimb.WriteReg16(self.DirID, self.addrMB, self.BaseCopy + self.offs_ADC_conf, self.n_ADC_conf))
      self.leConf.setText("{:04X}".format(self.n_ADC_conf)) 
    except:
      self.leConf.setText('?')
      print(sys.exc_info())   # TODO логирование


  def on_leIOFinished(self):
    try:
      self.n_ADC_IO = int(self.leIO.text(), 16) & 0xff
    except:
      self.leIO.setText("{:02X}".format(self.n_ADC_IO))
      print(sys.exc_info())   # TODO логирование
    self.leIO.clearFocus() 


  def on_tbIORd_toggle(self):
    try:
      tmpT = svimb.ReadRegs16(self.DirID, self.addrMB, self.BaseCopy + self.offs_ADC_IO, 1) 
      self.n_ADC_IO = (ToUns16(tmpT[0])) & 0xff
      self.leIO.setText("{:02X}".format(self.n_ADC_IO))    
    except:
      self.leIO.setText('?') 
      print(sys.exc_info())   # TODO логирование


  def on_tbIOWr_toggle(self):
    try:
      self.leIO.clearFocus() 
      self.n_ADC_IO = (ToUns16(svimb.WriteReg16(self.DirID, self.addrMB, self.BaseCopy + self.offs_ADC_IO, self.n_ADC_IO))) & 0xff
      self.leIO.setText("{:02X}".format(self.n_ADC_IO))   
    except:
      self.leIO.setText('?')
      print(sys.exc_info())   # TODO логирование


  def on_leSerNumFinished(self):
    try:
      self.n_SerNum = eval(self.leSerNum.text(), {}, {})
    except:
      self.leSerNum.setText(str(self.n_SerNum))
      LL.exception('')
    self.leSerNum.clearFocus() 


  def on_tbSerNumRd_toggle(self):
    try:
      tmpT = svimb.ReadRegs16(self.DirID, self.addrMB, self.BaseCopy + self.offs_SerNum, 1) 
      self.n_SerNum = ToUns16(tmpT[0])
      self.leSerNum.setText(str(self.n_SerNum))    
    except:
      self.leSerNum.setText('?') 
      LL.exception('')


  def on_tbSerNumWr_toggle(self):
    try:
      self.leSerNum.clearFocus() 
      self.n_SerNum = ToUns16(svimb.WriteReg16(self.DirID, self.addrMB, self.BaseCopy + self.offs_SerNum, self.n_SerNum))
      self.leSerNum.setText(str(self.n_SerNum))  
    except:
      self.leSerNum.setText('?') 
      LL.exception('')

  def on_teDescribeFinished(self):
    a=1

  def on_tbDescribeRd_toggle(self):
    try:
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
      except: a=0
      self.n_Describe=tmptxt

      self.teDescribe.setText(str(self.n_Describe))    
    except:
      self.teDescribe.setText('?') 
      LL.exception('')


  def on_tbDescribemWr_toggle(self):
    try:
      self.n_Describe = self.teDescribe.toPlainText()
      Tmpt=[ord(c) for c in self.n_Describe]
      ltxt=len(self.n_Describe)


      self.teDescribe.clearFocus() 
      i=0
      while(i<ltxt):
       svimb.WriteReg16(self.DirID, self.addrMB, self.BaseCopy + self.offs_Descr+i, Tmpt[i])
       i=i+1
      self.teDescribe.setText(str(self.n_Describe))  
    except:
      self.teDescribe.setText('?') 
      LL.exception('')


  def on_leTypeIDFinished(self):
    try:
      self.n_TypeID = eval(self.leTypeID.text(), {}, {})
    except:
      self.leTypeID.setText(str(self.n_TypeID))
      LL.exception('')
    self.leSerNum.clearFocus() 


  def on_tbTypeIDRd_toggle(self):
    try:
      tmpT = svimb.ReadRegs16(self.DirID, self.addrMB, self.BaseCopy + self.offs_TypeID, 1) 
      self.n_TypeID = ToUns16(tmpT[0])
      self.leTypeID.setText(str(self.n_TypeID))    
    except:
      self.leTypeID.setText('?') 
      LL.exception('')


  def on_tbTypeIDWr_toggle(self):
    try:
      self.leTypeID.clearFocus() 
      self.n_TypeID = ToUns16(svimb.WriteReg16(self.DirID, self.addrMB, self.BaseCopy + self.offs_TypeID, self.n_TypeID))
      self.leTypeID.setText(str(self.n_TypeID))  
    except:
      self.leTypeID.setText('?') 
      LL.exception('')

  def on_tbSave_toggle(self):
    try:
      svimb.WriteBit(self.DirID, self.addrMB, self.fUpdConf, 1)
    except:
      LL.exception('')
############################################AMPER END
#/////////////////////////////////////////////////
class CfmNewConv(QtGui.QWidget, Ui_fmNewConv):
  def __init__(self,vCE):
    super(CfmNewConv, self).__init__() 
    self.setupUi(self)
    self.vCE=vCE
    self.mconv = CMConv() # реально редактируемый экземпляр будет получен в show()    
    self.Cm_K = 1
    self.Aref_K = 1
 
    self.leC0.setText("{}".format(self.mconv.C0))    
    self.leK.setText("{}".format(self.mconv.K))
    self.leCm_K.setText("{}".format(self.Cm_K))
    self.leAref_K.setText("{}".format(self.Aref_K))

    self.leC0.editingFinished.connect(self.on_leC0Finish) 
    self.leK.editingFinished.connect(self.on_leKFinish)
    self.leCm_K.editingFinished.connect(self.on_leCm_K)
    self.leAref_K.editingFinished.connect(self.on_leAref_K)
    self.tbSampleC0.clicked.connect(self.on_SampleC0_toggle)
    self.tbCalcK.clicked.connect(self.on_CalcK_toggle)
    self.tbSampleC_K.clicked.connect(self.on_SampleC_K_toggle)


  def show(self, mconv):
    """  mconv - экземпляр CMConv, который будет редактироваться данной формой """ 
    self.mconv = mconv
    super(CfmNewConv, self).show() 


  def on_leC0Finish(self):
    try:
      self.mconv.C0 = eval(self.leC0.text(), {}, {})
    except:
      print(sys.exc_info())   # TODO логирование
    self.leC0.setText("{}".format(self.mconv.C0))
    self.leC0.clearFocus()

 
  def on_leKFinish(self):
    try:
      self.mconv.K = eval(self.leK.text(), {}, {})
    except:
      print(sys.exc_info())   # TODO логирование
    self.leK.setText("{}".format(self.mconv.K))
    self.leK.clearFocus()


  def on_leCm_K(self):
    try:
      self.Cm_K = eval(self.leCm_K.text(), {}, {})
    except:
      print(sys.exc_info())   # TODO логирование
    self.leCm_K.setText("{}".format(self.Cm_K))
    self.leCm_K.clearFocus() 


  def on_leAref_K(self):
    try:
      self.Aref_K = eval(self.leAref_K.text(), {}, {})
    except:
      print(sys.exc_info())   # TODO логирование
    self.leAref_K.setText("{}".format(self.Aref_K))
    self.leAref_K.clearFocus()


  def on_SampleC0_toggle(self):
    self.mconv.C0 = winADC.aData  
    self.leC0.setText("{}".format(self.mconv.C0))   


  def on_CalcK_toggle(self):
    self.leAref_K.clearFocus()
    self.leCm_K.clearFocus() 
    try:
      self.mconv.K = self.Aref_K / self.Cm_K
    except:
      print(sys.exc_info())   # TODO логирование
    self.leK.setText("{}".format(self.mconv.K))


  def on_SampleC_K_toggle(self):
    self.Cm_K = winADC.aData 
    self.leCm_K.setText("{}".format(self.Cm_K))

#---
class CfmTPar(QtGui.QMainWindow, Ui_fmTPar): 
  # addrMB   - адрес термометра в сети MODBUS
  # scanS    - структура для разбора технологического скана
  # ntScan   - namedtuple для упрощения именования полей на выходе scanF
  # scan     - экземпляр ntScan c данными последнего скана 

  # fAuto    - True - запущен автоматическое сканирование по таймеру
  # trAutoScan - ID таймера сканирования
  # filtr    - экземпляр filtrP для фильтрации отсчетов АЦП 
  # wSize    - размер окна filtrP (параметр filtrP)
  # min_cntS - минимально приемлимое значение оставшихся в окне сэмплов для формирования результата (параметр filtrP)

  # раскладка карты MODBUS для параметризации термометра:
  #  mba_tsStart   -  стартовый адрес скана в регистровом поле MODBUS
  #  mbq_tsQnt     -  кол-во регистров MODBUS в технологическом скане
  #  mba_CR0       -  код АЦП при температуре 0 С  
  #  DirID    - активное направление обмена (пока извлекается первое из словаря дескрипторов dirD) TODO 
  #  oldTitle - сохраненный заголовок окна

  def __init__(self,vCE, confMB):
    """ confMB - словарь с картой в регистровом\битовом поле MODBUS """
       
    super().__init__()
    self.setupUi(self)
    self.vCE=vCE
    self.addrMB = 1
    self.scan = None
    self.fAuto = False

    self.oldTitle = self.windowTitle()
    self.lcdDataConv.setDigitCount(9)
    self.lcdDataConvF.setDigitCount(9)
    self.wSize = 30
    self.min_cntS = 20
    self.filtr = filtrP(self.wSize, self.min_cntS)

    self.mba_CR0 = int(confMB["CR0"])
    self.scanS = Struct(confMB["techStr"])
    self.ntScan = namedtuple('ntScan', confMB["techLst"])
    self.mba_tsStart = int(confMB["techStart"])
    self.mbq_tsQnt = int(confMB["techQnt"])

    self.leAddrMB.setText(str(self.addrMB))
    self.leWSize.setText(str(self.wSize))
    self.leMinCntS.setText(str(self.min_cntS))

    self.actConf.triggered.connect(self.on_muConf_toggle)
    self.menubar.addAction(self.actConf)

    self.leAddrMB.editingFinished.connect(self.on_leAddrMBFinish)
    self.leCR0.editingFinished.connect(self.on_leCR0Finish)
    self.tbCR0Rd.clicked.connect(self.on_CR0Rd_toggle)
    self.tbCR0Wr.clicked.connect(self.on_CR0Wr_toggle)

    self.leWSize.editingFinished.connect(self.on_leWSizeFinish)
    self.leMinCntS.editingFinished.connect(self.on_leMinCntSFinish)

    self.tbScan.clicked.connect(self.on_Scan_toggle)
    self.tbAutoScan.clicked.connect(self.on_AutoScan_toggle) 


  def showEvent(self, e):
    global dirD 

    tmpL = [k for k in dirD.keys()]
    try:
      self.DirID = tmpL[0]  # пока за активное направление принимается первое TODO
      self.setWindowTitle("{} [{}]".format(self.oldTitle, dirD[self.DirID]["cmnt"]))
    except:
      self.DirID = 0
      LL.exception('') 
    super().showEvent(e)


  def timerEvent(self, e):
    # print("timerEvent ID = {}".format(e.timerId())) 
    self.tbScan.click()    

    self.llData.update()
    if (self.scan):
      self.ADCF = self.filtr.newS(self.scan.ADCcode) 
      #self.mVF = (self.ADCF - self.scan.ZeroA) / self.mK  
      self.llDataF.setText(str(self.ADCF))
      self.llCntS.setText(str(self.filtr.cntS))
      self.llNumPass.setText(str(self.filtr.NumPass))
      #self.lcdDataConvF.display(self.mVF)

      self.llDataF.update()
      self.llCntS.update()  
      self.llNumPass.update() 
      #print("adc = {} \t mV = {} \t adcF = {} \t mVF = {}".format(self.scan.ADCcode, self.scan.mV, self.ADCF, self.mVF))               
      #print("adc = {} \t adcF = {} \t mVF = {}".format(self.scan.ADCcode, self.ADCF, self.mVF))
      print("adc = {} \t T = {} \t adcF = {}".format(self.scan.ADCcode, self.scan.T, self.ADCF))


  def on_muConf_toggle(self):
    self.vCE.winCT.show(self.DirID, self.addrMB)


  def on_leAddrMBFinish(self):
    try:
      self.addrMB = eval(self.leAddrMB.text(), {}, {})
    except:
      LL.exception('') 
    self.leAddrMB.setText(str(self.addrMB))
    self.leAddrMB.clearFocus() 


  def on_leCR0Finish(self):
    try:
      self.CR0 = eval(self.leCR0.text(), {}, {})
    except:
      LL.exception('') 
    self.leCR0.setText(str(self.CR0))
    self.leCR0.clearFocus()


  def on_CR0Rd_toggle(self):
    try:
      (rlow, rhigh) = svimb.ReadRegs16(self.DirID, self.addrMB, self.mba_CR0, 2)
      self.CR0 = ToUns32(rlow, rhigh)
      self.leCR0.setText(str(self.CR0))
    except:
      self.leCR0.setText('?')
      LL.exception('') 


  def on_CR0Wr_toggle(self):
    try:
      self.leCR0.clearFocus()
      svimb.WriteReg16(self.DirID, self.addrMB, self.mba_CR0, self.CR0 & 0xffff)
      svimb.WriteReg16(self.DirID, self.addrMB, self.mba_CR0+1, (self.CR0 & 0xffff0000) >> 16)
    except:
      self.leCR0.setText('?')
      LL.exception('')  


  def on_Scan_toggle(self):
    try:
      tmpL = svimb.ReadRegs16(self.DirID, self.addrMB, self.mba_tsStart, self.mbq_tsQnt)
      #print(tmpL)               
      ba = bytearray()
      for reg in tmpL:
        ba += reg.to_bytes(2, 'little', signed = True)
      #print("ba={}".format(ba)) 
      self.scan = self.ntScan._make(self.scanS.unpack(ba))
      #print(self.scan)               
      self.llData.setText(str(self.scan.ADCcode)) 
      self.lcdDataConv.display(self.scan.T)
    except:
      LL.exception('') 


  def on_AutoScan_toggle(self):
    self.fAuto = not self.fAuto
    self.tbAutoScan.setDown(self.fAuto)    
    if (self.fAuto):
      self.trAutoScan = self.startTimer(1000)  
      print("trAutoScan = {}".format(self.trAutoScan))      

    else:
      self.killTimer(self.trAutoScan) 


  def on_leWSizeFinish(self):
    try:
      self.wSize = eval(self.leWSize.text(), {}, {})
      self.filtr = filtrP(self.wSize, self.min_cntS) 
    except:
      LL.exception('') 
    self.leWSize.setText(str(self.wSize))
    self.leWSize.clearFocus()


  def on_leMinCntSFinish(self):
    try:
      self.min_cntS = eval(self.leMinCntS.text(), {}, {})
      self.filtr = filtrP(self.wSize, self.min_cntS) 
    except:
      LL.exception('') 
    self.leMinCntS.setText(str(self.min_cntS))
    self.leMinCntS.clearFocus()

#---
class CfmTConf(QtGui.QMainWindow, Ui_fmTConf): 
  # DirID - активное направление MODBUS 
  # addrMB - адрес конфигурируемого милливольтметра на направлении DirID
  # wnCaption - заголовок окна

  # новые параметры в редактируемой копии конфигурации милливольтметра
  #  n_addrMB - адрес в сети MODBUS
  #  n_thrAT  - предельно допустимая распределенная пауза в приемном пакете 
  #  n_CR0      - код АЦП при температуре 0 С (32р) [unsigned]
  #  n_Ka       - коэффициент типа термометра-сопротивления (1024/a) (32р) [unsigned]
  #  n_ADC_mode - загружаемое значение в регистр mode AЦП
  #  n_ADC_conf - загружаемое значение в регистр configuration AЦП
  #  n_ADC_IO   - загружаемое значение в регистр IO AЦП (младший байт)
  #  n_SerNum   - серийный номер узла

  # раскладка карты MODBUS для параметризации термометра:
  # mbv_CR0        - код АЦП при температуре 0 С в SysVar (32р) [unsigned]
  # fUpdConf       - дискретная команда на запись редактируемой копии в энергонезависимую память
  # следующие поля заданы в виде регистровых смещений относительно Base
  #  BaseMain      - начало активной конфигурации (доступна только для чтения)
  #  BaseCopy      - начало редактируемой копии конфигурации
  #  offs_addr     - адрес данного устройства в сети MODBUS 
  #  offs_thrAT    - предельно допустимая распределенная пауза в приемном пакете 
  #  offs_CR0      - код АЦП при температуре 0 С (32р) [unsigned]
  #  offs_Ka       - коэффициент типа термометра-сопротивления (1024/a) (32р) [unsigned]
  #  offs_ADC_mode - загружаемое значение в регистр mode AЦП
  #  offs_ADC_conf - загружаемое значение в регистр configuration AЦП
  #  offs_ADC_IO   - загружаемое значение в регистр IO AЦП (младший байт)
  #  offs_SerNum   - серийный номер узла 

  def __init__(self,vCE, confMB, mbv_CR0):
    """ confMB - словарь с картой в регистровом\битовом поле MODBUS 
        mbv_CR0 - адрес в структуре системных переманных SysVar """

    super().__init__()
    self.setupUi(self)
    self.vCE=vCE
    self.addrMB = 1
    self.wnCaption = self.windowTitle()

    self.mbv_CR0 = mbv_CR0
    self.fUpdConf = int(confMB["fUpdConf"])
    self.BaseMain = int(confMB["BaseMain"])
    self.BaseCopy = int(confMB["BaseCopy"])
    self.offs_addr = int(confMB["offs_addr"])
    self.offs_thrAT = int(confMB["offs_thrAT"])
    self.offs_CR0 = int(confMB["offs_CR0"])
    self.offs_Ka = int(confMB["offs_Ka"])
    self.offs_ADC_mode = int(confMB["offs_ADC_mode"])
    self.offs_ADC_conf = int(confMB["offs_ADC_conf"])
    self.offs_ADC_IO = int(confMB["offs_ADC_IO"])
    self.offs_SerNum = int(confMB["offs_SerNum"])

    try:
      self.offs_Descr = int(confMB["offs_Descr"])
      self.offs_TypeID = int(confMB["offs_TypeID"])
    except:q=0
    
    self.leAddrMB.editingFinished.connect(self.on_leAddrMBFinished)
    self.tbAddrMBRd.clicked.connect(self.on_tbAddrMBRd_toggle)
    self.tbAddrMBWr.clicked.connect(self.on_tbAddrMBWr_toggle)
    self.lethrAT.editingFinished.connect(self.on_lethrATFinished)
    self.tbthrATRd.clicked.connect(self.on_tbthrATRd_toggle)
    self.tbthrATWr.clicked.connect(self.on_tbthrATWr_toggle)
    self.leCR0.editingFinished.connect(self.on_leCR0Finished)
    self.tbCR0RdVar.clicked.connect(self.on_tbCR0RdVar_toggle)
    self.tbCR0Rd.clicked.connect(self.on_tbCR0Rd_toggle)
    self.tbCR0Wr.clicked.connect(self.on_tbCR0Wr_toggle)
    self.leKa.editingFinished.connect(self.on_leKaFinished)
    self.tbKaRd.clicked.connect(self.on_tbKaRd_toggle)   
    self.tbKaWr.clicked.connect(self.on_tbKaWr_toggle)
    self.leMode.editingFinished.connect(self.on_leModeFinished)
    self.tbModeRd.clicked.connect(self.on_tbModeRd_toggle)
    self.tbModeWr.clicked.connect(self.on_tbModeWr_toggle)
    self.leConf.editingFinished.connect(self.on_leConfFinished)
    self.tbConfRd.clicked.connect(self.on_tbConfRd_toggle)
    self.tbConfWr.clicked.connect(self.on_tbConfWr_toggle)
    self.leIO.editingFinished.connect(self.on_leIOFinished)
    self.tbIORd.clicked.connect(self.on_tbIORd_toggle)
    self.tbIOWr.clicked.connect(self.on_tbIOWr_toggle)
    self.leSerNum.editingFinished.connect(self.on_leSerNumFinished)
    self.tbSerNumRd.clicked.connect(self.on_tbSerNumRd_toggle)
    self.tbSerNumWr.clicked.connect(self.on_tbSerNumWr_toggle)

    self.teDescribe.cursorPositionChanged.connect(self.on_teDescribeFinished)
    self.tbDescribeRd.clicked.connect(self.on_tbDescribeRd_toggle)
    self.tbDescribeWr.clicked.connect(self.on_tbDescribemWr_toggle)
    self.leTypeID.editingFinished.connect(self.on_leTypeIDFinished)
    self.tbTypeIDRd.clicked.connect(self.on_tbTypeIDRd_toggle)
    self.tbTypeIDWr.clicked.connect(self.on_tbTypeIDWr_toggle)

    self.tbSave.clicked.connect(self.on_tbSave_toggle) 


  def show(self, DirID, addrMB):
    """ DirID - активное направление MODBUS 
        addrMB - адрес конфигурируемого термометра на направлении DirID """
    self.DirID = DirID
    self.addrMB = addrMB  # TODO обновить значение в поле ввода
    self.setWindowTitle(self.wnCaption + " [{:02X}h]".format(self.addrMB))
    super().show()


  def on_leAddrMBFinished(self):
    try:
      self.n_addrMB = eval(self.leAddrMB.text(), {}, {})
    except:
      self.leAddrMB.setText(str(ToUns16(self.n_addrMB)))
      LL.exception('') 
    self.leAddrMB.clearFocus()    


  def on_tbAddrMBRd_toggle(self):
    try:
      tmpT = svimb.ReadRegs16(self.DirID, self.addrMB, self.BaseCopy + self.offs_addr, 1) 
      self.n_addrMB = tmpT[0]
      self.leAddrMB.setText(str(ToUns16(self.n_addrMB)))    
    except:
      self.leAddrMB.setText('?') 
      LL.exception('') 


  def on_tbAddrMBWr_toggle(self):
    try:
      self.leAddrMB.clearFocus() 
      self.n_addrMB = svimb.WriteReg16(self.DirID, self.addrMB, self.BaseCopy + self.offs_addr, self.n_addrMB)
      self.leAddrMB.setText(str(ToUns16(self.n_addrMB)))
    except:
      self.leAddrMB.setText('?')
      LL.exception('') 


  def on_lethrATFinished(self):
    try:
      self.n_thrAT = eval(self.lethrAT.text(), {}, {})
    except:
      self.lethrAT.setText(str(ToUns16(self.n_thrAT)))
      LL.exception('')
    self.lethrAT.clearFocus() 


  def on_tbthrATRd_toggle(self):
    try:
      tmpT = svimb.ReadRegs16(self.DirID, self.addrMB, self.BaseCopy + self.offs_thrAT, 1) 
      self.n_thrAT = tmpT[0]
      self.lethrAT.setText(str(ToUns16(self.n_thrAT)))    
    except:
      self.lethrAT.setText('?') 
      LL.exception('')


  def on_tbthrATWr_toggle(self):
    try:
      self.lethrAT.clearFocus() 
      self.n_thrAT = svimb.WriteReg16(self.DirID, self.addrMB, self.BaseCopy + self.offs_thrAT, self.n_thrAT)
      self.lethrAT.setText(str(ToUns16(self.n_thrAT))) 
    except:
      self.lethrAT.setText('?')
      LL.exception('')


  def on_leCR0Finished(self):
    try: 
      self.n_CR0 = eval(self.leCR0.text(), {}, {})
    except:
      self.leCR0.setText(str(self.n_CR0))
      LL.exception('')
    self.leCR0.clearFocus() 


  def on_tbCR0RdVar_toggle(self):
    try:
      (rlow, rhigh) = svimb.ReadRegs16(self.DirID, self.addrMB, self.mbv_CR0, 2)
      self.n_CR0 = ToUns32(rlow, rhigh)
      self.leCR0.setText(str(self.n_CR0))    
    except:
      self.leCR0.setText('?') 
      LL.exception('')


  def on_tbCR0Rd_toggle(self):
    try:
      (rlow, rhigh) = svimb.ReadRegs16(self.DirID, self.addrMB, self.BaseCopy + self.offs_CR0, 2)
      self.n_CR0 = ToUns32(rlow, rhigh)
      self.leCR0.setText(str(self.n_CR0))    
    except:
      self.leCR0.setText('?') 
      LL.exception('')


  def on_tbCR0Wr_toggle(self):
    try: 
      self.leCR0.clearFocus() 
      svimb.WriteReg16(self.DirID, self.addrMB, self.BaseCopy + self.offs_CR0, self.n_CR0 & 0xffff)
      svimb.WriteReg16(self.DirID, self.addrMB, self.BaseCopy + self.offs_CR0 + 1, (self.n_CR0 & 0xffff0000) >> 16)
    except:
      self.leCR0.setText('?') 
      LL.exception('')  


  def on_leKaFinished(self):
    try: 
      self.n_Ka = eval(self.leKa.text(), {}, {})
    except:
      self.leKa.setText(str(self.n_Ka))
      LL.exception('')
    self.leKa.clearFocus() 


  def on_tbKaRd_toggle(self):
    try:
      (rlow, rhigh) = svimb.ReadRegs16(self.DirID, self.addrMB, self.BaseCopy + self.offs_Ka, 2)
      self.n_Ka = ToUns32(rlow, rhigh)
      self.leKa.setText(str(self.n_Ka))    
    except:
      self.leKa.setText('?') 
      LL.exception('')


  def on_tbKaWr_toggle(self):
    try: 
      self.leKa.clearFocus() 
      svimb.WriteReg16(self.DirID, self.addrMB, self.BaseCopy + self.offs_Ka, self.n_Ka & 0xffff)
      svimb.WriteReg16(self.DirID, self.addrMB, self.BaseCopy + self.offs_Ka + 1, (self.n_Ka & 0xffff0000) >> 16)
    except:
      self.leKa.setText('?') 
      LL.exception('')


  def on_leModeFinished(self):
    try:
      self.n_ADC_mode = int(self.leMode.text(), 16)
    except:
      self.leMode.setText("{:04X}".format(self.n_ADC_mode))
      LL.exception('')
    self.leMode.clearFocus()  


  def on_tbModeRd_toggle(self):
    try:
      tmpT = svimb.ReadRegs16(self.DirID, self.addrMB, self.BaseCopy + self.offs_ADC_mode, 1) 
      self.n_ADC_mode = ToUns16(tmpT[0])
      self.leMode.setText("{:04X}".format(self.n_ADC_mode))    
    except:
      self.leMode.setText('?') 
      LL.exception('')


  def on_tbModeWr_toggle(self):
    try:
      self.leMode.clearFocus() 
      self.n_ADC_mode = ToUns16(svimb.WriteReg16(self.DirID, self.addrMB, self.BaseCopy + self.offs_ADC_mode, self.n_ADC_mode))
      self.leMode.setText("{:04X}".format(self.n_ADC_mode)) 
    except:
      self.leMode.setText('?')
      LL.exception('')
 

  def on_leConfFinished(self):
    try:
      self.n_ADC_conf = int(self.leConf.text(), 16)
    except:
      self.leConf.setText("{:04X}".format(self.n_ADC_conf))
      LL.exception('')
    self.leConf.clearFocus() 


  def on_tbConfRd_toggle(self):
    try:
      tmpT = svimb.ReadRegs16(self.DirID, self.addrMB, self.BaseCopy + self.offs_ADC_conf, 1) 
      self.n_ADC_conf = ToUns16(tmpT[0])
      self.leConf.setText("{:04X}".format(self.n_ADC_conf))    
    except:
      self.leConf.setText('?') 
      LL.exception('')


  def on_tbConfWr_toggle(self):
    try:
      self.leConf.clearFocus() 
      self.n_ADC_conf = ToUns16(svimb.WriteReg16(self.DirID, self.addrMB, self.BaseCopy + self.offs_ADC_conf, self.n_ADC_conf))
      self.leConf.setText("{:04X}".format(self.n_ADC_conf)) 
    except:
      self.leConf.setText('?')
      LL.exception('')


  def on_leIOFinished(self):
    try:
      self.n_ADC_IO = int(self.leIO.text(), 16) & 0xff
    except:
      self.leIO.setText("{:02X}".format(self.n_ADC_IO))
      LL.exception('')
    self.leIO.clearFocus() 


  def on_tbIORd_toggle(self):
    try:
      tmpT = svimb.ReadRegs16(self.DirID, self.addrMB, self.BaseCopy + self.offs_ADC_IO, 1) 
      self.n_ADC_IO = (ToUns16(tmpT[0])) & 0xff
      self.leIO.setText("{:02X}".format(self.n_ADC_IO))    
    except:
      self.leIO.setText('?') 
      LL.exception('')


  def on_tbIOWr_toggle(self):
    try:
      self.leIO.clearFocus() 
      self.n_ADC_IO = (ToUns16(svimb.WriteReg16(self.DirID, self.addrMB, self.BaseCopy + self.offs_ADC_IO, self.n_ADC_IO))) & 0xff
      self.leIO.setText("{:02X}".format(self.n_ADC_IO))   
    except:
      self.leIO.setText('?')
      LL.exception('')


  def on_leSerNumFinished(self):
    try:
      self.n_SerNum = eval(self.leSerNum.text(), {}, {})
    except:
      self.leSerNum.setText(str(self.n_SerNum))
      LL.exception('')
    self.leSerNum.clearFocus() 


  def on_tbSerNumRd_toggle(self):
    try:
      tmpT = svimb.ReadRegs16(self.DirID, self.addrMB, self.BaseCopy + self.offs_SerNum, 1) 
      self.n_SerNum = ToUns16(tmpT[0])
      self.leSerNum.setText(str(self.n_SerNum))    
    except:
      self.leSerNum.setText('?') 
      LL.exception('')


  def on_tbSerNumWr_toggle(self):
    try:
      self.leSerNum.clearFocus() 
      self.n_SerNum = ToUns16(svimb.WriteReg16(self.DirID, self.addrMB, self.BaseCopy + self.offs_SerNum, self.n_SerNum))
      self.leSerNum.setText(str(self.n_SerNum))  
    except:
      self.leSerNum.setText('?') 
      LL.exception('')

################################################


  def on_teDescribeFinished(self):
    a=1

  def on_tbDescribeRd_toggle(self):
    try:
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
      except: a=0
      self.n_Describe=tmptxt

      self.teDescribe.setText(str(self.n_Describe))    
    except:
      self.teDescribe.setText('?') 
      LL.exception('')


  def on_tbDescribemWr_toggle(self):
    try:
      self.n_Describe = self.teDescribe.toPlainText()
      Tmpt=[ord(c) for c in self.n_Describe]

      ltxt=len(self.n_Describe)
      self.teDescribe.clearFocus() 
      i=0
      while(i<ltxt):
       svimb.WriteReg16(self.DirID, self.addrMB, self.BaseCopy + self.offs_Descr+i, Tmpt[i])
       i=i+1
      self.teDescribe.setText(str(self.n_Describe))  
    except:
      self.teDescribe.setText('?') 
      LL.exception('')


  def on_leTypeIDFinished(self):
    try:
      self.n_TypeID = eval(self.leTypeID.text(), {}, {})
    except:
      self.leTypeID.setText(str(self.n_TypeID))
      LL.exception('')
    self.leSerNum.clearFocus() 


  def on_tbTypeIDRd_toggle(self):
    try:
      tmpT = svimb.ReadRegs16(self.DirID, self.addrMB, self.BaseCopy + self.offs_TypeID, 1) 
      self.n_TypeID = ToUns16(tmpT[0])
      self.leTypeID.setText(str(self.n_TypeID))    
    except:
      self.leTypeID.setText('?') 
      LL.exception('')


  def on_tbTypeIDWr_toggle(self):
    try:
      self.leTypeID.clearFocus() 
      self.n_TypeID = ToUns16(svimb.WriteReg16(self.DirID, self.addrMB, self.BaseCopy + self.offs_TypeID, self.n_TypeID))
      self.leTypeID.setText(str(self.n_TypeID))  
    except:
      self.leTypeID.setText('?') 
      LL.exception('')

  def on_tbSave_toggle(self):
    try:
      svimb.WriteBit(self.DirID, self.addrMB, self.fUpdConf, 1)
    except:
      LL.exception('')
#---
class CfmTPPar(QtGui.QMainWindow, Ui_fmTPPar): 
  # addrMB   - адрес термометра в сети MODBUS
  # scanS    - структура для разбора технологического скана
  # ntScan   - namedtuple для упрощения именования полей на выходе scanF
  # scan     - экземпляр ntScan c данными последнего скана 

  # fAuto    - True - запущен автоматическое сканирование по таймеру
  # trAutoScan - ID таймера сканирования
  # filtr    - экземпляр filtrP для фильтрации отсчетов АЦП 
  # wSize    - размер окна filtrP (параметр filtrP)
  # min_cntS - минимально приемлимое значение оставшихся в окне сэмплов для формирования результата (параметр filtrP)

  # раскладка карты MODBUS для параметризации термометра:
  #  mba_tsStart   -  стартовый адрес скана в регистровом поле MODBUS
  #  mbq_tsQnt     -  кол-во регистров MODBUS в технологическом скане
  #  mba_CR0       -  код АЦП при температуре 0 С  
  #  DirID    - активное направление обмена (пока извлекается первое из словаря дескрипторов dirD) TODO 
  #  oldTitle - сохраненный заголовок окна

  def __init__(self,vCE,confMB):
    """ confMB - словарь с картой в регистровом\битовом поле MODBUS """
       
    super().__init__()
    self.setupUi(self)
    self.vCE=vCE
    self.addrMB = 1
    self.scan = None
    self.fAuto = False

    self.oldTitle = self.windowTitle()
    self.lcdDataConv.setDigitCount(9)
    self.lcdDataConvF.setDigitCount(9)
    self.wSize = 30
    self.min_cntS = 20
    self.wSizeP = 30
    self.min_cntSP = 20
    self.filtr = filtrP(self.wSize, self.min_cntS)
    self.filtr_T = filtrP(self.wSize, self.min_cntS)
    self.filtr_P = filtrP(self.wSizeP, self.min_cntSP)
    self.filtr_P1 = filtrP(self.wSizeP, self.min_cntSP)

    self.mba_CR0 = int(confMB["CR0"])
    self.mba_P0 = int(confMB["P0"])
    self.mba_Ap = int(confMB["Ap"])
    self.scanS = Struct(confMB["techStr"])
    self.ntScan = namedtuple('ntScan', confMB["techLst"])
    self.mba_tsStart = int(confMB["techStart"])
    self.mbq_tsQnt = int(confMB["techQnt"])

    self.leAddrMB.setText(str(self.addrMB))
    self.leWSize.setText(str(self.wSize))
    self.leMinCntS.setText(str(self.min_cntS))

    self.leWSizeP.setText(str(self.wSizeP))
    self.leMinCntSP.setText(str(self.min_cntSP))

    self.actConf.triggered.connect(self.on_muConf_toggle)
    self.menubar.addAction(self.actConf)

    self.leAddrMB.editingFinished.connect(self.on_leAddrMBFinish)
    self.leCR0.editingFinished.connect(self.on_leCR0Finish)
    self.tbCR0Rd.clicked.connect(self.on_CR0Rd_toggle)
    self.tbCR0Wr.clicked.connect(self.on_CR0Wr_toggle)

    self.leP0.editingFinished.connect(self.on_leP0Finish)
    self.tbP0Rd.clicked.connect(self.on_tbP0Rd_toggle)
    self.tbP0Wr.clicked.connect(self.on_tbP0Wr_toggle)

    self.leAp.editingFinished.connect(self.on_leApFinish)
    self.tbApRd.clicked.connect(self.on_tbApRd_toggle)
    self.tbApWr.clicked.connect(self.on_tbApWr_toggle)

    self.leWSize.editingFinished.connect(self.on_leWSizeFinish)
    self.leMinCntS.editingFinished.connect(self.on_leMinCntSFinish)

    self.tbScan.clicked.connect(self.on_Scan_toggle)
    self.tbAutoScan.clicked.connect(self.on_AutoScan_toggle) 


  def showEvent(self, e):
    global dirD 

    tmpL = [k for k in dirD.keys()]
    try:
      self.DirID = tmpL[0]  # пока за активное направление принимается первое TODO
      self.setWindowTitle("{} [{}]".format(self.oldTitle, dirD[self.DirID]["cmnt"]))
    except:
      self.DirID = 0
      LL.exception('') 
    super().showEvent(e)


  def timerEvent(self, e):
    # print("timerEvent ID = {}".format(e.timerId())) 
    self.tbScan.click()    

    self.llData.update()
    if (self.scan):
      self.ADCF = self.filtr.newS(self.scan.ADCcode) 
      self.TF = self.filtr_T.newS(self.scan.T)  
      self.llDataF.setText(str(self.ADCF))
      self.llCntS.setText(str(self.filtr.cntS))
      self.llNumPass.setText(str(self.filtr.NumPass))
      self.lcdDataConvF.display(self.TF)

      self.llDataF.update()
      self.llCntS.update()  
      self.llNumPass.update() 
      #print("adc = {} \t mV = {} \t adcF = {} \t mVF = {}".format(self.scan.ADCcode, self.scan.mV, self.ADCF, self.mVF))               
      #print("adc = {} \t adcF = {} \t mVF = {}".format(self.scan.ADCcode, self.ADCF, self.mVF))
      #print("adc = {} \t T = {} \t adcF = {}".format(self.scan.ADCcode, self.scan.T, self.ADCF))

    if (self.scan):
      #self.llData_P.setText(str(self.scan.ADCcodeP))
      self.ADCF_P = self.filtr_P.newS(self.scan.ADCcodeP) 
      self._PF = self.filtr_P1.newS(self.scan.P) 
      #self.mVF = (self.ADCF - self.scan.ZeroA) / self.mK  
      self.llDataF_P.setText(str(self.ADCF_P))
      self.llCntS_2.setText(str(self.filtr_P.cntS))
      self.llNumPass_2.setText(str(self.filtr_P.NumPass))
      #self.lcdDataConv_P.display(self.ADCF_P)
      self.lcdDataConvF_P.display(self._PF)
      self.llData_P.update()
      self.llDataF_P.update()
      self.llCntS_2.update()  
      self.llNumPass_2.update()
      print("adc = {} \t T = {} \t adcP = {} \t P = {}".format(self.scan.ADCcode, self.scan.T, self.scan.ADCcodeP, self.scan.P)) 

  def on_muConf_toggle(self):
    self.vCE.winCTP.show(self.DirID, self.addrMB)


  def on_leAddrMBFinish(self):
    try:
      self.addrMB = eval(self.leAddrMB.text(), {}, {})
    except:
      LL.exception('') 
    self.leAddrMB.setText(str(self.addrMB))
    self.leAddrMB.clearFocus() 


  def on_leCR0Finish(self):
    try:
      self.CR0 = eval(self.leCR0.text(), {}, {})
    except:
      LL.exception('') 
    self.leCR0.setText(str(self.CR0))
    self.leCR0.clearFocus()


  def on_CR0Rd_toggle(self):
    try:
      (rlow, rhigh) = svimb.ReadRegs16(self.DirID, self.addrMB, self.mba_CR0, 2)
      self.CR0 = ToUns32(rlow, rhigh)
      self.leCR0.setText(str(self.CR0))
    except:
      self.leCR0.setText('?')
      LL.exception('') 


  def on_CR0Wr_toggle(self):
    try:
      self.leCR0.clearFocus()
      svimb.WriteReg16(self.DirID, self.addrMB, self.mba_CR0, self.CR0 & 0xffff)
      svimb.WriteReg16(self.DirID, self.addrMB, self.mba_CR0+1, (self.CR0 & 0xffff0000) >> 16)
    except:
      self.leCR0.setText('?')
      LL.exception('')  

  def on_leP0Finish(self):
    try:
      self.P0 = eval(self.leP0.text(), {}, {})
    except:
      LL.exception('') 
    self.leP0.setText(str(self.P0))
    self.leP0.clearFocus()

  def on_tbP0Rd_toggle(self):
    try:
      (rlow, rhigh) = svimb.ReadRegs16(self.DirID, self.addrMB, self.mba_P0, 2)
      self.P0 = ToUns32(rlow, rhigh)
      self.leP0.setText(str(self.P0))
    except:
      self.leP0.setText('?')
      LL.exception('') 

  def on_tbP0Wr_toggle(self):
    try:
      self.leP0.clearFocus()
      svimb.WriteReg16(self.DirID, self.addrMB, self.mba_P0, self.P0 & 0xffff)
      svimb.WriteReg16(self.DirID, self.addrMB, self.mba_P0+1, (self.P0 & 0xffff0000) >> 16)
    except:
      self.leP0.setText('?')
      LL.exception('')  


  def on_leApFinish(self):
    try:
      self.Ap = eval(self.leAp.text(), {}, {})
    except:
      LL.exception('') 
    self.leAp.setText(str(self.Ap))
    self.leAp.clearFocus()

  def on_tbApRd_toggle(self):
    try:
      (rlow, rhigh) = svimb.ReadRegs16(self.DirID, self.addrMB, self.mba_Ap, 2)
      self.Ap = ToUns32(rlow, rhigh)
      self.leAp.setText(str(self.Ap))
    except:
      self.leCR0.setText('?')
      LL.exception('') 

  def on_tbApWr_toggle(self):
    try:
      self.leAp.clearFocus()
      svimb.WriteReg16(self.DirID, self.addrMB, self.mba_Ap, self.Ap & 0xffff)
      svimb.WriteReg16(self.DirID, self.addrMB, self.mba_Ap+1, (self.Ap & 0xffff0000) >> 16)
    except:
      self.leAp.setText('?')
      LL.exception('')  



  def on_Scan_toggle(self):
    try:
      tmpL = svimb.ReadRegs16(self.DirID, self.addrMB, self.mba_tsStart, self.mbq_tsQnt)
      #print(tmpL)               
      ba = bytearray()
      for reg in tmpL:
        ba += reg.to_bytes(2, 'little', signed = True)
      #print("ba={}".format(ba)) 
      self.scan = self.ntScan._make(self.scanS.unpack(ba))
      #print(self.scan)               
      self.llData.setText(str(self.scan.ADCcode)) 
      self.lcdDataConv.display(self.scan.T)
      self.llData_P.setText(str(self.scan.ADCcodeP)) 
      self.lcdDataConv_P.display(self.scan.P)
    except:
      LL.exception('') 


  def on_AutoScan_toggle(self):
    self.fAuto = not self.fAuto
    self.tbAutoScan.setDown(self.fAuto)    
    if (self.fAuto):
      self.trAutoScan = self.startTimer(1000)  
      print("trAutoScan = {}".format(self.trAutoScan))      

    else:
      self.killTimer(self.trAutoScan) 


  def on_leWSizeFinish(self):
    try:
      self.wSize = eval(self.leWSize.text(), {}, {})
      self.filtr = filtrP(self.wSize, self.min_cntS) 
      self.filtr_T = filtrP(self.wSize, self.min_cntS) 
    except:
      LL.exception('') 
    self.leWSize.setText(str(self.wSize))
    self.leWSize.clearFocus()


  def on_leMinCntSFinish(self):
    try:
      self.min_cntS = eval(self.leMinCntS.text(), {}, {})
      self.filtr = filtrP(self.wSize, self.min_cntS) 
      self.filtr_T = filtrP(self.wSize, self.min_cntS) 
    except:
      LL.exception('') 
    self.leMinCntS.setText(str(self.min_cntS))
    self.leMinCntS.clearFocus()

  def on_leWSizePFinish(self):
    try:
      self.wSizeP = eval(self.leWSizeP.text(), {}, {})
      self.filtr_P = filtrP(self.wSizeP, self.min_cntSP) 
      self.filtr_P1 = filtrP(self.wSizeP, self.min_cntSP) 
    except:
      LL.exception('') 
    self.leWSizeP.setText(str(self.wSize))
    self.leWSizeP.clearFocus()


  def on_leMinCntSPFinish(self):
    try:
      self.min_cntSP = eval(self.leMinCntSP.text(), {}, {})
      self.filtr_P = filtr(self.wSizeP, self.min_cntSP) 
      self.filtr_P1 = filtr(self.wSizeP, self.min_cntSP)
    except:
      LL.exception('') 
    self.leMinCntSP.setText(str(self.min_cntSP))
    self.leMinCntSP.clearFocus()

#---
class CfmTPConf(QtGui.QMainWindow, Ui_fmTPConf): 
  # DirID - активное направление MODBUS 
  # addrMB - адрес конфигурируемого милливольтметра на направлении DirID
  # wnCaption - заголовок окна

  # новые параметры в редактируемой копии конфигурации милливольтметра
  #  n_addrMB - адрес в сети MODBUS
  #  n_thrAT  - предельно допустимая распределенная пауза в приемном пакете 
  #  n_CR0      - код АЦП при температуре 0 С (32р) [unsigned]
  #  n_Ka       - коэффициент типа термометра-сопротивления (1024/a) (32р) [unsigned]
  #  n_ADC_mode - загружаемое значение в регистр mode AЦП
  #  n_ADC_conf - загружаемое значение в регистр configuration AЦП
  #  n_ADC_IO   - загружаемое значение в регистр IO AЦП (младший байт)
  #  n_SerNum   - серийный номер узла

  # раскладка карты MODBUS для параметризации термометра:
  # mbv_CR0        - код АЦП при температуре 0 С в SysVar (32р) [unsigned]
  # fUpdConf       - дискретная команда на запись редактируемой копии в энергонезависимую память
  # следующие поля заданы в виде регистровых смещений относительно Base
  #  BaseMain      - начало активной конфигурации (доступна только для чтения)
  #  BaseCopy      - начало редактируемой копии конфигурации
  #  offs_addr     - адрес данного устройства в сети MODBUS 
  #  offs_thrAT    - предельно допустимая распределенная пауза в приемном пакете 
  #  offs_CR0      - код АЦП при температуре 0 С (32р) [unsigned]
  #  offs_Ka       - коэффициент типа термометра-сопротивления (1024/a) (32р) [unsigned]
  #  offs_ADC_mode - загружаемое значение в регистр mode AЦП
  #  offs_ADC_conf - загружаемое значение в регистр configuration AЦП
  #  offs_ADC_IO   - загружаемое значение в регистр IO AЦП (младший байт)
  #  offs_SerNum   - серийный номер узла 

  def __init__(self,vCE, confMB, mbv_CR0, mbv_P0, mbv_Ap):
    """ confMB - словарь с картой в регистровом\битовом поле MODBUS 
        mbv_CR0 - адрес в структуре системных переманных SysVar """

    super().__init__()
    self.setupUi(self)
    self.vCE=vCE
    self.addrMB = 1
    self.wnCaption = self.windowTitle()

    self.mbv_CR0 = mbv_CR0

    self.mbv_P0 = mbv_P0
    self.mbv_Ap = mbv_Ap

    self.fUpdConf = int(confMB["fUpdConf"])
    self.BaseMain = int(confMB["BaseMain"])
    self.BaseCopy = int(confMB["BaseCopy"])
    self.offs_addr = int(confMB["offs_addr"])
    self.offs_thrAT = int(confMB["offs_thrAT"])
    self.offs_CR0 = int(confMB["offs_CR0"])
    self.offs_Ka = int(confMB["offs_Ka"])
    self.offs_ADC_mode = int(confMB["offs_ADC_mode"])
    self.offs_ADC_conf = int(confMB["offs_ADC_conf"])
    self.offs_ADC_IO = int(confMB["offs_ADC_IO"])
    self.offs_SerNum = int(confMB["offs_SerNum"])
    try:
      self.offs_Descr = int(confMB["offs_Descr"])
      self.offs_TypeID = int(confMB["offs_TypeID"])
    except:q=0

    self.offs_P0 = int(confMB["offs_P0"])
    self.offs_Ap = int(confMB["offs_Ap"])
    self.offs_ADC_modeP = int(confMB["offs_ADC_modeP"]) 
    self.offs_ADC_confP = int(confMB["offs_ADC_confP"])
    self.offs_ADC_IOP = int(confMB["offs_ADC_IOP"])
    self.leAddrMB.editingFinished.connect(self.on_leAddrMBFinished)
    self.tbAddrMBRd.clicked.connect(self.on_tbAddrMBRd_toggle)
    self.tbAddrMBWr.clicked.connect(self.on_tbAddrMBWr_toggle)
    self.lethrAT.editingFinished.connect(self.on_lethrATFinished)
    self.tbthrATRd.clicked.connect(self.on_tbthrATRd_toggle)
    self.tbthrATWr.clicked.connect(self.on_tbthrATWr_toggle)
    self.leCR0.editingFinished.connect(self.on_leCR0Finished)
    self.tbCR0RdVar.clicked.connect(self.on_tbCR0RdVar_toggle)
    self.tbCR0Rd.clicked.connect(self.on_tbCR0Rd_toggle)
    self.tbCR0Wr.clicked.connect(self.on_tbCR0Wr_toggle)
    self.leKa.editingFinished.connect(self.on_leKaFinished)
    self.tbKaRd.clicked.connect(self.on_tbKaRd_toggle)   
    self.tbKaWr.clicked.connect(self.on_tbKaWr_toggle)
    self.leMode.editingFinished.connect(self.on_leModeFinished)
    self.tbModeRd.clicked.connect(self.on_tbModeRd_toggle)
    self.tbModeWr.clicked.connect(self.on_tbModeWr_toggle)
    self.leConf.editingFinished.connect(self.on_leConfFinished)
    self.tbConfRd.clicked.connect(self.on_tbConfRd_toggle)
    self.tbConfWr.clicked.connect(self.on_tbConfWr_toggle)
    self.leIO.editingFinished.connect(self.on_leIOFinished)
    self.tbIORd.clicked.connect(self.on_tbIORd_toggle)
    self.tbIOWr.clicked.connect(self.on_tbIOWr_toggle)
    self.leSerNum.editingFinished.connect(self.on_leSerNumFinished)
    self.tbSerNumRd.clicked.connect(self.on_tbSerNumRd_toggle)
    self.tbSerNumWr.clicked.connect(self.on_tbSerNumWr_toggle)

    self.leP0.editingFinished.connect(self.on_leP0Finished)
    self.tbP0RdVar.clicked.connect(self.on_tbP0RdVar_toggle)
    self.tbP0Rd.clicked.connect(self.on_tbP0Rd_toggle)
    self.tbP0Wr.clicked.connect(self.on_tbP0Wr_toggle)

    self.leAp.editingFinished.connect(self.on_leApFinished)
    self.tbApRdVar.clicked.connect(self.on_tbApRdVar_toggle)
    self.tbApRd.clicked.connect(self.on_tbApRd_toggle)
    self.tbApWr.clicked.connect(self.on_tbApWr_toggle)

    self.leMode_P.editingFinished.connect(self.on_leMode_PFinished)
    self.tbPModeRd.clicked.connect(self.on_tbPModeRd_toggle)
    self.tbPModeWr.clicked.connect(self.on_tbPModeWr_toggle)

    self.leConf_P.editingFinished.connect(self.on_leConf_PFinished)
    self.tbPConfRd.clicked.connect(self.on_tbPConfRd_toggle)
    self.tbPConfWr.clicked.connect(self.on_tbPConfWr_toggle)

    self.leIO_P.editingFinished.connect(self.on_leIO_PFinished)
    self.tbPIORd.clicked.connect(self.on_tbPIORd_toggle)
    self.tbPIOWr.clicked.connect(self.on_tbPIOWr_toggle)

    self.teDescribe.cursorPositionChanged.connect(self.on_teDescribeFinished)
    self.tbDescribeRd.clicked.connect(self.on_tbDescribeRd_toggle)
    self.tbDescribeWr.clicked.connect(self.on_tbDescribemWr_toggle)
    self.leTypeID.editingFinished.connect(self.on_leTypeIDFinished)
    self.tbTypeIDRd.clicked.connect(self.on_tbTypeIDRd_toggle)
    self.tbTypeIDWr.clicked.connect(self.on_tbTypeIDWr_toggle)

    self.tbSave.clicked.connect(self.on_tbSave_toggle) 

    self.n_TypeID=''


  def show(self, DirID, addrMB):
    """ DirID - активное направление MODBUS 
        addrMB - адрес конфигурируемого термометра на направлении DirID """
    self.DirID = DirID
    self.addrMB = addrMB  # TODO обновить значение в поле ввода
    self.setWindowTitle(self.wnCaption + " [{:02X}h]".format(self.addrMB))
    super().show()


  def on_leAddrMBFinished(self):
    try:
      self.n_addrMB = eval(self.leAddrMB.text(), {}, {})
    except:
      self.leAddrMB.setText(str(ToUns16(self.n_addrMB)))
      LL.exception('') 
    self.leAddrMB.clearFocus()    


  def on_tbAddrMBRd_toggle(self):
    try:
      tmpT = svimb.ReadRegs16(self.DirID, self.addrMB, self.BaseCopy + self.offs_addr, 1) 
      self.n_addrMB = tmpT[0]
      self.leAddrMB.setText(str(ToUns16(self.n_addrMB)))    
    except:
      self.leAddrMB.setText('?') 
      LL.exception('') 


  def on_tbAddrMBWr_toggle(self):
    try:
      self.leAddrMB.clearFocus() 
      self.n_addrMB = svimb.WriteReg16(self.DirID, self.addrMB, self.BaseCopy + self.offs_addr, self.n_addrMB)
      self.leAddrMB.setText(str(ToUns16(self.n_addrMB)))
    except:
      self.leAddrMB.setText('?')
      LL.exception('') 


  def on_lethrATFinished(self):
    try:
      self.n_thrAT = eval(self.lethrAT.text(), {}, {})
    except:
      self.lethrAT.setText(str(ToUns16(self.n_thrAT)))
      LL.exception('')
    self.lethrAT.clearFocus() 


  def on_tbthrATRd_toggle(self):
    try:
      tmpT = svimb.ReadRegs16(self.DirID, self.addrMB, self.BaseCopy + self.offs_thrAT, 1) 
      self.n_thrAT = tmpT[0]
      self.lethrAT.setText(str(ToUns16(self.n_thrAT)))    
    except:
      self.lethrAT.setText('?') 
      LL.exception('')


  def on_tbthrATWr_toggle(self):
    try:
      self.lethrAT.clearFocus() 
      self.n_thrAT = svimb.WriteReg16(self.DirID, self.addrMB, self.BaseCopy + self.offs_thrAT, self.n_thrAT)
      self.lethrAT.setText(str(ToUns16(self.n_thrAT))) 
    except:
      self.lethrAT.setText('?')
      LL.exception('')


  def on_leCR0Finished(self):
    try: 
      self.n_CR0 = eval(self.leCR0.text(), {}, {})
    except:
      self.leCR0.setText(str(self.n_CR0))
      LL.exception('')
    self.leCR0.clearFocus() 


  def on_tbCR0RdVar_toggle(self):
    try:
      (rlow, rhigh) = svimb.ReadRegs16(self.DirID, self.addrMB, self.mbv_CR0, 2)
      self.n_CR0 = ToUns32(rlow, rhigh)
      self.leCR0.setText(str(self.n_CR0))    
    except:
      self.leCR0.setText('?') 
      LL.exception('')


  def on_tbCR0Rd_toggle(self):
    try:
      (rlow, rhigh) = svimb.ReadRegs16(self.DirID, self.addrMB, self.BaseCopy + self.offs_CR0, 2)
      self.n_CR0 = ToUns32(rlow, rhigh)
      self.leCR0.setText(str(self.n_CR0))    
    except:
      self.leCR0.setText('?') 
      LL.exception('')


  def on_tbCR0Wr_toggle(self):
    try: 
      self.leCR0.clearFocus() 
      svimb.WriteReg16(self.DirID, self.addrMB, self.BaseCopy + self.offs_CR0, self.n_CR0 & 0xffff)
      svimb.WriteReg16(self.DirID, self.addrMB, self.BaseCopy + self.offs_CR0 + 1, (self.n_CR0 & 0xffff0000) >> 16)
    except:
      self.leCR0.setText('?') 
      LL.exception('')  


  def on_leKaFinished(self):
    try: 
      self.n_Ka = eval(self.leKa.text(), {}, {})
    except:
      self.leKa.setText(str(self.n_Ka))
      LL.exception('')
    self.leKa.clearFocus() 


  def on_tbKaRd_toggle(self):
    try:
      (rlow, rhigh) = svimb.ReadRegs16(self.DirID, self.addrMB, self.BaseCopy + self.offs_Ka, 2)
      self.n_Ka = ToUns32(rlow, rhigh)
      self.leKa.setText(str(self.n_Ka))    
    except:
      self.leKa.setText('?') 
      LL.exception('')


  def on_tbKaWr_toggle(self):
    try: 
      self.leKa.clearFocus() 
      svimb.WriteReg16(self.DirID, self.addrMB, self.BaseCopy + self.offs_Ka, self.n_Ka & 0xffff)
      svimb.WriteReg16(self.DirID, self.addrMB, self.BaseCopy + self.offs_Ka + 1, (self.n_Ka & 0xffff0000) >> 16)
    except:
      self.leKa.setText('?') 
      LL.exception('')


  def on_leModeFinished(self):
    try:
      self.n_ADC_mode = int(self.leMode.text(), 16)
    except:
      self.leMode.setText("{:04X}".format(self.n_ADC_mode))
      LL.exception('')
    self.leMode.clearFocus()  


  def on_tbModeRd_toggle(self):
    try:
      tmpT = svimb.ReadRegs16(self.DirID, self.addrMB, self.BaseCopy + self.offs_ADC_mode, 1) 
      self.n_ADC_mode = ToUns16(tmpT[0])
      self.leMode.setText("{:04X}".format(self.n_ADC_mode))    
    except:
      self.leMode.setText('?') 
      LL.exception('')


  def on_tbModeWr_toggle(self):
    try:
      self.leMode.clearFocus() 
      self.n_ADC_mode = ToUns16(svimb.WriteReg16(self.DirID, self.addrMB, self.BaseCopy + self.offs_ADC_mode, self.n_ADC_mode))
      self.leMode.setText("{:04X}".format(self.n_ADC_mode)) 
    except:
      self.leMode.setText('?')
      LL.exception('')
 

  def on_leConfFinished(self):
    try:
      self.n_ADC_conf = int(self.leConf.text(), 16)
    except:
      self.leConf.setText("{:04X}".format(self.n_ADC_conf))
      LL.exception('')
    self.leConf.clearFocus() 


  def on_tbConfRd_toggle(self):
    try:
      tmpT = svimb.ReadRegs16(self.DirID, self.addrMB, self.BaseCopy + self.offs_ADC_conf, 1) 
      self.n_ADC_conf = ToUns16(tmpT[0])
      self.leConf.setText("{:04X}".format(self.n_ADC_conf))    
    except:
      self.leConf.setText('?') 
      LL.exception('')


  def on_tbConfWr_toggle(self):
    try:
      self.leConf.clearFocus() 
      self.n_ADC_conf = ToUns16(svimb.WriteReg16(self.DirID, self.addrMB, self.BaseCopy + self.offs_ADC_conf, self.n_ADC_conf))
      self.leConf.setText("{:04X}".format(self.n_ADC_conf)) 
    except:
      self.leConf.setText('?')
      LL.exception('')


  def on_leIOFinished(self):
    try:
      self.n_ADC_IO = int(self.leIO.text(), 16) & 0xff
    except:
      self.leIO.setText("{:02X}".format(self.n_ADC_IO))
      LL.exception('')
    self.leIO.clearFocus() 


  def on_tbIORd_toggle(self):
    try:
      tmpT = svimb.ReadRegs16(self.DirID, self.addrMB, self.BaseCopy + self.offs_ADC_IO, 1) 
      self.n_ADC_IO = (ToUns16(tmpT[0])) & 0xff
      self.leIO.setText("{:02X}".format(self.n_ADC_IO))    
    except:
      self.leIO.setText('?') 
      LL.exception('')


  def on_tbIOWr_toggle(self):
    try:
      self.leIO.clearFocus() 
      self.n_ADC_IO = (ToUns16(svimb.WriteReg16(self.DirID, self.addrMB, self.BaseCopy + self.offs_ADC_IO, self.n_ADC_IO))) & 0xff
      self.leIO.setText("{:02X}".format(self.n_ADC_IO))   
    except:
      self.leIO.setText('?')
      LL.exception('')


  def on_leSerNumFinished(self):
    try:
      self.n_SerNum = eval(self.leSerNum.text(), {}, {})
    except:
      self.leSerNum.setText(str(self.n_SerNum))
      LL.exception('')
    self.leSerNum.clearFocus() 


  def on_tbSerNumRd_toggle(self):
    try:
      tmpT = svimb.ReadRegs16(self.DirID, self.addrMB, self.BaseCopy + self.offs_SerNum, 1) 
      self.n_SerNum = ToUns16(tmpT[0])
      self.leSerNum.setText(str(self.n_SerNum))    
    except:
      self.leSerNum.setText('?') 
      LL.exception('')


  def on_tbSerNumWr_toggle(self):
    try:
      self.leSerNum.clearFocus() 
      self.n_SerNum = ToUns16(svimb.WriteReg16(self.DirID, self.addrMB, self.BaseCopy + self.offs_SerNum, self.n_SerNum))
      self.leSerNum.setText(str(self.n_SerNum))  
    except:
      self.leSerNum.setText('?') 
      LL.exception('')

  def on_leP0Finished(self):
    try: 
      self.n_P0 = eval(self.leP0.text(), {}, {})
    except:
      self.leP0.setText(str(self.n_P0))
      LL.exception('')
    self.leP0.clearFocus() 

  def on_tbP0RdVar_toggle(self):
    try:
      (rlow, rhigh) = svimb.ReadRegs16(self.DirID, self.addrMB, self.mbv_P0, 2)
      self.n_P0 = ToUns32(rlow, rhigh)
      self.leP0.setText(str(self.n_P0))    
    except:
      self.leP0.setText('?') 
      LL.exception('')

  def on_tbP0Rd_toggle(self):
    try:
      (rlow, rhigh) = svimb.ReadRegs16(self.DirID, self.addrMB, self.BaseCopy + self.offs_P0, 2)
      self.n_P0 = ToUns32(rlow, rhigh)
      self.leP0.setText(str(self.n_P0))    
    except:
      self.leP0.setText('?') 
      LL.exception('')

  def on_tbP0Wr_toggle(self):
    try: 
      self.leP0.clearFocus() 
      svimb.WriteReg16(self.DirID, self.addrMB, self.BaseCopy + self.offs_P0, self.n_P0 & 0xffff)
      svimb.WriteReg16(self.DirID, self.addrMB, self.BaseCopy + self.offs_P0 + 1, (self.n_P0 & 0xffff0000) >> 16)
    except:
      self.leP0.setText('?') 
      LL.exception('')  

  def on_leApFinished(self):
    try: 
      self.n_Ap = eval(self.leAp.text(), {}, {})
    except:
      self.leAp.setText(str(self.n_Ap))
      LL.exception('')
    self.leAp.clearFocus() 

  def on_tbApRdVar_toggle(self):
    try:
      (rlow, rhigh) = svimb.ReadRegs16(self.DirID, self.addrMB, self.mbv_Ap, 2)
      self.n_Ap = ToUns32(rlow, rhigh)
      self.leAp.setText(str(self.n_Ap))    
    except:
      self.leAp.setText('?') 
      LL.exception('')

  def on_tbApRd_toggle(self):
    try:
      (rlow, rhigh) = svimb.ReadRegs16(self.DirID, self.addrMB, self.BaseCopy + self.offs_Ap, 2)
      self.n_Ap = ToUns32(rlow, rhigh)
      self.leAp.setText(str(self.n_Ap))    
    except:
      self.leAp.setText('?') 
      LL.exception('')

  def on_tbApWr_toggle(self):
    try: 
      self.leAp.clearFocus() 
      svimb.WriteReg16(self.DirID, self.addrMB, self.BaseCopy + self.offs_Ap, self.n_Ap & 0xffff)
      svimb.WriteReg16(self.DirID, self.addrMB, self.BaseCopy + self.offs_Ap + 1, (self.n_Ap & 0xffff0000) >> 16)
    except:
      self.leAp.setText('?') 
      LL.exception('')  

  def on_leMode_PFinished(self):
    try:
      self.n_Mode_P = int(self.leMode_P.text(), 16) & 0xff
    except:
      self.leMode_P.setText("{:02X}".format(self.n_Mode_P))
      LL.exception('')
    self.leMode_P.clearFocus() 

  def on_tbPModeRd_toggle(self):
    try:
      tmpT = svimb.ReadRegs16(self.DirID, self.addrMB, self.BaseCopy + self.offs_ADC_modeP, 1) 
      self.n_Mode_P = (ToUns16(tmpT[0])) & 0xff
      self.leMode_P.setText("{:02X}".format(self.n_Mode_P))    
    except:
      self.leMode_P.setText('?') 
      LL.exception('')

  def on_tbPModeWr_toggle(self):
    try:
      self.leMode_P.clearFocus() 
      self.n_Mode_P = (ToUns16(svimb.WriteReg16(self.DirID, self.addrMB, self.BaseCopy + self.offs_ADC_modeP, self.n_Mode_P))) & 0xff
      self.leMode_P.setText("{:02X}".format(self.n_Mode_P))  
    except:
      self.leMode_P.setText('?') 
      LL.exception('')


  def on_leConf_PFinished(self):
    try:
      self.n_Conf_P = int(self.leConf_P.text(), 16) & 0xff
    except:
      self.leConf_P.setText("{:02X}".format(self.n_Conf_P))
      LL.exception('')
    self.leConf_P.clearFocus() 

  def on_tbPConfRd_toggle(self):
    try:
      tmpT = svimb.ReadRegs16(self.DirID, self.addrMB, self.BaseCopy + self.offs_ADC_confP, 1) 
      self.n_Conf_P = (ToUns16(tmpT[0])) & 0xff
      self.leConf_P.setText("{:02X}".format(self.n_Conf_P))    
    except:
      self.leConf_P.setText('?') 
      LL.exception('')

  def on_tbPConfWr_toggle(self):
    try:
      self.leConf_P.clearFocus() 
      self.n_Conf_P = (ToUns16(svimb.WriteReg16(self.DirID, self.addrMB, self.BaseCopy + self.offs_ADC_confP, self.n_Conf_P))) & 0xff
      self.leConf_P.setText("{:02X}".format(self.n_Conf_P))    
    except:
      self.leConf_P.setText('?') 
      LL.exception('')


  def on_leIO_PFinished(self):
    try:
      self.n_ADC_IOP = int(self.leIO.text(), 16) & 0xff
    except:
      self.leIO_P.setText("{:02X}".format(self.n_ADC_IOP))
      LL.exception('')
    self.leIO_P.clearFocus() 

  def on_tbPIORd_toggle(self):
    try:
      tmpT = svimb.ReadRegs16(self.DirID, self.addrMB, self.BaseCopy + self.offs_ADC_IOP, 1) 
      self.n_ADC_IOP = (ToUns16(tmpT[0])) & 0xff
      self.leIO_P.setText("{:02X}".format(self.n_ADC_IOP))    
    except:
      self.leIO.setText('?') 
      LL.exception('')

  def on_tbPIOWr_toggle(self):
    try:
      self.leIO_P.clearFocus() 
      self.n_ADC_IOP = (ToUns16(svimb.WriteReg16(self.DirID, self.addrMB, self.BaseCopy + self.offs_ADC_IOP, self.n_ADC_IOP))) & 0xff
      self.leIO_P.setText("{:02X}".format(self.n_ADC_IOP))   
    except:
      self.leIO_P.setText('?') 
      LL.exception('')

  def on_teDescribeFinished(self):
    a=1

  def on_tbDescribeRd_toggle(self):
    try:
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
      except: a=0
      self.n_Describe=tmptxt

      self.teDescribe.clear()
      self.teDescribe.setText(str(self.n_Describe))    
    except:
      self.teDescribe.setText('?') 
      LL.exception('')


  def on_tbDescribemWr_toggle(self):
    try:
      self.n_Describe =''
      self.n_Describe = self.teDescribe.toPlainText()+'                                                                      '
      Tmpt=[ord(c) for c in self.n_Describe]
      ltxt=len(self.n_Describe)
      self.teDescribe.clearFocus() 
      i=0
      while(i<ltxt):
       svimb.WriteReg16(self.DirID, self.addrMB, self.BaseCopy + self.offs_Descr+i, Tmpt[i])
       i=i+1
      self.teDescribe.clear()
      self.teDescribe.setText(str(self.n_Describe))  
    except:
      self.teDescribe.setText('?') 
      LL.exception('')


  def on_leTypeIDFinished(self):
    try:
      self.n_TypeID = eval(self.leTypeID.text(), {}, {})
    except:
      self.leTypeID.setText(str(self.n_TypeID))
      LL.exception('')
    self.leSerNum.clearFocus() 


  def on_tbTypeIDRd_toggle(self):
    try:
      tmpT = svimb.ReadRegs16(self.DirID, self.addrMB, self.BaseCopy + self.offs_TypeID, 1) 
      self.n_TypeID = ToUns16(tmpT[0])
      self.leTypeID.setText(str(self.n_TypeID))    
    except:
      self.leTypeID.setText('?') 
      LL.exception('')


  def on_tbTypeIDWr_toggle(self):
    try:
      self.leTypeID.clearFocus() 
      self.n_TypeID = ToUns16(svimb.WriteReg16(self.DirID, self.addrMB, self.BaseCopy + self.offs_TypeID, self.n_TypeID))
      self.leTypeID.setText(str(self.n_TypeID))  
    except:
      self.leTypeID.setText('?') 
      LL.exception('')

  def on_tbSave_toggle(self):
    try:
      svimb.WriteBit(self.DirID, self.addrMB, self.fUpdConf, 1)
    except:
      LL.exception('')
#---

class CVButton(QtGui.QToolButton):
  """ класс кнопки на основном окне СВП под вывод лицевой панели виртуального прибора """
  # vi - наименование экземпляра виртуального прибора, соответствующего данной кнопке
  cnt = 1  # счетчик для генерации уникальных наименований экземпляров 

  def __init__(self, caption, parent = None):
    """ caption - надпись на кнопке """
    super().__init__(parent)
    self.vi = caption

    self.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
    self.setArrowType(QtCore.Qt.NoArrow)
        
    font = QtGui.QFont()
    font.setFamily("Verdana")
    font.setPointSize(12)
    self.setFont(font)
        
    self.setSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
    self.setObjectName("vbut{}".format(CVButton.cnt))  # автогенерируемое наименование
    CVButton.cnt = CVButton.cnt + 1
    self.setText(caption)
    self.setFocusPolicy(QtCore.Qt.NoFocus)  # фокусировка Tab'ом сбивает фиксацию
    self.clicked.connect(self.on_toggle)


  def on_toggle(self):
    global vinstrD
    try:
      vinstrD[self.vi]['obj'].ShowFP()
    except:
      LL.exception('') 

#---
class CfmMain(QtGui.QMainWindow, Ui_fmMain):
  """ основное окно СВП (режим пользователя) """
  #  vbut - список с экземплярами CIButton (кнопки вывода лицывых панелей виртуальных приборов)
  #  dictState - словарь сохраняемых при выключении переменных\параметров
  #  fFirstShow - True - первое отображение окна ("костыль" для восстановления сохраненного расположения)
  #  fRec - флаг для блокировки рекурентного вызова closeEvent 

  def __init__(self):
    global vinstrD
    global cstateD

    super().__init__()      
    self.setupUi(self)
 
    self.fRec = False
    self.fFirstShow = True

    if 'CfmMain' in cstateD: 
      self.dictState = cstateD['CfmMain'] 
    else:
      self.dictState = {}
      cstateD['CfmMain'] = self.dictState 

    self.vbut = []
    i = 1
    for vi in sorted(vinstrD):
      bt = CVButton(vi, self.centralwidget)
      #bt = self.CreateVBut(vi) 
      self.vbut.append(bt)
      self.gridLayout.addWidget(bt, i, 0) #, alignment = QtCore.Qt.AlignHCenter)  
      i = i + 1 

    self.resize(10,10)  # переход на минимально-возможный размер, определяемый надписями на кнопках
  
  def show(self):
    super().show()
    if self.fFirstShow: 
      self.fFirstShow = False
  
      desktop = QtGui.QApplication.desktop() 
      dh = desktop.height()
      dw = desktop.width()  
      rect = self.geometry()
      self.setFixedSize(rect.width(), rect.height())

      x = safeDget(self.dictState, "win.left", dw - rect.width())
      if (x > dw):  x = dw - rect.width()

      y = safeDget(self.dictState, "win.top", dh - rect.height())
      if (y > dh):  y = dh - rect.height()

      self.setGeometry(QtCore.QRect(QtCore.QPoint(x, y), self.size()))
      

  def closeEvent(self, event):
    if self.fRec:
      # рекурентный вызов от closeAllWindows
      event.accept() 
    else:
      self.fRec = True
      rect = self.geometry()
      self.dictState["win.left"] = rect.left()
      self.dictState["win.top"] = rect.top()

      app.closeAllWindows()
      event.accept()

 

#---------------------------------------------- 
#        Глобальные переменные
# if sys.platform == 'win32' - TODO различные пути под Windows и Linux
fTech = False # флаг технологического режима (настройка, калибровка)
fTechLoad = False # флаг технологического режима (настройка, калибровка)
main_dir = os.path.dirname(os.path.abspath(__file__)) 
sstate.setStateDir(main_dir) # файлы сохраненных состояний размещаются в каталоге с основным модулем
cfg_dir = main_dir+'/conf'
log_dir = main_dir+'/log'
Cfg_tpl = {}  # вспомогательный шаблон для разбора конфигурации (словарь словарей)

vinstrD = {}  # словарь дескрипторов(по-сути словарей) доступных виртуальных приборов (ключ - наименование)
              #   значения: vtype - строка - тип виртуального прибора (требуется для выбора конструктора)
              #             obj   - экземпляр виртуального прибора (потомок от CVInstr)
              #             ВСЕ ключи из конфигурации  
              #             meas  - список наименований измерительных каналов, требующихся для работы виртуального прибора
              #                     (создается конструктором виртуального прибора)   

adataD = {}   # срез актуальных данных от измерителей (ключ - ID канала; значение - (данные, время измерения))
chanD = {}    # словарь дескрипторов (по-сути словарей) активных измерительных каналов (ключ - ID  канала)
              #   значения: DirID, DevAddr, RegAddr, наименование, Link - список наименований виртуальных приборов где используется данный канал
dirD = {}     # словарь дескрипторов (по-сути словарей) активных направлений (ключ - ID направления)
              #   значения: (cmnt - строка - комментарий)

vstateD = sstate.vstateD  # словарь сохраняемых состояний доступных виртуальных приборов (ключ - наименование)
                          #   значение: словарь параметров (например иономер хранит там профили электродов) 

cstateD = sstate.cstateD  # словарь сохраняемых состояний общего назначения (ключ - имя типа класса)
                          #   значение: словарь параметров (например СfmMain хранит там расположение окна)  
cfg_stateD = sstate.cfg_stateD
table_stateD = sstate.table_stateD


#CommonProfil_stateD = sstate.CommonProfil_stateD

LL = logging.getLogger('SVI')
fLRotated = False  # true - ротация старого сессионного лога в постоянный произведена
#----------------------------------------------

def OnDataReady(dataLst):
  """ обработчик callback данных от измерительных каналов 
      (вызывается в контексте отдельного потока svimb) """

  print(dataLst)  
  for ch_data in dataLst:
    ch_id = ch_data[0]
    if ch_id in chanD:
      for vi_key in chanD[ch_id]["Link"]:
        if vi_key in vinstrD:
          if "obj" in vinstrD[vi_key]:  vinstrD[vi_key]["obj"].NewData({chanD[ch_id]["наименование"]: ch_data}) # TODO - сгруппировать данные (возможна "пробуксовка")
 
#---      
        
def OnExit():
  """ обработчик сигнала завершения работы программы  """

  sstate.saveVstate()
  sstate.saveCstate()

  if LL.level: # логер сконфигурирован - можно оставить сообщение
    LL.I("SVI завершен")

#---
def SVIconf():
  """ сконфигурировать\переконфигурировать СВП """
  global Cfg       # конфигурация 
  global fLRotated 
  global fTechLoad 

  #--- подготовка Cfg_tpl для будущего разбора конфигурации
  tmpD = LoadCfg(cfg_dir+'/main.tpl')
  if "мультисекции" in tmpD['Default']:
    Cfg_tpl["мультисекции"] = dict.fromkeys(tmpD['Default']["мультисекции"], 1) # значение ключей пока не используется
  if "мультипараметры" in tmpD['Default']:
    Cfg_tpl["мультипараметры"] = dict.fromkeys(tmpD['Default']["мультипараметры"], 1)

  #--- загрузка конфигурации
  if fTechLoad!=True:
    Cfg = LoadCfg(cfg_dir+'/svi.conf', tpl = Cfg_tpl)
    sstate.cfg_stateD=Cfg
    sstate.cfg_stateD.update()
    sstate.save_Cfg_state()
    Cfg = LoadCfg(cfg_dir+'/tech.conf', Cfg)
    Cfg = LoadCfg(cfg_dir+'/common.conf', Cfg)
  if fTechLoad==True:
    Cfg = LoadCfg(cfg_dir+'/svi.conf', tpl = Cfg_tpl)
    sstate.load_Cfg_state()
    Cfg.update(cfg_stateD)
    Cfg = LoadCfg(cfg_dir+'/tech.conf', Cfg)
    Cfg = LoadCfg(cfg_dir+'/common.conf', Cfg)

  if not fLRotated: 
    #--- ротация в постоянный лог   
    mreg = re.compile(r'^\[.*?\]') # только строки со временем (а оно в квадратных скобках вначале)
    log.Rotate(mreg, log_dir+Cfg['Log']['SessLog'], log_dir+Cfg['Log']['PersLog'], Cfg['Log']['CodePage'])
    fLRotated = True

  #--- настройка логера 
  if not LL.level: # чтобы избежать повторной настройки при переконфигурировании
    # под Линуксом правильнее использовать класс WatchedFileHandler, чтоб не сбивать системную ротацию логов
    fh = logging.FileHandler(log_dir+Cfg['Log']['SessLog'], 'w', Cfg['Log']['CodePage'])
    #fh = log.NewFHandler(log_dir+Cfg['Log']['SessLog'], 'w', Cfg['Log']['CodePage'])
    #formF = log.SmartForm("%(asctime)s %(module)s: %(message)s", "<%H:%M:%S %d.%m.%Y>") # "неизвестные" сообщения идут с меткой времени, но не попадают в постоянный лог
    formF = log.SmartForm("%(asctime)s %(module)s: %(message)s", "<%H:%M:%S:%mS %d.%m.%Y>") # "неизвестные" сообщения идут с меткой времени, но не попадают в постоянный лог
    formF.setFormStr(log.NINFO, "%(asctime)s %(amodule)s: %(message)s", "[%H:%M:%S %d.%m.%Y]") 
    formF.setFormStr(log.NERROR, "%(asctime)s %(amodule)s: error: %(message)s", "[%H:%M:%S %d.%m.%Y]")  
    formF.setFormStr(log.NWARN, "%(amodule)s: %(message)s") 
    formF.setFormStr(log.NDEBUG, "%(amodule)s: debug: %(message)s")  
    formF.setModuleA('base', 'sqla')

    fh.setFormatter(formF)
    stdh = logging.StreamHandler(sys.stdout) 
    formStd = formF.copy()
    formStd.setFormStr(log.NINFO, "%(asctime)s %(amodule)s: %(message)s", "%H:%M:%S") # для вывода в консоль можно обойтись без даты 
    stdh.setFormatter(formStd)

    mainLL = log.NINFO - int(Cfg['Log'].get('Level'))  
    fh.setLevel(mainLL) 
    stdh.setLevel(log.NINFO)
    LL.setLevel(mainLL) 
    LL.addHandler(fh)
    LL.addHandler(stdh)

#---
def SVIstart():
  """ подготовка и запуск системы виртуальных приборов 
      (вызывать ПОСЛЕ создания  QtGui.QApplication) """

  global fTech     # флаг технологического режима 
  global Cfg       # конфигурация
  global chanD     # словарь дескрипторов измерительных каналов
  global vinstrD   # словарь дескрипторов виртуальных приборов
  global vstateD   # словарь сохраняемых состояний виртуальных приборов  
 
  chNamesD = {}    # вспомогательный словарь (key - наименование канала; value - ID канала

  #--- запуск активных направлений
  for dirC in Cfg["MODBUS RTU"]:
    tmpD = renameDK(dirC, {"скорость":"Speed", "четность":"Parity", "таймаут":"Timeout", "пауза":"ReqPause"})
    #DirID = svimb.CreateRTUdir(int(dirC["порт"]), 38400, 0, 2000, 0)
    DirID = svimb.CreateRTUdir(int(dirC["порт"]), **tmpD)

    LL.I("Направление MODBUS RTU COM{} [DirID={}] запущено успешно".format(dirC["порт"], DirID)) 
 
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

          chanD[ChID] = chD
          chNamesD[chD['наименование']] = ChID
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

          chanD[ChID] = chD
          LL.I("Измерительный канал '{}' в устройстве c адресом {} [RegAddr={:x}h DirID={}] запущен успешно".format(
                chD['наименование'], chD['DevAddr'],  chD['RegAddr'], chD['DirID'])) 

  #--- строим словарь доступных виртуальных приборов на основании конфигурации
  for vkey in Cfg["Виртуальные приборы"]:
    for vi in Cfg["Виртуальные приборы"][vkey]:
      vinstrD[vi["наименование"]] = {"vtype": vkey } 
      vinstrD[vi["наименование"]].update(vi) # переносим все ключи - экземпляр виртуального прибора потом сам разберется 

  #--- cоздаем набор виртуальных приборов на основании разобранной конфигурации
  for vikey, vi in vinstrD.items():
    if vikey not in vstateD:  vstateD[vikey] = {}  # виртуальный прибор сам заполнит свой словарь состояний
    vtype = vi["vtype"]
    if vtype == "Вольтметр":
      vi["obj"] = CVolt(vi, vstateD[vikey], fTech = fTech)
    if vtype == "Термометр":
      vi["obj"] = CTemp(vi, vstateD[vikey], fTech = fTech)
    if vtype == "Иономер":
      vi["obj"] = CIon(vi, vstateD[vikey], fTech = fTech)
    if vtype == "Измеритель тока":
      vi["obj"] = CAmper(vi, vstateD[vikey], fTech = fTech)
    if vtype == "Кислородомер":
      vi["obj"] = CO_2(vi,table_stateD, vstateD[vikey], fTech = fTech)
    if vtype == "Измеритель сопротивления":
      vi["obj"] = CCond(vi, vstateD[vikey], fTech = fTech)
    if vtype == "Сопротивление.Диапазон":
      vi["obj"] = CR_Band(vi, vstateD[vikey], fTech = fTech)
    if vtype == "Измеритель давления":
      vi["obj"] = CPressure(vi, vstateD[vikey], fTech = fTech)
    if vtype == "Модуль":
      vi["obj"] = CUnit(vi, vstateD[vikey], fTech = fTech)
    if vtype == "График":
      vi["obj"] = CChart_II(vi, vstateD[vikey], fTech = fTech)
    if vtype == "Блокнот":
      vi["obj"] = CNotepad(vi, vstateD[vikey], fTech = fTech)
    if vtype == "Протокол":
      vi["obj"] = CProtokol(vi, vstateD[vikey], fTech = fTech)

      #CChart_II
    # TODO остальные типы и отработка ошибок неизвестных типов

  #--- связка каналов с виртуальными приборами TODO - обработка ошибок 
  for vikey, vi in vinstrD.items():
    if ("obj" in vi) and ("meas" in vi):
      for chN in vi["meas"]:
        chanD[chNamesD[chN]]['Link'].append(vikey)  

  #--- установка Callback ф-ии в драйвер
  #svimb.SetDSCallback(OnDataReady) 


#---------------------------------------------- 
#        Глобальные переменные

#LL = logging.getLogger('SVI')  # сконфигурирован основным модулем

 


#----------------------------------------------
def main(argv):

  global fTech     # флаг технологического режима
  global fTechLoad     # флаг технологического режима
  #global Cfg       # конфигурация 
  global Cfg_tpl   # вспомогательный шаблон для разбора конфигурации 
  global vstateD   # словарь сохраняемых состояний виртуальных приборов  
  global cstateD   # словарь сохраняемых состояний общего назначения  
  global app      
  global winM      # основное окно (в зависимости от режима может быть технологическим или пользовательским)
  global winPC     # консоль порта
  global winMBC    # консоль драйвера MODBUS
  global winADC    # прямой доступ к AD779x 
  global winPV     # параметризация милливольтметра
  global winCV     # конфигурирование милливольтметра
  global winPT     # параметризация термометра
  global winCT     # конфигурирование термометра
  global winPTP     # параметризация термометра измеритель давления
  global winCTP     # конфигурирование термометр измеритель давления
  global winPCond     # параметризация кондуктометра
  global winCCond     # конфигурирование кондуктометра
  global dgReg     # диалог определения нового регистра
  global winConv   # окно для ввода коэффициентов масштабного преобразования для окна прямого доступа к АЦП AD779x
  global gActDirID # код активного направления (пока драйвер поддерживает только одно)
  global winSetting

  global ConfigEditor      # основное окно ()




  

  Results.InitRes()

  gActDirID = 0    # 0 - не выбрано активного направления

  atexit.register(OnExit)

  #--- определяемся с режимом работы
  fTech = False
  if len(argv):
    for s in argv:
      if s.find('naladka') != -1:   fTech = True   # запуск в технологическом режиме
      if s.find('load') != -1:   fTechLoad = True   # запуск в технологическом режиме
     
  else: # параметры отсутствуют - такое может быть только при отладочном запуске ручной загрузкой модуля в интерпретатор
    fTech = True   # технологический режим активен  

  fTech = False   # запуск в технологическом режиме
  fTechLoad = True   # запуск в технологическом режиме
  
  SVIconf()

  LL.D("argv = {}".format(argv))

  LL.I("SVI версии {} (сборка от {}) стартовал".format(__version__, __date__))
  sstate.loadVstate()  # загрузка словаря сохраняемых состояний виртуальных приборов 
  sstate.loadCstate()  # загрузка словаря состояний общего назначения 
  sstate.load_Table_state()  # загрузка словаря состояний общего назначения 
  #sstate.load_Cfg_state()  # загрузка словаря сохраняемых состояний виртуальных приборов 
  

  app = QtGui.QApplication(sys.argv)

  if fTech:
    # технологический режим - подготовка дополнительных окон  
    winM = CfmNaladka()
    winPC = CfmPortCons()
    winMBC = CfmMBCons(main_dir)
    winADC = CfmAD779x()
    winPV = CfmVPar(Cfg["Калибровка мВ"])
    winCV = CfmVConf(Cfg["Конфигурация мВ"], int(Cfg["Калибровка мВ"]["ZeroA32"]), int(Cfg["Калибровка мВ"]["mK32"]))
    winPCond = CfmCondPar(Cfg["Калибровка Кондуктометр"])
    winCCond = CfmCondConf(Cfg["Конфигурация Кондуктометр"], int(Cfg["Калибровка Кондуктометр"]["ZeroA32"]), int(Cfg["Калибровка Кондуктометр"]["mK32"]))
    winPT = CfmTPar(Cfg["Калибровка T"])
    winCT = CfmTConf(Cfg["Конфигурация T"], int(Cfg["Калибровка T"]["CR0"]))
    winPTP = CfmTPPar(Cfg["Калибровка P"])
    winCTP = CfmTPConf(Cfg["Конфигурация P"], int(Cfg["Калибровка P"]["CR0"]),  int(Cfg["Калибровка P"]["P0"]),  int(Cfg["Калибровка P"]["Ap"]))
    dgReg = CfmNewReg()
    winConv = CfmNewConv()
    #winSetting = CfmChangeVPribors()
    winM.show()
  else:
    # пользовательский режим работы
    a=0
    #svimb.SetDSCallback(OnDataReady)  # AlekB:  перенес в окончание SVIstart_3 (необходимо для нормальной работы драйвера СВП под Linux)
    svimb.SetDSCallback(OnDataReady)
    ConfigEditor=CConfigEditor(fTech,Cfg,chanD,vinstrD)

  if __name__ == '__main__': 
    ecode = app.exec_()

    sys.exit(ecode)


if __name__ == '__main__':  
  try:
    main(sys.argv) 
  #except sa.exc.InterfaceError as e: 
  #  LL.E(e.orig) 
  #  LL.exception('') 
  except SystemExit:
    pass # детализация в обработчике OnExit 
  except:
    LL.exception('') 



def Programm_SN(_DirID, _par, _new_addr, _serial_num):
    res=0
    try:
      res=svimb.WriteReg16(_DirID, 0, _new_addr, _serial_num)
    except:q=0
    return res
'''
def OpenPort(NumPort):

    DirID = svimb.CreateRTUdir(NumPort, 38400, 0, 7, 0)
    LL.I("Направление MODBUS RTU COM{} [DirID={}] запущено успешно".format(NumPort, DirID))
    '''
 
