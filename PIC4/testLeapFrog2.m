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


C=1/(1+(t/2/g)^2*(Bx^2+By^2+Bz^2))

A=[A11,A12,A13;A21,A22,A23;A31,A32,A33]


figure(1)
text(0.1,0.5,['$',latex(A),'$'],'Interpreter','latex','FontSize',18)


A_C=A*C
A_C_S=simplify(A_C)


figure(2)
for i=1:3
    for j=1:3
        text(0.1+0.3*(i-1),0.8-0.3*(j-1),['$',latex(A_C_S(i,j)),'$'],'Interpreter','latex','FontSize',23)
    end
end



syms Px Py Pz

P=[Px;Py;Pz]

Pnew=A_C_S*P

Pnew_1=simplify(Pnew(1))
Pnew_2=simplify(Pnew(2))
Pnew_3=simplify(Pnew(3))

figure(3)
hold on
text(0.1,0.8,['$',latex(Pnew_1),'$'],'Interpreter','latex','FontSize',18)
text(0.1,0.5,['$',latex(Pnew_2),'$'],'Interpreter','latex','FontSize',18)
text(0.1,0.2,['$',latex(Pnew_3),'$'],'Interpreter','latex','FontSize',18)


%%

syms c q m L px py pz
PnewSubs=subs(Pnew,{t,Bx,By,Bz,Px,Py,Pz},{t*c/L,q*L*Bx/m/c,q*L*By/m/c,q*L*Bz/m/c,px/m/c,py/m/c,pz/m/c})*m*c

PnewSubs_1=simplify(PnewSubs(1))
PnewSubs_2=simplify(PnewSubs(2))
PnewSubs_3=simplify(PnewSubs(3))

figure(4)
hold on
text(0.1,0.8,['$',latex(PnewSubs_1),'$'],'Interpreter','latex','FontSize',18)
text(0.1,0.5,['$',latex(PnewSubs_2),'$'],'Interpreter','latex','FontSize',18)
text(0.1,0.2,['$',latex(PnewSubs_3),'$'],'Interpreter','latex','FontSize',18)









