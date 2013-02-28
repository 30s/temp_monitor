# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from scanwin32 import comports
from ui_monitoringconfigdlg import *
import model


class MonitoringConfigDlg(QDialog, Ui_MonitoringConfigDlg):
    def __init__(self, parent=None):
        super(MonitoringConfigDlg, self).__init__(parent)
        self.setupUi(self)
        self.sys_config = model.get_sys_config()
        self.boiler_configs = model.get_boiler_config()
        self.cur_boiler = 0
        # print self.sys_config
        # print self.boiler_configs
        self.spin_boiler_num.setValue(self.sys_config[0])
        self.spin_fan_num.setValue(self.sys_config[3])
        self.spin_acq_interval.setValue(self.sys_config[4])
        self.spin_timeout.setValue(self.sys_config[5])
        self.spin_sensor_num.setValue(self.boiler_configs[0][6])
        self.cbo_boiler.addItem(u"默认", 0)
        self.cbo_boiler.addItems(
            [u"风炉 %02d" % (i + 1) for i in range(self.sys_config[0])])
        self.edit_company_info.setText(self.sys_config[2])
        for port in sorted(comports()):
            self.cbo_com.addItem(port[1])
        com, port = self.sys_config[1].split(";")
        self.cbo_com.setCurrentIndex(
            self.cbo_com.findText(com))
        self.cbo_baudrate.setCurrentIndex(
            self.cbo_baudrate.findText(port))
            

    @pyqtSignature("int")
    def on_lst_configs_currentRowChanged(self, row):
        self.stack_configs.setCurrentIndex(row)


    @pyqtSignature("")
    def on_btn_apply_scope_clicked(self):
        if not model.set_boiler_num(self.spin_boiler_num.value()):
            QMessageBox.critical(self, u"监控参数设置", u"设置风炉数量失败!")
            return

        if not model.set_sensor_num(self.spin_sensor_num.value()):
            QMessageBox.critical(self, u"监控参数设置", u"设置温度传感器数量失败!")
            return
            
        if not model.set_fan_num(self.spin_fan_num.value()):
            QMessageBox.critical(self, u"监控参数设置", u"设置风机数量失败!")
            return


    @pyqtSignature("int")
    def on_cbo_boiler_currentIndexChanged(self, index):
        self.cur_boiler = index
        if not self.boiler_configs.has_key(index):
            self.boiler_configs[index] = list(self.boiler_configs[0])
        self.spin_low_temp.setValue(self.boiler_configs[index][0])
        self.spin_hi_temp.setValue(self.boiler_configs[index][1])
        self.spin_alert_temp.setValue(self.boiler_configs[index][2])
        self.spin_alert_time.setValue(self.boiler_configs[index][3])
        self.spin_pasteu_time.setValue(self.boiler_configs[index][4] / 60)
        self.spin_pasteu_alert_time.setValue(self.boiler_configs[index][5])
        self.chk_hi_temp_alert.setCheckState(self.boiler_configs[index][7])
        

    @pyqtSignature("int")
    def on_spin_low_temp_valueChanged(self, val):
        self.boiler_configs[self.cur_boiler][0] = val


    @pyqtSignature("int")    
    def on_spin_hi_temp_valueChanged(self, val):
        self.boiler_configs[self.cur_boiler][1] = val


    @pyqtSignature("int")    
    def on_spin_alert_temp_valueChanged(self, val):
        self.boiler_configs[self.cur_boiler][2] = val


    @pyqtSignature("int")    
    def on_spin_alert_time_valueChanged(self, val):
        self.boiler_configs[self.cur_boiler][3] = val


    @pyqtSignature("int")    
    def on_spin_pasteu_time_valueChanged(self, val):
        self.boiler_configs[self.cur_boiler][4] = val * 60


    @pyqtSignature("int")    
    def on_spin_pasteu_alert_time_valueChanged(self, val):
        self.boiler_configs[self.cur_boiler][5] = val


    @pyqtSignature("int")    
    def on_chk_hi_temp_alert_stateChanged(self, state):
        self.boiler_configs[self.cur_boiler][7] = val        


    @pyqtSignature("")
    def on_btn_apply_sensor_clicked(self):
        if not model.set_boiler_config(self.boiler_configs):
            QMessageBox.critical(self, u"监控参数设置", u"设置风炉失败!")


    @pyqtSignature("")
    def on_btn_apply_com_clicked(self):
        com = unicode(self.cbo_com.currentText())
        port = unicode(self.cbo_baudrate.currentText())
        if not model.set_com_str("%s;%s" % (com, port)):
            QMessageBox.critical(self, u"监控参数设置", u"串口设置失败!")
            return
        if not model.set_acq_intvl(self.spin_acq_interval.value()):
            QMessageBox.critical(self, u"监控参数设置", u"采集间隔时间设置失败!")
            return
        if not model.set_timeout(self.spin_timeout.value()):
            QMessageBox.critical(self, u"监控参数设置", u"串口超时设置失败!")
            return


    @pyqtSignature("")
    def on_btn_apply_others_clicked(self):
        info = unicode(self.edit_company_info.text())
        if not model.set_company_info(info):
            QMessageBox.critical(self, u"监控参数设置", u"设置公司信息错误!")


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    form = MonitoringConfigDlg()
    form.show()
    sys.exit(app.exec_())
    
