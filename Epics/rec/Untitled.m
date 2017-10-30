clear;
clc;
close all;

cd 'C:\Users\A\Desktop\rec'
rec=importdata('Rec.dat');


for i = 15:24
    figure(i)
    plot(rec(:,i),'.')

end

rec(11125:11844,:)=[];

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


% save('Rec.txt','rec','-ascii')
% size(rec)

fid=fopen('Rec.txt','w+');
for i =1:length(rec)
    fprintf(fid,'%s\n',num2str(rec(i,:)));
end
fclose(fid);









