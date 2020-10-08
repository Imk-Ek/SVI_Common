import logging
import copy 
from vp_classes import *
from PyQt4 import QtCore, QtGui 
from datetime import datetime
from common import *
from vp_classes import *
from fmIonEdit import Ui_fmIonEdit
from fpIon_2 import Ui_fpIon
from fmICalib import Ui_fmICalib
from fmSelectProfil_Ion import Ui_fmSelectProfil_Ion

from fmIonDigitSelect import Ui_fmIonDigitSelect
from fmIonMessage import Ui_fmIonMessage
from fmIonMessageOK import Ui_fmIonMessageOK
from fmIonMessSelect import Ui_fmIonMessSelect
from fmIonSelect import Ui_fmIonSelect
from fmIonProfilNameOK import Ui_fmIonProfilNameOK
from fmOtherSettingV import Ui_fmOtherSettingV
from vinstr import *
#LL = logging.getLogger('SVI')

class CIon(CVInstr):
  """ виртуальный иономер """
  #  measN - наименование измерительного канала напряжения, связанного с данным экземпляром иономера
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

  #  внешние свойства:
  #    fTempTech - True  - режим ручного ввода температуры (_fTempTech - private копия)
  #                False - автоматическое сканирование измерителя температуры                  
  #    fTempComp - True  - режим термокоррекции включен (_fTempComp - private копия)
  #    fDlog     - True - технологическое логирование в консоль

  def __init__(self,vCE, dcfg, dstate = {}, dSize={}, LocalProfilsDict={},  fTech = False):
    super().__init__(dcfg, dstate, fTech)
    self.vCE=vCE
    self.Name=dcfg['наименование']
    self.ProfilsDict=LocalProfilsDict
    self.ProfilsDict.setdefault('Иономер',{})
    self.ProfilsDict['Иономер'].setdefault(self.Name,{})
    self.LastProfil=self.ProfilsDict['Иономер'][self.Name].setdefault('Текущий профмль','')
    #  
    self.measN = self.dictCfg["каналНапряжение"]
    self.measT = self.dictCfg["каналТемпература"]
    self.dictCfg["meas"] = [self.measN, self.measT] # фактически вносится в vinstrD
    self.closeFlag=0  
    self.CurrProfil=''
    self.LastProfil=''
    self.Name=dcfg['наименование']
    self.ProfilsDict=LocalProfilsDict
    self.ProfilsDict.setdefault('Иономер',{})
    self.ProfilsDict['Иономер'].setdefault(self.Name,{})
    self.LastProfil=self.ProfilsDict['Иономер'][self.Name].setdefault('Текущий профмль','')
    self.InLight_Notepad=0
    self.ID_VP='0'
    self.CreateIonFlag=0
    self.CountFilter_2=1
    self.CurrCountFilter_2=1
    self.U_Sum_Filter_2=0
    self.U_Filter_2=0
    self.ID=0

    self.pX =0

    '''self.IonDict={}
    self.IonDict[0]={}
    self.IonDict[0][0]='H'
    self.IonDict[0][1]=1
    self.IonDict[0][2]=1.00794
    self.IonDict[0][3]=1.0
    self.IonDict[0][4]=1


    self.IonDict[1]={}
    self.IonDict[1][0]='Li'
    self.IonDict[1][1]=-1
    self.IonDict[1][2]=6.941
    self.IonDict[1][3]=1.0
    self.IonDict[1][4]=1


    self.IonDict[2]={}
    self.IonDict[2][0]='F'
    self.IonDict[2][1]=1
    self.IonDict[2][2]=18.9984
    self.IonDict[2][3]=1.0
    self.IonDict[2][4]=1

    self.IonDict[3]={}
    self.IonDict[3][0]='NH4'
    self.IonDict[3][1]=-1
    self.IonDict[3][2]=18.0385
    self.IonDict[3][3]=1.0
    self.IonDict[3][4]=1


    self.IonDict[4]={}
    self.IonDict[4][0]='Na'
    self.IonDict[4][1]=1
    self.IonDict[4][2]=22.989768
    self.IonDict[4][3]=1.0
    self.IonDict[4][4]=1

    self.IonDict[5]={}
    self.IonDict[5][0]='CN'
    self.IonDict[5][1]=2
    self.IonDict[5][2]=26.01774
    self.IonDict[5][3]=1.0
    self.IonDict[5][4]=1

    self.IonDict[6]={}
    self.IonDict[6][0]='S'
    self.IonDict[6][1]=-2
    self.IonDict[6][2]=32.066
    self.IonDict[6][3]=1.0
    self.IonDict[6][4]=1

    self.IonDict[7]={}
    self.IonDict[7][0]='Cl'
    self.IonDict[7][1]=-1
    self.IonDict[7][2]=35.4527
    self.IonDict[7][3]=1.0
    self.IonDict[7][4]=1

    self.IonDict[8]={}
    self.IonDict[8][0]='K'
    self.IonDict[8][1]=1
    self.IonDict[8][2]=39.0989
    self.IonDict[8][3]=1.0
    self.IonDict[8][4]=1

    self.IonDict[9]={}
    self.IonDict[9][0]='Ca'
    self.IonDict[9][1]=2
    self.IonDict[9][2]=40.078
    self.IonDict[9][3]=1.0
    self.IonDict[9][4]=1

   
    self.IonDict[10]={}
    self.IonDict[10][0]='SCN'
    self.IonDict[10][1]=-1
    self.IonDict[10][2]=58.0874
    self.IonDict[10][3]=1.0
    self.IonDict[10][4]=1

    self.IonDict[11]={}
    self.IonDict[11][0]='NO3'
    self.IonDict[11][1]=-1
    self.IonDict[11][2]=62.00494
    self.IonDict[11][3]=1.0
    self.IonDict[11][4]=1

    self.IonDict[12]={}
    self.IonDict[12][0]='Cu'
    self.IonDict[12][1]=2
    self.IonDict[12][2]=63.545
    self.IonDict[12][3]=1.0
    self.IonDict[12][4]=1

    self.IonDict[13]={}
    self.IonDict[13][0]='Br'
    self.IonDict[13][1]=-1
    self.IonDict[13][2]=79.904
    self.IonDict[13][3]=1.0
    self.IonDict[13][4]=1

    self.IonDict[14]={}
    self.IonDict[14][0]='ClO4'
    self.IonDict[14][1]=-1
    self.IonDict[14][2]=99.4503
    self.IonDict[14][3]=1.0
    self.IonDict[14][4]=1

 
    self.IonDict[15]={}
    self.IonDict[15][0]='Ag'
    self.IonDict[15][1]=1
    self.IonDict[15][2]=107.8682
    self.IonDict[15][3]=1.0
    self.IonDict[15][4]=1

    self.IonDict[16]={}
    self.IonDict[16][0]='Cd'
    self.IonDict[16][1]=2
    self.IonDict[16][2]=112.411
    self.IonDict[16][3]=1.0
    self.IonDict[16][4]=1

    self.IonDict[17]={}
    self.IonDict[17][0]='I'
    self.IonDict[17][1]=-1
    self.IonDict[17][2]=126.90447
    self.IonDict[17][3]=1.0
    self.IonDict[17][4]=1

    self.IonDict[18]={}
    self.IonDict[18][0]='Ba'
    self.IonDict[18][1]=1
    self.IonDict[18][2]=137.327
    self.IonDict[18][3]=1.0
    self.IonDict[18][4]=1

    self.IonDict[19]={}
    self.IonDict[19][0]='Hg'
    self.IonDict[19][1]=2
    self.IonDict[19][2]=200.58
    self.IonDict[19][3]=1.0
    self.IonDict[19][4]=1

    
    self.IonDict[20]={}
    self.IonDict[20][0]='Pb'
    self.IonDict[20][1]=2
    self.IonDict[20][2]=207.2
    self.IonDict[20][3]=1.0
    self.IonDict[20][4]=1

    self.IonDict[21]={}
    self.IonDict[21][0]='X'
    self.IonDict[21][1]=-1
    self.IonDict[21][2]=1.0
    self.IonDict[21][3]=1.0
    self.IonDict[21][4]=1

    self.IonDict[22]={}
    self.IonDict[22][0]='X'
    self.IonDict[22][1]=-2
    self.IonDict[22][2]=1.0
    self.IonDict[22][3]=1.0
    self.IonDict[22][4]=1

    self.IonDict[23]={}
    self.IonDict[23][0]='X'
    self.IonDict[23][1]=1
    self.IonDict[23][2]=1.0
    self.IonDict[23][3]=1.0
    self.IonDict[23][4]=1

    self.IonDict[24]={}
    self.IonDict[24][0]='X'
    self.IonDict[24][1]=2
    self.IonDict[24][2]=1.0
    self.IonDict[24][3]=1.0
    self.IonDict[24][4]=1

    self.ProfilsDict['Иономер']['Ions_Table']=self.IonDict
    self.ProfilsDict['Иономер']['Ions_Table_Const_Count']=25
    self.ProfilsDict['Иономер']['Ions_Table_All_Count']=25
    self.ProfilsDict['Иономер']['Ions_Table_All_Count']=self.ProfilsDict['Иономер']['Ions_Table_All_Count']-1    
    self.vCE.save_LocalProfil_state()'''

    self.IonDict=self.ProfilsDict['Иономер']['Ions_Table']
    self.widthD = 3
    self.precD = 3
    self.formS = "{:"+str(self.widthD)+"."+str(self.precD)+"f}" 

    self.widthD_2 = 5 # 4
    self.precD_2 = 2  # 3
    self.formS_2 = "{:"+str(self.widthD_2)+"."+str(self.precD_2)+"f}"
    self.profD = {}
    self.ManualT_Flag=0
    self.OffT_Flag=0
    self.AutoT_Flag=0
    self.T_curr=0
    self.lastT=0
    self.U_izm=0.00
    self.ReqFlag=1

    self.Ecm=0.0
    self.Stc=0.054153
    self.Kt=1.9836e-4
    self.pXu=7.0
    self.Tcb=20.0
    self.S_min=57.0
    self.Ion_Name=''
    self.Ion_Val=1
    self.Ion_K=1.0
    self.Ion_Mol_Massa=1.0

    self.PrDescr=''
    self.PrName='(???µ??)'
    self.ParamMess=dSize['VPParam']
    self.InputUnit=[0,0,0,0]
    self.InputVal=[0,0,0,0]
    self.OutputVal=[0,0,0,0]
    self.OutputParam=[0,0,0,0]
    self.OutputEdIzm=[0,0,0,0]
    self.InputUnit[0]=dSize['VPChModulNameList'][0]
    self.InputUnit[1]=dSize['VPChModulNameList'][1]
    #self.InputUnit[2]=dSize['VPChModulNameList'][2]
    self.InputVal[0]=dSize['VPChNameList'][0]
    self.InputVal[1]=dSize['VPChNameList'][1]
    #self.InputVal[2]=dSize['VPChNameList'][2]
    self.OutputVal[0]=dSize['VPChOutTypeList'][0]
    self.OutputVal[1]=dSize['VPChOutTypeList'][1]
    self.OutputVal[2]=dSize['VPChOutTypeList'][2]
    self.Ion_ed='pH'
    Results.Result_Dict[self.Name]={}
    Results.Result_Dict[self.Name][self.OutputVal[0]]=0
    Results.Result_Dict[self.Name][self.OutputVal[1]]=0
    Results.Result_Dict[self.Name][self.OutputVal[2]]=0
    self.dSize=dSize

    self.width=self.dSize.setdefault('width',100)
    self.height=self.dSize.setdefault('height',100)
    self.x=self.dSize.setdefault('x',100)
    self.y=self.dSize.setdefault('y',100) 
    self.Ions=CIonC(self)
    self.IonGrad=CIonGrad(self)
    self.Profils=CProfilsC(self,self.ProfilsDict)

    self.winProbaID =CfmProbaID(self)
    self.winAboutVP =CfmAboutVP(self)
    self.winMessage =CfmMessage(self)
    self.win = CfpIon(self)
    self.winSelectProfil = CfmSelectProfil_Ion(self)
    self.winIon = CfmICalib(self)

    self.winProbaID =CfmProbaID(self)
    self.winAboutVP =CfmAboutVP(self)
    self.winMessage =CfmMessage(self)

    self.C_index=0
    self.C_0=0.0
    self.C_1=0.0
    self.C_2=0.0
    self.C__=0.0
    self.winIonEdit  = CfmIonEdit(self)
    self.winIonDigitSelect  = CfmIonDigitSelect(self)
    self.winIonMessage  = CfmIonMessage(self)
    self.winIonMessageOK  = CfmIonMessageOK(self)
    self.winIonMessSelect  = CfmIonMessSelect(self)
    self.winIonSelect  = CfmIonSelect(self)
    self.fmIonProfilNameOK = CfmIonProfilNameOK(self)
    self.winOtherSettingV = CfmOtherSettingV(self)
    
    tmppr=''
    self.LastProfil=self.ProfilsDict['Иономер'][self.Name]['Текущий профмль']
    tmppr=self.LastProfil
    try:
      self.Profils.LoadProfil(self.LastProfil)
      self._PrName=self.LastProfil
      self.win.lblEd.setText('p'+self.Profils.Ion_Name)
      self.win.lblConcentr.setText('Содержание '+self.Profils.Ion_Name)
    except: 
        tmppr='не выбран'         
    self.win.lblProfilName.setText(tmppr)

    self.LoadState()
    Results.Result_Dict[self.Name]['В блокнот']=0
    self.timerM = QtCore.QTimer()
    self.timerM.timeout.connect(self.NewDataTimerM)
    self.timerM.start(100)
    q=0


    
  def LoadState(self):
    super().LoadState()

  def SaveState(self):
    super().SaveState()



  def NewData(self, ddata):
   if(self.ReqFlag==1): 
    self.ReqFlag=0
    if self.measT in ddata:
      self.lastT = ddata[self.measT][1]
      self.timeT = ddata[self.measT][2]   
      fNewTemp = True
    else:  
      fNewTemp = False
    if self.measN in ddata:
      # расчет pX идет только при наличии данных от милливольтметра

      self.U_izm=ddata[self.measN][1]
      ###############################################################################################################
      if(self.CurrCountFilter_2<=self.CountFilter_2):
           self.U_Sum_Filter_2=self.U_Sum_Filter_2+self.U_izm
           self.CurrCountFilter_2=self.CurrCountFilter_2+1
      if(self.CurrCountFilter_2>=self.CountFilter_2):
           self.U_Filter_2=self.U_Sum_Filter_2/self.CurrCountFilter_2
           self.U_Sum_Filter_2=0
           self.CurrCountFilter_2=0
      ###############################################################################################################
    self.ReqFlag=1
    if (self.vCE.Close_Config_Flag==1)and(self.closeFlag==0): 
          self.closeFlag=1
          self.timerM.stop()        
          self.win.close()
          self. delete()
          a=0

  def Calc(self, U, T):
    """ метод возвращает pX(U,T) где U [B], T [град Цельсия] """ 
    pX = self.pXu + (self.Ecm - U)/(self.Stc + (self.Kt * T))
    return pX 

  def DispTemp(self, temp):
    #temp=12.1234
    """ обновить значение температуры temp на лицевой панели """
    self.win.leTemp.setText("{:2.1f}".format(temp))
    q=0

  def NewDataTimerM(self):
    self.CalcDpX(self.U_Filter_2, self.lastT)
    a=datetime.today()
    a1=a.date()
    a2=a.time()
    dt1=str(a1)+"  \t"+a2.strftime("%H:%M:%S") 
    #self.win.lblDateTime.setText(str(dt1))
    if (self.vCE.Close_Config_Flag==1)and(self.closeFlag==0): 
          self.closeFlag=1      
          self.win.close()
          self.timerM.stop()
          self. delete()

          a=0



  def CalcDpX(self, Um , Tm):
    """ расчет pX в зависимости от режима и вывод на лицевую панель 
    Um - актуальное напряжение [B] от измерителя - милливольтметра
    Tm - актуальная температура [град Цельсия] от измерителя - термометра  """

    if (self.OffT_Flag==1): 
     self.T_curr= 25.0 # при отключенной термокоррекции расчет идет на температуре калибровки 
     self.DispTemp(self.T_curr) 

    if (self.ManualT_Flag==1): 
      q=0
            
    if (self.AutoT_Flag==1):                   
      self.T_curr=self.lastT          # расчет на основе температуры от измерителя
      if((self.T_curr<-200.0)|(self.T_curr>200.0)):self.T_curr= 25.0 
      self.DispTemp(self.T_curr)  
    try:
      self.pX = self.pXu + (self.Ecm - Um)/(self.Stc + (self.Kt * self.T_curr))
    except: q=0
    #if self._fDlog:  print("E = {} \t T = {:5.2f} \t pX = {:6.3f}".format(Um, self.T_curr, pX))
    self.U_m=Um*1000.0
    self.C_0=(10.0**(-self.pX))*self.Ion_K
    self.C_2=(10.0**(-self.pX))*self.Ion_K*self.Ion_Mol_Massa
    self.C_3=self.C_2*1000.0
    self.C_1=self.C_0/math.fabs(self.Ion_Val)
    #self.pX=-12.1234567
    self.win.lcdMain.display(self.formS.format(self.pX))
    #self.U_m=1.1234567
    self.win.lcdMain_2.display(self.formS_2.format(self.U_m))
    if(self.C_index==0):
        self.C__=self.C_0
        self.Ion_ed2='моль/л'
        q=0
    if(self.C_index==1):
        self.C__=self.C_1
        self.Ion_ed2='моль экв./л'
        q=0
    if(self.C_index==2):
        self.C__=self.C_2
        self.Ion_ed2='г/л'
        q=0
    if(self.C_index==3):
        self.C__=self.C_3
        self.Ion_ed2='мг/л'
        q=0
    self.win.lcdMain_3.display(self.formS.format(self.C__))
    self.Ion_ed1='мВ'

    Results.Result_Dict[self.Name][self.OutputVal[0]]=self.pX
    Results.Result_Dict[self.Name]['Параметр '+self.OutputVal[0]]='Ph'
    Results.Result_Dict[self.Name]['Единица '+self.OutputVal[0]]=self.Ion_ed

    Results.Result_Dict[self.Name][self.OutputVal[1]]=self.U_m
    Results.Result_Dict[self.Name]['Параметр '+self.OutputVal[1]]='Um'
    Results.Result_Dict[self.Name]['Единица '+self.OutputVal[1]]=self.Ion_ed1

    Results.Result_Dict[self.Name][self.OutputVal[2]]=self.C__
    Results.Result_Dict[self.Name]['Параметр '+self.OutputVal[2]]='(C)'
    Results.Result_Dict[self.Name]['Единица '+self.OutputVal[2]]=self.Ion_ed2
    if(Results.Result_Dict[self.Name]['В блокнот']!=2):Results.Result_Dict[self.Name]['В блокнот']=self.InLight_Notepad
    Results.Result_Dict[self.Name]['ID_VP']=self.ID_VP
    Results.Result_Dict[self.Name]['LastProfil']=self.LastProfil
    if(Results.Result_Dict[self.Name]['В блокнот']==2):
        Results.Result_Dict[self.Name]['В блокнот']=0
        self.InLight_Notepad=0
    #self.win.lblEd.setText(self.Ion_ed)
    self.win.lblEd_2.setText(self.Ion_ed1)

