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

xSigma=[1,0;0,1];
ySigma=[1,0;0,1];

O=zeros(2);

allMean=[xMean,xpMean,yMean,ypMean];
allSigma=[xSigma,O;O,ySigma];
numParticle=1e5;
partDistri=mvnrnd(allMean,allSigma,numParticle);




inputPara=find(Lattice(:,1)==2);
% inputParaMax=ones(length(inputPara),1)*15;
% inputParaMin=-ones(length(inputPara),1)*15;

partDistriTemp=partDistri;

flagPart=ones(numParticle,1);

[LatticeM,LatticeN]=size(Lattice);
VSM=length(find(Lattice(:,1)==11 | Lattice(:,1)==12));
VSPartRec=zeros(VSM,5);
FCM=length(find(Lattice(:,1)==11));
FCPartRec=zeros(1,FCM);

nVSPartRec=1;
nFCPartRec=1;
for iLatticeM=1:LatticeM
    Para=Lattice(iLatticeM,:);
    if Para(1)<=10
        switch Para(1)
            case 1
                M=Drift(Para(2));
            case 2
                M=Quadrupole(Para(4),Para(3));
            case 3
                M=Quadrupole(Para(5),Para(6));
        end
        
        
        partDistriTemp(flagPart==1,1)=M(1,1)*partDistri(flagPart==1,1)+M(1,2)*partDistri(flagPart==1,2)+M(1,3)*partDistri(flagPart==1,3)+M(1,4)*partDistri(flagPart==1,4);
        partDistriTemp(flagPart==1,2)=M(2,1)*partDistri(flagPart==1,1)+M(2,2)*partDistri(flagPart==1,2)+M(2,3)*partDistri(flagPart==1,3)+M(2,4)*partDistri(flagPart==1,4);
        partDistriTemp(flagPart==1,3)=M(3,1)*partDistri(flagPart==1,1)+M(3,2)*partDistri(flagPart==1,2)+M(3,3)*partDistri(flagPart==1,3)+M(3,4)*partDistri(flagPart==1,4);
        partDistriTemp(flagPart==1,4)=M(4,1)*partDistri(flagPart==1,1)+M(4,2)*partDistri(flagPart==1,2)+M(4,3)*partDistri(flagPart==1,3)+M(4,4)*partDistri(flagPart==1,4);
        
        partDistri=partDistriTemp;
        rParticle=sqrt(partDistri(:,1).^2+partDistri(:,3).^2);
        flagPart(rParticle>40)=0;
        
    elseif Para(1)==11
        covPara=cov(partDistri(flagPart==1,[1,3]));
        VSPartRec(nVSPartRec,:)=[mean(partDistri(flagPart==1,1)),mean(partDistri(flagPart==1,3)),sqrt(covPara(1)),sqrt(covPara(4)),covPara(2)/(sqrt(covPara(1))*sqrt(covPara(4)))];
        FCPartRec(nFCPartRec)=length(find(flagPart==1));
        nVSPartRec=nVSPartRec+1;
        nFCPartRec=nFCPartRec+1;
    elseif Para(1)==12
        covPara=cov(partDistri(flagPart==1,[1,3]));
        VSPartRec(nVSPartRec,:)=[mean(partDistri(flagPart==1,1)),mean(partDistri(flagPart==1,3)),sqrt(covPara(1)),sqrt(covPara(4)),covPara(2)/(sqrt(covPara(1))*sqrt(covPara(4)))];
        nVSPartRec=nVSPartRec+1;
    end
    
    
end

obj1_effi=0.3*(FCPartRec(2)/FCPartRec(1))+0.2*(FCPartRec(3)/FCPartRec(2))+0.5*(FCPartRec(3)/FCPartRec(1));
obj2_cent=sum(VSPartRec(:,1).^2+VSPartRec(:,2).^2);
obj3_size=sum(VSPartRec(:,3).^2+VSPartRec(:,4).^2);
obj4_coef=sum(abs(VSPartRec(:,5)));









