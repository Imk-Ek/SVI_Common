
#import sys, traceback
import logging
from PyQt4 import QtCore, QtGui 
#import sstate
from datetime import datetime
from common import *
from vp_classes import *
import Results
if PCFlag==1:from fpO_2_2 import Ui_fpO_2
if PCFlag==2:from fpO_2_2_t import Ui_fpO_2
from fmO_2Calib import Ui_fmO_2Calib
from fmSelectProfil_O2 import Ui_fmSelectProfil_O2
from vinstr import CVInstr
LL = logging.getLogger('SVI')
from PyQt4.QtCore import SIGNAL
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

#---
class CO_2(CVInstr):
  """ виртуальный кислородомер """
  #  measI - наименование измерительного канала напряжения, связанного с данным экземпляром иономера
  #  measT - наименование измерительного канала температуры, связанного с данным экземпляром иономера
  #  lastT - последнее значение температуры, полученное из измерительного канала
  #  timeT - время измерения температуры
  #  lastN - последнее значение напряжения,  полученное из измерительного канала
  #  timeN - время измерения температуры
  #  techT - температура, введенная вручную с лицевой панели
  #  workT - температура, на основании которой был выполнен последний расчет pX (зависит от режима)
  #  profD - словарь доступных профилей  (key - наименование; value - экземпляр CIProf) (при сохранение - словарь инициализационных контейнеров профилей)
  #  actPr - активный профиль (экземпляр CIProf - по-сути указатель на value в profD)
  #  actPrName - наименование активного профиля (сохраняется при выключении)  (по-сути key в profD)

  #      pStDict- таблица значений зависимости концентрации кислорода в воде от температуры 
  #      pH2ODict-таблица давлений насыщенного пара воды, кПа

  #  внешние свойства:
  #    fTempTech - True  - режим ручного ввода температуры (_fTempTech - private копия)
  #                False - автоматическое сканирование измерителя температуры                  
  #    fTempComp - True  - режим термокоррекции включен (_fTempComp - private копия)
  #    fPressTech - True  - режим ручного ввода давления (_fPressTech - private копия)
  #                False - автоматическое сканирование измерителя давления                  
  #    fPressComp - True  - режим коррекции по давлению включен (_fPressComp - private копия)
  #    fDlog     - True - технологическое логирование в консоль

  def __init__(self,vCE, dcfg, dstate_ = {}, dstate = {}, dSize={}, LocalProfilsDict={},  fTech = False):
    super().__init__(dcfg, dstate, fTech)
    self.vCE=vCE
    self.Name=dcfg['наименование']
    self.ParamMess=dSize['VPParam']
    self.InputUnit=[0,0,0,0]
    self.InputVal=[0,0,0,0]
    self.OutputVal=[0,0,0,0]
    self.InputUnit[0]=dSize['VPChModulNameList'][0]
    self.InputUnit[1]=dSize['VPChModulNameList'][1]
    self.InputUnit[2]=dSize['VPChModulNameList'][2]
    self.InputVal[0]=dSize['VPChNameList'][0]
    self.InputVal[1]=dSize['VPChNameList'][1]
    self.InputVal[2]=dSize['VPChNameList'][2]
    self.OutputVal[0]=dSize['VPChOutTypeList'][0]
    self.OutputVal[1]=dSize['VPChOutTypeList'][1]
    self.C_ed_0='мг/дм3'
    self.C_ed_1='%'
    self.C_ed_2='oC'
    self.C_ed_3='кПа'
    #self.OutputVal[2]=dSize['VPChOutTypeList'][2]
    #self.OutputVal[3]=dSize['VPChOutTypeList'][3]
    self.closeFlag=0  
    Results.Result_Dict[self.Name]={}
    Results.Result_Dict[self.Name][self.OutputVal[0]]=0
    Results.Result_Dict[self.Name][self.OutputVal[1]]=0
    Results.Result_Dict[self.Name]['В блокнот']=0
    self.InLight_Notepad=0
    self.ID_VP='0'

    self.MessMode=0
    self.lastP=0.0
    self.lastT=0.0
    self.S=0.0
    self.Sp=0.0
    self.A_1=0.0
    self.A_0=0.0
    self.Ap_0=0.0
    self.P_curr=0.0
    self.T_curr=0.0
    self.P_grad=0.0
    self.T_grad=0.0
    self.Sensor=0
    self.Ap_1=0
    self.Ap_2=100
    self.A_izm=0.0
    # TODO обработку ошибок конфигурации
    '''dstate['pStDict']=0
    dstate['pH2ODict']=0
    dstate['pSaltDict']=0
    self.dictState.update
    sstate.saveVstate()'''
    self.dictStateTable = dstate_
    '''self.dictStateTable['pStDict']=dstate['pH2ODict']
    self.dictStateTable['pH2ODict']=dstate['pStDict']
    self.dictStateTable['pSaltDict']=dstate['pSaltDict']
    self.dictStateTable.update()
    sstate.save_Table_state()'''
    if((self.ParamMess=='0')or(self.ParamMess=='2')):
      self.measI = self.dictCfg["каналТок"]
      self.measT = self.dictCfg["каналТемпература"]
      self.measP = self.dictCfg["каналДавление"]
      self.dictCfg["meas"] = [self.measI, self.measT, self.measP] # фактически вносится в vinstrD

    if(self.ParamMess=='1'):
      self.timer = QtCore.QTimer()
      self.timer.timeout.connect(self.NewDataTimer)
      self.timer.start(1000)

    self.CurrProfil=''
    self.LastProfil=''
    self.Name=dcfg['наименование']
    self.ProfilsDict=LocalProfilsDict
    self.ProfilsDict.setdefault('Кислородомер',{})
    self.ProfilsDict['Кислородомер'].setdefault(self.Name,{})
    self.LastProfil=self.ProfilsDict['Кислородомер'][self.Name].setdefault('Текущий профмль','')


    self.TypeMess=0
    self.widthD = 5
    self.precD = 3
    self.formS = "{:"+str(self.widthD)+"."+str(self.precD)+"f}" 
    self.widthD1 = 4
    self.precD1 = 1
    self.formSp = "{:"+str(self.widthD1)+"."+str(self.precD1)+"f}" 
    self._fTempTech = False
    self._fTempComp = True 
    self._fPressTech = False
    self._fPressComp = True 
    self._fDlog = False
    self.techT = 20
    self.workT = 20

    self.techP = 100
    self.workP = 100

    self.lastT = 20    # ВРЕМЕННО - TODO решить вопрос с запуском иономера при неисправном термометре
    self.lastP = 760     # ВРЕМЕННО - давление

    self.ManualT_Flag=0
    self.OffT_Flag=0
    self.AutoT_Flag=0
    self.ManualP_Flag=0
    self.OffP_Flag=0
    self.AutoP_Flag=0


    self.P_O2_mmrtst=0.0
    self.P_O2_kPa=0
    self.P_O2_percent=0
    self.P_O2_mgdm3=0
    self.P_O2_mmrtst_=0.0
    self.P_O2_kPa_=0
    self.P_O2_percent_=0
    self.P_O2_mgdm3_=0
    self.P_O2_percent_min=0
    self.P_O2_mgdm3_min=0
    self.P_O2_percent_max=0
    self.P_O2_mgdm3_max=0
    self.P_O2_Draw=0
    self.P_b=0  #Барометрическое давление, мм.рт.ст.  
    self.X_percent=0  #% содержание кислорода в газовой смеси, %
    self.p_H2O=0 #давление насыщенных водяных паров при температуре измерения, мм.рт.ст.
    self.He=0 #коэффициент растворимости кислорода при температуре измерения, мг/дм3/мм.рт.ст
    self.C_O2tabl=0 #концентрация кислорода в дистиллированной воде для данной температуры, из таблицы. 
    self.p_O2_vozduh=0# парциальное давление кислорода в воздухе для P_b=760 мм.рт.ст., X_percent=20.93 при данной температуре 
    self.T_grad=0# Температура градуировки прибора
    self.T_izm=0# Темпреатура измерения
    self.He_grad=0 #коэффициент растворимости кислорода при температуре измерения при градуировке , мг/дм3/мм.рт.ст
    self.He_izm=0 #коэффициент растворимости кислорода при температуре измерения при измерении , мг/дм3/мм.рт.ст
    self.A_ist_mgdm3=0# истинное значение pO2
    self.A_ist_mm_kpa=0# истинное значение pO2
    self.A_ist_membr=0# истинное значение pO2
    self.A_izm=0# измеренное значение pO2
    self.Salt=0.0
    #self.pH2ODict = {}
    #self.pStDict = {}
    #self.pH2ODict=self.dictState['pH2ODict']
    #self.pStDict=self.dictState['pStDict']


    self.dSize=dSize
    self.width=self.dSize.setdefault('width',100)
    self.height=self.dSize.setdefault('height',100)
    self.x=self.dSize.setdefault('x',100)
    self.y=self.dSize.setdefault('y',100) 

    self.winProbaID =CfmProbaID(self)
    self.winAboutVP =CfmAboutVP(self)
    self.winMessage =CfmMessage(self)
    self.Profils=CProfilsC(self,self.ProfilsDict)
    self.win = CfpO_2(self)
    self.winSelectProfil = CfmSelectProfil_O2(self)
    self.winCO_2 = CfmO_2Calib(self)

    tmppr=''
    self.LastProfil=self.ProfilsDict['Кислородомер'][self.Name]['Текущий профмль']
    tmppr=self.LastProfil
    try:
      self.Profils.LoadProfil(self.LastProfil)
      self._PrName=self.LastProfil
    except:
        tmppr='не выбран' 
    if((tmppr=='не выбран')|(tmppr=='')|(tmppr=='(нет)')):
        cntpr=self.Profils.Listcount
        if(cntpr>0):
                prname=self.ProfilsDict['Кислородомер']['List'][0]
                try:
                   self.Profils.PrName=prname
                   self.Profils.LoadProfil(prname)
                   self._PrName=prname
                   #tmppr=self.Profils.PrName
                   tmppr=self.Profils.PrName
                except:
                    tmppr='не выбран'
        if(cntpr==0): 
            self.Profils.PrName='DefaultProfil'
            self.Profils.CreateProfil()
            self.Profils.LoadProfil(self.Profils.PrName)
            tmppr=self.Profils.PrName
        qq=0       
    #self.win.lblProfilName.setText(tmppr)
    
    #--- синхронизация с лицевой панелью
    # отображение профилей
    #self.SelectPr(self.actPrName, True)
    # вызовы сеттеров для синхронизации состояния кислородомера и лицевой панели
    '''self.fTempComp = self._fTempComp 
    self.fTempTech = self._fTempTech
    self.fPressComp = self._fPressComp 
    self.fPressTech = self._fPressTech'''   
    self.dSize=dSize


    self.LoadState()
 


    #self.CreateDictonary()
    self.EdIzm=0
    self.SredaIzm=0
    #self.win.Sens_2.setData(self.win.x_draw,self.win.y_draw)

  def CreateDictonary(self):
    #self.pStDict = {}
    #self.pStDict1 = {}
    fname='D:\ormet\source\svi_vs\par.txt'
    f= open(fname)
    n=0
    self.pStDict={}
    #name = safeDget(self.dictState, 'pH2ODict', '0')
    while n<=50 :
        ln = f.readline()
        #LL.I(ln)
        ln1=ln.rstrip()
        #LL.I(ln1)
        parts = ln1.split(' ')
        self.pStDict[(n,0)]=parts[0]
        self.pStDict[(n,1)]=parts[1]
        self.dictState['pStDict']=self.pStDict#
        # print<< self.pStDict
        # LL.I("Р".format(self.pStDict))
        #LL.I(parts[0])
        #LL.I(parts[1])
        n=n+1
    #LL.I(self.dictState['pStDict'])
    #self.pStDict1 = {}
    #self.pStDict1=self.dictState['pStDict']

    self.dictState.update
    sstate.saveVstate()

  def CreateDictonary1(self):
    self.pH2ODict = {}
    self.pH2ODict1 = {}
    fname='D:\ormet\source\svi_vs\o2.txt'
    f= open(fname)
    n=0
    while n<360 :
        ln = f.readline()
        #LL.I(ln)
        ln1=ln.rstrip()
        #LL.I(ln1)
        parts = ln1.split(' ')
        self.pH2ODict[(n,0)]=parts[0]
        self.pH2ODict[(n,1)]=parts[1]
        self.dictState['pH2ODict']=self.pH2ODict#'''
        # print<< self.pStDict
        # LL.I("Р".format(self.pStDict))
        LL.I(parts[0])
        LL.I(parts[1])
        n=n+1
    #LL.I(self.dictState['pStDict'])
    self.pH2ODict1 = {}
    self.pH2ODict1=self.dictState['pH2ODict']
    LL.I(self.pH2ODict1[(359,1)])
    self.dictState.update
    sstate.saveVstate()

  def CreateDictonary2(self,dstate_):
    self.pSaltDict = {}
    #dstate_['pSaltDict'] = {}
    fname='D:\ormet\source\svi_vs_last\salt.txt'
    f= open(fname)
    n=0
    while n<51 :
        ln = f.readline()
        #LL.I(ln)
        ln1=ln.rstrip()
        #LL.I(ln1)
        parts = ln1.split(' ')
        self.pSaltDict[(n,0)]=parts[0]
        self.pSaltDict[(n,1)]=parts[1]
        self.dictState['pSaltDict']=self.pSaltDict#'''
        # print<< self.pStDict
        # LL.I("Р".format(self.pStDict))
        #LL.I(parts[0])
        #LL.I(parts[1])
        LL.I(self.pSaltDict[(n,0)])
        LL.I(self.pSaltDict[(n,1)])
        n=n+1
    #self.dictState['pStDict']
    #LL.I(self.dictState['pSaltDict'])
    #LL.I(self.pSaltDict[(50,1)])
    self.dictState.update
    sstate.saveVstate()

  def Get_pSt(self,Temp):#Get_pH2O
    n=0
    if(Temp<0): Temp=0
    a=self.dictStateTable.get('pStDict')
    a1=float(a[(n,0)])
    a11=a1*10
    a2=int(a11)
    while  a2!=int(Temp*10):
        n=n+1
        a1=float(a[(n,0)])
        a11=a1*10
        a2=int(a11)
    Res=float(a[(n,1)]) 
    return Res 

  def Get_pH2O(self,Temp):#Get_pSt
    n=0
    if(Temp<0): Temp=0
    a=self.dictStateTable.get('pH2ODict')
    while float(a[(n,0)])!=int(Temp):
        n=n+1
    Res=float(a[(n,1)]) 
    return Res 


  def Get_P_O2(self,Temp,P):
    self.C_O2tabl=self.Get_pSt(Temp)
    self.p_O2_vozduh=(P/0.133-self.Get_pH2O(Temp)/0.133)*20.93/100
    return self.p_O2_vozduh
 
  def Get_K_salt(self,Temp):
    n=0
    a=self.dictStateTable.get('pSaltDict')
    while int(a[(n,0)])!=int(Temp):
        n=n+1
    Res=float(a[(n,1)]) 
    return Res 

  def Get_He(self,Temp,P):
    self.C_O2tabl=self.Get_pSt(Temp)
    He=self.C_O2tabl/self.Get_P_O2(Temp,P)
    return He 

  def Corr_Salt(self,A,cS,Temp):
    Res=A*(1-cS*self.Get_K_salt(Temp)/1000)
    return Res

  def Mark_mgdm3_percentNas(self,A, Temp):
    Res=A*100/self.Get_pSt(Temp) 
    return Res

  def Mark_mgdm3_percent(self,A, Temp, P):
    Res=A*101.325*20.95/(P*self.Get_pSt(Temp))
    return Res

  def Mark_mgdm3_vozduh(self,P, Temp):
    Res=P*self.Get_pSt(Temp)/101.325
    return Res

  def Corr_Hanna(self,Temp,A):
    self.A_ist_mm_kpa=A*(1+0.0275*(self.T_grad-Temp))
    return self.A_ist_mm_kpa
  def Corr_mm_kPa(self,Temp,A):
    self.A_ist_mm_kpa=A*(1+0.0275*(self.T_grad-Temp))
    #LL.I("A= {:7.4f}\t A_ist_mm_kpa=A*(1+0.0275*(T_grad-Temp)) = {:7.4f}".format(A, self.A_ist_mm_kpa))
    #LL.I("T_grad = {:7.4f}".format(self.T_grad)) 
    return self.A_ist_mm_kpa

  def Corr_mgdm3(self,Temp,P,A):
    #tmp1=self.Get_He(Temp)/self.Get_He(self.T_grad)
    self.A_ist_mgm3=A*(1+0.0275*(self.T_grad-Temp))*self.Get_He(Temp,P)/self.Get_He(self.T_grad,self.P_grad)
    #LL.I("A= {:7.4f}\t A_ist_mgm3=A*(1+0.0275*(T_grad-Temp))*Get_He(Temp)/Get_He(T_grad) = {:7.4f}".format(A, self.A_ist_mgm3))

    return self.A_ist_mgm3

  def Corr_membr(self,Temp,P,A):
    self.A_ist_membr=A*self.Get_He(Temp,P)/self.Get_He(self.T_grad,self.P_grad)
    #LL.I("A= {:7.4f}\t A_ist_membr=A*self.Get_He(Temp)/Get_He(T_grad) = {:7.4f}".format(A, self.A_ist_membr))
    return self.A_ist_membr

  def Percent_nas_vvode(self,Temp, P, A):
    Per_nas=A*100/(self.Get_pSt(Temp)*P/101.3)
    return Per_nas

  def Percent_nas_vvozduhe(self,Temp, P, A):
    Per_nas=A*101.3/100
    return Per_nas

  def LoadState(self):
    super().LoadState()


  def SaveState(self):
    # генерация словаря инициализационных контейнеров
    super().SaveState()


  def NewData(self, ddata):

    
   if((self.ParamMess=='0')or(self.ParamMess=='2')): 
    if self.measT in ddata:
      self.lastT = ddata[self.measT][1]
      self.timeT = ddata[self.measT][2] 
      #print(self.timeT)
 
      fNewTemp = True
    else:  
      fNewTemp = False
    if self.measP in ddata:
      if(self.ParamMess=='0'): self.lastP = ddata[self.measP][1]
      if(self.ParamMess=='2'): self.lastP = 101.33
    if self.measI in ddata:

      self.CalcP_02(ddata[self.measI][1], self.lastT, self.lastP)
   if (self.vCE.Close_Config_Flag==1)and(self.closeFlag==0): 
          self.closeFlag=1   
          self.timer.stop()     
          self.win.close()
          self. delete()
          a=0


  def Calibr_Max(self):
      self.T_grad=self.T_curr
      self.P_grad=self.P_curr
      self.A_2=self.Get_pSt(self.T_grad)*self.P_grad/101.33
      self.I_2=self.A_izm
      self.S=(self.A_2-self.A_1)/(self.I_2-self.I_1)
      self.A_0=self.S*self.I_1-self.A_1
      self.Sp=(self.Ap_2-self.Ap_1)/(self.I_2-self.I_1)
      self.Ap_0=self.Sp*self.I_1-self.Ap_1
      # сохраняем состояние вирт. прибора (т.е. вместе с обновленным профилем) в файл
      self.Profils.T_grad=self.T_grad
      self.Profils.P_grad=self.P_grad
      self.Profils.A_2=self.A_2
      self.Profils.I_2=self.I_2
      self.Profils.S=self.S
      self.Profils.A_0=self.A_0
      self.Profils.Sp=self.Sp
      self.Profils.Ap_0=self.Ap_0
      self.Profils.SaveCurrProfil()
 

  def Calibr_Min(self):

      self.T_grad=self.T_curr
      self.P_grad=self.P_curr
      self.A_1=0
      self.I_1=self.A_izm
      self.S=(self.A_2-self.A_1)/(self.I_2-self.I_1)
      self.A_0=self.S*self.I_1-self.A_1

      self.Sp=(self.Ap_2-self.Ap_1)/(self.I_2-self.I_1)
      self.Ap_0=self.Sp*self.I_1-self.Ap_1    
      # сохраняем состояние вирт. прибора (т.е. вместе с обновленным профилем) в файл
      self.Profils.T_grad=self.T_grad
      self.Profils.P_grad=self.P_grad
      self.Profils.A_1=self.A_1
      self.Profils.I_1=self.I_1
      self.Profils.S=self.S
      self.Profils.A_0=self.A_0
      self.Profils.Sp=self.Sp
      self.Profils.Ap_0=self.Ap_0
      self.Profils.SaveCurrProfil()

 

  def NewDataTimer(self):
    
   if(self.ParamMess=='1'): 
    
      self.lastT = 25
      self.lastP =100
      self.lastI =8
      try:
       self.lastI=float(Results.Result_Dict[self.InputUnit[0]][self.InputVal[0]])
      except: self.lastI=0.0
      try:
       self.lastT=float(Results.Result_Dict[self.InputUnit[1]][self.InputVal[1]])
      except: self.lastT=0.0
      try:
       self.lastP=float(Results.Result_Dict[self.InputUnit[2]][self.InputVal[2]])
      except: self.lastP=0.0
      
      self.CalcP_02(self.lastI, self.lastT, self.lastP)
    
      self.DispTemp(self.lastT)
      if (self.vCE.Close_Config_Flag==1)and(self.closeFlag==0): 
          self.closeFlag=1      
          self.win.close()


    
      
  def DispTemp(self, temp):
    #temp=12.1234
    #press=123.1234
    """ обновить значение температуры temp на лицевой панели """
    #if not self._fTempTech:  self.win.leTemp.setText("{:3.1f}".format(temp))
    self.win.leTemp.setText("{:3.1f}".format(temp))
  def DispPress(self, press):
    """ обновить значение температуры temp на лицевой панели """
    #if not self._fPressTech:  self.win.lePressure.setText("{:3.0f}".format(press))
    self.win.lePressure.setText("{:3.1f}".format(press))


  def Calc_Ormet(self,A,P):
    ''' метод возвращает % насыщения'''

    Percent_nas=A*100/(GetP_st(T)*P/101.3)

    return Percent_nas 
  def Calc_percent_pH2O_to_mgdm3(self,A_percent_pH2O):
    ''' метод возвращает '''
    '''self.P_O2_percent=self.P_O2_mgdm3*100*0.133/(P*(self.Get_He(T)))'''
    Res=A_percent_pH2O*self.Get_He(self.T_grad,self.P_grad)*(self.P_grad/0.133-self.Get_pH2O(self.T_grad))/100.0

    return Res

  def Calc_percent_to_mgdm3(self,A_percent):
    ''' метод возвращает '''
    '''self.P_O2_percent=self.P_O2_mgdm3*100*0.133/(P*(self.Get_He(T)))'''
    Res=A_percent*self.P_grad*(self.Get_He(self.T_grad,self.P_grad))/(100*0.133)

    return Res 

  def Calc_kPa_to_mgdm3(self,A_kPa):
    ''' метод возвращает'''
    '''self.P_O2_kPa=0.133*self.P_O2_mgdm3/self.Get_He(T)'''
    Res=A_kPa*self.Get_He(self.T_grad,self.P_grad)/0.133
    return Res 

  def Calc_mmrtst_to_mgdm3(self,A_mmrtst):
    ''' метод возвращает '''
    '''self.P_O2_mmrtst=self.P_O2_mgdm3/self.Get_He(T)'''
    Res=A_mmrtst/self.Get_He(self.T_grad,self.P_grad)

    return Res

  def CalcP_02(self, Im , Tm, Pm):
    """ расчет pO2 в зависимости от режима и вывод на лицевую панель 
        Um - актуальное напряжение [B] от измерителя - милливольтметра
        Tm - актуальная температура [град Цельсия] от измерителя - термометра  
        Pm - актуальное давление [кПа] от измерителя - манометра"""

    self.A_izm=Im
    ################################################################
    if (self.OffT_Flag==1): 
      self.T_curr= 25.0 # при отключенной термокоррекции расчет идет на температуре калибровки 
      self.DispTemp(self.T_curr)
    if (self.ManualT_Flag==1): 
      q=0
            
    if (self.AutoT_Flag==1):                   
      self.T_curr=self.lastT          # расчет на основе температуры от измерителя 
      if((self.T_curr<0.0)|(self.T_curr>35.9)):self.T_curr= 25.0 
      self.DispTemp(self.T_curr)  
      #self.workT = T  
       
    if (self.OffP_Flag==1): 
      self.P_curr= 101.31
      self.DispPress(self.P_curr)
    if (self.ManualP_Flag==1): 
      q=0
            
    if (self.AutoP_Flag==1):                   
      self.P_curr=self.lastP          # расчет на основе температуры от измерителя  
      self.DispPress(self.P_curr)  

    Xp = Im*self.S-self.A_0 
    self.P_O2_per = Im*self.Sp-self.Ap_0 
   
    self.P_O2_mgdm3=Xp;
    self.Calc_O2(self.T_curr, self.P_curr)


  def Calc_O2(self, T, P):
    if self.Sensor==0:
     self.P_O2_per_=self.Corr_mm_kPa(T,self.P_O2_per)
     self.P_O2_mgdm3_=self.Corr_mgdm3(T,P,self.P_O2_mgdm3) 
    elif self.Sensor==1:
     self.P_O2_per_=self.Corr_membr(T,P,self.P_O2_per)
     self.P_O2_mgdm3_=self.Corr_membr(T,P,self.P_O2_mgdm3)
    elif self.Sensor>=3:
     self.P_O2_per_=self.Corr_mm_kPa(T,self.P_O2_per) 
     self.P_O2_mgdm3_=self.Corr_mgdm3(T,P,self.P_O2_mgdm3) 
    if (self.Salt>0):
     self.P_O2_per_=self.Corr_Salt(self.P_O2_per,self.Salt,T)
     self.P_O2_mgdm3_=self.Corr_Salt(self.P_O2_mgdm3,self.Salt,T)

    if self._fDlog:  print(" P_O2_mgdm3_corr = {:4.3f} \t  T = {:5.2f} \t P = {:6.3f}".format(self.P_O2_mgdm3_, T, P))
    #self.P_O2_mgdm3_=12.123456
    #self.P_O2_per_=123.123456
    self.win.lcdMain.display(self.formS.format(self.P_O2_mgdm3_))
    self.win.lcdMain_2.display(self.formSp.format(self.P_O2_per_))

    Results.Result_Dict[self.Name][self.OutputVal[0]]=self.P_O2_mgdm3_
    Results.Result_Dict[self.Name][self.OutputVal[1]]=self.P_O2_per_
    Results.Result_Dict[self.Name][self.OutputVal[2]]=self.techT
    Results.Result_Dict[self.Name][self.OutputVal[3]]=self.techP
    Results.Result_Dict[self.Name]['Параметр '+self.OutputVal[0]]='Концентрация(мг)'
    Results.Result_Dict[self.Name]['Единица '+self.OutputVal[0]]=self.C_ed_0
    Results.Result_Dict[self.Name]['Параметр '+self.OutputVal[1]]='Концентрация(%)'
    Results.Result_Dict[self.Name]['Единица '+self.OutputVal[1]]=self.C_ed_1
    if(Results.Result_Dict[self.Name]['В блокнот']!=2):Results.Result_Dict[self.Name]['В блокнот']=self.InLight_Notepad
    Results.Result_Dict[self.Name]['ID_VP']=self.ID_VP
    Results.Result_Dict[self.Name]['LastProfil']=self.LastProfil
    if(Results.Result_Dict[self.Name]['В блокнот']==2):
        Results.Result_Dict[self.Name]['В блокнот']=0
        self.InLight_Notepad=0
    self.win.lblEd.setText(self.C_ed_0)
    self.win.lblEd_2.setText(self.C_ed_1)