class CfmOtherSettingV(QtGui.QMainWindow, Ui_fmOtherSettingV):
  """ лицевая панель виртуального вольтметра  
        vVolt  - экземпляр виртуального вольтметра, соответствующий данной панели
        basePS - (pointSize, height) базовая связка для масштабирования наименования физ-величины (llData)  
  """
      
  def __init__(self, vOs):
    """ numDigits - суммарное кол-во выводимых знаков результата (C учетом запятой) """
    super(CfmOtherSettingV, self).__init__() 
    self.setupUi(self)
    self.vOs = vOs
    self.tbSaveSettingV.clicked.connect(self.on_tbSaveSettingV_toggle)
#---
  def on_tbSaveSettingV_toggle(self):
    try:
      self.vOs.CountFilter_2 = eval(self.leCounts.text(), {}, {})
    except:
     q=0
    qq=0
#---

class CfpIon(QtGui.QMainWindow, Ui_fpIon):
  """ лицевая панель виртуального иономера """
  #  winCI  - экземпляр CfmICalib - окно настройки иономера
  #  vIon   - экземпляр виртуального иономера, соответствующий данной панели
  #  fFreeze - True - отключить обработку событий выпадающего списка профилей

  def __init__(self, vIon):

    super().__init__() 
    self.setupUi(self)
    self.setStyleSheet("QMainWindow {background: '#97F657';}")
    self.vIon = vIon
    rect = QtCore.QRect()   
    w=self.vIon.width 
    h=self.vIon.height
    x=self.vIon.x         
    y=self.vIon.y  
    rect = QtCore.QRect(x,y,w,h) 
    rect.setRect(x,y,w,h) 
    self.setGeometry(rect)    
    self.fFreeze = False
    #self.lcdMain.setDigitCount(self.vIon.widthD + 2)
    self.lcdMain.setDigitCount(6)
    self.lcdMain_2.setDigitCount(5)
    self.lcdMain_3.setDigitCount(5)

    self.cbEd_3.clear()
    self.cbEd_3.addItem('моль/л')
    self.cbEd_3.addItem('моль экв./л')
    self.cbEd_3.addItem('г/л')
    self.cbEd_3.addItem('мг/л')
    self.cbEd_3.setCurrentIndex(0)
    self.vIon.ID_VP=self.vIon.dSize.setdefault('ID_VP','0')
    self.lblID.setText(str(self.vIon.ID_VP))
    #self.leID.clearFocus()
    #self.actTech = QtGui.QAction("Настройка", self) 
    #self.actTech.triggered.connect(self.on_Setting)  
    #self.menubar.addAction(self.actTech)
    if self.vIon.fTech:   
      # виртуальный прибор запущен в технологическом режиме 
      self.actTech = QtGui.QAction("Отладка", self) 
      self.actTech.triggered.connect(self.on_muTech_toggle)  
      self.menubar.addAction(self.actTech)
    self.rbManualT.toggled.connect(self.on_ManualT_toggle)
    self.rbOffT.toggled.connect(self.on_OffT_toggle)
    self.rbAutoT.toggled.connect(self.on_AutoT_toggle)
    self.tbEnterT.clicked.connect(self.on_tbEnterT_clicked) 
    self.tbSaveToNotepad_.clicked.connect(self.on_tbSaveToNotepad_clicked) 
    self.rbAutoT.setChecked(True)    #self.tbTComp.clicked.connect(self.on_TComp_toggle)
    self.Type=4
    #self.tbSelectProfil.clicked.connect(self.on_tbSelectProfil_toggle)
    self.cbEd_3.currentIndexChanged.connect(self.on_currentIndexChanged)
    self.Reset_Flag=1

    # Menu Profile
    self.actTech = QtGui.QAction("Профиль", self) 
    self.actTech.triggered.connect(self.on_tbSelectProfil_toggle)  
    self.menubar.addAction(self.actTech)

    # Common menu of VP
    self.actTech = QtGui.QAction("Проба", self) 
    self.actTech.triggered.connect(self.on_Proba_toggle)  
    self.menubar.addAction(self.actTech)

    self.actTech = QtGui.QAction("О приборе", self) 
    self.actTech.triggered.connect(self.on_AboutVP_toggle)  
    self.menubar.addAction(self.actTech)
    ## End of common menu of VP

  def on_tbSaveToNotepad_clicked(self):
      if(Results.Result_Dict[self.vIon.Name]['В блокнот']==0):
        self.vIon.ID_VP=self.lblID.text() #self.ID_VP
        self.vIon.dSize['ID_VP']=self.vIon.ID_VP
        self.vIon.InLight_Notepad=1
      q=0 

  def on_Setting(self):
   self.vIon.winOtherSettingV.show()
   q=0
    
  def on_currentIndexChanged(self,index):
      self.vIon.C_index=index
      q=0

  def show(self, newsize = None):
    """ newsize - экземпляр QSize для передачи новых размеров окна """
    super().show()   # важно выполнить ПЕРЕД resize - иначе resize может не пройти
    if newsize:  self.resize(newsize)

  def on_Proba_toggle(self):
      self.vIon.winProbaID.show()
      w=0

  def on_AboutVP_toggle(self):
      self.vIon.winAboutVP.show()
      w=0 

  def closeEvent(self, event):
    self.vIon.SaveState()
    self.vIon.ProfilsDict['Иономер'][self.vIon.Name]['Текущий профмль']=self.vIon.Profils.PrName
    self.vIon.vCE.save_LocalProfil_state()
    rect = self.geometry()
    self.vIon.dSize['x'] = rect.left()
    self.vIon.dSize['y'] = rect.top()
    self.vIon.dSize['height'] = rect.height() 
    self.vIon.dSize['width'] = rect.width()
    event.accept() 


  def on_tbSelectProfil_toggle(self):
    if(self.vIon.vCE.OpenProfilVP_1Flag==0)&(self.vIon.vCE.OpenProfilVP_2Flag==0):
        self.vIon.vCE.OpenProfilVP_1Flag=1
        self.vIon.winSelectProfil.show()
        w=0

  def on_muConf_toggle(self):
    smartShow(self.winCI, self.vIon.profD, self.vIon.actPr, self.vIon)

  def on_muTech_toggle(self):
    self.vIon.fDlog = not self.vIon.fDlog

  def on_ManualT_toggle(self):
    if(self.vIon.ManualT_Flag==0):
       self.vIon.ManualT_Flag=1
       self.vIon.OffT_Flag=0
       self.vIon.AutoT_Flag=0
       self.leTemp.setReadOnly(False) 
       q=1
    q=0

  def on_OffT_toggle(self):
    if(self.vIon.OffT_Flag==0):
       self.vIon.OffT_Flag=1
       self.vIon.ManualT_Flag=0
       self.vIon.AutoT_Flag=0
       self.leTemp.setReadOnly(True) 
       q=1
    q=0

  def on_AutoT_toggle(self):
    if(self.vIon.AutoT_Flag==0):
       self.vIon.AutoT_Flag=1
       self.vIon.ManualT_Flag=0
       self.vIon.OffT_Flag=0
       self.leTemp.setReadOnly(True) 
       q=1 
    q=0

  def on_tbEnterT_clicked(self):
    if(self.vIon.ManualT_Flag==1):       
       self.vIon.T_curr= eval(self.leTemp.text(), {}, {})
       if((self.vIon.T_curr<-200.0)|(self.vCond.T_curr>200.0)):self.vIon.T_curr= 25.0 
       self.vIon.DispTemp(self.vIon.T_curr)
    q=0

