function F=GetList(pathFile)
nowCD=cd;
cd(pathFile)
% F1=ls;
% F1
% length(F1)
% whos F1
% 
% [m,n]=size(F1);
% 
% for iF1=3:m
%     disp(F1(iF1,:))
% end
%     

F1=ls;
F=F1(3:end,:);
cd(nowCD)
return