#---



class CfpO_2(QtGui.QMainWindow, Ui_fpO_2):
  """ лицевая панель виртуального кислородомера """
  #  winCO_2  - экземпляр CfmO_2Calib - окно настройки кислородомера
  #  vO_2   - экземпляр виртуального кислородомера, соответствующий данной панели #A4EBFD


  def __init__(self, vO_2):
    super().__init__() 
    self.setupUi(self)
    #################################### 
    # Если версия для ПК
    if PCFlag==1:
      #self.leSalt = QtGui.QLineEdit(self.centralwidget)
      self.leSalt = QLineEdit_1(self.centralwidget)
      self.leSalt.setGeometry(QtCore.QRect(140, 390, 84, 31))
      sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
      sizePolicy.setHorizontalStretch(0)
      sizePolicy.setVerticalStretch(0)
      sizePolicy.setHeightForWidth(self.leSalt.sizePolicy().hasHeightForWidth())
      self.leSalt.setSizePolicy(sizePolicy)
      self.leSalt.setMinimumSize(QtCore.QSize(81, 31))
      font = QtGui.QFont()
      font.setFamily(_fromUtf8("Verdana"))
      font.setPointSize(12)
      self.leSalt.setFont(font)
      self.leSalt.setFrame(True)
      self.leSalt.setReadOnly(True)
      self.leSalt.setObjectName(_fromUtf8("leSalt"))
    #####################################
    self.setStyleSheet("QMainWindow {background: '#A4EBFD';}")
    self.leSalt.setReadOnly(0)
    self.leSalt.setText('0')
    self.TypeMess=0;
    self.vO_2 = vO_2
    rect = QtCore.QRect()   
    w=self.vO_2.width 
    h=self.vO_2.height
    x=self.vO_2.x         
    y=self.vO_2.y  
    rect = QtCore.QRect(x,y,w,h) 
    rect.setRect(x,y,w,h) 
    self.setGeometry(rect)

    self.fFreeze = False
    #self.lcdMain.setDigitCount(self.vO_2.widthD + 1)
    #self.lcdMain_2.setDigitCount(self.vO_2.widthD + 1)
    self.lcdMain.setDigitCount(5)
    self.lcdMain_2.setDigitCount(4)

    self.vO_2.ID_VP=self.vO_2.dSize.setdefault('ID_VP','0')
    self.lblID.setText(str(self.vO_2.ID_VP))
    # self.leID.clearFocus()     
    
    self.Type=5

    self.edIndex=1;
    if self.vO_2.fTech:   
      # виртуальный прибор запущен в технологическом режиме 
      self.actTech = QtGui.QAction("Отладка", self) 
      self.actTech.triggered.connect(self.on_muTech_toggle)  
      self.menubar.addAction(self.actTech)

    self.actTech = QtGui.QAction("Калибровка ''100%''", self) 
    self.actTech.triggered.connect(self.on_Calibr_Max_toggle)  
    self.menubar.addAction(self.actTech)

    self.actTech = QtGui.QAction("Калибровка ''0%''", self) 
    self.actTech.triggered.connect(self.on_Calibr_Min_toggle)  
    self.menubar.addAction(self.actTech)

    # Common menu of VP
    self.actTech = QtGui.QAction("Проба", self) 
    self.actTech.triggered.connect(self.on_Proba_toggle)  
    self.menubar.addAction(self.actTech)

    self.actTech = QtGui.QAction("О приборе", self) 
    self.actTech.triggered.connect(self.on_AboutVP_toggle)  
    self.menubar.addAction(self.actTech)
    ## End of common menu of VP

    #self.leTemp.editingFinished.connect(self.on_leTempFinish)
    #self.lePressure.editingFinished.connect(self.on_leTempFinish)
    #self.leSalt.editingFinished.connect(self.on_leSaltFinish)
    #self.leSalt.returnPressed.connect(self.on_leSalttextChanged)
    ##self.leSalt.installEventFilter(self)
    self.connect(self.leSalt, SIGNAL("editingFinished()"),self.on_leSaltFinish)
    self.connect(self.leSalt, SIGNAL("dcEmitApp()"),self.on_leSaltFinish1)
    self.connect(self.leSalt, SIGNAL("dcEmitApp1()"),self.on_leSaltFinish2)
    #self.connect(slider, QtCore.SIGNAL('valueChanged(int)'), lcd, QtCore.SLOT('display(int)'))

    ##self.leSalt.mouseDoubleClickEvent(self)

    self.rbManualT.toggled.connect(self.on_ManualT_toggle)
    self.rbOffT.toggled.connect(self.on_OffT_toggle)
    self.rbAutoT.toggled.connect(self.on_AutoT_toggle)
    self.tbEnterT.clicked.connect(self.on_tbEnterT_clicked) 
    self.rbAutoT.setChecked(True)

    self.rbManualP.toggled.connect(self.on_ManualP_toggle)
    self.rbOffP.toggled.connect(self.on_OffP_toggle)
    self.rbAutoP.toggled.connect(self.on_AutoP_toggle)
    self.tbEnterP.clicked.connect(self.on_tbEnterP_clicked) 
    self.rbAutoP.setChecked(True)

  
    self.tbSaveToNotepad.clicked.connect(self.on_tbSaveToNotepad_clicked) 
    #self.rbManualP.toggled.connect(self.on_ManualP_toggle)
    #self.rbOffP.toggled.connect(self.on_OffP_toggle)
    #self.rbAutoP.toggled.connect(self.on_AutoP_toggle)
    #self.tbEnterP.clicked.connect(self.on_tbEnterP_clicked) 
    #self.rbAutoP.setChecked(True)
    #self.tbSaveToNotepad_.clicked.connect(self.on_tbSaveToNotepad_clicked) 

    #self.tbSelectProfil.clicked.connect(self.on_tbSelectProfil_toggle)
    #self.tbSelectProfil.setVisible(False)
    #self.lblProfilName.setVisible(False)
    #self.label_31.setVisible(False)
    self.Reset_Flag=1

    self.trAutoScan =None
    self.trAutoScan = self.startTimer(1000)

  '''def eventFilter(self, obj, event):
        # you could be doing different groups of actions
        # for different types of widgets and either filtering
        # the event or not.
        # Here we just check if its one of the layout widgets
        if self.layout.indexOf(obj) != -1:
            if event.type() == event.MouseButtonPress:
                q=0'''
  #def event(self,e):
      #if(e.type==self.leSalt.mouseDoubleClickEvent):
       #q=0
  def mousePressEvent(self, event):
        q=0

  def mouseDoubleClickEvent(self, event):
        q=0

  def focusInEvent(self, event):
        q=0 


  def timerEvent(self, e):
  #Отображение даты по таймеру
        a=datetime.today()
        a1=a.date()
        a2=a.time()
        dt1=str(a1)+"  \t"+a2.strftime("%H:%M:%S") 
        #self.lblDateTime.setText(str(dt1))
        q=0
        if (self.vO_2.vCE.Close_Config_Flag==1)and(self.vO_2.closeFlag==0): 
          self.vO_2.closeFlag=1      
          self.close()


  def on_tbSaveToNotepad_clicked(self):
      #Запись в блокнот
      if(Results.Result_Dict[self.vO_2.Name]['В блокнот']==0):
        self.vO_2.ID_VP=self.lblID.text()
        self.vO_2.dSize['ID_VP']=self.vO_2.ID_VP
        self.vO_2.InLight_Notepad=1
      q=0 


  def show(self, newsize = None):
    """ newsize - экземпляр QSize для передачи новых размеров окна """
    super().show()   # важно выполнить ПЕРЕД resize - иначе resize может не пройти

    if newsize:  self.resize(newsize)

  def on_Proba_toggle(self):
      self.vO_2.winProbaID.show()
      w=0

  def on_AboutVP_toggle(self):
      self.vO_2.winAboutVP.show()
      w=0    


  def closeEvent(self, event):
    #Закрытие формы кислородомера
    self.vO_2.SaveState()
    self.vO_2.ProfilsDict['Кислородомер'][self.vO_2.Name]['Текущий профмль']=self.vO_2.Profils.PrName
    self.vO_2.vCE.save_LocalProfil_state()
    rect = self.geometry()
    self.vO_2.dSize['x'] = rect.left()
    self.vO_2.dSize['y'] = rect.top()
    self.vO_2.dSize['height'] = rect.height() 
    self.vO_2.dSize['width'] = rect.width()
    event.accept() 

  def on_tbSelectProfil_toggle(self):
      #Нажатие кнопки выбора профиля
      self.vO_2.winSelectProfil.show()
      w=0

  def on_muConf_toggle(self):
    #self.winCO_2.show(self.vO_2.profD, self.vO_2.actPr, self.vO_2)
    smartShow(self.winCO_2, self.vO_2.profD, self.vO_2.actPr, self.vO_2)

  def on_leSalttextChanged(self):
     self.vO_2.vCE.winDigitalKeyboard.show()

  def on_muTech_toggle(self):
    self.vO_2.fDlog = not self.vO_2.fDlog


  def on_TComp_toggle(self):
    self.vO_2.fTempComp = not self.vO_2.fTempComp


  def on_AutoT_toggle(self): 
    self.vO_2.fTempTech = not self.vO_2.fTempTech

  def on_leTempFinish(self):
    try:
      self.vO_2.techT = eval(self.leTemp.text(), {}, {})
    except:
      LL.exception('') 
    self.leTemp.setText("{:5.2f}".format(self.vO_2.techT))
    self.leTemp.clearFocus()

  def on_ManualT_toggle(self):
    #Установка температуры вручную
    if(self.vO_2.ManualT_Flag==0):
       self.vO_2.ManualT_Flag=1
       self.vO_2.OffT_Flag=0
       self.vO_2.AutoT_Flag=0
       self.leTemp.setReadOnly(False) 

       q=1

    #self.vCond.fTempComp = not self.vCond.fTempComp
    q=0

  def on_OffT_toggle(self):
    #Установка температуры по умолчанию
    if(self.vO_2.OffT_Flag==0):
       self.vO_2.OffT_Flag=1
       self.vO_2.ManualT_Flag=0
       self.vO_2.AutoT_Flag=0
       self.leTemp.setReadOnly(True) 

       q=1

    q=0

  def on_AutoT_toggle(self):
    #Установка температуры автоматически
    if(self.vO_2.AutoT_Flag==0):
       self.vO_2.AutoT_Flag=1
       self.vO_2.ManualT_Flag=0
       self.vO_2.OffT_Flag=0
       self.leTemp.setReadOnly(True) 

       q=1 
    #self.vCond.fTempTech = not self.vCond.fTempTech
    q=0

  def on_tbEnterT_clicked(self):
    #Ввод значения температуры вручную
    if(self.vO_2.ManualT_Flag==1):       
       self.vO_2.T_curr= eval(self.leTemp.text(), {}, {})
       if((self.vO_2.T_curr<0.0)|(self.vO_2.T_curr>35.9)):self.vO_2.T_curr= 25.0 
       self.vO_2.DispTemp(self.vO_2.T_curr)
    q=0

  def on_ManualP_toggle(self):
    #Установка давления вручную
    if(self.vO_2.ManualP_Flag==0):
       self.vO_2.ManualP_Flag=1
       self.vO_2.OffP_Flag=0
       self.vO_2.AutoP_Flag=0
       self.lePressure.setReadOnly(False) 

  def on_OffP_toggle(self):
    #Установка давления по умолчанию
    if(self.vO_2.OffP_Flag==0):
       self.vO_2.OffP_Flag=1
       self.vO_2.ManualP_Flag=0
       self.vO_2.AutoP_Flag=0
       self.lePressure.setReadOnly(True) 
    q=0

  def on_AutoP_toggle(self):
    #Установка давления автоматически
    if(self.vO_2.AutoP_Flag==0):
       self.vO_2.AutoP_Flag=1
       self.vO_2.ManualP_Flag=0
       self.vO_2.OffP_Flag=0
       self.lePressure.setReadOnly(True) 
    q=0

  def on_tbEnterP_clicked(self):
    #Ввод значения давления вручную
    if(self.vO_2.ManualP_Flag==1):       
       self.vO_2.P_curr= eval(self.lePressure.text(), {}, {})
       self.vO_2.DispPress(self.vO_2.P_curr)
    q=0


  def on_leSaltFinish(self):
    #Ввод значения соли вручную
    try:
      self.vO_2.Salt = eval(self.leSalt.text(), {}, {})
    except:
      LL.exception('') 
    self.leSalt.setText("{:5.2f}".format(self.vO_2.Salt))
    self.leSalt.clearFocus()

  def on_leSaltFinish1(self):
    #Ввод значения соли вручную
    self.vO_2.vCE.winDigitalKeyboard.show()
    self.vO_2.vCE.winKeyboard.show()
    if(self.vO_2.vCE.DigData!=''):
        self.leSalt.setText(self.vO_2.vCE.DigData)
        self.leSalt.clearFocus()
        self.vO_2.vCE.winDigitalKeyboard.on_tb_()
        self.vO_2.vCE.winDigitalKeyboard.close()

  def on_leSaltFinish2(self):
    #Ввод значения соли вручную
    self.leSalt.setText(self.vO_2.vCE.DigData)
    self.vO_2.vCE.winDigitalKeyboard.on_tb_()
    self.vO_2.vCE.winDigitalKeyboard.close()

  def on_Calibr_Max_toggle(self):
      #Калибровка по максимуму
      self.vO_2.Calibr_Max()

  def on_Calibr_Min_toggle(self):
      #Калибровка по минимуму
      self.vO_2.Calibr_Min()


