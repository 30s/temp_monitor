# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'curvedlg.ui'
#
# Created: Sun Sep 11 18:39:33 2011
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_CurveDlg(object):
    def setupUi(self, CurveDlg):
        CurveDlg.setObjectName(_fromUtf8("CurveDlg"))
        CurveDlg.resize(716, 512)
        CurveDlg.setWindowTitle(QtGui.QApplication.translate("CurveDlg", "曲线图", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalLayout = QtGui.QVBoxLayout(CurveDlg)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        spacerItem = QtGui.QSpacerItem(248, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 0, 1, 1)
        self.lcd_temp = QtGui.QLCDNumber(CurveDlg)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lcd_temp.sizePolicy().hasHeightForWidth())
        self.lcd_temp.setSizePolicy(sizePolicy)
        self.lcd_temp.setMaximumSize(QtCore.QSize(100, 16777215))
        self.lcd_temp.setAutoFillBackground(True)
        self.lcd_temp.setLineWidth(1)
        self.lcd_temp.setSmallDecimalPoint(False)
        self.lcd_temp.setNumDigits(2)
        self.lcd_temp.setDigitCount(2)
        self.lcd_temp.setSegmentStyle(QtGui.QLCDNumber.Filled)
        self.lcd_temp.setObjectName(_fromUtf8("lcd_temp"))
        self.gridLayout.addWidget(self.lcd_temp, 0, 1, 3, 1)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_3 = QtGui.QLabel(CurveDlg)
        self.label_3.setText(QtGui.QApplication.translate("CurveDlg", "巴氏消毒完成度：", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout.addWidget(self.label_3)
        self.prog_pasteu = QtGui.QProgressBar(CurveDlg)
        self.prog_pasteu.setProperty("value", 0)
        self.prog_pasteu.setObjectName(_fromUtf8("prog_pasteu"))
        self.horizontalLayout.addWidget(self.prog_pasteu)
        self.label_2 = QtGui.QLabel(CurveDlg)
        self.label_2.setText(QtGui.QApplication.translate("CurveDlg", "当前温度：", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(248, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.wdt_mpl = MplWidget(CurveDlg)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wdt_mpl.sizePolicy().hasHeightForWidth())
        self.wdt_mpl.setSizePolicy(sizePolicy)
        self.wdt_mpl.setObjectName(_fromUtf8("wdt_mpl"))
        self.verticalLayout.addWidget(self.wdt_mpl)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.btn_query = QtGui.QPushButton(CurveDlg)
        self.btn_query.setText(QtGui.QApplication.translate("CurveDlg", "历史数据查询", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_query.setObjectName(_fromUtf8("btn_query"))
        self.horizontalLayout_2.addWidget(self.btn_query)
        self.btn_quit = QtGui.QPushButton(CurveDlg)
        self.btn_quit.setText(QtGui.QApplication.translate("CurveDlg", "退出", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_quit.setObjectName(_fromUtf8("btn_quit"))
        self.horizontalLayout_2.addWidget(self.btn_quit)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.label = QtGui.QLabel(CurveDlg)
        self.label.setText(QtGui.QApplication.translate("CurveDlg", "当前时间：", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout_2.addWidget(self.label)
        self.edit_cur_time = QtGui.QLineEdit(CurveDlg)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edit_cur_time.sizePolicy().hasHeightForWidth())
        self.edit_cur_time.setSizePolicy(sizePolicy)
        self.edit_cur_time.setMaxLength(20)
        self.edit_cur_time.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.edit_cur_time.setReadOnly(True)
        self.edit_cur_time.setObjectName(_fromUtf8("edit_cur_time"))
        self.horizontalLayout_2.addWidget(self.edit_cur_time)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(CurveDlg)
        QtCore.QMetaObject.connectSlotsByName(CurveDlg)

    def retranslateUi(self, CurveDlg):
        pass

from mplwidget import MplWidget
