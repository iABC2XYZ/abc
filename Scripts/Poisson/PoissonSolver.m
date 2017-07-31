close all;
clc;
clear;



%% Test Data:
Npar=100000;     % ������Ŀ

%% Test XY
ParLocaRrms=2;     % �����ߴ�  �����ηֲ��İ뾶  ������  ��˹�ֲ���rms�ߴ磩

% ���ȷֲ�
ParLocaX=rand(1.5*Npar,1)*2*ParLocaRrms-ParLocaRrms;
ParLocaY=rand(1.5*Npar,1)*2*ParLocaRrms-ParLocaRrms;
ParLocaR2=ParLocaX.^2+ParLocaY.^2;
ParLocaR2_Flag=find(ParLocaR2<=ParLocaRrms^2);
ParLocaR2_Flag(Npar+1:end)=[];
ParLoca=[ParLocaX(ParLocaR2_Flag),ParLocaY(ParLocaR2_Flag)];

%��˹�ֲ�
% ParLoca=mvnrnd([0,0],[ParLocaRrms^2,0;0,ParLocaRrms^2],Npar);


% ���������
ParLoca(1,:)=[0,0];


% ������ͼ
figure(101)
plot(ParLoca(:,1),ParLoca(:,2),'.')
axis equal

% �߽�
XminSet=-10;
YminSet=-10;
XmaxSet=10;
YmaxSet=10;

% X-Y�ռ�
Symme='xy';

%% �����Ŀ    2^GridNum   Ҫ���������   ��ע�⣺ [10,10] ��ζ��1024*1024����ռ���ڴ� 1024*1024*8=8M��  ��12,12��ռ��128M. ʵ��ʹ��������Ҫ���㣩��
GridNum=[10,10];

%% ÿһ�����ӵĵ��̬�������Ƕ���̬��
Q=ones(Npar,1);


%%   %%%%%%%%%  ���»�������

%% Test DATA OVER

L_GridNum=length(GridNum);
[m_ParLoca,n_ParLoca]=size(ParLoca);


%%


Xmin=XminSet;
Ymin=YminSet;
Xmax=XmaxSet;
Ymax=YmaxSet;

Xww=Xmax-Xmin;
Yww=Ymax-Ymin;



%% Dividing meshes
Qpoints=Q;

ParLocaMin=[Xmin,Ymin];
ParLocaMax=[Xmax,Ymax];


NGrid=2.^GridNum-2;
ParLocaDiff=ParLocaMax-ParLocaMin;
dParLocaDiff=ParLocaDiff./NGrid;

%% particles weighting::::: Particle-system transform to Cloud-system.
ParLocaDIFF=ParLoca-ones(m_ParLoca,1)*ParLocaMin;
n_ParLocaDIFF=ParLocaDIFF./(ones(m_ParLoca,1)*dParLocaDiff);

FlagIgnore=sum(n_ParLocaDIFF'<0)+sum((n_ParLocaDIFF>ones(m_ParLoca,1)*NGrid)');
n_ParLocaDIFF(FlagIgnore>0,:)=1;

Mod_ParLocaDIFF=zeros(m_ParLoca,n_ParLoca,2);
mod_ParLocaDIFF=mod(n_ParLocaDIFF,1);   % corresponding to (Xn-Xi)/hx
imod_ParLocaDIFF=1-mod_ParLocaDIFF;     % corresponding to 1-(Xn-Xi)/hx
Mod_ParLocaDIFF(:,:,1)=imod_ParLocaDIFF;
Mod_ParLocaDIFF(:,:,2)=mod_ParLocaDIFF;

Qpoints(FlagIgnore>0)=0;
F_ParLocaDIFF=ceil(n_ParLocaDIFF);

Qgrids=zeros(NGrid+1);


