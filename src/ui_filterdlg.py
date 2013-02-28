# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'filterdlg.ui'
#
# Created: Wed Dec 28 21:37:40 2011
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_FilterDlg(object):
    def setupUi(self, FilterDlg):
        FilterDlg.setObjectName(_fromUtf8("FilterDlg"))
        FilterDlg.resize(400, 223)
        FilterDlg.setWindowTitle(QtGui.QApplication.translate("FilterDlg", "曲线过滤", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalLayout = QtGui.QVBoxLayout(FilterDlg)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.label_3 = QtGui.QLabel(FilterDlg)
        self.label_3.setText(QtGui.QApplication.translate("FilterDlg", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'宋体\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600; color:#aa0000;\">注意！</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; color:#aa0000;\">超出过滤上下限的值将在曲线中显示空白,</span></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:11pt; color:#aa0000;\">要查看过滤前的数据请重新查询！</span></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.formLayout = QtGui.QFormLayout()
        self.formLayout.setObjectName(_fromUtf8("formLayout"))
        self.label = QtGui.QLabel(FilterDlg)
        self.label.setText(QtGui.QApplication.translate("FilterDlg", "过滤上限：", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.label)
        self.spin_hig = QtGui.QSpinBox(FilterDlg)
        self.spin_hig.setAlignment(QtCore.Qt.AlignCenter)
        self.spin_hig.setButtonSymbols(QtGui.QAbstractSpinBox.UpDownArrows)
        self.spin_hig.setSuffix(QtGui.QApplication.translate("FilterDlg", " ℃", None, QtGui.QApplication.UnicodeUTF8))
        self.spin_hig.setMinimum(-1000)
        self.spin_hig.setMaximum(1000)
        self.spin_hig.setObjectName(_fromUtf8("spin_hig"))
        self.formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.spin_hig)
        self.label_2 = QtGui.QLabel(FilterDlg)
        self.label_2.setText(QtGui.QApplication.translate("FilterDlg", "过滤下限：", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.label_2)
        self.spin_low = QtGui.QSpinBox(FilterDlg)
        self.spin_low.setAlignment(QtCore.Qt.AlignCenter)
        self.spin_low.setSuffix(QtGui.QApplication.translate("FilterDlg", " ℃", None, QtGui.QApplication.UnicodeUTF8))
        self.spin_low.setMinimum(-1000)
        self.spin_low.setMaximum(1000)
        self.spin_low.setObjectName(_fromUtf8("spin_low"))
        self.formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.spin_low)
        self.horizontalLayout.addLayout(self.formLayout)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem = QtGui.QSpacerItem(20, 38, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.buttonBox = QtGui.QDialogButtonBox(FilterDlg)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(FilterDlg)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), FilterDlg.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), FilterDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(FilterDlg)

    def retranslateUi(self, FilterDlg):
        pass

