function [xxpPic,xxpCam]=GenPic(numGS,numPart,sizePic,cutRatio)

%   Author : Jiang Peiyong
%   Email£º  jiangpeiyong@impcas.ac.cn

%   Objective£º Generate particles 
%                default: 2 GS add together.

% The code is open and free. But if you use or change it, you should let
% the author know: Courtesy.



if (nargin==3)
    cutRatio=0.7;
end
if (nargin==2)
    sizePic=[300,300];
    cutRatio=0.7;
end
if (nargin==1)
    numPart=3e5;
    sizePic=[300,300];
    cutRatio=0.7;
end
if (nargin==0)
    numGS=2;
    numPart=[2e5,3e5];
    sizePic=[300,300];
    cutRatio=0.7;
end


xxp = GenPart(numGS,numPart);

xxpHist=hist3(xxp,sizePic);

xxpPic=SmoothHist(xxpHist,2);

xxpPic=xxpPic/(max(max(xxpPic)));

xxpCam=xxpPic/cutRatio;
xxpCam(xxpCam>1)=1;
