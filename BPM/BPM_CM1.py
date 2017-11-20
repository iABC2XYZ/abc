# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np

from epics import caget, caput

import time


'''
MEBT_PS:DCH_01:ISet
BPM:1-X11
BPM:1-Y11
'''










NTotal=1e5
iTotal=0
nFresh=30
Amp=2.5
AmpBound=10

Q1=caget('MEBT_PS:QUAD_01:IMon')+1.
Q2=caget('MEBT_PS:QUAD_02:IMon')+1.
Q3=caget('MEBT_PS:QUAD_03:IMon')+1.
Q4=caget('MEBT_PS:QUAD_04:IMon')+1.
Q5=caget('MEBT_PS:QUAD_05:IMon')+1.
Q6=caget('MEBT_PS:QUAD_06:IMon')+1.
Q7=caget('MEBT_PS:QUAD_07:IMon')+1.

'''
dCH1=caget('MEBT_PS:DCH_01:IMon')+1.
dCH2=caget('MEBT_PS:DCH_02:IMon')+1.
dCH3=caget('MEBT_PS:DCH_03:IMon')+1.
dCH4=caget('MEBT_PS:DCH_04:IMon')+1.
dCH5=caget('MEBT_PS:DCH_05:IMon')+1.
dCH6=caget('MEBT_PS:DCH_06:IMon')+1.
dCH7=caget('MEBT_PS:DCH_07:IMon')+1.

dCV1=caget('MEBT_PS:DCV_01:IMon')+1.
dCV2=caget('MEBT_PS:DCV_02:IMon')+1.
dCV3=caget('MEBT_PS:DCV_03:IMon')+1.
dCV4=caget('MEBT_PS:DCV_04:IMon')+1.
dCV5=caget('MEBT_PS:DCV_05:IMon')+1.
dCV6=caget('MEBT_PS:DCV_06:IMon')+1.
dCV7=caget('MEBT_PS:DCV_07:IMon')+1.
'''

dCH1,dCH2,dCH3,dCH4,dCH5,dCH6,dCH7=1.,1.,1.,1.,1.,1.,1.
dCV1,dCV2,dCV3,dCV4,dCV5,dCV6,dCV7=1.,1.,1.,1.,1.,1.,1.


now = int(time.time())
timeArray = time.localtime(now)
nowClock= time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
nameNowClock=nowClock[5:7]+nowClock[8:10]+'_'+nowClock[11:13]+nowClock[14:16]

