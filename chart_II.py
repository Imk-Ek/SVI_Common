

import sys, traceback
import logging
from PyQt4 import QtCore, QtGui 
#import sstate
#from common import *
import Results

from PyQt4 import QtCore, QtGui 

from fpChart_II import Ui_fpChart_II
#####################################
import math
import sys
import numpy
from PyQt4 import Qt
import PyQt4.Qwt5 as Qwt
from vinstr import *

#from PyQt4.Qt import *
#from PyQt4.Qwt5 import *
#import pyqtSlot,SIGNAL,SLOT
#####################################

class CChart_II(CVInstr):
  """ виртуальный """
  #  measN - наименование измерительного канала, связанного с данным экземпляром вольтметра
  #  widthD - суммарное кол-во выводимых знаков результата (БЕЗ учета запятой)
  #  precD  - кол-во знаков после запятой 
  #  formS  - строка форматирования для вывода результата (под НОВЫЙ метод format)

  def __init__(self,vCE,  dcfg, dstate = {}, dSize={}, fTech = False):
    super().__init__(dcfg, dstate, fTech)
    self.vCE=vCE
    self.closeFlag=0 
    self.Name=dcfg['наименование']
    # TODO обработку ошибок конфигурации
    self.measN ='0'# self.dictCfg["канал_"]
    self.dictCfg["meas"] = [self.measN] # фактически вносится в vinstrD
    self.ParamMess=dSize['VPParam']
    self.Reset_Flag=0
    self.InputUnit=[0,0,0]
    self.InputVal=[0,0,0]
    self.OutputVal=[0,0,0]
    self.InputUnit[0]=dSize['VPChModulNameList'][0]
    self.InputUnit[1]=dSize['VPChModulNameList'][1]
    # self.InputUnit[2]=dSize['VPChModulNameList'][2]
    self.InputVal[0]=dSize['VPChNameList'][0]
    self.InputVal[1]=dSize['VPChNameList'][1]
    #self.InputVal[2]=dSize['VPChNameList'][2]
    self.tmpVal_Param_1='-1'
    self.tmpVal_EDIzm_1='-1'
    self.tmpVal_Param_2='-1'
    self.tmpVal_EDIzm_2='-1'
    self.InLight_Notepad=0
    self.ID_VP='0'
    '''self.OutputVal[0]=dSize['VPChOutTypeList'][0]
    self.OutputVal[1]=dSize['VPChOutTypeList'][1]
    self.OutputVal[2]=dSize['VPChOutTypeList'][2]
    self.OutputVal[3]=dSize['VPChOutTypeList'][3]'''
    self.MessMode=0
    self.Val_min_1=0
    self.Val_max_1=0
    self.Val_min_2=0
    self.Val_max_2=0

    self.widthD = 6 # 4
    self.precD = 3  # 3
    self.formS = "{:"+str(self.widthD)+"."+str(self.precD)+"f}"
    self.dSize=dSize
    self.width=self.dSize.setdefault('width',100)
    self.height=self.dSize.setdefault('height',100)
    self.x=self.dSize.setdefault('x',100)
    self.y=self.dSize.setdefault('y',100) 
    self.win = CfpChart_II(self.widthD + 1, self)
    self.LoadState()
   

  def LoadState(self):
    super().LoadState()


  def SaveState(self):
    super().SaveState()


  def NewData(self, ddata):
    #global Result_Dict
    self.tmpVal4=Results.Result_Dict
    '''
    if self.measN in ddata:
      #self.win.lcdVolt.display(self.formS.format(ddata[self.measN][1]))
      self.tmpVal=ddata[self.measN][1]

    if self.win.Reset_Flag==1:
        self.Val_min=self.tmpVal
        self.Val_max=self.tmpVal
        self.win.Reset_Flag=0
        self.win.win_Chart.Reset_Flag=0
        self.win.win_Chart.Count_draw=0

    if self.tmpVal<self.Val_min:
        self.Val_min=self.tmpVal
    if self.tmpVal>self.Val_max:
        self.Val_max=self.tmpVal'''
    '''
        self.win.win_Chart.Sens_1.show()
        self.win.win_Chart.Sens_2.hide()
    self.win.win_Chart.lcdMain_mg.display(self.formS.format(self.tmpVal))
    self.win.win_Chart.lcdMain_mg_min.display(self.formS.format(self.Val_min))
    self.win.win_Chart.lcdMain_mg_max.display(self.formS.format(self.Val_max))
    self.win.win_Chart.y_draw=numpy.append(self.win.win_Chart.y_draw,self.tmpVal)
    self.win.win_Chart.x_draw=numpy.append(self.win.win_Chart.x_draw,self.win.win_Chart.Count_draw)
    self.win.win_Chart.Count_draw=self.win.win_Chart.Count_draw+1
    self.win.win_Chart.Sens_1.setData(self.win.win_Chart.x_draw,self.win.win_Chart.y_draw)
    #Results.Result_Dict[(self.Name)][('Value')]=self.tmpVal
    #Results.Result_Dict[(self.Name)][('EdIzm')]=0'''

  def Test(self):
    try:
     self.tmpVal4=Results.Result_Dict[self.InputUnit[0]][self.InputVal[0]]
    except:self.tmpVal4=-1
    try:
     self.tmpVal_Param_1=Results.Result_Dict[self.InputUnit[0]]['Параметр '+self.InputVal[0]]
     self.tmpVal_EDIzm_1=Results.Result_Dict[self.InputUnit[0]]['Единица '+self.InputVal[0]]

    except:
     self.tmpVal_Param_1=' '
     self.tmpVal_EDIzm_1=' '
    try:
     self.tmpVal5=Results.Result_Dict[(self.InputUnit[1])][self.InputVal[1]]
    except:self.tmpVal5=-1
    try:
     self.tmpVal_Param_2=Results.Result_Dict[self.InputUnit[1]]['Параметр '+self.InputVal[1]]
     self.tmpVal_EDIzm_2=Results.Result_Dict[self.InputUnit[1]]['Единица '+self.InputVal[1]]

    except:
     self.tmpVal_Param_2=' '
     self.tmpVal_EDIzm_2=' '

    if self.Reset_Flag==1:
     self.Val_min_1=self.tmpVal4
     self.Val_max_1=self.tmpVal4
     self.Val_min_2=self.tmpVal5
     self.Val_max_2=self.tmpVal5
     self.Reset_Flag=0


    if self.tmpVal4<self.Val_min_1:
        self.Val_min_1=self.tmpVal4
    if self.tmpVal4>self.Val_max_1:
        self.Val_max_1=self.tmpVal4

    if self.tmpVal5<self.Val_min_2:
        self.Val_min_2=self.tmpVal5
    if self.tmpVal5>self.Val_max_2:
        self.Val_max_2=self.tmpVal5


    self.win.Init_EdIzmParam()
    self.win.lcdMain_mg.display(self.formS.format(self.tmpVal4))
    self.win.lcdMain_percent.display(self.formS.format(self.tmpVal5))
    self.win.lcdMain_mg_min.display(self.formS.format(self.Val_min_1))
    self.win.lcdMain_percent_min.display(self.formS.format(self.Val_min_2))
    self.win.lcdMain_mg_max.display(self.formS.format(self.Val_max_1))
    self.win.lcdMain_percent_max.display(self.formS.format(self.Val_max_2))

    self.win.Sens_1.show()
    self.win.Sens_2.show()
    self.win.y_draw=numpy.append(self.win.y_draw,self.tmpVal4)
    self.win.y_p_draw=numpy.append(self.win.y_p_draw,self.tmpVal5)
    self.win.x_draw=numpy.append(self.win.x_draw,self.win.Count_draw)
    self.win.Count_draw=self.win.Count_draw+1
    self.win.Sens_1.setData(self.win.x_draw,self.win.y_draw)
    self.win.Sens_2.setData(self.win.x_draw,self.win.y_p_draw)


