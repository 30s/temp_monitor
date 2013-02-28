# -*- coding: utf-8 -*-
#!/usr/bin/env python
#
# @file mainwindow.py
#
# @author ax003d@gmail.com
#


WIN_TITLE = u"温度监测系统 - V 1.0 alpha - 86"

#
# Change logs:
#
# [2011-12-28 21:33] V 1.0 alpha - 86
# * Show history curve auto filter with boiler highest and lowest temp config.
#
# [2011-12-19 23:11] V 1.0 alpha - 85
# * Remove filter from acquisition, add filter button on history curve dialog.
#
# [2011-12-07 23:30] V 1.0 alpha - 83
# * Filter noise temperature data.
#
# [2011-12-07 20:38] V 1.0 alpha - 82
# * Fix: Catch DB operation exceptions.
# 
# [2011-12-03 23:04] V 1.0 alpha - 79
# * Fix: when acquisitioned sensor num less than setting sensor num, 
#   cause list out of index exception.
# * Refactoring the database timestamp to seconds, speed up history drawing.
# 
# [2011-11-06 17:36] V 1.0 alpha - 77
# * Do not reset sensor to 0 when acquisition failed.
# * Fix: when no data for a range cannot show history curve normally.
#
# [2011-11-06 11:26] V 1.0 alpha - 75
# * historycurvedlg show maximize.
# * Add progress dlg for history query
# * data export and import.
# * Fix: when there is bad sensor, it will always in STATE_LOTEMP, so it will not
#   do data record.
#
# [2011-10-30 21:52] V 1.0 alpha - 69
# * Add pasteu procedure time record interface: start log, start pasteu, end pasteu, end log
# * Record pasteu procedure times
# * Realtime curve show 'EE' and space when sensor error
# * query by procedure
# * query with mutlti-sensors
#
# [2011-10-26 23:21] V 1.0 alpha - 65
# * Prompt when close window.
# * Optimize historycurvedlg update curve, set ylim properly.
# * Filter error temperature
# 
# [2011-09-18 18:02] V 1.0 alpha - 58
# * curvedlg add data query
# * add navigation toolbar for history dlg
# * curvedlg's lcdnum flash when sensor high temp
# * seperate boiler and sensor to other files
# * fix: compreparedlg close when prepared not done, cause program collapse
# * maxmize the curvedlg and historycurvedlg
# * Use QtDesigner to refactoring the MainWindow
# * Refactoring compreparedlg's logging mechanism, add MainWindow's do_log interface 
# * Auto start acquisition when prepare ok
# * Refactoring logging mechanism, use common logger to emit logging event
# * improve shake hands chance, if acquisition failed, set temperature to 0
# * historycurvedlg add company info, and add time range setting and update, revert button
# * set curvedlg to show 3 mins realtime data
# 

# [2011-09-10 15:24] V 1.0 alpha - 46
# * When display temperature, round it.
# * Query from multi dbs
# 

# [2011-09-08 23:17] V 1.0 alpha - 42
# * Add simple authority management, normal user can't change sys configs
# * Change curve's text to Chinese
# * History curve printing support
# * Fix: Restart acquisition cannot get data
# * Set yellow LED and buzzer first alarm, set red LED and buzzer finish alarm.
#   Close buzzer when alert time passed.
# * Do not neet to set params during communication preparation
# * Add finish state, close port.
# * Per sensor high temp alert.
# * Flash when sensor high temp
#

# [2011-09-04 11:30] V 1.0 alpha - 32
# * First time publish to customer
# 


import os
import datetime
import shutil
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import serial

import ui_mainwindow

from boilerview import BoilerView
from boiler import *
import accountsmanagedlg
import chgpwddlg
import monitoringconfigdlg
import querylogdlg
import curvedlg
import compreparedlg
import communicate
import model
import utils
from logger import *


SIG_START_ACQUISITION = "startAcquisition(bool)"
SIG_MONITOR_FINISHED  = "monitoringFinished()"
SIG_PASTEU_PROC_LOG   = "log_pasteu_proc(int)"

LOG_COLORS = [QColor(Qt.black), QColor(Qt.darkCyan), QColor(Qt.darkYellow), QColor(Qt.red)]

