# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from sensor import *
import curvedlg
import model


SIGNAL_SENSOR_CLICKED = "sensorClicked(int)"


class SensorLCDNumber(QLCDNumber):
    def __init__(self, sid, num_digits, parent=None):
        super(SensorLCDNumber, self).__init__(num_digits, parent)
        self.sid = sid


    def event(self, e):
         ret_val = super(SensorLCDNumber, self).event(e)
         if e.type() == QEvent.MouseButtonDblClick:
             self.emit(SIGNAL(SIGNAL_SENSOR_CLICKED), self.sid)
             ret_val = True

         return ret_val



class BoilerView(QFrame):
    def __init__(self, sensor_num, company, boilers, parent=None):
        super(BoilerView, self).__init__(parent)     

        self.sensor_num = sensor_num
        self.lbl_title = QLabel(u"<h1>风炉#1</h1>")
        self.lbl_title.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        gridLayout = QGridLayout()
        gridLayout.addWidget(self.lbl_title, 0, 2, 1, 2)
        self.lcd_nums = []
        self.boilers = boilers
        self.cur_boiler = 0

        sid = 0
        for row in range(10):
            lblLeft = QLabel(u"<h3>温度#%02d -&gt;</h3>" % (row * 4 + 1))
            lblLeft.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
            lblRight = QLabel(u"<h3>&lt;- 温度#%02d</h3>" % (row * 4 + 4))
            lblRight.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
            gridLayout.addWidget(lblLeft, 2 + row , 0)
            gridLayout.addWidget(lblRight, 2 + row, 5)
            
            for col in range(4):             
                lcd_num = SensorLCDNumber(sid, 2)
                lcd_num.setSegmentStyle(QLCDNumber.Filled)
                if sid >= sensor_num:
                    lcd_num.setEnabled(False)
                else:
                    sid = sid + 1
                lcd_num.setAutoFillBackground(True)
                lcd_num.display("00")
                self.connect(lcd_num, SIGNAL(SIGNAL_SENSOR_CLICKED),
                             self.show_realtime_view)
                self.lcd_nums.append(lcd_num)
                gridLayout.addWidget(lcd_num, 2 + row, col + 1)

        self.company_info = company
        lblCopyright = QLabel(company)
        lblCopyright.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
        gridLayout.addWidget(lblCopyright, 12, 0, 1, 6)
        self.setLayout(gridLayout)


    def update(self, bid):
        self.cur_boiler = bid
        for idx, s in enumerate(self.boilers[bid].sensors):
            lcd = self.lcd_nums[idx]
            if s.temp == None:
                lcd.display("EE")
                continue
            lcd.display(round(s.temp))
            pal = lcd.palette()
            if s.state != STATE_HITEMP:
                pal.setColor(QPalette.Normal, QPalette.Window, 
                             model.COLORS[s.state])
                lcd.setPalette(pal)
                continue
            if pal.color(QPalette.Normal, QPalette.Window) == \
                    model.COLORS[s.state]:
                pal.setColor(QPalette.Normal, QPalette.Window, 
                             model.COLORS[s.state - 1])
            else:
                pal.setColor(QPalette.Normal, QPalette.Window, 
                             model.COLORS[s.state])                
            lcd.setPalette(pal)


    def show_realtime_view(self, sid):
        curve_dlg = curvedlg.CurveDlg(
            len(self.boilers), self.sensor_num,
            self.cur_boiler, sid, 
            self.boilers[self.cur_boiler].sensors[sid], 
            self.company_info, self)
        curve_dlg.exec_()        
