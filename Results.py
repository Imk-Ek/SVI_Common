import os, sys

def InitRes():
    global Result_D
    global Result_Dict
    Result_Dict={}
    Result_D=[1,2,3,4,5,6]
    Result_D[1]=1.0

def InitPriborRes1(PrName):
    global Result_Dict
    Dct1={}
    Dct1[('Value')]=0.0
    Dct1[('EdIzm')]=1
    Dct={}
    Dct[(PrName)]=Dct1
    Result_Dict.update(Dct)

def InitPriborRes(PrName):
    global Result_Dict
    Dct1={}
    Dct1['Value']=0.0
    Dct1['EdIzm']=1
    Dct={}
    Dct[PrName]=Dct1
    Result_Dict.update(Dct)