class CfmO_2Calib(QtGui.QMainWindow, Ui_fmO_2Calib): 
  """ окно калибровки виртуального кислородомера """


  def __init__(self, vCond):
     
    super().__init__()
    self.setupUi(self)
    self.vCond = vCond
    self.ShowFlag=0
    '''
    self.cbEd.addItem('кПа')
    self.cbEd.addItem('мм.рт.ст.')
    self.cbEd.addItem('%')
    self.cbEd.addItem('%_pH20')
    self.cbEd.setCurrentIndex(0);
    '''
    #self.cbSensor.addItem('ACpO2-00')
    self.cbSensor.addItem('ACpO2-01')
    self.cbSensor.addItem('ACpO2-02')
    self.cbSensor.addItem('Hana')
    self.cbSensor.addItem('Другой')
    self.cbSensor.setCurrentIndex(0);
    #self.cbSreda.addItem('Жидкость')
    #self.cbSreda.addItem('Газ')
    #self.cbSreda.setCurrentIndex(0);
    #self.cbTypeMess.addItem('Кислородомер')
    #self.cbTypeMess.addItem('БПК')
    #self.cbTypeMess.setCurrentIndex(0);
    self.formpX = "{:5.2f}" 
    self.formE = "{:6.1f}"
    self.hint = QtCore.Qt.UserRole + 1 
    self.fFreeze = False
    self.lastPrInd = -1
    self.lastPrName = '' 
    self.stPrEd = 0
    self.fNewPr = False
    ###self.leElec.setHidden(True)  # строка редактирования наименования профиля
    self.A=1
    self.A_mgdm3=1
    self.Ed_A=0

    self.leA_1.editingFinished.connect(self.on_leA_1Finish)
    self.leA_2.editingFinished.connect(self.on_leA_2Finish)
    self.leA_0.editingFinished.connect(self.on_leA_0Finish)
    self.leI_1.editingFinished.connect(self.on_leI_1Finish)
    self.leI_2.editingFinished.connect(self.on_leI_2Finish)
    self.leS.editingFinished.connect(self.on_leSFinish)
    self.leT_grad.editingFinished.connect(self.on_leT_gradFinish)
    self.leP_grad.editingFinished.connect(self.on_leP_gradFinish)
    #self.leA.editingFinished.connect(self.on_leAFinish)
    #self.leA_mgdm3.editingFinished.connect(self.on_leA_mgdm3Finish)

    self.tbCalib.clicked.connect(self.on_tbCalib_toggle)
    #self.cbEd.currentIndexChanged.connect(self.on_cbEd_changed)
    ###self.cbSreda.currentIndexChanged.connect(self.on_cbSreda_changed)
   ## self.cbTypeMess.currentIndexChanged.connect(self.on_cbTypeMess_changed)
    self.cbSensor.currentIndexChanged.connect(self.on_cbSensor_changed)
    #self.tbEd.clicked.connect(self.on_tbEd_toggle)
    self.tbSaveProfilO2.clicked.connect(self.on_tbSaveProfilO2_toggle)
    ###self.actTIns.triggered.connect(self.on_actTIns_toggle)
    ###self.actTDel.triggered.connect(self.on_actTDel_toggle)    

    ###self.cbElec.currentIndexChanged.connect(self.on_cbElec_changed)
    
    ###self.leElec.editingFinished.connect(self.on_leElecFinish)
    ###self.tbElecAdd.clicked.connect(self.on_actPrIns_toggle) 

    
  def on_Change_Any(self):
      if(self.ShowFlag==1):
        A_1=0.0
        A_2=0.0
        A_0=0.0
        I_1=0.0
        I_2=0.0
        T_grad=0.0
        P_grad=0.0
        A=0.0
        A_mgdm3=0.0
        S=0.0
        SensorID=0.0

        A_1=eval(self.leA_1.text(), {}, {})
        A_2=eval(self.leA_2.text(), {}, {})
        A_0=eval(self.leA_0.text(), {}, {})
        I_1=eval(self.leI_1.text(), {}, {})
        I_2=eval(self.leI_2.text(), {}, {})
        T_grad=eval(self.leT_grad.text(), {}, {})
        P_grad=eval(self.leP_grad.text(), {}, {})
        #A=eval(self.leA.text(), {}, {})
        #A_mgdm3=eval(self.leA_mgdm3.text(), {}, {})
        S=eval(self.leS.text(), {}, {})
        SensorID=self.cbSensor.currentIndex()
        PrName=self.leProfilName_.text()
        PrDescr=self.leDescr_.text()
        self.vCond.Profils.ChangeCurrProfil(A_1, A_2, A_0, I_1, I_2, T_grad, P_grad, A, A_mgdm3, S, SensorID, PrName, PrDescr)



  def on_tbSaveProfilO2_toggle(self):
        if(self.ShowFlag==1):
          self.on_Change_Any()
          self.vCond.Profils.SaveCurrProfil()
          self.vCond.winSelectProfil.InitProfilsList()
        q=0

  def Calibration(self):
        A_1=eval(self.leA_1.text(), {}, {})
        A_2=eval(self.leA_2.text(), {}, {})
        A_0=eval(self.leA_0.text(), {}, {})
        I_1=eval(self.leI_1.text(), {}, {})
        I_2=eval(self.leI_2.text(), {}, {})
        T_grad=eval(self.leT_grad.text(), {}, {})
        P_grad=eval(self.leP_grad.text(), {}, {})

        A_2=self.vCond.Get_pSt(T_grad)*P_grad/101.33
        S=(A_2-A_1)/(I_2-I_1)
        A_0=S*I_1-A_1
        Ap_1=0
        Ap_2=100
        Sp=(Ap_2-Ap_1)/(I_2-I_1)
        Ap_0=Sp*I_1-Ap_1
        # сохраняем состояние вирт. прибора (т.е. вместе с обновленным профилем) в файл
        self.vCond.Profils.T_grad=T_grad
        self.vCond.Profils.P_grad=P_grad
        self.vCond.Profils.A_2=A_2
        self.vCond.Profils.I_2=I_2
        self.vCond.Profils.S=S
        self.vCond.Profils.A_0=A_0
        self.vCond.Profils.Sp=Sp
        self.vCond.Profils.Ap_0=Ap_0
        self.vCond.Profils.SaveCurrProfil()

  def on_Init_Any(self):
      self.leA_1.setText(str(self.vCond.Profils.A_1))
      self.leA_2.setText(str(self.vCond.Profils.A_2))
      self.leA_0.setText(str(self.vCond.Profils.A_0))
      self.leI_1.setText(str(self.vCond.Profils.I_1))
      self.leI_2.setText(str(self.vCond.Profils.I_2))
      self.leT_grad.setText(str(self.vCond.Profils.T_grad))
      self.leP_grad.setText(str(self.vCond.Profils.P_grad))
      #self.leA.setText(str(self.vCond.Profils.A))
      #self.leA_mgdm3.setText(str(self.vCond.Profils.A_mgdm3))
      self.leS.setText(str(self.vCond.Profils.S))
      self.cbSensor.setCurrentIndex(int(self.vCond.Profils.SensorID))

      try:
       a=self.vCond.Profils.PrName
      except:
          a=''
      self.leProfilName_.setText(a)
      try:
       b=self.vCond.Profils.PrDescr
      except:
          b=''
      self.leDescr_.setText(b)
      self.leA_1.setFocus()
        
  def show(self, profD, actPr, vO_2): 
    self.on_Init_Any()
    self.ShowFlag=1
    super().show()

  def closeEvent(self, event):
    self.ShowFlag=0

  def on_leA_1Finish(self):
    q=0


  def on_leA_2Finish(self):
    q=0

  def on_leA_0Finish(self):
    q=0


  def on_leI_1Finish(self):
    q=0

  def on_leI_2Finish(self):
    q=0

  def on_leSFinish(self):
    q=0

  def on_leT_gradFinish(self):
    q=0


  def on_leP_gradFinish(self):
    q=0

  def on_leAFinish(self):
    q=0

  def on_leA_mgdm3Finish(self):
    q=0

  def on_leT_1_Finish(self):
    q=0

  def on_leT_2_Finish(self):
    q=0

  def on_leA_T_1_Finish(self):
    q=0

  def on_leA_T_2_Finish(self):
    q=0

  def on_tbEd_toggle(self):
    """ расчет калибровочных коэффициентов """
    if self.Ed_A==0:
        self.A_mgdm3=self.A
    if self.Ed_A==1:
        self.A_mgdm3=self.vCond.Calc_kPa_to_mgdm3(self.A)
    if self.Ed_A==2:
        self.A_mgdm3=self.vCond.Calc_mmrtst_to_mgdm3(self.A)
    if self.Ed_A==3:
        self.A_mgdm3=self.vCond.Calc_percent_to_mgdm3(self.A)
    if self.Ed_A==4:
        self.A_mgdm3=self.vCond.Calc_percent_pH2O_to_mgdm3(self.A)

    self.leA_mgdm3.setText(self.formpX.format(self.A_mgdm3))
    self.leA_mgdm3.clearFocus()

  def on_cbEd_changed(self, ind):
    self.Ed_A=ind 

  def on_cbSreda_changed(self, ind):
    self.Ed_A=self.Ed_A 

  def on_cbTypeMess_changed(self, ind):
    self.Ed_A=self.Ed_A 

  def on_cbSensor_changed(self, ind):
    q=0

  def on_tbCalib_toggle(self):
    """ расчет калибровочных коэффициентов """
    self.Calibration()
    self.leS.setText(self.formpX.format(self.vCond.Profils.S))
    self.leS.clearFocus()
    self.leA_0.setText(self.formpX.format(self.vCond.Profils.A_0))
    self.leA_0.clearFocus()


