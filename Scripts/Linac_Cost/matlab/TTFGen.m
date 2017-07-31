function [betaC,TTF]=TTFGen(N,energyInMeV,energyOutMeV,betaOpt)
betaCEnds=Energy2Beta([energyInMeV,energyOutMeV]);
betaC=linspace(betaCEnds(1),betaCEnds(2),1000);
TTF=TTFOptGen(N,betaC,betaOpt);