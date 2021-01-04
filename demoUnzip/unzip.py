# -*- coding: utf-8 -*-
"""
Created on Mon Dec 28 11:36:41 2020

@author: 86152
"""
import sys
import zipfile
import os
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from PyQt5 import QtWidgets
from unzipWindow_2 import Ui_Dialog




class MainForm(QMainWindow, Ui_Dialog):
    def __init__(self):
        super(MainForm, self).__init__()
        self.setupUi(self)
        #
        # self.zip_path='E:/Ex/file.zip'
        # self.out_zip_path='E:/Ex/out1/'
        self.zip_path = []
        self.out_zip_path = 'E:/'
        
        
        self.pushButton_Open.clicked.connect(self.OpenFile)
        self.pushButton_Unzip.clicked.connect(lambda: self.Unzip(self.zip_path,self.out_zip_path))
        self.pushButton_Extract.clicked.connect(self.ExtractFile)
        
        
    def OpenFile(self):
        #打开多个文件（加s)
        fileName_choose, filetype = QFileDialog.getOpenFileNames(self,  "Open Many File",  "E:/Ex/","All Files(*);;Text Files(*.zip)")   # 设置文件扩展名过滤,用双分号间隔
        self.zip_path = fileName_choose
        print(self.zip_path)
        
        
        #分解文件路径和文件名       
        filePath,tempFilename = os.path.split(fileName_choose[0])
        # passfilename,extension= os.path.splitext(tempFilename)
        self.out_zip_path = filePath + "/"
        print(self.out_zip_path)
        # print(tempFilename)
        
       
    def ExtractFile(self):
        dir_choose = QFileDialog.getExistingDirectory(self, "选取文件夹", "E:/") # 起始路径
        self.out_zip_path = dir_choose + "/"
        print(self.out_zip_path)
    
    def Unzip(self, zip_path, out_zip_path):
        for m_zipPath in zip_path:
            print(m_zipPath)
            self.unzip_file(m_zipPath,out_zip_path)
    
        
    
    def unzip_file(self,zip_path,out_zip_path):
        #获取压缩文件的名字
        filePath,tempFilename = os.path.split(zip_path)
        Zipfilename,extension= os.path.splitext(tempFilename)
        
        
        z =zipfile.ZipFile(zip_path, 'r')
        #遍历每一个对象
        for f in z.namelist():
            #获取后缀名
            print(f)
            filename,endsName= os.path.splitext(f)
            
            if endsName == ".pdf":             
                z.extract(f, out_zip_path) #解压到文件夹 pdf
                #更改文件名字，和压缩包名称一致
                Olddir = out_zip_path + f
                Newdir = out_zip_path + Zipfilename +".pdf"
                os.rename(Olddir, Newdir)
            elif endsName == ".zip":
                z.extract(f, out_zip_path) #解压到文件夹 zip
                new_path = os.path.join(out_zip_path,f)
                self.unzip_file(new_path , out_zip_path)
            else:
                continue
        
    

    

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_())
    

