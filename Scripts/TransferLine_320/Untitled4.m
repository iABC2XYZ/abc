% clear;
% clc;
% clear all;
% close;
% 
% Lattice=xlsread('Changjj.xlsx','Lattice','A2:F26');
Lattice(:,2)=Lattice(:,2)/1000;
Lattice(:,4)=Lattice(:,4)/1000;
Lattice(:,5)=Lattice(:,5)/1000;
Lattice(:,6)=Lattice(:,6)/180*pi;

[LatticeM,LatticeN]=size(Lattice);
for iLatticeM=1:LatticeM
    Para=Lattice(iLatticeM,:);
    switch Para(1)
        case 1
            M=Drift(Para(2));
        case 2
            M=Quadrupole(Para(4),Para(3));
        case 3
            M=Quadrupole(Para(5),Para(6));
    end
end
            













