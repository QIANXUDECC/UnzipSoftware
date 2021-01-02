# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'unzipWindow_1.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(601, 516)
        font = QtGui.QFont()
        font.setFamily("3ds")
        font.setPointSize(11)
        Dialog.setFont(font)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(230, 100, 91, 31))
        self.label.setObjectName("label")
        self.pushButton_Unzip = QtWidgets.QPushButton(Dialog)
        self.pushButton_Unzip.setGeometry(QtCore.QRect(290, 210, 141, 71))
        self.pushButton_Unzip.setObjectName("pushButton_Unzip")
        self.pushButton_Open = QtWidgets.QPushButton(Dialog)
        self.pushButton_Open.setGeometry(QtCore.QRect(100, 210, 141, 71))
        self.pushButton_Open.setObjectName("pushButton_Open")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "UnzipSoftware"))
        self.label.setText(_translate("Dialog", "hello world"))
        self.pushButton_Unzip.setText(_translate("Dialog", "unzip"))
        self.pushButton_Open.setText(_translate("Dialog", "Open"))