class CfmIonEdit(QtGui.QMainWindow, Ui_fmIonEdit):

  def __init__(self, vIon):     
    super().__init__()
    self.setupUi(self)
    self.vIon = vIon
    self.ShowFlag=0
    self.tbSaveIon_.clicked.connect(self.on_tbSaveIon_clicked)
    self.setWindowTitle("Изменение иона");

  def on_tbSaveIon_clicked(self):
      self.vIon.Ions.IonName=self.leIonName.text()
      self.vIon.Ions.IonVal=self.leIonVal.text()
      self.vIon.Ions.MolMassa=self.leMolMassa.text()
      self.vIon.Ions.K=self.leK.text()
      if(self.vIon.CreateIonFlag==1):
          self.index=self.vIon.ProfilsDict['Иономер']['Ions_Table_All_Count']
          self.vIon.IonDict[self.index]={}
          self.vIon.IonDict[self.index][0]=self.vIon.Ions.IonName
          self.vIon.IonDict[self.index][1]=self.vIon.Ions.IonVal
          self.vIon.IonDict[self.index][2]=self.vIon.Ions.MolMassa
          self.vIon.IonDict[self.index][3]=self.vIon.Ions.K
          self.vIon.IonDict[self.index][4]=0
          self.vIon.ProfilsDict['Иономер']['Ions_Table_All_Count']=self.index+1
          q=0
      else:
          self.index=self.vIon.winIonSelect.index
          self.vIon.IonDict[self.index][0]=self.vIon.Ions.IonName
          self.vIon.IonDict[self.index][1]=self.vIon.Ions.IonVal
          self.vIon.IonDict[self.index][2]=self.vIon.Ions.MolMassa
          self.vIon.IonDict[self.index][3]=self.vIon.Ions.K
          q=0
      self.vIon.CreateIonFlag=0
      self.vIon.vCE.save_LocalProfil_state()
      self.vIon.winIonSelect.DrawIonTable()
      self.close()
      q=0

