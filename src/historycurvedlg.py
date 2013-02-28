# -*- coding: utf-8 -*-

import bisect
import math
import time
import datetime
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import matplotlib as mpl
import dateutil.parser as dp
import ui_historycurvedlg
import filterdlg
import model
from matplotlib.backends.backend_qt4agg import \
    NavigationToolbar2QTAgg as NavigationToolbar

mpl.rcParams['font.sans-serif'].insert(0, 'SimHei')
mpl.rcParams['axes.unicode_minus'] = False


def date_parse(dstr):
    return datetime.datetime.strptime(dstr, "%Y-%m-%d %H:%M:%S")


class HistoryCurveDlg(QDialog, 
                      ui_historycurvedlg.Ui_HistoryCurveDlg):
    def __init__(self, bid, logs, company_info, dt_start, dt_end, parent=None):
        super(HistoryCurveDlg, self).__init__(parent, Qt.WindowMinMaxButtonsHint)
        self.setupUi(self)

        # custome do not want revert button
        self.btn_revert.setVisible(False)
        self.filter_dlg = filterdlg.FilterDlg()
        self.lst_sensors.setVisible(False)
        for i in range(len(logs)):
            wdgt = QListWidgetItem(u"温度_%02d" % (i + 1))
            wdgt.setFlags( wdgt.flags() | Qt.ItemIsUserCheckable)
            if i < 6:
                wdgt.setCheckState(Qt.Checked)
            else:
                wdgt.setCheckState(Qt.Unchecked)
            self.lst_sensors.addItem(wdgt)
        self.bid = bid
        self.company_info = company_info
        # ntb = NavigationToolbar(self.wdgt_curve.canvas, self)
        # self.verticalLayout.insertWidget(0, ntb)
        self.start_t = dt_start
        self.end_t   = dt_end
        # self.dt_start.setDateTimeRange(self.start_t, self.end_t)
        self.dt_start.setDateTime(self.start_t)
        # self.dt_end.setDateTimeRange(self.start_t, self.end_t)
        self.dt_end.setDateTime(self.end_t)

        self.xdata = None
        self.ydata = []
        for s_log in logs:
            if self.xdata == None:
                self.xdata = [ 
                datetime.datetime.fromtimestamp(i[0]) for i in s_log ]
            self.ydata.append([i[1] for i in s_log])
        QTimer.singleShot(1000, self.auto_filter)
        

    @pyqtSignature("")
    def on_btn_choose_sensors_clicked(self):
        if self.lst_sensors.isVisible():
            self.lst_sensors.setVisible(False)
        else:
            self.lst_sensors.move(self.btn_choose_sensors.x(),
                                  self.btn_choose_sensors.y() - 310)
            self.lst_sensors.setVisible(True)


    @pyqtSignature("")
    def on_btn_update_clicked(self):
        start_t = self.dt_start.dateTime().toPyDateTime()
        end_t   = self.dt_end.dateTime().toPyDateTime()
        canvas  = self.wdgt_curve.canvas
        ax      = canvas.ax
        ax.cla()
        ax.set_title(u"风炉#%02d (%s ~ %s)" % (self.bid, start_t, end_t))
        ax.set_xlabel(u"时间\n\n%s" % self.company_info)
        ax.set_ylabel(u"温度/℃")
        ax.grid(True)
        canvas.fig.autofmt_xdate(bottom=0.18)
        show_lst = []
        for i in range(self.lst_sensors.count()):
            wdgt = self.lst_sensors.item(i)
            if wdgt.checkState() == Qt.Checked:
                show_lst.append(i)
        y_highs    = []
        y_lows     = []
        none_lst   = []
        prog_dlg = QProgressDialog(u"绘图中，请稍候...", u"取消", 0, len(show_lst))
        prog_dlg.setWindowModality(Qt.WindowModal)
        prog_dlg.setWindowTitle(u"历史记录曲线")
        prog_dlg.show()
        draw_idx = 0
        for i in show_lst:
            draw_idx += 1
            prog_dlg.setValue(draw_idx)
            if (prog_dlg.wasCanceled()):
                break
            if len(self.xdata) == 0:
                none_lst.append(i)
                continue
            start_idx = bisect.bisect(self.xdata, start_t)
            end_idx   = bisect.bisect(self.xdata, end_t)
            if len(self.xdata[start_idx: end_idx]) == 0:
                none_lst.append(i)
                continue
            y_high    = max(self.ydata[i][start_idx: end_idx])
            if y_high != None:
                y_highs.append(y_high)
            low_lst = [ x for x in self.ydata[i][start_idx: end_idx] if x != None]
            if len(low_lst) == 0:
                none_lst.append(i)
                continue
            y_low     = min(low_lst)
            if y_low != None:
                y_lows.append(y_low)
            ax.plot(self.xdata[start_idx: end_idx], 
                    self.ydata[i][start_idx: end_idx], 
                    label=u"温度_%02d" % (i + 1))
        if len(y_highs) == 0:
            QMessageBox.information(self, u"历史曲线", u"该范围内没有数据!")
            return
        if len(none_lst) != 0:
            QMessageBox.information(
                self, u"历史曲线", 
                u"温度传感器(%s)在该范围内没有数据!" % \
                    ", ".join(["#%02d" % (i + 1) for i in none_lst]))
        canvas.ax.set_xlim(start_t, end_t)
        canvas.ax.set_ylim(math.floor(min(y_lows) / 10.0) * 10, 
                           math.ceil(max(y_highs) / 10.0) * 10)        
        ax.legend(loc="best")
        canvas.draw()


    @pyqtSignature("")
    def on_btn_filter_clicked(self):
        if self.filter_dlg.exec_() != QDialog.Accepted:
            return
        
        low, high = self.filter_dlg.get_bounds()
        self.noise_filter(low, high)


    def auto_filter(self):
        boiler_config = model.get_boiler_config()
        self.noise_filter(boiler_config[0][0], boiler_config[0][1])
        

    def noise_filter(self, low, high):
        for lst in self.ydata:
            for idx, i in enumerate(lst):
                if i < low or i > high:
                    lst[idx] = None
        self.on_btn_update_clicked()
        

    @pyqtSignature("")
    def on_btn_revert_clicked(self):
        self.dt_start.setDateTime(self.start_t)
        self.dt_end.setDateTime(self.end_t)
        self.on_btn_update_clicked()


    @pyqtSignature("")
    def on_btn_quit_clicked(self):
        self.done(QDialog.Rejected)


    @pyqtSignature("")
    def on_btn_print_clicked(self):
        self.wdgt_curve.canvas.fig.savefig("print.png", dpi=300, papertype='a4')
        self.image = QImage("print.png")
        self.printer = QPrinter(QPrinter.HighResolution)
        self.printer.setPageSize(QPrinter.A4)
        form = QPrintDialog(self.printer, self)
        if form.exec_():
            painter = QPainter(self.printer)
            rect = painter.viewport().adjusted(0, 100, 0, -100)
            size = self.image.size()
            self.image = self.image.scaled(
                rect.size(), Qt.IgnoreAspectRatio)
            size.scale(rect.size(), Qt.IgnoreAspectRatio)
            painter.setViewport(rect.x(), rect.y(), size.width(),
                                size.height())
            painter.drawImage(0, 0, self.image)
        
        

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    form = HistoryCurveDlg()
    form.show()
    sys.exit(app.exec_())
