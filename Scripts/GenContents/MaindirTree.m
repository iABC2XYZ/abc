clear
clc;
close all;
fileName='G:\����鵵';

fid =fopen('˵��.txt','w');

F1=GetList(fileName);

% idFolder=CheckFolder(fileName,F1)
%
%
% subFileName=GetSubName(fileName,F1,1)

[mF1,nF1]=size(F1);
for iF1=1:mF1
    
    s1FileName=fileName;
    idFolder=CheckFolder(s1FileName,F1);
    fprintf(fid,'%s\n',[F1(iF1,:)]);
    if any(idFolder==iF1)
        s2FileName=GetSubName(s1FileName,F1,iF1);
        F2=GetList(s2FileName);
        [mF2,nF2]=size(F2);
        for iF2=1:mF2
            i2dFolder=CheckFolder(s2FileName,F2);
            fprintf(fid,'%s\n',['    ',F2(iF2,:)]); 
            if F1(iF1,1:4)=='��ҵ����'
                continue;
            end
            if F1(iF1,1:4)=='���ɳ���'
                continue;
            end
            if F1(iF1,1:6)=='������������'
                s3FileName=GetSubName(s2FileName(1:end-1),F2,iF2);
                F3=GetList(s3FileName);
                [mF3,nF3]=size(F3);
                for iF3 =1:mF3
                    fprintf(fid,'%s\n',['        ',F3(iF3,:)]); 
                end
            end
            
        end
        
    end
end




fclose(fid);