class CfmIonDigitSelect(QtGui.QMainWindow, Ui_fmIonDigitSelect):

  def __init__(self, vIon):    
    super().__init__()
    self.setupUi(self)
    self.vIon = vIon
    self.setWindowTitle("Выбор буфера");
    self.indexIon=0
    m=0
    self.twIonDigitSelect_.clear()
    self.twIonDigitSelect_.setColumnCount(2)
    self.twIonDigitSelect_.setRowCount(3) 	
    while(m<=2):
        n=0
        while(n<=1):
              newitem = QtGui.QTableWidgetItem()
              tmpi=m*2+n
              newitem.setText(str(self.vIon.IonGrad.BufRastvor[tmpi]))
              self.twIonDigitSelect_.setItem(m, n, newitem)
              n=n+1
        m=m+1
    q=0
    self.twIonDigitSelect_.cellClicked.connect(self.on_twIonDigitSelect_cellClicked)
    self.twIonDigitSelect_.cellDoubleClicked.connect(self.on_twIonDigitSelect_cellDoubleClicked)
    self.tbSelectDigitIon.clicked.connect(self.on_tbSelectDigitIon)

  def on_twIonDigitSelect_cellClicked(self,i,j):
      self.indexIon=i*2+j
      self.leIonDigitSelect_.setText(str(self.vIon.IonGrad.BufRastvor[self.indexIon]))
      q=0

  def on_twIonDigitSelect_cellDoubleClicked(self,i,j):
      self.indexIon=i*2+j
      self.leIonDigitSelect_.setText(str(self.vIon.IonGrad.BufRastvor[self.indexIon]))
      self.on_tbSelectDigitIon()
      q=0
  def on_tbSelectDigitIon(self):
       self.vIon.IonGrad.CurrBufRastvor= eval(self.leIonDigitSelect_.text(), {}, {})#eval(self.leNt_1.text(), {}, {})
       self.vIon.IonGrad.SetDataToTable()
       self.vIon.winIonMessage.NextStep()
       self.close()
       q=0

class CfmIonMessageOK(QtGui.QMainWindow, Ui_fmIonMessageOK):

  def __init__(self, vIon):    
    super().__init__()
    self.setupUi(self)
    self.vIon = vIon
    self.ShowFlag=0
    self.tbOK.clicked.connect(self.close)

class CfmIonProfilNameOK(QtGui.QMainWindow, Ui_fmIonProfilNameOK):

  def __init__(self, vIon):    
    super().__init__()
    self.setupUi(self)
    self.vIon = vIon
    self.ShowFlag=0
    self.tbOK.clicked.connect(self.on_tbOK )

  def on_tbOK(self):
      qq=self.leProfilName_.text()
      if((qq!='')&(qq!=' ')):
          self.vIon.Profils.CurrentProf=-1
          self.vIon.Profils.PrName=qq
          self.vIon.winIon.show(0,0,0)
          self.close()
      q=0

class CfmIonMessage(QtGui.QMainWindow, Ui_fmIonMessage):

  def __init__(self, vIon):     
    super().__init__()
    self.setupUi(self)
    self.vIon = vIon
    self.ShowFlag=0
    self.AutoIzmCounter=0
    self.dCurrU=0
    self.dCurrU_Minus=0
    self.dCurrU_Plus=0
    self.dCurrU_Null=0
    self.CurrU_tmp_const=0
    self.btnOK.clicked.connect(self.on_buttonBox_accept)
    self.btnCancel.clicked.connect(self.on_buttonBox_reject)
    self.setWindowTitle("Выбор значения  ЭДС буферного раствора");

  def on_buttonBox_accept(self):
    if(self.vIon.IonGrad.StepIzm==3):
       self.vIon.IonGrad.SetDataToProfil()
       self.vIon.IonGrad.Reset()
       self.close()
    if((self.vIon.IonGrad.StepIzm==2)&(self.vIon.IonGrad.AutoIzmWaitFlag==1)):
       self.vIon.IonGrad.AutoIzmStepCancel=1
       q=0
    ''' '''
    if((self.vIon.IonGrad.StepIzm==2)&(self.vIon.IonGrad.AutoIzmWaitFlag==0)):
       self.vIon.winIonDigitSelect.show()
       self.close()

    if(self.vIon.IonGrad.StepIzm==1):       
       self.vIon.IonGrad.CurrU=round(self.vIon.U_m,2)
       self.lblMessage.setText('Напряжение U='+self.vIon.formS_2.format(self.vIon.IonGrad.CurrU)+'мВ')
       self.lblMessage_1.setText('Выберите значение  ЭДС буферного раствора')
       self.lblMessage_2.setText('')
       self.vIon.IonGrad.StepIzm=2

       self.trAuto=self.startTimer(300)
       self.vIon.IonGrad.AutoIzmWaitFlag=1
    q=0

  def on_buttonBox_reject(self):
    self.vIon.IonGrad.Reset()
    self.close()
    q=0

  def showEvent(self, event):
      q=0

  def timerEvent(self, e):
      ''' '''
      self.vIon.IonGrad.CurrU=round(self.vIon.U_m,2)
      self.lblMessage.setText('Напряжение U='+self.vIon.formS_2.format(self.vIon.IonGrad.CurrU)+'мВ')
      ''' '''
      if(self.vIon.IonGrad.AutoIzm==0):
          self.vIon.IonGrad.AutoIzmWaitFlag=0 # 
          q=0
      '''  '''
      if(self.vIon.IonGrad.AutoIzm==1):
          self.lblMessage_1.setText('Напряжение устанавливается...')
          self.lblMessage_2.setText('Для прекращения установки и фиксации значения нажмите "ОК"')
          if(self.AutoIzmCounter==0): self.CurrU_tmp_const=self.vIon.IonGrad.CurrU
          self.dCurrU=self.vIon.IonGrad.CurrU-self.CurrU_tmp_const
          if(self.dCurrU>0):
              self.dCurrU_Plus=self.dCurrU_Plus+1
              self.dCurrU_Minus=0
              self.dCurrU_Plus=0
              self.dCurrU_Null=0
          if(self.dCurrU<0):
              self.dCurrU_Minus=self.dCurrU_Minus+1
              self.dCurrU_Plus=0
              self.dCurrU_Null=0
          if(self.dCurrU==0):
              self.dCurrU_Null=self.dCurrU_Null+1
              self.dCurrU_Plus=0
              self.dCurrU_Minus=0
          '''  '''
          if((math.fabs(self.dCurrU)<0.12)&(self.dCurrU_Plus<=3)&(self.dCurrU_Minus<=3)|(self.vIon.IonGrad.AutoIzmStepCancel==1)):
             self.AutoIzmCounter=self.AutoIzmCounter+1
             '''    '''
             if((self.AutoIzmCounter>25)|(self.vIon.IonGrad.AutoIzmStepCancel==1)):
                 self.killTimer(self.trAuto)
                 self.vIon.IonGrad.AutoIzmWaitFlag=0
                 self.lblMessage_1.setText('Выберите значение буфера раствора')
                 self.lblMessage_2.setText('')
                 self.AutoIzmCounter=0
                 self.dCurrU=0
                 self.dCurrU_Minus=0
                 self.dCurrU_Plus=0
                 self.dCurrU_Null=0
                 self.CurrU_tmp_const=0
                 self.vIon.IonGrad.AutoIzmStepCancel=0
          else: self.AutoIzmCounter=0
      q=0

  def NextStep(self):
    if(self.vIon.IonGrad.StepIzm==1):
      self.setWindowTitle("Выбор значения  ЭДС буферного раствора");
      self.lblMessage.setText('Введите электрод в буферный раствор'+str(self.vIon.IonGrad.CurrIzm))
      self.lblMessage_2.setText('')
      self.lblMessage_1.setText(' ')
    if(self.vIon.IonGrad.StepIzm==3):
      self.setWindowTitle('Выбор значения  ЭДС буферного раствора');
      self.lblMessage.setText('Градуировка выполнена')
      self.lblMessage_1.setText('Производить замену существующих данных?')
      self.lblMessage_2.setText('')
    self.show()

  def closeEvent(self, event):
    self.killTimer(self.trAuto)

class CfmIonMessSelect(QtGui.QMainWindow, Ui_fmIonMessSelect):

  def __init__(self, vIon):     
    super().__init__()
    self.setupUi(self)
    self.vIon = vIon
    self.KolIzmIon=0
    self.chbAutoIzm.setChecked(True)
    self.tbSelectKolIzm.clicked.connect(self.on_tbSelectKolIzm)
    self.tbSelectKolIon_1.clicked.connect(self.on_tbSelectKolIon_1)
    self.tbSelectKolIon_2.clicked.connect(self.on_tbSelectKolIon_2)
    self.tbSelectKolIon_3.clicked.connect(self.on_tbSelectKolIon_3)
    self.tbSelectKolIon_4.clicked.connect(self.on_tbSelectKolIon_4)

  def on_tbSelectKolIzm(self):
    if(self.vIon.IonGrad.KolIzm==0):
        self.KolIzmIon=self.spinBox.value()
        if(self.KolIzmIon>0):
           self.SelKolIzm()
    q=0
    
  def on_tbSelectKolIon_1(self):
      self.KolIzmIon=1
      self.SelKolIzm()
      q=0

  def on_tbSelectKolIon_2(self):
      self.KolIzmIon=2
      self.SelKolIzm()
      q=0

  def on_tbSelectKolIon_3(self):
      self.KolIzmIon=3
      self.SelKolIzm()
      q=0

  def on_tbSelectKolIon_4(self):
      self.KolIzmIon=4
      self.SelKolIzm()
      q=0

  def SelKolIzm(self):
      self.vIon.IonGrad.StepIzm=1
      self.vIon.IonGrad.KolIzm=self.KolIzmIon
      self.vIon.IonGrad.AutoIzm=int(self.chbAutoIzm.isChecked())
      self.CurrIzm=1
      self.vIon.IonGrad.CurrIzm=1
      self.vIon.winIonMessage.NextStep()
      self.close()
      q=0