Qweight_ij=Qpoints.*Mod_ParLocaDIFF(:,1,1).*Mod_ParLocaDIFF(:,2,1);
Qweight_i1j=Qpoints.*Mod_ParLocaDIFF(:,1,2).*Mod_ParLocaDIFF(:,2,1);
Qweight_ij1=Qpoints.*Mod_ParLocaDIFF(:,1,1).*Mod_ParLocaDIFF(:,2,2);
Qweight_i1j1=Qpoints.*Mod_ParLocaDIFF(:,1,2).*Mod_ParLocaDIFF(:,2,2);
for im_ParLoca=1:m_ParLoca
    F_ParLocaDIFF_i=F_ParLocaDIFF(im_ParLoca,1);
    F_ParLocaDIFF_j=F_ParLocaDIFF(im_ParLoca,2);
    
    F_ParLocaDIFF_i1=F_ParLocaDIFF(im_ParLoca,1)+1;
    F_ParLocaDIFF_j1=F_ParLocaDIFF(im_ParLoca,2)+1;
    
    Qgrids(F_ParLocaDIFF_i,F_ParLocaDIFF_j)=Qgrids(F_ParLocaDIFF_i,F_ParLocaDIFF_j)+Qweight_ij(im_ParLoca);
    Qgrids(F_ParLocaDIFF_i1,F_ParLocaDIFF_j)=Qgrids(F_ParLocaDIFF_i1,F_ParLocaDIFF_j)+Qweight_i1j(im_ParLoca);
    Qgrids(F_ParLocaDIFF_i,F_ParLocaDIFF_j1)=Qgrids(F_ParLocaDIFF_i,F_ParLocaDIFF_j1)+Qweight_ij1(im_ParLoca);
    Qgrids(F_ParLocaDIFF_i1,F_ParLocaDIFF_j1)=Qgrids(F_ParLocaDIFF_i1,F_ParLocaDIFF_j1)+Qweight_i1j1(im_ParLoca);
    
end

Qgrids=Qgrids/(prod(dParLocaDiff));

%% CHECK
figure;
hist3(ParLoca);
figure(40)
mesh(Qgrids);
title('ORIGIN   RHO')

NumQgrids=sum(sum(Qgrids));

disp(['Particles:  in particle-system:    ',num2str(length(ParLocaDIFF)),'  and in cloud-system:  ',num2str(sum(sum(Qgrids))),' If the two numbers are equal, the code is correct.']);
%% CHECK OVER




%% poisson solver   ::    DST

Nx=NGrid(1)+1;
Ny=NGrid(2)+1;

s1Qgrids=dst(Qgrids);
s2Qgrids=dst(s1Qgrids')';

figure(11)
mesh(s2Qgrids)
title('s2Qgrids')


fNx=1:Nx;
fNy=1:Ny;
[fNX,fNY]=ndgrid(fNx,fNy);

s2Ugrids=s2Qgrids./((pi*fNX/Xww).^2+(pi*fNY/Yww).^2);

s1Ugrids=idst(s2Ugrids')';
dstUgrids=idst(s1Ugrids);

% %% ���Ƴ���ϵ��   %%%%%%%%%%%%%%%%   ע��   %%%%%%%%%%%
% Coe=(GridNum(1)-4)*2-1;
% dstUgrids=dstUgrids*(sum(2.^(Coe:-2:Coe-2)));
% %% ���Ƴ���ϵ������

% �������ݶ� -�� �糡 Ex Ey
[XdstEgrids,YdstEgrids]=gradient(dstUgrids,dParLocaDiff(1),dParLocaDiff(2));
% Er
RdstEgrids=(XdstEgrids.^2+YdstEgrids.^2).^0.5;

%% ͨ���������ɵ�ɷֲ�
dstRHO=-2*2*del2(dstUgrids,dParLocaDiff(1),dParLocaDiff(2));
NumdstQgrids=sum(sum(dstRHO));   % �ܵ�ɷֲ�ͳ��



figure(21)
mesh(dstUgrids)
title('DST   :     Ugrids')

figure(31)
subplot(1,2,1)
mesh(XdstEgrids)
title('DST   :     Egrids X')
view(0,0)
subplot(1,2,2)
mesh(YdstEgrids)
title('DST   :     Egrids Y')
view(0,0)

figure(61)
mesh(RdstEgrids)
title('DST   :     Egrids')
view(0,0)

figure(41)
mesh(dstRHO)
title('DST    RHO')



disp([char(13), 'Particle''s number:  ',char(13),'Origin Grids:   ',num2str(NumQgrids),char(13),'DST Grids:   ',num2str(NumdstQgrids),char(13)]);


AnaEmax=sum(Qpoints)/(2*pi*ParLocaRrms);



%% 
%%  ��˹����
Rtest=0:0.05:10;
Rtest2=Rtest.^2;
Etest=zeros(size(Rtest));
ParLocaRtest2=ParLoca(:,1).^2+ParLoca(:,2).^2;
for nRtest=1:length(Rtest)
    iRtest2=Rtest2(nRtest);
    iRtest=Rtest(nRtest);
    Rtest2Flag=find(ParLocaRtest2<=iRtest2);
    Etest(nRtest)=sum(Qpoints(Rtest2Flag))/(2*pi*iRtest);
end

figure(211)
plot(Rtest,Etest)


Etest(isinf(Etest))=0;

%%  ��˹�������

% ��˹�����õ糡���ֵ
AnaEmax=max(Etest);

% DST ����糡���ֵ
CalEmax=max(max(RdstEgrids));

[AnaEmax,CalEmax,]

AnaEmax/CalEmax
