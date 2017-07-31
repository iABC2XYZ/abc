function [TTF,betaOpt]=TTFGeometryGen(N,betaC,betaG)
if mod(N,2)==0
    TTF=TTFEven(N,betaC,betaG);
else
   TTF=TTFOdd(N,betaC,betaG); 
end
[maxBetaCV,maxBetaCL]=max(TTF);

betaOpt=betaC(maxBetaCL);