class CfmIonSelect(QtGui.QMainWindow, Ui_fmIonSelect):

  def __init__(self, vIon):     
    super().__init__()
    self.setupUi(self)
    self.vIon = vIon
    self._i=-1
    self._j=-1
    self.ShowFlag=0
    self.DrawIonTable()
    self.twIonSelect.cellClicked .connect(self.on_twIonSelect_changed_)
    self.twIonSelect.cellDoubleClicked .connect(self.on_twIonSelect_closed_)
    self.tbSelectIon.clicked.connect(self.on_tbSelectIon_clicked)
    self.tbAddIon_.clicked.connect(self.on_tbAddIon_clicked)
    self.tbDelIon_.clicked.connect(self.on_tbDelIon_clicked)
    self.tbEditIon_.clicked.connect(self.on_tbEditIon_clicked)

  def DrawIonTable(self):
    m=0
    tmp1=self.vIon.ProfilsDict['Иономер']['Ions_Table_All_Count']/5.0
    tmp2=self.vIon.ProfilsDict['Иономер']['Ions_Table_All_Count']//5
    if(tmp1>tmp2):
        _row=tmp2+1
    else:
        _row=tmp2
    self.twIonSelect.clear()
    self.twIonSelect.setColumnCount(5)
    self.twIonSelect.setRowCount(_row) 	
    while(m<=_row):
        n=0
        while(n<=4):
            if(m*5+n<self.vIon.ProfilsDict['Иономер']['Ions_Table_All_Count']):
              newitem = QtGui.QTableWidgetItem()
              newitem.setText(self.vIon.IonDict[m*5+n][0])#+'A<sub>'+str(self.vIon.IonDict[m*5+n][2])+'</sub>')
              cl_1=QtGui.QColor(123,140,66)
              cl_2=QtGui.QColor(123,140,66)
              if(self.vIon.IonDict[m*5+n][3]==1):newitem.setBackgroundColor(cl_1 )
              if(self.vIon.IonDict[m*5+n][3]==0):newitem.setBackgroundColor(cl_2 )
              self.twIonSelect.setItem(m, n, newitem)
            n=n+1
        m=m+1

  def on_tbAddIon_clicked(self):
    self.vIon.CreateIonFlag=1
    self.vIon.winIonEdit.show()
    m=0

  def on_tbDelIon_clicked(self):
    self.index=self._i*5+self._j
    tmpi=self.index
    if(self.index>self.vIon.ProfilsDict['Иономер']['Ions_Table_Const_Count']-1):
        while(tmpi<self.vIon.ProfilsDict['Иономер']['Ions_Table_All_Count']-1):
            self.vIon.IonDict[tmpi]=self.vIon.IonDict[tmpi+1]
            tmpi=tmpi+1
            w=0
        del self.vIon.IonDict[tmpi] 
        self.vIon.ProfilsDict['Иономер']['Ions_Table_All_Count']=self.vIon.ProfilsDict['Иономер']['Ions_Table_All_Count']-1       
        self.vIon.vCE.save_LocalProfil_state()
        self.vIon.winIonSelect.DrawIonTable()
        q=0
    m=0

  def on_tbEditIon_clicked(self):
    self.index=self._i*5+self._j
    if(self.index>self.vIon.ProfilsDict['Иономер']['Ions_Table_Const_Count']-1):
      self.vIon.winIonEdit.leIonName.setText(str(self.vIon.IonDict[self.index][0]))
      self.vIon.winIonEdit.leIonVal.setText(str(self.vIon.IonDict[self.index][1]))
      self.vIon.winIonEdit.leMolMassa.setText(str(self.vIon.IonDict[self.index][2]))
      self.vIon.winIonEdit.leK.setText(str(self.vIon.IonDict[self.index][3]))
      self.vIon.winIonEdit.show()
    m=0

  def on_twIonSelect_changed_(self,i,j):
      self._i=i
      self._j=j
      self.index=self._i*5+self._j
      self.lblIon.setText(self.vIon.IonDict[self.index][0]+' '+str(self.vIon.IonDict[self.index][1]))
      self.lblMol_Massa.setText(str(self.vIon.IonDict[self.index][2]))
      self.lblKIon.setText(str(self.vIon.IonDict[self.index][3]))

  def on_twIonSelect_closed_(self,i,j):
      self._i=i
      self._j=j
      self.on_tbSelectIon_clicked()
      q=0

  def on_tbSelectIon_clicked(self):
      self.index=self._i*5+self._j
      self.vIon.Profils.Ion_Name=self.vIon.IonDict[self.index][0]
      self.vIon.Profils.Ion_Val=self.vIon.IonDict[self.index][1]
      self.vIon.Profils.Ion_Mol_Massa=self.vIon.IonDict[self.index][2]
      self.vIon.Profils.Ion_K=self.vIon.IonDict[self.index][3]
      self.vIon.winIon.lblIon.setText(self.vIon.Profils.Ion_Name+'  '+str(self.vIon.Profils.Ion_Val))
      self.vIon.winIon.lblMol_Massa.setText(str(self.vIon.Profils.Ion_Mol_Massa))
      self.vIon.winIon.lblKIon.setText(str(self.vIon.Profils.Ion_K))
      #self.vIon.win.llMain.setText('p'+self.vIon.Profils.Ion_Name)
      self.vIon.Ion_ed='p'+self.vIon.Profils.Ion_Name
      self.close()
      q=0
