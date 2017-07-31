function energyMeV=Beta2Energy(betaC)
gammaC=1./sqrt(1-betaC.^2);
energyMeV=(gammaC-1)*938.274;

