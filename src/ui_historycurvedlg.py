# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'historycurvedlg.ui'
#
# Created: Mon Dec 19 22:01:59 2011
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_HistoryCurveDlg(object):
    def setupUi(self, HistoryCurveDlg):
        HistoryCurveDlg.setObjectName(_fromUtf8("HistoryCurveDlg"))
        HistoryCurveDlg.setWindowModality(QtCore.Qt.ApplicationModal)
        HistoryCurveDlg.resize(1024, 480)
        HistoryCurveDlg.setWindowTitle(QtGui.QApplication.translate("HistoryCurveDlg", "历史记录曲线", None, QtGui.QApplication.UnicodeUTF8))
        HistoryCurveDlg.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.verticalLayout = QtGui.QVBoxLayout(HistoryCurveDlg)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.wdgt_curve = MplWidget(HistoryCurveDlg)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wdgt_curve.sizePolicy().hasHeightForWidth())
        self.wdgt_curve.setSizePolicy(sizePolicy)
        self.wdgt_curve.setObjectName(_fromUtf8("wdgt_curve"))
        self.lst_sensors = QtGui.QListWidget(self.wdgt_curve)
        self.lst_sensors.setGeometry(QtCore.QRect(440, 30, 100, 300))
        self.lst_sensors.setObjectName(_fromUtf8("lst_sensors"))
        self.verticalLayout.addWidget(self.wdgt_curve)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label = QtGui.QLabel(HistoryCurveDlg)
        self.label.setText(QtGui.QApplication.translate("HistoryCurveDlg", "起始时间：", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.horizontalLayout.addWidget(self.label)
        self.dt_start = QtGui.QDateTimeEdit(HistoryCurveDlg)
        self.dt_start.setDisplayFormat(QtGui.QApplication.translate("HistoryCurveDlg", "yyyy-MM-dd HH:mm:ss", None, QtGui.QApplication.UnicodeUTF8))
        self.dt_start.setObjectName(_fromUtf8("dt_start"))
        self.horizontalLayout.addWidget(self.dt_start)
        self.label_2 = QtGui.QLabel(HistoryCurveDlg)
        self.label_2.setText(QtGui.QApplication.translate("HistoryCurveDlg", "结束时间：", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        self.dt_end = QtGui.QDateTimeEdit(HistoryCurveDlg)
        self.dt_end.setDisplayFormat(QtGui.QApplication.translate("HistoryCurveDlg", "yyyy-MM-dd HH:mm:ss", None, QtGui.QApplication.UnicodeUTF8))
        self.dt_end.setObjectName(_fromUtf8("dt_end"))
        self.horizontalLayout.addWidget(self.dt_end)
        self.btn_choose_sensors = QtGui.QPushButton(HistoryCurveDlg)
        self.btn_choose_sensors.setText(QtGui.QApplication.translate("HistoryCurveDlg", "选择传感器...", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_choose_sensors.setObjectName(_fromUtf8("btn_choose_sensors"))
        self.horizontalLayout.addWidget(self.btn_choose_sensors)
        self.btn_filter = QtGui.QPushButton(HistoryCurveDlg)
        self.btn_filter.setText(QtGui.QApplication.translate("HistoryCurveDlg", "过滤...", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_filter.setObjectName(_fromUtf8("btn_filter"))
        self.horizontalLayout.addWidget(self.btn_filter)
        self.btn_update = QtGui.QPushButton(HistoryCurveDlg)
        self.btn_update.setText(QtGui.QApplication.translate("HistoryCurveDlg", "刷新", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_update.setObjectName(_fromUtf8("btn_update"))
        self.horizontalLayout.addWidget(self.btn_update)
        self.btn_revert = QtGui.QPushButton(HistoryCurveDlg)
        self.btn_revert.setText(QtGui.QApplication.translate("HistoryCurveDlg", "恢复", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_revert.setObjectName(_fromUtf8("btn_revert"))
        self.horizontalLayout.addWidget(self.btn_revert)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.btn_print = QtGui.QPushButton(HistoryCurveDlg)
        self.btn_print.setText(QtGui.QApplication.translate("HistoryCurveDlg", "打印", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_print.setObjectName(_fromUtf8("btn_print"))
        self.horizontalLayout.addWidget(self.btn_print)
        self.btn_quit = QtGui.QPushButton(HistoryCurveDlg)
        self.btn_quit.setText(QtGui.QApplication.translate("HistoryCurveDlg", "退出", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_quit.setObjectName(_fromUtf8("btn_quit"))
        self.horizontalLayout.addWidget(self.btn_quit)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(HistoryCurveDlg)
        QtCore.QMetaObject.connectSlotsByName(HistoryCurveDlg)

    def retranslateUi(self, HistoryCurveDlg):
        pass

from mplwidget import MplWidget
