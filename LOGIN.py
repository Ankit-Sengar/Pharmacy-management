# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LOGIN.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1122, 866)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.log = QtWidgets.QPushButton(self.centralwidget)
        self.log.setGeometry(QtCore.QRect(470, 530, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.log.setFont(font)
        self.log.setObjectName("log")
        self.usr = QtWidgets.QLineEdit(self.centralwidget)
        self.usr.setGeometry(QtCore.QRect(470, 411, 181, 31))
        self.usr.setObjectName("usr")
        self.pswd = QtWidgets.QLineEdit(self.centralwidget)
        self.pswd.setGeometry(QtCore.QRect(472, 460, 181, 31))
        self.pswd.setEchoMode(QtWidgets.QLineEdit.Password)
        self.pswd.setObjectName("pswd")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(360, 410, 101, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(360, 460, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(390, 90, 341, 151))
        font = QtGui.QFont()
        font.setFamily("Playbill")
        font.setPointSize(72)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(340, 230, 431, 91))
        font = QtGui.QFont()
        font.setFamily("Playbill")
        font.setPointSize(72)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.stat = QtWidgets.QLineEdit(self.centralwidget)
        self.stat.setGeometry(QtCore.QRect(470, 600, 181, 22))
        self.stat.setObjectName("stat")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1122, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.log.clicked.connect(self.LOGIN)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.log.setText(_translate("MainWindow", "LOGIN"))
        self.label.setText(_translate("MainWindow", "USERNAME"))
        self.label_2.setText(_translate("MainWindow", "PASSWORD"))
        self.label_3.setText(_translate("MainWindow", "PHARMACY"))
        self.label_4.setText(_translate("MainWindow", "MANAGEMENT"))

    def LOGIN(self,text):
        if self.usr.text()=='ANKIT' and self.pswd.text()=='123' or self.usr.text()=='DEVESH' and self.pswd.text()=='123':
            self.stat.setText("LOGIN SUCCESS")
            self.usr.setText("")
            self.pswd.setText("")
            from dlg1 import Ui_vit
            vit = QtWidgets.QDialog()
            ui = Ui_vit()
            ui.setupUi(vit)
            vit.show()
            #print("effieh")
            ret=vit.exec_()
        else:
          self.usr.setText("")
          self.pswd.setText("")
          self.stat.setText("LOGIN FAIL")



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
