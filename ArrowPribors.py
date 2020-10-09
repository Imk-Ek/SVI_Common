#print('Hello World')
#!/usr/bin/python3
# -*- coding: utf-8 -*-
 
import sys
import math
from PyQt4 import QtCore, QtGui
from PyQt4.QtCore import QObject, Qt, pyqtSignal, QPoint, QRect
from PyQt4.QtGui import QWidget, QSlider, QApplication, QHBoxLayout, QVBoxLayout, QFont, QColor, QPen, QPainter, QPolygon
#from PyQt5.QtWidgets import (QWidget, QSlider, QApplication, QHBoxLayout, QVBoxLayout)
#from PyQt5.QtCore import QObject, Qt, pyqtSignal
#from PyQt5.QtGui import QPainter, QFont, QColor, QPen

 
class Communicate(QObject):
    updateBW = pyqtSignal(int)
 
class BurningWidget(QWidget):
  
    def __init__(self):      
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setMinimumSize(1, 30)
        self.value = 75
        self.num = [75, 150, 225, 300, 375, 450, 525, 600, 675]
 
    def setValue(self, value):
        self.value = value
 
    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawWidget(qp)
        qp.end()
      
    def drawWidget(self, qp):
        font = QFont('Serif', 7, QFont.Light)
        qp.setFont(font)
 
        size = self.size()
        w = size.width()
        h = size.height()
 
        step = int(round(w / 15.0))
 
        till = int(((w / 750.0) * self.value))
        full = int(((w / 750.0) * 700))
 
        if self.value >= 700:
            qp.setPen(QColor(255, 255, 255))
            qp.setBrush(QColor(255, 255, 184))
            qp.drawRect(0, 0, full, h)
            qp.setPen(QColor(255, 175, 175))
            qp.setBrush(QColor(255, 175, 175))
            qp.drawRect(full, 0, till-full, h)
            
            
        else:
            
            qp.setPen(QColor(255, 255, 255))
            qp.setBrush(QColor(255, 255, 184))
            qp.drawRect(0, 0, till, h)
 
        pen = QPen(QColor(20, 20, 20), 1, 
            Qt.SolidLine)
            
        qp.setPen(pen)
        qp.setBrush(Qt.NoBrush)
        qp.drawRect(0, 0, w-1, h-1)
 
        j = 0
 
        for i in range(step, 10*step, step):
          
            qp.drawLine(i, 0, i, 5)
            metrics = qp.fontMetrics()
            fw = metrics.width(str(self.num[j]))
            qp.drawText(i-fw/2, h/2, str(self.num[j]))
            j = j + 1

class ZoneWidget(QWidget):
  
    def __init__(self):      
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setMinimumSize(100, 200)
        self.setFixedWidth(100)
        self.value = 75
        self.num = [0, 1, 2, 3, 4, 5, 6, 7, 8]
 
    def setValue(self, value):
        self.value = value
 
    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawWidget(qp)
        qp.end()
      
    def drawWidget(self, qp):
        font = QFont('Serif', 7, QFont.Light)
        qp.setFont(font)
        size = self.size()
        w = size.width()
        h = size.height()
 
        #step = int(round(w / 10.0))
        step = int(round(h / 10.0))
 
        till = int(((w / 750.0) * self.value))
        till = int(((h / 750.0) * self.value))
        #full = int(((w / 750.0) * 700))
        full = int(((h / 750.0) * 700))
 
        if self.value >=700:
            qp.setPen(QColor(255, 255, 255))
            qp.setBrush(QColor(255, 255, 184))
            #qp.drawRect(0, 0, full, h)
            qp.drawRect(0, 0, w, till)
            qp.setPen(QColor(255, 175, 175))
            qp.setBrush(QColor(255, 175, 175))
            #qp.drawRect(full, 0, till-full, h)
            qp.drawRect(0, full, w, till-full)
            
        else:
            
            qp.setPen(QColor(255, 255, 255))
            qp.setBrush(QColor(255, 255, 184))
            #qp.drawRect(0, 0, till, h)
            qp.drawRect(0, 0, w, till)
 
        pen = QPen(QColor(20, 20, 20), 1, 
            Qt.SolidLine)
            
        qp.setPen(pen)
        qp.setBrush(Qt.NoBrush)
        qp.drawRect(0, 0, w-1, h-1)
        ##qp.drawRect(0, 0, h-1, w-1)
 
        j = 0
 
        for i in range(step, 10*step, step):
          
            #qp.drawLine(i, 0, i, 5)
            qp.drawLine(0, i, 5, i)
            metrics = qp.fontMetrics()
            fw = metrics.width(str(self.num[j]))
            #fw = metrics.height(str(self.num[j]))
            #qp.drawText(i-fw/2, h/2, str(self.num[j]))
            qp.drawText(0.05*w, i-fw/2, str(self.num[j]))
            j = j + 1   
 