#---
class CfmICalib(QtGui.QMainWindow, Ui_fmICalib): 
  """ окно калибровки виртуального иономера"""

  def __init__(self, vIon):     
    super().__init__()
    self.setupUi(self)
    self.vIon = vIon
    self.ShowFlag=0
    self.formpX = "{:5.2f}" 
    self.formE = "{:6.3f}"
    self.formE1 = "{:4.3f}"
    self.hint = QtCore.Qt.UserRole + 1 
    self.fFreeze = False
    self.lastPrInd = -1
    self.lastPrName = '' 
    self.stPrEd = 0
    self.GradFlag = 0
    self.fNewPr = False
    # меню наименования профиля (всплывающее и выпадающее)
    self.menuC = QtGui.QMenu(self)
    self.menuC.addAction(self.actPrIns)
    self.muProf.addAction(self.actPrIns)
    self.menuC.addAction(self.actPrRen)
    self.muProf.addAction(self.actPrRen)
    self.menuC.addSeparator()
    self.muProf.addSeparator()
    self.menuC.addAction(self.actPrDel) 
    self.muProf.addAction(self.actPrDel)
     # меню калибровочной таблицы (всплывающее и выпадающее)
    self.menuT = QtGui.QMenu(self)
    self.menuT.addAction(self.actTIns)
    self.muTabl.addAction(self.actTIns) 
    self.menuT.addSeparator()
    self.muTabl.addSeparator()
    self.menuT.addAction(self.actTDel)
    self.muTabl.addAction(self.actTDel)
    self.teCalib.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)    
    self.teCalib.customContextMenuRequested.connect(self.on_teCalib_menu)
    self.teCalib.itemChanged.connect(self.on_teCalib_changed_)
    self.tbSelectIon.clicked.connect(self.on_tbSelectIon_toggle)
    self.tbGrad.clicked.connect(self.on_tbGrad_toggle)
    self.actTIns.triggered.connect(self.on_actTIns_toggle)
    self.actTDel.triggered.connect(self.on_actTDel_toggle)  
    self.tbAddRow.clicked.connect(self.on_Add_Row)
    self.tbDelRow.clicked.connect(self.on_Del_Row)   
    self.tbSaveProfilIon.clicked.connect(self.on_tbSaveProfilIon_toggle) 
    self.leZero.setEnabled(False)

  def on_tbSelectIon_toggle(self):
      self.vIon.winIonSelect.show()

  def on_tbGrad_toggle(self):
      self.GradFlag = 1
      self.vIon.IonGrad.Reset()
      self.vIon.winIonMessSelect.show()
     
  def on_Change_Any(self):
      if(self.ShowFlag==1):
        Kt=1.9836e-4
        pXu=eval(self.lepXu.text(), {}, {})
        Ecm=eval(self.leZero.text(), {}, {})
       
        PrName=self.leProfilName_.text()
        PrDescr=self.leDescr_.text()
        S_min=eval(self.leS_min.text(), {}, {})
        self.vIon.Profils.ChangeCurrProfil(self.vIon.Profils.Ecm, self.vIon.Profils.Stc, Kt, pXu, self.vIon.Profils.Tcb, PrName, PrDescr,S_min)

  def on_Init_Any(self):
      self.lepXu.setText(str(self.vIon.Profils.pXu))
      self.leZero.setText(str(self.vIon.Profils.Ecm*1000))
      self.vIon.winIon.lblIon.setText(self.vIon.Profils.Ion_Name+'  '+str(self.vIon.Profils.Ion_Val))
      self.vIon.winIon.lblMol_Massa.setText(str(self.vIon.Profils.Ion_Mol_Massa))
      self.vIon.winIon.lblKIon.setText(str(self.vIon.Profils.Ion_K))
      self.vIon.win.lblProfilName.setText(self.vIon.Profils.PrName)
      self.vIon.Ion_ed='p'+self.vIon.Profils.Ion_Name
      try:
       a=self.vIon.Profils.PrName
      except:
          a=''
      self.leProfilName_.setText(a)
      try:
       b=self.vIon.Profils.PrDescr
      except:
          b=''
      self.leDescr_.setText(b)
      try:
       Sm=self.vIon.Profils.S_min
      except:
          Sm=57.0
      self.leS_min.setText(str(Sm))
      self.lepXu.setFocus()  

  def ClTbl_draw_(self):
    """ отрисовка профиля  в калибровочной таблице teCalib + подготовка к редактированию """
    self.pXcol = sorted(self.vIon.Profils.pXdict)
    pXsize = len(self.pXcol)
    if pXsize:
      self.fFreeze = True # "заморозка" на время заполнения таблицы    
      # извлекаем данные из профиля в таблицу
      if self.teCalib.rowCount() != pXsize:  self.teCalib.setRowCount(pXsize)
      for row in range(pXsize): 
        if not self.teCalib.verticalHeaderItem(row):
          head = QtGui.QTableWidgetItem("")
          self.teCalib.setVerticalHeaderItem(row, head)
        else: 
          head = self.teCalib.verticalHeaderItem(row)
 
        head.setText(str(row + 1))
        head.setData(self.hint, row)  # хинт для связи с pXcol -> pXdict, независимый от вставки новых незаполненных строк

        if not self.teCalib.item(row, 0):  self.teCalib.setItem(row, 0, QtGui.QTableWidgetItem(""))
        self.teCalib.item(row, 0).setText((self.formpX.format(self.pXcol[row])))  # pX

        if not self.teCalib.item(row, 1):  self.teCalib.setItem(row, 1, QtGui.QTableWidgetItem(""))
        try:
           self.teCalib.item(row, 1).setText(self.formE.format(1000 * self.vIon.Profils.pXdict[self.pXcol[row]][0])) # E [мВ]
        except:
           q=0

        ###self.teCalib.setItem(row, 2, QtGui.QTableWidgetItem("")) # Отклонение
        if not self.teCalib.item(row, 2):  self.teCalib.setItem(row, 2, QtGui.QTableWidgetItem(""))
        self.teCalib.item(row, 2).setText(self.formE.format(1000 * self.vIon.Profils.pXdict[self.pXcol[row]][1])) # Отклонение

      self.fFreeze = False 
    self.teCalib.resizeColumnsToContents()

  def Prof_show_(self,):
    """ полная отрисовка профиля в окне градуировки """
    self.ClTbl_draw_()
    self.lepXu.setText(self.formpX.format(self.vIon.Profils.pXu)) # pX?? 
    self.leZero.setText(self.formE.format(self.vIon.Profils.Ecm*1000)) # Ecm
    self.lblS.setText(self.formE.format(self.vIon.Profils.S)) # S
    try:
      self.leS_min.setText(self.formE.format(self.vIon.Profils.S_min)) # S
    except:
      self.leS_min.setText(self.formE.format(57.0)) # S

  def closeEvent(self, event):
    self.vIon.vCE.OpenProfilVP_2Flag=0
    self.ShowFlag=0

  def show(self, profD, actPr, vIon): 
    if(self.vIon.vCE.OpenProfilVP_2Flag==0):
      self.on_Init_Any()
      self.ShowFlag=1
      self.Prof_show_()
      super().show()
      self.vIon.vCE.OpenProfilVP_2Flag=1

  def on_teCalib_menu(self, pos):
    self.menuT.popup(self.teCalib.mapToGlobal(pos)) 

  def on_cbElec_menu(self, pos):
    self.menuC.popup(self.cbElec.mapToGlobal(pos))


  def on_lepXuFinish(self):
    q=0

  def on_tbSaveProfilIon_toggle(self):
    """ сохранение профиля иономера """
    self.on_tbCalib_toggle_()
    if(self.ShowFlag==1):
      self.on_Change_Any()
      self.vIon.Profils.SaveCurrProfil()
      self.leProfilName_.setText(self.vIon.Profils.PrName)
      self.vIon.winSelectProfil.InitProfilsList()
      q=0

  def on_tbCalib_toggle_(self):
    """ расчет калибровочных коэффициентов """
    #LL.I("? ?°?????µ?? ???????????»?? {}".format(self.actPr.Name))
    for key in sorted(self.vIon.Profils.pXdict):
      #LL.I("pX = {} \t {}".format(key, self.actPr.pXdict[key]))
      q=0
     # нахождение Ecm и S методом наименьших квадратов
    pX_acc = 0
    E_acc = 0
    pXE_acc = 0
    pX2_acc = 0
    for pX, val in self.vIon.Profils.pXdict.items():
      pX_acc += pX  
      E_acc += val[0]
      pXE_acc += pX * val[0]
      pX2_acc += pX * pX 

    N = len(self.vIon.Profils.pXdict)    
    pX_av = pX_acc / N
    E_av = E_acc / N
    S = (pXE_acc / N) - (pX_av * E_av)  
    S = S / ((pX2_acc / N) - (pX_av * pX_av))
    E0 =  E_av - (S * pX_av)
    

    T = self.vIon.T_curr
    #LL.I("E0 = {}  S = {}  T = {}".format(E0, S, T))
    self.ClTbl_draw_()
    # расчет отклонений для каждой калибровочной точки в таблице
    self.fFreeze = True
    for row in range(self.teCalib.rowCount()):
      head = self.teCalib.verticalHeaderItem(row)
      if (head.text() != "-") and (head.data(self.hint) != None):
        pX_tst = self.pXcol[head.data(self.hint)]
        Offs = E0 + (S * pX_tst) - self.vIon.Profils.pXdict[pX_tst][0]
        self.teCalib.item(row, 2).setText(self.formE.format(1000 * Offs))  # Отклонение [мВ]
    self.fFreeze = False
    # перенос в профиль - c пересчетом к изопотенциальной точке 
    #(МНК привел к виду E = E0 + S * pX)
    self.vIon.Profils.pXu  = eval(self.lepXu.text(), {}, {})
    self.vIon.Profils.Ecm = E0 + S * self.vIon.Profils.pXu
    self.vIon.Profils.Tcb = T
    try:
      self.vIon.Profils.S_min  = eval(self.leS_min.text(), {}, {})
    except:
      self.vIon.Profils.S_min  =57.0
      self.leS_min.setText(self.vIon.Profils.S_min)

    if(self.vIon.Profils.Ion_Val <0): 
        tmpV=-self.vIon.Profils.Ion_Val 
    else:
        tmpV=self.vIon.Profils.Ion_Val
    self.vIon.Profils.Stc = (-S - (self.vIon.Profils.Kt * T))/tmpV  
    self.vIon.Profils.S = S*1000
    if(self.vIon.Profils.S<0):self.vIon.Profils.S=self.vIon.Profils.S*(-1)
    self.lblS.setText(self.formE1.format(self.vIon.Profils.S)) # S
    tmptxt=''
    '''if(self.GradFlag == 1):
      if (self.vIon.Profils.S<50): 
        tmptxt='Электрод неисправен. Требуется замена электрода'
      if (self.vIon.Profils.S>56):
        tmptxt='Электрод исправен.'
      if ((self.vIon.Profils.S<=56)&(self.vIon.Profils.S>=50)):
        tmptxt='Электрод требует регенерации.'
        '''
    Sminmin=self.vIon.Profils.S_min-5
    if(self.GradFlag == 1):
      if (self.vIon.Profils.S<Sminmin): 
        tmptxt='Электрод неисправен. Требуется замена электрода'
      if (self.vIon.Profils.S>self.vIon.Profils.S_min):
        tmptxt='Электрод исправен.'
      if ((self.vIon.Profils.S<=self.vIon.Profils.S_min)&(self.vIon.Profils.S>Sminmin)):
        tmptxt='Электрод требует регенерации.'
        
      self.vIon.winIonMessageOK.lblMessage.setText(tmptxt)
      self.vIon.winIonMessageOK.show()
      self.GradFlag = 0
  
    ###LL.I("pXu = {}".format( self.actPr.pXu)) 
    ###LL.I("Ecm = {}  Stc = {}  Kt = {} ".format(self.actPr.Ecm, self.actPr.Stc, self.actPr.Kt)) 
    # сохраняем состояние вирт. прибора (т.е. вместе с обновленным профилем) в файл
    self.vIon.SaveState()
    sstate.saveVstate()

  def on_actTIns_toggle(self):
    #print("on_actTIns_toggle !!!")
    cur_row = self.teCalib.currentRow()
    if cur_row == -1:  cur_row = 0;  # если нет выбранной строки - вставка в начало таблицы
    self.teCalib.insertRow(cur_row) 
    self.fFreeze = True
    if not self.teCalib.verticalHeaderItem(cur_row):  
      self.teCalib.setVerticalHeaderItem(cur_row, QtGui.QTableWidgetItem("-"))
    else: 
      self.teCalib.verticalHeaderItem(cur_row).setText("-")
    if not self.teCalib.item(cur_row, 0):
      self.teCalib.setItem(cur_row, 0, QtGui.QTableWidgetItem(""))  # pX 
    if not self.teCalib.item(cur_row, 1): 
      self.teCalib.setItem(cur_row, 1, QtGui.QTableWidgetItem(""))  # E [????]    
    if not self.teCalib.item(cur_row, 2): 
      self.teCalib.setItem(cur_row, 2, QtGui.QTableWidgetItem(""))  # ???????»?????µ?????µ 
    self.fFreeze = False 

  def on_actTDel_toggle(self):
    #print("on_actTDel_toggle !!!")  
    cur_row = self.teCalib.currentRow()
    head = self.teCalib.verticalHeaderItem(cur_row)
    if (head.text() != "-") and (head.data(self.hint) != None):
      pX = self.pXcol[head.data(self.hint)]
      del self.pXcol[head.data(self.hint)]
      del self.vIon.Profils.pXdict[pX]  

    self.teCalib.removeRow(cur_row)
    self.ClTbl_draw_()

  def on_Add_Row(self):
    #print("on_actTIns_toggle !!!")
    cur_row = self.teCalib.currentRow()
    if cur_row == -1:  cur_row = 0;  # если нет выбранной строки - вставка в начало таблицы
    self.teCalib.insertRow(cur_row) 
    self.fFreeze = True
    if not self.teCalib.verticalHeaderItem(cur_row):  
      self.teCalib.setVerticalHeaderItem(cur_row, QtGui.QTableWidgetItem("-"))
    else: 
      self.teCalib.verticalHeaderItem(cur_row).setText("-")
    if not self.teCalib.item(cur_row, 0):
      self.teCalib.setItem(cur_row, 0, QtGui.QTableWidgetItem(""))  # pX 
    if not self.teCalib.item(cur_row, 1): 
      self.teCalib.setItem(cur_row, 1, QtGui.QTableWidgetItem(""))  # E [????]    
    if not self.teCalib.item(cur_row, 2): 
      self.teCalib.setItem(cur_row, 2, QtGui.QTableWidgetItem(""))  # ???????»?????µ?????µ 
    self.fFreeze = False 

  def on_Del_Row(self):
    #print("on_actTDel_toggle !!!")  
    cur_row = self.teCalib.currentRow()
    head = self.teCalib.verticalHeaderItem(cur_row)
    if (head.text() != "-") and (head.data(self.hint) != None):
      pX = self.pXcol[head.data(self.hint)]
      del self.pXcol[head.data(self.hint)]
      del self.vIon.Profils.pXdict[pX]  

    self.teCalib.removeRow(cur_row)
    self.ClTbl_draw_()

  def on_teCalib_changed_(self, item):
    #print("on_teCalib_changed ({},{}) text='{}'".format(item.row(), item.column(), item.text()))
    if not self.fFreeze: 
      #print("item={}".format(item))
    
      res = None
      try:
        res = eval(item.text(), {}, {})
      except:
        ###LL.exception('')
        Q=0

      if res != None: 
        head = self.teCalib.verticalHeaderItem(item.row())
        #print("head hint = {}".format(head.data(self.hint))) 
        if (head.data(self.hint) == None) or (head.text() == "-"):
          # идет редактирование новой строки
          if item.column() == 0:
            # pX 
            newV = [0,0] #self.actPr.getEmptyDVal() ???????° =0
            try:
              # перенос остальных колонок 
              for i in range(1, len(newV)+1):
                tmpI = self.teCalib.item(item.row(), i)
                if tmpI and tmpI.text():
                  data = eval(tmpI.text(), {}, {}) 
                  if i == 1:
                    # напряжение (в таблице [мВ], в профиле [B]) 
                    newV[i-1] = data / 1000
                  else:
                    # 
                    newV[i-1] = data 
            except:
              ###LL.exception('') 
              q=0
            self.vIon.Profils.pXdict[res] = newV
            self.ClTbl_draw_() 

          else:
            #  pX
            pass
        else:
          # 
          old_pX = self.pXcol[head.data(self.hint)]
          #print("old_pX = {} res = {}".format(old_pX, res)) 
          if item.column() == 0:
            # pX
            oldV = self.vIon.Profils.pXdict.pop(old_pX)
            self.vIon.Profils.pXdict[res] = oldV
            self.pXcol[head.data(self.hint)] = res  
            self.ClTbl_draw_() # для пересортировки по возрастанию pX

          elif item.column() == 1:
            # напряжение (в таблице [мВ], в профиле [B])
            self.vIon.Profils.pXdict[old_pX][item.column() - 1] = res / 1000
            q=0  
          else:
            # все остальные колонки
            self.vIon.Profils.pXdict[old_pX][item.column() - 1] = res
            q=0
      else:
        #print("freezed !")    
        pass 

