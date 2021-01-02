# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'unzipWindow.ui'
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
        self.label.setGeometry(QtCore.QRect(240, 90, 91, 31))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(200, 190, 151, 51))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "UnzipSoftware"))
        self.label.setText(_translate("Dialog", "hello world"))
        self.pushButton.setText(_translate("Dialog", "hello world"))

