clear;
clc;
close all;


%   Author : Jiang Peiyong
%   Email£º  jiangpeiyong@impcas.ac.cn

%   Objective£º Reconstruction of a beam VS pictrue.
%   Basic thoughts:
%        - Generate a picture.            GenPic Function
%        - Reconstruct the picture.       CamReconstruction  Function 
%   xxpPic means: the origin picture
%   xxpCam means:  the cameral picture about the xxpPic from a VS 

% The code is open and free. But if you use or change it, you should let
% the author know: Courtesy.




[xxpPic,xxpCam]=GenPic(2,3e5,[200,300]);

xxpCamReconstruction=CamReconstruction(xxpCam);

xxpRes=(xxpCamReconstruction-xxpPic)./xxpPic;


figure(1)
contour(xxpPic,40)

figure(2)
contour(xxpCam,40)

figure(5)
contour(xxpCamReconstruction,40)

figure(6)
contour(xxpRes,40)
figure(61)
mesh(xxpRes)




figure(10)
subplot(1,3,1)
mesh(xxpPic)
view(90,0)
subplot(1,3,2)
mesh(xxpCamReconstruction)
view(90,0)
subplot(1,3,3)
mesh(xxpCam)
view(90,0)


