
import logging
from PyQt4 import QtCore, QtGui 
from datetime import datetime

from common import *
from vp_classes import *
if PCFlag==1:
  from fpCond_1 import Ui_fpCond
  from fpCond_2 import Ui_fpCond_Compact
  from fpVATP import Ui_fpVATP
  from fmCondCalib1 import Ui_fmCondCalib
  from fmSelectProfil import Ui_fmSelectProfil
  from fmVPPassword import Ui_fmVPPassword
  from fmSelectV import Ui_fmSelectV
  from fmTKR import Ui_fmTKR
if PCFlag==2:
  from fpCond_1_t import Ui_fpCond
  from fpCond_2_t import Ui_fpCond_Compact
  from fpVATP_t import Ui_fpVATP
  from fmCondCalib1_t import Ui_fmCondCalib
  from fmSelectProfil_t import Ui_fmSelectProfil
  from fmVPPassword_t import Ui_fmVPPassword
  from fmSelectV_t import Ui_fmSelectV
  from fmTKR_t import Ui_fmTKR

from vinstr import *
#LL = logging.getLogger('SVI')



class CfpCond(QtGui.QMainWindow, Ui_fpCond):
  """ лицевая панель виртуального кислородомера """
  #  winCO_2  - экземпляр CfmO_2Calib - окно настройки кислородомера
  #  vO_2   - экземпляр виртуального кислородомера, соответствующий данной панели
  #  fFreeze - True - отключить обработку событий выпадающего списка профилей

  def __init__(self, vCond):
    super().__init__() 
    self.setupUi(self)
    self.fFreeze = False
    self.vCond = vCond
    rect = QtCore.QRect()   
    w=self.vCond.width 
    h=self.vCond.height
    x=self.vCond.x         
    y=self.vCond.y  
    rect = QtCore.QRect(x,y,w,h) 
    rect.setRect(x,y,w,h) 
    self.setGeometry(rect)
    self.lcdMain.setDigitCount(self.vCond.widthD + 1)
    self.lcdMain_2.setDigitCount(self.vCond.widthD + 1)
    self.lcdMain_3.setDigitCount(self.vCond.widthD + 1)
    
    self.vCond.ID_VP=self.vCond.dSize.setdefault('ID_VP','0')
    self.lblID.setText(str(self.vCond.ID_VP))


    self.Type=7
    self.edIndex=1;

    if self.vCond.fTech:   
      # виртуальный прибор запущен в технологическом режиме 
      self.actTech = QtGui.QAction("Отладка", self) 
      self.actTech.triggered.connect(self.on_muTech_toggle)  
      self.menubar.addAction(self.actTech)
    self.Reset_Flag=1
    #Дорбавка из профиля
    self.formpX = "{:5.2f}" 
    self.formE = "{:6.1f}"
    self.hint = QtCore.Qt.UserRole + 1 
    self.fFreeze = False
    self.lastPrInd = -1
    self.lastPrName = '' 
    self.stPrEd = 0
    self.fNewPr = False
    self.A=1
    self.A_mgdm3=1
    self.Ed_A=0

    self.rbManualT.toggled.connect(self.on_ManualT_toggle)
    self.rbOffT.toggled.connect(self.on_OffT_toggle)
    self.rbAutoT.toggled.connect(self.on_AutoT_toggle)
    self.tbEnterT.clicked.connect(self.on_tbEnterT_clicked) 
    self.rbAutoT.setChecked(True)
    self.tbSelectProfil.clicked.connect(self.on_tbSelectProfil_toggle)
    self.tbSaveToNotepad_.clicked.connect(self.on_tbSaveToNotepad_clicked) 

  def on_tbSaveToNotepad_clicked(self):
     if(Results.Result_Dict[self.vCond.Name]['В блокнот']==0):
        self.vCond.ID_VP=self.lblID.text()
        self.vCond.dSize['ID_VP']=self.vCond.ID_VP
        self.vCond.InLight_Notepad=1
     q=0 

  def show(self, newsize = None):
    """ newsize - экземпляр QSize для передачи новых размеров окна """
    super().show()   # важно выполнить ПЕРЕД resize - иначе resize может не пройти


  def closeEvent(self, event):
    self.vCond.ProfilsDict['Кондуктомер'][self.vCond.Name]['Текущий профмль']=self.vCond.Profils.PrName
    self.vCond.vCE.save_LocalProfil_state()
    self.vCond.SaveState()


    rect = self.geometry()
    self.vCond.dSize['x'] = rect.left()
    self.vCond.dSize['y'] = rect.top()
    self.vCond.dSize['height'] = rect.height() 
    self.vCond.dSize['width'] = rect.width()
    event.accept() 


  def on_muConf_toggle(self):
    smartShow(self.winCCond, self.vCond.profD, self.vCond.actPr, self.vCond)

  def on_tbSelectProfil_toggle(self):
      self.vCond.vCE.load_LocalProfil_state()
      self.vCond.winSelectProfil.show()
      w=0

  def on_muTech_toggle(self):
    #self.vCond.fDlog = not self.vCond.fDlog
    q=0


  def on_ManualT_toggle(self):
    if(self.vCond.ManualT_Flag==0):
       self.vCond.ManualT_Flag=1
       self.vCond.OffT_Flag=0
       self.vCond.AutoT_Flag=0
       self.leTemp.setReadOnly(False) 
       q=1
    q=0

  def on_OffT_toggle(self):
    if(self.vCond.OffT_Flag==0):
       self.vCond.OffT_Flag=1
       self.vCond.ManualT_Flag=0
       self.vCond.AutoT_Flag=0
       self.leTemp.setReadOnly(True) 
       q=1
    q=0

  def on_AutoT_toggle(self):
    if(self.vCond.AutoT_Flag==0):
       self.vCond.AutoT_Flag=1
       self.vCond.ManualT_Flag=0
       self.vCond.OffT_Flag=0
       self.leTemp.setReadOnly(True) 
       q=1 
    q=0

  def on_tbEnterT_clicked(self):
    if(self.vCond.ManualT_Flag==1):       
       self.vCond.T_curr= eval(self.leTemp.text(), {}, {})
       if((self.vCond.T_curr<-200.0)|(self.vCond.T_curr>200.0)):self.vCond.T_curr= 25.0 
       self.vCond.DispTemp(self.vCond.T_curr)
    q=0

  def on_leTempFinish(self):
    q=0

  def on_leA_Finish(self):
    try:
      self.vCond.Salt = eval(self.leSalt.text(), {}, {})
    except:
      LL.exception('') 
    self.leSalt.setText("{:5.2f}".format(self.vCond.Salt))
    self.leSalt.clearFocus()
    q=0
#Компактный вариант передней панели
class CfpCond_Compact(QtGui.QMainWindow, Ui_fpCond_Compact):
  """ лицевая панель виртуального кислородомера """
  #  winCO_2  - экземпляр CfmO_2Calib - окно настройки кислородомера
  #  vO_2   - экземпляр виртуального кислородомера, соответствующий данной панели
  #  fFreeze - True - отключить обработку событий выпадающего списка профилей

  def __init__(self, vCond):
    super().__init__() 
    self.setupUi(self)
    self.fFreeze = False
    self.vCond = vCond
    rect = QtCore.QRect()   
    w=self.vCond.width 
    h=self.vCond.height
    x=self.vCond.x         
    y=self.vCond.y  
    rect = QtCore.QRect(x,y,w,h) 
    rect.setRect(x,y,w,h) 
    self.setGeometry(rect)
    self.lcdMain.setDigitCount(5)
    self.lcdMain_2.setDigitCount(self.vCond.widthD + 1)
    self.lcdMain_3.setDigitCount(self.vCond.widthD + 1)
    
    self.vCond.ID_VP=self.vCond.dSize.setdefault('ID_VP','0')
    self.lblID.setText(str(self.vCond.ID_VP))
    self.lblID.clearFocus()

    self.Type=7
    self.edIndex=1;

    if self.vCond.fTech:   
      # виртуальный прибор запущен в технологическом режиме 
      self.actTech = QtGui.QAction("Отладка", self) 
      self.actTech.triggered.connect(self.on_muTech_toggle)  
      self.menubar.addAction(self.actTech)
    self.Reset_Flag=1
    #Дорбавка из профиля
    self.formpX = "{:5.2f}" 
    self.formE = "{:6.1f}"
    self.hint = QtCore.Qt.UserRole + 1 
    self.fFreeze = False
    self.lastPrInd = -1
    self.lastPrName = '' 
    self.stPrEd = 0
    self.fNewPr = False
    self.A=1
    self.A_mgdm3=1
    self.Ed_A=0

    self.rbManualT.toggled.connect(self.on_ManualT_toggle)
    self.rbOffT.toggled.connect(self.on_OffT_toggle)
    self.rbAutoT.toggled.connect(self.on_AutoT_toggle)
    self.tbEnterT.clicked.connect(self.on_tbEnterT_clicked) 
    self.rbAutoT.setChecked(True)
    #self.tbSelectProfil.clicked.connect(self.on_tbSelectProfil_toggle)
    self.tbSaveToNotepad_.clicked.connect(self.on_tbSaveToNotepad_clicked) 

  def on_tbSaveToNotepad_clicked(self):
     if(Results.Result_Dict[self.vCond.Name]['В блокнот']==0):
        self.vCond.ID_VP=self.lblID.text()
        self.vCond.dSize['ID_VP']=self.vCond.ID_VP
        self.vCond.InLight_Notepad=1
     q=0 

  def show(self, newsize = None):
    """ newsize - экземпляр QSize для передачи новых размеров окна """
    super().show()   # важно выполнить ПЕРЕД resize - иначе resize может не пройти

  def closeEvent(self, event):
    self.vCond.ProfilsDict['Кондуктомер'][self.vCond.Name]['Текущий профмль']=self.vCond.Profils.PrName
    self.vCond.vCE.save_LocalProfil_state()
    self.vCond.SaveState()

    rect = self.geometry()
    self.vCond.dSize['x'] = rect.left()
    self.vCond.dSize['y'] = rect.top()
    self.vCond.dSize['height'] = rect.height() 
    self.vCond.dSize['width'] = rect.width()
    event.accept() 


  def on_muConf_toggle(self):
    smartShow(self.winCCond, self.vCond.profD, self.vCond.actPr, self.vCond)

  def on_tbSelectProfil_toggle(self):
      self.vCond.vCE.load_LocalProfil_state()
      self.vCond.winSelectProfil.show()
      w=0

  def on_muTech_toggle(self):
    #self.vCond.fDlog = not self.vCond.fDlog
    q=0


  def on_ManualT_toggle(self):
    if(self.vCond.ManualT_Flag==0):
       self.vCond.ManualT_Flag=1
       self.vCond.OffT_Flag=0
       self.vCond.AutoT_Flag=0
       self.leTemp.setReadOnly(False) 
       q=1
    q=0

  def on_OffT_toggle(self):
    if(self.vCond.OffT_Flag==0):
       self.vCond.OffT_Flag=1
       self.vCond.ManualT_Flag=0
       self.vCond.AutoT_Flag=0
       self.leTemp.setReadOnly(True) 
       q=1
    q=0

  def on_AutoT_toggle(self):
    if(self.vCond.AutoT_Flag==0):
       self.vCond.AutoT_Flag=1
       self.vCond.ManualT_Flag=0
       self.vCond.OffT_Flag=0
       self.leTemp.setReadOnly(True) 
       q=1 
    q=0

  def on_tbEnterT_clicked(self):
    if(self.vCond.ManualT_Flag==1):       
       self.vCond.T_curr= eval(self.leTemp.text(), {}, {})
       if((self.vCond.T_curr<-200.0)|(self.vCond.T_curr>200.0)):self.vCond.T_curr= 25.0 
       self.vCond.DispTemp(self.vCond.T_curr)
    q=0

  def on_leTempFinish(self):
    q=0

  def on_leA_Finish(self):
    try:
      self.vCond.Salt = eval(self.leSalt.text(), {}, {})
    except:
      LL.exception('') 
    self.leSalt.setText("{:5.2f}".format(self.vCond.Salt))
    self.leSalt.clearFocus()
    q=0
# Конец компактного варианта передней панели

