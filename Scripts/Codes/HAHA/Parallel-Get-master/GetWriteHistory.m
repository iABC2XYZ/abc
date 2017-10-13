function GetWriteHistory(idCodes)
fidFlagCodes=fopen('idCodesFlag.txt','w');
for i=1:length(idCodes)
    clear dataCode;
    try
    titleCode=idCodes(i,:);
    dataCode=get_hist_data(titleCode,'d');
    
    fidDate =fopen([titleCode,'.date.txt'],'w');
    fidOpen =fopen([titleCode,'.open.txt'],'w');
    fidHigh =fopen([titleCode,'.high.txt'],'w');
    fidClose =fopen([titleCode,'.close.txt'],'w');
    fidLow =fopen([titleCode,'.low.txt'],'w');
    fidVolume =fopen([titleCode,'.volume.txt'],'w');
    fidPricechange =fopen([titleCode,'.pricechange.txt'],'w');
    for j=1:height(dataCode)
        fprintf(fidDate,'%s\n',cell2mat(dataCode.date(j,:)));
        fprintf(fidOpen,'%s\n',cell2mat(dataCode.open(j,:)));
        fprintf(fidHigh,'%s\n',cell2mat(dataCode.high(j,:)));
        fprintf(fidClose,'%s\n',cell2mat(dataCode.close(j,:)));
        fprintf(fidLow,'%s\n',cell2mat(dataCode.low(j,:)));
        fprintf(fidVolume,'%s\n',cell2mat(dataCode.volume(j,:)));
        fprintf(fidPricechange,'%s\n',cell2mat(dataCode.price_change(j,:)));
    end
    fclose(fidDate);
    fclose(fidOpen);
    fclose(fidHigh);
    fclose(fidClose);
    fclose(fidLow);
    fclose(fidVolume);
    fclose(fidPricechange);
    
    fprintf(fidFlagCodes,'%d\n',1);
    catch
        fprintf(fidFlagCodes,'%d\n',0);
    end
end
    fclose(fidFlagCodes);
    
    
    
    
    
    
    