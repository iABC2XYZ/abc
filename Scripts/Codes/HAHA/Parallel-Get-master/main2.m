clear;
clc;
close all;

flagUpdate=0;
idCodes=GetCodes(flagUpdate);  

GetWriteHistoryUpdate(flagUpdate,idCodes);

% tic
% [dateCode,openCode,highCode,closeCode,lowCode,volumeCode,pricechangeCode]=ReadHistoryData(idCodes(2,:));
% toc

% openCode=ReadOpenCode(idCodes(2,:));
% 
% 
% zOpenCode=(1:length(openCode))';
% funFit = @(x,xdata)(x(1)*xdata+x(2)+sin(x(3)*xdata+x(4)));
% x0=[0,0,0,0];
% x = lsqcurvefit(funFit,x0,zOpenCode,openCode)
% 
% figure(11)
% hold on;
% plot(zOpenCode,openCode,'k');
% plot(zOpenCode,funFit(x,zOpenCode),'r');

% 
% zOpenCode=(1:length(openCode))';
% funFit = @(x,xdata)(x(4)+x(3)*sin(x(1)*xdata+x(2)));
% x0=[0,1,1,1];
% x = lsqcurvefit(funFit,x0,zOpenCode,openCode)
% 
% 
% figure(11)
% clf;
% hold on;
% plot(zOpenCode,openCode,'k');
% plot(zOpenCode,funFit(x,zOpenCode),'r');
% 

openCode=ReadOpenCode(idCodes(178,:));
zOpenCode=(1:length(openCode))';
P=polyfit(zOpenCode,openCode,10)
close(figure(12))
figure(12)
clf;
hold on;
plot(zOpenCode,openCode,'k');
plot(zOpenCode,polyval(P,zOpenCode),'r');


fid=fopen('idCodesChoose.txt','w');
for iidCodes=1:max(length(idCodes),3)
    iidCodes
    
    clear openCode;
    openCode=ReadOpenCode(idCodes(iidCodes,:));
    if length(openCode)<30
        continue;
    end
    meanOpenCode=mean(openCode);
    stadOpenCode=std(openCode);
    nowOpenCode=openCode(end);
    if nowOpenCode<meanOpenCode
        continue;
    end
    
    fprintf(fid,'%s\n',idCodes(iidCodes,:));
    
    figure(100)
    clf;
    plot(openCode)
    title([num2str(iidCodes),'  ',idCodes(iidCodes,:)]);
    saveas(figure(100),[idCodes(iidCodes,:),'.jpg']);
    pause(0.2)

end
fclose(fid);



% 
% 
% figure(1)
% clf;
% hold on;
% plot(openCode,'b.')
% plot(closeCode,'k.')
% plot(pricechangeCode,'r.')
% 
% 
% figure(2)
% clf;
% hold on;
% plot(highCode,'b.')
% plot(lowCode,'k.')
% plot(pricechangeCode,'r.')
% 
% 
% 
% figure(3)
% clf;
% plot(pricechangeCode,'r.')
% 
% pricechangeCodeInt=pricechangeCode;
% for i=2:length(pricechangeCodeInt)
%     pricechangeCodeInt(i)=pricechangeCodeInt(i-1)+pricechangeCode(i);
% end
% 
% figure(4)
% clf;
% plot(pricechangeCodeInt,'r.')
% 

