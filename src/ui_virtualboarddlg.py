# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'virtualboarddlg.ui'
#
# Created: Wed Oct 26 22:13:45 2011
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_VirtualBoardDlg(object):
    def setupUi(self, VirtualBoardDlg):
        VirtualBoardDlg.setObjectName(_fromUtf8("VirtualBoardDlg"))
        VirtualBoardDlg.resize(400, 300)
        VirtualBoardDlg.setWindowTitle(QtGui.QApplication.translate("VirtualBoardDlg", "虚拟监控板", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalLayout = QtGui.QVBoxLayout(VirtualBoardDlg)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(VirtualBoardDlg)
        self.label.setText(QtGui.QApplication.translate("VirtualBoardDlg", "当前温度：", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.spin_temp = QtGui.QSpinBox(VirtualBoardDlg)
        self.spin_temp.setProperty("value", 49)
        self.spin_temp.setObjectName(_fromUtf8("spin_temp"))
        self.horizontalLayout.addWidget(self.spin_temp)
        self.chk_random = QtGui.QCheckBox(VirtualBoardDlg)
        self.chk_random.setText(QtGui.QApplication.translate("VirtualBoardDlg", "随机模式", None, QtGui.QApplication.UnicodeUTF8))
        self.chk_random.setObjectName(_fromUtf8("chk_random"))
        self.horizontalLayout.addWidget(self.chk_random)
        self.chk_err = QtGui.QCheckBox(VirtualBoardDlg)
        self.chk_err.setText(QtGui.QApplication.translate("VirtualBoardDlg", "传感器错误", None, QtGui.QApplication.UnicodeUTF8))
        self.chk_err.setObjectName(_fromUtf8("chk_err"))
        self.horizontalLayout.addWidget(self.chk_err)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.buttonBox = QtGui.QDialogButtonBox(VirtualBoardDlg)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(VirtualBoardDlg)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), VirtualBoardDlg.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), VirtualBoardDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(VirtualBoardDlg)

    def retranslateUi(self, VirtualBoardDlg):
        pass

