function idF1=CheckFolder(fileName,F1)
[mF1,nF1]=size(F1);
idF1=[];
for iF1=1:mF1
    fF1=F1(iF1,:);
    subFileName=[fileName,'\',fF1];
    if exist(subFileName)==7
        idF1=[idF1,iF1];
    end
end



