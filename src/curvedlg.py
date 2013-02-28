# -*- coding: utf-8 -*-

import random
import datetime
import time
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import matplotlib as mpl
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from ui_curvedlg import *
from sensor import STATE_HITEMP
import querylogdlg
import model


mpl.rcParams['font.sans-serif'].insert(0, 'SimHei')
mpl.rcParams['axes.unicode_minus'] = False


class CurveDlg(QDialog, Ui_CurveDlg):
    def __init__(self, boiler_num, sensor_num, bid, sid, sensor, 
                 company_info, parent=None):
        super(CurveDlg, self).__init__(parent, Qt.WindowMinMaxButtonsHint)
        self.setupUi(self)
        self.boiler_num = boiler_num
        self.sensor_num = sensor_num
        self.bid = bid
        self.sid = sid
        self.sensor = sensor
        self.company_info = company_info
        self.span = 300
        boiler = self.sensor.boiler
        self.state = None
        self.set_lcd_color()

        ax = self.wdt_mpl.canvas.ax
        ax.set_ylim(boiler.low_temp, boiler.high_temp)
        ax.set_xlim(0, self.span)
        ax.set_title(u"风炉#%02d 温度传感器#%02d" % (bid + 1, sid + 1))
        ax.set_xlabel(u"时间/秒")
        ax.set_ylabel(u"温度/℃")
        ax.grid(True)

        self.data = [None] * self.span
        self.l_sensor, = self.wdt_mpl.canvas.ax.plot(
            range(self.span), self.data, label="sensor")
        self.wdt_mpl.canvas.draw()
        self.timer = self.startTimer(1000)


    def set_lcd_color(self):
        update_color = False
        if (not self.state) or (self.state != self.sensor.state):
            self.state = self.sensor.state
            update_color = True
        if self.state == STATE_HITEMP:
            update_color = True
        if not update_color:
            return

        pal = self.lcd_temp.palette()
        if self.state != STATE_HITEMP:
            pal.setColor(QPalette.Normal, QPalette.Window, 
                         model.COLORS[self.state])
            self.lcd_temp.setPalette(pal)
            return

        if pal.color(QPalette.Normal, QPalette.Window) == \
                model.COLORS[self.state]:
            pal.setColor(QPalette.Normal, QPalette.Window, 
                         model.COLORS[self.state - 1])
        else:
            pal.setColor(QPalette.Normal, QPalette.Window, 
                         model.COLORS[self.state])                
        self.lcd_temp.setPalette(pal)

        
    def timerEvent(self, evt):
        # temp = gen_temp(random.randint(-1, 1))
        self.set_lcd_color()
        temp = self.sensor.temp
        self.data.pop(0)
        self.data.append(temp)
        self.l_sensor.set_data(range(self.span), self.data)
        self.wdt_mpl.canvas.draw()
        self.edit_cur_time.setText(time.strftime("%Y-%m-%d %H:%M:%S"))
        if temp == None:
            self.lcd_temp.display("EE")
        else:
            self.lcd_temp.display(temp)
        self.prog_pasteu.setValue(
            100 *
            (1 - self.sensor.pasteu_time * 1.0/self.sensor.boiler.pasteu_time))
        if self.sensor.state == 4:
            self.prog_pasteu.setValue(100)


    @pyqtSignature("")
    def on_btn_quit_clicked(self):
        self.done(QDialog.Rejected)


    @pyqtSignature("")
    def on_btn_query_clicked(self):        
        query_dlg = querylogdlg.QueryLogDlg(
            self.boiler_num, self.sensor_num, self.company_info, 
            self.bid, self.sid)
        query_dlg.exec_()



if __name__ == "__main__":
    import sys
    from tempmonitor import Sensor, Boiler, gen_temp

    sys_config = model.get_sys_config()
    boiler_configs = model.get_boiler_config()

    boiler_num = sys_config[0]
    sensor_num = boiler_configs[0][6]
    boilers = []
    for i in range(boiler_num):
        bconf = boiler_configs[0]
        if boiler_configs.has_key(i):
            bconf = boiler_configs[i]
        boilers.append(Boiler(*bconf))
    

    app = QApplication(sys.argv)
    form = CurveDlg(1, 1, boilers[0].sensors[0])
    form.show()
    sys.exit(app.exec_())
