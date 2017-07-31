clear
clc;
close all;
fclose('all');

STEM_FLAG=1;        %%     是否 ADD STEM              0：不加   1： 加
SIM_FLAG=1;         %%     T型板 简版还是繁版          0： 繁版  1：简版

if SIM_FLAG==0
    StruPara='StruPara.txt';
    StruVBA='StruVBA.txt';
else
    StruPara='SIM_StruPara.txt';
    StruVBA='SIM_StruVBA.txt';
end

Stru = xlsread('Struc.xlsx','TUBE');

[Ntube,Npara]=size(Stru);


CStem_1_Flag=Stru(1,21);
CStem_2_Flag=Stru(1,32);
CStem_3_Flag=Stru(1,43);
Stem_Spin_Degree_Flag=Stru(1,47:50);
Tube_Blend_Outer_Flag=Stru(1,7);

fid=fopen(StruPara,'w');


for nTube=2:Ntube
    if nTube<=10
        NumberTube=['00',num2str(nTube-1)];
    elseif nTube<=100
        NumberTube=['0',num2str(nTube-1)];
    else
        NumberTube=[num2str(nTube-1)];
    end
    
    fprintf(fid,'%s',['Tube_Z_Begin_',NumberTube,char(9),char(9),char(9),num2str(Stru(nTube,2)),char(9),char(13)]);
    fprintf(fid,'%s',['Tube_Z_End_',NumberTube,char(9),char(9),char(9),num2str(Stru(nTube,3)),char(9),char(13)]);
    fprintf(fid,'%s',['Tube_R_Inner_',NumberTube,char(9),char(9),char(9),num2str(Stru(nTube,4)),char(9),char(13)]);
    fprintf(fid,'%s',['Tube_R_Outer_',NumberTube,char(9),char(9),char(9),num2str(Stru(nTube,5)),char(9),char(13)]);
    fprintf(fid,'%s',['Tube_Blend_Inner_',NumberTube,char(9),char(9),char(9),num2str(Stru(nTube,6)),char(9),char(13)]);
    fprintf(fid,'%s',['Tube_Blend_Outer_',NumberTube,char(9),char(9),char(9),num2str(Stru(nTube,7)),char(9),char(13)]);
    fprintf(fid,'%s',['Tube_Ear_Center_Left_',NumberTube,char(9),char(9),char(9),num2str(Stru(nTube,8)),char(9),char(13)]);
    fprintf(fid,'%s',['Tube_Ear_Thick_Left_',NumberTube,char(9),char(9),char(9),num2str(Stru(nTube,9)),char(9),char(13)]);
    
    fprintf(fid,'%s',['Tube_Ear_Blend_Left_',NumberTube,char(9),char(9),char(9),num2str(Stru(nTube,10)),char(9),char(13)]);
    fprintf(fid,'%s',['Tube_Ear_Center_Right_',NumberTube,char(9),char(9),char(9),num2str(Stru(nTube,11)),char(9),char(13)]);
    fprintf(fid,'%s',['Tube_Ear_Thick_Right_',NumberTube,char(9),char(9),char(9),num2str(Stru(nTube,12)),char(9),char(13)]);
    
    fprintf(fid,'%s',['Tube_Ear_Blend_Right_',NumberTube,char(9),char(9),char(9),num2str(Stru(nTube,13)),char(9),char(13)]);
    fprintf(fid,'%s',['Stem_1_Xmin_',NumberTube,char(9),char(9),char(9),num2str(Stru(nTube,14)),char(9),char(13)]);
    fprintf(fid,'%s',['Stem_1_Xmax_',NumberTube,char(9),char(9),char(9),num2str(Stru(nTube,15)),char(9),char(13)]);
    fprintf(fid,'%s',['Stem_1_Ymin_',NumberTube,char(9),char(9),char(9),num2str(Stru(nTube,16)),char(9),char(13)]);
    fprintf(fid,'%s',['Stem_1_Ymax_',NumberTube,char(9),char(9),char(9),num2str(Stru(nTube,17)),char(9),char(13)]);
    fprintf(fid,'%s',['Stem_1_Zmin_',NumberTube,char(9),char(9),char(9),num2str(Stru(nTube,18)),char(9),char(13)]);
    fprintf(fid,'%s',['Stem_1_Zmax_',NumberTube,char(9),char(9),char(9),num2str(Stru(nTube,19)),char(9),char(13)]);
    fprintf(fid,'%s',['Stem_1_Blend_',NumberTube,char(9),char(9),char(9),num2str(Stru(nTube,20)),char(9),char(13)]);
    fprintf(fid,'%s',['Stem_1_Cylinder_Center_',NumberTube,char(9),char(9),char(9),num2str(Stru(nTube,21)),char(9),char(13)]);
    fprintf(fid,'%s',['Stem_1_Cylinder_Radius_',NumberTube,char(9),char(9),char(9),num2str(Stru(nTube,22)),char(9),char(13)]);
    fprintf(fid,'%s',['Stem_1_Cylinder_Ymin_',NumberTube,char(9),char(9),char(9),num2str(Stru(nTube,23)),char(9),char(13)]);
    fprintf(fid,'%s',['Stem_1_Cylinder_Ymax_',NumberTube,char(9),char(9),char(9),num2str(Stru(nTube,24)),char(9),char(13)]);
    fprintf(fid,'%s',['Stem_2_Xmin_',NumberTube,char(9),char(9),char(9),num2str(Stru(nTube,25)),char(9),char(13)]);
    fprintf(fid,'%s',['Stem_2_Xmax_',NumberTube,char(9),char(9),char(9),num2str(Stru(nTube,26)),char(9),char(13)]);
    fprintf(fid,'%s',['Stem_2_Ymin_',NumberTube,char(9),char(9),char(9),num2str(Stru(nTube,27)),char(9),char(13)]);
    fprintf(fid,'%s',['Stem_2_Ymax_',NumberTube,char(9),char(9),char(9),num2str(Stru(nTube,28)),char(9),char(13)]);
    fprintf(fid,'%s',['Stem_2_Zmin_',NumberTube,char(9),char(9),char(9),num2str(Stru(nTube,29)),char(9),char(13)]);
    fprintf(fid,'%s',['Stem_2_Zmax_',NumberTube,char(9),char(9),char(9),num2str(Stru(nTube,30)),char(9),char(13)]);
    fprintf(fid,'%s',['Stem_2_Blend_',NumberTube,char(9),char(9),char(9),num2str(Stru(nTube,31)),char(9),char(13)]);
    fprintf(fid,'%s',['Stem_2_Cylinder_Center_',NumberTube,char(9),char(9),char(9),num2str(Stru(nTube,32)),char(9),char(13)]);
    fprintf(fid,'%s',['Stem_2_Cylinder_Radius_',NumberTube,char(9),char(9),char(9),num2str(Stru(nTube,33)),char(9),char(13)]);
    fprintf(fid,'%s',['Stem_2_Cylinder_Ymin_',NumberTube,char(9),char(9),char(9),num2str(Stru(nTube,34)),char(9),char(13)]);
    fprintf(fid,'%s',['Stem_2_Cylinder_Ymax_',NumberTube,char(9),char(9),char(9),num2str(Stru(nTube,35)),char(9),char(13)]);
    fprintf(fid,'%s',['Stem_3_Xmin_',NumberTube,char(9),char(9),char(9),num2str(Stru(nTube,36)),char(9),char(13)]);
    fprintf(fid,'%s',['Stem_3_Xmax_',NumberTube,char(9),char(9),char(9),num2str(Stru(nTube,37)),char(9),char(13)]);
    fprintf(fid,'%s',['Stem_3_Ymin_',NumberTube,char(9),char(9),char(9),num2str(Stru(nTube,38)),char(9),char(13)]);
    fprintf(fid,'%s',['Stem_3_Ymax_',NumberTube,char(9),char(9),char(9),num2str(Stru(nTube,39)),char(9),char(13)]);
    fprintf(fid,'%s',['Stem_3_Zmin_',NumberTube,char(9),char(9),char(9),num2str(Stru(nTube,40)),char(9),char(13)]);
    fprintf(fid,'%s',['Stem_3_Zmax_',NumberTube,char(9),char(9),char(9),num2str(Stru(nTube,41)),char(9),char(13)]);
    fprintf(fid,'%s',['Stem_3_Blend_',NumberTube,char(9),char(9),char(9),num2str(Stru(nTube,42)),char(9),char(13)]);
    fprintf(fid,'%s',['Stem_3_Cylinder_Center_',NumberTube,char(9),char(9),char(9),num2str(Stru(nTube,43)),char(9),char(13)]);
    fprintf(fid,'%s',['Stem_3_Cylinder_Radius_',NumberTube,char(9),char(9),char(9),num2str(Stru(nTube,44)),char(9),char(13)]);
    fprintf(fid,'%s',['Stem_3_Cylinder_Ymin_',NumberTube,char(9),char(9),char(9),num2str(Stru(nTube,45)),char(9),char(13)]);
    fprintf(fid,'%s',['Stem_3_Cylinder_Ymax_',NumberTube,char(9),char(9),char(9),num2str(Stru(nTube,46)),char(9),char(13)]);
    
    %%
    fprintf(fid,'%s',['Stem_Spin_Degree_1_',NumberTube,char(9),char(9),char(9),num2str(Stru(nTube,47)),char(9),char(13)]);
    fprintf(fid,'%s',['Stem_Spin_Degree_2_',NumberTube,char(9),char(9),char(9),num2str(Stru(nTube,48)),char(9),char(13)]);
    fprintf(fid,'%s',['Stem_Spin_Degree_3_',NumberTube,char(9),char(9),char(9),num2str(Stru(nTube,49)),char(9),char(13)]);
    fprintf(fid,'%s',['Stem_Spin_Degree_4_',NumberTube,char(9),char(9),char(9),num2str(Stru(nTube,50)),char(9),char(13)]);
end

fclose(fid);

% if Stru(1,9)==1 | Stru(1,11)==1
%     Stru(1,7)=1;
% end
% if Stru(1,19)==0 | Stru(1,20)==0 | Stru(1,21)==0
%     Stru(1,19:21)=0;
% else
%     Stru(1,12:18)=0;
% end
%
% if Stru(1,29)==0 | Stru(1,30)==0 | Stru(1,31)==0
%     Stru(1,29:31)=0;
% else
%     Stru(1,22:28)=0;
% end
%
% if Stru(1,39)==0 | Stru(1,40)==0 | Stru(1,41)==0
%     Stru(1,39:41)=0;
% else
%     Stru(1,32:38)=0;
% end




