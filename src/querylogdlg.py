# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ui_querylogdlg import *
import historycurvedlg
import model


class QueryLogDlg(QDialog, Ui_QueryLogDlg):
    def __init__(self, boiler_num, sensor_num, company_info, 
                 bid=0, sid=0, parent=None):
        super(QueryLogDlg, self).__init__(parent)
        self.setupUi(self)

        self.company_info = company_info
        self.cbo_boiler.addItems(
            ["%02d" % (i + 1) for i in range(boiler_num)])
        self.sensor_num = sensor_num
        self.cbo_boiler.setCurrentIndex(bid)
        self.dt_start.setDateTime(QDateTime.currentDateTime())
        self.dt_end.setDateTime(QDateTime.currentDateTime())


    @pyqtSignature("int, int")    
    def on_tbl_result_cellClicked(self, row, col):
        dt_s = self.tbl_result.item(row, 1).text()
        dt_e = self.tbl_result.item(row, 2).text()
        self.dt_start.setDateTime(self.dt_start.dateTimeFromText(dt_s))
        if dt_e != "--":
            self.dt_end.setDateTime(self.dt_end.dateTimeFromText(dt_e))
            return
        if row == 0:
            self.dt_end.setDateTime(QDateTime.currentDateTime())
        else:
            dt_e = self.tbl_result.item(row - 1, 1).text()
            self.dt_end.setDateTime(self.dt_end.dateTimeFromText(dt_e))

        
        
    @pyqtSignature("")    
    def on_btn_query_clicked(self):
        for i in range(self.tbl_result.rowCount()):
            self.tbl_result.removeRow(0)
        proc_infos = model.get_pasteu_procs(
            self.cbo_boiler.currentIndex() + 1)
        if len(proc_infos) == 0:
            QMessageBox.information(self, u"历史记录查询", u"该风炉无监测过程记录!")
            return
        for row, pi in enumerate(proc_infos):
            self.tbl_result.insertRow(0)
            # boiler id
            wdgt = QTableWidgetItem(str(pi[1]))
            self.tbl_result.setItem(0, 0, wdgt)
            # start log
            wdgt = QTableWidgetItem(str(pi[2]))
            self.tbl_result.setItem(0, 1, wdgt)
            # end log
            if not pi[5]:
                wdgt = QTableWidgetItem("--")
            else:
                wdgt = QTableWidgetItem(str(pi[5]))
            self.tbl_result.setItem(0, 2, wdgt)
        self.tbl_result.resizeColumnsToContents()


    @pyqtSignature("")
    def on_btn_curve_clicked(self):
        bid = self.cbo_boiler.currentIndex() + 1
        prog_dlg = QProgressDialog(u"查询中...", u"取消", 0, 
                                   self.sensor_num)
        prog_dlg.setWindowModality(Qt.WindowModal)
        prog_dlg.setWindowTitle(u"历史记录查询")
        prog_dlg.show()
        log_lst = []
        for i in range(self.sensor_num):
            prog_dlg.setLabelText(u"查询温度传感器#%02d" % (i + 1))
            log_lst.append(
                model.get_sensor_log(
                    bid, i + 1, 
                    self.dt_start.dateTime().toPyDateTime(),
                    self.dt_end.dateTime().toPyDateTime()))
            prog_dlg.setValue(i)
            if prog_dlg.wasCanceled():
                return
        prog_dlg.setValue(self.sensor_num)
        if max([len(i) for i in log_lst]) == 0:
            QMessageBox.warning(self, u"历史记录查询", u"该范围内没有数据!")
            return
        prog_dlg.setLabelText(u"正在绘图，请稍候...")
        his_curve_dlg = historycurvedlg.HistoryCurveDlg(
            bid, log_lst, self.company_info, 
            self.dt_start.dateTime(), self.dt_end.dateTime())
        his_curve_dlg.showMaximized()
        his_curve_dlg.exec_()



if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    form = QueryLogDlg(7, 25, "XXX Company")
    form.show()
    sys.exit(app.exec_())
