clear;
close all;
clc;
Lattice_read=xlsread('Changjj.xlsx','Lattice4','A2:F33');
Lattice=Lattice_read;
Lattice(:,2)=Lattice_read(:,2)/1000;
Lattice(:,4)=Lattice_read(:,4)/1000;
Lattice(:,5)=Lattice_read(:,5)/1000;
Lattice(:,6)=Lattice_read(:,6)/180*pi;


%%
xMean=0;
xpMean=0;
yMean=0;
ypMean=0;

xSigma=[100,0;0,1];
ySigma=[100,0;0,1];


O=zeros(2);

allMean=[xMean,xpMean,yMean,ypMean];
allSigma=[xSigma,O;O,ySigma];



numParticle=1e5;
partDistri=mvnrnd(allMean,allSigma,numParticle);

partDistriBak=partDistri;

partDistriTemp=partDistri;

flagPart=ones(numParticle,1);

[LatticeM,LatticeN]=size(Lattice);
partDistriAll=zeros(numParticle,4,LatticeM+1);

partDistriAll(:,:,1)=partDistri;
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
        
        partDistriAll(:,:,1+iLatticeM)=partDistri;
        
        rParticle=sqrt(partDistri(:,1).^2+partDistri(:,3).^2);
        flagPart(rParticle>40)=0;
    end
end


xEmit=sqrt(det(cov(partDistriBak(flagPart==1,[1,2]))));
yEmit=sqrt(det(cov(partDistriBak(flagPart==1,[3,4]))));

xBetaFunc=zeros(LatticeM+1,1);
yBetaFunc=zeros(LatticeM+1,1);
for iLatticeM=1:LatticeM+1
    xBetaFunc(iLatticeM)=std(partDistriAll(flagPart==1,1,iLatticeM))/xEmit;
    yBetaFunc(iLatticeM)=std(partDistriAll(flagPart==1,3,iLatticeM))/yEmit;
end
figure(301)
subplot(1,2,1)
plot(xBetaFunc(xBetaFunc>0))
hold on
plot(xBetaFunc(xBetaFunc>0),'r*')
subplot(1,2,2)
plot(yBetaFunc(yBetaFunc>0))
hold on
plot(yBetaFunc(yBetaFunc>0),'r*')

Ratio=length(find(flagPart==1))/numParticle

% figure(1001)
% for iLatticeM=1:LatticeM+1
%     plot(partDistriAll(flagPart==1,1,iLatticeM),partDistriAll(flagPart==1,2,iLatticeM),'.');
%     pause(0.2)
% end


figure(1101)
for iLatticeM=1:LatticeM+1
    plot(partDistriAll(:,1,iLatticeM),partDistriAll(:,2,iLatticeM),'.');
    title(iLatticeM)
    pause(0.2);
end