class ZoneWidget_2(QWidget):
  
    def __init__(self):      
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setMinimumSize(400, 500)
        self.setFixedWidth(400)
        self.value = 0.0
        self.min_value=0.0
        self.max_value=14.0
        self.zone_2=3.0
        self.zone_3=6.0
        self.num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
 
    def setValue(self, value):
        self.value = value/100.0
 
    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawWidget(qp)
        qp.end()
      
    def drawWidget(self, qp):
        font = QFont('Serif', 7, QFont.Light)
        qp.setFont(font)
        size = self.size()
        w = size.width()
        h = size.height()
 
        #step = int(round(w / 10.0))
        step = int(round(h / self.max_value))
 
        #till = int(((w / 750.0) * self.value))
        #till = int(((h / 750.0) * self.value))
        #full = int(((w / 750.0) * 700))
        #full = int(((h / 750.0) * 700))
        self.max_value=14
        self.fill_zone_1=int(((h / self.max_value) * self.zone_2))
        self.fill_zone_2=int(((h / self.max_value) * self.zone_3))
        #self.draw_value=int(((h / self.max_value*100) * self.value*100.0))
        self.draw_value=int(((h / (self.max_value*100.0)) *self.value*100.0))
        
        #qp.setPen(QColor(255, 255, 255),2)
        qp.setPen(QPen(QColor(255, 255, 255), 3))
        qp.setBrush(QColor(255, 50, 50))
        qp.drawRect(0, 0, w, self.fill_zone_1)

        qp.setPen(QColor(255, 255, 255))
        qp.setBrush(QColor(0, 255, 0))
        qp.drawRect(0, self.fill_zone_1, w, self.fill_zone_2)

        qp.setPen(QColor(255, 255, 255))
        qp.setBrush(QColor(255, 50, 50))
        qp.drawRect(0, self.fill_zone_2, w, h)
 
        '''if self.value >=700:
            qp.setPen(QColor(255, 255, 255))
            qp.setBrush(QColor(255, 255, 184))
            #qp.drawRect(0, 0, full, h)
            qp.drawRect(0, 0, w, till)
            qp.setPen(QColor(255, 175, 175))
            qp.setBrush(QColor(255, 175, 175))
            #qp.drawRect(full, 0, till-full, h)
            qp.drawRect(0, full, w, till-full)
            
        else:
            
            qp.setPen(QColor(255, 255, 255))
            qp.setBrush(QColor(255, 255, 184))
            #qp.drawRect(0, 0, till, h)
            qp.drawRect(0, 0, w, till)'''
 
        pen = QPen(QColor(20, 20, 20), 1, 
            Qt.SolidLine)
            
        qp.setPen(pen)
        qp.setBrush(Qt.NoBrush)
        qp.drawRect(0, 0, w-1, h-1)
        ##qp.drawRect(0, 0, h-1, w-1)
        begin_line=int(0.2*w)
        #Стрелка
        qp.setPen(QPen(QColor(0, 0, 0), 3))
        qp.drawLine(begin_line, self.draw_value, w, self.draw_value)
        qp.drawPolygon (QPoint(w-15, self.draw_value),
        QPoint(w, self.draw_value+5),
        QPoint(w, self.draw_value-5))
 
        j = 0
 
        for i in range(0, 14*step, step):
          
            qp.drawLine(0, i, 8, i)
            metrics = qp.fontMetrics()
            #fw = metrics.width(str(self.num[j]))
            #fw = metrics.height(str(self.num[j]))
            #qp.drawText(i-fw/2, h/2, str(self.num[j]))
            #font.setPointSize(font.pointSize()+0.9);
            font.setPixelSize(17);
            font.setBold(True)
            qp.setFont(font);
            qp.drawText(0.1*w, i, str(self.num[j]))
            j = j + 1   
            
        for i1 in range(int(step/2), 16*step, step):
          
            #qp.drawLine(i, 0, i, 5)
            qp.drawLine(0, i1, 3, i1) 
            
        qp.drawLine(w-8, self.fill_zone_1, w, self.fill_zone_1)
        qp.drawLine(w-8, self.fill_zone_2, w, self.fill_zone_2)
        qp.drawText(w-0.1*w, self.fill_zone_1, str(self.zone_2))
        qp.drawText(w-0.1*w, self.fill_zone_2, str(self.zone_3))     
        
