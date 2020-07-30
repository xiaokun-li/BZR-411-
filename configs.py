# -*- coding: utf-8 -*-
# FileName: configs.py
import os

FilePrefix=[
    'irlsprct.baxwqq',
    'irlspinv.baxwqq',
    'HPE_irlsprct.baxwqq',
    'HPE_irlspinv.baxwqq',
    'ICQFACT.SCHE.SXI.BZR',
    'ICQFACT.SCHE.SXI.BZI',
    ]
# HPE_irlsprct.baxwqq.2016011113940004.xml  20 
# HPE_irlspinv.baxwqq.2016012622940457.xml
# irlspinv.baxwqq.2016012319904552.xml
# irlsprct.baxwqq.2016010612000091.xml
# ICQFACT.SCHE.SXI.BZI01062015142794.xml
# ICQFACT.SCHE.SXI.BZR11122015170590.xml

FilePostfix='.xml'
#FileNameSample='irlsprct.baxwqq.2016010711900199'
FileGeneratedDateTime=''

TargetDirectory=[
    r'C:\Users\xman\Desktop\esmi\sha',
    r'\\10.213.27.245\CPMO_CQ_Data\ESMI',
    r'\\10.213.27.245\CPMO_Data\esmi',
    r'\\10.213.27.245\cpmohpe_data\ESMI',
    r'\\10.213.25.155\ftp\HPCPMO\bak'
    ]

FileType = [
    'BCI','BCR','BZI','BZR'
    ]

#temp list for file list
l2=[]

#temp list for file content
l3=[]

# get a file list
def collectFiles(_targetstring,p2):

    path=TargetDirectory[2]

    if p2=='HPI' or p2=='hpi':
        path=TargetDirectory[2]
    elif p2=='HPE' or p2=='hpe':
        path=TargetDirectory[3]

    l = os.listdir(path)
    vvs =(sortTargetString(_targetstring))[0:11] #[0:12]
    for f in l:
        if f.find(vvs)>=0:
            l2.append(f) 
    print(l2)

# find the targetstring in fils
def findControlid(_targetstring,p2):

    path=TargetDirectory[2]

    if p2=='HPI' or p2=='hpi':
        path=TargetDirectory[2]
    elif p2=='HPE' or p2=='hpe':
        path=TargetDirectory[3]
    
    for f in l2:
        f1 = open(path+'\\'+f)
        f1.readline()
        f1.readline()
        f1.readline()
        f1.readline()
        tt = f1.readline()
        if tt.find(_targetstring)>=0:
            print (tt)
            print (f)
            l3.append(tt)
            #print('copy '+path+'\\'+f+r' c:\tttt'+'\\')
            os.system('copy '+path+'\\'+f+r' c:\tttt'+'\\')
    print (l3)
    print("Finished...")
    l2[:]=[]
    l3[:]=[]

# !!!
def sortTargetString(ss):
    newstr = (ss[4:8]+ss[2:4]+ss[0:2]+ss[8:14])
    return newstr


# Entry
def run(_controlid,p2):
    collectFiles(_controlid,p2)
    findControlid(_controlid,p2)


def getDateString(_targetstring):
    datestring=""
    if _targetstring.find('HPE') > -1:
    #if _type=='HPE' or _type=='hpe':
        datestring=_targetstring[20:34]
    elif _targetstring.find('irl') > -1:
    #elif _type=='HPI' or _type=='hpi':
        datestring=_targetstring[16:30]
    elif _targetstring.find('ICQ') > -1:    
    #elif _type=='hpcq' or _type=='hpcq':
        datestring=sortTargetString(_targetstring[20:34])
    return datestring
        

    