#Компактный вариант передней панели 2
class CfpCond_Compact_2(QtGui.QMainWindow, Ui_fpCond_Compact):
  """ лицевая панель виртуального кислородомера """
  #  winCO_2  - экземпляр CfmO_2Calib - окно настройки кислородомера
  #  vO_2   - экземпляр виртуального кислородомера, соответствующий данной панели
  #  fFreeze - True - отключить обработку событий выпадающего списка профилей #FEABA7

  def __init__(self, vCond):
    super().__init__() 
    self.setupUi(self)
    self.setStyleSheet("QMainWindow {background: '#FEABA7';}")
    self.fFreeze = False
    self.vCond = vCond
    rect = QtCore.QRect()   
    w=self.vCond.width 
    h=self.vCond.height
    x=self.vCond.x         
    y=self.vCond.y  
    rect = QtCore.QRect(x,y,w,h) 
    rect.setRect(x,y,w,h) 
    self.setGeometry(rect)
    self.lcdMain.setDigitCount(5)
    self.lcdMain_2.setDigitCount(5)
    self.lcdMain_3.setDigitCount(5)
    
    self.vCond.ID_VP=self.vCond.dSize.setdefault('ID_VP','0')
    self.lblID.setText(str(self.vCond.ID_VP))
    #self.leID.setText(str(self.vCond.ID_VP))
    #self.leID.clearFocus()

    self.Type=7
    self.edIndex=1;

    if self.vCond.fTech:   
      # виртуальный прибор запущен в технологическом режиме 
      self.actTech = QtGui.QAction("Отладка", self) 
      self.actTech.triggered.connect(self.on_muTech_toggle)  
      self.menubar.addAction(self.actTech)
    self.Reset_Flag=1
    #Дорбавка из профиля
    self.formpX = "{:5.2f}" 
    self.formE = "{:6.1f}"
    self.hint = QtCore.Qt.UserRole + 1 
    self.fFreeze = False
    self.lastPrInd = -1
    self.lastPrName = '' 
    self.stPrEd = 0
    self.fNewPr = False
    self.A=1
    self.A_mgdm3=1
    self.Ed_A=0
    # Menu Profile
    self.actTech = QtGui.QAction("Профиль", self) 
    self.actTech.triggered.connect(self.on_tbSelectProfil_toggle)  
    self.menubar.addAction(self.actTech)
    # Menu V-vo
    self.actTech = QtGui.QAction("Вещество", self) 
    self.actTech.triggered.connect(self.on_tbSelectV_toggle)  
    self.menubar.addAction(self.actTech)
    # Menu АТК
    self.actTech = QtGui.QAction("Тип АТК", self) 
    self.actTech.triggered.connect(self.on_tbSelectATK_toggle)  
    self.menubar.addAction(self.actTech)
    # Common menu of VP
    self.actTech = QtGui.QAction("Проба", self) 
    self.actTech.triggered.connect(self.on_Proba_toggle)  
    self.menubar.addAction(self.actTech)

    self.actTech = QtGui.QAction("О приборе", self) 
    self.actTech.triggered.connect(self.on_AboutVP_toggle)  
    self.menubar.addAction(self.actTech)
    ## End of common menu of VP
    if(self.vCond.fpCond_Version==1):
      self.rbManualT.toggled.connect(self.on_ManualT_toggle)
      self.rbOffT.toggled.connect(self.on_OffT_toggle)
      self.rbAutoT.toggled.connect(self.on_AutoT_toggle)
      self.tbEnterT.clicked.connect(self.on_tbEnterT_clicked) 
      self.rbAutoT.setChecked(True)
    #self.tbSelectProfil.clicked.connect(self.on_tbSelectProfil_toggle)
    self.tbSaveToNotepad_.clicked.connect(self.on_tbSaveToNotepad_clicked) 
    self.lcdMain.setStyleSheet("QLabel { background-color : darkCyan; color : black; }");
    #self.lblEd.setStyleSheet("QLabel { background-color : darkCyan; color : black; }");
    q=0

  def on_tbSaveToNotepad_clicked(self):
     if(Results.Result_Dict[self.vCond.Name]['В блокнот']==0):
        #self.vCond.winMessage.tbMessage.clear()
        #self.vCond.winMessage.tbMessage.setText('Введите идентификатор пробы, отличный от нуля!')
        #self.vCond.winMessage.show()
        self.vCond.ID_VP=self.lblID.text()
        self.vCond.dSize['ID_VP']=self.vCond.ID_VP
        self.vCond.InLight_Notepad=1
     q=0 

  def show(self, newsize = None):
    """ newsize - экземпляр QSize для передачи новых размеров окна """
    super().show()   # важно выполнить ПЕРЕД resize - иначе resize может не пройти

  def closeEvent(self, event):
    self.vCond.ProfilsDict['Кондуктомер'][self.vCond.Name]['Текущий профмль']=self.vCond.Profils.PrName
    self.vCond.vCE.save_LocalProfil_state()
    self.vCond.SaveState()

    rect = self.geometry()
    self.vCond.dSize['x'] = rect.left()
    self.vCond.dSize['y'] = rect.top()
    self.vCond.dSize['height'] = rect.height() 
    self.vCond.dSize['width'] = rect.width()
    event.accept() 


  def on_muConf_toggle(self):
    smartShow(self.winCCond, self.vCond.profD, self.vCond.actPr, self.vCond)

  def on_tbSelectProfil_toggle(self):
      if(self.vCond.vCE.OpenProfilVP_1Flag==0)&(self.vCond.vCE.OpenProfilVP_2Flag==0):
        self.vCond.vCE.OpenProfilVP_1Flag=1
        self.vCond.vCE.load_LocalProfil_state()
        self.vCond.winSelectProfil.show()
        w=0

  def on_tbSelectV_toggle(self):
      #self.vCond.vCE.load_LocalProfil_state()
      self.vCond.winSelectV.show(1)
      w=0

  def on_tbSelectATK_toggle(self):
      #self.vCond.vCE.load_LocalProfil_state()
      self.vCond.winTKR.show(1)
      w=0

  def on_Proba_toggle(self):
      self.vCond.winProbaID.show()
      w=0

  def on_AboutVP_toggle(self):
      self.vCond.winAboutVP.show()
      w=0

  def on_muTech_toggle(self):
    #self.vCond.fDlog = not self.vCond.fDlog
    q=0


  def on_ManualT_toggle(self):
    if(self.vCond.ManualT_Flag==0):
       self.vCond.ManualT_Flag=1
       self.vCond.OffT_Flag=0
       self.vCond.AutoT_Flag=0
       self.leTemp.setReadOnly(False) 
       q=1
    q=0

  def on_OffT_toggle(self):
    if(self.vCond.OffT_Flag==0):
       self.vCond.OffT_Flag=1
       self.vCond.ManualT_Flag=0
       self.vCond.AutoT_Flag=0
       self.leTemp.setReadOnly(True) 
       q=1
    q=0

  def on_AutoT_toggle(self):
    if(self.vCond.AutoT_Flag==0):
       self.vCond.AutoT_Flag=1
       self.vCond.ManualT_Flag=0
       self.vCond.OffT_Flag=0
       self.leTemp.setReadOnly(True) 
       q=1 
    q=0

  def on_tbEnterT_clicked(self):
    if(self.vCond.ManualT_Flag==1):       
       self.vCond.T_curr= eval(self.leTemp.text(), {}, {})
       if((self.vCond.T_curr<-200.0)|(self.vCond.T_curr>200.0)):self.vCond.T_curr= 25.0 
       self.vCond.DispTemp(self.vCond.T_curr)
    q=0

  def on_leTempFinish(self):
    q=0

  def on_leA_Finish(self):
    try:
      self.vCond.Salt = eval(self.leSalt.text(), {}, {})
    except:
      LL.exception('') 
    self.leSalt.setText("{:5.2f}".format(self.vCond.Salt))
    self.leSalt.clearFocus()
    q=0
# Конец компактного варианта передней панели 2

class CfmSelectProfil(QtGui.QMainWindow, Ui_fmSelectProfil): 
  """ окно выбора профиля виртуального кондуктомера"""


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

  def closeEvent(self, event):
    self.vCond.vCE.OpenProfilVP_1Flag=0
    self.vCond.vCE.save_LocalProfil_state()
    self.close()
    s=0

  def on_tbAddProfil_toggle(self):
     self.vCond.Profils.CurrentProf=-1
     self.vCond.winCCond.show(0,0,0)
     return 0

  def InitProfilsList(self):
     self.vCond.Profils.Listcount=self.vCond.ProfilsDict['Кондуктомер']['Listcount']
     tmpCnt=self.vCond.Profils.Listcount
     tmpNum=0
     self.lwProfils_.clear()
     while (tmpNum<tmpCnt):
         self.lwProfils_.addItem(self.vCond.ProfilsDict['Кондуктомер']['List'][tmpNum])
         tmpNum=tmpNum+1
     return 0
       # self.vCE.ProfilsDict['Кондуктомер']['Listcount']=self.Listcount

  def InitProfilsList1(self):
     self.vCond.Profils.Listcount=self.vCond.ProfilsDict['Кондуктомер']['Listcount']
     tmpCnt=self.vCond.Profils.Listcount
     tmpNum=0
     self.lwProfils_.clear()
     while (tmpNum<tmpCnt):
         self.lwProfils_.addItem(self.vCond.ProfilsDict['Кондуктомер']['List'][tmpNum])
         tmpNum=tmpNum+1
     return 0

  def on_tbSelectProfil_toggle(self):
     i=0
     a=self.lwProfils_.currentRow()
     self.vCond.Profils.SelectProfil(a)
     self.vCond.win.lblProfilName.setText(self.vCond.Profils.PrName)
     self.vCond.win.label_8.setText(self.vCond.Profils.V_vo + "  "+str(self.vCond.Profils.TK_V_vo)+ "% "+str(self.vCond.Profils.T_ATK)+ " oC" )
     self.close()
     return 0

  def on_tbChangeProfil(self):
     i=0
     a=self.lwProfils_.currentRow()
     self.vCond.Profils.SelectProfil(a)
     self.vCond.winCCond.show(0,0,0)
     return 0
 
  def on_tbDelProfil(self):
     i=0
     a=self.lwProfils_.currentRow()
     self.vCond.Profils.DelProfil(a)
     self.InitProfilsList()
     return 0
   
  def on_lwProfils_Change(self):
     i=0
     a=self.lwProfils_.currentRow()
     self.vCond.Profils.SelectedProfilNum=a
     return 0

  def on_lwProfils_doubleClicked(self):
     self.vCond.winCCond.show(0,0,0)
     return 0

  def on_lwProfils_clicked(self):
     a=self.lwProfils_.currentRow()
     self.vCond.Profils.SelectProfil(a)
     tmptxt=self.vCond.Profils.PrDescr
     self.tbDescribeProfil.setText(tmptxt)
     return 0

'''

class CfmCondCalib(QtGui.QMainWindow, Ui_fmCondCalib): 
  """ окно калибровки виртуального кондуктомера (характеризация электродов) """
#
  def __init__(self, vCond):
     
    super().__init__()
    self.setupUi(self)
    self.vCond = vCond
    self.ShowFlag=0
 
    self.leB_.valueChanged.connect(self.on_Change_Any) 
    self.leKu_.valueChanged.connect(self.on_Change_Any) 
    self.leKu_1_.valueChanged.connect(self.on_Change_Any) 
    self.leKu_2_.valueChanged.connect(self.on_Change_Any) 
    self.leKu_3_.valueChanged.connect(self.on_Change_Any) 
    self.leKu_4_.valueChanged.connect(self.on_Change_Any) 
    self.leKu_5_.valueChanged.connect(self.on_Change_Any) 
    self.leKu_6_.valueChanged.connect(self.on_Change_Any) 
    self.leDescr_.textChanged.connect(self.on_Change_Any) 
    self.tbSaveCalib_.clicked.connect(self.on_tbSaveCalib_toggle) 
    self.chbBKd.stateChanged.connect(self.on_chbBKd_checked)

  def show(self, profD, actPr, vCond): 
    self.on_Init_Any()
    self.ShowFlag=1
    self.chbBKd.setChecked(False)
    self.gbxBKd.setEnabled(False)
    super().show()

  def closeEvent(self, event):
    self.ShowFlag=0
    #self.vCond.vCE.wi
    self.vCond.ProfilsDict['Кондуктомер'][self.vCond.Name]['Текущий профмль']=self.vCond.Profils.PrName
    self.vCond.vCE.save_LocalProfil_state()
    self.vCond.SaveState()

    rect = self.geometry()
    self.vCond.dSize['x'] = rect.left()
    self.vCond.dSize['y'] = rect.top()
    self.vCond.dSize['height'] = rect.height() 
    self.vCond.dSize['width'] = rect.width()
    event.accept()

  def on_chbBKd_checked(self):      
      if (self.chbBKd.checkState()):self.vCond.winCondPassword.show() #self.gbxBKd.setEnabled(True)
      else: self.gbxBKd.setEnabled(False)

  def on_tbSaveCalib_toggle(self):
    """ сохранение профиля иономера """
    if(self.ShowFlag==1):
      self.on_Change_Any()
      self.vCond.Profils.SaveCurrProfil()
      self.leProfilName_.setText(self.vCond.Profils.PrName)
      self.vCond.winSelectProfil.InitProfilsList()
      q=0

  def on_Change_Any(self):
      if(self.ShowFlag==1):
        B=0.0
        Kya=0.0
        Kd1=0.0
        Kd2=0.0
        Kd3=0.0
        Kd4=0.0
        Kd5=0.0
        Kd6=0.0
        B=self.leB_.value()
        Kya=self.leKu_.value()
        Kd1=self.leKu_1_.value()
        Kd2=self.leKu_2_.value()
        Kd3=self.leKu_3_.value()
        Kd4=self.leKu_4_.value()
        Kd5=self.leKu_5_.value()
        Kd6=self.leKu_6_.value()
        PrName=self.leProfilName_.text()
        PrDescr=self.leDescr_.text()
        self.vCond.Profils.ChangeCurrProfil(B, Kya, Kd1, Kd2, Kd3, Kd4, Kd5, Kd6, PrName, PrDescr)

  def on_Init_Any(self):
      self.leB_.setValue(self.vCond.Profils.B)
      self.leKu_.setValue(self.vCond.Profils.Kya)
      self.leKu_1_.setValue(self.vCond.Profils.Kd1)
      self.leKu_2_.setValue(self.vCond.Profils.Kd2)
      self.leKu_3_.setValue(self.vCond.Profils.Kd2)
      self.leKu_4_.setValue(self.vCond.Profils.Kd4)
      self.leKu_5_.setValue(self.vCond.Profils.Kd5)
      self.leKu_6_.setValue(self.vCond.Profils.Kd6)
      a=self.vCond.Profils.PrName
      self.leProfilName_.setText(a)
      b=self.vCond.Profils.PrDescr
      self.leDescr_.setText(b)
      self.leB_.setFocus()


class CProfils():

    def __init__(self,profils={}):
       b=0
       self.profs=profils
       self.profs.setdefault('Listcount',0)
       self.profs.setdefault('List',{})
       self.Listcount=self.profs['Listcount']
       self.CurrentProf=-1
       self.B=0
       self.Kya=0
       self.Kd1=1.0
       self.Kd2=1.0
       self.Kd3=1.0
       self.Kd4=1.0
       self.Kd5=1.0
       self.Kd6=1.0
       self.PrName=''
       self.PrDescr=''

    def LoadProfilsList(self):
       tmpi=0
       tmpl=[]
       while tmpi<self.Listcount-1:
           tmpl.append(self.profs['List'][tmpi])
       return tmpl
 
    def CreateProfil(self):
       tmpname=self.PrName
       tmpNum=0
       tmpi=0
       while (tmpi<self.Listcount-1):
          if(tmpNum>0):tmpnameNum=tmpname+tmpNum 
          else: tmpnameNum=tmpname 
          if (self.profs['List'][tmpi]==tmpnameNum):
              tmpNum=tmpNum+1
              tmpi=0
       self.profs['List'].setdefault(str(tmpnameNum),{})
       self.Listcount=self.Listcount+1
       self.profs['Listcount']=self.Listcount
       self.profs[self.PrName]['B']=self.B
       self.profs[self.PrName]['Kya']=self.Kya
       self.profs[self.PrName]['Kd1']=self.Kd1
       self.profs[self.PrName]['Kd2']=self.Kd2
       self.profs[self.PrName]['Kd3']=self.Kd3
       self.profs[self.PrName]['Kd4']=self.Kd4
       self.profs[self.PrName]['Kd5']=self.Kd5
       self.profs[self.PrName]['Kd6']=self.Kd6
       self.profs[self.PrName]['PrDescr']=self.PrDescr

    def DelProfil(self, index):
       tmpi=0
       tmpname=self.profs['List'][index]
       del self.profs['tmpname']
       tmpi=index
       while (tmpi<self.Listcount-2):
          self.profs['List'][index]=self.profs['List'][index+1]

       del self.profs['List'][self.Listcount-1]
       self.Listcount=self.Listcount-1
       self.profs['Listcount']=self.Listcount

    def ChangeProfil(self, index):
       self.CurrentProf=index
       self.Listcount=self.profs['Listcount']
       if(self.profs['List'][self.CurrentProf]!=self.PrName):
         self.profs['List'][self.CurrentProf]={}
         del self.profs[self.PrName]  
       else:
         self.profs[self.PrName]['B']=self.B
         self.profs[self.PrName]['Kya']=self.Kya
         self.profs[self.PrName]['Kd1']=self.Kd1
         self.profs[self.PrName]['Kd2']=self.Kd2
         self.profs[self.PrName]['Kd3']=self.Kd3
         self.profs[self.PrName]['Kd4']=self.Kd4
         self.profs[self.PrName]['Kd5']=self.Kd5
         self.profs[self.PrName]['Kd6']=self.Kd6
         self.profs[self.PrName]['PrDescr']=self.PrDescr

    def SelectProfil(self, index):
       self.CurrentProf=index
       self.Listcount=self.profs['Listcount']
       self.PrName=self.profs['List'][self.CurrentProf]
       self.B=self.profs[self.PrName]['B']
       self.Kya=self.profs[self.PrName]['Kya']
       self.Kd1=self.profs[self.PrName]['Kd1']
       self.Kd2=self.profs[self.PrName]['Kd2']
       self.Kd3=self.profs[self.PrName]['Kd3']
       self.Kd4=self.profs[self.PrName]['Kd4']
       self.Kd5=self.profs[self.PrName]['Kd5']
       self.Kd6=self.profs[self.PrName]['Kd6']
       self.PrDescr=self.profs[self.PrName]['PrDescr']

    def GetInfoProfil(self, index):
       self.CurrentProf=index

    def ChangeCurrProfil(self, B=0.0, Kya=0.0, Kd1=1.0, Kd2=1.0, Kd3=1.0, Kd4=1.0, Kd5=1.0, Kd6=1.0, PrName='Pr1', PrDescr=' ' ):
       self.B=B
       self.Kya=Kya
       self.Kd1=Kd1
       self.Kd2=Kd2
       self.Kd3=Kd3
       self.Kd4=Kd4
       self.Kd5=Kd5
       self.Kd6=Kd6
       self.PrName=PrName
       self.PrDescr=PrDescr

    def SaveCurrProfil(self):
        if (self.CurrentProf==-1):
            self.CreateProfil()
        else:
            self.ChangeProfil()

class CProfilsC():

    def __init__(self, vCE, profils={}):
       b=0
       self.profs=profils
       self.vCE=vCE
       self.vCE.ProfilsDict['Кондуктомер'].setdefault('Listcount',0)
       self.vCE.ProfilsDict['Кондуктомер'].setdefault('List',{})
       #self.vCE.ProfilsDict['Кондуктомер']['Listcount']=4
       self.Listcount=self.vCE.ProfilsDict['Кондуктомер']['Listcount']
       self.CurrentProf=-1
       self.B=0
       self.Kya=1.0
       self.Kd1=1.0
       self.Kd2=1.0
       self.Kd3=1.0
       self.Kd4=1.0
       self.Kd5=1.0
       self.Kd6=1.0
       self.PrName=''
       self.PrDescr=''
       self.SelectedProfilNum=-1

    def LoadProfilsList(self):
       tmpi=0
       tmpl=[]
       while tmpi<self.Listcount-1:
           tmpl.append(self.vCE.ProfilsDict['Кондуктомер']['List'][tmpi])
       return tmpl
 
    def LoadProfil(self,prName=''):
        tmpname=self.PrName
        tmpNum=0
        tmpi=0
        if(self.Listcount==0):
           self.B=1
           self.Kya=1
           self.Kd1=1
           self.Kd2=1
           self.Kd3=1
           self.Kd4=1
           self.Kd5=1
           self.Kd6=1
           self.PrName='(нет)'
           self.vCE._PrName=self.PrName    
           self.vCE._B=self.B
           self.vCE._Ku=self.Kya
           self.vCE._Kdu1=self.Kd1
           self.vCE._Kdu2=self.Kd2
           self.vCE._Kdu3=self.Kd3
           self.vCE._Kdu4=self.Kd4
           self.vCE._Kdu5=self.Kd5
           self.vCE._Kdu6=self.Kd6
        tmpi=0
        if(self.Listcount>0):
           while (tmpi<self.Listcount): 
             if (self.vCE.ProfilsDict['Кондуктомер']['List'][tmpi]==prName):
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
          if (self.vCE.ProfilsDict['Кондуктомер']['List'][tmpi]==tmpnameNum):
              tmpNum=tmpNum+1
              tmpi=0
          tmpi=tmpi+1
       self.PrName=tmpnameNum
       self.vCE.ProfilsDict['Кондуктомер']['List'][self.Listcount]=str(self.PrName)
       self.Listcount=self.Listcount+1
       self.vCE.ProfilsDict['Кондуктомер']['Listcount']=self.Listcount
       self.vCE.ProfilsDict['Кондуктомер'][self.PrName]={}
       self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['B']=self.B
       self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['Kya']=self.Kya
       self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['Kd1']=self.Kd1
       self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['Kd2']=self.Kd2
       self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['Kd3']=self.Kd3
       self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['Kd4']=self.Kd4
       self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['Kd5']=self.Kd5
       self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['Kd6']=self.Kd6
       self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['PrDescr']=self.PrDescr
       

    def DelProfil(self, index):
       tmpi=0
       tmpname=self.vCE.ProfilsDict['Кондуктомер']['List'][index]
       del self.vCE.ProfilsDict['Кондуктомер'][tmpname]
       tmpi=index
       while (tmpi<=self.Listcount-2):
          self.vCE.ProfilsDict['Кондуктомер']['List'][tmpi]=self.vCE.ProfilsDict['Кондуктомер']['List'][tmpi+1]
          tmpi=tmpi+1
       #while (tmpi<self.Listcount-1):#
       del self.vCE.ProfilsDict['Кондуктомер']['List'][self.Listcount-1]
       self.Listcount=self.Listcount-1
       self.vCE.ProfilsDict['Кондуктомер']['Listcount']=self.Listcount

    def ChangeProfil(self, index=-1):
       self.CurrentProf=index
       if(self.CurrentProf!=-1):
         self.Listcount=self.vCE.ProfilsDict['Кондуктомер']['Listcount']
         if(self.vCE.ProfilsDict['Кондуктомер']['List'][self.CurrentProf]!=self.PrName):
           self.vCE.ProfilsDict['Кондуктомер']['List'][self.CurrentProf]={}
           del self.vCE.ProfilsDict['Кондуктомер'][self.PrName]  
         else:
           self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['B']=self.B
           self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['Kya']=self.Kya
           self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['Kd1']=self.Kd1
           self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['Kd2']=self.Kd2
           self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['Kd3']=self.Kd3
           self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['Kd4']=self.Kd4
           self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['Kd5']=self.Kd5
           self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['Kd6']=self.Kd6
           self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['PrDescr']=self.PrDescr

    def SelectProfil(self, index):
       self.CurrentProf=index
       self.Listcount=self.vCE.ProfilsDict['Кондуктомер']['Listcount']
       tmpa=self.vCE.ProfilsDict['Кондуктомер']['List'][self.CurrentProf]
       self.PrName=tmpa
       self.B=self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['B']
       self.Kya=self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['Kya']
       self.Kd1=self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['Kd1']
       self.Kd2=self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['Kd2']
       self.Kd3=self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['Kd3']
       self.Kd4=self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['Kd4']
       self.Kd5=self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['Kd5']
       self.Kd6=self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['Kd6']

       self.PrDescr=self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['PrDescr']
       q=0
       self.vCE._PrName=self.PrName    
       self.vCE._B=self.B
       self.vCE._Ku=self.Kya
       self.vCE._Kdu1=self.Kd1
       self.vCE._Kdu2=self.Kd2
       self.vCE._Kdu3=self.Kd3
       self.vCE._Kdu4=self.Kd4
       self.vCE._Kdu5=self.Kd5
       self.vCE._Kdu6=self.Kd6

    def GetInfoProfil(self, index):
       self.CurrentProf=index

    def ChangeCurrProfil(self, B=0.0, Kya=0.0, Kd1=1.0, Kd2=1.0, Kd3=1.0, Kd4=1.0, Kd5=1.0, Kd6=1.0, PrName='Pr1', PrDescr=' ' ):

       self.B=B
       self.Kya=Kya
       self.Kd1=Kd1
       self.Kd2=Kd2
       self.Kd3=Kd3
       self.Kd4=Kd4
       self.Kd5=Kd5
       self.Kd6=Kd6
       self.PrName=PrName
       self.PrDescr=PrDescr

    def SaveCurrProfil(self):
        if (self.CurrentProf==-1):
            self.CreateProfil()
            self.CurrentProf=self.Listcount-1
        else:
            self.ChangeProfil(self.CurrentProf)

        self.vCE.vCE.save_LocalProfil_state()

'''