class ZoneWidget_3(QWidget):
  
    def __init__(self):      
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setMinimumSize(400, 500)
        self.setFixedWidth(400)
        self.value = 0.0
        self.min_value=0.0
        self.center_value=4.0
        self.max_value=14.0
        self.zone_2=3.0
        self.zone_3=5.0
        self.num = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
 
    def setValue(self, value):
        self.value = value/100.0
 
    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawWidget(qp)
        qp.end()
      
    def drawWidget(self, qp):
        font = QFont('Serif', 7, QFont.Light)
        qp.setFont(font)
        size = self.size()
        w = size.width()
        h = size.height()
 
        #step = int(round(w / 10.0))
        step = int(round(h / self.max_value))
 
        #till = int(((w / 750.0) * self.value))
        #till = int(((h / 750.0) * self.value))
        #full = int(((w / 750.0) * 700))
        #full = int(((h / 750.0) * 700))
        self.max_value=14
        self.fill_zone_1=int(((h / self.max_value) * self.zone_2))
        self.fill_zone_2=int(((h / self.max_value) * self.zone_3))
        #self.draw_value=int(((h / self.max_value*100) * self.value*100.0))
        self.draw_value=int(((h / (self.max_value*100.0)) *self.value*100.0))
        
        #qp.setPen(QColor(255, 255, 255),2)
        qp.setPen(QPen(QColor(255, 255, 255), 3))
        qp.setBrush(QColor(255, 50, 50))
        qp.drawRect(0, 0, w*0.66, 0.25*h)

        qp.setPen(QColor(255, 255, 255))
        qp.setBrush(QColor(0, 255, 0))
        qp.drawRect(0, 0.25*h, w*0.66, 0.75*h)

        qp.setPen(QColor(255, 255, 255))
        qp.setBrush(QColor(255, 50, 50))
        qp.drawRect(0, 0.75*h, w*0.66, h)

 
        pen = QPen(QColor(20, 20, 20), 1, 
            Qt.SolidLine)
            
        qp.setPen(pen)
        qp.setBrush(Qt.NoBrush)
        qp.drawRect(0, 0, w-1, h-1)
        ##qp.drawRect(0, 0, h-1, w-1)
        begin_line=int(0.05*w)
        #Стрелка
        qp.setPen(QPen(QColor(0, 0, 0), 3))
        qp.drawLine(begin_line, self.draw_value, w, self.draw_value)
        #qfr=Qt.FillRule
        #qfr=Qt.OddEvenFill
        #Arrowp=QPolygon
        #qp.setPen(QPen(QColor(255, 255, 255), 3))
        #qp.setBrush(QColor(255, 255, 255))
        qp.drawPolygon(QPoint(0.66*w, self.draw_value), 
        QPoint(0.66*w+45, self.draw_value+5),
        QPoint(0.66*w+45, self.draw_value-5))
        #qp.drawPolygon(Arrowp,qfr)

        j=0
        for i in range(1, 20, 1):
          
            qp.drawLine(0.66*w, i*h/20, 0.66*w-8, i*h/20)
            metrics = qp.fontMetrics()
            #fw = metrics.width(str(self.num[j]))
            #fw = metrics.height(str(self.num[j]))
            #qp.drawText(i-fw/2, h/2, str(self.num[j]))
            #font.setPointSize(font.pointSize()+0.9);
            font.setPixelSize(30);
            font.setBold(True)
            qp.setFont(font);
            #qp.drawText(0.1*w, i, str(self.num[j]))
            j = j + 1   
            
        for i1 in range(int(step/2), 16*step, step):
          
            #qp.drawLine(i, 0, i, 5)
            #qp.drawLine(0, i1, 3, i1) 
            k=0
            
        qp.drawLine(0.66*w, 0.25*h, 0.66*w-0.1*w, 0.25*h)
        qp.drawLine(0.66*w, 0.5*h, 0.66*w-0.1*w, 0.5*h)
        qp.drawLine(0.66*w, 0.75*h, 0.66*w-0.1*w, 0.75*h)
        qp.drawText(0.66*w-0.3*w, 0.27*h, str(self.zone_2))
        qp.drawText(0.66*w-0.3*w, 0.52*h, str(self.center_value))
        qp.drawText(0.66*w-0.3*w, 0.77*h, str(self.zone_3)) 
        
        qp.drawLine(0.66*w, 0, 0.66*w, h)   

