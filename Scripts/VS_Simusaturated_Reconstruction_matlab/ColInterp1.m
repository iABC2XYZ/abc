function xxpCamInterp1 = ColInterp1(xxpCam)

%   Author : Jiang Peiyong
%   Email��  jiangpeiyong@impcas.ac.cn

%   Objective�� Interplate by columns.

% The code is open and free. But if you use or change it, you should let
% the author know: Courtesy.


xxpCamCol=xxpCam';
xxpCamColInterp1=RowInterp1(xxpCamCol);
xxpCamInterp1=xxpCamColInterp1';
