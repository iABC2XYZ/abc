# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 18:34:40 2017

@author: Peiyong Jiang :jiangpeiyong@impcas.ac.cn
         Wangsheng Wang : wwshunan@impcas.ac.cn
         Chi Feng  : fengchi@impcas.ac.cn
         
         supervised by
         Zhijun Wang  & Yuan He

             
"""

import os
from win32com.client import Dispatch


folderDealTmp=input('Please input the absolute path of the father-folder:\n')

folderDeal=folderDealTmp.replace('\\','\\\\')

def GetPage5Docx(fileNameWithPath):
    #open Word
    word = Dispatch('Word.Application')
    word.Visible = False
    word = word.Documents.Open(fileNameWithPath)
    
    #get number of sheets
    word.Repaginate()
    num_of_sheets = word.ComputeStatistics(2)
    
    return num_of_sheets

def GetPage5PPT(fileNameWithPath):
    Application = Dispatch("PowerPoint.Application")
    Presentation = Application.Presentations.Open(fileNameWithPath, WithWindow=False)
    slide_count = len(Presentation.Slides)
    Presentation.Close()
    return slide_count


for root, dirs, files in os.walk(folderDeal, topdown=False):
    StatisticFile=root+'\\Counter.txt'
    with open(StatisticFile,'w') as fid:
        pass

for root, dirs, files in os.walk(folderDeal, topdown=False):
    StatisticFile=root+'\\Counter.txt'
    with open(StatisticFile,'a+') as fid:
        pagesTotal=0
        for name in files:
            nameFile=os.path.join(root, name)
            
            mainFile,appdFile=os.path.splitext(nameFile)
            mainFolder,fullFile=os.path.split(nameFile)
            if (appdFile=='.docx') and (fullFile[0:2]!='~$'):   
                pagesThis=GetPage5Docx(nameFile)
                fid.writelines(fullFile+'    '+str(pagesThis)+'\n')
                pagesTotal+=pagesThis
                
                
        fid.writelines('All Docx files in this folder have the pages:  '+str(pagesTotal)+'\n\n\n\n\n\n')
       

for root, dirs, files in os.walk(folderDeal, topdown=False):
    
    StatisticFile=root+'\\Counter.txt'
    with open(StatisticFile,'a+') as fid:
        pagesTotal=0
        for name in files:
            nameFile=os.path.join(root, name)
            
            mainFile,appdFile=os.path.splitext(nameFile)
            mainFolder,fullFile=os.path.split(nameFile)
            if ((appdFile=='.pptx') or (appdFile=='.ppt')) and (fullFile[0:2]!='~$'):   
                pagesThis=GetPage5PPT(nameFile)
                fid.writelines(fullFile+'    '+str(pagesThis)+'\n')
                pagesTotal+=pagesThis
                
                
        fid.writelines('All PPT/PPTX files in this folder have the pages:    '+str(pagesTotal)+'\n\n\n\n\n\n')



print('Done. Please check it!')







