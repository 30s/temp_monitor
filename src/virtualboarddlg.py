# -*- coding: utf-8 -*-

import serial
import time
import random
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ui_virtualboarddlg import *
from communicate import *


temp = 60
sensor_err = False

def gen_temp(sa):
    global temp
    if sa == 0:
        return temp
    add = False
    if sa == 1:
        add = True
    if temp >= 75:
        add = False
    elif temp <= 50:
        add = True
    if add:
        temp = temp + 1
    else:
        temp = temp - 1
    return temp


port = serial.Serial('COM2', timeout=0.5)


def rsp_shake_hands(frame):
    print "rsp_shake_hands"
    return build_send_frame(
        CMD_SHAKE_HANDS + 1, [ord(frame[4]), 0x00])


def rsp_get_temp(frame):
    # print "rsp_get_temp"
    global temp, sensor_err
    params = [ord(frame[4])]
    # params.extend([gen_temp(random.randint(-1, 1)), 0x0F] * 20)
    if sensor_err:
        params.extend([0xFF, 0xFF] * 40)
    else:
        params.extend([temp, 0x0F] * 18)
        params.extend([0xFF, 0xFF] * 22)
    return build_send_frame(
        CMD_GET_TEMP + 1, params)


def rsp_set_params(frame):
    print "rsp_set_params"
    return build_send_frame(
        CMD_SET_PARAMS + 1, [ord(frame[4]), 0x00])
    

def rsp_get_params(frame):
    print "rsp_get_params"
    return build_send_frame(
        CMD_GET_PARAMS + 1, [ord(frame[4]), 0x46, 0x1E, 0x0F])


def rsp_fan_on(frame):
    print "rsp_fan_on"
    return build_send_frame(
        CMD_FAN_ON + 1, [ord(frame[4]), 0x00])
    

def rsp_fan_off(frame):
    print "rsp_fan_off"
    return build_send_frame(
        CMD_FAN_OFF + 1, [ord(frame[4]), 0x00])


def rsp_alarm_on(frame):
    print "rsp_alarm_on:",
    print_frame(frame)
    return build_send_frame(
        CMD_ALARM_ON + 1, [ord(frame[4]), 0x00])


def rsp_alarm_off(frame):
    print "rsp_alarm_off",
    print_frame(frame)
    return build_send_frame(
        CMD_ALARM_OFF + 1, [ord(frame[4]), 0x00])


dispatcher = {
    CMD_SHAKE_HANDS: rsp_shake_hands,
    CMD_GET_TEMP:    rsp_get_temp,
    CMD_SET_PARAMS:  rsp_set_params,
    CMD_GET_PARAMS:  rsp_get_params,
    CMD_FAN_ON:      rsp_fan_on,
    CMD_FAN_OFF:     rsp_fan_off,
    CMD_ALARM_ON:    rsp_alarm_on,
    CMD_ALARM_OFF:   rsp_alarm_off,
    }


class RspThread(QThread):
    def __init__(self, port, parent):
        super(RspThread, self).__init__(parent)
        self.port = port


    def run(self):
        while True:
            frame = port.read(port.inWaiting())
            if len(frame) != 0:
                # print "recv:", 
                # print_frame(frame)
                rsp = dispatcher[ord(frame[3])](frame)
                # print "send:",
                # print_frame(rsp)
                port.write(rsp)
            time.sleep(1)
        


class VirtualBoardDlg(QDialog, Ui_VirtualBoardDlg):
    def __init__(self, parent=None):
        super(VirtualBoardDlg, self).__init__(parent)
        self.setupUi(self)
        
        self.timer = QTimer(self)
        self.timer.setInterval(1000)
        self.connect(self.timer, SIGNAL("timeout()"), self.update_temp)
        self.timer.start()
        self.th_rsp = RspThread(port, self)
        self.th_rsp.start()
        

    def update_temp(self):
        global temp, sensor_err
        if self.chk_err.checkState() == Qt.Checked:
            sensor_err = True
        else:
            sensor_err = False

        if self.chk_random.checkState() == Qt.Checked:
            temp = gen_temp(random.randint(-1, 1))
        else:
            temp = self.spin_temp.value()
        # print temp
        


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    form = VirtualBoardDlg()
    form.show()
    sys.exit(app.exec_())
    
