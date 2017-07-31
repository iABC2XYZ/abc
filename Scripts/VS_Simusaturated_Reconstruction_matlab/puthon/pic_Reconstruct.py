# -*- coding: utf-8 -*-
"""
Created on Fri Jun 30 17:19:07 2017

@author: Administrator
"""

import numpy as np
from scipy import interpolate
import cv2
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D


def RowInterpl(pic):
    '''按行插值,此函数内id(pic)=id(pic_interpl)'''
    #全图饱和点的标志符
    flag_pic=(pic>=1.0)
    pic_interpl=pic
    m_row,n_col=pic.shape
    for i in range(m_row):
        #本行
        i_row=pic[i,:]
        #本行饱和点标志
        flag_row=flag_pic[i,:]
        #如果本行无饱和点，则进行下一行迭代
        str_flag_row=flag_row.tostring()
        if str_flag_row.find(1)<0:
            continue
        #本行未饱和部分x0/y0
        x0=np.where(i_row<1.0)[0]
        y0=i_row[x0]
        #本行饱和部分的索引x1
        x1=np.where(i_row>=1.0)[0]
        #使用样条插值对饱和部分进行插值
        tck = interpolate.splrep(x0, y0,s=0.05)
        y1 = interpolate.BSpline
        y1 = interpolate.splev(x1, tck, der=0)

        pic_interpl[i,x1]=y1
        
    return pic_interpl

def ColInterpl(pic):
    '''按列插值,id(pic)≠id(col_interpl)'''
    #转置时会自动发生复制，地址发生了改变
    pic_1=pic.T
    pic_2=RowInterpl(pic_1)
    col_interpl=pic_2.T
    return col_interpl

def pic_Reconstruct(pic):
    '''图像的插值重构'''
    pic1 = np.copy(pic)
    pic2 = np.copy(pic)

    pic_Row = RowInterpl(pic1)
    pic_Col = ColInterpl(pic2)    
 
    pic_Recon = (pic_Row+pic_Col)/2
    
    return pic_Recon

'''三次样条插值重构'''
img_int8 = cv2.imread("sun1.png",cv2.IMREAD_GRAYSCALE)
img2_float64 = img_int8/img_int8.max()
img_recon = pic_Reconstruct(img2_float64)
print(img_recon.max())
'''卷积滤波&&高斯滤波'''
kernel = np.ones((5,5),np.float64)/25
dst1 = cv2.filter2D(img_recon,-1,kernel)
dst2 = cv2.GaussianBlur(img_recon,(5,5),0)

'''3D视图'''
rows,cols=img_int8.shape
fig1 = plt.figure('原始图像')
fig2 = plt.figure('重构后图像')
fig3 = plt.figure('图像差')
ax1 = Axes3D(fig1)
ax2 = Axes3D(fig2)
ax3 = Axes3D(fig3)
X = range(cols)
Y = range(rows)
X, Y = np.meshgrid(X, Y)
Z = img_int8
Z1 = dst1*255.0
Z2 = dst2*255.0

ax1.plot_surface(X,Y, Z)
ax2.plot_surface(X,Y, Z1)
ax3.plot_surface(X,Y, Z1-Z)
#ax.contourf(X, Y, Z2, zdir='z', offset=-2, cmap=plt.cm.hot)
plt.show()