function smoothHist=SmoothHist(matHist,nIter)
%   Author : Jiang Peiyong
%   Email£º  jiangpeiyong@impcas.ac.cn

%   Objective£º smoothness to get a smooth VS picture, so that the center of
%   the picture would be saturated.

% The code is open and free. But if you use or change it, you should let
% the author know: Courtesy.


[mMatHist,nMatHist]=size(matHist);
smoothHist=matHist;

iIter=0;
while iIter<nIter
    iIter=iIter+1;
    
    for i=1:mMatHist
        smoothHist(i,:)=smooth(smoothHist(i,:),round(nMatHist/10));
    end
    for j=1:nMatHist
        smoothHist(:,j)=smooth(smoothHist(:,j),round(nMatHist/10));
    end
    
end