class AcquisitionThread(QThread):
    def __init__(self, port, acq_intvl, boilers, fan_num, parent):
        super(AcquisitionThread, self).__init__(parent)
        self.port = port
        self.acq_intvl = acq_intvl
        self.boilers = boilers
        self.fan_num = fan_num
        self.running = False
        

    def set_boiler_alarm(self, idx, boiler):
        ac = boiler.alarm_cmds
        if ac["red_led_on"] or ac["green_led_on"] or ac["alarm_on"]:
            communicate.alarm_on(
                self.port, 0x81 + idx,
                ac["red_led_on"], ac["green_led_on"], ac["alarm_on"])

        if ac["red_led_off"] or ac["green_led_off"] or ac["alarm_off"]:
            communicate.alarm_off(
                self.port, 0x81 + idx,
                ac["red_led_off"], ac["green_led_off"], ac["alarm_off"])

        if ac["close_fan"]:
            for i in range(self.fan_num):
                communicate.fan_off(self.port, 0x81 + idx, i)

        for i in ac.keys():
            ac[i] = False


    def run(self):
        self.running = True
        self.logger = model.DataLogger(time.strftime("%Y-%m") + ".db3")
        self.emit(SIGNAL(SIG_START_ACQUISITION), True)
        while self.running:
            acq_end = True
            for idx, b in enumerate(self.boilers):
                if b.state == BSTAT_ALL_END:
                    continue

                acq_end = False
                if not b.com_state:
                    ret = communicate.shake_hands(self.port, 0x81 + idx)
                    if not ret[0]:
                        continue
                    if ret[1] == 0:
                        b.com_state = True
                    else:
                        continue

                ret = communicate.get_temp(self.port, 0x81 + idx)
                temps = None
                if ret[0]:
                    b.update(ret[1])
                    self.set_boiler_alarm(idx, b)
                    if b.proc_logs != None:
                        self.emit(SIGNAL(SIG_PASTEU_PROC_LOG), idx)
                    temps = ret[1]
                else:
                    temps = [None] * b.sensor_num
                    # b.update(temps)
                    b.com_state = False
                if b.log_started:
                    self.logger.add_log(idx, temps)
            if acq_end:
                break
            self.logger.commit()
            time.sleep(self.acq_intvl)
        self.port.close()
        self.emit(SIGNAL(SIG_MONITOR_FINISHED))


