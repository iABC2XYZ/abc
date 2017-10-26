clear
clc;
close all;

syms px py pz px1 py1 pz1

Pn1=[px1, py1, pz1]
Pn=[px, py, pz]

syms Bx By Bz

syms t c g q m

Bn=[Bx By Bz]

fn=cross((Pn1-Pn)/(t*c)-(Pn1+Pn)/(2*g),q*Bn/(m*c))


figure(1)
text(0.1,0.5,['$',latex(fn),'$'],'Interpreter','latex','FontSize',18)


fn1=fn(1)
fn2=fn(2)
fn3=fn(3)


figure(11)
text(0.1,0.5,['$',latex(fn1),'$'],'Interpreter','latex','FontSize',18)

figure(12)
text(0.1,0.5,['$',latex(fn2),'$'],'Interpreter','latex','FontSize',18)

figure(13)
text(0.1,0.5,['$',latex(fn3),'$'],'Interpreter','latex','FontSize',18)

[px1, py1, pz1]=solve([fn1,fn2,fn3],[px1,py1,pz1])


figure(21)
text(0.1,0.5,['$',latex(px1),'$'],'Interpreter','latex','FontSize',18)

figure(22)
text(0.1,0.5,['$',latex(py1),'$'],'Interpreter','latex','FontSize',18)

figure(23)
text(0.1,0.5,['$',latex(pz1),'$'],'Interpreter','latex','FontSize',18)

%%

fn1V=simplify((fn1))
fn2V=simplify((fn2))
fn3V=simplify((fn3))

figure(31)
text(0.1,0.5,['$',latex(fn1V),'$'],'Interpreter','latex','FontSize',18)

figure(32)
text(0.1,0.5,['$',latex(fn2V),'$'],'Interpreter','latex','FontSize',18)

figure(33)
text(0.1,0.5,['$',latex(fn3V),'$'],'Interpreter','latex','FontSize',18)














