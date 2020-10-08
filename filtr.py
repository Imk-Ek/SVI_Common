# -*- coding: utf-8 -*-

import math
from collections import namedtuple

class filtrP:
  # wSize    - размер окна
  # cntS     - кол-во реально учитываемых сэмплов в окне
  # min_cntS - минимально приемлимое значение оставшихся в окне сэмплов для формирования результата
  # NumPass  - кол-во проходов алгоритма для отсеивания всех промахов
  # Average  - среднее значение, расчитанное по окну сэмплов (int) 
  # Disp     - дисперсия, расчитанное по окну сэмплов (int) 
  # Sg       - сигма
  # last_Average - значение среднего рассчитанное в прошлый вызов фильтра 
  #                (используется если не удалось получить достоверного результата в текущую итерацию)
  # lstSmp   - список - окно входных сэмплов 
  # lstMark  - список флагов: True - отсчет считается промахом 

  def __init__(self, wSize, min_cntS):
    self.wSize = wSize
    self.min_cntS = min_cntS
    self.lstSmp = list(0 for x in range(wSize))   
    self.lstDev2 = list(0 for x in range(wSize))  
    self.NumPass = 0
    self.last_Average = 0


  def OnePass(self, sample = None):
    """ один проход расчетов метод - обновляет cntS, Average, Disp   
        с учетом очередного отсчета sample (которого может и не быть в мультипроходном режиме) """

    if sample != None:
      del self.lstSmp[0]
      self.lstSmp.append(sample)
      self.lstMark = list(False for x in range(self.wSize)) 

    self.cntS = self.wSize  # кол-во реально учитываемых сэмплов
    acc = 0
    for i in range(self.wSize):
      if (self.lstMark[i]):  self.cntS -= 1  # промах
      else:                  acc += self.lstSmp[i]  
    self.Average = acc // self.cntS
    
    acc = 0
    for i in range(self.wSize):
      if not(self.lstMark[i]):
        tmp = self.lstSmp[i] - self.Average
        #self.lstDev2[i] = tmp * tmp
        acc += tmp * tmp 

    self.Disp = acc // self.cntS
    self.Sg = math.sqrt(self.Disp)


  def Check(self, Thres):
    """ проверка результатов и отметка промахов на базе порога Thres (отклонение от среднего)
        метод возвращает True если новых промахов не обнаружено """
 
    fRes = True
    for i in range(self.wSize):
      if not (self.lstMark[i]):
        if ((abs(self.lstSmp[i] - self.Average)) > Thres):
          self.lstMark[i] =  True  # промах
          fRes = False

    return fRes

    
  def newS(self, sample):
    """ основной расчетный метод - возвращает текущий результат фильтрации 
        с учетом очередного отсчета sample (или производит перерасчет если sample = None) """

    self.NumPass = 1
    self.OnePass(sample)
    while 1:
      fBadRes = (self.cntS < self.min_cntS)
      if self.Check(3 * self.Sg) or fBadRes:  break
      self.NumPass += 1   
      self.OnePass()
    
    if fBadRes:  return self.last_Average
    else:
      self.last_Average = self.Average
      return self.Average