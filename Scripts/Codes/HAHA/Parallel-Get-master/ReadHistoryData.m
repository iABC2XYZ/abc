function [dateCode,openCode,highCode,closeCode,lowCode,volumeCode,pricechangeCode]=ReadHistoryData(indexCode)
fid =fopen('idCodes.txt','r');
nLine=1;
while ~feof(fid)
    indexCodeRead=fgetl(fid);
    if (length(indexCodeRead)==length(indexCode)) && prod(indexCodeRead==indexCode)
        break;
    end
    nLine=nLine+1;
end
fclose(fid);

idCodesFlag=importdata('idCodesFlag.txt');
if idCodesFlag(nLine)==0
    dateCode='3000-01-01';
    openCode=0;
    highCode=0;
    closeCode=0;
    lowCode=0;
    volumeCode=0;
    pricechangeCode=0;
else
    openCode=flip(importdata([indexCode,'.open.txt']));
    highCode=flip(importdata([indexCode,'.high.txt']));
    closeCode=flip(importdata([indexCode,'.close.txt']));
    lowCode=flip(importdata([indexCode,'.low.txt']));
    volumeCode=flip(importdata([indexCode,'.volume.txt']));
    pricechangeCode=flip(importdata([indexCode,'.pricechange.txt']));
    
    [mOpenCode,nOpenCode]=size(openCode);
    dateCode=char(zeros(mOpenCode,10));
    fid=fopen([indexCode,'.date.txt'],'r');
    nLine=0;
    while ~feof(fid)
        dateCode(mOpenCode-nLine,:)=fgetl(fid);
        nLine=nLine+1;
    end
end
