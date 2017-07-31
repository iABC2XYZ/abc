function xxpCamReconstructionNorm=CamReconstruction(xxpCam)


%   Author : Jiang Peiyong
%   Email£º  jiangpeiyong@impcas.ac.cn

%   Objective£º Reconstruction 
%   Basic thoughts:
%        - interplate by rows and columms
%        - get the mean. 

% The code is open and free. But if you use or change it, you should let
% the author know: Courtesy.



xxpCamRow = RowInterp1(xxpCam);
xxpCamCol = ColInterp1(xxpCam);

xxpCamReconstruction=(xxpCamRow+xxpCamCol)/2;



xxpCamReconstructionNorm=xxpCamReconstruction/max(max(xxpCamReconstruction));