class CfmSelectProfil_Ion(QtGui.QMainWindow, Ui_fmSelectProfil_Ion): 
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

  def __init__(self, vIon):
     
    super().__init__()
    self.vIon = vIon
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

  def closeEvent(self, event):
    self.vIon.vCE.OpenProfilVP_1Flag=0
    self.close()
    s=0

  def on_tbAddProfil_toggle(self):
     self.vIon.fmIonProfilNameOK.show()
     self.close()
     
     return 0

  def InitProfilsList(self):
     self.vIon.Profils.Listcount=self.vIon.Profils.vCE.ProfilsDict['Иономер']['Listcount']
     tmpCnt=self.vIon.Profils.Listcount
     tmpNum=0
     self.lwProfils_.clear()#lwProfils
     while (tmpNum<tmpCnt):
         self.lwProfils_.addItem(self.vIon.Profils.vCE.ProfilsDict['Иономер']['List'][tmpNum])
         tmpNum=tmpNum+1
     return 0

  def on_tbSelectProfil_toggle(self):
     i=0
     a=self.lwProfils_.currentRow()
     self.vIon.Profils.SelectProfil(a)
     self.vIon.win.lblProfilName.setText(self.vIon.Profils.PrName)
     self.vIon.win.lblEd.setText('p'+self.vIon.Profils.Ion_Name)
     self.vIon.win.lblConcentr.setText('Содержание '+self.vIon.Profils.Ion_Name)
     self.close()
     return 0

  def on_tbChangeProfil(self):
     i=0
     a=self.lwProfils_.currentRow()
     self.vIon.Profils.SelectProfil(a)
     self.vIon.winIon.show(0,0,0)
     self.close()
     return 0
 
  def on_tbDelProfil(self):
     i=0
     a=self.lwProfils_.currentRow()
     self.vIon.Profils.DelProfil(a)
     self.InitProfilsList()
     return 0
   
  def on_lwProfils_Change(self):
     i=0
     a=self.lwProfils_.currentRow()
     self.vIon.Profils.SelectedProfilNum=a
     return 0

  def on_lwProfils_doubleClicked(self):
     self.vIon.Profils.SelectProfil(a)
     self.vIon.win.lblProfilName.setText(self.vIon.Profils.PrName)
     self.vIon.win.lblEd.setText('p'+self.vIon.Profils.Ion_Name)
     self.vIon.win.lblConcentr.setText('Содержание '+self.vIon.Profils.Ion_Name)
     self.vIon.winIon.show(0,0,0)
     self.close()
     return 0

  def on_lwProfils_clicked(self):
     a=self.lwProfils_.currentRow()
     tmpa=self.vIon.ProfilsDict['Иономер']['List'][a]
     tmp_PrDescr=self.vIon.ProfilsDict['Иономер'][tmpa]['PrDescr']
     self.tbDescribeProfil.setText(tmp_PrDescr)
     return 0

class CIonC():

    def __init__(self, vCE):
        q=0
        self.IonName=0
        self.IonVal=0
        self.MolMassa=1
        self.K=1

    def SaveIon():
        q=0

class CIonGrad():

    def __init__(self, vCE):
        q=0
        self.vCE=vCE
        self.KolIzm=0
        self.AutoIzm=0
        self.AutoIzmStepCancel=0
        self.AutoIzmWaitFlag=0
        self.StepIzm=0
        self.BufRastvor={}
        self.CalibrTable={}
        self.BufRastvor[0]=1.65
        self.BufRastvor[1]=3.56
        self.BufRastvor[2]=4.01
        self.BufRastvor[3]=6.86
        self.BufRastvor[4]=9.18
        self.BufRastvor[5]=12.43
        self.CurrIzm=0
        self.CurrBufRastvor=0
        self.CurrU=0

    def Reset(self):
        self.KolIzm=0
        self.AutoIzm=0
        self.StepIzm=0
        self.CurrIzm=0
        self.CurrBufRastvor=0
        self.CurrU=0
        self.CalibrTable={}
        q=0

    def SetDataToTable(self):
        self.CalibrTable[self.CurrIzm]={}
        self.CalibrTable[self.CurrIzm][1]=self.CurrU
        self.CalibrTable[self.CurrIzm][0]=self.CurrBufRastvor
        self.CurrIzm=self.CurrIzm+1
        self.StepIzm=1
        if(self.KolIzm<self.CurrIzm):self.StepIzm=3
        q=0

    def SetDataToProfil(self):
        while(self.vCE.winIon.teCalib.rowCount()>0):
            self.vCE.winIon.teCalib.selectRow(0)
            self.vCE.winIon.on_actTDel_toggle()
        tmpi=1
        while(tmpi<=self.KolIzm):
            self.vCE.winIon.on_actTIns_toggle()
            self.vCE.winIon.teCalib.selectRow(0)
            self.vCE.winIon.teCalib.item(0,1).setText(str(self.CalibrTable[tmpi][1]))
            self.vCE.winIon.teCalib.item(0,0).setText(str(self.CalibrTable[tmpi][0]))
            self.vCE.winIon.teCalib.setFocus()            
            tmpi=tmpi+1
        self.vCE.winIon.on_tbSaveProfilIon_toggle() 
        q=0

