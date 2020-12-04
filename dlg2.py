# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Records.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog2(object):
    def setupUi(self, Dialog2):
        Dialog2.setObjectName("Dialog2")
        Dialog2.resize(1008, 644)
        Dialog2.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.label = QtWidgets.QLabel(Dialog2)
        self.label.setGeometry(QtCore.QRect(290, 0, 191, 41))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(28)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.custid = QtWidgets.QLineEdit(Dialog2)
        self.custid.setGeometry(QtCore.QRect(140, 90, 113, 20))
        self.custid.setObjectName("custid")
        self.label_2 = QtWidgets.QLabel(Dialog2)
        self.label_2.setGeometry(QtCore.QRect(30, 90, 111, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(9)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.srch = QtWidgets.QPushButton(Dialog2)
        self.srch.setGeometry(QtCore.QRect(270, 90, 141, 23))
        self.srch.setObjectName("srch")
        self.list1 = QtWidgets.QTableWidget(Dialog2)
        self.list1.setGeometry(QtCore.QRect(20, 190, 561, 451))
        self.list1.setRowCount(11)
        self.list1.setColumnCount(4)
        self.list1.setObjectName("list1")
        self.list2 = QtWidgets.QTableWidget(Dialog2)
        self.list2.setGeometry(QtCore.QRect(600, 200, 401, 81))
        self.list2.setRowCount(1)
        self.list2.setColumnCount(3)
        self.list2.setObjectName("list2")
        self.label_3 = QtWidgets.QLabel(Dialog2)
        self.label_3.setGeometry(QtCore.QRect(170, 130, 151, 20))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog2)
        self.label_4.setGeometry(QtCore.QRect(720, 120, 191, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(12)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog2)
        self.label_5.setGeometry(QtCore.QRect(200, 170, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(9)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(Dialog2)
        self.label_6.setGeometry(QtCore.QRect(320, 165, 81, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(9)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(Dialog2)
        self.label_7.setGeometry(QtCore.QRect(450, 170, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(9)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(Dialog2)
        self.label_8.setGeometry(QtCore.QRect(630, 160, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(9)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(Dialog2)
        self.label_9.setGeometry(QtCore.QRect(780, 160, 47, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(9)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(Dialog2)
        self.label_10.setGeometry(QtCore.QRect(920, 160, 47, 31))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(9)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(Dialog2)
        self.label_11.setGeometry(QtCore.QRect(90, 170, 47, 21))
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")

        self.srch.clicked.connect(self.record)

        self.retranslateUi(Dialog2)
        QtCore.QMetaObject.connectSlotsByName(Dialog2)

    def retranslateUi(self, Dialog2):
        _translate = QtCore.QCoreApplication.translate
        Dialog2.setWindowTitle(_translate("Dialog2", "Dialog"))
        self.label.setText(_translate("Dialog2", "RECORDS"))
        self.label_2.setText(_translate("Dialog2", "Customer Id"))
        self.srch.setText(_translate("Dialog2", "SEARCH"))
        self.label_3.setText(_translate("Dialog2", "Medicine Info"))
        self.label_4.setText(_translate("Dialog2", "Customer Info"))
        self.label_5.setText(_translate("Dialog2", "Medicine "))
        self.label_6.setText(_translate("Dialog2", "Quantity"))
        self.label_7.setText(_translate("Dialog2", "Price"))
        self.label_8.setText(_translate("Dialog2", "CustomerID"))
        self.label_9.setText(_translate("Dialog2", "Name"))
        self.label_10.setText(_translate("Dialog2", "Age"))
        self.label_11.setText(_translate("Dialog2", "DATE"))

    def record(self,text):
        import sqlite3
        customerid=self.custid.text()
        connection=sqlite3.connect('MRECORD.db')
        result=connection.execute('''SELECT * FROM {}'''.format(customerid))
        self.list1.setRowCount(0)
        for row_number,row_data in enumerate(result):
            self.list1.insertRow(row_number)
            for column_number,data in enumerate(row_data):
                self.list1.setItem(row_number,column_number,QtWidgets.QTableWidgetItem(str(data)))
        connection.close()
        connection1=sqlite3.connect('CRECORD.db')
        result1=connection1.execute('''SELECT * FROM Record WHERE CustId='{}' '''.format(customerid))
        self.list2.setRowCount(0)
        for row_number,row_data in enumerate(result1):
            self.list2.insertRow(row_number)
            for column_number,data in enumerate(row_data):
                self.list2.setItem(row_number,column_number,QtWidgets.QTableWidgetItem(str(data)))

        connection1.close()




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog2 = QtWidgets.QDialog()
    ui = Ui_Dialog2()
    ui.setupUi(Dialog2)
    Dialog2.show()
    sys.exit(app.exec_())
