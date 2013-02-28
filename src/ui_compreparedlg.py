# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'compreparedlg.ui'
#
# Created: Sun Sep 04 16:11:27 2011
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_ComPrepareDlg(object):
    def setupUi(self, ComPrepareDlg):
        ComPrepareDlg.setObjectName(_fromUtf8("ComPrepareDlg"))
        ComPrepareDlg.resize(423, 412)
        ComPrepareDlg.setWindowTitle(QtGui.QApplication.translate("ComPrepareDlg", "监测准备", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalLayout = QtGui.QVBoxLayout(ComPrepareDlg)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.edit_log = QtGui.QTextEdit(ComPrepareDlg)
        self.edit_log.setReadOnly(True)
        self.edit_log.setObjectName(_fromUtf8("edit_log"))
        self.verticalLayout.addWidget(self.edit_log)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btn_start = QtGui.QPushButton(ComPrepareDlg)
        self.btn_start.setEnabled(False)
        self.btn_start.setText(QtGui.QApplication.translate("ComPrepareDlg", "开始监测", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_start.setObjectName(_fromUtf8("btn_start"))
        self.horizontalLayout.addWidget(self.btn_start)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.btn_cancel = QtGui.QPushButton(ComPrepareDlg)
        self.btn_cancel.setEnabled(False)
        self.btn_cancel.setText(QtGui.QApplication.translate("ComPrepareDlg", "取消", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_cancel.setObjectName(_fromUtf8("btn_cancel"))
        self.horizontalLayout.addWidget(self.btn_cancel)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(ComPrepareDlg)
        QtCore.QMetaObject.connectSlotsByName(ComPrepareDlg)

    def retranslateUi(self, ComPrepareDlg):
        pass