class ZoneWidget_4(QWidget):
 
    def __init__(self, *args, **kwargs):
        super(ZoneWidget_4, self).__init__(*args, **kwargs)
        self.value = 0.0
        self.delta_value=2.0
        self.center_value=14.001
        self.ed_="кДж"
        self.initUI()
    #def __init__(self):      
        #super().__init__()
        #self.initUI()
        
    def initUI(self):
        self.h=500
        #self.h=self.height();
        #self.setMinimumSize(self.h/2, self.h/2)
        self.setFixedHeight(self.h)
        self.setFixedWidth(self.h/2)
        #self.value = 0.0
        #self.delta_value=2.0
        #self.center_value=14.001
        #self.ed_="кДж"

        
 
    def setValue(self, value):
        if(value>self.center_value+1.9*self.delta_value ): self.value=self.center_value+1.9*self.delta_value 
        else:
              if (value<self.center_value-1.9*self.delta_value ): self.value=self.center_value-1.9*self.delta_value
              else: self.value= value #/100.0
 
    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawWidget(qp)
        qp.end()
      
    def drawWidget(self, qp):
        font = QFont('Serif', 7, QFont.Light)
        qp.setFont(font)
        size = self.size()
        w = size.width()
        h = size.height()

        begin_line=int(0.05*w)
        split_line=0.5

        self.draw_value=int(h-((h / (4*100*self.delta_value))* (self.value*100-100*(self.center_value-2*self.delta_value))))
        #self.draw_value=int(((h / (4*100*self.delta_value))* (self.value*100-100*(self.center_value-2*self.delta_value))))
        #self.draw_value=int(((h / (self.center_value*100.0)) *self.value*100.0))
        #self.val=(self.value-100*(self.center_value-2*self.delta_value))*90.0/(4*100*self.delta_value)#1400.0
        
        qp.setPen(QPen(QColor(255, 255, 255), 3))
        qp.setBrush(QColor(255, 50, 50))
        qp.drawRect(0, 0, w*split_line, 0.25*h)

        qp.setPen(QColor(255, 255, 255))
        qp.setBrush(QColor(0, 255, 0))
        qp.drawRect(0, 0.25*h, w*split_line, 0.75*h)

        qp.setPen(QColor(255, 255, 255))
        qp.setBrush(QColor(255, 50, 50))
        qp.drawRect(0, 0.75*h, w*split_line, h)

 
        pen = QPen(QColor(20, 20, 20), 1, 
            Qt.SolidLine)
            
        qp.setPen(pen)
        qp.setBrush(Qt.NoBrush)
        qp.drawRect(0, 0, w-1, h-1)


        #Стрелка
        qp.setPen(QPen(QColor(0, 0, 0), 3))
        qp.drawLine(begin_line, self.draw_value, w, self.draw_value)

        qp.drawPolygon(QPoint(split_line*w-0.1*w, self.draw_value), 
        QPoint(split_line*w-0.1*w-60, self.draw_value+5),
        QPoint(split_line*w-0.1*w-60, self.draw_value-5))


        for i in range(1, 20, 1):          
            qp.drawLine(split_line*w, i*h/20, split_line*w-8, i*h/20)

        metrics = qp.fontMetrics()
        font.setPixelSize(30);
        font.setBold(True)
        qp.setFont(font);    
        qp.drawLine(split_line*w, 0.25*h, split_line*w-0.1*w, 0.25*h)
        qp.drawLine(split_line*w, 0.5*h, split_line*w-0.1*w, 0.5*h)
        qp.drawLine(split_line*w, 0.75*h, split_line*w-0.1*w, 0.75*h)
        min_=round((self.center_value-self.delta_value),3)
        max_=round((self.center_value+self.delta_value),3)
        qp.drawText((split_line+0.1)*w, 0.08*h, str(self.ed_))

        #qp.drawText((split_line+0.1)*w, 0.16*h, str(self.value))

        qp.drawText((split_line+0.02)*w, 0.27*h, str(max_))
        qp.drawText((split_line+0.02)*w, 0.52*h, str(self.center_value))
        qp.drawText((split_line+0.02)*w, 0.77*h, str(min_)) 
        
        qp.drawLine(split_line*w, 0, split_line*w, h)   
                