class CfmCondCalib(QtGui.QMainWindow, Ui_fmCondCalib): 
  """ окно калибровки виртуального кондуктомера (характеризация электродов) """
#
  def __init__(self, vCond):
     
    super().__init__()
    self.setupUi(self)
    self.vCond = vCond
    self.ShowFlag=0
    self.gbxBKd.setEnabled(False)
    self.leCondSet.setEnabled(False)
    self.lblKD6_2.setEnabled(False)
    self.tbRecalc.setEnabled(False)
    if PCFlag==1:
      self.leB_1.valueChanged.connect(self.on_Change_Any) 
      self.leB_2.valueChanged.connect(self.on_Change_Any)
      self.leB_3.valueChanged.connect(self.on_Change_Any)
      self.leB_4.valueChanged.connect(self.on_Change_Any)
      self.leB_5.valueChanged.connect(self.on_Change_Any)
      self.leB_6.valueChanged.connect(self.on_Change_Any)
      self.leA_1.valueChanged.connect(self.on_Change_Any)
      self.leA_2.valueChanged.connect(self.on_Change_Any)
      self.leA_3.valueChanged.connect(self.on_Change_Any)
      self.leA_4.valueChanged.connect(self.on_Change_Any)
      self.leA_5.valueChanged.connect(self.on_Change_Any)
      self.leA_6.valueChanged.connect(self.on_Change_Any)
      self.leKu_.valueChanged.connect(self.on_Change_Any) 
      self.leKu_1_.valueChanged.connect(self.on_Change_Any) 
      self.leKu_2_.valueChanged.connect(self.on_Change_Any) 
      self.leKu_3_.valueChanged.connect(self.on_Change_Any) 
      self.leKu_4_.valueChanged.connect(self.on_Change_Any) 
      self.leKu_5_.valueChanged.connect(self.on_Change_Any) 
      self.leKu_6_.valueChanged.connect(self.on_Change_Any) 
    if PCFlag==2: 
      self.leB_1.textChanged.connect(self.on_Change_Any) 
      self.leB_2.textChanged.connect(self.on_Change_Any)
      self.leB_3.textChanged.connect(self.on_Change_Any)
      self.leB_4.textChanged.connect(self.on_Change_Any)
      self.leB_5.textChanged.connect(self.on_Change_Any)
      self.leB_6.textChanged.connect(self.on_Change_Any)
      self.leA_1.textChanged.connect(self.on_Change_Any)
      self.leA_2.textChanged.connect(self.on_Change_Any)
      self.leA_3.textChanged.connect(self.on_Change_Any)
      self.leA_4.textChanged.connect(self.on_Change_Any)
      self.leA_5.textChanged.connect(self.on_Change_Any)
      self.leA_6.textChanged.connect(self.on_Change_Any)
      self.leKu_.textChanged.connect(self.on_Change_Any) 
      #self.leKu_.
      self.leKu_1_.textChanged.connect(self.on_Change_Any) 
      self.leKu_2_.textChanged.connect(self.on_Change_Any) 
      self.leKu_3_.textChanged.connect(self.on_Change_Any) 
      self.leKu_4_.textChanged.connect(self.on_Change_Any) 
      self.leKu_5_.textChanged.connect(self.on_Change_Any) 
      self.leKu_6_.textChanged.connect(self.on_Change_Any) 
    
    self.leDescr_.textChanged.connect(self.on_Change_Any) 
    self.leCond_min.textChanged.connect(self.on_Change_Any) 
    self.leCond_max.textChanged.connect(self.on_Change_Any) 
    self.tbSaveCalib_.clicked.connect(self.on_tbSaveCalib_toggle) 
    self.chbBKd.stateChanged.connect(self.on_chbBKd_checked)
    self.tbRecalc.clicked.connect(self.on_tbRecalc_toggle) 

  def show(self, profD, actPr, vCond): 
    if(self.vCond.vCE.OpenProfilVP_2Flag==0):
      self.on_Init_Any()
      self.ShowFlag=1
      self.chbBKd.setChecked(False)
      self.gbxBKd.setEnabled(False)
      self.leCondSet.setEnabled(False)
      self.lblKD6_2.setEnabled(False)
      self.tbRecalc.setEnabled(False)
      super().show()
      self.vCond.vCE.OpenProfilVP_2Flag=1


  def closeEvent(self, event):
    self.ShowFlag=0
    self.vCond.vCE.OpenProfilVP_2Flag=0

  def on_tbRecalc_toggle(self):
    """ сохранение профиля иономера on_tbRecalc_toggle"""
    self.vCond.tmpX_Set=float(self.leCondSet.text())
    q=0

  def on_chbBKd_checked(self):
      if (self.chbBKd.checkState()):self.vCond.winCondPassword.show() #self.gbxBKd.setEnabled(True)
      else: 
          self.gbxBKd.setEnabled(False)
          self.leCondSet.setEnabled(False)
          self.lblKD6_2.setEnabled(False)
          self.tbRecalc.setEnabled(False)

  def on_tbSaveCalib_toggle(self):
    """ сохранение профиля иономера """
    if(self.ShowFlag==1):
      self.on_Change_Any()
      self.vCond.Profils.SaveCurrProfil()
      self.leProfilName_.setText(self.vCond.Profils.PrName)
      self.vCond.winSelectProfil.InitProfilsList()
      q=0

  def on_Change_Any(self):
      if(self.ShowFlag==1):
        B=0.0
        Kya=0.0
        Kd1=0.0
        Kd2=0.0
        Kd3=0.0
        Kd4=0.0
        Kd5=0.0
        Kd6=0.0
        B1=0.0
        B2=0.0
        B3=0.0
        B4=0.0
        B5=0.0
        B6=0.0

        A1=0.0
        A2=0.0
        A3=0.0
        A4=0.0
        A5=0.0
        A6=0.0
        Cond_min=0.0
        Cond_max=0.0
        #B=self.leB_.value()
        if PCFlag==1:
          Kya=self.leKu_.value()
          Kd1=self.leKu_1_.value()
          Kd2=self.leKu_2_.value()
          Kd3=self.leKu_3_.value()
          Kd4=self.leKu_4_.value()
          Kd5=self.leKu_5_.value()
          Kd6=self.leKu_6_.value()
          B1=self.leB_1.value()
          B2=self.leB_2.value()
          B3=self.leB_3.value()
          B4=self.leB_4.value()
          B5=self.leB_5.value()   
          B6=self.leB_6.value()
          A1=self.leA_1.value()
          A2=self.leA_2.value()
          A3=self.leA_3.value()
          A4=self.leA_4.value()
          A5=self.leA_5.value()
          A6=self.leA_6.value()
        if PCFlag==2:
          Kya=float(self.leKu_.text())
          Kd1=float(self.leKu_1_.text())
          Kd2=float(self.leKu_2_.text())
          Kd3=float(self.leKu_3_.text())
          Kd4=float(self.leKu_4_.text())
          Kd5=float(self.leKu_5_.text())
          Kd6=float(self.leKu_6_.text())
          B1=float(self.leB_1.text())
          B2=float(self.leB_2.text())
          B3=float(self.leB_3.text())
          B4=float(self.leB_4.text())
          B5=float(self.leB_5.text())   
          B6=float(self.leB_6.text())
          A1=float(self.leA_1.text())
          A2=float(self.leA_2.text())
          A3=float(self.leA_3.text())
          A4=float(self.leA_4.text())
          A5=float(self.leA_5.text())
          A6=float(self.leA_6.text())
        Cond_min=float(self.leCond_min.text())
        Cond_max=float(self.leCond_max.text())
        PrName=self.leProfilName_.text()
        PrDescr=self.leDescr_.text()
        self.vCond.Profils.ChangeCurrProfil(B, Kya, Kd1, Kd2, Kd3, Kd4, Kd5, Kd6, PrName, PrDescr,B1,B2,B3,B4,B5,B6,A1,A2,A3,A4,A5,A6,Cond_min,Cond_max)




  def on_Init_Any(self):
      if PCFlag==1:
       #self.leB_.setValue(self.vCond.Profils.B)
       self.leKu_.setValue(self.vCond.Profils.Kya)
       self.leKu_1_.setValue(self.vCond.Profils.Kd1)
       self.leKu_2_.setValue(self.vCond.Profils.Kd2)
       self.leKu_3_.setValue(self.vCond.Profils.Kd3)
       self.leKu_4_.setValue(self.vCond.Profils.Kd4)
       self.leKu_5_.setValue(self.vCond.Profils.Kd5)
       self.leKu_6_.setValue(self.vCond.Profils.Kd6)
       try:
        self.leB_6.setValue(self.vCond.Profils.B6)
       except: self.leB_6.setValue(0.0)

       try:
        self.leB_5.setValue(self.vCond.Profils.B5)
        self.leB_4.setValue(self.vCond.Profils.B4)
        self.leB_3.setValue(self.vCond.Profils.B3)
        self.leB_2.setValue(self.vCond.Profils.B2)
        self.leB_1.setValue(self.vCond.Profils.B1)

        self.leA_6.setValue(self.vCond.Profils.A6)
        self.leA_5.setValue(self.vCond.Profils.A5)
        self.leA_4.setValue(self.vCond.Profils.A4)
        self.leA_3.setValue(self.vCond.Profils.A3)
        self.leA_2.setValue(self.vCond.Profils.A2)
        self.leA_1.setValue(self.vCond.Profils.A1)
       except: 
        self.leB_5.setValue(0.0)
        self.leB_4.setValue(0.0)
        self.leB_3.setValue(0.0)
        self.leB_2.setValue(0.0)
        self.leB_1.setValue(0.0)

        self.leA_6.setValue(0.0)
        self.leA_5.setValue(0.0)
        self.leA_4.setValue(0.0)
        self.leA_3.setValue(0.0)
        self.leA_2.setValue(0.0)
        self.leA_1.setValue(0.0)
      if PCFlag==2:
        self.leKu_.setText('{:.3f}'.format(self.vCond.Profils.Kya,3))
        self.leKu_1_.setText('{:.6f}'.format(self.vCond.Profils.Kd1))#!s:.8
        self.leKu_2_.setText('{:.6f}'.format(self.vCond.Profils.Kd2))
        self.leKu_3_.setText('{:.6f}'.format(self.vCond.Profils.Kd3))
        self.leKu_4_.setText('{:.6f}'.format(self.vCond.Profils.Kd4))
        self.leKu_5_.setText('{:.6f}'.format(self.vCond.Profils.Kd5))
        self.leKu_6_.setText('{:.6f}'.format(self.vCond.Profils.Kd6))
        try:
          self.leB_6.setText('{:.6f}'.format(self.vCond.Profils.B6))
        except: self.leB_6.setText(str(0.0))

        try:
          self.leB_5.setText('{:.9f}'.format(self.vCond.Profils.B5))# !s:.15
          self.leB_4.setText('{:.9f}'.format(self.vCond.Profils.B4))
          self.leB_3.setText('{:.9f}'.format(self.vCond.Profils.B3))
          self.leB_2.setText('{:.9f}'.format(self.vCond.Profils.B2))
          self.leB_1.setText('{:.9f}'.format(self.vCond.Profils.B1))

          self.leA_6.setText('{:.9f}'.format(self.vCond.Profils.A6))
          self.leA_5.setText('{:.9f}'.format(self.vCond.Profils.A5))
          self.leA_4.setText('{:.9f}'.format(self.vCond.Profils.A4))
          self.leA_3.setText('{:.9f}'.format(self.vCond.Profils.A3))
          self.leA_2.setText('{:.9f}'.format(self.vCond.Profils.A2))
          self.leA_1.setText('{:.9f}'.format(self.vCond.Profils.A1))
        except: 
          self.leB_5.setText(str(0.0))
          self.leB_4.setText(str(0.0))
          self.leB_3.setText(str(0.0))
          self.leB_2.setText(str(0.0))
          self.leB_1.setText(str(0.0))

          self.leA_6.setText(str(0.0))
          self.leA_5.setText(str(0.0))
          self.leA_4.setText(str(0.0))
          self.leA_3.setText(str(0.0))
          self.leA_2.setText(str(0.0))
          self.leA_1.setText(str(0.0))
	  
      try:
        self.leCond_min.setText('{:.6f}'.format(self.vCond.Profils.Cond_min))
        self.leCond_max.setText('{:.6f}'.format(self.vCond.Profils.Cond_max))
      except: 
        self.leCond_min.setText(str(0.0))
        self.leCond_max.setText(str(0.0))
      a=self.vCond.Profils.PrName
      self.leProfilName_.setText(a)
      b=self.vCond.Profils.PrDescr
      self.leDescr_.setText(b)
      #self.leB_.setFocus()


