function xxp = GenPart(numIter,numPart)

%   Author : Jiang Peiyong
%   Email£º  jiangpeiyong@impcas.ac.cn

%   Objective£º Generate particles with numIter times.
%              if numPart is a value, then there are numPart particles
%              every time. But if numPart is a vector, then there are
%              numPart(i) particles every time.

% The code is open and free. But if you use or change it, you should let
% the author know: Courtesy.


    if length(numPart)==1
        xxp=zeros(numIter*numPart,2);
    else
        xxp=zeros(sum(numPart),2);
    end

    iParticle=1;
    
for iIter=1:numIter
    if length(numPart)==1
        numParticle=numPart;
    else
        numParticle=numPart(iIter);
    end
    
    xxp(iParticle:iParticle-1+numParticle,:)=GenRand(numParticle);
    iParticle=iParticle+numParticle;
end
    
    
    