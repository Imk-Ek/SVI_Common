﻿OrmID - исходники под цифровой модуль на базе AVR32U4
svi - система виртуальных приборов (ПО верхнего уровня)

Проект OrmID собран в Atmel Studio 6.0.1996 service pack 2,
думаю что соберется и с другими версиями.
Проект svi использует среду python 3.3.0 и расширение
PyQt gpl 4.9.5-1 - лучше воспользоваться именно этими версиями для работы

x86
http://python.org/ftp/python/3.3.0/python-3.3.0.msi
x86
http://sourceforge.net/projects/pyqt/files/PyQt4/PyQt-4.9.5/PyQt-Py3.3-x86-gpl-4.9.5-1.exe/download

Для запуска приложения верхнего уровня в консольном режиме необходимо:
1) определить переменную среды  PYTHONPATH (через системные настройки)  - путь до проекта svi (например с:\svi)
2) запустить консоль python (через меню запуска программ)
 набрать:
import svi
svi.main('')  

3) В окне "СВП Ормет" выбрать пункт меню "Отладка->Консоль порта"
4) В окне "Консоль отладки обмена" выбрать пункт меню, соответствующий COM порту,
   к которому подключен цифровой модуль - в результате драйвер svimb проинициализирует
   данный порт и определит направление обмена.
5) В окне "СВП Ормет" выбрать пункт меню "Отладка->AD779x" для вызова окна
   "Прямой доступ к AD779x", обеспечивающего работу с АЦП в интерактивном режиме
    
   Кнопка "А" на вкладке "Данные" (справа от значения "Данные АЦП") включает режим непрерывных
   измерений (т.е. взятие отсчетов с АЦП каждые 2с) 

6) Для завершения работы достаточно набрать в консоли python Ctr-Z и <enter>, либо воспользоваться
   командой "Закрыть все окна" из всплывающего меню на панели задач