function M=Quadrupole(l,k)

K=sqrt(abs(k))*l;
Mx=[cos(K),1/sqrt(abs(k))*sin(K);
    -sqrt(abs(k))*sin(K),cos(K)];
My=[cosh(K),1/sqrt(abs(k))*sinh(K);
    -sqrt(abs(k))*sinh(K),cosh(K)];
Mo=zeros(2);
if k>0
    M=[Mx,Mo;Mo,My];
else
    M=[My,Mo;Mo,Mx];
end