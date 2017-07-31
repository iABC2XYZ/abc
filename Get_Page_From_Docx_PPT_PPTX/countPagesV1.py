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


folderDealTmp=input('请输入总文件夹的绝对路径: \n')

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
    StatisticFile=root+'\\统计.txt'
    with open(StatisticFile,'w') as fid:
        pass

for root, dirs, files in os.walk(folderDeal, topdown=False):
    StatisticFile=root+'\\统计.txt'
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
                
                
        fid.writelines('本文件夹所有DOCX共有页数：    '+str(pagesTotal)+'\n\n\n\n\n\n')
       

for root, dirs, files in os.walk(folderDeal, topdown=False):
    
    StatisticFile=root+'\\统计.txt'
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
                
                
        fid.writelines('本文件夹所有PPT/PPTX共有页数：    '+str(pagesTotal)+'\n\n\n\n\n\n')



print('结束，请查看！')