#----------------------------------------------

class CfmSelectProfil_O2(QtGui.QMainWindow, Ui_fmSelectProfil_O2): 
  """ окно выбора профиля виртуального кондуктомера (характеризация электродов) """
  #    PrD - словарь доступных профилей (key: наименование; value: экземпляр CO_2Prof)
  #    actPr  - активный редактируемый профиль (КОПИЯ экземпляра CO_2Prof из словаря PrD) 
  #             (устанавливается в PrD ПОСЛЕ завершения расчетов)
  #    fNewPr - True - редактируемый профиль НОВЫЙ (т.е. не нужно удалять старый из словаря как при редактировании)
  #    vCond   - виртуальный кондуктомер, к которому подключена калибруемая электродная пара
  #    pXcol  - список содержщий колонку pX (ключи в pXdict редактируемого профиля)
  #    formpX - строка форматирования под pX (под НОВЫЙ метод format)
  #    formE  - строка форматирования под напряжение (под НОВЫЙ метод format)
  #    menuT  - контекстное меню калибровочной таблицы
  #    menuC  - контекстное меню выпадающего списка профилей
  #    hint   - ролевой код доп. данных в элементе-заголовке строки калибровочной таблицы
  #    fFreeze - True - отключить обработку событий калибровочной таблицы и выпадающего списка профилей
  #    lastPrName - наименование ПРЕДЫДУЩЕГО редактируемого профиля
  #    lastPrInd  - индекс в выпадающем списке ПРЕДЫДУЩЕГО редактируемого профиля
  #    stPrEd - состояние редактирования профиля:
  #              0 - отсутствуют какие-либо операции с наименованием профиля
  #              1 - редактируется наименование активного профиля
  #              2 - создается наименование нового профиля    
  #             данным состояниям соответствуют команды автомату редактирования профилей + дополнительные:
  #             10 - расчет активного профиля завершен   
  #             20 - удалить активный профиль  
  #             30 - выбор нового активного профиля из словаря

  def __init__(self, vCond):
     
    super().__init__()
    self.vCond = vCond
    self.setupUi(self)
 
    self.formpX = "{:5.2f}"
    self.tbAddProfil.clicked.connect(self.on_tbAddProfil_toggle)
    self.tbSelectProfil.clicked.connect(self.on_tbSelectProfil_toggle) 
    self.tbChangeProfil.clicked.connect(self.on_tbChangeProfil) 
    self.tbDelProfil.clicked.connect(self.on_tbDelProfil)   
    self.lwProfils_.currentItemChanged.connect(self.on_lwProfils_Change)
    self.lwProfils_.doubleClicked.connect(self.on_lwProfils_doubleClicked)
    self.lwProfils_.clicked.connect(self.on_lwProfils_clicked)
    self.InitProfilsList()

  def showEvent(self, event):
    self.InitProfilsList()

  def on_tbAddProfil_toggle(self):
     self.vCond.Profils.CurrentProf=-1
     self.vCond.winCO_2.show(0,0,0)
     return 0

  def InitProfilsList(self):
     tmpCnt=self.vCond.Profils.Listcount
     tmpNum=0
     self.lwProfils_.clear()#lwProfils
     while (tmpNum<tmpCnt):
         self.lwProfils_.addItem(self.vCond.Profils.vCE.ProfilsDict['Кислородомер']['List'][tmpNum])
         #a=str(self.vCond.Profils.profs['List'][tmpNum])
         #self.listWidget1.addItem(a)
         tmpNum=tmpNum+1
     #self.listWidget1.clear()
     #self.listWidget1.addItem('qq')

     return 0

  def on_tbSelectProfil_toggle(self):
     i=0
     a=self.lwProfils_.currentRow()
     #i=self.lwProfils_.takeItem(a)
     self.vCond.Profils.SelectProfil(a)
     #self.vCond.win.lblProfilName.setText(self.vCond.Profils.PrName)
     self.close()
     return 0

  def on_tbChangeProfil(self):
     i=0
     a=self.lwProfils_.currentRow()
     #i=self.lwProfils_.takeItem(a)
     self.vCond.Profils.SelectProfil(a)
     self.vCond.winCO_2.show(0,0,0)
     return 0
 
  def on_tbDelProfil(self):
     i=0
     a=self.lwProfils_.currentRow()
     #i=self.lwProfils_.takeItem(a)
     self.vCond.Profils.DelProfil(a)
     self.InitProfilsList()
     return 0
   
  def on_lwProfils_Change(self):
     i=0
     a=self.lwProfils_.currentRow()
     #i=self.lwProfils_.takeItem(a)
     self.vCond.Profils.SelectedProfilNum=a

     #strtxt=self.vCond.Profils.GetInfoProfil(i) 
     #self.tbDescribeProfil.setText(strtxt )        
     return 0

  def on_lwProfils_doubleClicked(self):
     self.vCond.winCO_2.show(0,0,0)
     return 0

  def on_lwProfils_clicked(self):
     a=self.lwProfils_.currentRow()
     self.vCond.Profils.SelectProfil(a)
     tmptxt=self.vCond.Profils.PrDescr
     self.tbDescribeProfil.setText(tmptxt)
     return 0

