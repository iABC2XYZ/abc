clear
clc;
close all;

ax=10
ay=10
az=10

syms s
aX2=ax^2+s
aY2=ay^2+s
aZ2=az^2+s
aXYZ=sqrt(aX2*aY2*aZ2)
Fx=1/(aX2*aXYZ)
Fy=1/(aY2*aXYZ)
Fz=1/(aZ2*aXYZ)
vFx=int(Fx,s,0,inf)
vFy=int(Fy,s,0,inf)
vFz=int(Fz,s,0,inf)

vpa(vFx)
vpa(vFy)
vpa(vFz)

vpa(vpa(vFx+vFy+vFz)*ax*ay*az/2)










