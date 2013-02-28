# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'AccountsManageDlg.ui'
#
# Created: Sun Aug 14 15:32:53 2011
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_AccountManageDlg(object):
    def setupUi(self, AccountManageDlg):
        AccountManageDlg.setObjectName(_fromUtf8("AccountManageDlg"))
        AccountManageDlg.resize(400, 300)
        AccountManageDlg.setWindowTitle(QtGui.QApplication.translate("AccountManageDlg", "帐号管理", None, QtGui.QApplication.UnicodeUTF8))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8(":/images/alarm_clock_red.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AccountManageDlg.setWindowIcon(icon)
        self.buttonBox = QtGui.QDialogButtonBox(AccountManageDlg)
        self.buttonBox.setGeometry(QtCore.QRect(30, 260, 341, 32))
        self.buttonBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.layoutWidget = QtGui.QWidget(AccountManageDlg)
        self.layoutWidget.setGeometry(QtCore.QRect(20, 30, 352, 214))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setText(QtGui.QApplication.translate("AccountManageDlg", "帐号列表：", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.verticalLayout.addWidget(self.label)
        self.lst_accounts = QtGui.QListWidget(self.layoutWidget)
        self.lst_accounts.setObjectName(_fromUtf8("lst_accounts"))
        self.verticalLayout.addWidget(self.lst_accounts)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.line = QtGui.QFrame(self.layoutWidget)
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.horizontalLayout.addWidget(self.line)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.btn_add = QtGui.QPushButton(self.layoutWidget)
        self.btn_add.setText(QtGui.QApplication.translate("AccountManageDlg", "添加", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_add.setObjectName(_fromUtf8("btn_add"))
        self.verticalLayout_2.addWidget(self.btn_add)
        self.btn_del = QtGui.QPushButton(self.layoutWidget)
        self.btn_del.setText(QtGui.QApplication.translate("AccountManageDlg", "删除", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_del.setObjectName(_fromUtf8("btn_del"))
        self.verticalLayout_2.addWidget(self.btn_del)
        self.btn_set_pwd = QtGui.QPushButton(self.layoutWidget)
        self.btn_set_pwd.setText(QtGui.QApplication.translate("AccountManageDlg", "重设密码", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_set_pwd.setObjectName(_fromUtf8("btn_set_pwd"))
        self.verticalLayout_2.addWidget(self.btn_set_pwd)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.retranslateUi(AccountManageDlg)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), AccountManageDlg.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), AccountManageDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(AccountManageDlg)

    def retranslateUi(self, AccountManageDlg):
        pass

import application_rc
