# -*- coding: utf-8 -*-

import os
import pickle
import logging
LL = logging.getLogger('SVI')


# ---------------------------------------------- 
#   сохранение\восстановление состояния СВП
# ---------------------------------------------- 


def setStateDir(spath):
  """ установка пути по которому будут размещаться файлы с сохраненными состояниями """
  global state_dir

  state_dir = spath


def saveDict(fname, dname):
  """ запись словаря dname в файл fname """
  if dname:
    with open(fname, 'wb') as pfile:
      pickle.dump(dname, pfile)


def loadVstate():
  """ загрузка словаря сохраняемых состояний виртуальных приборов (vstateD) """
  global vstateD

  try: 
    fname = state_dir+'/vstate.pk'
    if os.path.isfile(fname):
      with open(fname, 'rb') as pfile:
        vstateD.update(pickle.load(pfile))
      LL.I("Загрузка {} выполнена успешно".format(fname))
    else:
      LL.I("Отсутствует {} - словарь vstateD пустой".format(fname)) 
  except:
    LL.E("Ошибка при загрузке {}".format(fname))
    LL.exception('') 


def loadCstate():
  """ загрузка словаря состояний общего назначения """ 
  global cstateD 

  try:
    fname = state_dir+'/cstate.pk'
    if os.path.isfile(fname):
      with open(fname, 'rb') as pfile:
        cstateD.update(pickle.load(pfile))
      LL.I("Загрузка {} выполнена успешно".format(fname))
    else:
      LL.I("Отсутствует {} - словарь cstateD пустой".format(fname)) 
  except:
    LL.E("Ошибка при загрузке {}".format(fname))
    LL.exception('')   


def saveVstate():
  """ сохранение словаря состояний виртуальных приборов (vstateD) """
  global vstateD

  try: 
    fname = state_dir+'/vstate.pk'
    if vstateD:
      with open(fname, 'wb') as pfile:
        pickle.dump(vstateD, pfile)
      LL.I("Сохранение {} выполнено успешно".format(fname)) 
    else:
      LL.I("Словарь vstateD пустой - сохранять в файл нечего")  
  except:
    LL.E("Ошибка при сохранении {}".format(fname))   
    LL.exception('')


def saveCstate():
  """ сохранение словаря состояний общего состояния (сstateD) """
  global cstateD

  try: 
    fname = state_dir+'/cstate.pk'
    if vstateD:
      with open(fname, 'wb') as pfile:
        pickle.dump(cstateD, pfile)
      LL.I("Сохранение {} выполнено успешно".format(fname)) 
    else:
      LL.I("Словарь cstateD пустой - сохранять в файл нечего")  
  except:
    LL.E("Ошибка при сохранении {}".format(fname))   
    LL.exception('')


#Загрузка и сохранение конфигурации параметров
def load_Cfg_state():
  """ загрузка словаря конфигурации параметров общего назначения """ 
  global cfg_stateD 

  try:
    fname = state_dir+'/cfg_state.pk'
    if os.path.isfile(fname):
      with open(fname, 'rb') as pfile:
        cfg_stateD.update(pickle.load(pfile))
      LL.I("Загрузка {} выполнена успешно".format(fname))
    else:
      LL.I("Отсутствует {} - словарь cfg_stateD пустой".format(fname)) 
  except:
    LL.E("Ошибка при загрузке {}".format(fname))
    LL.exception('')   

def save_Cfg_state():
  """ сохранение словаря конфигурации параметров состояния (сstateD) """
  global cfg_stateD

  try: 
    fname = state_dir+'/cfg_state.pk'
    if cfg_stateD:
      with open(fname, 'wb') as pfile:
        pickle.dump(cfg_stateD, pfile)

     #########################################
      LL.I("Сохранение {} выполнено успешно".format(fname)) 
    else:
      LL.I("Словарь cfg_stateD пустой - сохранять в файл нечего")  
  except:
    #LL.E("Ошибка при сохранении {}".format(fname)) 
    q=1
    #LL.exception('')

#Загрузка и сохранение таблиц параметров
def load_Table_state():
  """ загрузка словаря таблиц данных """ 
  global table_stateD 

  try:
    fname = state_dir+'/table_state.pk'
    if os.path.isfile(fname):
      with open(fname, 'rb') as pfile:
        table_stateD.update(pickle.load(pfile))
      LL.I("Загрузка {} выполнена успешно".format(fname))
    else:
      LL.I("Отсутствует {} - словарь table_stateD пустой".format(fname)) 
  except:
    LL.E("Ошибка при загрузке {}".format(fname))
    LL.exception('')   

def save_Table_state():
  """ сохранение словаря таблиц данных (table_stateD) """
  global table_stateD

  try: 
    fname = state_dir+'/table_state.pk'
    if table_stateD:
      with open(fname, 'wb') as pfile:
        pickle.dump(table_stateD, pfile)
      LL.I("Сохранение {} выполнено успешно".format(fname)) 
    else:
      LL.I("Словарь table_stateD пустой - сохранять в файл нечего")  
  except:
    LL.E("Ошибка при сохранении {}".format(fname))   
    LL.exception('')

#Загрузка и сохранение  параметров режима наладки
def load_Naladka_state():
  """ загрузка словаря таблиц данных """ 
  global Naladka_stateD 

  try:
    fname = state_dir+'/Naladka_state.pk'
    if os.path.isfile(fname):
      with open(fname, 'rb') as pfile:
        Naladka_stateD.update(pickle.load(pfile))
      LL.I("Загрузка {} выполнена успешно".format(fname))
    else:
      LL.I("Отсутствует {} - словарь Naladka_stateD пустой".format(fname)) 
  except:
    LL.E("Ошибка при загрузке {}".format(fname))
    LL.exception('')   

def save_Naladka_state():
  """ сохранение словаря таблиц данных (table_stateD) """
  global Naladka_stateD

  try: 
    fname = state_dir+'/Naladka_state.pk'
    if Naladka_stateD:
      with open(fname, 'wb') as pfile:
        pickle.dump(Naladka_stateD, pfile)
      LL.I("Сохранение {} выполнено успешно".format(fname)) 
    else:
      LL.I("Словарь Naladka_stateD пустой - сохранять в файл нечего")  
  except:
    LL.E("Ошибка при сохранении {}".format(fname))   
    LL.exception('')

#---------------------------------------------- 
#        Глобальные переменные

state_dir = None  # устанавливается setStateDir из основного модуля (svi)
vstateD = {}  # словарь сохраняемых состояний доступных виртуальных приборов (ключ - наименование)
              #   значение: словарь параметров (например иономер хранит там профили электродов) 

cstateD = {}  # словарь сохраняемых состояний общего назначения (ключ - имя типа класса)
              #   значение: словарь параметров (например СfmMain хранит там расположение окна)

cfg_stateD = {}  # словарь

table_stateD = {}  # словарь
Naladka_stateD = {}  # словарь


#LL = logging.getLogger('SVI')