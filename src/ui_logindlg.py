# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'logindlg.ui'
#
# Created: Thu Aug 18 12:50:19 2011
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_LoginDlg(object):
    def setupUi(self, LoginDlg):
        LoginDlg.setObjectName(_fromUtf8("LoginDlg"))
        LoginDlg.resize(290, 183)
        LoginDlg.setWindowTitle(QtGui.QApplication.translate("LoginDlg", "登录", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalLayout = QtGui.QVBoxLayout(LoginDlg)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(LoginDlg)
        self.label.setText(QtGui.QApplication.translate("LoginDlg", "<h1>温度监测系统</h1>", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        spacerItem = QtGui.QSpacerItem(20, 17, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label_2 = QtGui.QLabel(LoginDlg)
        self.label_2.setText(QtGui.QApplication.translate("LoginDlg", "用户名：", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.edit_usr_name = QtGui.QLineEdit(LoginDlg)
        self.edit_usr_name.setObjectName(_fromUtf8("edit_usr_name"))
        self.gridLayout.addWidget(self.edit_usr_name, 0, 1, 1, 1)
        self.label_3 = QtGui.QLabel(LoginDlg)
        self.label_3.setText(QtGui.QApplication.translate("LoginDlg", "密码：", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.edit_pwd = QtGui.QLineEdit(LoginDlg)
        self.edit_pwd.setEchoMode(QtGui.QLineEdit.Password)
        self.edit_pwd.setObjectName(_fromUtf8("edit_pwd"))
        self.gridLayout.addWidget(self.edit_pwd, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem1 = QtGui.QSpacerItem(20, 18, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.btn_login = QtGui.QPushButton(LoginDlg)
        self.btn_login.setText(QtGui.QApplication.translate("LoginDlg", "登录", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_login.setObjectName(_fromUtf8("btn_login"))
        self.horizontalLayout.addWidget(self.btn_login)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.btn_cancel = QtGui.QPushButton(LoginDlg)
        self.btn_cancel.setText(QtGui.QApplication.translate("LoginDlg", "取消", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_cancel.setObjectName(_fromUtf8("btn_cancel"))
        self.horizontalLayout.addWidget(self.btn_cancel)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(LoginDlg)
        QtCore.QMetaObject.connectSlotsByName(LoginDlg)

    def retranslateUi(self, LoginDlg):
        pass