#---


class CfpChart_II(QtGui.QMainWindow, Ui_fpChart_II):
  # fRec - флаг для блокировки рекурентного вызова closeEvent

  def __init__(self, numDigits, vfpChart_II):
    super(CfpChart_II, self).__init__()      
    self.setupUi(self)
    self.setStyleSheet("QMainWindow {background: '#FDE3C3';}")
    self.vfpChart_II=vfpChart_II
    rect = QtCore.QRect()   
    #rect.normalized()   
    w=self.vfpChart_II.width 
    h=self.vfpChart_II.height
    x=self.vfpChart_II.x         
    y=self.vfpChart_II.y  
    rect = QtCore.QRect(x,y,w,h) 
    rect.setRect(x,y,w,h) 
    self.setGeometry(rect)
    self.timer = QtCore.QTimer()

    self.timer.timeout.connect(self.on_Test2_toggle)
    self.x_draw=numpy.array([])
    self.y_draw=numpy.array([])
    self.y_p_draw=numpy.array([])
    self.Count_draw=0
    self.Marker=numpy.array([])
    self.Count_Marker=0
    
    self.vfP=100;
    try:
      self.AsixName=self.vfpChart_II.tmpVal_Param_1
      self.Ed_1=self.vfpChart_II.tmpVal_EdIzm_1
    except:
      self.AsixName='_'
      self.Ed_1='_'
      self.Ed_2='_'
    
    '''
    if self.vfP==1: 
        self.AsixName='Ток'
        self.Ed_1='нА'
        self.Ed_2=''
        self.lcdMain_percent.setVisible(0)
        self.lcdMain_percent_min.setVisible(0)
        self.lcdMain_percent_max.setVisible(0)

    if self.vfP==2: 
        self.AsixName='Напряжение'
        self.Ed_1='В'
        self.Ed_2=''
        self.lcdMain_percent.setVisible(0)
        self.lcdMain_percent_min.setVisible(0)
        self.lcdMain_percent_max.setVisible(0)

    if self.vfP==3: 
        self.AsixName='Температура'
        self.Ed_1='<sup>o</sup>C'
        self.Ed_2=''
        self.lcdMain_percent.setVisible(0)
        self.lcdMain_percent_min.setVisible(0)
        self.lcdMain_percent_max.setVisible(0)

    if self.vfP==4: 
        self.AsixName='pH'
        self.Ed_1='%'
        self.Ed_2=''
        self.lcdMain_percent.setVisible(0)
        self.lcdMain_percent_min.setVisible(0)
        self.lcdMain_percent_max.setVisible(0)

    if self.vfP==5: 
        self.AsixName='Концентрация'
        self.Ed_1='мг/дм<sup>3</sup>'
        self.Ed_2='%'
        self.lcdMain_percent.setVisible(1)
        self.lcdMain_percent_min.setVisible(1)
        self.lcdMain_percent_max.setVisible(1)
    if self.vfP==6: 
        self.AsixName='Давление'
        self.Ed_1='кПа'
        self.Ed_2=''
        self.lcdMain_percent.setVisible(0)
        self.lcdMain_percent_min.setVisible(0)
        self.lcdMain_percent_max.setVisible(0)
    if self.vfP==7: 
        self.AsixName='Сопротивление'
        self.Ed_1='Ом/м'
        self.Ed_2=''
        self.lcdMain_percent.setVisible(0)
        self.lcdMain_percent_min.setVisible(0)
        self.lcdMain_percent_max.setVisible(0)
    if self.vfP==8: 
        self.AsixName='Сопротивление.Диапазон'
        self.Ed_1=''
        self.Ed_2=''
        self.lcdMain_percent.setVisible(0)
        self.lcdMain_percent_min.setVisible(0)
        self.lcdMain_percent_max.setVisible(0)
    self.lcdMain_percent.setVisible(1)
    '''
    self.lblVal_1.setText(self.Ed_1)
    self.lblVal_2.setText(self.Ed_1)
    self.lblVal_3.setText(self.Ed_1)
    self.lblVal_4.setText(self.Ed_2)
    self.lblVal_5.setText(self.Ed_2)
    self.lblVal_6.setText(self.Ed_2)
    self.rbCon.setText(self.AsixName)
    self.Init_Draw_()
    self.Init__Draw()


    self.actTech = QtGui.QAction("Сохранить PDF", self) 
    self.actTech.triggered.connect(self.exportPDF)  
    self.menubar.addAction(self.actTech)

    self.tbResetViewPar.clicked.connect(self.ResetDraw)
    self.tbAddMarker.clicked.connect(self.AddMarker)
    self.tbDelMarker.clicked.connect(self.DelMarker)
    self.chbPause.stateChanged.connect(self.PauseDraw)
    self.chbZoom.stateChanged.connect(self.zoom)
    self.Reset_Flag=1
    

    


    
  def on_Test2_toggle(self):
      self.vfpChart_II.Test()
      self.qwtPlot.replot()
      #self.setWindowTitle('TEST')#self.vfP.windowTitle())  

      if (self.vfpChart_II.vCE.Close_Config_Flag==1)and(self.vfpChart_II.closeFlag==0): 
          self.vfpChart_II.closeFlag=1      
          self.close()


  def exportPDF(self):
        if Qt.QT_VERSION > 0x040100:
            fileName = Qt.QFileDialog.getSaveFileName(
                self,
                'Export File Name',
                '__-%s.pdf' % Qt.qVersion(),
                'PDF Documents (*.pdf)')

        if not fileName=="":
            printer = Qt.QPrinter()
            printer.setOutputFormat(Qt.QPrinter.PdfFormat)
            printer.setOrientation(Qt.QPrinter.Landscape)
            printer.setOutputFileName(fileName)

            printer.setCreator('_ example')
            self.qwtPlot.print_(printer)

    # exportPDF()
  def Init_EdIzmParam(self):
      try:
        self.AsixName=self.vfpChart_II.tmpVal_Param_1
        self.Ed_1=self.vfpChart_II.tmpVal_EDIzm_1
      except:
        self.AsixName='_'
        self.Ed_1='_'
        self.Ed_2='_'
      try:
        #self.AsixName=self.vfpChart_II.tmpVal_Param_1
        self.Ed_2=self.vfpChart_II.tmpVal_EDIzm_2
      except:
        #self.AsixName='_'

        self.Ed_2='_'
      self.qwtPlot.setAxisTitle(Qwt.QwtPlot.yLeft, self.AsixName+', ' +self.Ed_1+' -->')
      self.lblVal_1.setText(self.Ed_1)
      self.lblVal_2.setText(self.Ed_1)
      self.lblVal_3.setText(self.Ed_1)
      self.lblVal_4.setText(self.Ed_2)
      self.lblVal_5.setText(self.Ed_2)
      self.lblVal_6.setText(self.Ed_2)
      self.rbCon.setText(self.AsixName)
      #self.Sens_1. = Qwt.QwtPlotCurve( self.Ed_1)
      #self.Sens_2 = Qwt.QwtPlotCurve( self.Ed_2)
    
  def Init_Draw_(self):
      self.x_draw=numpy.array([])
      self.y_draw=numpy.array([])
      self.y_p_draw=numpy.array([])
      self.Count_draw=0

      self.qwtPlot.setTitle(' ')
      self.qwtPlot.insertLegend(Qwt.QwtLegend(), Qwt.QwtPlot.RightLegend)

        # a variation on the C++ example #self.qwtPlot.plotLayout().setAlignCanvasToScales(False)
      #self.qwtPlot.plotLayout().setAlignCanvasToScales(False)
      
      
      self.grid = Qwt.QwtPlotGrid()
      self.grid.attach(self.qwtPlot)
      self.grid.setPen(Qt.QPen(Qt.Qt.black, 0, Qt.Qt.DotLine))
        
        # set axis titles
      self.qwtPlot.setAxisTitle(Qwt.QwtPlot.xBottom, 'отсчеты -->')
      self.qwtPlot.setAxisTitle(Qwt.QwtPlot.yLeft, self.AsixName+', ' +self.Ed_1+' -->')

        # insert a few curves
      self.Sens_1 = Qwt.QwtPlotCurve( self.Ed_1)
      self.Sens_1.setPen(Qt.QPen(Qt.Qt.blue))
      self.Sens_1.attach(self.qwtPlot)
      self.Sens_2 = Qwt.QwtPlotCurve(self.Ed_2)
      self.Sens_2.setPen(Qt.QPen(Qt.Qt.red))
      self.Sens_2.attach(self.qwtPlot)

      self.Sens_2.setData(self.x_draw,self.y_p_draw)
      self.Sens_1.setData(self.x_draw,self.y_draw)

      #if self.vfP.Type==5:

        # insert a horizontal marker at y = 0



        # insert a vertical marker at x = 2 pi


        # replot
      self.qwtPlot.replot()
      self.timer.start(1000)

  def Init_DataDraw_(self):
      #numpy.insert(self.y_draw,self.Count_draw,self.Count_draw*self.Count_draw)
      #numpy.insert(self.x_draw,self.Count_draw,self.Count_draw)
      self.y_draw=numpy.append(self.y_draw,self.Count_draw*self.Count_draw)
      self.x_draw=numpy.append(self.x_draw,self.Count_draw)
      self.Count_draw=self.Count_draw+1
      if self.vfP.Type==5: self.Sens_2.setData(self.x_draw,self.y_draw)
      self.qwtPlot.replot()
  
  def Init__Draw(self):
        ##QMainWindow.__init__(self, *args)

        ##self.plot = BodePlot(self)
        ##self.plot.setMargin(5)

        ##self.setContextMenuPolicy(Qt.NoContextMenu)
        
        self.zoomers = []
        zoomer = Qwt.QwtPlotZoomer(
            self.qwtPlot.xBottom,
            self.qwtPlot.yLeft,
            Qwt.QwtPicker.DragSelection,
            Qwt.QwtPicker.AlwaysOff,
            self.qwtPlot.canvas())
        zoomer.setRubberBandPen(Qt.QPen(Qt.Qt.green))
        self.zoomers.append(zoomer)

        zoomer = Qwt.QwtPlotZoomer(
            self.qwtPlot.xTop,
            self.qwtPlot.yRight,
            Qwt.QwtPicker.PointSelection | Qwt.QwtPicker.DragSelection,
            Qwt.QwtPicker.AlwaysOff,
            self.qwtPlot.canvas())
        zoomer.setRubberBand(Qwt.QwtPicker.NoRubberBand)
        self.zoomers.append(zoomer)

        self.picker = Qwt.QwtPlotPicker(
            self.qwtPlot.xBottom,
            self.qwtPlot.yLeft,
            Qwt.QwtPicker.PointSelection | Qwt.QwtPicker.DragSelection,
            Qwt.QwtPlotPicker.CrossRubberBand,
            Qwt.QwtPicker.AlwaysOn,
            self.qwtPlot.canvas())
        self.picker.setRubberBandPen(Qt.QPen(Qt.Qt.green))
        self.picker.setTrackerPen(Qt.QPen(Qt.Qt.black))
 
        ##self.setCentralWidget(self.plot)
        """
        toolBar = QToolBar(self)
        self.addToolBar(toolBar)
        
        btnZoom = QToolButton(toolBar)
        btnZoom.setText("Zoom")
        btnZoom.setIcon(QIcon(QPixmap(zoom_xpm)))
        btnZoom.setCheckable(True)
        btnZoom.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        toolBar.addWidget(btnZoom)

        btnPrint = QToolButton(toolBar)
        btnPrint.setText("Print")
        btnPrint.setIcon(QIcon(QPixmap(print_xpm)))
        btnPrint.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        toolBar.addWidget(btnPrint)
        self.connect(btnPrint, SIGNAL('clicked()'), self.print_)

        if QT_VERSION >= 0X040100:
            btnPDF = QToolButton(toolBar)
            btnPDF.setText("PDF")
            btnPDF.setIcon(QIcon(QPixmap(print_xpm)))
            btnPDF.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
            toolBar.addWidget(btnPDF)
            self.connect(btnPDF, SIGNAL('clicked()'), self.exportPDF)

        if QT_VERSION >= 0x040300:
            btnSVG = QToolButton(toolBar)
            btnSVG.setText("SVG")
            btnSVG.setIcon(QIcon(QPixmap(print_xpm)))
            btnSVG.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
            toolBar.addWidget(btnSVG)            
            self.connect(btnSVG, SIGNAL('clicked()'), self.exportSVG)
            
        toolBar.addSeparator()

        dampBox = QWidget(toolBar)
        dampLayout = QHBoxLayout(dampBox)
        dampLayout.setSpacing(0)
        dampLayout.addWidget(QWidget(dampBox), 10) # spacer
        dampLayout.addWidget(QLabel("Damping Factor", dampBox), 0)
        dampLayout.addSpacing(10)

        self.cntDamp = QwtCounter(dampBox)
        self.cntDamp.setRange(0.01, 5.0, 0.01)
        self.cntDamp.setValue(0.01)
        dampLayout.addWidget(self.cntDamp, 10)

        toolBar.addWidget(dampBox)"""

        self.statusBar()
        
        self.zoom(False)
        self.showInfo()
        '''
        self.connect(self.cntDamp,
                     SIGNAL('valueChanged(double)'),
                     self.plot.setDamp)
        self.connect(btnZoom,
                     SIGNAL('toggled(bool)'),
                     self.zoom)'''
        self.connect(self.picker,
                     Qt.SIGNAL('moved(const QPoint &)'),
                     self.moved)
        self.connect(self.picker,
                     Qt.SIGNAL('selected(const QPolygon &)'),
                     self.selected)

    # __init__Draw()
  def showInfo(self, text=None):
      if not text:
          if self.picker.rubberBand():
              text = 'Cursor Pos: Press left mouse button in plot region'
          else:
              text = 'Zoom: Press mouse button and drag'
                
      self.statusBar().showMessage(text)

  def zoom(self, on):
      if on>0: on=1
      self.zoomers[0].setEnabled(on)
      #self.zoomers[0].zoom(0.5)
      self.zoomers[0].setZoomBase(True)
        
      self.zoomers[1].setEnabled(on)
      #self.zoomers[1].zoom(0.5)
      self.zoomers[1].setZoomBase(True)
      #self.qwtPlot.setAxisAutoScale(True)

      if on:
          a=1
 
          
      else:
          a=1
          self.qwtPlot.setAxisAutoScale(self.qwtPlot.xBottom)
          self.qwtPlot.setAxisAutoScale(self.qwtPlot.yLeft)
         
          

      #self.showInfo()

    # zoom()
  def moved(self, point):
     info = "Отсчёт=%g, С(О2)=%g" % (
          round(self.qwtPlot.invTransform(Qwt.QwtPlot.xBottom, point.x())),
          self.qwtPlot.invTransform(Qwt.QwtPlot.yLeft, point.y()))
     self.showInfo(info)

    # moved()

  def selected(self, _):
     self.showInfo()

    # selected()
  def ResetDraw(self):
      self.vfpChart_II.Reset_Flag=1;

      #self.vfP.Reset_Flag=1
      a=self.Count_draw-1
      while a>=0:
          self.y_draw=numpy.delete(self.y_draw,a)
          #if self.vfP.Type==5: self.y_p_draw=numpy.delete(self.y_p_draw,a)
          self.y_p_draw=numpy.delete(self.y_p_draw,a)
          self.x_draw=numpy.delete(self.x_draw,a)
          a=a-1
      self.Count_draw=0
      self.vfpChart_II.Val_min_1=self.vfpChart_II.tmpVal4
      self.vfpChart_II.Val_max_1=self.vfpChart_II.tmpVal4
      self.vfpChart_II.Val_min_2=self.vfpChart_II.tmpVal5
      self.vfpChart_II.Val_max_2=self.vfpChart_II.tmpVal5

  def PauseDraw(self):
      if self.chbPause.isChecked()==1:
          self.timer.stop()
      else:
          self.timer.start()

  def AddMarker(self):
      self.Mrk = Qwt.QwtPlotMarker()
      txt=self.leComment_marker.text()
      val=float(self.leVal_marker.text())
      if self.rbTime.isChecked()==1:
          typ=1
          self.Mrk.setLineStyle(Qwt.QwtPlotMarker.VLine)
          self.Mrk.setXValue(val)
          d= '. отсчёт '
      else:
          typ=2
          self.Mrk.setLineStyle(Qwt.QwtPlotMarker.HLine)
          self.Mrk.setYValue(val)
          d='. '+self.AsixName
      self.Mrk.setLabel(Qwt.QwtText(txt))
      self.Mrk.setLabelAlignment(Qt.Qt.AlignRight | Qt.Qt.AlignTop)

      
      self.Mrk.attach(self.qwtPlot)
      #self.Mrk.detach()
      Res='Маркер '+str(self.Count_Marker)+d+str(val)+'. '+txt
      self.lwListMarker.addItem(Res)
      self.Marker=numpy.append(self.Marker,self.Mrk)
      self.Count_Marker=self.Count_Marker+1

  def DelMarker(self):
      a=self.lwListMarker.currentRow()
      self.lwa=self.lwListMarker.takeItem(a)
      self.lwListMarker.removeItemWidget(self.lwa)
      self.Mrk=self.Marker.item(a)
      b=0
      self.Mrk.detach()
      self.Marker=numpy.delete(self.Marker,a)

  def closeEvent(self, event):
    rect = self.geometry()
    self.vfpChart_II.dSize['x'] = rect.left()
    self.vfpChart_II.dSize['y'] = rect.top()
    self.vfpChart_II.dSize['height'] = rect.height() 
    self.vfpChart_II.dSize['width'] = rect.width()
    event.accept()
      
  def show(self, newsize = None):
     """ newsize - экземпляр QSize для передачи новых размеров окна """
     super().show()   # важно выполнить ПЕРЕД resize - иначе resize может не пройти
     ##if newsize:  self.resize(newsize) 

#-------------------------------------------------           
# ---------------------------------------------- 