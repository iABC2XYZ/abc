function TTF=TTFOdd(N,betaC,betaG)
if betaC==betaG
    TTF=pi/4;
else
    TTF=(betaC./betaG).^2.*cos(pi*N./(2*betaC./betaG))*(-1)^((N-1)/2)./(N.*((betaC./betaG).^2-1));
TTF(betaC==betaG)=pi/4;
end

