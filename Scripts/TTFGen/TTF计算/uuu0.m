% Transit time factor for HWR cavity,use efficiency length.
clc;clear;close all;
frquency=162.5*10^6;
energymin=1.3;
energymax=10;
E0=931.494;
lamd=3.0*10^8/frquency;%(m)
V0011=4.79E5;
betamin=0.005;
betamax=1;
inputdata=importdata('E:\calculatefile\HIAF\1-5mA_25MeV\HWR1.3-25MeV_5mA\TTF\e.txt');
beta0min=sqrt(1-1/((E0+energymin)/E0)^2);
beta0max=sqrt(1-1/((E0+energymax)/E0)^2);
data=inputdata.data;
data_size=size(data);
x011=data(:,1);
x011=x011-(x011(data_size(1))+x011(1))/2;
Ex011=data(:,4);
T011=zeros(data_size(1),1);
beta=betamin:(betamax-betamin)/(data_size(1)-1):betamax;
for i=1:1:data_size(1);
T011(i)=sum((-Ex011*10^6).*sin((2*pi.*(x011))./(beta(i)*lamd))*(x011(data_size(1))-x011(1))/(data_size(1)-1))/ ...
         sum((abs(-Ex011)*10^6)*(x011(data_size(1))-x011(1))/(data_size(1)-1));
end
i=1;
while beta0min>beta(i)
    i=i+1;
end
i=i-1;
j=1;
while beta0max>beta(j)
    j=j+1;
end
s=sum((abs(Ex011)*10^6)*(x011(data_size(1))-x011(1))/(data_size(1)-1))
TTF=T011';
plot(beta,T011);hold on;
plot(beta(i:j),T011(i:j),'r','LineWidth',5);hold on;

% Transit time factor for HWR cavity,use efficiency length.
clc;clear;
frquency=81.25*10^6;
energymin=1.54;
energymax=60.6;
E0=931.494;
lamd=3.0*10^8/frquency;%(m)
V0011=4.79E5;
betamin=0.005;
betamax=1;
inputdata=importdata('D:\calculatefile\HIAF\1.4-17MeV\HIAF0.4-15-1mA\TTF\085.txt');
beta0min=sqrt(1-1/((E0+energymin)/E0)^2);
beta0max=sqrt(1-1/((E0+energymax)/E0)^2);
data=inputdata.data;
data_size=size(data);
x011=data(:,1);
x011=x011-(x011(data_size(1))+x011(1))/2;
Ex011=data(:,4);
T011=zeros(data_size(1),1);
beta=betamin:(betamax-betamin)/(data_size(1)-1):betamax;
for i=1:1:data_size(1);
T011(i)=sum((Ex011*10^6).*sin((2*pi.*(x011))./(beta(i)*lamd))*(x011(data_size(1))-x011(1))/(data_size(1)-1))/ ...
         sum((abs(Ex011)*10^6)*(x011(data_size(1))-x011(1))/(data_size(1)-1));
end
i=1;
while beta0min>beta(i)
    i=i+1;
end
i=i-1;
j=1;
while beta0max>beta(j)
    j=j+1;
end
s=sum((abs(Ex011)*10^6)*(x011(data_size(1))-x011(1))/(data_size(1)-1))
TTF=T011';
plot(beta,T011);hold on;
plot(beta(i:j),T011(i:j),'g','LineWidth',5);hold on;

% Transit time factor for HWR cavity,use efficiency length.
clc;clear;
frquency=325*10^6;
energymin=17;
energymax=43;
E0=931.494;
lamd=3.0*10^8/frquency;%(m)
V0011=4.79E5;
betamin=0.005;
betamax=1;
inputdata=importdata('D:\calculatefile\HIAF\1.4-17MeV\HIAF2.1-17\TTF¼ÆËã\021.txt');
beta0min=sqrt(1-1/((E0+energymin)/E0)^2);
beta0max=sqrt(1-1/((E0+energymax)/E0)^2);
data=inputdata.data;
data_size=size(data);
x011=data(:,1);
x011=x011-(x011(data_size(1))+x011(1))/2;
Ex011=data(:,4);
T011=zeros(data_size(1),1);
beta=betamin:(betamax-betamin)/(data_size(1)-1):betamax;
for i=1:1:data_size(1);
T011(i)=sum((Ex011*10^6).*sin((2*pi.*(x011))./(beta(i)*lamd))*(x011(data_size(1))-x011(1))/(data_size(1)-1))/ ...
         sum((abs(Ex011)*10^6)*(x011(data_size(1))-x011(1))/(data_size(1)-1));
end
i=1;
while beta0min>beta(i)
    i=i+1;
end
i=i-1;
j=1;
while beta0max>beta(j)
    j=j+1;
end
s=sum((abs(Ex011)*10^6)*(x011(data_size(1))-x011(1))/(data_size(1)-1))
TTF=T011';
plot(beta,T011);hold on;
plot(beta(i:j),T011(i:j),'y','LineWidth',5);hold on;

% Transit time factor for HWR cavity,use efficiency length.
clc;clear;
frquency=325*10^6;
energymin=43;
energymax=150;
E0=931.494;
lamd=3.0*10^8/frquency;%(m)
V0011=4.79E5;
betamin=0.005;
betamax=1;
inputdata=importdata('D:\calculatefile\HIAF\1.4-17MeV\HIAF2.1-17\TTF¼ÆËã\040.txt');
beta0min=sqrt(1-1/((E0+energymin)/E0)^2);
beta0max=sqrt(1-1/((E0+energymax)/E0)^2);
data=inputdata.data;
data_size=size(data);
x011=data(:,1);
x011=x011-(x011(data_size(1))+x011(1))/2;
Ex011=data(:,4);
T011=zeros(data_size(1),1);
beta=betamin:(betamax-betamin)/(data_size(1)-1):betamax;
for i=1:1:data_size(1);
T011(i)=sum((Ex011*10^6).*sin((2*pi.*(x011))./(beta(i)*lamd))*(x011(data_size(1))-x011(1))/(data_size(1)-1))/ ...
         sum((abs(Ex011)*10^6)*(x011(data_size(1))-x011(1))/(data_size(1)-1));
end
i=1;
while beta0min>beta(i)
    i=i+1;
end
i=i-1;
j=1;
while beta0max>beta(j)
    j=j+1;
end
s=sum((abs(Ex011)*10^6)*(x011(data_size(1))-x011(1))/(data_size(1)-1))
TTF=T011';
plot(beta,T011);hold on;
plot(beta(i:j),T011(i:j),'c','LineWidth',5)