nameRec='Rec_'+nameNowClock+'.dat'
with open(nameRec,'a+') as fid:
    while True:
        flagHVWrite=0
        acct1=caget('ADS_SLIT_VALUE.CHAN4_VAL_M')
        acct2=caget('ADS_SLIT_VALUE.CHAN5_VAL_M')
        acct3=caget('ADS_SLIT_VALUE.CHAN6_VAL_M')
        fc2=caget('ADS_SLIT_VALUE.CHAN2_VAL')

        if (acct1<1.05) or (acct2<1.05) or (acct2<0.5) or (fc2>0.5):
            print iTotal
            print 'WARNING ! ! !   Current  !!! '
            time.sleep(3)
            continue

	Q10,Q20,Q30,Q40,Q50,Q60,Q70=Q1,Q2,Q3,Q4,Q5,Q6,Q7


        Q1=caget('MEBT_PS:QUAD_01:IMon')+1.
	Q2=caget('MEBT_PS:QUAD_02:IMon')+1.
        Q3=caget('MEBT_PS:QUAD_03:IMon')+1.
	Q4=caget('MEBT_PS:QUAD_04:IMon')+1.
        Q5=caget('MEBT_PS:QUAD_05:IMon')+1.
	Q6=caget('MEBT_PS:QUAD_06:IMon')+1.
	Q7=caget('MEBT_PS:QUAD_07:IMon')+1.



	dQ1,dQ2,dQ3,dQ4,dQ5,dQ6,dQ7=np.abs((Q1-Q10)/Q10),np.abs((Q2-Q20)/Q20),np.abs((Q3-Q30)/Q30),np.abs((Q4-Q40)/Q40),np.abs((Q5-Q50)/Q50),np.abs((Q6-Q60)/Q60),np.abs((Q7-Q70)/Q70)

	if (dQ1>0.2) or (dQ2>0.2) or (dQ3>0.2) or (dQ4>0.2) or (dQ5>0.2) or (dQ6>0.2) or (dQ7>0.2) :
            print iTotal
            print 'WARNING ! ! !   Q  !!! '
            time.sleep(3)
            continue  

        dCH10,dCH20,dCH30,dCH40,dCH50,dCH60,dCH70=dCH1,dCH2,dCH3,dCH4,dCH5,dCH6,dCH7
        dCV10,dCV20,dCV30,dCV40,dCV50,dCV60,dCV70=dCV1,dCV2,dCV3,dCV4,dCV5,dCV6,dCV7

        dCH1=caget('MEBT_PS:DCH_01:IMon')+15.
        dCH2=caget('MEBT_PS:DCH_02:IMon')+15.
        dCH3=caget('MEBT_PS:DCH_03:IMon')+15.
        dCH4=caget('MEBT_PS:DCH_04:IMon')+15.
        dCH5=caget('MEBT_PS:DCH_05:IMon')+15.
        dCH6=caget('MEBT_PS:DCH_06:IMon')+15.
        dCH7=caget('MEBT_PS:DCH_07:IMon')+15.

        dCV1=caget('MEBT_PS:DCV_01:IMon')+15.
        dCV2=caget('MEBT_PS:DCV_02:IMon')+15.
        dCV3=caget('MEBT_PS:DCV_03:IMon')+15.
        dCV4=caget('MEBT_PS:DCV_04:IMon')+15.
        dCV5=caget('MEBT_PS:DCV_05:IMon')+15.
        dCV6=caget('MEBT_PS:DCV_06:IMon')+15.
        dCV7=caget('MEBT_PS:DCV_07:IMon')+15.


        dDCH1,dDCH2,dDCH3,dDCH4,dDCH5,dDCH6,dDCH7=np.abs((dCH1-dCH10)/dCH10),np.abs((dCH2-dCH20)/dCH20),np.abs((dCH3-dCH30)/dCH30),np.abs((dCH4-dCH40)/dCH40),np.abs((dCH5-dCH50)/dCH50),np.abs((dCH6-dCH60)/dCH60),np.abs((dCH7-dCH70)/dCH70)
        dDCV1,dDCV2,dDCV3,dDCV4,dDCV5,dDCV6,dDCV7=np.abs((dCV1-dCV10)/dCV10),np.abs((dCV2-dCV20)/dCV20),np.abs((dCV3-dCV30)/dCV30),np.abs((dCV4-dCV40)/dCV40),np.abs((dCV5-dCV50)/dCV50),np.abs((dCV6-dCV60)/dCV60),np.abs((dCV7-dCV70)/dCV70)


	if (dDCH1<1e-4) or (dDCH2<1e-4) or (dDCH3<1e-4) or (dDCH4<1e-4) or (dDCH5<1e-4) or (dDCH6<1e-4) or (dDCV7<1e-4) or (dDCV1<1e-4) or (dDCV2<1e-4) or (dDCV3<1e-4) or (dDCV4<1e-4) or (dDCV5<1e-4) or (dDCV6<1e-4) or (dDCV7<1e-4) :
            print iTotal
            print 'WARNING ! ! !   dCHV  !!! '
            time.sleep(3)
            dCH1,dCH2,dCH3,dCH4,dCH5,dCH6,dCH7=1.,1.,1.,1.,1.,1.,1.
            dCV1,dCV2,dCV3,dCV4,dCV5,dCV6,dCV7=1.,1.,1.,1.,1.,1.,1.
            flagHVWrite=1  

        iTotal+=1
        if iTotal>NTotal:
            break
        print iTotal
                  


        if iTotal % nFresh==1:
            cHV=np.round(np.random.random((14))*AmpBound*20-AmpBound*10)/10.
            flagHV=np.ones((14))*np.sign(np.random.random((14))-0.5)
        else:
            if iTotal % np.round(nFresh/4)==nFresh/8:
                flagHV=np.ones((14))*np.sign(np.random.random((14))-0.5)
            
            cHV+=np.random.random((14))*Amp*flagHV
            flagHV[cHV>AmpBound]=-1
            flagHV[cHV<-AmpBound]=1
            cHV[cHV>AmpBound]=AmpBound*2-cHV[cHV>AmpBound]
            cHV[cHV<-AmpBound]=-AmpBound*2-cHV[cHV<-AmpBound]
        
        cHV=np.round(cHV*100)/100
        
        for iCH in range(7):
            nameCH='MEBT_PS:DCH_0'+str(iCH+1)+':ISet'
            caput(nameCH,cHV[iCH])
            
        for iCV in range(7):
            nameCV='MEBT_PS:DCV_0'+str(iCV+1)+':ISet'
            caput(nameCV,cHV[iCV+7])    
        
        if iTotal>10:
            xBPMStd=np.std([xBpm1,xBpm2,xBpm3,xBpm4]) 
            yBPMStd=np.std([yBpm1,yBpm2,yBpm3,yBpm4])               
            if (xBPMStd<1e-7) and (yBPMStd<1e-7):
                iTotal-=1
                print iTotal
                print 'WARNING ! ! !   BPM  !!! '
                time.sleep(10)
                continue 



        time.sleep(2.8)
        if iTotal % nFresh==1:
            time.sleep(6)

        
        
        nAve=1
        xBpm=np.zeros((5))
        yBpm=np.zeros((5))
        
        for iAve in range(nAve):
            for iBPM in range(5):
                nameXBPM='BPM:'+str(iBPM+1)+'-X11'
                nameYBPM='BPM:'+str(iBPM+1)+'-Y11'
                
                xBpm[iBPM]+=caget(nameXBPM)
                yBpm[iBPM]+=caget(nameYBPM)
                
            #time.sleep(.1)
            
        xBpm/=nAve
        yBpm/=nAve
    
	if iTotal==1:
            xBpm1=np.mean(xBpm)
            yBpm1=np.mean(yBpm)
        elif iTotal==2:
            xBpm2=np.mean(xBpm1)
            yBpm2=np.mean(yBpm1)
            xBpm1=np.mean(xBpm)
            yBpm1=np.mean(yBpm)

	elif iTotal==3:
            xBpm3=np.mean(xBpm2)
            yBpm3=np.mean(yBpm2)
            xBpm2=np.mean(xBpm1)
            yBpm2=np.mean(yBpm1)
            xBpm1=np.mean(xBpm)
            yBpm1=np.mean(yBpm)
	else:
            xBpm4=np.mean(xBpm3)
            yBpm4=np.mean(yBpm3)	
            xBpm3=np.mean(xBpm2)
            yBpm3=np.mean(yBpm2)	
            xBpm2=np.mean(xBpm1)
            yBpm2=np.mean(yBpm1)
            xBpm1=np.mean(xBpm)
            yBpm1=np.mean(yBpm)
    

        strWrite=str(cHV).replace('\n','')[1:-1:]+' '+ str(np.round(xBpm*100.)/100).replace('\n','')[1:-1:]+'  ' \
        + str(np.round(yBpm*100.)/100).replace('\n','')[1:-1:]+'  ' \
        +str(Q1)+'  '+str(Q2)+'  '+str(Q3)+'  '+str(Q4)+'  '+str(Q5)+'  '+str(Q6)+'  ' +str(Q7)+'  ' \
        +str(dCH1-15.)+'  '+str(dCH2-15.)+'  '+str(dCH3-15.)+'  '+str(dCH4-15.)+'  '+str(dCH5-15.)+'  '+str(dCH6-15.)+'  ' +str(dCH7-15.)+'  '\
        +str(dCV1-15.)+'  '+str(dCV2-15.)+'  '+str(dCV3-15.)+'  '+str(dCV4-15.)+'  '+str(dCV5-15.)+'  '+str(dCV6-15.)+'  ' +str(dCV7-15.)+'  '\
        +str(acct1)+'  '+str(acct2)+'  '+str(acct3)+'\n'
	if flagHVWrite==0:
            fid.writelines(strWrite)
    
