class CProfils():

    def __init__(self,profils={}):
       b=0
       self.profs=profils
       self.profs.setdefault('Listcount',0)
       self.profs.setdefault('List',{})
       self.Listcount=self.profs['Listcount']
       self.CurrentProf=-1
       self.B=0
       self.Kya=0
       self.ATK=1.0
       self.V_vo=0.0
       self.TK_V_vo=0.0
       self.Kd1=1.0
       self.Kd2=1.0
       self.Kd3=1.0
       self.Kd4=1.0
       self.Kd5=1.0
       self.Kd6=1.0
       self.B_6=0.0
       self.B_5=0.0
       self.B_4=0.0
       self.B_3=0.0
       self.B_2=0.0
       self.B_1=0.0
       self.A_1=0.0
       self.A_2=0.0
       self.A_3=0.0
       self.A_4=0.0
       self.A_5=0.0
       self.A_6=0.0
       self.PrName=''
       self.PrDescr=''

    def LoadProfilsList(self):
       tmpi=0
       tmpl=[]
       while tmpi<self.Listcount-1:
           tmpl.append(self.profs['List'][tmpi])
       return tmpl
 
    def CreateProfil(self):
       tmpname=self.PrName
       tmpNum=0
       tmpi=0
       while (tmpi<self.Listcount-1):
          if(tmpNum>0):tmpnameNum=tmpname+tmpNum 
          else: tmpnameNum=tmpname 
          if (self.profs['List'][tmpi]==tmpnameNum):
              tmpNum=tmpNum+1
              tmpi=0
       self.profs['List'].setdefault(str(tmpnameNum),{})
       self.Listcount=self.Listcount+1
       self.profs['Listcount']=self.Listcount
       self.profs[self.PrName]['B']=self.B
       self.profs[self.PrName]['Kya']=self.Kya
       self.profs[self.PrName]['Kd1']=self.Kd1
       self.profs[self.PrName]['Kd2']=self.Kd2
       self.profs[self.PrName]['Kd3']=self.Kd3
       self.profs[self.PrName]['Kd4']=self.Kd4
       self.profs[self.PrName]['Kd5']=self.Kd5
       self.profs[self.PrName]['Kd6']=self.Kd6
       self.profs[self.PrName]['B6']=self.B6
       self.profs[self.PrName]['B5']=self.B5
       self.profs[self.PrName]['B4']=self.B4
       self.profs[self.PrName]['B3']=self.B3
       self.profs[self.PrName]['B2']=self.B2
       self.profs[self.PrName]['B1']=self.B1
       self.profs[self.PrName]['A1']=self.A1
       self.profs[self.PrName]['A2']=self.A2
       self.profs[self.PrName]['A3']=self.A3
       self.profs[self.PrName]['A4']=self.A4
       self.profs[self.PrName]['A5']=self.A5
       self.profs[self.PrName]['A6']=self.A6
       self.profs[self.PrName]['PrDescr']=self.PrDescr

    def DelProfil(self, index):
       tmpi=0
       tmpname=self.profs['List'][index]
       del self.profs['tmpname']
       tmpi=index
       while (tmpi<self.Listcount-2):
          self.profs['List'][index]=self.profs['List'][index+1]

       del self.profs['List'][self.Listcount-1]
       self.Listcount=self.Listcount-1
       self.profs['Listcount']=self.Listcount

    def ChangeProfil(self, index):
       self.CurrentProf=index
       self.Listcount=self.profs['Listcount']
       if(self.profs['List'][self.CurrentProf]!=self.PrName):
         self.profs['List'][self.CurrentProf]={}
         del self.profs[self.PrName]  
       else:
         self.profs[self.PrName]['B']=self.B
         self.profs[self.PrName]['Kya']=self.Kya
         self.profs[self.PrName]['Kd1']=self.Kd1
         self.profs[self.PrName]['Kd2']=self.Kd2
         self.profs[self.PrName]['Kd3']=self.Kd3
         self.profs[self.PrName]['Kd4']=self.Kd4
         self.profs[self.PrName]['Kd5']=self.Kd5
         self.profs[self.PrName]['Kd6']=self.Kd6
         self.profs[self.PrName]['B1']=self.B1
         self.profs[self.PrName]['B2']=self.B2
         self.profs[self.PrName]['B3']=self.B3
         self.profs[self.PrName]['B4']=self.B4
         self.profs[self.PrName]['B5']=self.B5
         self.profs[self.PrName]['B6']=self.B6
         self.profs[self.PrName]['A1']=self.A1
         self.profs[self.PrName]['A2']=self.A2
         self.profs[self.PrName]['A3']=self.A3
         self.profs[self.PrName]['A4']=self.A4
         self.profs[self.PrName]['A5']=self.A5
         self.profs[self.PrName]['A6']=self.A6

         self.profs[self.PrName]['PrDescr']=self.PrDescr

    def SelectProfil(self, index):
       self.CurrentProf=index
       self.Listcount=self.profs['Listcount']
       self.PrName=self.profs['List'][self.CurrentProf]
       self.B=self.profs[self.PrName]['B']
       self.Kya=self.profs[self.PrName]['Kya']
       self.ATK=self.profs[self.PrName]['ATK']
       self.V_vo=self.profs[self.PrName]['V_vo']
       self.TK_V_vo=self.profs[self.PrName]['TK_V_vo']
       self.Kd1=self.profs[self.PrName]['Kd1']
       self.Kd2=self.profs[self.PrName]['Kd2']
       self.Kd3=self.profs[self.PrName]['Kd3']
       self.Kd4=self.profs[self.PrName]['Kd4']
       self.Kd5=self.profs[self.PrName]['Kd5']
       self.Kd6=self.profs[self.PrName]['Kd6']
       try:
         self.B6=self.profs[self.PrName]['B6']
       except: self.B6=0.0

       try:
         self.B1=self.profs[self.PrName]['B1']
         self.B2=self.profs[self.PrName]['B2']
         self.B3=self.profs[self.PrName]['B3']
         self.B4=self.profs[self.PrName]['B4']
         self.B5=self.profs[self.PrName]['B5']
         self.A1=self.profs[self.PrName]['A1']
         self.A2=self.profs[self.PrName]['A2']
         self.A3=self.profs[self.PrName]['A3']
         self.A4=self.profs[self.PrName]['A4']
         self.A5=self.profs[self.PrName]['A5']
         self.A6=self.profs[self.PrName]['A6']
       except: 
         self.B5=0.0
         self.B4=0.0
         self.B3=0.0
         self.B2=0.0
         self.B1=0.0
         self.A1=0.0
         self.A2=0.0
         self.A3=0.0
         self.A4=0.0
         self.A5=0.0
         self.A6=0.0
       self.PrDescr=self.profs[self.PrName]['PrDescr']

    def GetInfoProfil(self, index):
       self.CurrentProf=index

    def ChangeCurrProfil(self, B=0.0, Kya=0.0, Kd1=1.0, Kd2=1.0, Kd3=1.0, Kd4=1.0, Kd5=1.0, Kd6=1.0, PrName='Pr1', PrDescr=' ',
                         B1=0.0, B2=0.0, B3=0.0, B4=0.0, B5=0.0, B6=0.0, A1=0.0, A2=0.0, A3=0.0, A4=0.0, A6=0.0, ATK=1.0, V_vo=0.0, 
                         TK_V_vo=0.0):
       self.B=B
       self.Kya=Kya
       self.ATK=ATK
       self.V_vo=V_vo
       self.TK_V_vo=TK_V_vo
       self.Kd1=Kd1
       self.Kd2=Kd2
       self.Kd3=Kd3
       self.Kd4=Kd4
       self.Kd5=Kd5
       self.Kd6=Kd6
       self.B1=B1
       self.B2=B2
       self.B3=B3
       self.B4=B4
       self.B5=B5
       self.B6=B6

       self.A1=A1
       self.A2=A2
       self.A3=A3
       self.A4=A4
       self.A5=A5
       self.A6=A6
       self.PrName=PrName
       self.PrDescr=PrDescr

    def SaveCurrProfil(self):
        if (self.CurrentProf==-1):
            self.CreateProfil()
        else:
            self.ChangeProfil()