class MainWindow(ui_mainwindow.Ui_MainWindow, QMainWindow):
    def __init__(self, usr_name, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.setCentralWidget(self.stack_view)

        self.usr_name = usr_name
        self.sys_config = model.get_sys_config()
        self.boiler_configs = model.get_boiler_config()

        boiler_num = self.sys_config[0]
        sensor_num = self.boiler_configs[0][6]
        self.boilers = []
        for i in range(boiler_num):
            bconf = self.boiler_configs[0]
            if self.boiler_configs.has_key(i):
                bconf = self.boiler_configs[i]
            self.boilers.append(Boiler(*bconf))
            self.boilers[i].id = i + 1

        self.th_monitor = None
        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        self.connect(self.timer, SIGNAL("timeout()"), self.update_view)

        self.tbl_sensors.setRowCount(boiler_num)
        self.tbl_sensors.setColumnCount(sensor_num)
        lst = [u"温度_%02d" % (i + 1) for i in range(sensor_num)]
        self.tbl_sensors.setHorizontalHeaderLabels(lst)
        lst = [u"风炉_%02d" % (i + 1) for i in range(boiler_num)]
        self.tbl_sensors.setVerticalHeaderLabels(lst)
        self.connect(self.tbl_sensors, SIGNAL("cellDoubleClicked(int, int)"),
                     self.tbl_sensors_double_clicked)

        font = QFont()
        font.setPointSize(14)
        for row in range(boiler_num):
            for col in range(sensor_num):
                wdgt = QTableWidgetItem("00")
                wdgt.setFont(font)
                wdgt.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                self.tbl_sensors.setItem(row, col, wdgt)
                self.tbl_sensors.setColumnWidth(col, 64)

        self.setup_views(boiler_num, sensor_num)
        self.stack_view.addWidget(self.splitter)
        
        self.connect(self.act_moni_conf, SIGNAL("triggered()"), 
                     self.monitor_config);
        self.connect(self.act_account_man, SIGNAL("triggered()"),
                     self.account_manage)
        self.connect(self.act_change_pwd, SIGNAL("triggered()"),
                     self.change_pwd)
        self.connect(self.act_global_view, SIGNAL("triggered()"),
                     self.view_global)
        self.connect(self.act_boiler_view, SIGNAL("triggered()"),
                     self.view_boiler)
        self.connect(self.act_query, SIGNAL("triggered()"),
                     self.query_log)
        self.connect(self.act_backup, SIGNAL("triggered()"),
                     self.backup)
        self.connect(self.act_recover, SIGNAL("triggered()"),
                     self.recover)

        self.connect(logger, SIGNAL(SIG_ADD_LOG), self.do_log)

        if self.usr_name == "admin":
            self.act_account_man.setVisible(True)
            self.act_moni_conf.setVisible(True)

        self.setWindowTitle(WIN_TITLE)

        QTimer.singleShot(1500, self.start_monitor)


    def tbl_sensors_double_clicked(self, row, col):
        curve_dlg = curvedlg.CurveDlg(
            self.sys_config[0], self.boiler_configs[0][6],
            row, col, self.boilers[row].sensors[col], 
            self.sys_config[2], self)
        curve_dlg.exec_()


    def update_global_view(self):
        for row, b in enumerate(self.boilers):
            for col, s in enumerate(b.sensors):
                item = self.tbl_sensors.item(row, col)
                if s.temp == None:
                    item.setText("EE")
                    continue
                item.setText("%02d" % round(s.temp))
                if s.state != STATE_HITEMP:
                    item.setBackgroundColor(model.COLORS[s.state])
                    continue
                if item.backgroundColor() == model.COLORS[s.state]:
                    item.setBackgroundColor(model.COLORS[s.state - 1])
                else:
                    item.setBackgroundColor(model.COLORS[s.state])


    def update_boiler_view(self):
        bid = self.lst_boiler.currentRow()
        if bid == -1:
            bid = 0
        self.boiler_view.update(bid)


    def update_view(self):
        if self.stack_view.currentIndex() == 0:
            self.update_global_view()
        else:
            self.update_boiler_view()


    def view_global(self):
        self.stack_view.setCurrentIndex(0)


    def view_boiler(self):
        self.stack_view.setCurrentIndex(1)


    def boiler_sel_changed(self, cur_row):
        self.boiler_view.lbl_title.setText(u"<h1>风炉#%02d</h1>" % (cur_row + 1))
    
    
    def setup_views(self, boiler_num, sensor_num):
        self.splitter = QSplitter()
        self.lst_boiler = QListWidget()
        lst = [u"风炉#%02d" % (i + 1) for i in range(boiler_num)]
        self.lst_boiler.addItems(lst)
        self.lst_boiler.setCurrentRow(0)
        self.connect(self.lst_boiler, SIGNAL("currentRowChanged(int)"), 
                     self.boiler_sel_changed)
        self.boiler_view = BoilerView(sensor_num, self.sys_config[2], self.boilers)
        self.splitter.addWidget(self.lst_boiler)
        self.splitter.addWidget(self.boiler_view)
        self.splitter.setStretchFactor(0, 0)
        self.splitter.setStretchFactor(1, 1)


    def change_pwd(self):
        dlg_chg_pwd = chgpwddlg.ChgPwdDlg(self.usr_name)
        dlg_chg_pwd.setModal(True)
        dlg_chg_pwd.exec_()


    def account_manage(self):
        account_man_dlg = accountsmanagedlg.AccountsManageDlg()
        account_man_dlg.exec_()


    def start_monitor(self):
        com, baud = self.sys_config[1].split(";")
        baud = int(baud)
        # timeout= (256 / (baud / 8.0)) * 5
        timeout = self.sys_config[5] / 1000.0
        try:
            # com = 'COM3'
            self.port = serial.Serial(com, baud, timeout=timeout)
        except Exception:
            QMessageBox.critical(self, u"温度监测系统", u"打开串口失败!")
            return

        prepare_dlg = compreparedlg.ComPrepareDlg(
            self.port, self.boilers, self.sys_config[3], self)
        if QDialog.Accepted != prepare_dlg.exec_():
            self.port.close()
            return

        if self.th_monitor != None:
            return        
        self.th_monitor = AcquisitionThread(
            self.port, self.sys_config[4], self.boilers, 
            self.sys_config[3], self)
        self.connect(self.th_monitor, SIGNAL(SIG_START_ACQUISITION),
                     self.start_timer)
        self.connect(self.th_monitor, SIGNAL(SIG_MONITOR_FINISHED),
                     self.monitoring_finished)
        self.connect(self.th_monitor, SIGNAL(SIG_PASTEU_PROC_LOG),
                     self.log_pasteu_proc)
        self.th_monitor.start()


    def start_timer(self, state):
        if state:
            self.timer.start()


    def stop_monitor(self):
        self.timer.stop()
        if not self.th_monitor:
            return
        self.th_monitor.running = False
        self.th_monitor.quit()
        self.th_monitor = None


    def monitor_config(self):
        moni_conf_dlg = monitoringconfigdlg.MonitoringConfigDlg()
        moni_conf_dlg.exec_()


    def query_log(self):
        query_dlg = querylogdlg.QueryLogDlg(
            self.sys_config[0], self.boiler_configs[0][6], self.sys_config[2])
        query_dlg.exec_()


    def do_log(self, log, level=0):
        self.tbl_logs.insertRow(0)
        wdgt = QTableWidgetItem(datetime.datetime.now().isoformat(' '))
        wdgt.setTextColor(LOG_COLORS[level])
        self.tbl_logs.setItem(0, 0, wdgt)
        wdgt = QTableWidgetItem(log)
        wdgt.setTextColor(LOG_COLORS[level])
        self.tbl_logs.setItem(0, 1, wdgt)
        self.tbl_logs.resizeColumnsToContents()


    def monitoring_finished(self):
        log = u"本次温度监测任务已经完成!"
        logger.warning(log)
        QMessageBox.information(self, u"温度监测系统", log)


    def log_pasteu_proc(self, idx):
        boiler = self.boilers[idx]
        if boiler.proc_logs == "start_log":
            boiler.proc_id = model.add_pasteu_procs(boiler.id)
        elif boiler.proc_logs == "start_pasteu":
            model.pasteu_started(boiler.proc_id)
        elif boiler.proc_logs == "end_pasteu":
            model.pasteu_finished(boiler.proc_id)
        elif boiler.proc_logs == "end_log":
            model.log_finished(boiler.proc_id)            
        boiler.proc_logs = None


    def backup(self):
        app_path = utils.module_path()
        files = [ i for i in os.listdir(app_path) if i.endswith(".db3")]
        bk_dir = unicode(QFileDialog.getExistingDirectory(self, u"选择备份路径"))

        proc_dlg = QProgressDialog(u"备份中...", u"取消", 0, len(files))
        proc_dlg.setWindowModality(Qt.WindowModal)
        proc_dlg.setWindowTitle(u"数据备份")
        proc_dlg.show()

        for idx, i in enumerate(files):
            fpath = os.path.join(app_path, i)
            proc_dlg.setLabelText(fpath)
            shutil.copy(fpath, bk_dir)
            proc_dlg.setValue(idx)
            if proc_dlg.wasCanceled():
                return
        proc_dlg.setValue(len(files))
        QMessageBox.information(self, u"温度监测系统", 
                                u"数据成功备份到 %s !" % bk_dir)
            

    def recover(self):
        app_path = utils.module_path()
        bk_dir = unicode(QFileDialog.getExistingDirectory(self, u"选择备份路径"))
        files = [ i for i in os.listdir(bk_dir) if i.endswith(".db3")]

        ret = QMessageBox.question(self, u"温度监测系统", 
                                   u"备份数据将覆盖现有数据, 确认要恢复数据?",
                                   QMessageBox.Yes, QMessageBox.No)
        if QMessageBox.Yes != ret:
            return

        proc_dlg = QProgressDialog(u"恢复中...", u"取消", 0, len(files))
        proc_dlg.setWindowModality(Qt.WindowModal)
        proc_dlg.setWindowTitle(u"数据恢复")
        proc_dlg.show()

        for idx, i in enumerate(files):
            fpath = os.path.join(bk_dir, i)
            proc_dlg.setLabelText(fpath)
            shutil.copy(fpath, app_path)
            proc_dlg.setValue(idx)
            if proc_dlg.wasCanceled():
                return
        proc_dlg.setValue(len(files))
        QMessageBox.information(self, u"温度监测系统", 
                                u"成功从 %s 恢复数据!" % bk_dir)

        
    def closeEvent(self, event):
        ret = QMessageBox.question(
            self, u"温度监测系统", u"确定退出监测?",  
            QMessageBox.Yes, QMessageBox.No)
        if QMessageBox.Yes == ret:
            event.accept()
        else:
            event.ignore()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    form = MainWindow("admin")
    form.show()
    # form.do_log("start up!")
    sys.exit(app.exec_())

