# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'querylogdlg.ui'
#
# Created: Sun Oct 30 15:15:52 2011
#      by: PyQt4 UI code generator 4.8.5
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_QueryLogDlg(object):
    def setupUi(self, QueryLogDlg):
        QueryLogDlg.setObjectName(_fromUtf8("QueryLogDlg"))
        QueryLogDlg.resize(521, 508)
        QueryLogDlg.setWindowTitle(QtGui.QApplication.translate("QueryLogDlg", "历史记录查询", None, QtGui.QApplication.UnicodeUTF8))
        self.verticalLayout = QtGui.QVBoxLayout(QueryLogDlg)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.label = QtGui.QLabel(QueryLogDlg)
        self.label.setText(QtGui.QApplication.translate("QueryLogDlg", "风炉编号：", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.cbo_boiler = QtGui.QComboBox(QueryLogDlg)
        self.cbo_boiler.setObjectName(_fromUtf8("cbo_boiler"))
        self.gridLayout.addWidget(self.cbo_boiler, 0, 1, 1, 1)
        spacerItem = QtGui.QSpacerItem(18, 17, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(18, 17, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 2, 1, 1)
        self.label_4 = QtGui.QLabel(QueryLogDlg)
        self.label_4.setText(QtGui.QApplication.translate("QueryLogDlg", "结束时间：", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.gridLayout.addWidget(self.label_4, 1, 3, 1, 1)
        self.dt_end = QtGui.QDateTimeEdit(QueryLogDlg)
        self.dt_end.setDisplayFormat(QtGui.QApplication.translate("QueryLogDlg", "yyyy-MM-dd HH:mm:ss", None, QtGui.QApplication.UnicodeUTF8))
        self.dt_end.setObjectName(_fromUtf8("dt_end"))
        self.gridLayout.addWidget(self.dt_end, 1, 4, 1, 1)
        self.label_3 = QtGui.QLabel(QueryLogDlg)
        self.label_3.setText(QtGui.QApplication.translate("QueryLogDlg", "起始时间：", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.dt_start = QtGui.QDateTimeEdit(QueryLogDlg)
        self.dt_start.setDisplayFormat(QtGui.QApplication.translate("QueryLogDlg", "yyyy-MM-dd HH:mm:ss", None, QtGui.QApplication.UnicodeUTF8))
        self.dt_start.setObjectName(_fromUtf8("dt_start"))
        self.gridLayout.addWidget(self.dt_start, 1, 1, 1, 1)
        self.btn_query = QtGui.QPushButton(QueryLogDlg)
        self.btn_query.setText(QtGui.QApplication.translate("QueryLogDlg", "查询监测过程记录", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_query.setObjectName(_fromUtf8("btn_query"))
        self.gridLayout.addWidget(self.btn_query, 0, 4, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.label_2 = QtGui.QLabel(QueryLogDlg)
        self.label_2.setText(QtGui.QApplication.translate("QueryLogDlg", "监测过程记录信息：", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout.addWidget(self.label_2)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tbl_result = QtGui.QTableWidget(QueryLogDlg)
        self.tbl_result.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tbl_result.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tbl_result.setRowCount(0)
        self.tbl_result.setColumnCount(3)
        self.tbl_result.setObjectName(_fromUtf8("tbl_result"))
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("QueryLogDlg", "风炉编号", None, QtGui.QApplication.UnicodeUTF8))
        self.tbl_result.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("QueryLogDlg", "起始记录时间", None, QtGui.QApplication.UnicodeUTF8))
        self.tbl_result.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        item.setText(QtGui.QApplication.translate("QueryLogDlg", "结束记录时间", None, QtGui.QApplication.UnicodeUTF8))
        self.tbl_result.setHorizontalHeaderItem(2, item)
        self.verticalLayout.addWidget(self.tbl_result)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.buttonBox = QtGui.QDialogButtonBox(QueryLogDlg)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.horizontalLayout_3.addWidget(self.buttonBox)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.btn_curve = QtGui.QPushButton(QueryLogDlg)
        self.btn_curve.setText(QtGui.QApplication.translate("QueryLogDlg", "曲线图", None, QtGui.QApplication.UnicodeUTF8))
        self.btn_curve.setObjectName(_fromUtf8("btn_curve"))
        self.horizontalLayout_3.addWidget(self.btn_curve)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.retranslateUi(QueryLogDlg)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), QueryLogDlg.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), QueryLogDlg.reject)
        QtCore.QMetaObject.connectSlotsByName(QueryLogDlg)

    def retranslateUi(self, QueryLogDlg):
        item = self.tbl_result.horizontalHeaderItem(0)
        item = self.tbl_result.horizontalHeaderItem(1)
        item = self.tbl_result.horizontalHeaderItem(2)

