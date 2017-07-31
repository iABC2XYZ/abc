clc;clear all;clf;
%%eps: emittance_z/emittance_x					
% first column: k_z/k_x (tune ratio)					
% second column: k_x/k_xo (tune depression)					
% third column: growth rate of exchange (darkest zones 					
% correspond to 1 e-folding in typically 1 betatron period (without 					
% space charge) - see I. Hofmann et al. PRSTAB 6, 024202 (2003)					
% Remarks on plotting: 					
% 1) Note that x stands for either transverse coordinate					
% 2) when creating contour plots for the "growth rates" as heights  					
%   note that the lowes  height value shouldn't be taken too small,					
%   otherwise the edge to zero values (white zones) has  					
%   too much of a zig-zag (like in Fig.2, of our recent paper 					
%   L. Groening et al., PRL); if it is too large the mountain peaks					
%   don't reach the level k_x/k_xo=1, which they should more or    					
% less do, at least close to 0.96 (I have stopped producing data at					
% k_x/k_xo=0.96 since the convergence degrades towards "1")					
fr=fopen('D:\calculatefile\HIAF\1.4-17MeV\HIAF2.1-17\QWR\u238_34-QWR\hofmman chart\yy.txt');%%%y
ff=fopen('D:\calculatefile\HIAF\1.4-17MeV\HIAF2.1-17\QWR\u238_34-QWR\hofmman chart\xx.txt');%%%x
fbat=xlsread('D:\calculatefile\HIAF\1.4-17MeV\HIAF2.1-17\QWR\u238_34-QWR\hofmman chart\1.xls');
k=5;%%%%% 第k组,表示计算不同的横纵向发射度比值—取值可从0.1—10
world2=fgetl(ff) ; %%%%每个文件含一行字母
world1=fgetl(fr) ; %%%%每个文件含一行字母
f2=fscanf(ff,'%f');
f1=fscanf(fr,'%f');
num_plot=42;
N=0;

for j=1:num_plot
        N=N+1;
        xx(j)=1/f2(j*3);  
        yy(j)=f1(j*4-2);      
end


myjet=jet(100);
for i=1:20
    my(i,:)=[1-0.05*(i-1),1-0.05*(i-1),1];
end
for i=1:100
    my(i+20,:)=myjet(i,:);    
end

N=0;
for i=1:200
    for j=1:51
        N=N+1;
        x(j,i)=fbat(N,k*4-3);
        y(j,i)=fbat(N,k*4-2);
        z(j,i)=fbat(N,k*4-1);
    end
end
for i=1:num_plot
    text(xx(i)+0.01,yy(i), num2str(i),'FontSize',10);hold on;
plot(xx(i),yy(i),'r*');hold on;
end
pcolor(x,y,z/50);
 axis([min(x(1,:)),max(x(1,:)),min(y(:,1)),1]);
 title('Hofmann chart@ eps=0.93','fontsize',15)
 xlabel('k_z/k_x(tune ratio)','fontsize',12);
 ylabel('k_x/k_xo(tune depression)','fontsize',12)
 shading interp
 colormap(my);
 colorbar;
 fclose('all');