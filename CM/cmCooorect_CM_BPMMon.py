#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 00:03:34 2017

@author: p
"""


import numpy as np
import os
import matplotlib.pyplot as plt

fNameBK='log_Nov_16_02:28:14_2017'
fNameLog='log'
fNameData='logData'

os.system('cp '+fNameBK+' '+fNameLog)

fidLog=open(fNameLog,'r')
fidData=open(fNameData,'w+')

lenI=0
iRec=0
for i in fidLog:
    iRec+=1
    if i[0]=='B':
        continue
    lenI+=len(i)
    if len(i)<lenI/iRec*0.8:
        continue
    fidData.writelines(i)
fidLog.close()
fidData.close()
    
data=np.loadtxt(fNameData)
print np.shape(data)

#######-------------------------------
plt.figure(101)
xBPM1=data[:,0]
plt.hist(xBPM1,200)
plt.title('xBPM1')

plt.figure(201)
yBPM1=data[:,1]
plt.hist(yBPM1,200)
plt.title('yBPM1')


#######-------------------------------
plt.figure(102)
xBPM2=data[:,2]
plt.hist(xBPM2,200)
plt.title('xBPM2')

plt.figure(202)
yBPM2=data[:,3]
plt.hist(yBPM2,200)
plt.title('yBPM2')

#######-------------------------------
plt.figure(103)
xBPM3=data[:,4]
plt.hist(xBPM3,200)
plt.title('xBPM3')

plt.figure(203)
yBPM3=data[:,5]
plt.hist(yBPM3,200)
plt.title('yBPM3')


#######-------------------------------
plt.figure(104)
xBPM4=data[:,6]
plt.hist(xBPM4,200)
plt.title('xBPM4')

plt.figure(204)
yBPM4=data[:,7]
plt.hist(yBPM4,200)
plt.title('yBPM4')


#######-------------------------------
plt.figure(105)
xBPM5=data[:,8]
plt.hist(xBPM5,200)
plt.title('xBPM5')

plt.figure(205)
yBPM5=data[:,9]
plt.hist(yBPM5,200)
plt.title('yBPM5')


#######-------------------------------
plt.figure(106)
xBPM6=data[:,10]
plt.hist(xBPM6,200)
plt.title('xBPM6')

plt.figure(206)
yBPM6=data[:,11]
plt.hist(yBPM6,200)
plt.title('yBPM6')


#######-------------------------------
plt.figure(107)
xBPM7=data[:,12]
plt.hist(xBPM7,200)
plt.title('xBPM7')

plt.figure(207)
yBPM7=data[:,13]
plt.hist(yBPM7,200)
plt.title('yBPM7')


#######-------------------------------
plt.figure(108)
xBPM8=data[:,14]
plt.hist(xBPM8,200)
plt.title('xBPM8')

plt.figure(208)
yBPM8=data[:,15]
plt.hist(yBPM8,200)
plt.title('yBPM8')


#######-------------------------------
plt.figure(109)
xBPM9=data[:,16]
plt.hist(xBPM9,200)
plt.title('xBPM9')

plt.figure(209)
yBPM9=data[:,17]
plt.hist(yBPM9,200)
plt.title('yBPM9')


#######-------------------------------
plt.figure(110)
xBPM10=data[:,18]
plt.hist(xBPM10,200)
plt.title('xBPM10')

plt.figure(210)
yBPM10=data[:,19]
plt.hist(yBPM10,200)
plt.title('yBPM10')


#######-------------------------------
plt.figure(111)
xBPM11=data[:,20]
plt.hist(xBPM11,200)
plt.title('xBPM11')

plt.figure(211)
yBPM11=data[:,21]
plt.hist(yBPM11,200)
plt.title('yBPM11')


#######-------------------------------
plt.figure(112)
xBPM12=data[:,22]
plt.hist(xBPM12,200)
plt.title('xBPM12')

plt.figure(212)
yBPM12=data[:,23]
plt.hist(yBPM12,200)
plt.title('yBPM12')


#######-------------------------------
plt.figure(113)
xBPM13=data[:,24]
plt.hist(xBPM13,200)
plt.title('xBPM13')

plt.figure(213)
yBPM13=data[:,25]
plt.hist(yBPM13,200)
plt.title('yBPM13')


#######-------------------------------
plt.figure(114)
xBPM14=data[:,26]
plt.hist(xBPM14,200)
plt.title('xBPM14')

plt.figure(214)
yBPM14=data[:,27]
plt.hist(yBPM14,200)
plt.title('yBPM14')


#######-------------------------------
plt.figure(115)
xBPM15=data[:,28]
plt.hist(xBPM15,200)
plt.title('xBPM15')

plt.figure(215)
yBPM15=data[:,29]
plt.hist(yBPM15,200)
plt.title('yBPM15')


#######-------------------------------
plt.figure(116)
xBPM16=data[:,30]
plt.hist(xBPM16,200)
plt.title('xBPM16')

plt.figure(216)
yBPM16=data[:,31]
plt.hist(yBPM16,200)
plt.title('yBPM16')


#######-------------------------------
plt.figure(117)
xBPM17=data[:,32]
plt.hist(xBPM17,200)
plt.title('xBPM17')

plt.figure(217)
yBPM17=data[:,33]
plt.hist(yBPM17,200)
plt.title('yBPM17')



plt.close('all')
##############################################################

#######-------------------------------
plt.figure(301)
xMEBT01=data[:,34]
plt.hist(xMEBT01,200)
plt.title('xMEBT01')

plt.figure(401)
yMEBT01=data[:,35]
plt.hist(yMEBT01,200)
plt.title('yMEBT01')

#######-------------------------------
plt.figure(302)
xMEBT02=data[:,36]
plt.hist(xMEBT02,200)
plt.title('xMEBT02')

plt.figure(402)
yMEBT02=data[:,37]
plt.hist(yMEBT02,200)
plt.title('yMEBT02')

#######-------------------------------
plt.figure(303)
xMEBT03=data[:,38]
plt.hist(xMEBT03,200)
plt.title('xMEBT03')

plt.figure(403)
yMEBT03=data[:,39]
plt.hist(yMEBT03,200)
plt.title('yMEBT03')

#######-------------------------------
plt.figure(304)
xMEBT04=data[:,40]
plt.hist(xMEBT04,200)
plt.title('xMEBT04')

plt.figure(404)
yMEBT04=data[:,41]
plt.hist(yMEBT04,200)
plt.title('yMEBT04')

#######-------------------------------
plt.figure(305)
xMEBT05=data[:,42]
plt.hist(xMEBT05,200)
plt.title('xMEBT05')

plt.figure(405)
yMEBT05=data[:,43]
plt.hist(yMEBT05,200)
plt.title('yMEBT05')

#######-------------------------------
plt.figure(306)
xMEBT06=data[:,44]
plt.hist(xMEBT06,200)
plt.title('xMEBT06')

plt.figure(406)
yMEBT06=data[:,45]
plt.hist(yMEBT06,200)
plt.title('yMEBT06')

#######-------------------------------
plt.figure(307)
xMEBT07=data[:,46]
plt.hist(xMEBT07,200)
plt.title('xMEBT07')

plt.figure(407)
yMEBT07=data[:,47]
plt.hist(yMEBT07,200)
plt.title('yMEBT07')

##############################################################

#######-------------------------------
plt.figure(501)
xHCM101=data[:,48]
plt.hist(xHCM101,200)
plt.title('xHCM101')

plt.figure(601)
yHCM101=data[:,49]
plt.hist(yHCM101,200)
plt.title('yHCM101')

#######-------------------------------
plt.figure(502)
xHCM102=data[:,50]
plt.hist(xHCM102,200)
plt.title('xHCM102')

plt.figure(602)
yHCM102=data[:,51]
plt.hist(yHCM102,200)
plt.title('yHCM102')

#######-------------------------------
plt.figure(503)
xHCM103=data[:,52]
plt.hist(xHCM103,200)
plt.title('xHCM103')

plt.figure(603)
yHCM103=data[:,53]
plt.hist(yHCM103,200)
plt.title('yHCM103')

#######-------------------------------
plt.figure(504)
xHCM104=data[:,54]
plt.hist(xHCM104,200)
plt.title('xHCM104')

plt.figure(604)
yHCM104=data[:,55]
plt.hist(yHCM104,200)
plt.title('yHCM104')

#######-------------------------------
plt.figure(505)
xHCM105=data[:,56]
plt.hist(xHCM105,200)
plt.title('xHCM105')

plt.figure(605)
yHCM105=data[:,57]
plt.hist(yHCM105,200)
plt.title('yHCM105')

#######-------------------------------
plt.figure(506)
xHCM106=data[:,58]
plt.hist(xHCM106,200)
plt.title('xHCM106')

plt.figure(606)
yHCM106=data[:,59]
plt.hist(yHCM106,200)
plt.title('yHCM106')




##############################################################

#######-------------------------------
plt.figure(701)
xHCM201=data[:,60]
plt.hist(xHCM201,200)
plt.title('xHCM201')

plt.figure(801)
yHCM201=data[:,61]
plt.hist(yHCM201,200)
plt.title('yHCM201')

#######-------------------------------
plt.figure(702)
xHCM202=data[:,62]
plt.hist(xHCM202,200)
plt.title('xHCM202')

plt.figure(802)
yHCM202=data[:,63]
plt.hist(yHCM202,200)
plt.title('yHCM202')

#######-------------------------------
plt.figure(703)
xHCM203=data[:,64]
plt.hist(xHCM203,200)
plt.title('xHCM203')

plt.figure(803)
yHCM203=data[:,65]
plt.hist(yHCM203,200)
plt.title('yHCM203')

#######-------------------------------
plt.figure(704)
xHCM204=data[:,66]
plt.hist(xHCM204,200)
plt.title('xHCM204')

plt.figure(804)
yHCM204=data[:,67]
plt.hist(yHCM204,200)
plt.title('yHCM204')

#######-------------------------------
plt.figure(705)
xHCM205=data[:,68]
plt.hist(xHCM205,200)
plt.title('xHCM205')

plt.figure(805)
yHCM205=data[:,69]
plt.hist(yHCM205,200)
plt.title('yHCM205')

#######-------------------------------
plt.figure(706)
xHCM206=data[:,70]
plt.hist(xHCM206,200)
plt.title('xHCM206')

plt.figure(806)
yHCM206=data[:,71]
plt.hist(yHCM206,200)
plt.title('yHCM206')