class CProfilsC():

    def __init__(self, vCE, profils={}):
       b=0
       self.profs=profils
       self.vCE=vCE
       #self.vCE.ProfilsDict['Кондуктомер'].setdefault('Listcount',0)
       #self.vCE.ProfilsDict['Кондуктомер'].setdefault('List',{})
       #self.vCE.ProfilsDict['Кондуктомер']['Listcount']=4
       #self.Listcount=self.vCE.ProfilsDict['Кондуктомер']['Listcount']
       self.CurrentProf=-1
       self.B=0
       self.T_ATK=0.0 
       self.T_grad=0.0
       self.V_vo=0.0
       self.TK_V_vo=0.0
       self.Cond_min=0.0
       self.Cond_max=0.0
       self.Kya=1.0
       self.Kd1=1.0
       self.Kd2=1.0
       self.Kd3=1.0
       self.Kd4=1.0
       self.Kd5=1.0
       self.Kd6=1.0
       self.B6=0.0
       self.B5=0.0
       self.B4=0.0
       self.B3=0.0
       self.B2=0.0
       self.B1=0.0
       self.A1=0.0
       self.A2=0.0
       self.A3=0.0
       self.A4=0.0
       self.A5=0.0
       self.A6=0.0
       self.PrName=''
       self.PrDescr=''
       self.SelectedProfilNum=-1

    def LoadProfilsList(self):
       tmpi=0
       tmpl=[]
       while tmpi<self.Listcount-1:
           tmpl.append(self.vCE.ProfilsDict['Кондуктомер']['List'][tmpi])
       return tmpl
 
    def LoadProfil(self,prName=''):
        tmpname=self.PrName
        tmpNum=0
        tmpi=0
        if(self.Listcount==0):
           self.B=1
           self.T_ATK=0.0 
           self.T_grad=0.0
           self.V_vo=0.0
           self.TK_V_vo=0.0
           self.Cond_min=0.0
           self.Cond_max=0.0
           self.Kya=1
           self.Kd1=1
           self.Kd2=1
           self.Kd3=1
           self.Kd4=1
           self.Kd5=1
           self.Kd6=1
           self.B1=0
           self.B2=0
           self.B3=0
           self.B4=0
           self.B5=0
           self.B6=0

           self.A1=0
           self.A2=0
           self.A3=0
           self.A4=0
           self.A5=0
           self.A6=0
           self.PrName='(нет)'
           self.vCE._PrName=self.PrName    
           self.vCE._B=self.B
           self.vCE._Ku=self.Kya
           self.vCE._Kdu1=self.Kd1
           self.vCE._Kdu2=self.Kd2
           self.vCE._Kdu3=self.Kd3
           self.vCE._Kdu4=self.Kd4
           self.vCE._Kdu5=self.Kd5
           self.vCE._Kdu6=self.Kd6
           self.vCE._B1=self.B1
           self.vCE._B2=self.B2
           self.vCE._B3=self.B3
           self.vCE._B4=self.B4
           self.vCE._B5=self.B5
           self.vCE._B6=self.B6

           self.vCE._A1=self.A1
           self.vCE._A2=self.A2
           self.vCE._A3=self.A3
           self.vCE._A4=self.A4
           self.vCE._A5=self.A5
           self.vCE._A6=self.A6
           self.vCE._T_ATK=self.T_ATK
           self.vCE._T_grad=self.T_grad
           self.vCE._V_vo=self.V_v
           self.vCE._TK_V_vo=self.TK_V_vo
           
           self.vCE._Cond_min=self.Cond_min
           self.vCE._Cond_max=self.Cond_max
        tmpi=0
        if(self.Listcount>0):
           while (tmpi<self.Listcount): 
             if (self.vCE.ProfilsDict['Кондуктомер']['List'][tmpi]==prName):
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
          if (self.vCE.ProfilsDict['Кондуктомер']['List'][tmpi]==tmpnameNum):
              tmpNum=tmpNum+1
              tmpi=0
          tmpi=tmpi+1
       self.PrName=tmpnameNum
       self.vCE.ProfilsDict['Кондуктомер']['List'][self.Listcount]=str(self.PrName)
       self.Listcount=self.Listcount+1
       self.vCE.ProfilsDict['Кондуктомер']['Listcount']=self.Listcount
       self.vCE.ProfilsDict['Кондуктомер'][self.PrName]={}
       self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['B']=self.B
       self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['Kya']=self.Kya
       self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['Kd1']=self.Kd1
       self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['Kd2']=self.Kd2
       self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['Kd3']=self.Kd3
       self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['Kd4']=self.Kd4
       self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['Kd5']=self.Kd5
       self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['Kd6']=self.Kd6
       self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['B1']=self.B1
       self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['B2']=self.B2
       self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['B3']=self.B3
       self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['B4']=self.B4
       self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['B5']=self.B5
       self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['B6']=self.B6
       self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['A1']=self.A1
       self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['A2']=self.A2
       self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['A3']=self.A3
       self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['A4']=self.A4
       self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['A5']=self.A5
       self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['A6']=self.A6
       self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['PrDescr']=self.PrDescr
       self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['T_ATK']=self.T_ATK
       self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['T_grad']=self.T_grad
       self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['V_vo']=self.V_vo
       self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['TK_V_voA6']=self.TK_V_vo
       self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['Cond_min']=self.Cond_min
       self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['Cond_max']=self.Cond_min
       

    def DelProfil(self, index):
       tmpi=0
       tmpname=self.vCE.ProfilsDict['Кондуктомер']['List'][index]
       del self.vCE.ProfilsDict['Кондуктомер'][tmpname]
       tmpi=index
       while (tmpi<=self.Listcount-2):
          self.vCE.ProfilsDict['Кондуктомер']['List'][tmpi]=self.vCE.ProfilsDict['Кондуктомер']['List'][tmpi+1]
          tmpi=tmpi+1
       #while (tmpi<self.Listcount-1):#
       del self.vCE.ProfilsDict['Кондуктомер']['List'][self.Listcount-1]
       self.Listcount=self.Listcount-1
       self.vCE.ProfilsDict['Кондуктомер']['Listcount']=self.Listcount

    def ChangeProfil(self, index=-1):
       self.CurrentProf=index
       if(self.CurrentProf!=-1):
         self.Listcount=self.vCE.ProfilsDict['Кондуктомер']['Listcount']
         if(self.vCE.ProfilsDict['Кондуктомер']['List'][self.CurrentProf]!=self.PrName):
           self.vCE.ProfilsDict['Кондуктомер']['List'][self.CurrentProf]={}
           del self.vCE.ProfilsDict['Кондуктомер'][self.PrName]  
         else:
           self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['B']=self.B
           self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['Kya']=self.Kya
           self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['Kd1']=self.Kd1
           self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['Kd2']=self.Kd2
           self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['Kd3']=self.Kd3
           self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['Kd4']=self.Kd4
           self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['Kd5']=self.Kd5
           self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['Kd6']=self.Kd6
           self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['B1']=self.B1
           self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['B2']=self.B2
           self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['B3']=self.B3
           self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['B4']=self.B4
           self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['B5']=self.B5
           self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['B6']=self.B6
           self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['A1']=self.A1
           self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['A2']=self.A2
           self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['A3']=self.A3
           self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['A4']=self.A4
           self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['A5']=self.A5
           self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['A6']=self.A6
           self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['PrDescr']=self.PrDescr
           self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['T_ATK']=self.T_ATK
           self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['T_grad']=self.T_grad
           self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['V_vo']=self.V_vo
           self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['TK_V_vo']=self.TK_V_vo
           
           self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['Cond_min']=self.Cond_min
           self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['Cond_max']=self.Cond_max

    def SelectProfil(self, index):
       self.CurrentProf=index
       self.Listcount=self.vCE.ProfilsDict['Кондуктомер']['Listcount']
       tmpa=self.vCE.ProfilsDict['Кондуктомер']['List'][self.CurrentProf]
       self.PrName=tmpa
       self.B=self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['B']
       self.Kya=self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['Kya']
       self.Kd1=self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['Kd1']
       self.Kd2=self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['Kd2']
       self.Kd3=self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['Kd3']
       self.Kd4=self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['Kd4']
       self.Kd5=self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['Kd5']
       self.Kd6=self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['Kd6']
       try:
         self.B6=self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['B6']
       except: self.B6=0.0

       try:
         self.B1=self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['B1']
         self.B2=self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['B2']
         self.B3=self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['B3']
         self.B4=self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['B4']
         self.B5=self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['B5']

         self.A1=self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['A1']
         self.A2=self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['A2']
         self.A3=self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['A3']
         self.A4=self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['A4']
         self.A5=self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['A5']
         self.A6=self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['A6']
       except: 
         self.B1=0.0
         self.B2=0.0
         self.B3=0.0
         self.B4=0.0
         self.B5=0.0

         self.A1=0.0
         self.A2=0.0
         self.A3=0.0
         self.A4=0.0
         self.A5=0.0
         self.A6=0.0
       try:
         self.PrDescr=self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['PrDescr']
       except:
         self.PrDescr=''

       try:
         self.T_ATK=self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['T_ATK']
         self.T_grad=self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['T_grad']
         self.V_vo=self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['V_vo']
         self.TK_V_vo=self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['TK_V_vo']
       except:
         self.T_ATK=0.0
         self.T_grad=0.0
         self.V_v=""
         self.TK_V_vo=0.0

       try:
         self.Cond_min=self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['Cond_min']
         self.Cond_max=self.vCE.ProfilsDict['Кондуктомер'][self.PrName]['Cond_max']
       except:
         self.Cond_min=0.0
         self.Cond_max=0.0

       q=0
       self.vCE._PrName=self.PrName    
       self.vCE._B=self.B
       self.vCE._Ku=self.Kya
       self.vCE._Kdu1=self.Kd1
       self.vCE._Kdu2=self.Kd2
       self.vCE._Kdu3=self.Kd3
       self.vCE._Kdu4=self.Kd4
       self.vCE._Kdu5=self.Kd5
       self.vCE._Kdu6=self.Kd6
       self.vCE._B1=self.B1
       self.vCE._B2=self.B2
       self.vCE._B3=self.B3
       self.vCE._B4=self.B4
       self.vCE._B5=self.B5
       self.vCE._B6=self.B6

       self.vCE._A1=self.A1
       self.vCE._A2=self.A2
       self.vCE._A3=self.A3
       self.vCE._A4=self.A4
       self.vCE._A5=self.A5
       self.vCE._A6=self.A6

       self.vCE._T_ATK=self.T_ATK
       self.vCE._T_grad=self.T_grad
       self.vCE._V_vo=self.V_vo
       self.vCE._TK_V_vo=self.TK_V_vo
       self.vCE._Cond_min=self.Cond_min
       self.vCE._Cond_max=self.Cond_max

#############################################################################
    def CreateVVTable(self):
       tmpNum=0
       tmpi=0
       """Создание таблицы"""
       self.vCE.ProfilsDict['Кондуктомер']['Таблица_Веществ']={}
       self.vCE.ProfilsDict['Кондуктомер']['Таблица_Веществ']['ListCount']=0
       self.vCE.ProfilsDict['Кондуктомер']['Таблица_Веществ']['List']={}
       """Заполнение таблицы"""
       ListCount=self.vCE.ProfilsDict['Кондуктомер']['Таблица_Веществ']['ListCount']
       self.vCE.ProfilsDict['Кондуктомер']['Таблица_Веществ']['List'][ListCount+1]={}
       self.vCE.ProfilsDict['Кондуктомер']['Таблица_Веществ']['List'][ListCount+1]['V_vo']='NaCl'
       self.vCE.ProfilsDict['Кондуктомер']['Таблица_Веществ']['List'][ListCount+1]['Value']='0.05'
       ListCount=ListCount+1
       self.vCE.ProfilsDict['Кондуктомер']['Таблица_Веществ']['ListCount']=ListCount

    def AddVVTable(self, V_vo, Value):
       """Добавление значения в  таблицу"""
       ListCount=self.vCE.ProfilsDict['Кондуктомер']['Таблица_Веществ']['ListCount']
       self.vCE.ProfilsDict['Кондуктомер']['Таблица_Веществ']['List'][ListCount+1]={}
       self.vCE.ProfilsDict['Кондуктомер']['Таблица_Веществ']['List'][ListCount+1]['V_vo']=V_vo
       self.vCE.ProfilsDict['Кондуктомер']['Таблица_Веществ']['List'][ListCount+1]['Value']=Value
       ListCount=ListCount+1
       self.vCE.ProfilsDict['Кондуктомер']['Таблица_Веществ']['ListCount']=ListCount
       

    def DelVV(self, index):
       tmpi=0
       tmpname=self.vCE.ProfilsDict['Кондуктомер']['List'][index]
       tmpi=index
       Listcount= self.vCE.ProfilsDict['Кондуктомер']['Таблица_Веществ']['ListCount']
       while (tmpi<=Listcount-1):
          self.vCE.ProfilsDict['Кондуктомер']['Таблица_Веществ']['List'][tmpi]=self.vCE.ProfilsDict['Кондуктомер']['Таблица_Веществ']['List'][tmpi+1]
          tmpi=tmpi+1
       #while (tmpi<self.Listcount-1):#
       del self.vCE.ProfilsDict['Кондуктомер']['Таблица_Веществ']['List'][Listcount]
       Listcount=Listcount-1
       self.vCE.ProfilsDict['Кондуктомер']['Таблица_Веществ']['Listcount']=Listcount

    def ChangeVV(self, index=-1, V_vo=0, Value=0):
       """Изменение значения в  таблице"""
       ListCount=index
       self.vCE.ProfilsDict['Кондуктомер']['Таблица_Веществ']['List'][ListCount]['V_vo']=V_vo
       self.vCE.ProfilsDict['Кондуктомер']['Таблица_Веществ']['List'][ListCount]['Value']=Value


    def SelectVV(self, index):
       ListCount=index
       V_vo=self.vCE.ProfilsDict['Кондуктомер']['Таблица_Веществ']['List'][ListCount]['V_vo']
       Value=self.vCE.ProfilsDict['Кондуктомер']['Таблица_Веществ']['List'][ListCount]['Value']
       self.V_vo=V_vo
       self.TK_V_vo=Value
       self.vCE._V_vo=self.V_vo
       self.vCE._TK_V_vo=self.TK_V_vo

    def InitVV(self):
       tmpi=1
       self.vCE.winSelectV.lwV.clear()
       Listcount= self.vCE.ProfilsDict['Кондуктомер']['Таблица_Веществ']['ListCount']
       while (tmpi<=Listcount):
        V_vo=self.vCE.ProfilsDict['Кондуктомер']['Таблица_Веществ']['List'][tmpi]['V_vo']
        Value=self.vCE.ProfilsDict['Кондуктомер']['Таблица_Веществ']['List'][tmpi]['Value']
        self.vCE.winSelectV.lwV.addItem(V_vo+"       "+Value)
        tmpi=tmpi+1
       q=0
       #while (tmpi<self.Listcount-1):#

#############################################################################


    def GetInfoProfil(self, index):
       self.CurrentProf=index

    def ChangeCurrProfil(self, B=0.0, Kya=0.0, Kd1=1.0, Kd2=1.0, Kd3=1.0, Kd4=1.0, Kd5=1.0, Kd6=1.0, PrName='Pr1', PrDescr=' ',
                         B1=0.0, B2=0.0, B3=0.0, B4=0.0, B5=0.0, B6=0.0, A1=0.0, A2=0.0, A3=0.0, A4=0.0, A5=0.0, A6=0.0, Cond_min=0.0, Cond_max=0.0):

       self.B=B
       self.Kya=Kya
       self.Kd1=Kd1
       self.Kd2=Kd2
       self.Kd3=Kd3
       self.Kd4=Kd4
       self.Kd5=Kd5
       self.Kd6=Kd6
       self.B1=B1
       self.B2=B2
       self.B3=B3
       self.B4=B4
       self.B5=B5
       self.B6=B6
       self.A1=A1
       self.A2=A2
       self.A3=A3
       self.A4=A4
       self.A5=A5
       self.A6=A6
       self.Cond_min=Cond_min
       self.Cond_max=Cond_max
       self.PrName=PrName
       self.PrDescr=PrDescr

    def ChangeCurrProfil_TKR(self, T_ATK=0.0, T_grad=0.0):
       self.T_ATK=T_ATK 
       self.T_grad=T_grad

    def ChangeCurrProfil_SelectV(self, V_vo='', TK_V_vo=0.0):
       self.V_vo=V_vo
       self.TK_V_vo=TK_V_vo

    def SaveCurrProfil(self):
        if (self.CurrentProf==-1):
            self.CreateProfil()
            self.CurrentProf=self.Listcount-1
        else:
            self.ChangeProfil(self.CurrentProf)

        self.vCE.vCE.save_LocalProfil_state()


class CCond(CVInstr):
  """ виртуальный кондуктометр """
  #  measI - наименование измерительного канала напряжения, связанного с данным экземпляром иономера
  #  measT - наименование измерительного канала температуры, связанного с данным экземпляром иономера
  #  lastT - последнее значение температуры, полученное из измерительного канала
  #  timeT - время измерения температуры
  #  lastN - последнее значение напряжения,  полученное из измерительного канала
  #  timeN - время измерения температуры

  def __init__(self,vCE, dcfg, dstate = {}, dSize={}, LocalProfilsDict={},  fTech = False):
    super().__init__(dcfg, dstate, fTech)

    self.vCE=vCE
    self.fpCond_Version=1
    self.K_temp=1.0
    self.lastT = 25
    self.lastR =100
    self.lastRD =8
    self.PrevTemp=0
    self.PrevR=0
    self.PrevRD=0
    self.tmpX_sm_t_Set=0.0
    self.tmpX_Set=0.0
    self.tmpX_sm_Set=0.0
    self.tmpKd_Set=0.0
    self.techT=0
    self.KBand=1
    self.KSaltBand=1
    self.closeFlag=0  
    self.T_curr=0.0
    self.Cond_ed='_'
    self.Salt_ed='_'
    self.CurrProfil=''
    self.LastProfil=''
    self.Name=dcfg['наименование']
    self.ProfilsDict=LocalProfilsDict
    self.ProfilsDict.setdefault('Кондуктомер',{})
    self.ProfilsDict['Кондуктомер'].setdefault(self.Name,{})
    self.LastProfil=self.ProfilsDict['Кондуктомер'][self.Name].setdefault('Текущий профмль','')
    self.tmpVal=0   
    self.tmpVal0=0  
    self.tmpVal1=0

    self.ParamMess=dSize['VPParam']
    self.InputUnit=[0,0,0,0]
    self.InputVal=[0,0,0,0]
    self.OutputVal=[0,0,0,0]
    self.OutputParam=[0,0,0,0]
    self.OutputEdIzm=[0,0,0,0]
    self.InputUnit[0]=dSize['VPChModulNameList'][0]
    self.InputUnit[1]=dSize['VPChModulNameList'][1]
    self.InputUnit[2]=dSize['VPChModulNameList'][2]
    self.InputVal[0]=dSize['VPChNameList'][0]
    self.InputVal[1]=dSize['VPChNameList'][1]
    self.InputVal[2]=dSize['VPChNameList'][2]
    self.OutputVal[0]=dSize['VPChOutTypeList'][0]
    #self.OutputVal[1]=dSize['VPChOutTypeList'][1]
    self.ManualT_Flag=0
    self.OffT_Flag=0
    self.AutoT_Flag=0

    self.tmpVal_2=0
    self.tmpVal_3=0
    self.TypeMess=0
    self.widthD = 7
    self.precD = 3
    self.dSize=dSize
    self.width=self.dSize.setdefault('width',100)
    self.height=self.dSize.setdefault('height',100)
    self.x=self.dSize.setdefault('x',100)
    self.y=self.dSize.setdefault('y',100) 
    self.Profils=CProfilsC(self,self.ProfilsDict)
    self.formS = "{:"+str(self.widthD)+"."+str(self.precD)+"f}" 
    #self.win = CfpCond(self)
    self.winProbaID =CfmProbaID(self)
    self.winAboutVP =CfmAboutVP(self)
    self.winMessage =CfmMessage(self)
    self.win = CfpCond_Compact_2(self)
    self.winCCond = CfmCondCalib(self)
    self.winSelectProfil = CfmSelectProfil(self)
    self.winCondPassword = CfmVPPassword(self)
    self.winSelectV = CfmSelectV(self)
    self.winTKR = CfmTKR(self)
    #self.win.leK_temp.setText('1.0')

    tmppr=''
    self.LastProfil=self.ProfilsDict['Кондуктомер'][self.Name]['Текущий профмль']
    tmppr=self.LastProfil
    try:
      self.Profils.LoadProfil(self.LastProfil)
      self._PrName=self.LastProfil
    except: tmppr='не выбран'        
    self.win.lblProfilName.setText(tmppr)
    try:
     self.win.label_8.setText(self.Profils.V_vo + "  "+str(self.Profils.TK_V_vo)+ "% "+str(self.Profils.T_ATK)+ " oC" )
    except:
     self.win.label_8.setText("Содержание ")
    
    if(self.ParamMess=='0'):
      self.measCond = self.dictCfg["каналСопротивление"]
      self.measR_B= self.dictCfg["каналДиапазонСопротивления"]
      self.measT = self.dictCfg["каналТемпература"]
      self.dictCfg["meas"] = [self.measCond, self.measR_B, self.measT] # фактически вносится в vinstrD

    if(self.ParamMess=='1'):
      self.timer = QtCore.QTimer()
      self.timer.timeout.connect(self.NewDataTimer)
      self.timer.start(1000)
    

    self._fTempTech = False
    self._fTempComp = True 
    self.lastT = 20    # ВРЕМЕННО 
    Results.Result_Dict[self.Name]={}
    Results.Result_Dict[self.Name][self.OutputVal[0]]=0
    Results.Result_Dict[self.Name]['В блокнот']=0
    self.InLight_Notepad=0
    # вызовы сеттеров для синхронизации состояния кислородомера и лицевой панели
    self.fTempComp = self._fTempComp 
    self.fTempTech = self._fTempTech
    self.dSize=dSize
    self.win.width=self.dSize.setdefault('width',100)
    self.win.height=self.dSize.setdefault('height',100)
    self.win.x=self.dSize.setdefault('x',100)
    self.win.y=self.dSize.setdefault('y',100)    
    self.LoadState()
    self.EdIzm=0
    self.timerM = QtCore.QTimer()
    self.timerM.timeout.connect(self.NewDataTimerM)
    self.timerM.start(100)

  def NewDataTimerM(self):
      #Начальная инициализация выходной величины
      self.tmpVal_R=0
      q=0
      a=datetime.today()
      a1=a.date()
      a2=a.time()
      dt1=str(a1)+"  \t"+a2.strftime("%H:%M:%S") 
      #self.win.lblDateTime.setText(str(dt1))