Fid=fopen(StruVBA,'w');
%%  FPRINT_HEAD;
L_1=['''CST History Data Exchange Format V1 ',char(10)];
L_2=[' ',char(10)];
L_3=['''@ define units ',char(10)];
L_4=[' ',char(10)];
L_5=['''[VERSION]2012.0|22.0.0|20120124[/VERSION] ',char(10)];
L_6=['With Units  ',char(10)];
L_7=['     .Geometry "mm"  ',char(10)];
L_8=['     .Frequency "MHz"  ',char(10)];
L_9=['     .Time "s"  ',char(10)];
L_10=['     .TemperatureUnit "Kelvin"  ',char(10)];
L_11=['     .Voltage "V"  ',char(10)];
L_12=['     .Current "A"  ',char(10)];
L_13=['     .Resistance "Ohm"  ',char(10)];
L_14=['     .Conductance "Siemens"  ',char(10)];
L_15=['     .Capacitance "PikoF"  ',char(10)];
L_16=['     .Inductance "NanoH"  ',char(10)];
L_17=['End With ',char(10)];
L_18=[' ',char(10)];
L_19=['''@ define background ',char(10)];
L_20=[' ',char(10)];
L_21=['''[VERSION]2012.0|22.0.0|20120124[/VERSION] ',char(10)];
L_22=[' ',char(10)];
L_23=[' ',char(10)];
L_24=['''@ use template: Resonator ',char(10)];
L_25=[' ',char(10)];
L_26=['''[VERSION]2009.5|18.0.3|20090230[/VERSION] ',char(10)];
L_27=[''' Template for Resonator ',char(10)];
L_28=[''' ============================== ',char(10)];
L_29=[''' (CSTxMWSxONLY) ',char(10)];
L_30=[''' set units to mm, ghz ',char(10)];
L_31=['With Units  ',char(10)];
L_32=['     .Geometry "mm"  ',char(10)];
L_33=['     .Frequency "ghz"  ',char(10)];
L_34=['     .Time "ns"  ',char(10)];
L_35=['End With  ',char(10)];
L_36=[''' set background material to pec ',char(10)];
L_37=['With Background  ',char(10)];
L_38=['     .Type "pec"  ',char(10)];
L_39=['     .XminSpace "0.0"  ',char(10)];
L_40=['     .XmaxSpace "0.0"  ',char(10)];
L_41=['     .YminSpace "0.0"  ',char(10)];
L_42=['     .YmaxSpace "0.0"  ',char(10)];
L_43=['     .ZminSpace "0.0"  ',char(10)];
L_44=['     .ZmaxSpace "0.0"  ',char(10)];
L_45=['End With  ',char(10)];
L_46=[''' set boundary conditions to electric ',char(10)];
L_47=['With Boundary ',char(10)];
L_48=['     .Xmin "electric"  ',char(10)];
L_49=['     .Xmax "electric"  ',char(10)];
L_50=['     .Ymin "electric"  ',char(10)];
L_51=['     .Ymax "electric"  ',char(10)];
L_52=['    .Zmin "electric"  ',char(10)];
L_53=['    .Zmax "electric"  ',char(10)];
L_54=['     .Xsymmetry "none"  ',char(10)];
L_55=['     .Ysymmetry "none"  ',char(10)];
L_56=['     .Zsymmetry "none"  ',char(10)];
L_57=['End With ',char(10)];
L_58=['Mesh.MeshType "PBA" ',char(10)];
L_59=[' ',char(10)];
L_60=['''@ set workplane properties ',char(10)];
L_61=[' ',char(10)];
L_62=['''[VERSION]2009.5|18.0.3|20090230[/VERSION] ',char(10)];
L_63=['With WCS ',char(10)];
L_64=['     .SetWorkplaneSize "1200"  ',char(10)];
L_65=['     .SetWorkplaneRaster "1"  ',char(10)];
L_66=['     .SetWorkplaneSnap "TRUE"  ',char(10)];
L_67=['     .SetWorkplaneSnapRaster "0.1"  ',char(10)];
L_68=['     .SetWorkplaneAutoadjust "TRUE"  ',char(10)];
L_69=['End With ',char(10)];
L_70=[' ',char(10)];
L_71=['''@ define units ',char(10)];
L_72=[' ',char(10)];
L_73=['''[VERSION]2009.5|18.0.3|20090230[/VERSION] ',char(10)];
L_74=['With Units  ',char(10)];
L_75=['     .Geometry "mm"  ',char(10)];
L_76=['     .Frequency "MHz"  ',char(10)];
L_77=['     .Time "ns"  ',char(10)];
L_78=['     .TemperatureUnit "Kelvin"  ',char(10)];
L_79=['     .Voltage "V"  ',char(10)];
L_80=['     .Current "A"  ',char(10)];
L_81=['     .Resistance "Ohm"  ',char(10)];
L_82=['     .Conductance "S"  ',char(10)];
L_83=['     .Capacitance "pF"  ',char(10)];
L_84=['     .Inductance "nH"  ',char(10)];
L_85=['End With ',char(10)];
L_86=[' ',char(10)];
L_87=['''@ define frequency range ',char(10)];
L_88=[' ',char(10)];
L_89=['''[VERSION]2009.5|18.0.3|20090230[/VERSION] ',char(10)];
L_90=['Solver.FrequencyRange "44", "60" ',char(10)];
L_91=[' ',char(10)];
L_92=['''@ define background ',char(10)];
L_93=[' ',char(10)];
L_94=['''[VERSION]2010.0|20.0.0|20091127[/VERSION] ',char(10)];
L_95=['With Background  ',char(10)];
L_96=['     .Reset  ',char(10)];
L_97=['     .Type "Pec"  ',char(10)];
L_98=['     .Epsilon "1.0"  ',char(10)];
L_99=['     .Mue "1.0"  ',char(10)];
L_100=['     .ElConductivity "0.0"  ',char(10)];
L_101=['     .ThermalType "Normal"  ',char(10)];
L_102=['     .ThermalConductivity "0.0"  ',char(10)];
L_103=['     .HeatCapacity "0.0"  ',char(10)];
L_104=['     .Rho "0.0"  ',char(10)];
L_105=['     .XminSpace "0.0"  ',char(10)];
L_106=['     .XmaxSpace "0.0"  ',char(10)];
L_107=['     .YminSpace "0.0"  ',char(10)];
L_108=['     .YmaxSpace "0.0"  ',char(10)];
L_109=['     .ZminSpace "0.0"  ',char(10)];
L_110=['     .ZmaxSpace "0.0"  ',char(10)];
L_111=['     .ApplyInAllDirections "False"  ',char(10)];
L_112=['End With ',char(10)];
L_113=[' ',char(10)];
L_114=['''@ define material: Copper (hard-drawn) ',char(10)];
L_115=[' ',char(10)];
L_116=['''[VERSION]2010.0|20.0.0|20091127[/VERSION] ',char(10)];
L_117=['With Material ',char(10)];
L_118=['     .Reset ',char(10)];
L_119=['     .Name "Copper (hard-drawn)" ',char(10)];
L_120=['     .FrqType "all"  ',char(10)];
L_121=['     .Type "Lossy metal"  ',char(10)];
L_122=['     .SetMaterialUnit "GHz", "mm"  ',char(10)];
L_123=['     .Mue "1.0"  ',char(10)];
L_124=['     .Kappa "5.96e+007"  ',char(10)];
L_125=['     .Rho "8930.0"  ',char(10)];
L_126=['     .ThermalType "Normal"  ',char(10)];
L_127=['     .ThermalConductivity "401.0"  ',char(10)];
L_128=['     .HeatCapacity "0"  ',char(10)];
L_129=['     .MetabolicRate "0"  ',char(10)];
L_130=['     .BloodFlow "0"  ',char(10)];
L_131=['     .VoxelConvection "0"  ',char(10)];
L_132=['     .MechanicsType "Isotropic"  ',char(10)];
L_133=['     .YoungsModulus "120"  ',char(10)];
L_134=['     .PoissonsRatio "0.33"  ',char(10)];
L_135=['     .ThermalExpansionRate "17"  ',char(10)];
L_136=['     .FrqType "static"  ',char(10)];
L_137=['     .Type "Normal"  ',char(10)];
L_138=['     .SetMaterialUnit "Hz", "mm"  ',char(10)];
L_139=['     .Epsilon "1"  ',char(10)];
L_140=['     .Mue "1.0"  ',char(10)];
L_141=['     .Kappa "5.96e+007"  ',char(10)];
L_142=['     .TanD "0.0"  ',char(10)];
L_143=['     .TanDFreq "0.0"  ',char(10)];
L_144=['     .TanDGiven "False"  ',char(10)];
L_145=['     .TanDModel "ConstTanD"  ',char(10)];
L_146=['     .KappaM "0"  ',char(10)];
L_147=['     .TanDM "0.0"  ',char(10)];
L_148=['     .TanDMFreq "0.0"  ',char(10)];
L_149=['     .TanDMGiven "False"  ',char(10)];
L_150=['     .TanDMModel "ConstTanD"  ',char(10)];
L_151=['     .DispModelEps "None"  ',char(10)];
L_152=['     .DispModelMue "None"  ',char(10)];
L_153=['     .DispersiveFittingSchemeEps "1st Order"  ',char(10)];
L_154=['     .DispersiveFittingSchemeMue "1st Order"  ',char(10)];
L_155=['     .UseGeneralDispersionEps "False"  ',char(10)];
L_156=['     .UseGeneralDispersionMue "False"  ',char(10)];
L_157=['     .Colour "1", "1", "0"  ',char(10)];
L_158=['     .Wireframe "False"  ',char(10)];
L_159=['     .Reflection "False"  ',char(10)];
L_160=['     .Allowoutline "True"  ',char(10)];
L_161=['     .Transparentoutline "False"  ',char(10)];
L_162=['     .Transparency "0"  ',char(10)];
L_163=['     .Create ',char(10)];
L_164=['End With ',char(10)];
L_165=[' ',char(10)];
L_166=['''@ new component: component1 ',char(10)];
L_167=[' ',char(10)];
L_168=['''[VERSION]2012.0|22.0.0|20120124[/VERSION] ',char(10)];
L_169=['Component.New "component1" ',char(10)];
L_170=[' ',char(10)];

for i_L=1:170
    NameL=['L_',num2str(i_L)];
    fprintf(Fid,'%s',eval(NameL));
end



%% Tube
for nTube=1:Ntube-1
    if nTube<=9
        NumberTube=['00',num2str(nTube)];
    elseif nTube<=99
        NumberTube=['0',num2str(nTube)];
    else
        NumberTube=[num2str(nTube)];
    end
    T_1=['With Cylinder  ',char(10)];
    T_2=['     .Reset   ',char(10)];
    T_3=['     .Name "Tube_',NumberTube,'"   ',char(10)];
    T_4=['     .Component "component1"   ',char(10)];
    T_5=['     .Material "Copper (hard-drawn)"   ',char(10)];
    T_6=['     .OuterRadius "Tube_R_Outer_',NumberTube,'"   ',char(10)];
    T_7=['     .InnerRadius "Tube_R_Inner_',NumberTube,'"   ',char(10)];
    T_8=['     .Axis "z"   ',char(10)];
    T_9=['     .Zrange "Tube_Z_Begin_',NumberTube,'", "Tube_Z_End_',NumberTube,'"   ',char(10)];
    T_10=['     .Xcenter "0"   ',char(10)];
    T_11=['     .Ycenter "0"   ',char(10)];
    T_12=['     .Segments "0"   ',char(10)];
    T_13=['     .Create   ',char(10)];
    T_14=['End With   ',char(10)];
    
    if nTube==1
        T_15=char(10);
    else
        T_15=['Pick.PickEdgeFromId "component1:Tube_',NumberTube,'", "2", "2"  ',char(10)];
    end
    if nTube==Ntube-1
        T_16=char(10);
    else
        T_16=['Pick.PickEdgeFromId "component1:Tube_',NumberTube,'", "4", "4"  ',char(10)];
    end
    T_17=['Solid.BlendEdge "Tube_Blend_Inner_',NumberTube,'"  ',char(10)];
    
    if Tube_Blend_Outer_Flag==1
        if nTube==1
            T_18=char(10);
        else
            T_18=['Pick.PickEdgeFromId "component1:Tube_',NumberTube,'", "1", "1"  ',char(10)];
        end
        if nTube==Ntube-1
            T_19=char(10);
        else
            T_19=['Pick.PickEdgeFromId "component1:Tube_',NumberTube,'", "3", "3"  ',char(10)];
        end
        T_20=['Solid.BlendEdge "Tube_Blend_Outer_',NumberTube,'"  ',char(10)];
    end
    
    
    
    
    
    if Tube_Blend_Outer_Flag==1
        for i_T=1:20
            NameT=['T_',num2str(i_T)];
            fprintf(Fid,'%s',eval(NameT));
        end
    else
        
        for i_T=1:17
            NameT=['T_',num2str(i_T)];
            fprintf(Fid,'%s',eval(NameT));
        end
    end
end


%%  LEFT EAR

if  Tube_Blend_Outer_Flag~=1
    for nTube=2:Ntube-1
        if nTube<=9
            NumberTube=['00',num2str(nTube)];
        elseif nTube<=99
            NumberTube=['0',num2str(nTube)];
        else
            NumberTube=[num2str(nTube)];
        end
        EL_1=['With Cylinder  ',char(10)];
        EL_2=['     .Reset   ',char(10)];
        EL_3=['     .Name "EarLeft_',NumberTube,'"   ',char(10)];
        EL_4=['     .Component "component1"   ',char(10)];
        EL_5=['     .Material "Copper (hard-drawn)"   ',char(10)];
        EL_6=['     .OuterRadius "Tube_R_Outer_',NumberTube,'+abs(Tube_Ear_Center_Left_',NumberTube,')"   ',char(10)];
        EL_7=['     .InnerRadius "Tube_R_Inner_',NumberTube,'+abs(Tube_Ear_Center_Left_',NumberTube,')"   ',char(10)];
        EL_8=['     .Axis "z"   ',char(10)];
        EL_9=['     .Zrange "Tube_Z_Begin_',NumberTube,'", "Tube_Z_Begin_',NumberTube,'+Tube_Ear_Thick_Left_',NumberTube,'"   ',char(10)];
        EL_10=['     .Xcenter "0"   ',char(10)];
        EL_11=['     .Ycenter "Tube_Ear_Center_Left_',NumberTube,'"   ',char(10)];
        EL_12=['     .Segments "0"   ',char(10)];
        EL_13=['     .Create   ',char(10)];
        EL_14=['End With   ',char(10)];
        
        
        
        EL_15=['Pick.PickEdgeFromId "component1:EarLeft_',NumberTube,'", "1", "1"  ',char(10)];
        EL_16=['Solid.BlendEdge "Tube_Ear_Blend_Left_',NumberTube,'"  ',char(10)];
        
        
        
        for i_EL=1:16
            NameEL=['EL_',num2str(i_EL)];
            fprintf(Fid,'%s',eval(NameEL));
        end
        
    end
end



%%  RIGHT EAR
if  Tube_Blend_Outer_Flag~=1
    for nTube=1:Ntube-2
        if nTube<=9
            NumberTube=['00',num2str(nTube)];
        elseif nTube<=99
            NumberTube=['0',num2str(nTube)];
        else
            NumberTube=[num2str(nTube)];
        end
        ER_1=['With Cylinder  ',char(10)];
        ER_2=['     .Reset   ',char(10)];
        ER_3=['     .Name "EarRight_',NumberTube,'"   ',char(10)];
        ER_4=['     .Component "component1"   ',char(10)];
        ER_5=['     .Material "Copper (hard-drawn)"   ',char(10)];
        ER_6=['     .OuterRadius "Tube_R_Outer_',NumberTube,'+abs(Tube_Ear_Center_Right_',NumberTube,')"   ',char(10)];
        ER_7=['     .InnerRadius "Tube_R_Inner_',NumberTube,'+abs(Tube_Ear_Center_Right_',NumberTube,')"   ',char(10)];
        ER_8=['     .Axis "z"   ',char(10)];
        ER_9=['     .Zrange "Tube_Z_End_',NumberTube,'-Tube_Ear_Thick_Right_',NumberTube,'",  "Tube_Z_End_',NumberTube,'"  ',char(10)];
        ER_10=['     .Xcenter "0"   ',char(10)];
        ER_11=['     .Ycenter "Tube_Ear_Center_Right_',NumberTube,'"   ',char(10)];
        ER_12=['     .Segments "0"   ',char(10)];
        ER_13=['     .Create   ',char(10)];
        ER_14=['End With   ',char(10)];
        
        
        ER_15=['Pick.PickEdgeFromId "component1:EarRight_',NumberTube,'", "3", "3"  ',char(10)];
        ER_16=['Solid.BlendEdge "Tube_Ear_Blend_Right_',NumberTube,'"  ',char(10)];
        
        
        
        for i_ER=1:16
            NameER=['ER_',num2str(i_ER)];
            fprintf(Fid,'%s',eval(NameER));
        end
        
    end
end


%%  方支撑杆
for nTube=2:Ntube-2
    if nTube<=9
        NumberTube=['00',num2str(nTube)];
    elseif nTube<=99
        NumberTube=['0',num2str(nTube)];
    else
        NumberTube=[num2str(nTube)];
    end
    
    %%  坐标系
    ST_1=['WCS.ActivateWCS "local"  ',char(10)];
    ST_2=['  ',char(10)];
    ST_3=['With WCS  ',char(10)];
    ST_4=['     .SetNormal "0", "0", "1"  ',char(10)];
    ST_5=['     .SetOrigin "0", "0", "0"  ',char(10)];
    ST_6=['     .SetUVector "1", "0", "0"  ',char(10)];
    ST_7=['End With  ',char(10)];
    ST_8=['  ',char(10)];
    ST_9=['WCS.MoveWCS "local", "0.0", "0.0", "(Tube_Z_Begin_',NumberTube,'+Tube_Z_End_',NumberTube,')/2"  ',char(10)];
    ST_10=['  ',char(10)];
    ST_11=['WCS.RotateWCS "u", "-90.0"  ',char(10)];
    ST_12=['  ',char(10)];
    ST_13=['WCS.RotateWCS "w", "-90.0"  ',char(10)];
    ST_14=['  ',char(10)];
    
    %% 1号支撑杆
    
    if CStem_1_Flag~=1
        ST_15=['With Brick  ',char(10)];
        ST_16=['     .Reset   ',char(10)];
        ST_17=['     .Name "Stem_1_',NumberTube,'"   ',char(10)];
        ST_18=['     .Component "component1"   ',char(10)];
        ST_19=['     .Material "Copper (hard-drawn)"   ',char(10)];
        ST_20=['     .Xrange "Stem_1_Xmin_',NumberTube,'", "Stem_1_Xmax_',NumberTube,'"   ',char(10)];
        ST_21=['     .Yrange "Stem_1_Ymin_',NumberTube,'", "Stem_1_Ymax_',NumberTube,'"   ',char(10)];
        ST_22=['     .Zrange "Stem_1_Zmin_',NumberTube,'", "Stem_1_Zmax_',NumberTube,'"   ',char(10)];
        ST_23=['     .Create  ',char(10)];
        ST_24=['End With  ',char(10)];
        ST_25=['  ',char(10)];
    else
        ST_15=char(10);
        ST_16=char(10);
        ST_17=char(10);
        ST_18=char(10);
        ST_19=char(10);
        ST_20=char(10);
        ST_21=char(10);
        ST_22=char(10);
        ST_23=char(10);
        ST_24=char(10);
        ST_25=char(10);
    end
    
    %% 2号支撑杆
    
    if CStem_2_Flag~=1
        ST_26=['With Brick  ',char(10)];
        ST_27=['     .Reset   ',char(10)];
        ST_28=['     .Name "Stem_2_',NumberTube,'"   ',char(10)];
        ST_29=['     .Component "component1"   ',char(10)];
        ST_30=['     .Material "Copper (hard-drawn)"   ',char(10)];
        ST_31=['     .Xrange "Stem_2_Xmin_',NumberTube,'", "Stem_2_Xmax_',NumberTube,'"   ',char(10)];
        ST_32=['     .Yrange "Stem_2_Ymin_',NumberTube,'", "Stem_2_Ymax_',NumberTube,'"   ',char(10)];
        ST_33=['     .Zrange "Stem_2_Zmin_',NumberTube,'", "Stem_2_Zmax_',NumberTube,'"   ',char(10)];
        ST_34=['     .Create  ',char(10)];
        ST_35=['End With  ',char(10)];
        ST_36=['  ',char(10)];
    else
        ST_26=char(10);
        ST_27=char(10);
        ST_28=char(10);
        ST_29=char(10);
        ST_30=char(10);
        ST_31=char(10);
        ST_32=char(10);
        ST_33=char(10);
        ST_34=char(10);
        ST_35=char(10);
        ST_36=char(10);
    end
    
    
    %%  3号支撑杆
    if CStem_3_Flag~=1
        ST_37=['With Brick  ',char(10)];
        ST_38=['     .Reset   ',char(10)];
        ST_39=['     .Name "Stem_3_',NumberTube,'"   ',char(10)];
        ST_40=['     .Component "component1"   ',char(10)];
        ST_41=['     .Material "Copper (hard-drawn)"   ',char(10)];
        ST_42=['     .Xrange "Stem_3_Xmin_',NumberTube,'", "Stem_3_Xmax_',NumberTube,'"   ',char(10)];
        ST_43=['     .Yrange "Stem_3_Ymin_',NumberTube,'", "Stem_3_Ymax_',NumberTube,'"   ',char(10)];
        ST_44=['     .Zrange "Stem_3_Zmin_',NumberTube,'", "Stem_3_Zmax_',NumberTube,'"   ',char(10)];
        ST_45=['     .Create  ',char(10)];
        ST_46=['End With  ',char(10)];
    else
        ST_37=char(10);
        ST_38=char(10);
        ST_39=char(10);
        ST_40=char(10);
        ST_41=char(10);
        ST_42=char(10);
        ST_43=char(10);
        ST_44=char(10);
        ST_45=char(10);
        ST_46=char(10);
    end
    
    %% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    %% 导角
    if CStem_1_Flag~=1
        ST_47=['Pick.PickEdgeFromId "component1:Stem_1_',NumberTube,'", "3", "3"  ',char(10)];
        ST_48=['Pick.PickEdgeFromId "component1:Stem_1_',NumberTube,'", "1", "1"  ',char(10)];
        ST_49=['Pick.PickEdgeFromId "component1:Stem_1_',NumberTube,'", "5", "5"  ',char(10)];
        ST_50=['Pick.PickEdgeFromId "component1:Stem_1_',NumberTube,'", "7", "7"  ',char(10)];
        ST_51=['Solid.BlendEdge "Stem_1_Blend_',NumberTube,'"  ',char(10)];
    else
        ST_47=char(10);
        ST_48=char(10);
        ST_49=char(10);
        ST_50=char(10);
        ST_51=char(10);
    end
    
    if CStem_2_Flag~=1
        ST_52=['Pick.PickEdgeFromId "component1:Stem_2_',NumberTube,'", "3", "3"  ',char(10)];
        ST_53=['Pick.PickEdgeFromId "component1:Stem_2_',NumberTube,'", "1", "1"  ',char(10)];
        ST_54=['Pick.PickEdgeFromId "component1:Stem_2_',NumberTube,'", "5", "5"  ',char(10)];
        ST_55=['Pick.PickEdgeFromId "component1:Stem_2_',NumberTube,'", "7", "7"  ',char(10)];
        ST_56=['Solid.BlendEdge "Stem_2_Blend_',NumberTube,'"  ',char(10)];
    else
        ST_52=char(10);
        ST_53=char(10);
        ST_54=char(10);
        ST_55=char(10);
        ST_56=char(10);
    end
    
    if CStem_3_Flag~=1
        ST_57=['Pick.PickEdgeFromId "component1:Stem_3_',NumberTube,'", "3", "3"  ',char(10)];
        ST_58=['Pick.PickEdgeFromId "component1:Stem_3_',NumberTube,'", "1", "1"  ',char(10)];
        ST_59=['Pick.PickEdgeFromId "component1:Stem_3_',NumberTube,'", "5", "5"  ',char(10)];
        ST_60=['Pick.PickEdgeFromId "component1:Stem_3_',NumberTube,'", "7", "7"  ',char(10)];
        ST_61=['Solid.BlendEdge "Stem_3_Blend_',NumberTube,'"  ',char(10)];
    else
        ST_57=char(10);
        ST_58=char(10);
        ST_59=char(10);
        ST_60=char(10);
        ST_61=char(10);
    end
    
    
    for i_ST=1:61
        NameST=['ST_',num2str(i_ST)];
        fprintf(Fid,'%s',eval(NameST));
    end
    
end



%%  圆支撑杆
for nTube=2:Ntube-2
    if nTube<=9
        NumberTube=['00',num2str(nTube)];
    elseif nTube<=99
        NumberTube=['0',num2str(nTube)];
    else
        NumberTube=[num2str(nTube)];
    end
    
    %%  坐标系
    
    CST_1=['WCS.ActivateWCS "local"  ',char(10)];
    CST_2=['  ',char(10)];
    CST_3=['With WCS  ',char(10)];
    CST_4=['     .SetNormal "0", "0", "1"  ',char(10)];
    CST_5=['     .SetOrigin "0", "0", "0"  ',char(10)];
    CST_6=['     .SetUVector "1", "0", "0"  ',char(10)];
    CST_7=['End With  ',char(10)];
    CST_8=['  ',char(10)];
    CST_9=['WCS.MoveWCS "local", "0.0", "0.0", "(Tube_Z_Begin_',NumberTube,'+Tube_Z_End_',NumberTube,')/2"  ',char(10)];
    CST_10=['  ',char(10)];
    CST_11=['WCS.RotateWCS "u", "-90.0"  ',char(10)];
    CST_12=['  ',char(10)];
    CST_13=['WCS.RotateWCS "w", "-90.0"  ',char(10)];
    CST_14=['  ',char(10)];
    
    
    
    %% 1号支撑杆
    if CStem_1_Flag==1
        CST_15=['With Cylinder  ',char(10)];
        CST_16=['     .Reset   ',char(10)];
        CST_17=['     .Name "CStem_1_',NumberTube,'"   ',char(10)];
        CST_18=['     .Component "component1"   ',char(10)];
        CST_19=['     .Material "Copper (hard-drawn)"   ',char(10)];
        CST_20=['     .OuterRadius "Stem_1_Cylinder_Radius_',NumberTube,'"   ',char(10)];
        CST_21=['     .InnerRadius "0"   ',char(10)];
        CST_22=['     .Axis "y"   ',char(10)];
        CST_23=['     .Yrange "Stem_1_Cylinder_Ymin_',NumberTube,'",  "Stem_1_Cylinder_Ymax_',NumberTube,'"  ',char(10)];
        CST_24=['     .Zcenter "0"   ',char(10)];
        CST_25=['     .Xcenter "Stem_1_Cylinder_Center_',NumberTube,'"   ',char(10)];
        CST_26=['     .Segments "0"   ',char(10)];
        CST_27=['     .Create   ',char(10)];
        CST_28=['End With   ',char(10)];
    else
        CST_15=char(10);
        CST_16=char(10);
        CST_17=char(10);
        CST_18=char(10);
        CST_19=char(10);
        CST_20=char(10);
        CST_21=char(10);
        CST_22=char(10);
        CST_23=char(10);
        CST_24=char(10);
        CST_25=char(10);
        CST_26=char(10);
        CST_27=char(10);
        CST_28=char(10);
    end
    
    %% 2号支撑杆
    if CStem_2_Flag==1
        CST_29=['With Cylinder  ',char(10)];
        CST_30=['     .Reset   ',char(10)];
        CST_31=['     .Name "CStem_2_',NumberTube,'"   ',char(10)];
        CST_32=['     .Component "component1"   ',char(10)];
        CST_33=['     .Material "Copper (hard-drawn)"   ',char(10)];
        CST_34=['     .OuterRadius "Stem_2_Cylinder_Radius_',NumberTube,'"   ',char(10)];
        CST_35=['     .InnerRadius "0"   ',char(10)];
        CST_36=['     .Axis "y"   ',char(10)];
        CST_37=['     .Yrange "Stem_2_Cylinder_Ymin_',NumberTube,'",  "Stem_2_Cylinder_Ymax_',NumberTube,'"  ',char(10)];
        CST_38=['     .Zcenter "0"   ',char(10)];
        CST_39=['     .Xcenter "Stem_2_Cylinder_Center_',NumberTube,'"   ',char(10)];
        CST_40=['     .Segments "0"   ',char(10)];
        CST_41=['     .Create   ',char(10)];
        CST_42=['End With   ',char(10)];
    else
        CST_29=char(10);
        CST_30=char(10);
        CST_31=char(10);
        CST_32=char(10);
        CST_33=char(10);
        CST_34=char(10);
        CST_35=char(10);
        CST_36=char(10);
        CST_37=char(10);
        CST_38=char(10);
        CST_39=char(10);
        CST_40=char(10);
        CST_41=char(10);
        CST_42=char(10);
    end
    
    %% 3号支撑杆
    if CStem_3_Flag==1
        CST_43=['With Cylinder  ',char(10)];
        CST_44=['     .Reset   ',char(10)];
        CST_45=['     .Name "CStem_3_',NumberTube,'"   ',char(10)];
        CST_46=['     .Component "component1"   ',char(10)];
        CST_47=['     .Material "Copper (hard-drawn)"   ',char(10)];
        CST_48=['     .OuterRadius "Stem_3_Cylinder_Radius_',NumberTube,'"   ',char(10)];
        CST_49=['     .InnerRadius "0"   ',char(10)];
        CST_50=['     .Axis "y"   ',char(10)];
        CST_51=['     .Yrange "Stem_3_Cylinder_Ymin_',NumberTube,'",  "Stem_3_Cylinder_Ymax_',NumberTube,'"  ',char(10)];
        CST_52=['     .Zcenter "0"   ',char(10)];
        CST_53=['     .Xcenter "Stem_3_Cylinder_Center_',NumberTube,'"   ',char(10)];
        CST_54=['     .Segments "0"   ',char(10)];
        CST_55=['     .Create   ',char(10)];
        CST_56=['End With   ',char(10)];
    else
        CST_43=char(10);
        CST_44=char(10);
        CST_45=char(10);
        CST_46=char(10);
        CST_47=char(10);
        CST_48=char(10);
        CST_49=char(10);
        CST_50=char(10);
        CST_51=char(10);
        CST_52=char(10);
        CST_53=char(10);
        CST_54=char(10);
        CST_55=char(10);
        CST_56=char(10);
    end
    
    
    for i_CST=1:56
        NameCST=['CST_',num2str(i_CST)];
        fprintf(Fid,'%s',eval(NameCST));
    end
end


%%  支撑杆连接——形成 LOFT
for nTube=2:Ntube-2
    if nTube<=9
        NumberTube=['00',num2str(nTube)];
    elseif nTube<=99
        NumberTube=['0',num2str(nTube)];
    else
        NumberTube=[num2str(nTube)];
    end
    
    
    %% LOFT_12
    if CStem_1_Flag==1
        LOFT_1=['Pick.PickFaceFromId "component1:CStem_1_',NumberTube,'", "3"   ',char(10)];
    else
        LOFT_1=['Pick.PickFaceFromId "component1:Stem_1_',NumberTube,'", "5"   ',char(10)];
    end
    if CStem_2_Flag==1
        LOFT_2=['Pick.PickFaceFromId "component1:CStem_2_',NumberTube,'", "1"   ',char(10)];
    else
        LOFT_2=['Pick.PickFaceFromId "component1:Stem_2_',NumberTube,'", "8"   ',char(10)];
    end
    
    LOFT_3=['With Loft   ',char(10)];
    LOFT_4=['     .Reset   ',char(10)];
    LOFT_5=['     .Name "Loft_12_',NumberTube,'"   ',char(10)];
    LOFT_6=['     .Component "component1"   ',char(10)];
    LOFT_7=['     .Material "Copper (hard-drawn)"   ',char(10)];
    LOFT_8=['     .Tangency "0.150000"   ',char(10)];
    LOFT_9=['     .CreateNew   ',char(10)];
    LOFT_10=['End With   ',char(10)];
    
    
    
    %% LOFT_23
    if CStem_2_Flag==1
        LOFT_11=['Pick.PickFaceFromId "component1:CStem_2_',NumberTube,'", "3"   ',char(10)];
    else
        LOFT_11=['Pick.PickFaceFromId "component1:Stem_2_',NumberTube,'", "5"   ',char(10)];
    end
    if CStem_3_Flag==1
        LOFT_12=['Pick.PickFaceFromId "component1:CStem_3_',NumberTube,'", "1"   ',char(10)];
    else
        LOFT_12=['Pick.PickFaceFromId "component1:Stem_3_',NumberTube,'", "8"   ',char(10)];
    end
    
    LOFT_13=['With Loft   ',char(10)];
    LOFT_14=['     .Reset   ',char(10)];
    LOFT_15=['     .Name "Loft_23_',NumberTube,'"   ',char(10)];
    LOFT_16=['     .Component "component1"   ',char(10)];
    LOFT_17=['     .Material "Copper (hard-drawn)"   ',char(10)];
    LOFT_18=['     .Tangency "0.150000"   ',char(10)];
    LOFT_19=['     .CreateNew   ',char(10)];
    LOFT_20=['End With   ',char(10)];
    
    for i_LOFT=1:20
        NameLOFT=['LOFT_',num2str(i_LOFT)];
        fprintf(Fid,'%s',eval(NameLOFT));
    end
end


%%   将支撑杆旋转到特定度数

Stem_Spin_Initial_Flag=find(Stem_Spin_Degree_Flag==1);
NStem_Spin_Initial_Flag=length(Stem_Spin_Initial_Flag);

for nStem_Spin_Degree_flag=1:4
    Stem_Spin_Degree_flag=Stem_Spin_Degree_Flag(nStem_Spin_Degree_flag);
    for nTube=2:Ntube-2
        if nTube<=9
            NumberTube=['00',num2str(nTube)];
        elseif nTube<=99
            NumberTube=['0',num2str(nTube)];
        else
            NumberTube=[num2str(nTube)];
        end
        if CStem_1_Flag==1
            STEM_1_Temp=['CStem_1_',NumberTube];
        else
            STEM_1_Temp=['Stem_1_',NumberTube];
        end
        if CStem_2_Flag==1
            STEM_2_Temp=['CStem_2_',NumberTube];
        else
            STEM_2_Temp=['Stem_2_',NumberTube];
        end
        if CStem_3_Flag==1
            STEM_3_Temp=['CStem_3_',NumberTube];
        else
            STEM_3_Temp=['Stem_3_',NumberTube];
        end
        STEM_4_Temp=['Loft_12_',NumberTube,];
        STEM_5_Temp=['Loft_23_',NumberTube,];
        
        
        
        switch Stem_Spin_Degree_flag
            case 0
            case 1
                StemSpin_0=['WCS.ActivateWCS "global" ',char(10)];
                StemSpin_1=['With Transform  ',char(10)];
                StemSpin_2=['     .Reset  ',char(10)];
                StemSpin_3=['     .Name "component1:',STEM_1_Temp,'"  ',char(10)];
                StemSpin_4=['     .Origin "Free"  ',char(10)];
                StemSpin_5=['     .Center "0", "0", "0"  ',char(10)];
                StemSpin_6=['     .Angle "0", "0", "Stem_Spin_Degree_',num2str(nStem_Spin_Degree_flag),'_',NumberTube,'"  ',char(10)];
                if NStem_Spin_Initial_Flag==1
                    if nStem_Spin_Degree_flag>Stem_Spin_Initial_Flag
                        StemSpin_6=['     .Angle "0", "0", "Stem_Spin_Degree_',num2str(nStem_Spin_Degree_flag),'_',NumberTube,'-Stem_Spin_Degree_',num2str(Stem_Spin_Initial_Flag),'_',NumberTube,'"  ',char(10)];
                    end
                elseif NStem_Spin_Initial_Flag==2
                    if nStem_Spin_Degree_flag>Stem_Spin_Initial_Flag(1)
                        StemSpin_6=['     .Angle "0", "0", "Stem_Spin_Degree_',num2str(nStem_Spin_Degree_flag),'_',NumberTube,'-Stem_Spin_Degree_',num2str(Stem_Spin_Initial_Flag(1)),'_',NumberTube,'"  ',char(10)];
                    end
                    if nStem_Spin_Degree_flag>Stem_Spin_Initial_Flag(2)
                        StemSpin_6=['     .Angle "0", "0", "Stem_Spin_Degree_',num2str(nStem_Spin_Degree_flag),'_',NumberTube,'-Stem_Spin_Degree_',num2str(Stem_Spin_Initial_Flag(2)),'_',NumberTube,'"  ',char(10)];
                    end
                elseif NStem_Spin_Initial_Flag==3
                    if nStem_Spin_Degree_flag>Stem_Spin_Initial_Flag(1)
                        StemSpin_6=['     .Angle "0", "0", "Stem_Spin_Degree_',num2str(nStem_Spin_Degree_flag),'_',NumberTube,'-Stem_Spin_Degree_',num2str(Stem_Spin_Initial_Flag(1)),'_',NumberTube,'"  ',char(10)];
                    end
                    if nStem_Spin_Degree_flag>Stem_Spin_Initial_Flag(2)
                        StemSpin_6=['     .Angle "0", "0", "Stem_Spin_Degree_',num2str(nStem_Spin_Degree_flag),'_',NumberTube,'-Stem_Spin_Degree_',num2str(Stem_Spin_Initial_Flag(2)),'_',NumberTube,'"  ',char(10)];
                    end
                    if nStem_Spin_Degree_flag>Stem_Spin_Initial_Flag(3)
                        StemSpin_6=['     .Angle "0", "0", "Stem_Spin_Degree_',num2str(nStem_Spin_Degree_flag),'_',NumberTube,'-Stem_Spin_Degree_',num2str(Stem_Spin_Initial_Flag(3)),'_',NumberTube,'"  ',char(10)];
                    end
                end
                StemSpin_7=['     .MultipleObjects "False"  ',char(10)];
                StemSpin_8=['     .GroupObjects "False"  ',char(10)];
                StemSpin_9=['     .Repetitions "1"  ',char(10)];
                StemSpin_10=['     .MultipleSelection "False"  ',char(10)];
                StemSpin_11=['     .Transform "Shape", "Rotate"  ',char(10)];
                StemSpin_12=['End With  ',char(10)];
                
                StemSpin_13=['With Transform  ',char(10)];
                StemSpin_14=['     .Reset  ',char(10)];
                StemSpin_15=['     .Name "component1:',STEM_2_Temp,'"  ',char(10)];
                StemSpin_16=['     .Origin "Free"  ',char(10)];
                StemSpin_17=['     .Center "0", "0", "0"  ',char(10)];
                StemSpin_18=['     .Angle "0", "0", "Stem_Spin_Degree_',num2str(nStem_Spin_Degree_flag),'_',NumberTube,'"  ',char(10)];
                if NStem_Spin_Initial_Flag==1
                    if nStem_Spin_Degree_flag>Stem_Spin_Initial_Flag
                        StemSpin_18=['     .Angle "0", "0", "Stem_Spin_Degree_',num2str(nStem_Spin_Degree_flag),'_',NumberTube,'-Stem_Spin_Degree_',num2str(Stem_Spin_Initial_Flag),'_',NumberTube,'"  ',char(10)];
                    end
                elseif NStem_Spin_Initial_Flag==2
                    if nStem_Spin_Degree_flag>Stem_Spin_Initial_Flag(1)
                        StemSpin_18=['     .Angle "0", "0", "Stem_Spin_Degree_',num2str(nStem_Spin_Degree_flag),'_',NumberTube,'-Stem_Spin_Degree_',num2str(Stem_Spin_Initial_Flag(1)),'_',NumberTube,'"  ',char(10)];
                    end
                    if nStem_Spin_Degree_flag>Stem_Spin_Initial_Flag(2)
                        StemSpin_18=['     .Angle "0", "0", "Stem_Spin_Degree_',num2str(nStem_Spin_Degree_flag),'_',NumberTube,'-Stem_Spin_Degree_',num2str(Stem_Spin_Initial_Flag(2)),'_',NumberTube,'"  ',char(10)];
                    end
                elseif NStem_Spin_Initial_Flag==3
                    if nStem_Spin_Degree_flag>Stem_Spin_Initial_Flag(1)
                        StemSpin_18=['     .Angle "0", "0", "Stem_Spin_Degree_',num2str(nStem_Spin_Degree_flag),'_',NumberTube,'-Stem_Spin_Degree_',num2str(Stem_Spin_Initial_Flag(1)),'_',NumberTube,'"  ',char(10)];
                    end
                    if nStem_Spin_Degree_flag>Stem_Spin_Initial_Flag(2)
                        StemSpin_18=['     .Angle "0", "0", "Stem_Spin_Degree_',num2str(nStem_Spin_Degree_flag),'_',NumberTube,'-Stem_Spin_Degree_',num2str(Stem_Spin_Initial_Flag(2)),'_',NumberTube,'"  ',char(10)];
                    end
                    if nStem_Spin_Degree_flag>Stem_Spin_Initial_Flag(3)
                        StemSpin_18=['     .Angle "0", "0", "Stem_Spin_Degree_',num2str(nStem_Spin_Degree_flag),'_',NumberTube,'-Stem_Spin_Degree_',num2str(Stem_Spin_Initial_Flag(3)),'_',NumberTube,'"  ',char(10)];
                    end
                end
                StemSpin_19=['     .MultipleObjects "False"  ',char(10)];
                StemSpin_20=['     .GroupObjects "False"  ',char(10)];
                StemSpin_21=['     .Repetitions "1"  ',char(10)];
                StemSpin_22=['     .MultipleSelection "False"  ',char(10)];
                StemSpin_23=['     .Transform "Shape", "Rotate"  ',char(10)];
                StemSpin_24=['End With  ',char(10)];
                
                StemSpin_25=['With Transform  ',char(10)];
                StemSpin_26=['     .Reset  ',char(10)];
                StemSpin_27=['     .Name "component1:',STEM_3_Temp,'"  ',char(10)];
                StemSpin_28=['     .Origin "Free"  ',char(10)];
                StemSpin_29=['     .Center "0", "0", "0"  ',char(10)];
                StemSpin_30=['     .Angle "0", "0", "Stem_Spin_Degree_',num2str(nStem_Spin_Degree_flag),'_',NumberTube,'"  ',char(10)];
                if NStem_Spin_Initial_Flag==1
                    if nStem_Spin_Degree_flag>Stem_Spin_Initial_Flag
                        StemSpin_30=['     .Angle "0", "0", "Stem_Spin_Degree_',num2str(nStem_Spin_Degree_flag),'_',NumberTube,'-Stem_Spin_Degree_',num2str(Stem_Spin_Initial_Flag),'_',NumberTube,'"  ',char(10)];
                    end
                elseif NStem_Spin_Initial_Flag==2
                    if nStem_Spin_Degree_flag>Stem_Spin_Initial_Flag(1)
                        StemSpin_30=['     .Angle "0", "0", "Stem_Spin_Degree_',num2str(nStem_Spin_Degree_flag),'_',NumberTube,'-Stem_Spin_Degree_',num2str(Stem_Spin_Initial_Flag(1)),'_',NumberTube,'"  ',char(10)];
                    end
                    if nStem_Spin_Degree_flag>Stem_Spin_Initial_Flag(2)
                        StemSpin_30=['     .Angle "0", "0", "Stem_Spin_Degree_',num2str(nStem_Spin_Degree_flag),'_',NumberTube,'-Stem_Spin_Degree_',num2str(Stem_Spin_Initial_Flag(2)),'_',NumberTube,'"  ',char(10)];
                    end
                elseif NStem_Spin_Initial_Flag==3
                    if nStem_Spin_Degree_flag>Stem_Spin_Initial_Flag(1)
                        StemSpin_30=['     .Angle "0", "0", "Stem_Spin_Degree_',num2str(nStem_Spin_Degree_flag),'_',NumberTube,'-Stem_Spin_Degree_',num2str(Stem_Spin_Initial_Flag(1)),'_',NumberTube,'"  ',char(10)];
                    end
                    if nStem_Spin_Degree_flag>Stem_Spin_Initial_Flag(2)
                        StemSpin_30=['     .Angle "0", "0", "Stem_Spin_Degree_',num2str(nStem_Spin_Degree_flag),'_',NumberTube,'-Stem_Spin_Degree_',num2str(Stem_Spin_Initial_Flag(2)),'_',NumberTube,'"  ',char(10)];
                    end
                    if nStem_Spin_Degree_flag>Stem_Spin_Initial_Flag(3)
                        StemSpin_30=['     .Angle "0", "0", "Stem_Spin_Degree_',num2str(nStem_Spin_Degree_flag),'_',NumberTube,'-Stem_Spin_Degree_',num2str(Stem_Spin_Initial_Flag(3)),'_',NumberTube,'"  ',char(10)];
                    end
                end
                StemSpin_31=['     .MultipleObjects "False"  ',char(10)];
                StemSpin_32=['     .GroupObjects "False"  ',char(10)];
                StemSpin_33=['     .Repetitions "1"  ',char(10)];
                StemSpin_34=['     .MultipleSelection "False"  ',char(10)];
                StemSpin_35=['     .Transform "Shape", "Rotate"  ',char(10)];
                StemSpin_36=['End With  ',char(10)];
                
                StemSpin_37=['With Transform  ',char(10)];
                StemSpin_38=['     .Reset  ',char(10)];
                StemSpin_39=['     .Name "component1:',STEM_4_Temp,'"  ',char(10)];
                StemSpin_40=['     .Origin "Free"  ',char(10)];
                StemSpin_41=['     .Center "0", "0", "0"  ',char(10)];
                StemSpin_42=['     .Angle "0", "0", "Stem_Spin_Degree_',num2str(nStem_Spin_Degree_flag),'_',NumberTube,'"  ',char(10)];
                if NStem_Spin_Initial_Flag==1
                    if nStem_Spin_Degree_flag>Stem_Spin_Initial_Flag
                        StemSpin_42=['     .Angle "0", "0", "Stem_Spin_Degree_',num2str(nStem_Spin_Degree_flag),'_',NumberTube,'-Stem_Spin_Degree_',num2str(Stem_Spin_Initial_Flag),'_',NumberTube,'"  ',char(10)];
                    end
                elseif NStem_Spin_Initial_Flag==2
                    if nStem_Spin_Degree_flag>Stem_Spin_Initial_Flag(1)
                        StemSpin_42=['     .Angle "0", "0", "Stem_Spin_Degree_',num2str(nStem_Spin_Degree_flag),'_',NumberTube,'-Stem_Spin_Degree_',num2str(Stem_Spin_Initial_Flag(1)),'_',NumberTube,'"  ',char(10)];
                    end
                    if nStem_Spin_Degree_flag>Stem_Spin_Initial_Flag(2)
                        StemSpin_42=['     .Angle "0", "0", "Stem_Spin_Degree_',num2str(nStem_Spin_Degree_flag),'_',NumberTube,'-Stem_Spin_Degree_',num2str(Stem_Spin_Initial_Flag(2)),'_',NumberTube,'"  ',char(10)];
                    end
                elseif NStem_Spin_Initial_Flag==3
                    if nStem_Spin_Degree_flag>Stem_Spin_Initial_Flag(1)
                        StemSpin_42=['     .Angle "0", "0", "Stem_Spin_Degree_',num2str(nStem_Spin_Degree_flag),'_',NumberTube,'-Stem_Spin_Degree_',num2str(Stem_Spin_Initial_Flag(1)),'_',NumberTube,'"  ',char(10)];
                    end
                    if nStem_Spin_Degree_flag>Stem_Spin_Initial_Flag(2)
                        StemSpin_42=['     .Angle "0", "0", "Stem_Spin_Degree_',num2str(nStem_Spin_Degree_flag),'_',NumberTube,'-Stem_Spin_Degree_',num2str(Stem_Spin_Initial_Flag(2)),'_',NumberTube,'"  ',char(10)];
                    end
                    if nStem_Spin_Degree_flag>Stem_Spin_Initial_Flag(3)
                        StemSpin_42=['     .Angle "0", "0", "Stem_Spin_Degree_',num2str(nStem_Spin_Degree_flag),'_',NumberTube,'-Stem_Spin_Degree_',num2str(Stem_Spin_Initial_Flag(3)),'_',NumberTube,'"  ',char(10)];
                    end
                end
                StemSpin_43=['     .MultipleObjects "False"  ',char(10)];
                StemSpin_44=['     .GroupObjects "False"  ',char(10)];
                StemSpin_45=['     .Repetitions "1"  ',char(10)];
                StemSpin_46=['     .MultipleSelection "False"  ',char(10)];
                StemSpin_47=['     .Transform "Shape", "Rotate"  ',char(10)];
                StemSpin_48=['End With  ',char(10)];
                
                StemSpin_49=['With Transform  ',char(10)];
                StemSpin_50=['     .Reset  ',char(10)];
                StemSpin_51=['     .Name "component1:',STEM_5_Temp,'"  ',char(10)];
                StemSpin_52=['     .Origin "Free"  ',char(10)];
                StemSpin_53=['     .Center "0", "0", "0"  ',char(10)];
                StemSpin_54=['     .Angle "0", "0", "Stem_Spin_Degree_',num2str(nStem_Spin_Degree_flag),'_',NumberTube,'"  ',char(10)];
                if NStem_Spin_Initial_Flag==1
                    if nStem_Spin_Degree_flag>Stem_Spin_Initial_Flag
                        StemSpin_54=['     .Angle "0", "0", "Stem_Spin_Degree_',num2str(nStem_Spin_Degree_flag),'_',NumberTube,'-Stem_Spin_Degree_',num2str(Stem_Spin_Initial_Flag),'_',NumberTube,'"  ',char(10)];
                    end
                elseif NStem_Spin_Initial_Flag==2
                    if nStem_Spin_Degree_flag>Stem_Spin_Initial_Flag(1)
                        StemSpin_54=['     .Angle "0", "0", "Stem_Spin_Degree_',num2str(nStem_Spin_Degree_flag),'_',NumberTube,'-Stem_Spin_Degree_',num2str(Stem_Spin_Initial_Flag(1)),'_',NumberTube,'"  ',char(10)];
                    end
                    if nStem_Spin_Degree_flag>Stem_Spin_Initial_Flag(2)
                        StemSpin_54=['     .Angle "0", "0", "Stem_Spin_Degree_',num2str(nStem_Spin_Degree_flag),'_',NumberTube,'-Stem_Spin_Degree_',num2str(Stem_Spin_Initial_Flag(2)),'_',NumberTube,'"  ',char(10)];
                    end
                elseif NStem_Spin_Initial_Flag==3
                    if nStem_Spin_Degree_flag>Stem_Spin_Initial_Flag(1)
                        StemSpin_54=['     .Angle "0", "0", "Stem_Spin_Degree_',num2str(nStem_Spin_Degree_flag),'_',NumberTube,'-Stem_Spin_Degree_',num2str(Stem_Spin_Initial_Flag(1)),'_',NumberTube,'"  ',char(10)];
                    end
                    if nStem_Spin_Degree_flag>Stem_Spin_Initial_Flag(2)
                        StemSpin_54=['     .Angle "0", "0", "Stem_Spin_Degree_',num2str(nStem_Spin_Degree_flag),'_',NumberTube,'-Stem_Spin_Degree_',num2str(Stem_Spin_Initial_Flag(2)),'_',NumberTube,'"  ',char(10)];
                    end
                    if nStem_Spin_Degree_flag>Stem_Spin_Initial_Flag(3)
                        StemSpin_54=['     .Angle "0", "0", "Stem_Spin_Degree_',num2str(nStem_Spin_Degree_flag),'_',NumberTube,'-Stem_Spin_Degree_',num2str(Stem_Spin_Initial_Flag(3)),'_',NumberTube,'"  ',char(10)];
                    end
                end
                StemSpin_55=['     .MultipleObjects "False"  ',char(10)];
                StemSpin_56=['     .GroupObjects "False"  ',char(10)];
                StemSpin_57=['     .Repetitions "1"  ',char(10)];
                StemSpin_58=['     .MultipleSelection "False"  ',char(10)];
                StemSpin_59=['     .Transform "Shape", "Rotate"  ',char(10)];
                StemSpin_60=['End With  ',char(10)];
                
                for i_StemSpin=0:60
                    NameStemSpin=['StemSpin_',num2str(i_StemSpin)];
                    fprintf(Fid,'%s',eval(NameStemSpin));
                end
            case 2
                
                StemSpin_0=['WCS.ActivateWCS "global" ',char(10)];
                StemSpin_1=['With Transform  ',char(10)];
                StemSpin_2=['     .Reset  ',char(10)];
                StemSpin_3=['     .Name "component1:',STEM_1_Temp,'"  ',char(10)];
                StemSpin_4=['     .Origin "Free"  ',char(10)];
                StemSpin_5=['     .Center "0", "0", "0"  ',char(10)];
                StemSpin_6=['     .Angle "0", "0", "Stem_Spin_Degree_',num2str(nStem_Spin_Degree_flag),'_',NumberTube,'"  ',char(10)];
                if NStem_Spin_Initial_Flag==1
                    if nStem_Spin_Degree_flag>Stem_Spin_Initial_Flag
                        StemSpin_6=['     .Angle "0", "0", "Stem_Spin_Degree_',num2str(nStem_Spin_Degree_flag),'_',NumberTube,'-Stem_Spin_Degree_',num2str(Stem_Spin_Initial_Flag),'_',NumberTube,'"  ',char(10)];
                    end
                elseif NStem_Spin_Initial_Flag==2
                    if nStem_Spin_Degree_flag>Stem_Spin_Initial_Flag(1)
                        StemSpin_6=['     .Angle "0", "0", "Stem_Spin_Degree_',num2str(nStem_Spin_Degree_flag),'_',NumberTube,'-Stem_Spin_Degree_',num2str(Stem_Spin_Initial_Flag(1)),'_',NumberTube,'"  ',char(10)];
                    end
                    if nStem_Spin_Degree_flag>Stem_Spin_Initial_Flag(2)
                        StemSpin_6=['     .Angle "0", "0", "Stem_Spin_Degree_',num2str(nStem_Spin_Degree_flag),'_',NumberTube,'-Stem_Spin_Degree_',num2str(Stem_Spin_Initial_Flag(2)),'_',NumberTube,'"  ',char(10)];
                    end
                elseif NStem_Spin_Initial_Flag==3
                    if nStem_Spin_Degree_flag>Stem_Spin_Initial_Flag(1)
                        StemSpin_6=['     .Angle "0", "0", "Stem_Spin_Degree_',num2str(nStem_Spin_Degree_flag),'_',NumberTube,'-Stem_Spin_Degree_',num2str(Stem_Spin_Initial_Flag(1)),'_',NumberTube,'"  ',char(10)];
                    end
                    if nStem_Spin_Degree_flag>Stem_Spin_Initial_Flag(2)
                        StemSpin_6=['     .Angle "0", "0", "Stem_Spin_Degree_',num2str(nStem_Spin_Degree_flag),'_',NumberTube,'-Stem_Spin_Degree_',num2str(Stem_Spin_Initial_Flag(2)),'_',NumberTube,'"  ',char(10)];
                    end
                    if nStem_Spin_Degree_flag>Stem_Spin_Initial_Flag(3)
                        StemSpin_6=['     .Angle "0", "0", "Stem_Spin_Degree_',num2str(nStem_Spin_Degree_flag),'_',NumberTube,'-Stem_Spin_Degree_',num2str(Stem_Spin_Initial_Flag(3)),'_',NumberTube,'"  ',char(10)];
                    end
                end
                StemSpin_7=['     .MultipleObjects "True"  ',char(10)];
                StemSpin_8=['     .GroupObjects "False"  ',char(10)];
                StemSpin_9=['     .Repetitions "1"  ',char(10)];
                StemSpin_10=['     .MultipleSelection "False"  ',char(10)];
                StemSpin_11=['     .Destination ""  ',char(10)];
                StemSpin_12=['     .Material ""  ',char(10)];
                StemSpin_13=['     .Transform "Shape", "Rotate"  ',char(10)];
                StemSpin_14=['End With  ',char(10)];
                
                StemSpin_15=['With Transform  ',char(10)];
                StemSpin_16=['     .Reset  ',char(10)];
                StemSpin_17=['     .Name "component1:',STEM_2_Temp,'"  ',char(10)];
                StemSpin_18=['     .Origin "Free"  ',char(10)];
                StemSpin_19=['     .Center "0", "0", "0"  ',char(10)];
                StemSpin_20=['     .Angle "0", "0", "Stem_Spin_Degree_',num2str(nStem_Spin_Degree_flag),'_',NumberTube,'"  ',char(10)];
                if NStem_Spin_Initial_Flag==1
                    if nStem_Spin_Degree_flag>Stem_Spin_Initial_Flag
                        StemSpin_20=['     .Angle "0", "0", "Stem_Spin_Degree_',num2str(nStem_Spin_Degree_flag),'_',NumberTube,'-Stem_Spin_Degree_',num2str(Stem_Spin_Initial_Flag),'_',NumberTube,'"  ',char(10)];
                    end
                elseif NStem_Spin_Initial_Flag==2
                    if nStem_Spin_Degree_flag>Stem_Spin_Initial_Flag(1)
                        StemSpin_20=['     .Angle "0", "0", "Stem_Spin_Degree_',num2str(nStem_Spin_Degree_flag),'_',NumberTube,'-Stem_Spin_Degree_',num2str(Stem_Spin_Initial_Flag(1)),'_',NumberTube,'"  ',char(10)];
                    end
                    if nStem_Spin_Degree_flag>Stem_Spin_Initial_Flag(2)
                        StemSpin_20=['     .Angle "0", "0", "Stem_Spin_Degree_',num2str(nStem_Spin_Degree_flag),'_',NumberTube,'-Stem_Spin_Degree_',num2str(Stem_Spin_Initial_Flag(2)),'_',NumberTube,'"  ',char(10)];
                    end
                elseif NStem_Spin_Initial_Flag==3
                    if nStem_Spin_Degree_flag>Stem_Spin_Initial_Flag(1)
                        StemSpin_20=['     .Angle "0", "0", "Stem_Spin_Degree_',num2str(nStem_Spin_Degree_flag),'_',NumberTube,'-Stem_Spin_Degree_',num2str(Stem_Spin_Initial_Flag(1)),'_',NumberTube,'"  ',char(10)];
                    end
                    if nStem_Spin_Degree_flag>Stem_Spin_Initial_Flag(2)
                        StemSpin_20=['     .Angle "0", "0", "Stem_Spin_Degree_',num2str(nStem_Spin_Degree_flag),'_',NumberTube,'-Stem_Spin_Degree_',num2str(Stem_Spin_Initial_Flag(2)),'_',NumberTube,'"  ',char(10)];
                    end
                    if nStem_Spin_Degree_flag>Stem_Spin_Initial_Flag(3)
                        StemSpin_20=['     .Angle "0", "0", "Stem_Spin_Degree_',num2str(nStem_Spin_Degree_flag),'_',NumberTube,'-Stem_Spin_Degree_',num2str(Stem_Spin_Initial_Flag(3)),'_',NumberTube,'"  ',char(10)];
                    end
                end
                StemSpin_21=['     .MultipleObjects "True"  ',char(10)];
                StemSpin_22=['     .GroupObjects "False"  ',char(10)];
                StemSpin_23=['     .Repetitions "1"  ',char(10)];
                StemSpin_24=['     .MultipleSelection "False"  ',char(10)];
                StemSpin_25=['     .Destination ""  ',char(10)];
                StemSpin_26=['     .Material ""  ',char(10)];
                StemSpin_27=['     .Transform "Shape", "Rotate"  ',char(10)];
                StemSpin_28=['End With  ',char(10)];
                
                StemSpin_29=['With Transform  ',char(10)];
                StemSpin_30=['     .Reset  ',char(10)];
                StemSpin_31=['     .Name "component1:',STEM_3_Temp,'"  ',char(10)];
                StemSpin_32=['     .Origin "Free"  ',char(10)];
                StemSpin_33=['     .Center "0", "0", "0"  ',char(10)];
                StemSpin_34=['     .Angle "0", "0", "Stem_Spin_Degree_',num2str(nStem_Spin_Degree_flag),'_',NumberTube,'"  ',char(10)];
                if NStem_Spin_Initial_Flag==1
                    if nStem_Spin_Degree_flag>Stem_Spin_Initial_Flag
                        StemSpin_34=['     .Angle "0", "0", "Stem_Spin_Degree_',num2str(nStem_Spin_Degree_flag),'_',NumberTube,'-Stem_Spin_Degree_',num2str(Stem_Spin_Initial_Flag),'_',NumberTube,'"  ',char(10)];
                    end
                elseif NStem_Spin_Initial_Flag==2
                    if nStem_Spin_Degree_flag>Stem_Spin_Initial_Flag(1)
                        StemSpin_34=['     .Angle "0", "0", "Stem_Spin_Degree_',num2str(nStem_Spin_Degree_flag),'_',NumberTube,'-Stem_Spin_Degree_',num2str(Stem_Spin_Initial_Flag(1)),'_',NumberTube,'"  ',char(10)];
                    end
                    if nStem_Spin_Degree_flag>Stem_Spin_Initial_Flag(2)
                        StemSpin_34=['     .Angle "0", "0", "Stem_Spin_Degree_',num2str(nStem_Spin_Degree_flag),'_',NumberTube,'-Stem_Spin_Degree_',num2str(Stem_Spin_Initial_Flag(2)),'_',NumberTube,'"  ',char(10)];
                    end
                elseif NStem_Spin_Initial_Flag==3
                    if nStem_Spin_Degree_flag>Stem_Spin_Initial_Flag(1)
                        StemSpin_34=['     .Angle "0", "0", "Stem_Spin_Degree_',num2str(nStem_Spin_Degree_flag),'_',NumberTube,'-Stem_Spin_Degree_',num2str(Stem_Spin_Initial_Flag(1)),'_',NumberTube,'"  ',char(10)];
                    end
                    if nStem_Spin_Degree_flag>Stem_Spin_Initial_Flag(2)
                        StemSpin_34=['     .Angle "0", "0", "Stem_Spin_Degree_',num2str(nStem_Spin_Degree_flag),'_',NumberTube,'-Stem_Spin_Degree_',num2str(Stem_Spin_Initial_Flag(2)),'_',NumberTube,'"  ',char(10)];
                    end
                    if nStem_Spin_Degree_flag>Stem_Spin_Initial_Flag(3)
                        StemSpin_34=['     .Angle "0", "0", "Stem_Spin_Degree_',num2str(nStem_Spin_Degree_flag),'_',NumberTube,'-Stem_Spin_Degree_',num2str(Stem_Spin_Initial_Flag(3)),'_',NumberTube,'"  ',char(10)];
                    end
                end
                StemSpin_35=['     .MultipleObjects "True"  ',char(10)];
                StemSpin_36=['     .GroupObjects "False"  ',char(10)];
                StemSpin_37=['     .Repetitions "1"  ',char(10)];
                StemSpin_38=['     .MultipleSelection "False"  ',char(10)];
                StemSpin_39=['     .Destination ""  ',char(10)];
                StemSpin_40=['     .Material ""  ',char(10)];
                StemSpin_41=['     .Transform "Shape", "Rotate"  ',char(10)];
                StemSpin_42=['End With  ',char(10)];
                
                StemSpin_43=['With Transform  ',char(10)];
                StemSpin_44=['     .Reset  ',char(10)];
                StemSpin_45=['     .Name "component1:',STEM_4_Temp,'"  ',char(10)];
                StemSpin_46=['     .Origin "Free"  ',char(10)];
                StemSpin_47=['     .Center "0", "0", "0"  ',char(10)];
                StemSpin_48=['     .Angle "0", "0", "Stem_Spin_Degree_',num2str(nStem_Spin_Degree_flag),'_',NumberTube,'"  ',char(10)];
                if NStem_Spin_Initial_Flag==1
                    if nStem_Spin_Degree_flag>Stem_Spin_Initial_Flag
                        StemSpin_48=['     .Angle "0", "0", "Stem_Spin_Degree_',num2str(nStem_Spin_Degree_flag),'_',NumberTube,'-Stem_Spin_Degree_',num2str(Stem_Spin_Initial_Flag),'_',NumberTube,'"  ',char(10)];
                    end
                elseif NStem_Spin_Initial_Flag==2
                    if nStem_Spin_Degree_flag>Stem_Spin_Initial_Flag(1)
                        StemSpin_48=['     .Angle "0", "0", "Stem_Spin_Degree_',num2str(nStem_Spin_Degree_flag),'_',NumberTube,'-Stem_Spin_Degree_',num2str(Stem_Spin_Initial_Flag(1)),'_',NumberTube,'"  ',char(10)];
                    end
                    if nStem_Spin_Degree_flag>Stem_Spin_Initial_Flag(2)
                        StemSpin_48=['     .Angle "0", "0", "Stem_Spin_Degree_',num2str(nStem_Spin_Degree_flag),'_',NumberTube,'-Stem_Spin_Degree_',num2str(Stem_Spin_Initial_Flag(2)),'_',NumberTube,'"  ',char(10)];
                    end
                elseif NStem_Spin_Initial_Flag==3
                    if nStem_Spin_Degree_flag>Stem_Spin_Initial_Flag(1)
                        StemSpin_48=['     .Angle "0", "0", "Stem_Spin_Degree_',num2str(nStem_Spin_Degree_flag),'_',NumberTube,'-Stem_Spin_Degree_',num2str(Stem_Spin_Initial_Flag(1)),'_',NumberTube,'"  ',char(10)];
                    end
                    if nStem_Spin_Degree_flag>Stem_Spin_Initial_Flag(2)
                        StemSpin_48=['     .Angle "0", "0", "Stem_Spin_Degree_',num2str(nStem_Spin_Degree_flag),'_',NumberTube,'-Stem_Spin_Degree_',num2str(Stem_Spin_Initial_Flag(2)),'_',NumberTube,'"  ',char(10)];
                    end
                    if nStem_Spin_Degree_flag>Stem_Spin_Initial_Flag(3)
                        StemSpin_48=['     .Angle "0", "0", "Stem_Spin_Degree_',num2str(nStem_Spin_Degree_flag),'_',NumberTube,'-Stem_Spin_Degree_',num2str(Stem_Spin_Initial_Flag(3)),'_',NumberTube,'"  ',char(10)];
                    end
                end
                StemSpin_49=['     .MultipleObjects "True"  ',char(10)];
                StemSpin_50=['     .GroupObjects "False"  ',char(10)];
                StemSpin_51=['     .Repetitions "1"  ',char(10)];
                StemSpin_52=['     .MultipleSelection "False"  ',char(10)];
                StemSpin_53=['     .Destination ""  ',char(10)];
                StemSpin_54=['     .Material ""  ',char(10)];
                StemSpin_55=['     .Transform "Shape", "Rotate"  ',char(10)];
                StemSpin_56=['End With  ',char(10)];
                
                StemSpin_57=['With Transform  ',char(10)];
                StemSpin_58=['     .Reset  ',char(10)];
                StemSpin_59=['     .Name "component1:',STEM_5_Temp,'"  ',char(10)];
                StemSpin_60=['     .Origin "Free"  ',char(10)];
                StemSpin_61=['     .Center "0", "0", "0"  ',char(10)];
                StemSpin_62=['     .Angle "0", "0", "Stem_Spin_Degree_',num2str(nStem_Spin_Degree_flag),'_',NumberTube,'"  ',char(10)];
                if NStem_Spin_Initial_Flag==1
                    if nStem_Spin_Degree_flag>Stem_Spin_Initial_Flag
                        StemSpin_62=['     .Angle "0", "0", "Stem_Spin_Degree_',num2str(nStem_Spin_Degree_flag),'_',NumberTube,'-Stem_Spin_Degree_',num2str(Stem_Spin_Initial_Flag),'_',NumberTube,'"  ',char(10)];
                    end
                elseif NStem_Spin_Initial_Flag==2
                    if nStem_Spin_Degree_flag>Stem_Spin_Initial_Flag(1)
                        StemSpin_62=['     .Angle "0", "0", "Stem_Spin_Degree_',num2str(nStem_Spin_Degree_flag),'_',NumberTube,'-Stem_Spin_Degree_',num2str(Stem_Spin_Initial_Flag(1)),'_',NumberTube,'"  ',char(10)];
                    end
                    if nStem_Spin_Degree_flag>Stem_Spin_Initial_Flag(2)
                        StemSpin_62=['     .Angle "0", "0", "Stem_Spin_Degree_',num2str(nStem_Spin_Degree_flag),'_',NumberTube,'-Stem_Spin_Degree_',num2str(Stem_Spin_Initial_Flag(2)),'_',NumberTube,'"  ',char(10)];
                    end
                elseif NStem_Spin_Initial_Flag==3
                    if nStem_Spin_Degree_flag>Stem_Spin_Initial_Flag(1)
                        StemSpin_62=['     .Angle "0", "0", "Stem_Spin_Degree_',num2str(nStem_Spin_Degree_flag),'_',NumberTube,'-Stem_Spin_Degree_',num2str(Stem_Spin_Initial_Flag(1)),'_',NumberTube,'"  ',char(10)];
                    end
                    if nStem_Spin_Degree_flag>Stem_Spin_Initial_Flag(2)
                        StemSpin_62=['     .Angle "0", "0", "Stem_Spin_Degree_',num2str(nStem_Spin_Degree_flag),'_',NumberTube,'-Stem_Spin_Degree_',num2str(Stem_Spin_Initial_Flag(2)),'_',NumberTube,'"  ',char(10)];
                    end
                    if nStem_Spin_Degree_flag>Stem_Spin_Initial_Flag(3)
                        StemSpin_62=['     .Angle "0", "0", "Stem_Spin_Degree_',num2str(nStem_Spin_Degree_flag),'_',NumberTube,'-Stem_Spin_Degree_',num2str(Stem_Spin_Initial_Flag(3)),'_',NumberTube,'"  ',char(10)];
                    end
                end
                StemSpin_63=['     .MultipleObjects "True"  ',char(10)];
                StemSpin_64=['     .GroupObjects "False"  ',char(10)];
                StemSpin_65=['     .Repetitions "1"  ',char(10)];
                StemSpin_66=['     .MultipleSelection "False"  ',char(10)];
                StemSpin_67=['     .Destination ""  ',char(10)];
                StemSpin_68=['     .Material ""  ',char(10)];
                StemSpin_69=['     .Transform "Shape", "Rotate"  ',char(10)];
                StemSpin_70=['End With  ',char(10)];
                for i_StemSpin=0:70
                    NameStemSpin=['StemSpin_',num2str(i_StemSpin)];
                    fprintf(Fid,'%s',eval(NameStemSpin));
                end
                
        end
        
    end
end


Stem_Spin_Initial_Flag_COPY=find(Stem_Spin_Degree_Flag==2);
NStem_Spin_Initial_Flag_COPY=length(Stem_Spin_Initial_Flag_COPY);

if STEM_FLAG==1
    %%  STEM、LOFT连接成一个整体
    
    for nTube=2:Ntube-2
        if nTube<=9
            NumberTube=['00',num2str(nTube)];
        elseif nTube<=99
            NumberTube=['0',num2str(nTube)];
        else
            NumberTube=[num2str(nTube)];
        end
        if CStem_1_Flag==1
            STEM_1_Temp=['CStem_1_',NumberTube];
        else
            STEM_1_Temp=['Stem_1_',NumberTube];
        end
        if CStem_2_Flag==1
            STEM_2_Temp=['CStem_2_',NumberTube];
        else
            STEM_2_Temp=['Stem_2_',NumberTube];
        end
        if CStem_3_Flag==1
            STEM_3_Temp=['CStem_3_',NumberTube];
        else
            STEM_3_Temp=['Stem_3_',NumberTube];
        end
        if nTube==2
            Tadd_1=['Solid.Rename "component1:',STEM_1_Temp,'", "STEM"  ',char(10)];
            Tadd_2=['Solid.Add "component1:STEM','", "component1:',STEM_2_Temp,'" ',char(10)];
            Tadd_3=['Solid.Add "component1:STEM','", "component1:',STEM_3_Temp,'" ',char(10)];
            Tadd_4=['Solid.Add "component1:STEM','", "component1:Loft_12_',NumberTube,'" ',char(10)];
            Tadd_5=['Solid.Add "component1:STEM','", "component1:Loft_23_',NumberTube,'" ',char(10)];
            
            for i_Tadd=1:5
                NameTadd=['Tadd_',num2str(i_Tadd)];
                fprintf(Fid,'%s',eval(NameTadd));
            end
        else
            Tadd_1=['Solid.Add "component1:STEM','", "component1:',STEM_1_Temp,'" ',char(10)];
            Tadd_2=['Solid.Add "component1:STEM','", "component1:',STEM_2_Temp,'" ',char(10)];
            Tadd_3=['Solid.Add "component1:STEM','", "component1:',STEM_3_Temp,'" ',char(10)];
            Tadd_4=['Solid.Add "component1:STEM','", "component1:Loft_12_',NumberTube,'" ',char(10)];
            Tadd_5=['Solid.Add "component1:STEM','", "component1:Loft_23_',NumberTube,'" ',char(10)];
            
            for i_Tadd=1:5
                NameTadd=['Tadd_',num2str(i_Tadd)];
                fprintf(Fid,'%s',eval(NameTadd));
            end
        end
        
        
        if NStem_Spin_Initial_Flag_COPY>0
            for nStem_Spin_Initial_Flag_COPY=1:NStem_Spin_Initial_Flag_COPY
                Tadd_1=['Solid.Add "component1:STEM','", "component1:',STEM_1_Temp,'_',num2str(nStem_Spin_Initial_Flag_COPY),'" ',char(10)];
                Tadd_2=['Solid.Add "component1:STEM','", "component1:',STEM_2_Temp,'_',num2str(nStem_Spin_Initial_Flag_COPY),'" ',char(10)];
                Tadd_3=['Solid.Add "component1:STEM','", "component1:',STEM_3_Temp,'_',num2str(nStem_Spin_Initial_Flag_COPY),'" ',char(10)];
                Tadd_4=['Solid.Add "component1:STEM','", "component1:Loft_12_',NumberTube,'_',num2str(nStem_Spin_Initial_Flag_COPY),'" ',char(10)];
                Tadd_5=['Solid.Add "component1:STEM','", "component1:Loft_23_',NumberTube,'_',num2str(nStem_Spin_Initial_Flag_COPY),'" ',char(10)];
                
                for i_Tadd=1:5
                    NameTadd=['Tadd_',num2str(i_Tadd)];
                    fprintf(Fid,'%s',eval(NameTadd));
                end
                
            end
        end
    end
    
    %% 支撑杆减去留在漂移管中的部分。   STEM 是 一体的
    if Ntube-1<=9
        NumberTube=['00',num2str(Ntube-1)];
    elseif Ntube-1<=99
        NumberTube=['0',num2str(Ntube-1)];
    else
        NumberTube=num2str(Ntube-1);
    end
    SUB_1=['WCS.ActivateWCS "global" ',char(10)];
    SUB_2=['With Cylinder  ',char(10)];
    SUB_3=['     .Reset   ',char(10)];
    SUB_4=['     .Name "SolidTube"   ',char(10)];
    SUB_5=['     .Component "component1"   ',char(10)];
    SUB_6=['     .Material "Copper (hard-drawn)"   ',char(10)];
    SUB_7=['     .OuterRadius "Tube_R_Inner_',NumberTube,'"   ',char(10)];
    SUB_8=['     .InnerRadius "0"   ',char(10)];
    SUB_9=['     .Axis "z"   ',char(10)];
    SUB_10=['     .Zrange "Tube_Z_Begin_001",  "Tube_Z_End_',NumberTube,'"  ',char(10)];
    SUB_11=['     .Xcenter "0"   ',char(10)];
    SUB_12=['     .Ycenter "0"   ',char(10)];
    SUB_13=['     .Segments "0"   ',char(10)];
    SUB_14=['     .Create   ',char(10)];
    SUB_15=['End With   ',char(10)];
    SUB_16=['Solid.Subtract "component1:STEM", "component1:SolidTube"   ',char(10)];
    for i_SUB=1:16
        NameSUB=['SUB_',num2str(i_SUB)];
        fprintf(Fid,'%s',eval(NameSUB));
    end
    
else
    
    %% 支撑杆减去留在漂移管中的部分。   STEM 是 离散的
    for nTube=2:Ntube-2
        if nTube<=9
            NumberTube=['00',num2str(nTube)];
        elseif nTube<=99
            NumberTube=['0',num2str(nTube)];
        else
            NumberTube=[num2str(nTube)];
        end
        
        
        
        SUB_1=['WCS.ActivateWCS "global" ',char(10)];
        
        SUB_2=['With Cylinder  ',char(10)];
        SUB_3=['     .Reset   ',char(10)];
        SUB_4=['     .Name "SubTube_1_',NumberTube,'"   ',char(10)];
        SUB_5=['     .Component "component1"   ',char(10)];
        SUB_6=['     .Material "Copper (hard-drawn)"   ',char(10)];
        SUB_7=['     .OuterRadius "Tube_R_Inner_',NumberTube,'"   ',char(10)];
        SUB_8=['     .InnerRadius "0"   ',char(10)];
        SUB_9=['     .Axis "z"   ',char(10)];
        SUB_10=['     .Zrange "Tube_Z_Begin_',NumberTube,'",  "Tube_Z_End_',NumberTube,'"  ',char(10)];
        SUB_11=['     .Xcenter "0"   ',char(10)];
        SUB_12=['     .Ycenter "0"   ',char(10)];
        SUB_13=['     .Segments "0"   ',char(10)];
        SUB_14=['     .Create   ',char(10)];
        SUB_15=['End With   ',char(10)];
        
        
        
        SUB_16=['With Cylinder  ',char(10)];
        SUB_17=['     .Reset   ',char(10)];
        SUB_18=['     .Name "SubTube_2_',NumberTube,'"   ',char(10)];
        SUB_19=['     .Component "component1"   ',char(10)];
        SUB_20=['     .Material "Copper (hard-drawn)"   ',char(10)];
        SUB_21=['     .OuterRadius "Tube_R_Inner_',NumberTube,'"   ',char(10)];
        SUB_22=['     .InnerRadius "0"   ',char(10)];
        SUB_23=['     .Axis "z"   ',char(10)];
        SUB_24=['     .Zrange "Tube_Z_Begin_',NumberTube,'",  "Tube_Z_End_',NumberTube,'"  ',char(10)];
        SUB_25=['     .Xcenter "0"   ',char(10)];
        SUB_26=['     .Ycenter "0"   ',char(10)];
        SUB_27=['     .Segments "0"   ',char(10)];
        SUB_28=['     .Create   ',char(10)];
        SUB_29=['End With   ',char(10)];
        
        
        SUB_30=['With Cylinder  ',char(10)];
        SUB_31=['     .Reset   ',char(10)];
        SUB_32=['     .Name "SubTube_3_',NumberTube,'"   ',char(10)];
        SUB_33=['     .Component "component1"   ',char(10)];
        SUB_34=['     .Material "Copper (hard-drawn)"   ',char(10)];
        SUB_35=['     .OuterRadius "Tube_R_Inner_',NumberTube,'"   ',char(10)];
        SUB_36=['     .InnerRadius "0"   ',char(10)];
        SUB_37=['     .Axis "z"   ',char(10)];
        SUB_38=['     .Zrange "Tube_Z_Begin_',NumberTube,'",  "Tube_Z_End_',NumberTube,'"  ',char(10)];
        SUB_39=['     .Xcenter "0"   ',char(10)];
        SUB_40=['     .Ycenter "0"   ',char(10)];
        SUB_41=['     .Segments "0"   ',char(10)];
        SUB_42=['     .Create   ',char(10)];
        SUB_43=['End With   ',char(10)];
        
        SUB_44=['With Cylinder  ',char(10)];
        SUB_45=['     .Reset   ',char(10)];
        SUB_46=['     .Name "SubTube_4_',NumberTube,'"   ',char(10)];
        SUB_47=['     .Component "component1"   ',char(10)];
        SUB_48=['     .Material "Copper (hard-drawn)"   ',char(10)];
        SUB_49=['     .OuterRadius "Tube_R_Inner_',NumberTube,'"   ',char(10)];
        SUB_50=['     .InnerRadius "0"   ',char(10)];
        SUB_51=['     .Axis "z"   ',char(10)];
        SUB_52=['     .Zrange "Tube_Z_Begin_',NumberTube,'",  "Tube_Z_End_',NumberTube,'"  ',char(10)];
        SUB_53=['     .Xcenter "0"   ',char(10)];
        SUB_54=['     .Ycenter "0"   ',char(10)];
        SUB_55=['     .Segments "0"   ',char(10)];
        SUB_56=['     .Create   ',char(10)];
        SUB_57=['End With   ',char(10)];
        
        
        SUB_58=['With Cylinder  ',char(10)];
        SUB_59=['     .Reset   ',char(10)];
        SUB_60=['     .Name "SubTube_5_',NumberTube,'"   ',char(10)];
        SUB_61=['     .Component "component1"   ',char(10)];
        SUB_62=['     .Material "Copper (hard-drawn)"   ',char(10)];
        SUB_63=['     .OuterRadius "Tube_R_Inner_',NumberTube,'"   ',char(10)];
        SUB_64=['     .InnerRadius "0"   ',char(10)];
        SUB_65=['     .Axis "z"   ',char(10)];
        SUB_66=['     .Zrange "Tube_Z_Begin_',NumberTube,'",  "Tube_Z_End_',NumberTube,'"  ',char(10)];
        SUB_67=['     .Xcenter "0"   ',char(10)];
        SUB_68=['     .Ycenter "0"   ',char(10)];
        SUB_69=['     .Segments "0"   ',char(10)];
        SUB_70=['     .Create   ',char(10)];
        SUB_71=['End With   ',char(10)];
        
        
        
        
        
        if CStem_1_Flag==1
            SUB_72=['Solid.Subtract "component1:CStem_1_',NumberTube,'", "component1:SubTube_1_',NumberTube,'"   ',char(10)];
        else
            SUB_72=['Solid.Subtract "component1:Stem_1_',NumberTube,'", "component1:SubTube_1_',NumberTube,'"   ',char(10)];
        end
        
        if CStem_2_Flag==1
            SUB_73=['Solid.Subtract "component1:CStem_2_',NumberTube,'", "component1:SubTube_2_',NumberTube,'"   ',char(10)];
        else
            SUB_73=['Solid.Subtract "component1:Stem_2_',NumberTube,'", "component1:SubTube_2_',NumberTube,'"   ',char(10)];
        end
        
        if CStem_3_Flag==1
            SUB_74=['Solid.Subtract "component1:CStem_3_',NumberTube,'", "component1:SubTube_3_',NumberTube,'"   ',char(10)];
        else
            SUB_74=['Solid.Subtract "component1:Stem_3_',NumberTube,'", "component1:SubTube_3_',NumberTube,'"   ',char(10)];
        end
        
        SUB_75=['Solid.Subtract "component1:Loft_12_',NumberTube,'", "component1:SubTube_4_',NumberTube,'"   ',char(10)];
        SUB_76=['Solid.Subtract "component1:Loft_23_',NumberTube,'", "component1:SubTube_5_',NumberTube,'"   ',char(10)];
        
        
        
        
        for i_SUB=1:76
            NameSUB=['SUB_',num2str(i_SUB)];
            fprintf(Fid,'%s',eval(NameSUB));
        end
        
        
        %%
        
        if NStem_Spin_Initial_Flag_COPY>0
            for nStem_Spin_Initial_Flag_COPY=1:NStem_Spin_Initial_Flag_COPY
                
                
                SUB_1=['WCS.ActivateWCS "global" ',char(10)];
                
                SUB_2=['With Cylinder  ',char(10)];
                SUB_3=['     .Reset   ',char(10)];
                SUB_4=['     .Name "SubTube_1_',NumberTube,'"   ',char(10)];
                SUB_5=['     .Component "component1"   ',char(10)];
                SUB_6=['     .Material "Copper (hard-drawn)"   ',char(10)];
                SUB_7=['     .OuterRadius "Tube_R_Inner_',NumberTube,'"   ',char(10)];
                SUB_8=['     .InnerRadius "0"   ',char(10)];
                SUB_9=['     .Axis "z"   ',char(10)];
                SUB_10=['     .Zrange "Tube_Z_Begin_',NumberTube,'",  "Tube_Z_End_',NumberTube,'"  ',char(10)];
                SUB_11=['     .Xcenter "0"   ',char(10)];
                SUB_12=['     .Ycenter "0"   ',char(10)];
                SUB_13=['     .Segments "0"   ',char(10)];
                SUB_14=['     .Create   ',char(10)];
                SUB_15=['End With   ',char(10)];
                
                
                
                SUB_16=['With Cylinder  ',char(10)];
                SUB_17=['     .Reset   ',char(10)];
                SUB_18=['     .Name "SubTube_2_',NumberTube,'"   ',char(10)];
                SUB_19=['     .Component "component1"   ',char(10)];
                SUB_20=['     .Material "Copper (hard-drawn)"   ',char(10)];
                SUB_21=['     .OuterRadius "Tube_R_Inner_',NumberTube,'"   ',char(10)];
                SUB_22=['     .InnerRadius "0"   ',char(10)];
                SUB_23=['     .Axis "z"   ',char(10)];
                SUB_24=['     .Zrange "Tube_Z_Begin_',NumberTube,'",  "Tube_Z_End_',NumberTube,'"  ',char(10)];
                SUB_25=['     .Xcenter "0"   ',char(10)];
                SUB_26=['     .Ycenter "0"   ',char(10)];
                SUB_27=['     .Segments "0"   ',char(10)];
                SUB_28=['     .Create   ',char(10)];
                SUB_29=['End With   ',char(10)];
                
                
                SUB_30=['With Cylinder  ',char(10)];
                SUB_31=['     .Reset   ',char(10)];
                SUB_32=['     .Name "SubTube_3_',NumberTube,'"   ',char(10)];
                SUB_33=['     .Component "component1"   ',char(10)];
                SUB_34=['     .Material "Copper (hard-drawn)"   ',char(10)];
                SUB_35=['     .OuterRadius "Tube_R_Inner_',NumberTube,'"   ',char(10)];
                SUB_36=['     .InnerRadius "0"   ',char(10)];
                SUB_37=['     .Axis "z"   ',char(10)];
                SUB_38=['     .Zrange "Tube_Z_Begin_',NumberTube,'",  "Tube_Z_End_',NumberTube,'"  ',char(10)];
                SUB_39=['     .Xcenter "0"   ',char(10)];
                SUB_40=['     .Ycenter "0"   ',char(10)];
                SUB_41=['     .Segments "0"   ',char(10)];
                SUB_42=['     .Create   ',char(10)];
                SUB_43=['End With   ',char(10)];
                
                SUB_44=['With Cylinder  ',char(10)];
                SUB_45=['     .Reset   ',char(10)];
                SUB_46=['     .Name "SubTube_4_',NumberTube,'"   ',char(10)];
                SUB_47=['     .Component "component1"   ',char(10)];
                SUB_48=['     .Material "Copper (hard-drawn)"   ',char(10)];
                SUB_49=['     .OuterRadius "Tube_R_Inner_',NumberTube,'"   ',char(10)];
                SUB_50=['     .InnerRadius "0"   ',char(10)];
                SUB_51=['     .Axis "z"   ',char(10)];
                SUB_52=['     .Zrange "Tube_Z_Begin_',NumberTube,'",  "Tube_Z_End_',NumberTube,'"  ',char(10)];
                SUB_53=['     .Xcenter "0"   ',char(10)];
                SUB_54=['     .Ycenter "0"   ',char(10)];
                SUB_55=['     .Segments "0"   ',char(10)];
                SUB_56=['     .Create   ',char(10)];
                SUB_57=['End With   ',char(10)];
                
                
                SUB_58=['With Cylinder  ',char(10)];
                SUB_59=['     .Reset   ',char(10)];
                SUB_60=['     .Name "SubTube_5_',NumberTube,'"   ',char(10)];
                SUB_61=['     .Component "component1"   ',char(10)];
                SUB_62=['     .Material "Copper (hard-drawn)"   ',char(10)];
                SUB_63=['     .OuterRadius "Tube_R_Inner_',NumberTube,'"   ',char(10)];
                SUB_64=['     .InnerRadius "0"   ',char(10)];
                SUB_65=['     .Axis "z"   ',char(10)];
                SUB_66=['     .Zrange "Tube_Z_Begin_',NumberTube,'",  "Tube_Z_End_',NumberTube,'"  ',char(10)];
                SUB_67=['     .Xcenter "0"   ',char(10)];
                SUB_68=['     .Ycenter "0"   ',char(10)];
                SUB_69=['     .Segments "0"   ',char(10)];
                SUB_70=['     .Create   ',char(10)];
                SUB_71=['End With   ',char(10)];
                
                if CStem_1_Flag==1
                    SUB_72=['Solid.Subtract "component1:CStem_1_',NumberTube,'_',num2str(nStem_Spin_Initial_Flag_COPY),'", "component1:SubTube_1_',NumberTube,'"   ',char(10)];
                else
                    SUB_72=['Solid.Subtract "component1:Stem_1_',NumberTube,'_',num2str(nStem_Spin_Initial_Flag_COPY),'", "component1:SubTube_1_',NumberTube,'"   ',char(10)];
                end
                
                if CStem_2_Flag==1
                    SUB_73=['Solid.Subtract "component1:CStem_2_',NumberTube,'_',num2str(nStem_Spin_Initial_Flag_COPY),'", "component1:SubTube_2_',NumberTube,'"   ',char(10)];
                else
                    SUB_73=['Solid.Subtract "component1:Stem_2_',NumberTube,'_',num2str(nStem_Spin_Initial_Flag_COPY),'", "component1:SubTube_2_',NumberTube,'"   ',char(10)];
                end
                
                if CStem_3_Flag==1
                    SUB_74=['Solid.Subtract "component1:CStem_3_',NumberTube,'_',num2str(nStem_Spin_Initial_Flag_COPY),'", "component1:SubTube_3_',NumberTube,'"   ',char(10)];
                else
                    SUB_74=['Solid.Subtract "component1:Stem_3_',NumberTube,'_',num2str(nStem_Spin_Initial_Flag_COPY),'", "component1:SubTube_3_',NumberTube,'"   ',char(10)];
                end
                
                SUB_75=['Solid.Subtract "component1:Loft_12_',NumberTube,'_',num2str(nStem_Spin_Initial_Flag_COPY),'", "component1:SubTube_4_',NumberTube,'"   ',char(10)];
                SUB_76=['Solid.Subtract "component1:Loft_23_',NumberTube,'_',num2str(nStem_Spin_Initial_Flag_COPY),'", "component1:SubTube_5_',NumberTube,'"   ',char(10)];
                
                for i_SUB=1:76
                    NameSUB=['SUB_',num2str(i_SUB)];
                    fprintf(Fid,'%s',eval(NameSUB));
                end
                
            end
        end
        
        
        
        
        
    end
end

fclose(Fid);


if SIM_FLAG~=1
    %% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    %%   %%  %%  T型板
    
    StruT = xlsread('Struc.xlsx','T');
    [MStruT,NStruT]=size(StruT);
    
    fid=fopen(StruPara,'a+');
    
    StruT_Flag=StruT(:,1);
    StruT_Flag(StruT_Flag>=10)=floor(StruT_Flag(StruT_Flag>=10)/10);
    StruT_Flag(StruT_Flag<=-10)=ceil(StruT_Flag(StruT_Flag<=-10)/10);
    for iMStruT=1:MStruT
        iStruT_Flag=StruT_Flag(iMStruT);
        
        
        if iMStruT<=9
            NumberTube=['00',num2str(iMStruT)];
        elseif iMStruT<=99
            NumberTube=['0',num2str(iMStruT)];
        else
            NumberTube=[num2str(iMStruT)];
        end
        
        switch iStruT_Flag
            case 0
                
            case 1
                T_1=['T_UU_Xmin_',NumberTube,char(9),char(9),char(9),num2str(StruT(iMStruT,2)),char(9),char(13)];
                T_2=['T_UU_Xmax_',NumberTube,char(9),char(9),char(9),num2str(StruT(iMStruT,3)),char(9),char(13)];
                T_3=['T_UU_Ymin_',NumberTube,char(9),char(9),char(9),num2str(StruT(iMStruT,4)),char(9),char(13)];
                T_4=['T_UU_Ymax_',NumberTube,char(9),char(9),char(9),num2str(StruT(iMStruT,5)),char(9),char(13)];
                T_5=['T_UU_Zmin_',NumberTube,char(9),char(9),char(9),num2str(StruT(iMStruT,6)),char(9),char(13)];
                T_6=['T_UU_Zmax_',NumberTube,char(9),char(9),char(9),num2str(StruT(iMStruT,7)),char(9),char(13)];
                
                for i_T=1:6
                    NameT=['T_',num2str(i_T)];
                    fprintf(fid,'%s',eval(NameT));
                end
                
            case -1
                T_1=['T_DD_Xmin_',NumberTube,char(9),char(9),char(9),num2str(StruT(iMStruT,2)),char(9),char(13)];
                T_2=['T_DD_Xmax_',NumberTube,char(9),char(9),char(9),num2str(StruT(iMStruT,3)),char(9),char(13)];
                T_3=['T_DD_Ymin_',NumberTube,char(9),char(9),char(9),num2str(StruT(iMStruT,4)),char(9),char(13)];
                T_4=['T_DD_Ymax_',NumberTube,char(9),char(9),char(9),num2str(StruT(iMStruT,5)),char(9),char(13)];
                T_5=['T_DD_Zmin_',NumberTube,char(9),char(9),char(9),num2str(StruT(iMStruT,6)),char(9),char(13)];
                T_6=['T_DD_Zmax_',NumberTube,char(9),char(9),char(9),num2str(StruT(iMStruT,7)),char(9),char(13)];
                
                for i_T=1:6
                    NameT=['T_',num2str(i_T)];
                    fprintf(fid,'%s',eval(NameT));
                end
                
            case 2
                T_1=['T_UD_Xmin_',NumberTube,char(9),char(9),char(9),num2str(StruT(iMStruT,2)),char(9),char(13)];
                T_2=['T_UD_Xmax_',NumberTube,char(9),char(9),char(9),num2str(StruT(iMStruT,3)),char(9),char(13)];
                T_3=['T_UD_Ymin_',NumberTube,char(9),char(9),char(9),num2str(StruT(iMStruT,4)),char(9),char(13)];
                T_4=['T_UD_Ymax_',NumberTube,char(9),char(9),char(9),num2str(StruT(iMStruT,5)),char(9),char(13)];
                T_5=['T_UD_Zmin_',NumberTube,char(9),char(9),char(9),num2str(StruT(iMStruT,6)),char(9),char(13)];
                T_6=['T_UD_Zmax_',NumberTube,char(9),char(9),char(9),num2str(StruT(iMStruT,7)),char(9),char(13)];
                for i_T=1:6
                    NameT=['T_',num2str(i_T)];
                    fprintf(fid,'%s',eval(NameT));
                end
                
            case -2
                T_1=['T_DU_Xmin_',NumberTube,char(9),char(9),char(9),num2str(StruT(iMStruT,2)),char(9),char(13)];
                T_2=['T_DU_Xmax_',NumberTube,char(9),char(9),char(9),num2str(StruT(iMStruT,3)),char(9),char(13)];
                T_3=['T_DU_Ymin_',NumberTube,char(9),char(9),char(9),num2str(StruT(iMStruT,4)),char(9),char(13)];
                T_4=['T_DU_Ymax_',NumberTube,char(9),char(9),char(9),num2str(StruT(iMStruT,5)),char(9),char(13)];
                T_5=['T_DU_Zmin_',NumberTube,char(9),char(9),char(9),num2str(StruT(iMStruT,6)),char(9),char(13)];
                T_6=['T_DU_Zmax_',NumberTube,char(9),char(9),char(9),num2str(StruT(iMStruT,7)),char(9),char(13)];
                for i_T=1:6
                    NameT=['T_',num2str(i_T)];
                    fprintf(fid,'%s',eval(NameT));
                end
            case 3
                
                T_1=['T_UU_Cut_Xmin_',NumberTube,char(9),char(9),char(9),num2str(StruT(StruT_Flag==1,2)*10),char(9),char(13)];
                T_2=['T_UU_Cut_Xmax_',NumberTube,char(9),char(9),char(9),num2str(StruT(StruT_Flag==1,3)*10),char(9),char(13)];
                T_3=['T_UU_Cut_Ymin_',NumberTube,char(9),char(9),char(9),num2str(StruT(iMStruT,2)),char(9),char(13)];
                T_4=['T_UU_Cut_Ymax_',NumberTube,char(9),char(9),char(9),num2str(StruT(iMStruT,3)),char(9),char(13)];
                T_5=['T_UU_Cut_U_Zmin_',NumberTube,char(9),char(9),char(9),num2str(StruT(iMStruT,4)),char(9),char(13)];
                T_6=['T_UU_Cut_U_Zmax_',NumberTube,char(9),char(9),char(9),num2str(StruT(iMStruT,5)),char(9),char(13)];
                T_7=['T_UU_Cut_D_Zmin_',NumberTube,char(9),char(9),char(9),num2str(StruT(iMStruT,6)),char(9),char(13)];
                T_8=['T_UU_Cut_D_Zmax_',NumberTube,char(9),char(9),char(9),num2str(StruT(iMStruT,7)),char(9),char(13)];
                for i_T=1:8
                    NameT=['T_',num2str(i_T)];
                    fprintf(fid,'%s',eval(NameT));
                end
            case -3
                
                T_1=['T_DU_Cut_Xmin_',NumberTube,char(9),char(9),char(9),num2str(StruT(StruT_Flag==-1,2)*10),char(9),char(13)];
                T_2=['T_DU_Cut_Xmax_',NumberTube,char(9),char(9),char(9),num2str(StruT(StruT_Flag==-1,3)*10),char(9),char(13)];
                T_3=['T_DU_Cut_Ymin_',NumberTube,char(9),char(9),char(9),num2str(StruT(iMStruT,2)),char(9),char(13)];
                T_4=['T_DU_Cut_Ymax_',NumberTube,char(9),char(9),char(9),num2str(StruT(iMStruT,3)),char(9),char(13)];
                T_5=['T_DU_Cut_U_Zmin_',NumberTube,char(9),char(9),char(9),num2str(StruT(iMStruT,4)),char(9),char(13)];
                T_6=['T_DU_Cut_U_Zmax_',NumberTube,char(9),char(9),char(9),num2str(StruT(iMStruT,5)),char(9),char(13)];
                T_7=['T_DU_Cut_D_Zmin_',NumberTube,char(9),char(9),char(9),num2str(StruT(iMStruT,6)),char(9),char(13)];
                T_8=['T_DU_Cut_D_Zmax_',NumberTube,char(9),char(9),char(9),num2str(StruT(iMStruT,7)),char(9),char(13)];
                for i_T=1:8
                    NameT=['T_',num2str(i_T)];
                    fprintf(fid,'%s',eval(NameT));
                end
            case 4
                T_1=['T_UD_Cut_Xmin_',NumberTube,char(9),char(9),char(9),num2str(StruT(StruT_Flag==1,2)*10),char(9),char(13)];
                T_2=['T_UD_Cut_Xmax_',NumberTube,char(9),char(9),char(9),num2str(StruT(StruT_Flag==1,3)*10),char(9),char(13)];
                T_3=['T_UD_Cut_Ymin_',NumberTube,char(9),char(9),char(9),num2str(StruT(iMStruT,2)),char(9),char(13)];
                T_4=['T_UD_Cut_Ymax_',NumberTube,char(9),char(9),char(9),num2str(StruT(iMStruT,3)),char(9),char(13)];
                T_5=['T_UD_Cut_U_Zmin_',NumberTube,char(9),char(9),char(9),num2str(StruT(iMStruT,4)),char(9),char(13)];
                T_6=['T_UD_Cut_U_Zmax_',NumberTube,char(9),char(9),char(9),num2str(StruT(iMStruT,5)),char(9),char(13)];
                T_7=['T_UD_Cut_D_Zmin_',NumberTube,char(9),char(9),char(9),num2str(StruT(iMStruT,6)),char(9),char(13)];
                T_8=['T_UD_Cut_D_Zmax_',NumberTube,char(9),char(9),char(9),num2str(StruT(iMStruT,7)),char(9),char(13)];
                for i_T=1:8
                    NameT=['T_',num2str(i_T)];
                    fprintf(fid,'%s',eval(NameT));
                end
            case -4
                T_1=['T_DD_Cut_Xmin_',NumberTube,char(9),char(9),char(9),num2str(StruT(StruT_Flag==-1,2)*10),char(9),char(13)];
                T_2=['T_DD_Cut_Xmax_',NumberTube,char(9),char(9),char(9),num2str(StruT(StruT_Flag==-1,3)*10),char(9),char(13)];
                T_3=['T_DD_Cut_Ymin_',NumberTube,char(9),char(9),char(9),num2str(StruT(iMStruT,2)),char(9),char(13)];
                T_4=['T_DD_Cut_Ymax_',NumberTube,char(9),char(9),char(9),num2str(StruT(iMStruT,3)),char(9),char(13)];
                T_5=['T_DD_Cut_U_Zmin_',NumberTube,char(9),char(9),char(9),num2str(StruT(iMStruT,4)),char(9),char(13)];
                T_6=['T_DD_Cut_U_Zmax_',NumberTube,char(9),char(9),char(9),num2str(StruT(iMStruT,5)),char(9),char(13)];
                T_7=['T_DD_Cut_D_Zmin_',NumberTube,char(9),char(9),char(9),num2str(StruT(iMStruT,6)),char(9),char(13)];
                T_8=['T_DD_Cut_D_Zmax_',NumberTube,char(9),char(9),char(9),num2str(StruT(iMStruT,7)),char(9),char(13)];
                for i_T=1:8
                    NameT=['T_',num2str(i_T)];
                    fprintf(fid,'%s',eval(NameT));
                end
        end
    end
    
    fclose(fid);
    
    
    %%  %%%%
    Fid=fopen(StruVBA,'a+');
    
    for iMStruT=1:MStruT
        iStruT_Flag=StruT_Flag(iMStruT);
        
        
        if iMStruT<=9
            NumberTube=['00',num2str(iMStruT)];
        elseif iMStruT<=99
            NumberTube=['0',num2str(iMStruT)];
        else
            NumberTube=[num2str(iMStruT)];
        end
        
        switch iStruT_Flag
            case 0
                
            case 1
                T_1=['With Brick  ',char(10)];
                T_2=['     .Reset   ',char(10)];
                T_3=['     .Name "T_UU_1"   ',char(10)];
                T_4=['     .Component "component1"   ',char(10)];
                T_5=['     .Material "Copper (hard-drawn)"   ',char(10)];
                T_6=['     .Xrange "T_UU_Xmin_',NumberTube,'", "T_UU_Xmax_',NumberTube,'"   ',char(10)];
                T_7=['     .Yrange "T_UU_Ymin_',NumberTube,'", "T_UU_Ymax_',NumberTube,'"   ',char(10)];
                T_8=['     .Zrange "T_UU_Zmin_',NumberTube,'", "T_UU_Zmax_',NumberTube,'"   ',char(10)];
                T_9=['     .Create  ',char(10)];
                T_10=['End With  ',char(10)];
                
                for i_T=1:10
                    NameT=['T_',num2str(i_T)];
                    fprintf(Fid,'%s',eval(NameT));
                end
                
            case -1
                T_1=['With Brick  ',char(10)];
                T_2=['     .Reset   ',char(10)];
                T_3=['     .Name "T_DD_1"   ',char(10)];
                T_4=['     .Component "component1"   ',char(10)];
                T_5=['     .Material "Copper (hard-drawn)"   ',char(10)];
                T_6=['     .Xrange "T_DD_Xmin_',NumberTube,'", "T_DD_Xmax_',NumberTube,'"   ',char(10)];
                T_7=['     .Yrange "T_DD_Ymin_',NumberTube,'", "T_DD_Ymax_',NumberTube,'"   ',char(10)];
                T_8=['     .Zrange "T_DD_Zmin_',NumberTube,'", "T_DD_Zmax_',NumberTube,'"   ',char(10)];
                T_9=['     .Create  ',char(10)];
                T_10=['End With  ',char(10)];
                
                for i_T=1:10
                    NameT=['T_',num2str(i_T)];
                    fprintf(Fid,'%s',eval(NameT));
                end
                
            case 2
                T_1=['With Brick  ',char(10)];
                T_2=['     .Reset   ',char(10)];
                T_3=['     .Name "T_UD_1"   ',char(10)];
                T_4=['     .Component "component1"   ',char(10)];
                T_5=['     .Material "Copper (hard-drawn)"   ',char(10)];
                T_6=['     .Xrange "T_UD_Xmin_',NumberTube,'", "T_UD_Xmax_',NumberTube,'"   ',char(10)];
                T_7=['     .Yrange "T_UD_Ymin_',NumberTube,'", "T_UD_Ymax_',NumberTube,'"   ',char(10)];
                T_8=['     .Zrange "T_UD_Zmin_',NumberTube,'", "T_UD_Zmax_',NumberTube,'"   ',char(10)];
                T_9=['     .Create  ',char(10)];
                T_10=['End With  ',char(10)];
                
                for i_T=1:10
                    NameT=['T_',num2str(i_T)];
                    fprintf(Fid,'%s',eval(NameT));
                end
                
            case -2
                T_1=['With Brick  ',char(10)];
                T_2=['     .Reset   ',char(10)];
                T_3=['     .Name "T_DU_1"   ',char(10)];
                T_4=['     .Component "component1"   ',char(10)];
                T_5=['     .Material "Copper (hard-drawn)"   ',char(10)];
                T_6=['     .Xrange "T_DU_Xmin_',NumberTube,'", "T_DU_Xmax_',NumberTube,'"   ',char(10)];
                T_7=['     .Yrange "T_DU_Ymin_',NumberTube,'", "T_DU_Ymax_',NumberTube,'"   ',char(10)];
                T_8=['     .Zrange "T_DU_Zmin_',NumberTube,'", "T_DU_Zmax_',NumberTube,'"   ',char(10)];
                T_9=['     .Create  ',char(10)];
                T_10=['End With  ',char(10)];
                
                for i_T=1:10
                    NameT=['T_',num2str(i_T)];
                    fprintf(Fid,'%s',eval(NameT));
                end
                
            case 3
                T_1=['With Brick  ',char(10)];
                T_2=['     .Reset   ',char(10)];
                T_3=['     .Name "T_UU_Cut_U_',NumberTube,'"   ',char(10)];
                T_4=['     .Component "component1"   ',char(10)];
                T_5=['     .Material "Copper (hard-drawn)"   ',char(10)];
                T_6=['     .Xrange "T_UU_Cut_Xmin_',NumberTube,'", "T_UU_Cut_Xmax_',NumberTube,'"   ',char(10)];
                T_7=['     .Yrange "T_UU_Cut_Ymax_',NumberTube,'-1", "T_UU_Cut_Ymax_',NumberTube,'"   ',char(10)];
                T_8=['     .Zrange "T_UU_Cut_U_Zmin_',NumberTube,'", "T_UU_Cut_U_Zmax_',NumberTube,'"   ',char(10)];
                T_9=['     .Create  ',char(10)];
                T_10=['End With  ',char(10)];
                
                T_11=['With Brick  ',char(10)];
                T_12=['     .Reset   ',char(10)];
                T_13=['     .Name "T_UU_Cut_D_',NumberTube,'"   ',char(10)];
                T_14=['     .Component "component1"   ',char(10)];
                T_15=['     .Material "Copper (hard-drawn)"   ',char(10)];
                T_16=['     .Xrange "T_UU_Cut_Xmin_',NumberTube,'", "T_UU_Cut_Xmax_',NumberTube,'"   ',char(10)];
                T_17=['     .Yrange "T_UU_Cut_Ymin_',NumberTube,'", "T_UU_Cut_Ymin_',NumberTube,'+1"   ',char(10)];
                T_18=['     .Zrange "T_UU_Cut_D_Zmin_',NumberTube,'", "T_UU_Cut_D_Zmax_',NumberTube,'"   ',char(10)];
                T_19=['     .Create  ',char(10)];
                T_20=['End With  ',char(10)];
                
                for i_T=1:20
                    NameT=['T_',num2str(i_T)];
                    fprintf(Fid,'%s',eval(NameT));
                end
                
                
                
            case -3
                T_1=['With Brick  ',char(10)];
                T_2=['     .Reset   ',char(10)];
                T_3=['     .Name "T_DU_Cut_U_',NumberTube,'"   ',char(10)];
                T_4=['     .Component "component1"   ',char(10)];
                T_5=['     .Material "Copper (hard-drawn)"   ',char(10)];
                T_6=['     .Xrange "T_DU_Cut_Xmin_',NumberTube,'", "T_DU_Cut_Xmax_',NumberTube,'"   ',char(10)];
                T_7=['     .Yrange "T_DU_Cut_Ymax_',NumberTube,'-1", "T_DU_Cut_Ymax_',NumberTube,'"   ',char(10)];
                T_8=['     .Zrange "T_DU_Cut_U_Zmin_',NumberTube,'", "T_DU_Cut_U_Zmax_',NumberTube,'"   ',char(10)];
                T_9=['     .Create  ',char(10)];
                T_10=['End With  ',char(10)];
                
                T_11=['With Brick  ',char(10)];
                T_12=['     .Reset   ',char(10)];
                T_13=['     .Name "T_DU_Cut_D_',NumberTube,'"   ',char(10)];
                T_14=['     .Component "component1"   ',char(10)];
                T_15=['     .Material "Copper (hard-drawn)"   ',char(10)];
                T_16=['     .Xrange "T_DU_Cut_Xmin_',NumberTube,'", "T_DU_Cut_Xmax_',NumberTube,'"   ',char(10)];
                T_17=['     .Yrange "T_DU_Cut_Ymin_',NumberTube,'", "T_DU_Cut_Ymin_',NumberTube,'+1"   ',char(10)];
                T_18=['     .Zrange "T_DU_Cut_D_Zmin_',NumberTube,'", "T_DU_Cut_D_Zmax_',NumberTube,'"   ',char(10)];
                T_19=['     .Create  ',char(10)];
                T_20=['End With  ',char(10)];
                
                for i_T=1:20
                    NameT=['T_',num2str(i_T)];
                    fprintf(Fid,'%s',eval(NameT));
                end
                
            case 4
                T_1=['With Brick  ',char(10)];
                T_2=['     .Reset   ',char(10)];
                T_3=['     .Name "T_UD_Cut_U_',NumberTube,'"   ',char(10)];
                T_4=['     .Component "component1"   ',char(10)];
                T_5=['     .Material "Copper (hard-drawn)"   ',char(10)];
                T_6=['     .Xrange "T_UD_Cut_Xmin_',NumberTube,'", "T_UD_Cut_Xmax_',NumberTube,'"   ',char(10)];
                T_7=['     .Yrange "T_UD_Cut_Ymax_',NumberTube,'-1", "T_UD_Cut_Ymax_',NumberTube,'"   ',char(10)];
                T_8=['     .Zrange "T_UD_Cut_U_Zmin_',NumberTube,'", "T_UD_Cut_U_Zmax_',NumberTube,'"   ',char(10)];
                T_9=['     .Create  ',char(10)];
                T_10=['End With  ',char(10)];
                
                T_11=['With Brick  ',char(10)];
                T_12=['     .Reset   ',char(10)];
                T_13=['     .Name "T_UD_Cut_D_',NumberTube,'"   ',char(10)];
                T_14=['     .Component "component1"   ',char(10)];
                T_15=['     .Material "Copper (hard-drawn)"   ',char(10)];
                T_16=['     .Xrange "T_UD_Cut_Xmin_',NumberTube,'", "T_UD_Cut_Xmax_',NumberTube,'"   ',char(10)];
                T_17=['     .Yrange "T_UD_Cut_Ymin_',NumberTube,'", "T_UD_Cut_Ymin_',NumberTube,'+1"   ',char(10)];
                T_18=['     .Zrange "T_UD_Cut_D_Zmin_',NumberTube,'", "T_UD_Cut_D_Zmax_',NumberTube,'"   ',char(10)];
                T_19=['     .Create  ',char(10)];
                T_20=['End With  ',char(10)];
                
                for i_T=1:20
                    NameT=['T_',num2str(i_T)];
                    fprintf(Fid,'%s',eval(NameT));
                end
                
            case -4
                T_1=['With Brick  ',char(10)];
                T_2=['     .Reset   ',char(10)];
                T_3=['     .Name "T_DD_Cut_U_',NumberTube,'"   ',char(10)];
                T_4=['     .Component "component1"   ',char(10)];
                T_5=['     .Material "Copper (hard-drawn)"   ',char(10)];
                T_6=['     .Xrange "T_DD_Cut_Xmin_',NumberTube,'", "T_DD_Cut_Xmax_',NumberTube,'"   ',char(10)];
                T_7=['     .Yrange "T_DD_Cut_Ymax_',NumberTube,'-1", "T_DD_Cut_Ymax_',NumberTube,'"   ',char(10)];
                T_8=['     .Zrange "T_DD_Cut_U_Zmin_',NumberTube,'", "T_DD_Cut_U_Zmax_',NumberTube,'"   ',char(10)];
                T_9=['     .Create  ',char(10)];
                T_10=['End With  ',char(10)];
                
                T_11=['With Brick  ',char(10)];
                T_12=['     .Reset   ',char(10)];
                T_13=['     .Name "T_DD_Cut_D_',NumberTube,'"   ',char(10)];
                T_14=['     .Component "component1"   ',char(10)];
                T_15=['     .Material "Copper (hard-drawn)"   ',char(10)];
                T_16=['     .Xrange "T_DD_Cut_Xmin_',NumberTube,'", "T_DD_Cut_Xmax_',NumberTube,'"   ',char(10)];
                T_17=['     .Yrange "T_DD_Cut_Ymin_',NumberTube,'", "T_DD_Cut_Ymin_',NumberTube,'+1"   ',char(10)];
                T_18=['     .Zrange "T_DD_Cut_D_Zmin_',NumberTube,'", "T_DD_Cut_D_Zmax_',NumberTube,'"   ',char(10)];
                T_19=['     .Create  ',char(10)];
                T_20=['End With  ',char(10)];
                
                for i_T=1:20
                    NameT=['T_',num2str(i_T)];
                    fprintf(Fid,'%s',eval(NameT));
                end
        end
    end
    
    
    
    %%   %%%%%%%   T型板 LOFT
    
    T_1=['Pick.PickFaceFromId "component1:T_UU_1", "3"  ',char(10)];
    T_2=['Pick.PickFaceFromId "component1:T_UD_1", "5"  ',char(10)];
    T_3=['With Loft  ',char(10)];
    T_4=['     .Reset  ',char(10)];
    T_5=['     .Name "T_U_1"  ',char(10)];
    T_6=['     .Component "component1"  ',char(10)];
    T_7=['     .Material "Copper (hard-drawn)"  ',char(10)];
    T_8=['     .Tangency "0.0"  ',char(10)];
    T_9=['     .CreateNew  ',char(10)];
    T_10=['End With  ',char(10)];
    
    T_11=['Pick.PickFaceFromId "component1:T_DU_1", "3"  ',char(10)];
    T_12=['Pick.PickFaceFromId "component1:T_DD_1", "5"  ',char(10)];
    T_13=['With Loft  ',char(10)];
    T_14=['     .Reset  ',char(10)];
    T_15=['     .Name "T_D_1"  ',char(10)];
    T_16=['     .Component "component1"  ',char(10)];
    T_17=['     .Material "Copper (hard-drawn)"  ',char(10)];
    T_18=['     .Tangency "0.0"  ',char(10)];
    T_19=['     .CreateNew  ',char(10)];
    T_20=['End With  ',char(10)];
    T_21=['Solid.Add "component1:T_U_1", "component1:T_UU_1" ',char(10)];
    T_22=['Solid.Add "component1:T_U_1", "component1:T_UD_1"  ',char(10)];
    T_23=['Solid.Add "component1:T_D_1", "component1:T_DU_1" ',char(10)];
    T_24=['Solid.Add "component1:T_D_1", "component1:T_DD_1"  ',char(10)];
    T_25=['Solid.Add "component1:T_U_1", "component1:T_D_1"  ',char(10)];
    T_26=['Solid.Rename "component1:T_U_1", "T"  ',char(10)];
    
    
    for i_T=1:26
        NameT=['T_',num2str(i_T)];
        fprintf(Fid,'%s',eval(NameT));
    end
    
    
    
    
    
    
    for iMStruT=1:MStruT
        iStruT_Flag=StruT_Flag(iMStruT);
        
        
        if iMStruT<=9
            NumberTube=['00',num2str(iMStruT)];
        elseif iMStruT<=99
            NumberTube=['0',num2str(iMStruT)];
        else
            NumberTube=[num2str(iMStruT)];
        end
        
        switch iStruT_Flag
            
            case 3
                T_1=['Pick.PickFaceFromId "component1:T_UU_Cut_U_',NumberTube,'", "3"  ',char(10)];
                T_2=['Pick.PickFaceFromId "component1:T_UU_Cut_D_',NumberTube,'", "5"  ',char(10)];
                T_3=['With Loft  ',char(10)];
                T_4=['     .Reset  ',char(10)];
                T_5=['     .Name "T_UU_Cut_',NumberTube,'"  ',char(10)];
                T_6=['     .Component "component1"  ',char(10)];
                T_7=['     .Material "Copper (hard-drawn)"  ',char(10)];
                T_8=['     .Tangency "0.0"  ',char(10)];
                T_9=['     .CreateNew  ',char(10)];
                T_10=['End With  ',char(10)];
                
                T_11=['Solid.Subtract "component1:T", "component1:T_UU_Cut_U_',NumberTube,'"   ',char(10)];
                T_12=['Solid.Subtract "component1:T", "component1:T_UU_Cut_D_',NumberTube,'"   ',char(10)];
                T_13=['Solid.Subtract "component1:T", "component1:T_UU_Cut_',NumberTube,'"   ',char(10)];
                
                for i_T=1:13
                    NameT=['T_',num2str(i_T)];
                    fprintf(Fid,'%s',eval(NameT));
                end
                
            case -3
                T_1=['Pick.PickFaceFromId "component1:T_DU_Cut_U_',NumberTube,'", "3"  ',char(10)];
                T_2=['Pick.PickFaceFromId "component1:T_DU_Cut_D_',NumberTube,'", "5"  ',char(10)];
                T_3=['With Loft  ',char(10)];
                T_4=['     .Reset  ',char(10)];
                T_5=['     .Name "T_DU_Cut_',NumberTube,'"  ',char(10)];
                T_6=['     .Component "component1"  ',char(10)];
                T_7=['     .Material "Copper (hard-drawn)"  ',char(10)];
                T_8=['     .Tangency "0.0"  ',char(10)];
                T_9=['     .CreateNew  ',char(10)];
                T_10=['End With  ',char(10)];
                
                T_11=['Solid.Subtract "component1:T", "component1:T_DU_Cut_U_',NumberTube,'"   ',char(10)];
                T_12=['Solid.Subtract "component1:T", "component1:T_DU_Cut_D_',NumberTube,'"   ',char(10)];
                T_13=['Solid.Subtract "component1:T", "component1:T_DU_Cut_',NumberTube,'"   ',char(10)];
                
                for i_T=1:13
                    NameT=['T_',num2str(i_T)];
                    fprintf(Fid,'%s',eval(NameT));
                end
                
            case 4
                T_1=['Pick.PickFaceFromId "component1:T_UD_Cut_U_',NumberTube,'", "3"  ',char(10)];
                T_2=['Pick.PickFaceFromId "component1:T_UD_Cut_D_',NumberTube,'", "5"  ',char(10)];
                T_3=['With Loft  ',char(10)];
                T_4=['     .Reset  ',char(10)];
                T_5=['     .Name "T_UD_Cut_',NumberTube,'"  ',char(10)];
                T_6=['     .Component "component1"  ',char(10)];
                T_7=['     .Material "Copper (hard-drawn)"  ',char(10)];
                T_8=['     .Tangency "0.0"  ',char(10)];
                T_9=['     .CreateNew  ',char(10)];
                T_10=['End With  ',char(10)];
                
                T_11=['Solid.Subtract "component1:T", "component1:T_UD_Cut_U_',NumberTube,'"   ',char(10)];
                T_12=['Solid.Subtract "component1:T", "component1:T_UD_Cut_D_',NumberTube,'"   ',char(10)];
                T_13=['Solid.Subtract "component1:T", "component1:T_UD_Cut_',NumberTube,'"   ',char(10)];
                
                for i_T=1:13
                    NameT=['T_',num2str(i_T)];
                    fprintf(Fid,'%s',eval(NameT));
                end
                
                
            case -4
                T_1=['Pick.PickFaceFromId "component1:T_DD_Cut_U_',NumberTube,'", "3"  ',char(10)];
                T_2=['Pick.PickFaceFromId "component1:T_DD_Cut_D_',NumberTube,'", "5"  ',char(10)];
                T_3=['With Loft  ',char(10)];
                T_4=['     .Reset  ',char(10)];
                T_5=['     .Name "T_DD_Cut_',NumberTube,'"  ',char(10)];
                T_6=['     .Component "component1"  ',char(10)];
                T_7=['     .Material "Copper (hard-drawn)"  ',char(10)];
                T_8=['     .Tangency "0.0"  ',char(10)];
                T_9=['     .CreateNew  ',char(10)];
                T_10=['End With  ',char(10)];
                
                T_11=['Solid.Subtract "component1:T", "component1:T_DD_Cut_U_',NumberTube,'"   ',char(10)];
                T_12=['Solid.Subtract "component1:T", "component1:T_DD_Cut_D_',NumberTube,'"   ',char(10)];
                T_13=['Solid.Subtract "component1:T", "component1:T_DD_Cut_',NumberTube,'"   ',char(10)];
                
                for i_T=1:13
                    NameT=['T_',num2str(i_T)];
                    fprintf(Fid,'%s',eval(NameT));
                end
        end
    end
    
    
    %%        %%%%%%%%%   把Tube全加起来
    
    for nTube=2:Ntube-1
        if nTube<=9
            NumberTube=['00',num2str(nTube)];
        elseif nTube<=99
            NumberTube=['0',num2str(nTube)];
        else
            NumberTube=[num2str(nTube)];
        end
        Tadd_1=['Solid.Add "component1:Tube_001','", "component1:Tube_',NumberTube,'" ',char(10)];
        fprintf(Fid,'%s',Tadd_1);
    end
    
    Tadd_2=['Solid.Rename "component1:Tube_001", "Tube"  ',char(10)];
    fprintf(Fid,'%s',Tadd_2);
    
    if  Tube_Blend_Outer_Flag~=1
        for nTube=2:Ntube-1
            if nTube<=9
                NumberTube=['00',num2str(nTube)];
            elseif nTube<=99
                NumberTube=['0',num2str(nTube)];
            else
                NumberTube=num2str(nTube);
            end
            Tadd_1=['Solid.Add "component1:Tube','", "component1:EarLeft_',NumberTube,'" ',char(10)];
            fprintf(Fid,'%s',Tadd_1);
        end
        for nTube=1:Ntube-2
            if nTube<=9
                NumberTube=['00',num2str(nTube)];
            elseif nTube<=99
                NumberTube=['0',num2str(nTube)];
            else
                NumberTube=num2str(nTube);
            end
            Tadd_1=['Solid.Add "component1:Tube','", "component1:EarRight_',NumberTube,'" ',char(10)];
            fprintf(Fid,'%s',Tadd_1);
        end
        
    end
    
    fclose(Fid);
    %% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    
    
else
    %% %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    %%   %%  %%  T型板
    
    StruT = xlsread('Struc.xlsx','TSim');
    [MStruT,NStruT]=size(StruT);
    
    fid=fopen(StruPara,'a+');
    
    StruTT_Flag=StruT(:,1);
    StruTT_Flag(StruTT_Flag>=10)=floor(StruTT_Flag(StruTT_Flag>=10)/10);
    StruTT_Flag(StruTT_Flag<=-10)=ceil(StruTT_Flag(StruTT_Flag<=-10)/10);
    for iMStruT=1:MStruT
        iStruTT_Flag=StruTT_Flag(iMStruT);
        
        
        if iMStruT<=9
            NumberTube=['00',num2str(iMStruT)];
        elseif iMStruT<=99
            NumberTube=['0',num2str(iMStruT)];
        else
            NumberTube=[num2str(iMStruT)];
        end
        
        switch iStruTT_Flag
            case 1
                
                TT_1=['TT_UU_Xmin',char(9),char(9),char(9),num2str(StruT(iMStruT,2)),char(9),char(13)];
                TT_2=['TT_UU_Xmax',char(9),char(9),char(9),num2str(StruT(iMStruT,3)),char(9),char(13)];
                TT_3=['TT_UU_Ymin',char(9),char(9),char(9),num2str(StruT(iMStruT,4)),char(9),char(13)];
                TT_4=['TT_UU_Ymax',char(9),char(9),char(9),num2str(StruT(iMStruT,5)),char(9),char(13)];
                TT_5=['TT_UU_Zmin',char(9),char(9),char(9),num2str(StruT(iMStruT,6)),char(9),char(13)];
                TT_6=['TT_UU_Zmax',char(9),char(9),char(9),num2str(StruT(iMStruT,7)),char(9),char(13)];
                
                
                
                for i_T=1:6
                    NameT=['TT_',num2str(i_T)];
                    fprintf(fid,'%s',eval(NameT));
                end
                
            case 2
                TT_1=['TT_UD_Xmin',char(9),char(9),char(9),num2str(StruT(iMStruT,2)),char(9),char(13)];
                TT_2=['TT_UD_Xmax',char(9),char(9),char(9),num2str(StruT(iMStruT,3)),char(9),char(13)];
                TT_3=['TT_UD_Ymin',char(9),char(9),char(9),num2str(StruT(iMStruT,4)),char(9),char(13)];
                TT_4=['TT_UD_Ymax',char(9),char(9),char(9),num2str(StruT(iMStruT,5)),char(9),char(13)];
                TT_5=['TT_UD_Zmin',char(9),char(9),char(9),'TT_UU_Zmin',char(9),char(13)];
                TT_6=['TT_UD_Zmax',char(9),char(9),char(9),'TT_UU_Zmax',char(9),char(13)];
                for i_T=1:6
                    NameT=['TT_',num2str(i_T)];
                    fprintf(fid,'%s',eval(NameT));
                end
                
            case 3
                
                TT_1=['TT_UU_Cut_Xmin_',NumberTube,char(9),char(9),char(9),'TT_UU_Xmin*10',char(9),char(13)];
                TT_2=['TT_UU_Cut_Xmax_',NumberTube,char(9),char(9),char(9),'TT_UU_Xmax*10',char(9),char(13)];
                TT_3=['TT_UU_Cut_Ymin_d_',NumberTube,char(9),char(9),char(9),num2str(StruT(iMStruT,2)),char(9),char(13)];
                TT_4=['TT_UU_Cut_Ymax_d_',NumberTube,char(9),char(9),char(9),num2str(StruT(iMStruT,3)),char(9),char(13)];
                TT_5=['TT_UU_Cut_U_Zmin_',NumberTube,char(9),char(9),char(9),num2str(StruT(iMStruT,4)),char(9),char(13)];
                TT_6=['TT_UU_Cut_U_Zmax_',NumberTube,char(9),char(9),char(9),num2str(StruT(iMStruT,5)),char(9),char(13)];
                TT_7=['TT_UU_Cut_D_Zmin_',NumberTube,char(9),char(9),char(9),num2str(StruT(iMStruT,6)),char(9),char(13)];
                TT_8=['TT_UU_Cut_D_Zmax_',NumberTube,char(9),char(9),char(9),num2str(StruT(iMStruT,7)),char(9),char(13)];
                for i_T=1:8
                    NameT=['TT_',num2str(i_T)];
                    fprintf(fid,'%s',eval(NameT));
                end
                
            case -3
                
                TT_1=['TT_UU_Cut_Xmin_',NumberTube,char(9),char(9),char(9),'TT_UU_Xmin*10',char(9),char(13)];
                TT_2=['TT_UU_Cut_Xmax_',NumberTube,char(9),char(9),char(9),'TT_UU_Xmax*10',char(9),char(13)];
                TT_3=['TT_UU_Cut_Ymin_d_',NumberTube,char(9),char(9),char(9),num2str(StruT(iMStruT,2)),char(9),char(13)];
                TT_4=['TT_UU_Cut_Ymax_d_',NumberTube,char(9),char(9),char(9),num2str(StruT(iMStruT,3)),char(9),char(13)];
                TT_5=['TT_UU_Cut_U_Zmin_',NumberTube,char(9),char(9),char(9),num2str(StruT(iMStruT,4)),char(9),char(13)];
                TT_6=['TT_UU_Cut_U_Zmax_',NumberTube,char(9),char(9),char(9),num2str(StruT(iMStruT,5)),char(9),char(13)];
                TT_7=['TT_UU_Cut_D_Zmin_',NumberTube,char(9),char(9),char(9),num2str(StruT(iMStruT,6)),char(9),char(13)];
                TT_8=['TT_UU_Cut_D_Zmax_',NumberTube,char(9),char(9),char(9),num2str(StruT(iMStruT,7)),char(9),char(13)];
                for i_T=1:8
                    NameT=['TT_',num2str(i_T)];
                    fprintf(fid,'%s',eval(NameT));
                end
                
            case 4
                
                TT_1=['TT_UD_Cut_Xmin_',NumberTube,char(9),char(9),char(9),'TT_UU_Xmin*10',char(9),char(13)];
                TT_2=['TT_UD_Cut_Xmax_',NumberTube,char(9),char(9),char(9),'TT_UU_Xmax*10',char(9),char(13)];
                TT_3=['TT_UD_Cut_Ymin_d_',NumberTube,char(9),char(9),char(9),num2str(StruT(iMStruT,2)),char(9),char(13)];
                TT_4=['TT_UD_Cut_Ymax_d_',NumberTube,char(9),char(9),char(9),num2str(StruT(iMStruT,3)),char(9),char(13)];
                TT_5=['TT_UD_Cut_U_Zmin_',NumberTube,char(9),char(9),char(9),num2str(StruT(iMStruT,4)),char(9),char(13)];
                TT_6=['TT_UD_Cut_U_Zmax_',NumberTube,char(9),char(9),char(9),num2str(StruT(iMStruT,5)),char(9),char(13)];
                TT_7=['TT_UD_Cut_D_Zmin_',NumberTube,char(9),char(9),char(9),num2str(StruT(iMStruT,6)),char(9),char(13)];
                TT_8=['TT_UD_Cut_D_Zmax_',NumberTube,char(9),char(9),char(9),num2str(StruT(iMStruT,7)),char(9),char(13)];
                for i_T=1:8
                    NameT=['TT_',num2str(i_T)];
                    fprintf(fid,'%s',eval(NameT));
                end
                
            case -4
                
                TT_1=['TT_UD_Cut_Xmin_',NumberTube,char(9),char(9),char(9),'TT_UU_Xmin*10',char(9),char(13)];
                TT_2=['TT_UD_Cut_Xmax_',NumberTube,char(9),char(9),char(9),'TT_UU_Xmax*10',char(9),char(13)];
                TT_3=['TT_UD_Cut_Ymin_d_',NumberTube,char(9),char(9),char(9),num2str(StruT(iMStruT,2)),char(9),char(13)];
                TT_4=['TT_UD_Cut_Ymax_d_',NumberTube,char(9),char(9),char(9),num2str(StruT(iMStruT,3)),char(9),char(13)];
                TT_5=['TT_UD_Cut_U_Zmin_',NumberTube,char(9),char(9),char(9),num2str(StruT(iMStruT,4)),char(9),char(13)];
                TT_6=['TT_UD_Cut_U_Zmax_',NumberTube,char(9),char(9),char(9),num2str(StruT(iMStruT,5)),char(9),char(13)];
                TT_7=['TT_UD_Cut_D_Zmin_',NumberTube,char(9),char(9),char(9),num2str(StruT(iMStruT,6)),char(9),char(13)];
                TT_8=['TT_UD_Cut_D_Zmax_',NumberTube,char(9),char(9),char(9),num2str(StruT(iMStruT,7)),char(9),char(13)];
                for i_T=1:8
                    NameT=['TT_',num2str(i_T)];
                    fprintf(fid,'%s',eval(NameT));
                end
                
        end
    end
    
    fclose(fid);
    
    
    %%  %%%%
    Fid=fopen(StruVBA,'a+');
    
    for iMStruT=1:MStruT
        iStruTT_Flag=StruTT_Flag(iMStruT);
        
        
        if iMStruT<=9
            NumberTube=['00',num2str(iMStruT)];
        elseif iMStruT<=99
            NumberTube=['0',num2str(iMStruT)];
        else
            NumberTube=[num2str(iMStruT)];
        end
        
        switch iStruTT_Flag
            
            case 1
                TT_1=['With Brick  ',char(10)];
                TT_2=['     .Reset   ',char(10)];
                TT_3=['     .Name "TT_UU_1"   ',char(10)];
                TT_4=['     .Component "component1"   ',char(10)];
                TT_5=['     .Material "Copper (hard-drawn)"   ',char(10)];
                TT_6=['     .Xrange "TT_UU_Xmin", "TT_UU_Xmax"   ',char(10)];
                TT_7=['     .Yrange "TT_UU_Ymin", "TT_UU_Ymax"   ',char(10)];
                TT_8=['     .Zrange "TT_UU_Zmin", "TT_UU_Zmax"   ',char(10)];
                TT_9=['     .Create  ',char(10)];
                TT_10=['End With  ',char(10)];
                
                for i_T=1:10
                    NameT=['TT_',num2str(i_T)];
                    fprintf(Fid,'%s',eval(NameT));
                end
                
            case -1
                TT_1=['With Brick  ',char(10)];
                TT_2=['     .Reset   ',char(10)];
                TT_3=['     .Name "TT_DD_1"   ',char(10)];
                TT_4=['     .Component "component1"   ',char(10)];
                TT_5=['     .Material "Copper (hard-drawn)"   ',char(10)];
                TT_6=['     .Xrange "TT_UU_Xmin", "TT_UU_Xmax"   ',char(10)];
                TT_7=['     .Yrange "-TT_UU_Ymin", "-TT_UU_Ymax"   ',char(10)];
                TT_8=['     .Zrange "TT_UU_Zmin", "TT_UU_Zmax"   ',char(10)];
                TT_9=['     .Create  ',char(10)];
                TT_10=['End With  ',char(10)];
                
                for i_T=1:10
                    NameT=['TT_',num2str(i_T)];
                    fprintf(Fid,'%s',eval(NameT));
                end
                
            case 2
                TT_1=['With Brick  ',char(10)];
                TT_2=['     .Reset   ',char(10)];
                TT_3=['     .Name "TT_UD_1"   ',char(10)];
                TT_4=['     .Component "component1"   ',char(10)];
                TT_5=['     .Material "Copper (hard-drawn)"   ',char(10)];
                TT_6=['     .Xrange "TT_UD_Xmin", "TT_UD_Xmax"   ',char(10)];
                TT_7=['     .Yrange "TT_UD_Ymin", "TT_UD_Ymax"   ',char(10)];
                TT_8=['     .Zrange "TT_UD_Zmin", "TT_UD_Zmax"   ',char(10)];
                TT_9=['     .Create  ',char(10)];
                TT_10=['End With  ',char(10)];
                
                for i_T=1:10
                    NameT=['TT_',num2str(i_T)];
                    fprintf(Fid,'%s',eval(NameT));
                end
                
            case -2
                TT_1=['With Brick  ',char(10)];
                TT_2=['     .Reset   ',char(10)];
                TT_3=['     .Name "TT_DU_1"   ',char(10)];
                TT_4=['     .Component "component1"   ',char(10)];
                TT_5=['     .Material "Copper (hard-drawn)"   ',char(10)];
                TT_6=['     .Xrange "TT_UD_Xmin", "TT_UD_Xmax"   ',char(10)];
                TT_7=['     .Yrange "-TT_UD_Ymin", "-TT_UD_Ymax"   ',char(10)];
                TT_8=['     .Zrange "TT_UD_Zmin", "TT_UD_Zmax"   ',char(10)];
                TT_9=['     .Create  ',char(10)];
                TT_10=['End With  ',char(10)];
                
                for i_T=1:10
                    NameT=['TT_',num2str(i_T)];
                    fprintf(Fid,'%s',eval(NameT));
                end
                
            case 3
                TT_1=['With Brick  ',char(10)];
                TT_2=['     .Reset   ',char(10)];
                TT_3=['     .Name "TT_UU_Cut_U_',NumberTube,'"   ',char(10)];
                TT_4=['     .Component "component1"   ',char(10)];
                TT_5=['     .Material "Copper (hard-drawn)"   ',char(10)];
                TT_6=['     .Xrange "TT_UU_Cut_Xmin_',NumberTube,'", "TT_UU_Cut_Xmax_',NumberTube,'"   ',char(10)];
                TT_7=['     .Yrange "TT_UU_Ymin+TT_UU_Cut_Ymax_d_',NumberTube,'-1", "TT_UU_Ymin+TT_UU_Cut_Ymax_d_',NumberTube,'"   ',char(10)];
                TT_8=['     .Zrange "TT_UU_Cut_U_Zmin_',NumberTube,'", "TT_UU_Cut_U_Zmax_',NumberTube,'"   ',char(10)];
                TT_9=['     .Create  ',char(10)];
                TT_10=['End With  ',char(10)];
                
                TT_11=['With Brick  ',char(10)];
                TT_12=['     .Reset   ',char(10)];
                TT_13=['     .Name "TT_UU_Cut_D_',NumberTube,'"   ',char(10)];
                TT_14=['     .Component "component1"   ',char(10)];
                TT_15=['     .Material "Copper (hard-drawn)"   ',char(10)];
                TT_16=['     .Xrange "TT_UU_Cut_Xmin_',NumberTube,'", "TT_UU_Cut_Xmax_',NumberTube,'"   ',char(10)];
                TT_17=['     .Yrange "TT_UD_Ymax+TT_UU_Cut_Ymin_d_',NumberTube,'", "TT_UD_Ymax+TT_UU_Cut_Ymin_d_',NumberTube,'+1"   ',char(10)];
                TT_18=['     .Zrange "TT_UU_Cut_D_Zmin_',NumberTube,'", "TT_UU_Cut_D_Zmax_',NumberTube,'"   ',char(10)];
                TT_19=['     .Create  ',char(10)];
                TT_20=['End With  ',char(10)];
                
                for i_T=1:20
                    NameT=['TT_',num2str(i_T)];
                    fprintf(Fid,'%s',eval(NameT));
                end
                
                
                
            case -3
                TT_1=['With Brick  ',char(10)];
                TT_2=['     .Reset   ',char(10)];
                TT_3=['     .Name "TT_DU_Cut_U_',NumberTube,'"   ',char(10)];
                TT_4=['     .Component "component1"   ',char(10)];
                TT_5=['     .Material "Copper (hard-drawn)"   ',char(10)];
                TT_6=['     .Xrange "TT_UU_Cut_Xmin_',NumberTube,'", "TT_UU_Cut_Xmax_',NumberTube,'"   ',char(10)];
                TT_7=['     .Yrange "-(TT_UU_Ymin+TT_UU_Cut_Ymax_d_',NumberTube,'-1)", "-(TT_UU_Ymin+TT_UU_Cut_Ymax_d_',NumberTube,')"   ',char(10)];
                TT_8=['     .Zrange "TT_UU_Cut_U_Zmin_',NumberTube,'", "TT_UU_Cut_U_Zmax_',NumberTube,'"   ',char(10)];
                TT_9=['     .Create  ',char(10)];
                TT_10=['End With  ',char(10)];
                
                TT_11=['With Brick  ',char(10)];
                TT_12=['     .Reset   ',char(10)];
                TT_13=['     .Name "TT_DU_Cut_D_',NumberTube,'"   ',char(10)];
                TT_14=['     .Component "component1"   ',char(10)];
                TT_15=['     .Material "Copper (hard-drawn)"   ',char(10)];
                TT_16=['     .Xrange "TT_UU_Cut_Xmin_',NumberTube,'", "TT_UU_Cut_Xmax_',NumberTube,'"   ',char(10)];
                TT_17=['     .Yrange "-(TT_UD_Ymax+TT_UU_Cut_Ymin_d_',NumberTube,')", "-(TT_UD_Ymax+TT_UU_Cut_Ymin_d_',NumberTube,'+1)"   ',char(10)];
                TT_18=['     .Zrange "TT_UU_Cut_D_Zmin_',NumberTube,'", "TT_UU_Cut_D_Zmax_',NumberTube,'"   ',char(10)];
                TT_19=['     .Create  ',char(10)];
                TT_20=['End With  ',char(10)];
                
                for i_T=1:20
                    NameT=['TT_',num2str(i_T)];
                    fprintf(Fid,'%s',eval(NameT));
                end
                
            case 4
                TT_1=['With Brick  ',char(10)];
                TT_2=['     .Reset   ',char(10)];
                TT_3=['     .Name "TT_UD_Cut_U_',NumberTube,'"   ',char(10)];
                TT_4=['     .Component "component1"   ',char(10)];
                TT_5=['     .Material "Copper (hard-drawn)"   ',char(10)];
                TT_6=['     .Xrange "TT_UD_Cut_Xmin_',NumberTube,'", "TT_UD_Cut_Xmax_',NumberTube,'"   ',char(10)];
                TT_7=['     .Yrange "TT_UD_Ymax+TT_UD_Cut_Ymax_d_',NumberTube,'-1", "TT_UD_Ymax+TT_UD_Cut_Ymax_d_',NumberTube,'"   ',char(10)];
                TT_8=['     .Zrange "TT_UD_Cut_U_Zmin_',NumberTube,'", "TT_UD_Cut_U_Zmax_',NumberTube,'"   ',char(10)];
                TT_9=['     .Create  ',char(10)];
                TT_10=['End With  ',char(10)];
                
                TT_11=['With Brick  ',char(10)];
                TT_12=['     .Reset   ',char(10)];
                TT_13=['     .Name "TT_UD_Cut_D_',NumberTube,'"   ',char(10)];
                TT_14=['     .Component "component1"   ',char(10)];
                TT_15=['     .Material "Copper (hard-drawn)"   ',char(10)];
                TT_16=['     .Xrange "TT_UD_Cut_Xmin_',NumberTube,'", "TT_UD_Cut_Xmax_',NumberTube,'"   ',char(10)];
                TT_17=['     .Yrange "TT_UD_Ymin+TT_UD_Cut_Ymin_d_',NumberTube,'", "TT_UD_Ymin+TT_UD_Cut_Ymin_d_',NumberTube,'+1"   ',char(10)];
                TT_18=['     .Zrange "TT_UD_Cut_D_Zmin_',NumberTube,'", "TT_UD_Cut_D_Zmax_',NumberTube,'"   ',char(10)];
                TT_19=['     .Create  ',char(10)];
                TT_20=['End With  ',char(10)];
                
                for i_T=1:20
                    NameT=['TT_',num2str(i_T)];
                    fprintf(Fid,'%s',eval(NameT));
                end
                
            case -4
                
                TT_1=['With Brick  ',char(10)];
                TT_2=['     .Reset   ',char(10)];
                TT_3=['     .Name "TT_DD_Cut_U_',NumberTube,'"   ',char(10)];
                TT_4=['     .Component "component1"   ',char(10)];
                TT_5=['     .Material "Copper (hard-drawn)"   ',char(10)];
                TT_6=['     .Xrange "TT_UD_Cut_Xmin_',NumberTube,'", "TT_UD_Cut_Xmax_',NumberTube,'"   ',char(10)];
                TT_7=['     .Yrange "-(TT_UD_Ymax+TT_UD_Cut_Ymax_d_',NumberTube,'-1)", "-(TT_UD_Ymax+TT_UD_Cut_Ymax_d_',NumberTube,')"   ',char(10)];
                TT_8=['     .Zrange "TT_UD_Cut_U_Zmin_',NumberTube,'", "TT_UD_Cut_U_Zmax_',NumberTube,'"   ',char(10)];
                TT_9=['     .Create  ',char(10)];
                TT_10=['End With  ',char(10)];
                
                TT_11=['With Brick  ',char(10)];
                TT_12=['     .Reset   ',char(10)];
                TT_13=['     .Name "TT_DD_Cut_D_',NumberTube,'"   ',char(10)];
                TT_14=['     .Component "component1"   ',char(10)];
                TT_15=['     .Material "Copper (hard-drawn)"   ',char(10)];
                TT_16=['     .Xrange "TT_UD_Cut_Xmin_',NumberTube,'", "TT_UD_Cut_Xmax_',NumberTube,'"   ',char(10)];
                TT_17=['     .Yrange "-(TT_UD_Ymin+TT_UD_Cut_Ymin_d_',NumberTube,')", "-(TT_UD_Ymin+TT_UD_Cut_Ymin_d_',NumberTube,'+1)"   ',char(10)];
                TT_18=['     .Zrange "TT_UD_Cut_D_Zmin_',NumberTube,'", "TT_UD_Cut_D_Zmax_',NumberTube,'"   ',char(10)];
                TT_19=['     .Create  ',char(10)];
                TT_20=['End With  ',char(10)];
                
                for i_T=1:20
                    NameT=['TT_',num2str(i_T)];
                    fprintf(Fid,'%s',eval(NameT));
                end
                
        end
    end
    
    
    
    %%   %%%%%%%   T型板 LOFT
    
    TT_1=['Pick.PickFaceFromId "component1:TT_UU_1", "3"  ',char(10)];
    TT_2=['Pick.PickFaceFromId "component1:TT_UD_1", "5"  ',char(10)];
    TT_3=['With Loft  ',char(10)];
    TT_4=['     .Reset  ',char(10)];
    TT_5=['     .Name "TT_U_1"  ',char(10)];
    TT_6=['     .Component "component1"  ',char(10)];
    TT_7=['     .Material "Copper (hard-drawn)"  ',char(10)];
    TT_8=['     .Tangency "0.0"  ',char(10)];
    TT_9=['     .CreateNew  ',char(10)];
    TT_10=['End With  ',char(10)];
    
    TT_11=['Pick.PickFaceFromId "component1:TT_DU_1", "3"  ',char(10)];
    TT_12=['Pick.PickFaceFromId "component1:TT_DD_1", "5"  ',char(10)];
    TT_13=['With Loft  ',char(10)];
    TT_14=['     .Reset  ',char(10)];
    TT_15=['     .Name "TT_D_1"  ',char(10)];
    TT_16=['     .Component "component1"  ',char(10)];
    TT_17=['     .Material "Copper (hard-drawn)"  ',char(10)];
    TT_18=['     .Tangency "0.0"  ',char(10)];
    TT_19=['     .CreateNew  ',char(10)];
    TT_20=['End With  ',char(10)];
    TT_21=['Solid.Add "component1:TT_U_1", "component1:TT_UU_1" ',char(10)];
    TT_22=['Solid.Add "component1:TT_U_1", "component1:TT_UD_1"  ',char(10)];
    TT_23=['Solid.Add "component1:TT_D_1", "component1:TT_DU_1" ',char(10)];
    TT_24=['Solid.Add "component1:TT_D_1", "component1:TT_DD_1"  ',char(10)];
    TT_25=['Solid.Add "component1:TT_U_1", "component1:TT_D_1"  ',char(10)];
    TT_26=['Solid.Rename "component1:TT_U_1", "T"  ',char(10)];
    
    
    for i_T=1:26
        NameT=['TT_',num2str(i_T)];
        fprintf(Fid,'%s',eval(NameT));
    end
    
    
    
    
    
    
    for iMStruT=1:MStruT
        iStruTT_Flag=StruTT_Flag(iMStruT);
        
        
        if iMStruT<=9
            NumberTube=['00',num2str(iMStruT)];
        elseif iMStruT<=99
            NumberTube=['0',num2str(iMStruT)];
        else
            NumberTube=[num2str(iMStruT)];
        end
        
        switch iStruTT_Flag
            
            case 3
                TT_1=['Pick.PickFaceFromId "component1:TT_UU_Cut_U_',NumberTube,'", "3"  ',char(10)];
                TT_2=['Pick.PickFaceFromId "component1:TT_UU_Cut_D_',NumberTube,'", "5"  ',char(10)];
                TT_3=['With Loft  ',char(10)];
                TT_4=['     .Reset  ',char(10)];
                TT_5=['     .Name "TT_UU_Cut_',NumberTube,'"  ',char(10)];
                TT_6=['     .Component "component1"  ',char(10)];
                TT_7=['     .Material "Copper (hard-drawn)"  ',char(10)];
                TT_8=['     .Tangency "0.0"  ',char(10)];
                TT_9=['     .CreateNew  ',char(10)];
                TT_10=['End With  ',char(10)];
                
                TT_11=['Solid.Subtract "component1:T", "component1:TT_UU_Cut_U_',NumberTube,'"   ',char(10)];
                TT_12=['Solid.Subtract "component1:T", "component1:TT_UU_Cut_D_',NumberTube,'"   ',char(10)];
                TT_13=['Solid.Subtract "component1:T", "component1:TT_UU_Cut_',NumberTube,'"   ',char(10)];
                
                for i_T=1:13
                    NameT=['TT_',num2str(i_T)];
                    fprintf(Fid,'%s',eval(NameT));
                end
                
            case -3
                TT_1=['Pick.PickFaceFromId "component1:TT_DU_Cut_U_',NumberTube,'", "3"  ',char(10)];
                TT_2=['Pick.PickFaceFromId "component1:TT_DU_Cut_D_',NumberTube,'", "5"  ',char(10)];
                TT_3=['With Loft  ',char(10)];
                TT_4=['     .Reset  ',char(10)];
                TT_5=['     .Name "TT_DU_Cut_',NumberTube,'"  ',char(10)];
                TT_6=['     .Component "component1"  ',char(10)];
                TT_7=['     .Material "Copper (hard-drawn)"  ',char(10)];
                TT_8=['     .Tangency "0.0"  ',char(10)];
                TT_9=['     .CreateNew  ',char(10)];
                TT_10=['End With  ',char(10)];
                
                TT_11=['Solid.Subtract "component1:T", "component1:TT_DU_Cut_U_',NumberTube,'"   ',char(10)];
                TT_12=['Solid.Subtract "component1:T", "component1:TT_DU_Cut_D_',NumberTube,'"   ',char(10)];
                TT_13=['Solid.Subtract "component1:T", "component1:TT_DU_Cut_',NumberTube,'"   ',char(10)];
                
                for i_T=1:13
                    NameT=['TT_',num2str(i_T)];
                    fprintf(Fid,'%s',eval(NameT));
                end
                
            case 4
                TT_1=['Pick.PickFaceFromId "component1:TT_UD_Cut_U_',NumberTube,'", "3"  ',char(10)];
                TT_2=['Pick.PickFaceFromId "component1:TT_UD_Cut_D_',NumberTube,'", "5"  ',char(10)];
                TT_3=['With Loft  ',char(10)];
                TT_4=['     .Reset  ',char(10)];
                TT_5=['     .Name "TT_UD_Cut_',NumberTube,'"  ',char(10)];
                TT_6=['     .Component "component1"  ',char(10)];
                TT_7=['     .Material "Copper (hard-drawn)"  ',char(10)];
                TT_8=['     .Tangency "0.0"  ',char(10)];
                TT_9=['     .CreateNew  ',char(10)];
                TT_10=['End With  ',char(10)];
                
                TT_11=['Solid.Subtract "component1:T", "component1:TT_UD_Cut_U_',NumberTube,'"   ',char(10)];
                TT_12=['Solid.Subtract "component1:T", "component1:TT_UD_Cut_D_',NumberTube,'"   ',char(10)];
                TT_13=['Solid.Subtract "component1:T", "component1:TT_UD_Cut_',NumberTube,'"   ',char(10)];
                
                for i_T=1:13
                    NameT=['TT_',num2str(i_T)];
                    fprintf(Fid,'%s',eval(NameT));
                end
                
                
            case -4
                TT_1=['Pick.PickFaceFromId "component1:TT_DD_Cut_U_',NumberTube,'", "3"  ',char(10)];
                TT_2=['Pick.PickFaceFromId "component1:TT_DD_Cut_D_',NumberTube,'", "5"  ',char(10)];
                TT_3=['With Loft  ',char(10)];
                TT_4=['     .Reset  ',char(10)];
                TT_5=['     .Name "TT_DD_Cut_',NumberTube,'"  ',char(10)];
                TT_6=['     .Component "component1"  ',char(10)];
                TT_7=['     .Material "Copper (hard-drawn)"  ',char(10)];
                TT_8=['     .Tangency "0.0"  ',char(10)];
                TT_9=['     .CreateNew  ',char(10)];
                TT_10=['End With  ',char(10)];
                
                TT_11=['Solid.Subtract "component1:T", "component1:TT_DD_Cut_U_',NumberTube,'"   ',char(10)];
                TT_12=['Solid.Subtract "component1:T", "component1:TT_DD_Cut_D_',NumberTube,'"   ',char(10)];
                TT_13=['Solid.Subtract "component1:T", "component1:TT_DD_Cut_',NumberTube,'"   ',char(10)];
                
                for i_T=1:13
                    NameT=['TT_',num2str(i_T)];
                    fprintf(Fid,'%s',eval(NameT));
                end
        end
    end
    
    
    %%        %%%%%%%%%   把Tube全加起来
    
    for nTube=2:Ntube-1
        if nTube<=9
            NumberTube=['00',num2str(nTube)];
        elseif nTube<=99
            NumberTube=['0',num2str(nTube)];
        else
            NumberTube=[num2str(nTube)];
        end
        Tadd_1=['Solid.Add "component1:Tube_001','", "component1:Tube_',NumberTube,'" ',char(10)];
        fprintf(Fid,'%s',Tadd_1);
    end
    
    Tadd_2=['Solid.Rename "component1:Tube_001", "Tube"  ',char(10)];
    fprintf(Fid,'%s',Tadd_2);
    
    if  Tube_Blend_Outer_Flag~=1
        for nTube=2:Ntube-1
            if nTube<=9
                NumberTube=['00',num2str(nTube)];
            elseif nTube<=99
                NumberTube=['0',num2str(nTube)];
            else
                NumberTube=num2str(nTube);
            end
            Tadd_1=['Solid.Add "component1:Tube','", "component1:EarLeft_',NumberTube,'" ',char(10)];
            fprintf(Fid,'%s',Tadd_1);
        end
        for nTube=1:Ntube-2
            if nTube<=9
                NumberTube=['00',num2str(nTube)];
            elseif nTube<=99
                NumberTube=['0',num2str(nTube)];
            else
                NumberTube=num2str(nTube);
            end
            Tadd_1=['Solid.Add "component1:Tube','", "component1:EarRight_',NumberTube,'" ',char(10)];
            fprintf(Fid,'%s',Tadd_1);
        end
        
    end
    
    
    
    fclose(Fid);
end



%%    %%%%%%%%%%%%%%% SHELL

StruAS = xlsread('Struc.xlsx','SHELL');
[StruASM,StruASN]=size(StruAS);

Fid=fopen(StruPara,'a+');
for StruASm=1:StruASM
    AS_1=['AS_R_',num2str(StruASm),char(9),char(9),char(9),num2str(StruAS(StruASm,2)),char(9),char(13)];
    AS_2=['AS_Z_Begin_',num2str(StruASm),char(9),char(9),char(9),num2str(StruAS(StruASm,3)),char(9),char(13)];
    AS_3=['AS_Z_End_',num2str(StruASm),char(9),char(9),char(9),num2str(StruAS(StruASm,4)),char(9),char(13)];
    
    for i_AS=1:3
        NameAS=['AS_',num2str(i_AS)];
        fprintf(Fid,'%s',eval(NameAS));
    end
end
fclose(Fid);

Fid=fopen(StruVBA,'a+');
for StruASm=1:StruASM
    
    AS_1=['WCS.ActivateWCS "global" ',char(10)];
    AS_2=['With Cylinder  ',char(10)];
    AS_3=['     .Reset   ',char(10)];
    AS_4=['     .Name "AS_',num2str(StruASm),'"   ',char(10)];
    AS_5=['     .Component "component1"   ',char(10)];
    AS_6=['     .Material "Vacuum"   ',char(10)];
    AS_7=['     .OuterRadius "AS_R_',num2str(StruASm),'"   ',char(10)];
    AS_8=['     .InnerRadius "0"   ',char(10)];
    AS_9=['     .Axis "z"   ',char(10)];
    AS_10=['     .Zrange "AS_Z_Begin_',num2str(StruASm),'",  "AS_Z_End_',num2str(StruASm),'"  ',char(10)];
    AS_11=['     .Xcenter "0"   ',char(10)];
    AS_12=['     .Ycenter "0"   ',char(10)];
    AS_13=['     .Segments "0"   ',char(10)];
    AS_14=['     .Create   ',char(10)];
    AS_15=['End With   ',char(10)];
    
    for i_AS=1:15
        NameAS=['AS_',num2str(i_AS)];
        fprintf(Fid,'%s',eval(NameAS));
    end
end
fclose(Fid);





%%    %%%%%%%%%%%%%%% MESH
StruMS = xlsread('Struc.xlsx','MESH');
[StruMSM,StruMSN]=size(StruMS);

Fid=fopen(StruPara,'a+');
for StruMSm=1:StruMSM
    MS_1=['MS_Xmin_',num2str(StruMSm),char(9),char(9),char(9),num2str(StruMS(StruMSm,2)),char(9),char(13)];
    MS_2=['MS_Xmax_',num2str(StruMSm),char(9),char(9),char(9),num2str(StruMS(StruMSm,3)),char(9),char(13)];
    MS_3=['MS_Ymin_',num2str(StruMSm),char(9),char(9),char(9),num2str(StruMS(StruMSm,4)),char(9),char(13)];
    MS_4=['MS_Ymax_',num2str(StruMSm),char(9),char(9),char(9),num2str(StruMS(StruMSm,5)),char(9),char(13)];
    MS_5=['MS_Zmin_',num2str(StruMSm),char(9),char(9),char(9),num2str(StruMS(StruMSm,6)),char(9),char(13)];
    MS_6=['MS_Zmax_',num2str(StruMSm),char(9),char(9),char(9),num2str(StruMS(StruMSm,7)),char(9),char(13)];
    for i_MS=1:6
        NameMS=['MS_',num2str(i_MS)];
        fprintf(Fid,'%s',eval(NameMS));
    end
end
fclose(Fid);

Fid=fopen(StruVBA,'a+');
for StruMSm=1:StruMSM
    
    
    MS_1=['With Brick  ',char(10)];
    MS_2=['     .Reset   ',char(10)];
    MS_3=['     .Name "MS_',NumberTube,'"   ',char(10)];
    MS_4=['     .Component "component1"   ',char(10)];
    MS_5=['     .Material "Vacuum"   ',char(10)];
    MS_6=['     .Xrange "MS_Xmin_',num2str(StruMSm),'", "MS_Xmax_',num2str(StruMSm),'"   ',char(10)];
    MS_7=['     .Yrange "MS_Ymin_',num2str(StruMSm),'", "MS_Ymax_',num2str(StruMSm),'"   ',char(10)];
    MS_8=['     .Zrange "MS_Zmin_',num2str(StruMSm),'", "MS_Zmax_',num2str(StruMSm),'"   ',char(10)];
    MS_9=['     .Create  ',char(10)];
    MS_10=['End With  ',char(10)];
    MS_11=['  ',char(10)];
    
    
    
    for i_MS=1:11
        NameMS=['MS_',num2str(i_MS)];
        fprintf(Fid,'%s',eval(NameMS));
    end
end
fclose(Fid);



%%    %%%%%%%%%%%%%%% HLine
if SIM_FLAG==1
    StruHL = xlsread('Struc.xlsx','HLINE');
    [StruHLM,StruHLN]=size(StruHL);
    
    Fid=fopen(StruPara,'a+');
    for StruHLm=1:StruHLM
        HL_X=StruHL(StruHLm,2);
        
        HL_Y=StruHL(StruHLm,3);
        
        
        
        HL_1=['HL_X_',num2str(StruHLm),char(9),char(9),char(9),num2str(HL_X),char(9),char(13)];
        HL_2=['HL_Y_',num2str(StruHLm),char(9),char(9),char(9),num2str(HL_Y),char(9),char(13)];
        
        for i_HL=1:2
            NameHL=['HL_',num2str(i_HL)];
            fprintf(Fid,'%s',eval(NameHL));
        end
    end
    fclose(Fid);
    
    
    Fid=fopen(StruVBA,'a+');
    for StruHLm=1:StruHLM
        
        HL_X=StruHL(StruHLm,2);
        if HL_X<=0
            HL_X_str=['N',num2str(abs(HL_X))];
        else
            HL_X_str=['P',num2str(abs(HL_X))];
        end
        
        HL_Y=StruHL(StruHLm,3);
        if HL_Y<=0
            HL_Y_str=['N',num2str(abs(HL_Y))];
        else
            HL_Y_str=['P',num2str(abs(HL_Y))];
        end
        
        HLineName=['HL_',HL_X_str,'_',HL_Y_str];
        
        HL_1=['    With Line ',char(10)];
        HL_2=['    .Reset ',char(10)];
        HL_3=['   .Name "',HLineName,'" ',char(10)];
        HL_4=['    .Curve "',HLineName,'" ',char(10)];
        HL_5=['    .X1 "0" ',char(10)];
        HL_6=['   .Y1 "TT_UU_Zmax" ',char(10)];
        HL_7=['    .X2 "0.0" ',char(10)];
        HL_8=['    .Y2 "0.0" ',char(10)];
        HL_9=['    .Create ',char(10)];
        HL_10=['    End With ',char(10)];
        
        
        HL_11=['With Transform  ',char(10)];
        HL_12=['     .Reset  ',char(10)];
        HL_13=['     .Name "',HLineName,'"  ',char(10)];
        HL_14=['     .Origin "Free"  ',char(10)];
        HL_15=['     .Center "0", "0", "0"  ',char(10)];
        HL_16=['    .Angle "90", "0", "0"  ',char(10)];
        HL_17=['     .MultipleObjects "False"  ',char(10)];
        HL_18=['     .GroupObjects "False"  ',char(10)];
        HL_19=['     .Repetitions "1"  ',char(10)];
        HL_20=['     .MultipleSelection "False"  ',char(10)];
        HL_21=['     .Transform "Curve", "Rotate"  ',char(10)];
        HL_22=['End With  ',char(10)];
        
        
        HL_23=['With Transform  ',char(10)];
        HL_24=['     .Reset  ',char(10)];
        HL_25=['    .Name "',HLineName,'"  ',char(10)];
        HL_26=['     .Vector "HL_X_',num2str(StruHLm),'", "HL_Y_',num2str(StruHLm),'", "0"  ',char(10)];
        HL_27=['    .UsePickedPoints "False"  ',char(10)];
        HL_28=['     .InvertPickedPoints "False"  ',char(10)];
        HL_29=['     .MultipleObjects "False"  ',char(10)];
        HL_30=['     .GroupObjects "False"  ',char(10)];
        HL_31=['     .Repetitions "1"  ',char(10)];
        HL_32=['     .MultipleSelection "False"  ',char(10)];
        HL_33=['     .Transform "Curve", "Translate"  ',char(10)];
        HL_34=['End With  ',char(10)];
        
        
        
        
        
        for i_HL=1:34
            NameHL=['HL_',num2str(i_HL)];
            fprintf(Fid,'%s',eval(NameHL));
        end
    end
    fclose(Fid);
else
    StruHL = xlsread('Struc.xlsx','HLINE');
    [StruHLM,StruHLN]=size(StruHL);
    
    Fid=fopen(StruPara,'a+');
    for StruHLm=1:StruHLM
        HL_X=StruHL(StruHLm,2);
        
        HL_Y=StruHL(StruHLm,3);
        
        
        
        HL_1=['HL_X_',num2str(StruHLm),char(9),char(9),char(9),num2str(HL_X),char(9),char(13)];
        HL_2=['HL_Y_',num2str(StruHLm),char(9),char(9),char(9),num2str(HL_Y),char(9),char(13)];
        
        for i_HL=1:2
            NameHL=['HL_',num2str(i_HL)];
            fprintf(Fid,'%s',eval(NameHL));
        end
    end
    fclose(Fid);
    
    
    Fid=fopen(StruVBA,'a+');
    for StruHLm=1:StruHLM
        
        HL_X=StruHL(StruHLm,2);
        if HL_X<=0
            HL_X_str=['N',num2str(abs(HL_X))];
        else
            HL_X_str=['P',num2str(abs(HL_X))];
        end
        
        HL_Y=StruHL(StruHLm,3);
        if HL_Y<=0
            HL_Y_str=['N',num2str(abs(HL_Y))];
        else
            HL_Y_str=['P',num2str(abs(HL_Y))];
        end
        
        HLineName=['HL_',HL_X_str,'_',HL_Y_str];
        
        HL_1=['    With Line ',char(10)];
        HL_2=['    .Reset ',char(10)];
        HL_3=['   .Name "',HLineName,'" ',char(10)];
        HL_4=['    .Curve "',HLineName,'" ',char(10)];
        HL_5=['    .X1 "0" ',char(10)];
        HL_6=['   .Y1 "T_UU_Zmax" ',char(10)];
        HL_7=['    .X2 "0.0" ',char(10)];
        HL_8=['    .Y2 "0.0" ',char(10)];
        HL_9=['    .Create ',char(10)];
        HL_10=['    End With ',char(10)];
        
        
        HL_11=['With Transform  ',char(10)];
        HL_12=['     .Reset  ',char(10)];
        HL_13=['     .Name "',HLineName,'"  ',char(10)];
        HL_14=['     .Origin "Free"  ',char(10)];
        HL_15=['     .Center "0", "0", "0"  ',char(10)];
        HL_16=['    .Angle "90", "0", "0"  ',char(10)];
        HL_17=['     .MultipleObjects "False"  ',char(10)];
        HL_18=['     .GroupObjects "False"  ',char(10)];
        HL_19=['     .Repetitions "1"  ',char(10)];
        HL_20=['     .MultipleSelection "False"  ',char(10)];
        HL_21=['     .Transform "Curve", "Rotate"  ',char(10)];
        HL_22=['End With  ',char(10)];
        
        
        HL_23=['With Transform  ',char(10)];
        HL_24=['     .Reset  ',char(10)];
        HL_25=['    .Name "',HLineName,'"  ',char(10)];
        HL_26=['     .Vector "HL_X_',num2str(StruHLm),'", "HL_Y_',num2str(StruHLm),'", "0"  ',char(10)];
        HL_27=['    .UsePickedPoints "False"  ',char(10)];
        HL_28=['     .InvertPickedPoints "False"  ',char(10)];
        HL_29=['     .MultipleObjects "False"  ',char(10)];
        HL_30=['     .GroupObjects "False"  ',char(10)];
        HL_31=['     .Repetitions "1"  ',char(10)];
        HL_32=['     .MultipleSelection "False"  ',char(10)];
        HL_33=['     .Transform "Curve", "Translate"  ',char(10)];
        HL_34=['End With  ',char(10)];
        
        
        
        
        
        for i_HL=1:34
            NameHL=['HL_',num2str(i_HL)];
            fprintf(Fid,'%s',eval(NameHL));
        end
    end
    fclose(Fid);
end

%%    %%%%%%%%%%%%%%% VLine
StruVL = xlsread('Struc.xlsx','VLINE');
[StruVLM,StruVLN]=size(StruVL);

Fid=fopen(StruPara,'a+');
for StruVLm=1:StruVLM
    VL_TubeNO=StruVL(StruVLm,2);
    VL_Z=StruVL(StruVLm,3);
    VL_Fai=StruVL(StruVLm,4);
    
    VL_1=['VL_TubeNO_',num2str(StruVLm),char(9),char(9),char(9),num2str(VL_TubeNO),char(9),char(13)];
    VL_2=['VL_Z_',num2str(StruVLm),char(9),char(9),char(9),num2str(VL_Z),char(9),char(13)];
    VL_3=['VL_Fai_',num2str(StruVLm),char(9),char(9),char(9),num2str(VL_Fai),char(9),char(13)];
    
    for i_VL=1:3
        NameVL=['VL_',num2str(i_VL)];
        fprintf(Fid,'%s',eval(NameVL));
    end
end
fclose(Fid);


Fid=fopen(StruVBA,'a+');

for StruVLm=1:StruVLM
    
    VL_TubeNO=StruVL(StruVLm,2);
    VL_Z=StruVL(StruVLm,3);
    VL_Fai=StruVL(StruVLm,4);
    
    if VL_Z<=0
        VL_Z_str=['N',num2str(abs(VL_Z))];
    else
        VL_Z_str=['P',num2str(abs(VL_Z))];
    end
    
    VL_TubeNO_str=num2str(VL_TubeNO);
    VL_Fai_str=num2str(VL_Fai);
    
    
    
    
    if VL_TubeNO<=9
        NumberTube=['00',num2str(VL_TubeNO)];
    elseif nTube<=99
        NumberTube=['0',num2str(VL_TubeNO)];
    else
        NumberTube=[num2str(VL_TubeNO)];
    end
    
    VL_TubeNONext=VL_TubeNO+1;
    if VL_TubeNONext<=9
        NumberTubeNext=['00',num2str(VL_TubeNONext)];
    elseif nTube<=99
        NumberTubeNext=['0',num2str(VL_TubeNONext)];
    else
        NumberTubeNext=[num2str(VL_TubeNONext-1)];
    end
    
    VLineName=['VL_',VL_TubeNO_str,'_',VL_Z_str,'_',VL_Fai_str];
    
    VL_1=['    With Line ',char(10)];
    VL_2=['    .Reset ',char(10)];
    VL_3=['   .Name "',VLineName,'" ',char(10)];
    VL_4=['    .Curve "',VLineName,'" ',char(10)];
    VL_5=['    .X1 "0" ',char(10)];
    VL_6=['   .Y1 "-Tube_R_Outer_',NumberTube,'*1.5" ',char(10)];
    VL_7=['    .X2 "0.0" ',char(10)];
    VL_8=['    .Y2 "Tube_R_Outer_',NumberTube,'*1.5" ',char(10)];
    VL_9=['    .Create ',char(10)];
    VL_10=['    End With ',char(10)];
    
    
    VL_11=['With Transform  ',char(10)];
    VL_12=['     .Reset  ',char(10)];
    VL_13=['     .Name "',VLineName,'"  ',char(10)];
    VL_14=['     .Origin "Free"  ',char(10)];
    VL_15=['     .Center "0", "0", "0"  ',char(10)];
    VL_16=['    .Angle "0", "0", "VL_Fai_',num2str(StruVLm),'"  ',char(10)];
    VL_17=['     .MultipleObjects "False"  ',char(10)];
    VL_18=['     .GroupObjects "False"  ',char(10)];
    VL_19=['     .Repetitions "1"  ',char(10)];
    VL_20=['     .MultipleSelection "False"  ',char(10)];
    VL_21=['     .Transform "Curve", "Rotate"  ',char(10)];
    VL_22=['End With  ',char(10)];
    
    
    VL_23=['With Transform  ',char(10)];
    VL_24=['     .Reset  ',char(10)];
    VL_25=['    .Name "',VLineName,'"  ',char(10)];
    VL_26=['     .Vector "0", "0", "VL_Z_',num2str(StruVLm),'+(Tube_Z_Begin_',NumberTubeNext,'+Tube_Z_End_',NumberTube,')/2"  ',char(10)];
    VL_27=['    .UsePickedPoints "False"  ',char(10)];
    VL_28=['     .InvertPickedPoints "False"  ',char(10)];
    VL_29=['     .MultipleObjects "False"  ',char(10)];
    VL_30=['     .GroupObjects "False"  ',char(10)];
    VL_31=['     .Repetitions "1"  ',char(10)];
    VL_32=['     .MultipleSelection "False"  ',char(10)];
    VL_33=['     .Transform "Curve", "Translate"  ',char(10)];
    VL_34=['End With  ',char(10)];
    
    
    for i_VL=1:34
        NameVL=['VL_',num2str(i_VL)];
        fprintf(Fid,'%s',eval(NameVL));
    end
end
fclose(Fid);


%%    %%%%%%%%%%%%%%% TUNER
StruTUNER = xlsread('Struc.xlsx','TUNER');
[StruTUNERM,StruTUNERN]=size(StruTUNER);

Fid=fopen(StruPara,'a+');
for StruTUNERm=1:StruTUNERM
    TUNER_Z=StruTUNER(StruTUNERm,2);
    TUNER_Fai=StruTUNER(StruTUNERm,3);
    TUNER_R=StruTUNER(StruTUNERm,4);
    TUNER_Rin=StruTUNER(StruTUNERm,5);
    TUNER_Rout=StruTUNER(StruTUNERm,6);
    
    
    
    TUNER_1=['TUNER_Z_',num2str(StruTUNERm),char(9),char(9),char(9),num2str(TUNER_Z),char(9),char(13)];
    TUNER_2=['TUNER_Fai_',num2str(StruTUNERm),char(9),char(9),char(9),num2str(TUNER_Fai),char(9),char(13)];
    TUNER_3=['TUNER_R_',num2str(StruTUNERm),char(9),char(9),char(9),num2str(TUNER_R),char(9),char(13)];
    TUNER_4=['TUNER_Rin_',num2str(StruTUNERm),char(9),char(9),char(9),num2str(TUNER_Rin),char(9),char(13)];
    TUNER_5=['TUNER_Rout_',num2str(StruTUNERm),char(9),char(9),char(9),num2str(TUNER_Rout),char(9),char(13)];
    
    
    
    
    for i_TUNER=1:5
        NameTUNER=['TUNER_',num2str(i_TUNER)];
        fprintf(Fid,'%s',eval(NameTUNER));
    end
end
fclose(Fid);


Fid=fopen(StruVBA,'a+');

for StruTUNERm=1:StruTUNERM
    
    TUNER_Z=StruTUNER(StruTUNERm,2);
    TUNER_Fai=StruTUNER(StruTUNERm,3);
    TUNER_R=StruTUNER(StruTUNERm,2);
    TUNER_Rin=StruTUNER(StruTUNERm,3);
    TUNER_Rout=StruTUNER(StruTUNERm,2);
    
    TUNER_Z_str=num2str(TUNER_Z);
    TUNER_Fai_str=num2str(TUNER_Fai);
    TUNER_R_str=num2str(TUNER_R);
    TUNER_Rin_str=num2str(TUNER_Rin);
    TUNER_Rout_str=num2str(TUNER_Rout);
    
    
    
    TUNERName=['TUNER_',TUNER_Z_str,'_',TUNER_Fai_str];
    
   
                TUNER_1=['With Cylinder  ',char(10)];
                TUNER_2=['     .Reset   ',char(10)];
                TUNER_3=['     .Name "',TUNERName,'"   ',char(10)];
                TUNER_4=['     .Component "component1"   ',char(10)];
                TUNER_5=['     .Material "Copper (hard-drawn)"   ',char(10)];
                TUNER_6=['     .OuterRadius "TUNER_R_',num2str(StruTUNERm),'"   ',char(10)];
                TUNER_7=['     .InnerRadius "0"   ',char(10)];
                TUNER_8=['     .Axis "z"   ',char(10)];
                TUNER_9=['     .Zrange "TUNER_Rin_',num2str(StruTUNERm),'",  "TUNER_Rout_',num2str(StruTUNERm),'"  ',char(10)];
                TUNER_10=['     .Xcenter "0"   ',char(10)];
                TUNER_11=['     .Ycenter "0"   ',char(10)];
                TUNER_12=['     .Segments "0"   ',char(10)];
                TUNER_13=['     .Create   ',char(10)];
                TUNER_14=['End With   ',char(10)];
                
            
    
    TUNER_15=['    With Transform  ',char(10)];
     TUNER_16=['    .Reset  ',char(10)];
     TUNER_17=['    .Name "component1:',TUNERName,'"  ',char(10)];
     TUNER_18=['    .Origin "Free"  ',char(10)];
    TUNER_19=['     .Center "0", "0", "0"  ',char(10)];
     TUNER_20=['    .Angle "-90", "0", "0"  ',char(10)];
      TUNER_21=['   .MultipleObjects "False"  ',char(10)];
      TUNER_22=['   .GroupObjects "False"  ',char(10)];
      TUNER_23=['   .Repetitions "1"  ',char(10)];
     TUNER_24=['    .MultipleSelection "False"  ',char(10)];
      TUNER_25=['   .Transform "Shape", "Rotate"  ',char(10)];
    TUNER_26=['End With              ',char(10)];
                
                
                
    
    TUNER_27=['With Transform  ',char(10)];
    TUNER_28=['     .Reset  ',char(10)];
    TUNER_29=['     .Name "component1:',TUNERName,'"  ',char(10)];
    TUNER_30=['     .Origin "Free"  ',char(10)];
    TUNER_31=['     .Center "0", "0", "0"  ',char(10)];
    TUNER_32=['    .Angle "0", "0", "TUNER_Fai_',num2str(StruTUNERm),'"  ',char(10)];
    TUNER_33=['     .MultipleObjects "False"  ',char(10)];
    TUNER_34=['     .GroupObjects "False"  ',char(10)];
    TUNER_35=['     .Repetitions "1"  ',char(10)];
    TUNER_36=['     .MultipleSelection "False"  ',char(10)];
    TUNER_37=['     .Transform "Shape", "Rotate"  ',char(10)];
    TUNER_38=['End With  ',char(10)];
    
    
    TUNER_39=['With Transform  ',char(10)];
    TUNER_40=['     .Reset  ',char(10)];
    TUNER_41=['    .Name "component1:',TUNERName,'"  ',char(10)];
    TUNER_42=['     .Vector "0", "0", "TUNER_Z_',num2str(StruTUNERm),'"  ',char(10)];
    TUNER_43=['    .UsePickedPoints "False"  ',char(10)];
    TUNER_44=['     .InvertPickedPoints "False"  ',char(10)];
    TUNER_45=['     .MultipleObjects "False"  ',char(10)];
    TUNER_46=['     .GroupObjects "False"  ',char(10)];
    TUNER_47=['     .Repetitions "1"  ',char(10)];
    TUNER_48=['     .MultipleSelection "False"  ',char(10)];
    TUNER_49=['     .Transform "Shape", "Translate"  ',char(10)];
    TUNER_50=['End With  ',char(10)];
    
    
    for i_TUNER=1:50
        NameTUNER=['TUNER_',num2str(i_TUNER)];
        fprintf(Fid,'%s',eval(NameTUNER));
    end
end
fclose(Fid);




