class ZoneArrowWidget(QWidget):
  
    #def __init__(self):      
        #super().__init__()
        #self.initUI()
    def __init__(self, *args, **kwargs):
        super(ZoneArrowWidget, self).__init__(*args, **kwargs)
        self.value = 0.0
        self.delta_value=2.0
        self.center_value=14.001
        self.ed_="кДж"
        self.initUI()

        
    def initUI(self):
        self.setMinimumSize(400, 400)
        self.setFixedWidth(400)
        self.setFixedHeight(400)
        self.value = 0.0
        self.delta_value=2.0
        self.center_value=14.001
        self.ed_="кДж"
 
    def setValue(self, value):
        if(value>self.center_value+1.9*self.delta_value ): self.value=self.center_value+1.9*self.delta_value 
        else:
              if (value<self.center_value-1.9*self.delta_value ): self.value=self.center_value-1.9*self.delta_value
              else: self.value= value #/100.0
        #self.value= value
    def paintEvent(self, e):
        qp = QPainter()
        qp.begin(self)
        self.drawWidget(qp)
        qp.end()
      
    def drawWidget(self, qp):
        font = QFont('Serif', 7, QFont.Light)
        qp.setFont(font)
        size = self.size()
        w = size.width()
        h = size.height()

        qp.setPen(QPen(QColor(0, 0, 0), 3))
 
        #Квадраты
        rect=QRect(0+10, 0+10, 2*w-20, 2*w-20)
        rect2=QRect(0+10, 0+10, 2*w-30, 2*w-30)
        rect1=QRect(0+10, 0+10, w-20, w-20)
        startAngle = 92*16;
        arcLength = 86*16;
        
         
        qp.drawRect(rect1)
        qp.setPen(QPen(QColor(255, 255, 255), 3))
        qp.setBrush(QColor(255, 50, 50))
        angle_01_=(-90-0)*math.pi/180.0
        angle_41_=(90-90)*math.pi/180.0
        qp.drawPie(rect2, -2880, -380 )

        qp.setPen(QColor(255, 255, 255))
        qp.setBrush(QColor(0, 255, 0))
        qp.drawPie(rect2, -3260, -690)

        qp.setPen(QColor(255, 255, 255))
        qp.setBrush(QColor(255, 50, 50))
        qp.drawPie(rect2, -3950, -690)       
        
        qp.setPen(QPen(QColor(0, 0, 0), 3))
        #qp.drawRect(rect1)
        qp.drawArc(rect, startAngle, arcLength); 
        pen = QPen(QColor(20, 20, 20), 1, 
            Qt.SolidLine)
            
        qp.setPen(pen)
        qp.setBrush(Qt.NoBrush)
        qp.drawRect(0, 0, w-1, h-1)
        ##qp.drawRect(0, 0, h-1, w-1)
        begin_line=int(0.2*w)
        #Стрелка
        self.val=(self.value*100.0-100*(self.center_value-2*self.delta_value))*90.0/(4*100*self.delta_value)#1400.0
        angle_=(90-self.val)*math.pi/180.0
        strel=w-20
        self.x2=int(w-10-strel*math.sin(angle_))
        self.y2=int(w-10-strel*math.cos(angle_))
        qp.setPen(QPen(QColor(0, 0, 0), 3))
        qp.drawLine(w-10, w-10, self.x2, self.y2 )
        strel=0.75*w
        self.x1s=int(w-10-strel*math.sin(angle_))
        self.y1s=int(w-10-strel*math.cos(angle_))
        strel=0.60*w
        self.x2s=int(w-10-strel*math.sin(angle_-0.007*math.pi))
        self.y2s=int(w-10-strel*math.cos(angle_-0.007*math.pi))
        self.x3s=int(w-10-strel*math.sin(angle_+0.007*math.pi))
        self.y3s=int(w-10-strel*math.cos(angle_+0.007*math.pi))        
        qp.drawPolygon (QPoint(self.x1s, self.y1s),
        QPoint(self.x2s, self.y2s),
        QPoint(self.x3s, self.y3s))
 
        for i in range(1, 20, 1):          
                    angle_1=4.5*i  
                    angle_11=(90-angle_1)*math.pi/180.0
                    strel_11=0.90*w 
                    strel_12=0.94*w 
                    self.x_11=int(w-10-strel_11*math.sin(angle_11))
                    self.y_11=int(w-10-strel_11*math.cos(angle_11)) 
                    self.x_12=int(w-10-strel_12*math.sin(angle_11))
                    self.y_12=int(w-10-strel_12*math.cos(angle_11)) 
                    qp.drawLine(self.x_11, self.y_11, self.x_12, self.y_12)
        min_=round((self.center_value-self.delta_value),3)
        max_=round((self.center_value+self.delta_value),3)
        metrics = qp.fontMetrics()
        font.setPixelSize(30);
        font.setBold(True)
        qp.setFont(font);
        angle_1=22.5  
        angle_11=(90-angle_1)*math.pi/180.0
        angle_11_=angle_11
        strel_11=0.90*w 
        strel_12=0.98*w 
        strel_13=0.85*w
        self.x_11=int(w-10-strel_11*math.sin(angle_11))
        self.y_11=int(w-10-strel_11*math.cos(angle_11)) 
        self.x_12=int(w-10-strel_12*math.sin(angle_11))
        self.y_12=int(w-10-strel_12*math.cos(angle_11)) 
        self.x_13=int(w-10-strel_13*math.sin(angle_11))
        self.y_13=int(w-10-strel_13*math.cos(angle_11))
        qp.drawLine(self.x_11, self.y_11, self.x_12, self.y_12)
        qp.drawText(self.x_13, self.y_13, str(min_))

        angle_1=45  
        angle_11=(90-angle_1)*math.pi/180.0
        angle_21_=angle_11
        strel_11=0.90*w 
        strel_12=0.98*w 
        strel_13=0.85*w
        self.x_11=int(w-10-strel_11*math.sin(angle_11))
        self.y_11=int(w-10-strel_11*math.cos(angle_11)) 
        self.x_12=int(w-10-strel_12*math.sin(angle_11))
        self.y_12=int(w-10-strel_12*math.cos(angle_11)) 
        self.x_13=int(w-10-strel_13*math.sin(angle_11))
        self.y_13=int(w-10-strel_13*math.cos(angle_11))
        qp.drawLine(self.x_11, self.y_11, self.x_12, self.y_12)
        qp.drawText(self.x_13, self.y_13, str(self.center_value))

        angle_1=67.5  
        angle_11=(90-angle_1)*math.pi/180.0
        angle_31_=angle_11
        strel_11=0.90*w 
        strel_12=0.98*w 
        strel_13=0.85*w
        self.x_11=int(w-10-strel_11*math.sin(angle_11))
        self.y_11=int(w-10-strel_11*math.cos(angle_11)) 
        self.x_12=int(w-10-strel_12*math.sin(angle_11))
        self.y_12=int(w-10-strel_12*math.cos(angle_11)) 
        self.x_13=int(w-10-strel_13*math.sin(angle_11))
        self.y_13=int(w-10-strel_13*math.cos(angle_11))
        qp.drawLine(self.x_11, self.y_11, self.x_12, self.y_12)
        qp.drawText(self.x_13, self.y_13, str(max_))
        qp.drawText(0.1*w, 0.2*w, str(self.ed_))

        #qp.drawText(0.1*w, 0.1*w, str(self.value))


         
