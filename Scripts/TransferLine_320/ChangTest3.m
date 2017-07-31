clear;

clear all;
close;
clc;
Lattice_read=xlsread('Changjj.xlsx','Lattice4','A2:F33');
Lattice=Lattice_read;
Lattice(:,2)=Lattice_read(:,2)/1000;
Lattice(:,4)=Lattice_read(:,4)/1000;
Lattice(:,5)=Lattice_read(:,5)/1000;
Lattice(:,6)=Lattice_read(:,6)/180*pi;

%% 
xMean=0.0;
xpMean=0;
yMean=-0.0;
ypMean=0;

xSigma=[50,10;10,8];
ySigma=[50,-10;-10,8];

O=zeros(2);

allMean=[xMean,xpMean,yMean,ypMean];
allSigma=[xSigma,O;O,ySigma];
numParticle=1e5;
partDistri=mvnrnd(allMean,allSigma,numParticle);




inputPara=find(Lattice(:,1)==2);
inputParaMax=ones(length(inputPara),1)*15;
inputParaMin=-ones(length(inputPara),1)*15;
% [obj1_effi,obj2_cent,obj3_size,obj4_coef]=Fit4cjj(partDistri,Lattice(inputPara,3),numParticle)

objBak=0;
LatticeBak=Lattice;
obj1_effiBak=[];
VSPartRecBak=zeros(4,5,100);
nVSPartRecBak=1;

for nInputPara=1:length(inputPara)
    iInputPara=inputPara(nInputPara);
    for iNSteps=1:12
        Lattice(iInputPara,3)=LatticeBak(iInputPara,3)*(1-0.11+(iNSteps-1)*0.02);
        [obj1_effi,obj2_cent,obj3_size,obj4_coef,obj5_EffiAll,VSPartRec]=Fit4cjj(partDistri,Lattice(inputPara,3),numParticle);
        obj=obj1_effi+obj2_cent+obj3_size+obj4_coef;
        obj=obj5_EffiAll;
        if obj>objBak
            objBak=obj;
            LatticeBak=Lattice;
            obj1_effiBak=[obj1_effiBak,obj];

            VSPartRecBak(:,:,nVSPartRecBak)=VSPartRec;
            nVSPartRecBak=nVSPartRecBak+1;
        end
    end
    nInputPara
end

LatticeBakWrite=LatticeBak;
LatticeBakWrite(:,2)=LatticeBakWrite(:,2)*1000;
LatticeBakWrite(:,4)=LatticeBakWrite(:,4)*1000;
LatticeBakWrite(:,5)=LatticeBakWrite(:,5)*1000;
LatticeBakWrite(:,6)=LatticeBakWrite(:,6)*180/pi;
LatticeBakWrite(inputPara,3)

xlswrite('Changjj.xlsx',LatticeBakWrite,'Lattice4','A2:F33')


figure(101)
plot(obj1_effiBak);
hold on
plot(obj1_effiBak,'ro');
