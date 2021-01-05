# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 16:01:29 2021

@author: 86152
"""


import sys
import os
import zipfile
from PyQt5 import QtCore
from PyQt5.Qt import QFileDialog,QTreeWidget,QFileSystemModel,QStandardItem,QHBoxLayout,QMainWindow,QTreeView,QStandardItemModel,QDirModel,QStyleFactory
from PyQt5 import QtWidgets
from software2 import Ui_Dialog




class MainForm(QMainWindow, Ui_Dialog):
    def __init__(self):
        super(MainForm, self).__init__()
        self.setupUi(self)
        
        
        self.Path = ""
        self.zipPathName = []
        self.outZipPath =""
       
        
        #获取系统所有文件
        self.model01 = QFileSystemModel()
        #进行筛选只显示文件夹，不显示文件和特色文件
        self.model01.setFilter(QtCore.QDir.Dirs|QtCore.QDir.NoDotAndDotDot)
        self.model01.setRootPath("/")
        # self.treeWidget1 = QTreeWidget()
        # self.treeWidget1.setModel(self.model01)
        
        
        # self.dir_model = QDirModel()
        #定义创建左边窗口
        self.treeView.setModel(self.model01) 
        for col in range(1, 4):
            self.treeView.setColumnHidden(col, True)
        self.treeView.doubleClicked.connect(self.initUI)
        #设置成有虚线连接的方式
        self.treeView.setStyle(QStyleFactory.create('windows'))
        
        
        
        
        #定义创建右边窗口
        self.model02 = QStandardItemModel()
        self.treeView_2.setModel(self.model02)
        
        
       
        #将创建的窗口进行添加
        self.layout = QHBoxLayout()
        self.layout.addWidget(self.treeView)
        self.layout.addWidget(self.treeView_2)
        self.setLayout(self.layout)
        
        #打开文件夹
        self.pushButton.clicked.connect(self.OpenFile)
        #获取选中的文件名
        self.pushButton_2.clicked.connect(self.getFileName)
        #设定解压文件的位置
        self.pushButton_3.clicked.connect(self.ExtractFile)
        #self.pushButton_2.clicked.connect(lambda: self.Unzip(self.zipPathName,self.outZipPath))
        
    def OpenFile(self):
        
        #数组清零
        self.zipPathName.clear()
        #打开多个文件（加s)
        fileName_choose, filetype = QFileDialog.getOpenFileNames(self,  "Open Many File",  "E:/Ex/","All Files(*);;Text Files(*.zip)")   # 设置文件扩展名过滤,用双分号间隔
        self.zipPathName =  fileName_choose
        print(self.zipPathName)
        
        
        #分解文件路径和文件名       
        filePath,tempFilename = os.path.split(fileName_choose[0])
        self.outZipPath = filePath + "/"
        print(self.outZipPath)
        # # print(tempFilename)
        
    def ExtractFile(self):
        dir_choose = QFileDialog.getExistingDirectory(self, "选取文件夹", "E:/") # 起始路径
        self.outZipPath = dir_choose + "/"
        print(self.outZipPath)
        
    def getFileName(self):
        
        #数组清零
        self.zipPathName.clear()
        
        itemList = self.model02.findItems("*",QtCore.Qt.MatchWildcard )    
        count = len(itemList)#返回列表中的数量
        
        
        if(count > 0):
            for row in range(len(itemList)):
                item = itemList[row]
                if item.checkState() == QtCore.Qt.Checked:
                    # print(item.text())
                    pathName = os.path.join(self.Path,item.text() )
                    self.zipPathName.append(pathName)
        # self.outZipPath = self.Path
        
        
        for m_zipPath in self.zipPathName:
            print(m_zipPath)
            self.unzip_file(m_zipPath,self.outZipPath)
        
        
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
     
            
     
    def initUI(self, Qmodelidx):
        #每次点击清空右边窗口数据
        self.model02.clear()
        
        #定义一个数组存储路径下的所有文件
        PathData = []
        #获取双击后的指定路径
        filePath = self.model01.filePath(Qmodelidx)
        self.Path = filePath +"/"  #绝对路径
        
        # List窗口文件赋值
        PathDataName = self.model02.invisibleRootItem()
        #拿到文件夹下的所有文件
        PathDataSet = os.listdir(filePath)
        #进行将拿到的数据进行排序
        PathDataSet.sort()
        #遍历判断拿到的文件是文件夹还是文件，Flase为文件，True为文件夹
        for Data in range(len(PathDataSet)):
            if os.path.isdir(filePath + '\\' + PathDataSet[Data]) == False:
                PathData.append(PathDataSet[Data])
            elif os.path.isdir(filePath + '\\' + PathDataSet[Data]) == True:
                print('2')
        
        #将拿到的所有文件放到数组中进行右边窗口赋值。
        for got in range(len(PathData)):
            gosData = QStandardItem(PathData[got])
            gosData.setCheckable(True)
            PathDataName.setChild(got, gosData)
        

        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainForm()
    window.show()
    sys.exit(app.exec_())
    
    
    
    
    