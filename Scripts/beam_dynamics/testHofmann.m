clear
clc;
close all;
dataEps06=importdata('eps06.txt');

Kz_Kx=dataEps06(:,1);
Kx_Kx0=dataEps06(:,2);
GrowthRate=dataEps06(:,3);

figure(1)
plot3(Kz_Kx,Kx_Kx0,GrowthRate)

view(0,90)