######################################################
      #self.tmpVal_3=self.lastR/100000000.0
      '''
      try:
        self.K_temp=eval(self.win.leK_temp.text(), {}, {})
      except:
          K_temp=1.0'''
      self.Temp=self.lastT
      self.Aetu=0
      self.tmpBd=0.0
      self.tmpAd=0.0
      if(self.lastRD==1):
          self.Aetu=self.Profils.Kd1
          self.tmpBd=self.Profils.B1
          self.tmpAd=self.Profils.A1*1000

      if(self.lastRD==2):
          self.Aetu=self.Profils.Kd2
          self.tmpBd=self.Profils.B2
          self.tmpAd=self.Profils.A2*1000

      if(self.lastRD==3):
          self.Aetu=self.Profils.Kd3
          self.tmpBd=self.Profils.B3
          self.tmpAd=self.Profils.A3

      if(self.lastRD==4):
          self.Aetu=self.Profils.Kd4
          self.tmpBd=self.Profils.B4
          self.tmpAd=self.Profils.A4

      if(self.lastRD==5):
          self.Aetu=self.Profils.Kd5
          self.tmpBd=self.Profils.B5
          self.tmpAd=self.Profils.A5

      if(self.lastRD==6):
          self.Aetu=self.Profils.Kd6
          self.tmpBd=self.Profils.B6
          self.tmpAd=self.Profils.A6

      if(self.lastRD>6) :self.Aetu=self.Profils.Kd6
       

      if (self.tmpVal1==1)or(self.tmpVal1==2)or(self.tmpVal1==3)or(self.tmpVal1==4):# МОм
          self.KBand=1000000.0
          self.KSaltBand=1
      if (self.tmpVal1>4)and(self.tmpVal1<8): # кОм
          self.KBand=1000.0
          self.KSaltBand=1000.0
      ###############################################################
      '''self.lastR=70.3'''

      self.tmpX=0
      self.tmpX_t=0.0
      self.tmpX_=0
      self.tmpX_ms=0
      self.tmpR=0
      self.tmpC=1.956947E-6
      
      if (self.lastR*self.Aetu!=0):
              self.tmpX_t=self.K_temp*(self.tmpAd*self.Profils.Kya/(float(self.lastR)*float(self.lastR)*1000000.0)-self.Profils.Kya*self.tmpC+self.Profils.Kya/(float(self.lastR)*self.Aetu)+ self.Profils.Kya*self.tmpBd/1000)#См
              #self.tmpX=self.tmpAd*self.Profils.Kya/(float(self.lastR)*float(self.lastR)*1000000.0)-self.Profils.Kya*self.tmpC+self.Profils.Kya/(float(self.lastR)*self.Aetu)+ self.tmpBd/1000#См
              if(self.OffT_Flag==1): self.tmpX=self.tmpX_t 
              if(self.ManualT_Flag==1):
                  dt=self.T_curr-float(self.Profils.T_ATK) 
                  at=float(self.Profils.TK_V_vo)*dt/100.0
                  at1=1.0+at
                  self.tmpX=self.tmpX_t/at1
                  #self.tmpX=self.tmpX_t *(1.0/(1.0+self.Profils.TK_V_vo(self.T_curr-self.Profils.T_ATK)))
              if(self.AutoT_Flag==1):
                  dt=self.lastT-float(self.Profils.T_ATK) 
                  at=float(self.Profils.TK_V_vo)*dt/100.0
                  at1=1.0+at
                  self.tmpX=self.tmpX_t/at1
                  #T_c=float(self.lastT)
                  self.DispTemp(self.lastT)
                  #self.tmpX=self.tmpX_t *(1.0/(1.0+float(self.Profils.TK_V_vo)(T_c-0.0)))#float(self.Profils.T_ATK)))))
                  

      if(self.tmpX>0):
              self.tmpR=1/self.tmpX
      if(self.tmpX<=0):
              self.tmpX=0
              self.tmpR=0

      self.tmpVal_3=self.tmpR



      ###############################################################
      if (self.tmpVal_3>=100000): # 100кОм
          self.tmpVal_R=self.tmpVal_3/1000000 # МОм
          self.win.lblEd_3.setText('МОм')
          #self.formS_4 = "{:"+str(self.widthD)+"."+str(3)+"f}"

      if (self.tmpVal_3<100000)and(self.tmpVal_3>=1000): # 1кОм
          self.tmpVal_R=self.tmpVal_3/1000 # кОм
          self.win.lblEd_3.setText('кОм')
          #self.formS_4 = "{:"+str(self.widthD)+"."+str(3)+"f}"

      if (self.tmpVal_3<1000): # 1кОм
          self.tmpVal_R=self.tmpVal_3 # Ом
          self.win.lblEd_3.setText('Ом')
          #self.formS_4 = "{:"+str(self.widthD)+"."+str(1)+"f}"

      if(self.tmpX<0):
          self.tmpX_=self.tmpX*(-1)
      else:
          self.tmpX_=self.tmpX

      if(float(self.tmpX_)!=0.0):
        #self.tmpVal=self.Profils.B+100000000.0*self.Profils.Kya/(float(self.lastR)*self.KBand*self.Aetu) # self.lastR
        #self.tmpVal=self.Profils.Kya/(float(self.lastR)*self.Aetu) # self.lastR
        
        #if(self.lastRD==5)or(self.lastRD==6):
        #    self.tmpB=0
        if (self.tmpX_<0.005): # 5 мСм
          self.tmpVal_Sm=self.tmpX*float(10**6) # мкСм
          self.win.lblEd.setText('мкСм/см')
          self.winCCond.lblCond_ed.setText('мкСм/см')
          #self.formS_5 = "{:"+str(self.widthD)+"."+str(2)+"f}"

        if (self.tmpX_<0.1)and(self.tmpX>=0.005): # 5 мСм-100 мСм
          self.tmpVal_Sm=self.tmpX*float(10**3) # мСм
          self.win.lblEd.setText('мСм/см')
          self.winCCond.lblCond_ed.setText('мСм/см')
          #self.formS_5 = "{:"+str(self.widthD)+"."+str(3)+"f}"

        if (self.tmpX_>=0.1): # 100 мСм
          self.tmpVal_Sm=self.tmpX # См
          self.win.lblEd.setText('См/см')
          self.winCCond.lblCond_ed.setText('См/см')
          #self.formS_5 = "{:"+str(self.widthD)+"."+str(4)+"f}"

        self.tmpVal_2=self.Calc_Salt_1(self.tmpX,self.T_curr)

#Автоматический расчет коэффициентов
      if(self.tmpX_Set>0):#tmpX_sm_Set
        if (self.tmpX_<0.005): # 5 мСм
          self.tmpX_sm_Set=self.tmpX_Set/float(10**6) # мкСм

        if (self.tmpX_<0.1)and(self.tmpX>=0.005): # 5 мСм-100 мСм
          self.tmpX_sm_Set=self.tmpX_Set/float(10**3) # мСм

        if (self.tmpX_>=0.1): # 100 мСм
          self.tmpX_sm_Set=self.tmpX_Set # См

        if(self.OffT_Flag==1): self.tmpX_sm_t_Set=self.tmpX_sm_Set 
        if(self.ManualT_Flag==1):
                  dt=self.T_curr-float(self.Profils.T_ATK) 
                  at=float(self.Profils.TK_V_vo)*dt/100.0
                  at1=1.0+at
                  self.tmpX_sm_t_Set=self.tmpX_sm_Set*at1

        if(self.AutoT_Flag==1):
                  dt=self.lastT-float(self.Profils.T_ATK) 
                  at=float(self.Profils.TK_V_vo)*dt/100.0
                  at1=1.0+at
                  self.tmpX_sm_t_Set=self.tmpX_sm_Set*at1

        #self.tmpX_t=self.K_temp*(self.tmpAd*self.Profils.Kya/(float(self.lastR)*float(self.lastR)*1000000.0)-self.Profils.Kya*self.tmpC+self.Profils.Kya/(float(self.lastR)*self.Aetu)+ self.Profils.Kya*self.tmpBd/1000)#См
        self.tmpKd_Set=self.Profils.Kya/((self.tmpX_sm_t_Set-self.K_temp*(self.tmpAd*self.Profils.Kya/(float(self.lastR)*float(self.lastR)*1000000.0)-self.Profils.Kya*self.tmpC+self.Profils.Kya*self.tmpBd/1000))*float(self.lastR))
        
        if(self.lastRD==1):
          self.winCCond.leKu_1_.setValue(self.tmpKd_Set)
          #self.winCCond.leKu_1_.clearFocus()

        if(self.lastRD==2):
          self.winCCond.leKu_2_.setValue(self.tmpKd_Set)
          #self.winCCond.leKu_2_.clearFocus()

        if(self.lastRD==3):
          self.winCCond.leKu_3_.setValue(self.tmpKd_Set)
          self.winCCond.leKu_3_.clearFocus()

        if(self.lastRD==4):
          self.winCCond.leKu_4_.setValue(self.tmpKd_Set)
          #self.winCCond.leKu_4_.clearFocus()

        if(self.lastRD==5):
          self.winCCond.leKu_5_.setValue(self.tmpKd_Set)
          #self.winCCond.leKu_5_.clearFocus()

        if(self.lastRD==6):
          self.winCCond.leKu_6_.setValue(self.tmpKd_Set)
          #self.winCCond.leKu_6_.clearFocus()

        self.tmpX_Set=0.0
#Окончание - Автоматический расчет коэффициентов 

      #self.win.lcdMain.display(self.formS_5.format(self.tmpVal_Sm))#Проводимость
      #self.win.lcdMain_2.display(self.formS.format(self.tmpVal_2))#Соленость
      #self.win.lcdMain_3.display(self.formS_4.format(self.tmpVal_R))# Сопротивление
