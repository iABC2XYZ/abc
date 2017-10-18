clear
clc;
close all;

A=[  0.08594525  0.97309479  0.4578155   0.69874609];

aDST=dst(A)

aDstDst=dst(aDST)

B= [0.48371213  0.2828192   0.91922809  0.04567313]

bDCT=dct(B)

bDctDct=dct(dct(B))

idct(bDCT)