class CProfilsC():

    def __init__(self, vCE, profils={}):
       b=0
       self.profs=profils
       self.vCE=vCE
       self.vCE.ProfilsDict['Иономер'].setdefault('Listcount',0)
       self.vCE.ProfilsDict['Иономер'].setdefault('List',{})
       self.Listcount=self.vCE.ProfilsDict['Иономер']['Listcount']

       self.CurrentProf=-1
       self.Ecm=0.0
       self.S=0.0
       self.Stc=0.054153
       self.Kt=1.9836e-4
       self.pXu=7.0
       self.Tcb=20.0
       self.Ion_Name=''
       self.Ion_Val=1
       self.Ion_K=1.0
       self.Ion_Mol_Massa=1.0
       self.pXdict={}
       self.pXdict[4.01] = [0,0]
       self.pXdict[6.86] = [0,0]
       self.pXdict[9.18] = [0,0] 
       self.PrName=''
       self.PrDescr=''
       self.SelectedProfilNum=-1

    def LoadProfilsList(self):
       tmpi=0
       tmpl=[]
       while tmpi<self.Listcount-1:
           tmpl.append(self.vCE.ProfilsDict['Иономер']['List'][tmpi])
       return tmpl
 
    def LoadProfil(self,prName=''):
        tmpname=self.PrName
        tmpNum=0
        tmpi=0
        if(self.Listcount==0):
           self.Ecm=0.0
           self.S=0.0
           self.Stc=0.054153
           self.Kt=1.9836e-4
           self.pXu=7.0
           self.Tcb=20.0
           self.S_min=57.0

           self.PrDescr=''
           self.PrName='(???µ??)'
           self.vCE.PrName=self.PrName    
           self.vCE.Ecm=self.Ecm
           self.vCE.Stc=self.Stc
           self.vCE.Kt=self.Kt
           self.vCE.pXu=self.pXu
           self.vCE.Tcb=self.Tcb
           elf.vCE.S_min=self.S_min

        tmpi=0
        if(self.Listcount>0):
           while (tmpi<self.Listcount): 
             if (self.vCE.ProfilsDict['Иономер']['List'][tmpi]==prName):
                 self.SelectProfil(tmpi)
                 tmpi=self.Listcount
             tmpi=tmpi+1
           self.PrName=prName
        return 0

    def CreateProfil(self):
       tmpname=self.PrName
       tmpNum=0
       tmpi=0
       if(self.Listcount==0): tmpnameNum=tmpname
       while (tmpi<self.Listcount):
          if(tmpNum>0):tmpnameNum=tmpname+str(tmpNum) 
          else: tmpnameNum=tmpname 
          if (self.vCE.ProfilsDict['Иономер']['List'][tmpi]==tmpnameNum):
              tmpNum=tmpNum+1
              tmpnameNum=tmpnameNum+str(tmpNum) 
              tmpi=0
          tmpi=tmpi+1
       self.PrName=tmpnameNum
       self.vCE.ProfilsDict['Иономер']['List'][self.Listcount]=str(self.PrName)
       self.Listcount=self.Listcount+1
       self.vCE.ProfilsDict['Иономер']['Listcount']=self.Listcount
       self.vCE.ProfilsDict['Иономер'][self.PrName]={}
       self.vCE.ProfilsDict['Иономер'][self.PrName]['Ecm']=self.Ecm
       self.vCE.ProfilsDict['Иономер'][self.PrName]['Stc']=self.Stc
       self.vCE.ProfilsDict['Иономер'][self.PrName]['S']=self.S
       self.vCE.ProfilsDict['Иономер'][self.PrName]['S_min']=self.S_min
       self.vCE.ProfilsDict['Иономер'][self.PrName]['Kt']=self.Kt
       self.vCE.ProfilsDict['Иономер'][self.PrName]['pXu']=self.pXu
       self.vCE.ProfilsDict['Иономер'][self.PrName]['Tcb']=self.Tcb
       self.vCE.ProfilsDict['Иономер'][self.PrName]['Ion_Name']=self.Ion_Name
       self.vCE.ProfilsDict['Иономер'][self.PrName]['Ion_Val']=self.Ion_Val
       self.vCE.ProfilsDict['Иономер'][self.PrName]['Ion_K']=self.Ion_K
       self.vCE.ProfilsDict['Иономер'][self.PrName]['Ion_Mol_Massa']=self.Ion_Mol_Massa
       self.vCE.ProfilsDict['Иономер'][self.PrName]['pXdict']={}
       self.vCE.ProfilsDict['Иономер'][self.PrName]['pXdict']=copy.deepcopy(self.pXdict)
       self.vCE.ProfilsDict['Иономер'][self.PrName]['PrDescr']=self.PrDescr

    def DelProfil(self, index):
       tmpi=0
       tmpname=self.vCE.ProfilsDict['Иономер']['List'][index]
       try:
        del self.vCE.ProfilsDict['Иономер'][tmpname]
       except: q=0
       tmpi=index
       while (tmpi<=self.Listcount-2):
          self.vCE.ProfilsDict['Иономер']['List'][tmpi]=self.vCE.ProfilsDict['Иономер']['List'][tmpi+1]
          tmpi=tmpi+1
       #while (tmpi<self.Listcount-1):#
       del self.vCE.ProfilsDict['Иономер']['List'][self.Listcount-1]
       self.Listcount=self.Listcount-1
       self.vCE.ProfilsDict['Иономер']['Listcount']=self.Listcount

    def ChangeProfil(self, index=-1):
       self.CurrentProf=index
       if(self.CurrentProf!=-1):
         self.Listcount=self.vCE.ProfilsDict['Иономер']['Listcount']
         if(self.vCE.ProfilsDict['Иономер']['List'][self.CurrentProf]!=self.PrName):
           self.vCE.ProfilsDict['Иономер']['List'][self.CurrentProf]={}
           del self.vCE.ProfilsDict['Иономер'][self.PrName]  
         else:
           self.vCE.ProfilsDict['Иономер'][self.PrName]['Ecm']=self.Ecm
           self.vCE.ProfilsDict['Иономер'][self.PrName]['Stc']=self.Stc
           self.vCE.ProfilsDict['Иономер'][self.PrName]['S']=self.S
           self.vCE.ProfilsDict['Иономер'][self.PrName]['Kt']=self.Kt
           self.vCE.ProfilsDict['Иономер'][self.PrName]['pXu']=self.pXu
           self.vCE.ProfilsDict['Иономер'][self.PrName]['Tcb']=self.Tcb
           self.vCE.ProfilsDict['Иономер'][self.PrName]['pXdict']=copy.deepcopy(self.pXdict)
           self.vCE.ProfilsDict['Иономер'][self.PrName]['PrDescr']=self.PrDescr
           self.vCE.ProfilsDict['Иономер'][self.PrName]['Ion_Name']=self.Ion_Name
           self.vCE.ProfilsDict['Иономер'][self.PrName]['Ion_Val']=self.Ion_Val
           self.vCE.ProfilsDict['Иономер'][self.PrName]['Ion_K']=self.Ion_K
           self.vCE.ProfilsDict['Иономер'][self.PrName]['Ion_Mol_Massa']=self.Ion_Mol_Massa
           try:
             self.vCE.ProfilsDict['Иономер'][self.PrName]['S_min']=self.S_min
           except:
             self.S_min=57.0
             self.vCE.ProfilsDict['Иономер'][self.PrName]['S_min']=self.S_min
                                 
    def SelectProfil(self, index):
       self.CurrentProf=index
       self.Listcount=self.vCE.ProfilsDict['Иономер']['Listcount']
       tmpa=self.vCE.ProfilsDict['Иономер']['List'][self.CurrentProf]
       self.PrName=tmpa
       self.Ecm=self.vCE.ProfilsDict['Иономер'][self.PrName]['Ecm']
       self.S=self.vCE.ProfilsDict['Иономер'][self.PrName]['S']
       self.Stc=self.vCE.ProfilsDict['Иономер'][self.PrName]['Stc']
       self.Kt=self.vCE.ProfilsDict['Иономер'][self.PrName]['Kt']
       self.pXu=self.vCE.ProfilsDict['Иономер'][self.PrName]['pXu']
       self.Tcb=self.vCE.ProfilsDict['Иономер'][self.PrName]['Tcb']
       self.Ion_Name=self.vCE.ProfilsDict['Иономер'][self.PrName]['Ion_Name']
       self.Ion_Val=self.vCE.ProfilsDict['Иономер'][self.PrName]['Ion_Val']
       self.Ion_K=self.vCE.ProfilsDict['Иономер'][self.PrName]['Ion_K']
       self.Ion_Mol_Massa=self.vCE.ProfilsDict['Иономер'][self.PrName]['Ion_Mol_Massa']
       self.pXdict=copy.deepcopy(self.vCE.ProfilsDict['Иономер'][self.PrName]['pXdict'])
       self.PrDescr=self.vCE.ProfilsDict['Иономер'][self.PrName]['PrDescr']
       try:
         self.S_min=self.vCE.ProfilsDict['Иономер'][self.PrName]['S_min']
       except:
         self.S_min=57.0
         self.vCE.ProfilsDict['Иономер'][self.PrName]['S_min']=self.S_min
       q=0
       self.vCE._PrName=self.PrName    
       self.vCE.Ecm=self.Ecm
       self.vCE.Stc=self.Stc
       self.vCE.Kt=self.Kt
       self.vCE.pXu=self.pXu
       self.vCE.Tcb=self.Tcb
       self.vCE.Ion_Name=self.Ion_Name
       self.vCE.Ion_Val=self.Ion_Val
       self.vCE.Ion_Mol_Massa=self.Ion_Mol_Massa
       self.vCE.Ion_K=self.Ion_K
       self.vCE.S_min=self.S_min
       q=0

    def GetInfoProfil(self, index):
       self.CurrentProf=index

    def ChangeCurrProfil(self,Ecm=0.0, Stc=0.054153, Kt=1.9836e-4, pXu=7.0, Tcb=20.0, PrName='Pr1', PrDescr=' ',S_min=57.0 ):
       self.Ecm=Ecm
       self.Stc=Stc
       self.Kt=Kt
       self.pXu=pXu
       self.Tcb=Tcb
       self.PrName=PrName
       self.PrDescr=PrDescr
       self.S_min=S_min

    def SaveCurrProfil(self):
        if (self.CurrentProf==-1):
            self.CreateProfil()
            self.CurrentProf=self.Listcount-1
        else:
            self.ChangeProfil(self.CurrentProf)
        self.vCE.vCE.save_LocalProfil_state()

