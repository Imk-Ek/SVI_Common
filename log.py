# -*- coding: utf-8 -*-
""" дополнительные возможности логирования.
    подключать этот модуль самым ПЕРВЫМ, так как он переопределяет базовый класс
    в системе логирования Python"""
import logging, traceback, os

#--- дополнительные уровни логирования (рассчитаны на срабатывание от уровня INFO)
NDEBUG = logging.INFO + 1
NWARN  = logging.INFO + 2
NERROR = logging.INFO + 3
NINFO  = logging.INFO + 4
#---


class MaskHandler(logging.Handler): 
  """ маскирующий и перенаправляющий обработчик сообщений 
      ("заточен" под трансляцию SQL запросов из движка SA) 
  """
  def __init__(self, destlog, destlevel = None, level = logging.NOTSET):
    """ destlog   - экземляр лога, в который будут перенаправляться сообщения данным обработчиком
        destlevel - под какой уровень будут маскироваться перенаправляемые сообщения
                    (если None - то маскировка не производится и сообщение передается "как есть") 
    """
    self.destlog = destlog # TODO проверку типа  
    logging.Handler.__init__(self, level)
    self.destlevel = destlevel 

  def emit(self, record):
    if self.destlevel:
      record.levelno = self.destlevel
    self.destlog.handle(record)

  def handler(self, record):
    """ т.к. это перенаправляющий обработчик, 
        в блокировке и фильтрации нет смысла - все будет выполнено 
        в экземпляре лога
    """
    self.emit(self, record)


class SmartForm(logging.Formatter):
  """ форматировщик записей в лог, поддерживающий разные форматы 
      для сообщений разного уровня, а также назначение псевдонимов модулям
      (возможность замещения строки формата с %(module)s на %(amodule)s)  
       sfmtD - словарь "персональных" форматов 
               (ключ - уровень сообщения,  значение - кортеж из fmt, datefmt)
       modD  - словарь псевдонимов модулей
               (ключ - имя модуля, значение - псевдоним, подставляемый по строке %(amodule)s   
  """
  def __init__(self, fmt=None, datefmt=None):
    """ устанавливает формат строки лога fmt и формат данных datefmt для всех сообщений
        (потом можно задать для каждого уровня сообщений свою раскладку)
    """ 
    logging.Formatter.__init__(self, fmt, datefmt)
    self.sfmtD = {}
    self.modD = {} 

  def setFormStr(self, level, fmt=None, datefmt=None):
    """ установить "персональный" формат для сообщений уровня level
    """  
    self.sfmtD[level] = (fmt, datefmt) 

  def copyFormStr(self, l_from, l_to):
    """ скопировать настройки для сообщений уровня l_from, в уровень l_to
    """
    self.sfmtD[l_to] = self.sfmtD[l_from] 

  def setModuleA(self, mname, aname):
    """ назначить псевдоним aname модулю mname
    """ 
    self.modD[mname] = aname

  def format(self, record):
    fmt, datefmt = self.sfmtD.get(record.levelno, (self._fmt, self.datefmt))
    record.amodule = self.modD.get(record.module, record.module) # при отсутствии псевдонима, им служит имя модуля

    record.message = record.getMessage()
    if fmt.find("%(asctime)") >= 0:
      record.asctime = self.formatTime(record, datefmt)
    s = fmt % record.__dict__
    if record.exc_info:
      # Cache the traceback text to avoid converting it multiple times
      # (it's constant anyway)
      if not record.exc_text:
        record.exc_text = self.formatException(record.exc_info)
    if record.exc_text:
      if s[-1:] != "\n":
        s = s + "\n"
      s = s + record.exc_text
    return s

  def copy(self):
    """ возвращает новый объект - копию данного
        (для упрощения переноса настроек)
    """
    new = SmartForm(self._fmt, self.datefmt)  
    new.sfmtD = self.sfmtD.copy()
    new.modD = self.modD.copy() 
    return new  


class NewLogger(logging.Logger):
  """ класс с дополнительными уровнями логирования под
      концепт с сессионным и накопительным логами
       ninfo   - временной штамп (далее ВШ), сообщение
       nerror  - ВШ, модуль, сообщение 
       nwarn   - модуль, сообщение
       ndebug  - модуль, debug: сообщение   
  """
  def __init__(self, name, level = logging.NOTSET):
    logging.Logger.__init__(self, name, level)

  def I(self, msg, *args, **kwargs):
    if self.isEnabledFor(NINFO): 
      self._log(NINFO, msg, args, **kwargs)
 
  def E(self, msg, *args, **kwargs):
    if self.isEnabledFor(NERROR): 
      self._log(NERROR, msg, args, **kwargs)
  
  def W(self, msg, *args, **kwargs):
    if self.isEnabledFor(NWARN): 
      self._log(NWARN, msg, args, **kwargs)

  def D(self, msg, *args, **kwargs):
    if self.isEnabledFor(NDEBUG): 
      self._log(NDEBUG, msg, args, **kwargs)


def Rotate(reobj, sessn, persn, codep): 
  """ротация сессионного лога в постоянный
     (сессионный лог также получает дополнительное расширение .old -  
      т.е. так сохраняется сессионный лог прошлой сессии)
      reobj - скомпилированный регэксп, при совпадении с которым, строка из сессионного копируется в постоянный лог
      sessn - полное имя сесионного лога
      persn - полное имя постоянного лога
      codep - кодовая страница логов
  """
  if os.path.isfile(sessn):
    with open(sessn, 'r', encoding = codep) as sess, open(persn, 'a', encoding = codep) as pers:
      for line in sess:
        if reobj.match(line):
          pers.write(line)

    old_sessn = sessn + '.old'
    if os.path.isfile(old_sessn):  os.remove(old_sessn) # в Windows нет атомарного переименовывания
    os.rename(sessn, old_sessn)


logging.addLevelName(NINFO, 'NINFO')
logging.addLevelName(NERROR, 'NERROR')
logging.addLevelName(NWARN, 'NWARN')
logging.addLevelName(NDEBUG, 'NDEBUG')

logging.setLoggerClass(NewLogger)