######################################################
      '''self.tmpVal_3=self.lastR/100000000.0
      self.Temp=self.lastT
      self.Aetu=0
      if(self.lastRD==1):self.Aetu=self.Profils.Kd1
      if(self.lastRD==2):self.Aetu=self.Profils.Kd2
      if(self.lastRD==3):self.Aetu=self.Profils.Kd3
      if(self.lastRD==4):self.Aetu=self.Profils.Kd4
      if(self.lastRD==5):self.Aetu=self.Profils.Kd5
      if(self.lastRD==6):self.Aetu=self.Profils.Kd6
      if(self.lastRD==7):self.Aetu=self.Profils.Kd6
      if(float(self.tmpVal0)*self.Aetu>0.0):
        self.tmpVal=self.Profils.B+100000000.0*self.Profils.Kya/(float(self.tmpVal0)*self.Aetu)''' 
      #T=0.0
      if (self.OffT_Flag==1): 
            self.T_curr= 25.0 # при отключенной термокоррекции расчет идет на температуре калибровки 
            self.DispTemp(self.T_curr)
      if (self.ManualT_Flag==1): 
            q=0

            
      if (self.AutoT_Flag==1):                   
            self.T_curr=self.Temp          # расчет на основе температуры от измерителя  
            if((self.T_curr<-200.0)|(self.T_curr>200.0)):self.T_curr= 25.0 
            self.DispTemp(self.T_curr)          
      if(self.PrevTemp!=self.lastT):
       fNewTemp = True
      else:  
       fNewTemp = False
      self.PrevTemp=self.lastT
      if(self.PrevR!=self.lastR):
       fNewR = True
      else:  
       fNewR = False
      self.PrevR=self.lastR

      if(self.PrevRD!=self.lastRD):
       fNewRD = True
      else:  
       fNewRD = False
      self.PrevRD=self.lastRD
      #self.win.leTemp.setText("{:2.1f}".format(temp))
      #self.tmpVal_2=self.Calc_Salt_1(self.tmpVal,self.T_curr)
      #self.win.lcdMain.display(self.formS.format(self.tmpVal))
      if ((self.tmpX>=self.Profils.Cond_min/1000)&(self.tmpX<=self.Profils.Cond_max/1000)|(self.Profils.Cond_min==self.Profils.Cond_max)):
          q=0
          self.winCCond.llCond_.setStyleSheet("color: rgb(0, 0, 0);")
          self.win.lcdMain.setStyleSheet("color: rgb(0, 0, 0);")
      else:
          self.winCCond.llCond_.setStyleSheet("color: rgb(255, 0, 0);")
          self.win.lcdMain.setStyleSheet("color: rgb(255, 0, 0);")
          q=1
      if (self.tmpVal_Sm>1000.0): 
          self.win.lcdMain.display("{:4.0f}".format(self.tmpVal_Sm))
          self.winCCond.llCond_.setText("{:4.0f}".format(self.tmpVal_Sm))
      if ((self.tmpVal_Sm>=100.0)&(self.tmpVal_Sm<1000.0)): 
          self.win.lcdMain.display("{:3.1f}".format(self.tmpVal_Sm))
          self.winCCond.llCond_.setText("{:3.1f}".format(self.tmpVal_Sm))
      if ((self.tmpVal_Sm>=10.0)&(self.tmpVal_Sm<100.0)): 
          self.win.lcdMain.display("{:2.2f}".format(self.tmpVal_Sm))
          self.winCCond.llCond_.setText("{:2.2f}".format(self.tmpVal_Sm))
      if ((self.tmpVal_Sm>=1.0)&(self.tmpVal_Sm<10.0)): 
          self.win.lcdMain.display("{:1.3f}".format(self.tmpVal_Sm))
          self.winCCond.llCond_.setText("{:1.3f}".format(self.tmpVal_Sm))
      if (self.tmpVal_Sm<1.0): 
          self.win.lcdMain.display("{:0.4f}".format(self.tmpVal_Sm))
          self.winCCond.llCond_.setText("{:0.4f}".format(self.tmpVal_Sm))

      #self.win.lcdMain_2.display(self.formS.format(self.tmpVal_2))
      if (self.tmpVal_2>1000.0): self.win.lcdMain_2.display("{:4.0f}".format(self.tmpVal_2))
      if ((self.tmpVal_2>=100.0)&(self.tmpVal_2<1000.0)): self.win.lcdMain_2.display("{:3.1f}".format(self.tmpVal_2))
      if ((self.tmpVal_2>=10.0)&(self.tmpVal_2<100.0)): self.win.lcdMain_2.display("{:2.2f}".format(self.tmpVal_2))
      if ((self.tmpVal_2>=1.0)&(self.tmpVal_2<10.0)): self.win.lcdMain_2.display("{:1.3f}".format(self.tmpVal_2))
      if (self.tmpVal_2<1.0): self.win.lcdMain_2.display("{:0.4f}".format(self.tmpVal_2))

      #self.win.lcdMain_3.display(self.formS.format(self.tmpVal_3))
      if (self.tmpVal_R>1000.0): self.win.lcdMain_3.display("{:4.0f}".format(self.tmpVal_R))
      if ((self.tmpVal_R>=100.0)&(self.tmpVal_R<1000.0)): self.win.lcdMain_3.display("{:3.1f}".format(self.tmpVal_R))
      if ((self.tmpVal_R>=10.0)&(self.tmpVal_R<100.0)): self.win.lcdMain_3.display("{:2.2f}".format(self.tmpVal_R))
      if ((self.tmpVal_R>=1.0)&(self.tmpVal_R<10.0)): self.win.lcdMain_3.display("{:1.3f}".format(self.tmpVal_R))
      if (self.tmpVal_R<1.0): self.win.lcdMain_3.display("{:0.4f}".format(self.tmpVal_R))

      Results.Result_Dict[self.Name][self.OutputVal[0]]=self.tmpVal_Sm
      Results.Result_Dict[self.Name]['Параметр '+self.OutputVal[0]]='Проводимость'
      Results.Result_Dict[self.Name]['Единица '+self.OutputVal[0]]=self.Cond_ed
      if(Results.Result_Dict[self.Name]['В блокнот']!=2):Results.Result_Dict[self.Name]['В блокнот']=self.InLight_Notepad
      Results.Result_Dict[self.Name]['ID_VP']=self.ID_VP
      Results.Result_Dict[self.Name]['LastProfil']=self.LastProfil
      if(Results.Result_Dict[self.Name]['В блокнот']==2):
        Results.Result_Dict[self.Name]['В блокнот']=0
        self.InLight_Notepad=0
      if(self.winCCond.gbxBKd.isEnabled()==True):
       paletteR=QtGui.QPalette()  
       paletteB=QtGui.QPalette()  
       #palette.setColor(QtGui.QPalette.Background,QtCore.Qt.red)  
       paletteR.setColor(QtGui.QPalette.Foreground,QtCore.Qt.red) 
       paletteB.setColor(QtGui.QPalette.Foreground,QtCore.Qt.black) 
       if(self.lastRD==1): self.winCCond.lblKD1.setPalette(paletteR)
       else:               self.winCCond.lblKD1.setPalette(paletteB)

       if(self.lastRD==2): self.winCCond.lblKD2.setPalette(paletteR)
       else:               self.winCCond.lblKD2.setPalette(paletteB)

       if(self.lastRD==3): self.winCCond.lblKD3.setPalette(paletteR)
       else:               self.winCCond.lblKD3.setPalette(paletteB)

       if(self.lastRD==4): self.winCCond.lblKD4.setPalette(paletteR)
       else:               self.winCCond.lblKD4.setPalette(paletteB)

       if(self.lastRD==5): self.winCCond.lblKD5.setPalette(paletteR)
       else:               self.winCCond.lblKD5.setPalette(paletteB)

       if(self.lastRD==6): self.winCCond.lblKD6.setPalette(paletteR)
       else:               self.winCCond.lblKD6.setPalette(paletteB)
      else:
       paletteG=QtGui.QPalette() 
       paletteG.setColor(QtGui.QPalette.Foreground,QtCore.Qt.gray) 
       self.winCCond.lblKD1.setPalette(paletteG)
       self.winCCond.lblKD2.setPalette(paletteG)
       self.winCCond.lblKD3.setPalette(paletteG)
       self.winCCond.lblKD4.setPalette(paletteG)
       self.winCCond.lblKD5.setPalette(paletteG)
       self.winCCond.lblKD6.setPalette(paletteG) 
      #self.winCCond.llCond_.setText(self.formS.format(self.tmpVal))
      Results.Result_Dict[(self.Name)][('Value')]=self.tmpVal
      #print(self.timeT)
      if(self.tmpVal_Sm==0): self.win.lblEd.setText('__')
      '''if (self.tmpVal1==1)or(self.tmpVal1==2)or(self.tmpVal1==3)or(self.tmpVal1==4): 
          self.win.lblEd.setText('мкСм/см')
          self.win.lblEd_3.setText('МОм')
          self.winCCond.lblCond_ed.setText('мкСм/см')
          self.KBand=1000000.0
          self.KSaltBand=1
      if (self.tmpVal1>4)and(self.tmpVal1<8): 
          self.win.lblEd.setText('мСм/см')
          self.win.lblEd_3.setText('кОм')
          self.winCCond.lblCond_ed.setText('мСм/см')
          self.KBand=1000.0
          self.KSaltBand=1000.0'''
      self.win.lblEd_2.setText('мг/дм3')
      self.R_ed=self.win.lblEd_3.text()
      self.Cond_ed=self.win.lblEd.text()
      self.Salt_ed='мг/дм3'
      if (self.vCE.Close_Config_Flag==1)and(self.closeFlag==0): 
          self.closeFlag=1
          self.timerM.stop()      
          self.win.close()
          #self.delete()
          a=0
          

 
  def Calc_Salt(self,A,Temp):
    Res=0
    K=0.0
    K=1+0.01996*(Temp-25)+0.0000584*(Temp-25)**2
    #Res=100000/(math.sqrt((2.1549*K/A)-1.563)-1.25)**2
    tmpk=-1.0
    try:
       tmpk=(2.1549*K/A)-1.563
    except: 
        tmpk=-2
        Res=-2
    if(tmpk>0.0):
        Res=100000/(math.sqrt((2.1549*K/A)-1.563)-1.25)**2
    else:
        Res=tmpk
    Res=K/A
    return Res

  def Calc_Salt_1(self,A,Temp):

    Res=A*0.53*1000000 #self.KSaltBand

    return Res


  def LoadState(self):
    super().LoadState()


  def SaveState(self):
    super().SaveState()


  def NewData(self, ddata):

    if self.measT in ddata:
       self.lastT = ddata[self.measT][1]
       self.timeT = ddata[self.measT][2] 

    if self.measR_B in ddata:
       self.lastRD = ddata[self.measR_B][1]
       self.tmpVal1=self.lastRD

    if self.measCond in ddata:
      self.lastR = ddata[self.measCond][1]
      self.tmpVal0=self.lastR

  def NewDataTimer(self):
    
   if(self.ParamMess=='1'): 

      try:
       self.lastR=float(Results.Result_Dict[self.InputUnit[0]][self.InputVal[0]])
      except: self.lastR=0.0
      try:
       self.lastRD=float(Results.Result_Dict[self.InputUnit[1]][self.InputVal[1]])
      except: self.lastRD=0.0
      try:
       self.lastT=float(Results.Result_Dict[self.InputUnit[2]][self.InputVal[2]])
      except: self.lastT=0.0
      if(self.PrevTemp!=self.lastT):
       self.fNewTemp = True
      else:  
       self.fNewTemp = False
      self.PrevTemp=self.lastT

      if(self.PrevR!=self.lastR):
       self.fNewR = True
      else:  
       self.fNewR = False
      self.PrevR=self.lastR

      if(self.PrevRD!=self.lastRD):
       self.fNewRD = True
      else:  
       self.fNewRD = False
      self.PrevRD=self.lastRD
      self.Calc_R_All()


  def Calc_R_All(self):
      if ((self.fNewR)|(self.fNewRD)|(self.fNewTemp)):
        self.tmpVal=100000000.0*self.Profils.Kya /(self.lastR)
        self.tmpVal_3=100000000.0*self.lastR
        self.Temp=self.lastT
        T=0.0
        if (self.OffT_Flag==1): 
            T = -1000.0 # при отключенной термокоррекции расчет идет на температуре калибровки 
        if (self.ManualT_Flag==1): 
            T = self.techT  # расчет на основе температуры заданной вручную
        if (self.AutoT_Flag==1):                   
            T = self.Temp          # расчет на основе температуры от измерителя    
            self.workT = self.Temp

        self.tmpVal_2=0
        self.win.lcdMain.display(self.formS.format(self.tmpVal))
        self.win.lcdMain_2.display(self.formS.format(self.tmpVal_2))
        self.win.lcdMain_3.display(self.formS.format(self.tmpVal_3))
        Results.Result_Dict[self.Name][self.OutputVal[0]]=self.tmpVal
        self.win.lblProfilName.setText(self._PrName)
        self.win.label_8.setText(self.Profils.V_vo + "  "+str(self.Profils.TK_V_vo)+ "% "+str(self.Profils.T_ATK)+ " oC" )

      if self.fNewRD:
        self.tmpVal1=int(self.lastRD)
        ###self.win.llBand.setText(str(self.tmpVal1))
        if(self.tmpVal1==0): self.win.lblEd.setText('__')
        if (self.tmpVal1==1)or(self.tmpVal1==2)or(self.tmpVal1==3)or(self.tmpVal1==4): 
            self.win.lblEd.setText('мкСм/см')
            self.win.lblEd_3.setText('МОм')
        if (self.tmpVal1>4)and(self.tmpVal1<8): 
            self.win.lblEd.setText('мСм/см')
            self.win.lblEd_3.setText('кОм')
        self.win.lblEd_2.setText('мг/дм3')
  #  def Calc_R_All()

  def DispTemp(self, temp):
    #temp=12.1234
    """ обновить значение температуры temp на лицевой панели """
    if not self._fTempTech:  self.win.leTemp.setText("{:2.1f}".format(temp))



  @property
  def fTempTech(self):
    return self._fTempTech

  @fTempTech.setter
  def fTempTech(self, value):
    self._fTempTech = value
    if value:          
      self.win.leTemp.setText("{:5.2f}".format(self.techT))
    else:
      self.win.leTemp.setText("{:5.2f}".format(self.lastT))

    ###self.win.tbAutoT.setDown(not self._fTempTech)
    self.win.leTemp.setReadOnly(not (self._fTempTech and self._fTempComp))   

  @property
  def fDlog(self):
    return self._fDlog

  @fDlog.setter
  def fDlog(self, value):
    self._fDlog = value

class CR_Band(CVInstr,CSaveRes):
  """ диапазон измерителя сопротивления"""
  #  measI - наименование измерительного канала, связанного с данным экземпляром амперметра
  #  widthD - суммарное кол-во выводимых знаков результата (БЕЗ учета запятой)
  #  precD  - кол-во знаков после запятой 
  #  formS  - строка форматирования для вывода результата (под НОВЫЙ метод format)

  def __init__(self,vCE, dcfg, dstate = {}, dSize={}, fTech = False):
    super().__init__(dcfg, dstate, fTech)
    # TODO обработку ошибок конфигурации
    self.Name=dcfg['наименование']
    #if(self.ParamMess=='0'):
    self.measR = self.dictCfg["каналСопротивление"]
    self.measR_B = self.dictCfg["каналДиапазонСопротивления"]
    self.vCE=vCE
    self.closeFlag=0 
    self.dictCfg["meas"] = [self.measR, self.measR_B] # фактически вносится в vinstrDD
    self.lastR=0
    self.lastRD=0
    self.tmpVal0=0
    self.tmpVal1=0


    self.widthD = 6 # 4
    self.precD = 3  # 3
    self.formS = "{:"+str(self.widthD)+"f}"
    self.InputUnit=[0,0,0]
    self.InputVal=[0,0,0]
    self.OutputVal=[0,0,0]
    self.InputUnit[0]=dSize['VPChModulNameList'][0]
    self.InputVal[0]=dSize['VPChNameList'][0]
    self.OutputVal[0]=dSize['VPChOutTypeList'][0]
    Results.Result_Dict[self.Name]={}
    Results.Result_Dict[self.Name][self.OutputVal[0]]=0
    Results.Result_Dict[self.Name]['В блокнот']=0
    self.InLight_Notepad=0
    self.ID_VP='0'
    self.dSize=dSize
    self.width=self.dSize.setdefault('width',100)
    self.height=self.dSize.setdefault('height',100)
    self.x=self.dSize.setdefault('x',100)
    self.y=self.dSize.setdefault('y',100) 
    self.winProbaID =CfmProbaID(self)
    self.winAboutVP =CfmAboutVP(self)
    self.winMessage =CfmMessage(self)
    self.win = CfpR_Band(self.widthD + 1, self)
    self.LoadState()
    #Создания словаря результатов
    Results.Result_Dict[self.Name]={}
    #Создания в словаре результатов переменной записи в блокнот
    Results.Result_Dict[self.Name]['В блокнот']=0
    self.timerM = QtCore.QTimer()
    self.timerM.timeout.connect(self.NewDataTimerM)
    self.timerM.start(100)

  def LoadState(self):
    super().LoadState()

  def SaveState(self):
    super().SaveState()

  def NewData1(self, ddata):
    if self.measR_B in ddata:
      self.tmpVal=int(ddata[self.measR_B][1])
      self.win.lcdMain.display(self.formS.format(self.tmpVal))
      self.win.lblEd.setText(self.I_ed)

      Results.Result_Dict[self.Name][self.OutputVal[0]]=self.tmpVal
      Results.Result_Dict[self.Name]['Параметр '+self.OutputVal[0]]='Сопротивление'
      Results.Result_Dict[self.Name]['Единица '+self.OutputVal[0]]=''
    if(Results.Result_Dict[self.Name]['В блокнот']!=2):Results.Result_Dict[self.Name]['В блокнот']=self.InLight_Notepad
    Results.Result_Dict[self.Name]['ID_VP']=self.ID_VP
    Results.Result_Dict[self.Name]['LastProfil']=self.LastProfil
    if(Results.Result_Dict[self.Name]['В блокнот']==2):
        Results.Result_Dict[self.Name]['В блокнот']=0
        self.InLight_Notepad=0
    self.timeT = ddata[self.measR_B][2] 
      #print(self.timeT)

  def NewData(self, ddata):

    if self.measR_B in ddata:
       self.lastRD = ddata[self.measR_B][1]
       self.tmpVal1=self.lastRD

    if self.measR in ddata:
      self.lastR = ddata[self.measR][1]
      self.tmpVal0=self.lastR

  def NewDataTimerM(self):
      q=0
      a=datetime.today()
      a1=a.date()
      a2=a.time()
      dt1=str(a1)+"  \t"+a2.strftime("%H:%M:%S") 
      #self.win.lblDateTime.setText(str(dt1))
