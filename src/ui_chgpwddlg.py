# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'chgpwddlg.ui'
#
# Created: Thu Aug 18 20:39:23 2011
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ChgPwdDlg(object):
    def setupUi(self, ChgPwdDlg):
        ChgPwdDlg.setObjectName(_fromUtf8("ChgPwdDlg"))
        ChgPwdDlg.resize(314, 156)
        ChgPwdDlg.setWindowTitle(QtGui.QApplication.translate("ChgPwdDlg", "修改密码", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalLayout = QtGui.QVBoxLayout(ChgPwdDlg)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(ChgPwdDlg)
        self.label.setText(QtGui.QApplication.translate("ChgPwdDlg", "旧密码：", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.edit_old_pwd = QtGui.QLineEdit(ChgPwdDlg)
        self.edit_old_pwd.setEchoMode(QtGui.QLineEdit.Password)
        self.edit_old_pwd.setObjectName(_fromUtf8("edit_old_pwd"))
        self.gridLayout.addWidget(self.edit_old_pwd, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(ChgPwdDlg)
        self.label_2.setText(QtGui.QApplication.translate("ChgPwdDlg", "新密码：", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.edit_new_pwd = QtGui.QLineEdit(ChgPwdDlg)
        self.edit_new_pwd.setEchoMode(QtGui.QLineEdit.Password)
        self.edit_new_pwd.setObjectName(_fromUtf8("edit_new_pwd"))
        self.gridLayout.addWidget(self.edit_new_pwd, 1, 1, 1, 1)
        self.label_3 = QtGui.QLabel(ChgPwdDlg)
        self.label_3.setText(QtGui.QApplication.translate("ChgPwdDlg", "确认密码：", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.edit_new_pwd_2 = QtGui.QLineEdit(ChgPwdDlg)
        self.edit_new_pwd_2.setEchoMode(QtGui.QLineEdit.Password)
        self.edit_new_pwd_2.setObjectName(_fromUtf8("edit_new_pwd_2"))
        self.gridLayout.addWidget(self.edit_new_pwd_2, 2, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        spacerItem = QtGui.QSpacerItem(20, 24, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.btn_ok = QtGui.QPushButton(ChgPwdDlg)
        self.btn_ok.setText(QtGui.QApplication.translate("ChgPwdDlg", "确定", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_ok.setObjectName(_fromUtf8("btn_ok"))
        self.horizontalLayout.addWidget(self.btn_ok)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.btn_cancel = QtGui.QPushButton(ChgPwdDlg)
        self.btn_cancel.setText(QtGui.QApplication.translate("ChgPwdDlg", "取消", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_cancel.setObjectName(_fromUtf8("btn_cancel"))
        self.horizontalLayout.addWidget(self.btn_cancel)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(ChgPwdDlg)
        QtCore.QMetaObject.connectSlotsByName(ChgPwdDlg)

    def retranslateUi(self, ChgPwdDlg):
        pass

