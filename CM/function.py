#!/usr/bin/env python2
# -*- coding: utf-8 -*-

import numpy as np
from math import sqrt
import time
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def StepOneEFirstAcct(pNorm, eNorm, tNorm, qCharge):
    argE = (tNorm * qCharge / 2) * eNorm
    pNorm_ = pNorm + argE
    return pNorm_

def StepTwoBRotation(pNorm_, bNorm, tNorm, qCharge):
    pNormX_ = pNorm_[0, 0]
    pNormY_ = pNorm_[1, 0]
    pNormZ_ = pNorm_[2, 0]
    global gammaC_
    gammaC_ = sqrt(1 + pNormX_ ** 2 + pNormY_ ** 2 + pNormZ_ ** 2)
    bNormX = bNorm[0, 0]
    bNormY = bNorm[1, 0]
    bNormZ = bNorm[2, 0]
    argA = ((tNorm * qCharge) / (2 * gammaC_))**2  
    e = qCharge * tNorm / gammaC_

    c = 1 / (1 + argA * (bNormX * bNormX + bNormY * bNormY + bNormZ * bNormZ))  

    argA11 = 1 + argA * (bNormX * bNormX - bNormY * bNormY - bNormZ * bNormZ)  
    argA12 = bNormZ * e + bNormX * bNormY * argA * 2
    argA13 = bNormX * bNormZ * argA * 2 - bNormY * e
    argA21 = bNormX * bNormY * argA * 2 - bNormZ * e
    argA22 = 1 + argA * (bNormY * bNormY - bNormX * bNormX - bNormZ * bNormZ)
    argA23 = bNormX * e + bNormY * bNormZ * argA * 2
    argA31 = bNormY * e + bNormX * bNormZ * argA * 2
    argA32 = bNormY * bNormZ * argA * 2 - bNormX * e
    argA33 = 1 + argA * (bNormZ * bNormZ - bNormY * bNormY - bNormX * bNormX)

    argAm = np.mat([[argA11, argA12, argA13],  
                    [argA21, argA22, argA23],
                    [argA31, argA32, argA33]])

    pNorm1_ = c * np.dot(argAm, pNorm_)
    return pNorm1_

def StepThreeBCoupleRZ(pNorm1_, tNorm, rNorm, xNorm):  
    pNormX1__ = pNorm1_[0, 0] + (pNorm1_[2, 0] * pNorm1_[2, 0]) * tNorm / (gammaC_ * (rNorm + xNorm))
    argS = tNorm / (4 * gammaC_ * (rNorm + xNorm))  
    pNormZ1__ = pNorm1_[2, 0] * ((1 - argS * (pNorm1_[0, 0] + pNormX1__)) / (1 + argS * (pNorm1_[0, 0] + pNormX1__)))
    pNormX1__ = pNorm1_[0, 0] + (tNorm / (gammaC_ * (rNorm + xNorm))) * ((pNorm1_[2, 0] + pNormZ1__) / 2) * ((pNorm1_[2, 0] + pNormZ1__) / 2)
    pNorm1__ = np.mat([[pNormX1__],
                       [pNorm1_[1, 0]],
                       [pNormZ1__]])
    return pNorm1__


def StepFourESecondAcct(pNorm1__, eNorm, tNorm, qCharge):
    argE = (tNorm * qCharge / 2) * eNorm
    pNorm1 = pNorm1__ + argE
    return pNorm1


def StepFiveXAdvance(xNorm, pNorm1, tNorm, rNorm):  
    pNormX1 = pNorm1[0, 0]
    pNormY1 = pNorm1[1, 0]
    pNormZ1 = pNorm1[2, 0]

    gammaC1 = sqrt(1 + pNormX1 ** 2 + pNormY1 ** 2 + pNormZ1 ** 2)
    argC = (tNorm / gammaC1) * pNorm1
    xNorm1 = xNorm + argC
    xNorm1[2, 0] = xNorm[2, 0] + (tNorm * pNorm1[2, 0]) / (gammaC1 * (1 + xNorm1[0, 0] / rNorm))
    return xNorm1

def PartAdvanceLeapFrog(xNorm, pNorm, eNorm, bNorm, tNorm, rNorm ,qCharge):
    pNorm_ = StepOneEFirstAcct(pNorm, eNorm, tNorm, qCharge)
    pNorm1_ = StepTwoBRotation(pNorm_, bNorm, tNorm, qCharge)
    pNorm1__ = StepThreeBCoupleRZ(pNorm1_, tNorm, rNorm, xNorm[0,0])
    pNorm1 = StepFourESecondAcct(pNorm1__, eNorm, tNorm, qCharge)
    xNorm1 = StepFiveXAdvance(xNorm, pNorm1, tNorm,  rNorm)
    return xNorm1, pNorm1


# 例子.......................................................................................................
xNorm = np.mat([[0],
                [0],
                [5]])
pNorm = np.mat([[0],
                [0],
                [5]])
eNorm = np.mat([[0],
                [0],
                [0]])
bNorm = np.mat([[9],
                [0],
                [0]])
tNorm = 0.001
rNorm = float("inf")
qCharge = 1
argLoop = 20000   #循环次数
i = 0
Filename = r"/home/p/CM/dat"
now = int(time.time())
timeArray = time.localtime()
otherStyleTime = time.strftime("%Y-%m-%d %H:%M:%S", timeArray)
f = open(Filename, 'a')
f.write('\n')
f.write(str(otherStyleTime))
f.write('\n')
f.close()
arrX = []
arrY = []
arrZ = []
while True:
    f = open(Filename, 'a')
    f.write(str(round(xNorm[0, 0], 4)))
    f.write("   ")
    f.write(str(round(xNorm[1, 0], 4)))
    f.write("   ")
    f.write(str(round(xNorm[2, 0], 4)))
    f.write("                 ")
    f.write(str(round(pNorm[0, 0], 4)))
    f.write("   ")
    f.write(str(round(pNorm[1, 0], 4)))
    f.write("   ")
    f.write(str(round(pNorm[2, 0], 4)))
    f.write('\n')
    f.close()
    arrX.append(xNorm[0, 0])
    arrY.append(xNorm[1, 0])
    arrZ.append(xNorm[2, 0])
    xNorm, pNorm = PartAdvance(xNorm, pNorm, eNorm, bNorm, tNorm, rNorm ,qCharge)
    i = i + 1
    if i == argLoop:
        break

fig = plt.figure()
ax = Axes3D(fig)
ax.plot(arrX, arrY, arrZ, label='curve')
ax.legend()
plt.show()



