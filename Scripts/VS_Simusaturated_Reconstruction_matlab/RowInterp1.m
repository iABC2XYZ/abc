function xxpCamInterp1 = RowInterp1(xxpCam)

%   Author : Jiang Peiyong
%   Email£º  jiangpeiyong@impcas.ac.cn

%   Objective£º Interplate by rows.

% The code is open and free. But if you use or change it, you should let
% the author know: Courtesy.


xxpCamFlag=xxpCam==1;
[m_xxpCam,n_xxpCam]=size(xxpCam);
xxpCamInterp1=xxpCam;
for i_xxpCam=1:m_xxpCam
    r_xxpCamFlag=xxpCamFlag(i_xxpCam,:);
    if r_xxpCamFlag==0
        continue;
    end
    x_xxpCam=find(r_xxpCamFlag<1);
    r_xxpCam=xxpCam(i_xxpCam,r_xxpCamFlag<1);
    
    rp_xxpCam=interp1(x_xxpCam,r_xxpCam,find(r_xxpCamFlag),'spline');
    xxpCamInterp1(i_xxpCam,r_xxpCamFlag)=rp_xxpCam;

end

