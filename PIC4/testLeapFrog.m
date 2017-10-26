clear
clc;
close all;

syms g t Bx By Bz

A11=1+t^2/(2*g)^2*(Bx^2-By^2-Bz^2)
A12=t*(Bz/g+Bx*By*t/(2*g^2))
A13=t*(-By/g+Bx*Bz*t/(2*g^2))

A21=t*(-Bz/g+Bx*By*t/(2*g^2))
A22=1+t^2/(2*g)^2*(By^2-Bx^2-Bz^2)
A23=t*(Bx/g+By*Bz*t/(2*g^2))

A31=t*(By/g+Bz*Bx*t/(2*g^2))
A32=t*(-Bx/g+By*Bz*t/(2*g^2))
A33=1+t^2/(2*g)^2*(Bz^2-Bx^2-By^2)





A=[A11,A12,A13;A21,A22,A23;A31,A32,A33]



figure(1)
text(0.1,0.5,['$',latex(A),'$'],'Interpreter','latex','FontSize',18)

syms c q m L 

B=subs(A,{t,Bx,By,Bz},{t*c/L,q*L*Bx/m/c,q*L*By/m/c,q*L*Bz/m/c})

figure(2)
for i=1:3
    for j=1:3
        text(0.1+0.3*(i-1),0.8-0.3*(j-1),['$',latex(B(i,j)),'$'],'Interpreter','latex','FontSize',23)
    end
end



syms px py pz
C=B

Px=px/m/c
Py=py/m/c
Pz=pz/m/c


C(:,1)=C(:,1)*Px
C(:,2)=C(:,2)*Py
C(:,3)=C(:,3)*Pz

C=simplify(C)

figure(3)
for i=1:3
    for j=1:3
        text(0.1+0.3*(i-1),0.8-0.3*(j-1),['$',latex(C(i,j)),'$'],'Interpreter','latex','FontSize',23)
    end
end



D=sum(C')'
D=simplify(D)
figure(1)
text(0.1,0.5,['$',latex(D(1)),'$'],'Interpreter','latex','FontSize',18)

E=D*m*c
E=simplify(E)
figure(1)
text(0.1,0.5,['$',latex(E(1)),'$'],'Interpreter','latex','FontSize',18)










