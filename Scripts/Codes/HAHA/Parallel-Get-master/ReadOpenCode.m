function openCode=ReadOpenCode(indexCode)
try
    openCode=flip(importdata([indexCode,'.open.txt']));
catch
    openCode=0;
end
