clear
clc;
close all;

nameF='TestSet_Rec.dat';

rec=importdata(nameF);

[mRec,nrec]=size(rec)


rec=rec(1:end-1,:)


for i = 15:24
    figure(i)
    plot(rec(:,i),'.')

end



for i = 15:25
    E=rec(:,i);
    Emean=mean(E);
    Estd=std(E);
    flagE=(E<Emean-3*Estd);
    rec(flagE,:)=[];
    
    E=rec(:,i);
    Emean=mean(E);
    Estd=std(E);
    flagE=(E>Emean+3*Estd);
    rec(flagE,:)=[];
end

close all
for i = 15:24
    figure(i+100)
    plot(rec(:,i),'.')

end

for i = 1:25
    figure(i+200)
    hist(rec(:,i),1000)
end


fid=fopen('testRec.dat','w+');
for i =1:length(rec)
    fprintf(fid,'%s ',[num2str(rec(i,:)),char(10)]);
end
fclose(fid);