######################################################
      #self.tmpVal_3=self.lastR/100000000.0
      '''
      try:
        self.K_temp=eval(self.win.leK_temp.text(), {}, {})
      except:
          K_temp=1.0'''
      self.Temp=0
      self.Aetu=0
      self.tmpBd=0.0
      self.tmpAd=0.0
      if(self.lastRD==1):
          a=0

      if(self.lastRD==2):
          a=0

      if(self.lastRD==3):
          a=0

      if(self.lastRD==4):
          a=0

      if(self.lastRD==5):
          a=0

      if(self.lastRD==6):
          a=0

      if(self.lastRD>6) :
          a=0

       

      if (self.tmpVal1==1)or(self.tmpVal1==2)or(self.tmpVal1==3)or(self.tmpVal1==4):# МОм
          self.KBand=1000000.0
          self.KSaltBand=1
      if (self.tmpVal1>4)and(self.tmpVal1<8): # кОм
          self.KBand=1000.0
          self.KSaltBand=1000.0
      ###############################################################
      '''self.lastR=70.3'''

      self.tmpX=0
      self.tmpX_t=0.0
      self.tmpX_=0
      self.tmpX_ms=0
      self.tmpR=0
      self.tmpC=1.956947E-6
      
      self.tmpR=(float(self.lastR)*511.0*float(10**3))/(511.0*float(10**3)-float(self.lastR))
      #self.tmpR=float(self.lastR)
      self.tmpVal_3=self.tmpR

      ###############################################################
      if (self.tmpVal_3>=100000): # 100кОм
          self.tmpVal_R=self.tmpVal_3/1000000 # МОм
          self.R_ed='МОм'
          #self.formS_4 = "{:"+str(self.widthD)+"."+str(3)+"f}"

      if (self.tmpVal_3<100000)and(self.tmpVal_3>=1000): # 1кОм
          self.tmpVal_R=self.tmpVal_3/1000 # кОм
          self.R_ed='кОм'
          #self.formS_4 = "{:"+str(self.widthD)+"."+str(3)+"f}"

      if (self.tmpVal_3<1000): # 1кОм
          self.tmpVal_R=self.tmpVal_3 # Ом
          self.R_ed='Ом'
          #self.formS_4 = "{:"+str(self.widthD)+"."+str(1)+"f}"
      self.win.lblEd.setText(self.R_ed)


      #self.win.lcdMain_3.display(self.formS.format(self.tmpVal_3))
      if (self.tmpVal_R>1000.0): self.win.lcdMain.display("{:4.0f}".format(self.tmpVal_R))
      if ((self.tmpVal_R>=100.0)&(self.tmpVal_R<1000.0)): self.win.lcdMain.display("{:3.1f}".format(self.tmpVal_R))
      if ((self.tmpVal_R>=10.0)&(self.tmpVal_R<100.0)): self.win.lcdMain.display("{:2.2f}".format(self.tmpVal_R))
      if ((self.tmpVal_R>=1.0)&(self.tmpVal_R<10.0)): self.win.lcdMain.display("{:1.3f}".format(self.tmpVal_R))
      if (self.tmpVal_R<1.0): self.win.lcdMain.display("{:0.4f}".format(self.tmpVal_R))

      Results.Result_Dict[self.Name][self.OutputVal[0]]=self.tmpVal_R
      Results.Result_Dict[self.Name]['Параметр '+self.OutputVal[0]]='Сопротивление'
      Results.Result_Dict[self.Name]['Единица '+self.OutputVal[0]]=self.R_ed
      if(Results.Result_Dict[self.Name]['В блокнот']!=2):Results.Result_Dict[self.Name]['В блокнот']=self.InLight_Notepad
      Results.Result_Dict[self.Name]['ID_VP']=self.ID_VP
      Results.Result_Dict[self.Name]['LastProfil']=''
      if(Results.Result_Dict[self.Name]['В блокнот']==2):
        Results.Result_Dict[self.Name]['В блокнот']=0
        self.InLight_Notepad=0

      Results.Result_Dict[(self.Name)][('Value')]=self.tmpVal_R



      if (self.vCE.Close_Config_Flag==1)and(self.closeFlag==0): 
          # Остановка таймера опроса
          self.timerM.stop();
          self.closeFlag=1      
          self.win.close()
          #self.delete()
          a=0

class CfpR_Band(QtGui.QMainWindow, Ui_fpVATP):
      
  def __init__(self, numDigits, vR_Band):
    """ numDigits - суммарное кол-во выводимых знаков результата (C учетом запятой) """
    super(CfpR_Band, self).__init__() 

    self.setupUi(self)
    self.setStyleSheet("QMainWindow {background: '#F76F6F';}")
    self.Type=8
    self.Reset_Flag=1
    self.vR_Band = vR_Band
    rect = QtCore.QRect()   
    w=self.vR_Band.width 
    h=self.vR_Band.height
    x=self.vR_Band.x         
    y=self.vR_Band.y  
    rect = QtCore.QRect(x,y,w,h) 
    rect.setRect(x,y,w,h) 
    self.setGeometry(rect)  
   
    
    self.vR_Band.ID_VP=self.vR_Band.dSize.setdefault('ID_VP','0')
    self.lblID.setText(str(self.vR_Band.ID_VP))
    self.vR_Band.dSize['ID_VP']=self.vR_Band.ID_VP 

    self.basePS = None
    self.lcdMain.setDigitCount(numDigits)
    self.tbSaveToNotepad_.clicked.connect(self.on_tbSaveToNotepad_clicked)
        # Common menu of VP
    self.actTech = QtGui.QAction("Проба", self) 
    self.actTech.triggered.connect(self.on_Proba_toggle)  
    self.menubar.addAction(self.actTech)

    self.actTech = QtGui.QAction("О приборе", self) 
    self.actTech.triggered.connect(self.on_AboutVP_toggle)  
    self.menubar.addAction(self.actTech)
    self.lcdMain.setDigitCount(6)
    ## End of common menu of VP
    self.trAutoScan =None
    self.trAutoScan = self.startTimer(1000) 


  def on_Proba_toggle(self):
      self.vR_Band.winProbaID.show()
      w=0

  def on_AboutVP_toggle(self):
      self.vR_Band.winAboutVP.show()
      w=0

  def timerEvent(self, e):
  #Отображение даты по таймеру
        if (self.vR_Band.vCE.Close_Config_Flag==1)and(self.vR_Band.closeFlag==0): 
          self.vR_Band.closeFlag=1      
          self.close()
          #self.delete()
          a=0


  def on_tbSaveToNotepad_clicked(self):
      if(Results.Result_Dict[self.vR_Band.Name]['В блокнот']==0):
        self.vR_Band.ID_VP=self.lblID.text()
        self.vR_Band.InLight_Notepad=1
      q=0     

  def show(self, newsize = None):
    """ newsize - экземпляр QSize для передачи новых размеров окна """
    super().show()   # важно выполнить ПЕРЕД resize - иначе resize может не пройти
    if newsize:  self.resize(newsize)

  def closeEvent(self, event):
    self.vR_Band.SaveState()

    rect = self.geometry()
    self.vR_Band.dSize['x'] = rect.left()
    self.vR_Band.dSize['y'] = rect.top()
    self.vR_Band.dSize['height'] = rect.height() 
    self.vR_Band.dSize['width'] = rect.width()
    event.accept() 

  def resizeEvent(self, event):
    a=0
    """rect = self.centralwidget.geometry()
    font = self.llData.font()
    fm = QtGui.QFontMetrics(font) 
    textH = fm.boundingRect(self.llData.text()).height()
    # print("layout.height = {} text.height = {} pointS = {}".format(rect.height(), textH, font.pointSize()))
    if self.basePS:
      # базовое значение уже зафиксировано - масштабируем 
      delta = rect.height() - textH
      if delta > 2 * self.basePS[1]:   deltaPS = 1
      elif delta < 1.5 * self.basePS[1]: deltaPS = -1  
      else:                              deltaPS = 0
      if deltaPS:
        font.setPointSize(font.pointSize() + deltaPS)
        self.llData.setFont(font)               
    else:    
      # первая отрисовка лицевой панели - захватываем базовые размеры для последующего масштабирования
      # TODO - проверить не повлияет ли стартовое восстановление прошлой геометрии окна
      self.basePS = (font.pointSize(), rect.height() - textH)  

    super().resizeEvent(event)"""


class CfmVPPassword(QtGui.QMainWindow, Ui_fmVPPassword):
  """Форма ввода пароля"""

  def __init__(self,vCnd):
    """ Инициализация формы ввода пароля"""
    global vinstrD
    global cstateD

    super().__init__()      
    self.setupUi(self)


    self.vCnd=vCnd
    self.fRec = False
    self.fFirstShow = True

    #if 'CfmVPPassword' in cstateD: 
    #  self.dictState = cstateD['CfmVPPassword'] 
    #else:
    #  self.dictState = {}
    #  cstateD['CfmVPPassword'] = self.dictState 

    self.setWindowTitle("Пароль настройки")
    self.tbEnterPassword.clicked.connect(self.on_tbEnterPasword_toggle)
    self.lePassword.editingFinished.connect(self.on_lePasswordFinished)
  

  def on_tbEnterPasword_toggle(self):
      """ Нажатие кнопки ввод по вводу пароля"""
      a=''
      try:
         a=eval(self.lePassword.text(), {}, {})
      except: q=0
      if (a==456):
         if (self.vCnd.winCCond.chbBKd.checkState()):
             self.vCnd.winCCond.gbxBKd.setEnabled(True)
             self.vCnd.winCCond.leCondSet.setEnabled(True)
             self.vCnd.winCCond.lblKD6_2.setEnabled(True)
             self.vCnd.winCCond.tbRecalc.setEnabled(True)
             self.close()
      else: 
             self.vCnd.winCCond.gbxBKd.setEnabled(False)
             self.vCnd.winCCond.leCondSet.setEnabled(False)
             self.vCnd.winCCond.lblKD6_2.setEnabled(False)
             self.vCnd.winCCond.tbRecalc.setEnabled(False)
      self.lePassword.setText("")


 
  def on_lePasswordFinished(self):
      a=1


class CfmSelectV(QtGui.QMainWindow, Ui_fmSelectV):
  """Форма ввода пароля"""

  def __init__(self,vCond):
    """ Инициализация формы ввода пароля"""
    global vinstrD
    global cstateD

    super().__init__()      
    self.setupUi(self)
    self.setupUi(self)
    self.vCond = vCond
    self.ShowFlag=0
    #self.vCond.Profils.CreateVVTable()
    
    self.tbSelect.clicked.connect(self.on_Change_Any_SelectV) 
    self.tbAdd.clicked.connect(self.on_tbAdd_SelectV) 
    self.tbChange.clicked.connect(self.on_tbChange_SelectV) 
    self.tbDel.clicked.connect(self.on_tbDel_SelectV) 
    self.lwV.clicked.connect(self.on_lwV_clicked_toggle)
    self.lwV.doubleClicked.connect(self.on_lwV_doubleClicked_toggle)

  def show(self, vCond): 
    self.on_Init_Any_SelectV() 
    self.vCond.Profils.InitVV()
    super().show()
    q=0  
    
  def on_Init_Any_SelectV(self):
      self.V_vo=self.vCond.Profils.V_vo
      self.TK_V_vo=self.vCond.Profils.TK_V_vo 
      self.leV_Name.setText(str(self.V_vo))
      self.leTKR.setText(str(self.TK_V_vo))
       

  def on_Change_Any_SelectV(self):
      self.V_vo=0.0
      self.TK_V_vo=0.0
      self.V_vo=self.leV_Name.text()
      self.TK_V_vo=self.leTKR.text()
      #a=self.V_vo
      #b=self.TK_V_vo
      #self.vCond.Profils.ChangeCurrProfil_SelectV(a, b)
      self.vCond.Profils.ChangeCurrProfil_SelectV(self.V_vo, self.TK_V_vo)
      self.vCond.win.label_8.setText(self.vCond.Profils.V_vo + "  "+str(self.vCond.Profils.TK_V_vo)+ "% "+str(self.vCond.Profils.T_ATK)+ " oC"  )
      self.vCond.Profils.SaveCurrProfil()
  def on_tbAdd_SelectV(self):
      V_vo=self.leV_Name.text()
      TK_V_vo=self.leTKR.text()
      self.vCond.Profils.AddVVTable(V_vo,TK_V_vo)
      self.vCond.Profils.InitVV()
      q=0
       
  def on_tbChange_SelectV(self):
      V_vo=self.leV_Name.text()
      TK_V_vo=self.leTKR.text()
      a=self.lwV.currentRow()
      self.vCond.Profils.ChangeVV(a+1,V_vo,TK_V_vo)
      self.vCond.Profils.InitVV()
      self.vCond.Profils.ChangeCurrProfil_SelectV(self.V_vo, self.TK_V_vo)
      self.vCond.Profils.SaveCurrProfil()
      q=0
        
  def on_tbDel_SelectV(self):
      a=self.lwV.currentRow()
      self.vCond.Profils.DelVV(a+1)
      self.vCond.Profils.InitVV()
      self.vCond.Profils.ChangeCurrProfil_SelectV(self.V_vo, self.TK_V_vo)
      self.vCond.Profils.SaveCurrProfil()
      q=0
        
  def on_lwV_clicked_toggle(self):
      a=self.lwV.currentRow()
      self.vCond.Profils.SelectVV(a+1)
      self.leV_Name.setText(str(self.vCond.Profils.V_vo))
      self.leTKR.setText(str(self.vCond.Profils.TK_V_vo))

      q=0
       
  def on_lwV_doubleClicked_toggle(self):
      self.vCond.Profils.ChangeCurrProfil_SelectV(self.vCond.Profils.V_vo, self.vCond.Profils.TK_V_vo)
      self.vCond.Profils.SaveCurrProfil()
      self.vCond.win.label_8.setText(self.vCond.Profils.V_vo + "  "+str(self.vCond.Profils.TK_V_vo)+ "% "+str(self.vCond.Profils.T_ATK)+ " oC" )
      self.close()
      q=0
       

class CfmTKR(QtGui.QMainWindow, Ui_fmTKR):
  """Форма ввода пароля"""

  def __init__(self,vCond):
    """ Инициализация формы ввода пароля"""
    global vinstrD
    global cstateD

    super().__init__()      
    self.setupUi(self)
    self.setupUi(self)
    self.vCond = vCond
    self.ShowFlag=0
    self.T_ATK=0.0
    self.rb_25.toggled.connect(self.on_T20_toggle)
    self.rb_20.toggled.connect(self.on_T25_toggle)
    self.rb_R.toggled.connect(self.on_TR_toggle)
    self.tbSave.clicked.connect(self.on_Change_Any_TKR)

  def show(self, vCond): 
    self.on_Init_Any_TKR()  
    super().show()  

  def on_Init_Any_TKR(self):
      self.T_grad=self.vCond.Profils.T_grad
      self.T_ATK=self.vCond.Profils.T_ATK
      self.leTemp_R.setText(str(self.T_ATK)) 
      self.leTemp.setText(str(self.T_grad))   
      if (float(self.T_ATK)==25.0):
          self.rb_25.setChecked(True) 
          self.rb_20.setChecked(False) 
          self.rb_R.setChecked(False)  
      if (float(self.T_ATK)==20.0):
          self.rb_25.setChecked(False) 
          self.rb_20.setChecked(True) 
          self.rb_R.setChecked(False) 
      if (self.T_ATK!=25.0)&(self.T_ATK!=20.0):
          self.rb_25.setChecked(False) 
          self.rb_20.setChecked(False) 
          self.rb_R.setChecked(True)   

  def on_Change_Any_TKR(self):
        #if(self.ShowFlag==1):
        
        self.T_grad=0.0
        if (self.rb_25.isChecked()): self.T_ATK=25
        if (self.rb_20.isChecked()): self.T_ATK=20
        if (self.rb_R.isChecked()): self.T_ATK=self.leTemp_R.text()
        self.T_grad=self.leTemp.text()
        self.vCond.Profils.ChangeCurrProfil_TKR(self.T_ATK, self.T_grad)
        self.vCond.Profils.SaveCurrProfil()
        self.vCond.win.label_8.setText(self.vCond.Profils.V_vo + "  "+str(self.vCond.Profils.TK_V_vo)+ "% "+str(self.vCond.Profils.T_ATK)+ " oC"  )

  def on_T20_toggle(self):
   #      self.T_ATK=20.0
   q=1

  def on_T25_toggle(self):
        #self.T_ATK=25.0
        q=1

  def on_TR_toggle(self):
        #self.T_ATK=self.leTemp_R.text()
        q=1