class Example(QWidget):
    

    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):      
        sld = QSlider(Qt.Horizontal, self)
        sld.setFocusPolicy(Qt.NoFocus)
        sld.setRange(0, 1400)
        sld.setValue(750)
        sld.setGeometry(30, 40, 150, 30)
 
        self.c = Communicate()        
        self.wid = BurningWidget()
        self.zw = ZoneWidget_3()
        self.zw4 = ZoneWidget_4()
        self.zaw = ZoneArrowWidget()


        
        self.c.updateBW[int].connect(self.wid.setValue)
        self.c.updateBW[int].connect(self.zw.setValue)
        self.c.updateBW[int].connect(self.zw4.setValue)
        self.c.updateBW[int].connect(self.zaw.setValue)
 
        sld.valueChanged[int].connect(self.changeValue)
        hbox = QHBoxLayout()
        hbox.addWidget(self.wid)
        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.zw, 0, Qt.AlignLeft)

        #hbox3 = QHBoxLayout()
        hbox2.addWidget(self.zw4, 0, Qt.AlignRight)
        hbox2.addWidget(self.zaw, 0, Qt.AlignRight)
        
        #self.setLayout(hbox)
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addLayout(hbox)
        vbox.addLayout(hbox2)
        #vbox.addLayout(hbox3)
        self.setLayout(vbox)
        
        #self.setGeometry(300, 300, 390, 210)
        self.setGeometry(0, 0, 590, 700)
        self.setWindowTitle('Burning widget')
        self.show()
        
    def changeValue(self, value):
        self.c.updateBW.emit(value)        
        self.wid.repaint()
        self.zw.repaint()
        self.zw4.repaint()
        self.zaw.repaint()
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
