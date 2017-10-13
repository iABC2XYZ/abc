function idCodes=GetCodes(flagUpdate)

if flagUpdate==1
    
    allStocks=get_today_all;
    idCodes=cell2mat(allStocks.code);
    
    fid =fopen('idCodes.txt','w');
    for i=1:length(idCodes)
        fprintf(fid,'%s\n',idCodes(i,:));
    end
    fclose(fid);
    
else
    idCodes=char(zeros(4000,6));
    fid =fopen('idCodes.txt','r');
    nLine=1;
    while ~feof(fid)
        idCodes(nLine,:)=fgetl(fid);
        nLine=nLine+1;
    end
    idCodes(nLine:end,:)=[];
end
  