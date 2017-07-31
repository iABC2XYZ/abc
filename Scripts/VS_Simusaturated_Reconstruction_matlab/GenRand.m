function xxpPart=GenRand(numPart)

%   Author : Jiang Peiyong
%   Email£º  jiangpeiyong@impcas.ac.cn

%   Objective£º Generator a GS.

% The code is open and free. But if you use or change it, you should let
% the author know: Courtesy.


alphaT=rand()*sign(rand()-0.5);

maxBetaT=1+alphaT^2;

betaT=rand()*maxBetaT;
gammaT=(1+alphaT^2)/betaT;


xxpPart=mvnrnd(rand(1,2).*[betaT,gammaT].*sign(rand(1,2)-0.5),[betaT,-alphaT;-alphaT,gammaT],numPart);












