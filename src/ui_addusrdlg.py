# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addusrdlg.ui'
#
# Created: Sun Aug 14 16:34:03 2011
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_AddUsrDlg(object):
    def setupUi(self, AddUsrDlg):
        AddUsrDlg.setObjectName(_fromUtf8("AddUsrDlg"))
        AddUsrDlg.resize(278, 134)
        AddUsrDlg.setWindowTitle(QtGui.QApplication.translate("AddUsrDlg", "添加用户", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalLayout = QtGui.QVBoxLayout(AddUsrDlg)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(AddUsrDlg)
        self.label.setText(QtGui.QApplication.translate("AddUsrDlg", "用户名:", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.edit_usr_name = QtGui.QLineEdit(AddUsrDlg)
        self.edit_usr_name.setObjectName(_fromUtf8("edit_usr_name"))
        self.gridLayout.addWidget(self.edit_usr_name, 0, 1, 1, 1)
        self.label_2 = QtGui.QLabel(AddUsrDlg)
        self.label_2.setText(QtGui.QApplication.translate("AddUsrDlg", "密码:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.edit_pwd = QtGui.QLineEdit(AddUsrDlg)
        self.edit_pwd.setEchoMode(QtGui.QLineEdit.Password)
        self.edit_pwd.setObjectName(_fromUtf8("edit_pwd"))
        self.gridLayout.addWidget(self.edit_pwd, 1, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtGui.QDialogButtonBox(AddUsrDlg)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(AddUsrDlg)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), AddUsrDlg.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), AddUsrDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(AddUsrDlg)

    def retranslateUi(self, AddUsrDlg):
        pass

