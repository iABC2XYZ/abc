function [obj1_effi,obj2_cent,obj3_size,obj4_coef,obj5_EffiAll,VSPartRec]=Fit4cjj(partDistri,inputParaValues,numParticle)
LatticeData;

inputPara=find(Lattice(:,1)==2);
try
    Lattice(inputPara,3)=inputParaValues;
catch
    Lattice(inputPara,3)=inputParaValues';
end

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
                M=Bend(Para(5),Para(6));
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
obj5_EffiAll=FCPartRec(3)/FCPartRec(1);



