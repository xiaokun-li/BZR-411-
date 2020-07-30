import os
import time
import traceback
from configs import getDateString
from configs import TargetDirectory


curr = time.time()

"""
print getDateString('HPE_irlsprct.baxwqq.2016011113340004.xml')
print getDateString('irlspinv.baxwqq.2016012319504552.xml')
print getDateString('ICQFACT.SCHE.SXI.BZI01062015142734.xml')
"""

"""
print ""
print curr
print time.mktime(time.strptime(getDateString('HPE_irlsprct.baxwqq.2016030113000000.xml','hpe'),'%Y%m%d%H%M%S'))
print ""
print (curr - time.mktime(time.strptime(getDateString('HPE_irlsprct.baxwqq.2016030113000000.xml','hpe'),'%Y%m%d%H%M%S')))/60
"""

path = TargetDirectory[4]
#path = r"C:\Users\terry\Desktop\test"
l = os.listdir(path)
ll=[]
lle=[]

print len(ll)
print len(lle)

for f in l:
    try:
        tfromfile = time.mktime(time.strptime(getDateString(f),'%Y%m%d%H%M%S'))
        if (curr - tfromfile ) / 60.00 <= 30.00:
            ll.append(f)

    except Exception,e:
        lle.append(f)
            
print ll
print ""
print "Error Collection:"
print lle
print ""
print len(ll)
print len(lle)

if len(ll)>0:
    print("OK")
else:
    os.system("D:\\New\\a.bat")
    
input("Press any key...")


"""
print ("abcdefg123456".find('8'))
    
#ctime = time.ctime(os.path.getctime(f))
"""

