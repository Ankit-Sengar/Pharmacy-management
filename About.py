# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'About.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ABOUT(object):
    def setupUi(self, ABOUT):
        ABOUT.setObjectName("ABOUT")
        ABOUT.resize(401, 191)
        self.verticalLayout = QtWidgets.QVBoxLayout(ABOUT)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(ABOUT)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_3 = QtWidgets.QLabel(ABOUT)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.label_4 = QtWidgets.QLabel(ABOUT)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.label_5 = QtWidgets.QLabel(ABOUT)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.label_6 = QtWidgets.QLabel(ABOUT)
        font = QtGui.QFont()
        font.setFamily("Segoe Print")
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.label_2 = QtWidgets.QLabel(ABOUT)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)

        self.retranslateUi(ABOUT)
        QtCore.QMetaObject.connectSlotsByName(ABOUT)

    def retranslateUi(self, ABOUT):
        _translate = QtCore.QCoreApplication.translate
        ABOUT.setWindowTitle(_translate("ABOUT", "Dialog"))
        self.label.setText(_translate("ABOUT", "DEVELOPED BY:"))
        self.label_3.setText(_translate("ABOUT", "ANKIT SENGAR"))
        self.label_4.setText(_translate("ABOUT", "DEVESH  KUMAR SINGH"))
        self.label_5.setText(_translate("ABOUT", "GL BAJAJ INSTITUTE OF TECHNOLOGY AND"))
        self.label_6.setText(_translate("ABOUT", "MANAGEMENT"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ABOUT = QtWidgets.QDialog()
    ui = Ui_ABOUT()
    ui.setupUi(ABOUT)
    ABOUT.show()
    sys.exit(app.exec_())
