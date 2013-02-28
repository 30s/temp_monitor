# -*- coding: utf-8 -*-

from sensor import *
from logger import *

BSTAT_NORMAL               = 0
BSTAT_ALL_PASTEU           = 1
BSTAT_ALL_FINISH           = 2
BSTAT_ALL_END              = 3

LOG_SENSOR_NUM_NOT_SAME    = u"风炉#%02d传感器个数与系统设置不一致!设置个数为: %02d, 实际个数为：%02d!"


class Boiler(object):
    def __init__(self, low_temp, high_temp, alert_temp, alert_hold_time,
                 pasteu_time, pasteu_alert_time, sensor_num, hi_temp_alert):
        self.id                  = 0
        self.low_temp            = low_temp
        self.high_temp           = high_temp
        self.alert_temp          = alert_temp
        self.alert_hold_time     = alert_hold_time
        self.pasteu_time         = pasteu_time
        self.pasteu_alert_time   = pasteu_alert_time
        self.sensor_num          = sensor_num
        self.sensors             = [ Sensor(self.pasteu_time, self) 
                                     for i in range(self.sensor_num)]
        self.sensor_states       = [s.state for s in self.sensors]
        self.log_started         = False
        self.state               = BSTAT_NORMAL
        self.state_trans         = [self.state_normal, self.state_pasteu, 
                                    self.state_finish, self.state_end]
        self.alarm_cmds          = {
            "red_led_on": False,  "green_led_on": False,  "alarm_on": False,
            "red_led_off": False, "green_led_off": False, "alarm_off": False,
            "close_fan": False }
        self.proc_logs           = None
        self.pasteu_alarmed      = False
        self.finish_alarmed      = False
        self.hitemp_alarmed      = False
        self.com_state           = False
        self.proc_id             = None
        

    def update(self, temp_lst):
        # print self.sensors[0].pasteu_time
        # print temp_lst
        if self.sensor_num  != len(temp_lst):
            if self.sensor_num > len(temp_lst):
                for i in range(self.sensor_num):
                    self.sensor_states[i] = STATE_ERR        
            logger.error( LOG_SENSOR_NUM_NOT_SAME % 
                          (self.id, self.sensor_num, len(temp_lst)))
            self.sensor_num = len(temp_lst)

        for idx, s in enumerate(self.sensors):
            if idx >= len(temp_lst):
                break
            self.sensor_states[idx] = s.update(temp_lst[idx])
            if (STATE_HITEMP in self.sensor_states) and (not self.hitemp_alarmed):
                # print "state_hitemp"
                self.alarm_cmds["red_led_on"] = True
                self.alarm_cmds["alarm_on"] = True
                self.hitemp_alarmed = True

            if (not (STATE_HITEMP in self.sensor_states)) and self.hitemp_alarmed:
                # print "state_normal"
                self.alarm_cmds["red_led_off"] = True
                self.alarm_cmds["alarm_off"] = True
                self.hitemp_alarmed = False
        self.state_trans[self.state]()


    def set_com_state(self, com_state):
        self.com_state = com_state


    def is_some_state(self, state):
        states = filter(lambda s: s != STATE_ERR, self.sensor_states)
        if states == [state] * len(states):
            return True
        else:
            return False


    def is_start_log(self):
        return self.is_some_state(STATE_NORMAL)


    def is_start_alarm(self):
        return self.is_some_state(STATE_PASTEU)


    def is_finish_alarm(self):
        return self.is_some_state(STATE_FINISH)


    def is_end(self):
        return self.is_some_state(STATE_END)


    def state_normal(self):
        if (not self.log_started) and self.is_start_log():
            logger.warning(u"风炉 #%02d 开始记录!" % self.id)
            # start log time            
            self.proc_logs = "start_log"
            self.log_started = True
            self.alarm_cmds["green_led_on"] = True
        if self.is_start_alarm():
            logger.warning(u"风炉 #%02d 开始巴氏消毒!" % self.id)
            # start pasteu time
            self.proc_logs = "start_pasteu"            
            self.state = BSTAT_ALL_PASTEU
            self.pasteu_alarm = time.time()
            self.alarm_cmds["red_led_on"] = True
            self.alarm_cmds["green_led_on"] = True
            self.alarm_cmds["alarm_on"] = True


    def state_pasteu(self):
        if (not self.pasteu_alarmed) and \
                (time.time() - self.pasteu_alarm > self.alert_hold_time):
            self.alarm_cmds["alarm_off"] = True
            self.pasteu_alarmed = True

        if self.is_finish_alarm():
            logger.warning(u"风炉 #%02d 巴氏消毒完成!" % self.id)
            # pasteu finish time
            self.proc_logs = "end_pasteu"
            self.state = BSTAT_ALL_FINISH
            self.finish_alarm = time.time()
            self.alarm_cmds["red_led_on"] = True
            self.alarm_cmds["alarm_on"] = True
            self.alarm_cmds["close_fan"] = True

            
    def state_finish(self):
        if (not self.finish_alarmed) and \
                (time.time() - self.finish_alarm > self.pasteu_alert_time):
            self.alarm_cmds["alarm_off"] = True
            self.finish_alarmed = True

        if self.is_end():
            # print "boiler all end"
            # end log time
            self.proc_logs = "end_log"
            logger.warning(u"风炉 #%02d 记录结束!" % self.id)
            self.state = BSTAT_ALL_END

            
    def state_end(self):
        pass