class CProfilsC():

    def __init__(self, vCE, profils={}):
       b=0
       self.profs=profils
       self.vCE=vCE
       self.vCE.ProfilsDict['Кислородомер'].setdefault('Listcount',0)
       self.vCE.ProfilsDict['Кислородомер'].setdefault('List',{})
       #self.vCE.ProfilsDict['Кондуктомер']['Listcount']=4
       self.Listcount=self.vCE.ProfilsDict['Кислородомер']['Listcount']
       self.CurrentProf=-1
       self.A_1=1.0
       self.A_2=1.0
       self.A_0=1.0
       self.I_1=1.0
       self.I_2=1.0
       self.T_grad=1.0
       self.P_grad=1.0
       self.A=1.0
       self.A_mgdm3=1.0
       self.S=1.0
       self.SensorID=0
       self.PrName=''
       self.PrDescr=''
       self.Sp=0
       self.Ap_0=0
       self.SelectedProfilNum=-1


    def LoadProfilsList(self):
       tmpi=0
       tmpl=[]
       while tmpi<self.Listcount-1:
           tmpl.append(self.vCE.ProfilsDict['Кислородомер']['List'][tmpi])
       return tmpl
 
    def LoadProfil(self,prName=''):

        #########################################
        tmpname=self.PrName
        tmpNum=0
        tmpi=0
        if(self.Listcount==0):
           self.A_1=1.0
           self.A_2=1.0
           self.A_0=1.0
           self.I_1=1.0
           self.I_2=1.0
           self.T_grad=1.0
           self.P_grad=1.0
           self.A=1.0
           self.A_mgdm3=1.0
           self.S=1.0
           self.SensorID=0
           self.PrDescr=''
           self.PrName='(нет)'
           self.vCE.PrName=self.PrName    
           self.vCE.A_1=self.A_1
           self.vCE.A_2=self.A_2
           self.vCE.A_0=self.A_0
           self.vCE.I_1=self.I_1
           self.vCE.I_2=self.I_2
           self.vCE.T_grad=self.T_grad
           self.vCE.P_grad=self.P_grad
           self.vCE.A=self.A
           self.vCE.A_mgdm3=self.A_mgdm3
           self.vCE.S=self.S
           self.vCE.SensorID=self.SensorID
        tmpi=0
        if(self.Listcount>0):
           while (tmpi<self.Listcount): 
             if (self.vCE.ProfilsDict['Кислородомер']['List'][tmpi]==prName):
                 self.SelectProfil(tmpi)
                 self.PrName=prName
                 tmpi=self.Listcount
             tmpi=tmpi+1
           
        #########################################

        return 0


    def CreateProfil(self):
       tmpname=self.PrName
       tmpNum=0
       tmpi=0
       if(self.Listcount==0): tmpnameNum=tmpname
       while (tmpi<self.Listcount):
          if(tmpNum>0):tmpnameNum=tmpname+str(tmpNum) 
          else: tmpnameNum=tmpname 
          if (self.vCE.ProfilsDict['Кислородомер']['List'][tmpi]==tmpnameNum):
              tmpNum=tmpNum+1
              tmpi=0
          tmpi=tmpi+1
       self.PrName=tmpnameNum
       #self.profs['List'].setdefault(str(tmpnameNum),{})
       self.vCE.ProfilsDict['Кислородомер']['List'][self.Listcount]=str(self.PrName)
       self.Listcount=self.Listcount+1
       self.vCE.ProfilsDict['Кислородомер']['Listcount']=self.Listcount
       self.vCE.ProfilsDict['Кислородомер'][self.PrName]={}
       self.vCE.ProfilsDict['Кислородомер'][self.PrName]['A_1']=self.A_1
       self.vCE.ProfilsDict['Кислородомер'][self.PrName]['A_2']=self.A_2
       self.vCE.ProfilsDict['Кислородомер'][self.PrName]['A_0']=self.A_0
       self.vCE.ProfilsDict['Кислородомер'][self.PrName]['I_1']=self.I_1
       self.vCE.ProfilsDict['Кислородомер'][self.PrName]['I_2']=self.I_2
       self.vCE.ProfilsDict['Кислородомер'][self.PrName]['T_grad']=self.T_grad
       self.vCE.ProfilsDict['Кислородомер'][self.PrName]['P_grad']=self.P_grad
       self.vCE.ProfilsDict['Кислородомер'][self.PrName]['A']=self.A
       self.vCE.ProfilsDict['Кислородомер'][self.PrName]['A_mgdm3']=self.A_mgdm3
       self.vCE.ProfilsDict['Кислородомер'][self.PrName]['S']=self.S
       self.vCE.ProfilsDict['Кислородомер'][self.PrName]['SensorID']=self.SensorID
       self.vCE.ProfilsDict['Кислородомер'][self.PrName]['PrDescr']=self.PrDescr
       self.vCE.ProfilsDict['Кислородомер'][self.PrName]['Sp']=self.Sp
       self.vCE.ProfilsDict['Кислородомер'][self.PrName]['Ap_0']=self.Ap_0
       

    def DelProfil(self, index):
       tmpi=0
       tmpname=self.vCE.ProfilsDict['Кислородомер']['List'][index]
       del self.vCE.ProfilsDict['Кислородомер'][tmpname]
       tmpi=index
       while (tmpi<=self.Listcount-2):
          self.vCE.ProfilsDict['Кислородомер']['List'][tmpi]=self.vCE.ProfilsDict['Кислородомер']['List'][tmpi+1]
          tmpi=tmpi+1
       #while (tmpi<self.Listcount-1):#
       del self.vCE.ProfilsDict['Кислородомер']['List'][self.Listcount-1]
       self.Listcount=self.Listcount-1
       self.vCE.ProfilsDict['Кислородомер']['Listcount']=self.Listcount


       #self.profSM_(20,'prname___')#self.profSM(20, self.cbElec.currentText())

    def ChangeProfil(self, index=-1):
       self.CurrentProf=index
       if(self.CurrentProf!=-1):
         self.Listcount=self.vCE.ProfilsDict['Кислородомер']['Listcount']
         if(self.vCE.ProfilsDict['Кислородомер']['List'][self.CurrentProf]!=self.PrName):
           self.vCE.ProfilsDict['Кислородомер']['List'][self.CurrentProf]={}
           del self.vCE.ProfilsDict['Кислородомер'][self.PrName]  
         else:
           self.vCE.ProfilsDict['Кислородомер'][self.PrName]['A_1']=self.A_1
           self.vCE.ProfilsDict['Кислородомер'][self.PrName]['A_2']=self.A_2
           self.vCE.ProfilsDict['Кислородомер'][self.PrName]['A_0']=self.A_0
           self.vCE.ProfilsDict['Кислородомер'][self.PrName]['I_1']=self.I_1
           self.vCE.ProfilsDict['Кислородомер'][self.PrName]['I_2']=self.I_2
           self.vCE.ProfilsDict['Кислородомер'][self.PrName]['T_grad']=self.T_grad
           self.vCE.ProfilsDict['Кислородомер'][self.PrName]['P_grad']=self.P_grad
           self.vCE.ProfilsDict['Кислородомер'][self.PrName]['A']=self.A
           self.vCE.ProfilsDict['Кислородомер'][self.PrName]['A_mgdm3']=self.A_mgdm3
           self.vCE.ProfilsDict['Кислородомер'][self.PrName]['S']=self.S
           self.vCE.ProfilsDict['Кислородомер'][self.PrName]['SensorID']=self.SensorID
           self.vCE.ProfilsDict['Кислородомер'][self.PrName]['PrDescr']=self.PrDescr
           self.vCE.ProfilsDict['Кислородомер'][self.PrName]['Sp']=self.Sp
           self.vCE.ProfilsDict['Кислородомер'][self.PrName]['Ap_0']=self.Ap_0

    def SelectProfil(self, index):
       self.CurrentProf=index
       self.Listcount=self.vCE.ProfilsDict['Кислородомер']['Listcount']
       tmpa=self.vCE.ProfilsDict['Кислородомер']['List'][self.CurrentProf]
       self.PrName=tmpa
       self.A_1=self.vCE.ProfilsDict['Кислородомер'][self.PrName]['A_1']
       self.A_2=self.vCE.ProfilsDict['Кислородомер'][self.PrName]['A_2']
       self.A_0=self.vCE.ProfilsDict['Кислородомер'][self.PrName]['A_0']
       self.I_1=self.vCE.ProfilsDict['Кислородомер'][self.PrName]['I_1']
       self.I_2=self.vCE.ProfilsDict['Кислородомер'][self.PrName]['I_2']
       self.T_grad=self.vCE.ProfilsDict['Кислородомер'][self.PrName]['T_grad']
       self.P_grad=self.vCE.ProfilsDict['Кислородомер'][self.PrName]['P_grad']
       self.A=self.vCE.ProfilsDict['Кислородомер'][self.PrName]['A']
       self.A_mgdm3=self.vCE.ProfilsDict['Кислородомер'][self.PrName]['A_mgdm3']
       self.S=self.vCE.ProfilsDict['Кислородомер'][self.PrName]['S']
       self.SensorID=self.vCE.ProfilsDict['Кислородомер'][self.PrName]['SensorID']

       self.PrDescr=self.vCE.ProfilsDict['Кислородомер'][self.PrName]['PrDescr']
       self.Sp=self.vCE.ProfilsDict['Кислородомер'][self.PrName]['Sp']
       self.Ap_0=self.vCE.ProfilsDict['Кислородомер'][self.PrName]['Ap_0']
       q=0
       self.vCE._PrName=self.PrName    
       self.vCE.A_1=self.A_1
       self.vCE.A_2=self.A_2
       self.vCE.A_0=self.A_0
       self.vCE.I_1=self.I_1
       self.vCE.I_2=self.I_2
       self.vCE.T_grad=self.T_grad
       self.vCE.P_grad=self.P_grad
       self.vCE.A=self.A
       self.vCE.Ap_0=self.Ap_0
       self.vCE.A_mgdm3=self.A_mgdm3
       self.vCE.S=self.S
       self.vCE.Sp=self.Sp
       self.vCE.SensorID=self.SensorID

    def GetInfoProfil(self, index):
       self.CurrentProf=index

    def ChangeCurrProfil(self,A_1=1.0, A_2=1.0, A_0=1.0, I_1=1.0, I_2=1.0, T_grad=1.0, P_grad=1.0, A=1.0, A_mgdm3=1.0, S=1.0, SensorID=0, PrName='Pr1', PrDescr=' ' ):

       self.A_1=A_1
       self.A_2=A_2
       self.A_0=A_0
       self.I_1=I_1
       self.I_2=I_2
       self.T_grad=T_grad
       self.P_grad=P_grad
       self.A=A
       self.A_mgdm3=A_mgdm3
       self.S=S
       self.SensorID=SensorID
       self.PrName=PrName
       self.PrDescr=PrDescr

       self.S=(self.A_2-self.A_1)/(self.I_2-self.I_1)
       self.A_0=self.S*self.I_1-self.A_1
       self.Ap_1=0 #
       self.Ap_2=100 #
       self.Sp=(self.Ap_2-self.Ap_1)/(self.I_2-self.I_1)
       self.Ap_0=self.Sp*self.I_1-self.Ap_1

    def SaveCurrProfil(self):
        if (self.CurrentProf==-1):
            self.CreateProfil()
        else:
            self.ChangeProfil(self.CurrentProf)
        self.vCE.vCE.save_LocalProfil_state()
