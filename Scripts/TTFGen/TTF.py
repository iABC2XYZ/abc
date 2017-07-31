# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 09:28:26 2017

@author: A
"""
import numpy as np
import matplotlib.pyplot as plt

plt.close('all')

nCell=3

betaG=0.6

betaC=0.3

betaStart=0.1
betaEnd=0.9
betaStep=0.001

def TTFC(nCell,betaC,betaG):
    if (np.abs(betaC-betaG)<1.0e-6):
        return np.pi/4.
    else:
        return (betaC/betaG)**2*np.cos(np.pi*nCell/(2*betaC/betaG))*(-1)**((nCell-1)/2)/(nCell*((betaC/betaG)**2-1))

        
def TTFS(nCell,betaC,betaG):
    if (np.abs(betaC-betaG)<1.0e-6):
        return np.pi/4.
    else:
        return (betaC/betaG)**2*np.sin(np.pi*nCell/(2*betaC/betaG))*(-1)**((nCell+2)/2)/(nCell*((betaC/betaG)**2-1))

        

def TTF(nCell,betaC,betaG):
    if (np.mod(nCell,2)==0):
        return TTFS(nCell,betaC,betaG)
    elif (np.mod(nCell,2)==1):
        return TTFC(nCell,betaC,betaG)
    else:
        pass
    
def TTFGen(nCell,betaG,betaStart,betaEnd,betaStep):
    betaArray=np.arange(betaStart,betaEnd,betaStep)
    TTFArray=np.zeros_like(betaArray)
    nBetaC=0
    for iBetaC in betaArray:
        TTFArray[nBetaC]=TTF(nCell,iBetaC,betaG)
        nBetaC+=1
    return betaArray,TTFArray
    

    


betaArray,TTFArray=TTFGen(nCell,betaG,betaStart,betaEnd,betaStep)


plt.figure('Beta - TTF')
plt.plot(betaArray,TTFArray,'.')




