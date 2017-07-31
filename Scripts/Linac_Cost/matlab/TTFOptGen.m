function TTF=TTFOptGen(N,betaC,betaOpt)

betaGGroupStart=betaOpt*0.5;
betaGGroupEnd=betaOpt;

betaOptRealRec=1;

while 1
    betaGGroup=linspace(betaGGroupStart,betaGGroupEnd,20);
    betaOptGroup=zeros(size(betaGGroup));
    betaCNew=linspace(betaGGroup(1),min(betaOpt*1.1,1),1000);
    
    n=1;
    for betaG=betaGGroup
        betaOptGroup(n)=TTFGeometryGenBetaOpt(N,betaCNew,betaG);
        n=n+1;
    end
    idBetaG=find(betaOptGroup<betaOpt,1,'last');
    
    
    betaGchosen=interp1(betaOptGroup,betaGGroup,betaOpt,'linear');
    [TTF,betaOptReal]=TTFGeometryGen(N,betaC,betaGchosen);
    if betaOptReal==betaOptRealRec
        break
    end
    betaOptRealRec=betaOptReal;

    betaGGroupStart=betaGGroup(idBetaG);
    betaGGroupEnd=betaGGroup(idBetaG+1);

end







