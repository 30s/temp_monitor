# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'setusrpwddlg.ui'
#
# Created: Sun Aug 14 18:29:59 2011
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_SetUsrPwdDlg(object):
    def setupUi(self, SetUsrPwdDlg):
        SetUsrPwdDlg.setObjectName(_fromUtf8("SetUsrPwdDlg"))
        SetUsrPwdDlg.resize(344, 147)
        SetUsrPwdDlg.setWindowTitle(QtGui.QApplication.translate("SetUsrPwdDlg", "重设密码", None, QtGui.QApplication.UnicodeUTF8))
        self.gridLayout = QtGui.QGridLayout(SetUsrPwdDlg)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(SetUsrPwdDlg)
        self.label.setText(QtGui.QApplication.translate("SetUsrPwdDlg", "新密码：", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.edit_new_pwd = QtGui.QLineEdit(SetUsrPwdDlg)
        self.edit_new_pwd.setEchoMode(QtGui.QLineEdit.Password)
        self.edit_new_pwd.setObjectName(_fromUtf8("edit_new_pwd"))
        self.gridLayout.addWidget(self.edit_new_pwd, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(SetUsrPwdDlg)
        self.label_2.setText(QtGui.QApplication.translate("SetUsrPwdDlg", "再次输入密码：", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.edit_new_pwd_2 = QtGui.QLineEdit(SetUsrPwdDlg)
        self.edit_new_pwd_2.setEchoMode(QtGui.QLineEdit.Password)
        self.edit_new_pwd_2.setObjectName(_fromUtf8("edit_new_pwd_2"))
        self.gridLayout.addWidget(self.edit_new_pwd_2, 1, 1, 1, 1)
        self.buttonBox = QtGui.QDialogButtonBox(SetUsrPwdDlg)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.gridLayout.addWidget(self.buttonBox, 2, 0, 1, 2)

        self.retranslateUi(SetUsrPwdDlg)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), SetUsrPwdDlg.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), SetUsrPwdDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(SetUsrPwdDlg)

    def retranslateUi(self, SetUsrPwdDlg):
        pass

