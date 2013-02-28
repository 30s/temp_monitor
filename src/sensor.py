import time

STATE_LOTEMP   = 0
STATE_NORMAL   = 1
STATE_PASTEU   = 2
STATE_HITEMP   = 3
STATE_FINISH   = 4
STATE_END      = 5
STATE_ERR      = 6


class Sensor(object):
    def __init__(self, pasteu_time, boiler):
        self.temp = 0
        self.state = STATE_LOTEMP
        self.pasteu_time = pasteu_time
        self.boiler = boiler
        self.state_trans = [self.state_lotemp, self.state_normal,
                            self.state_pasteu, self.state_hitemp,
                            self.state_finish, self.state_end]
        self.last_update_time = 0

    
    def update(self, temp):        
        if temp == None:
            self.temp = temp
            return STATE_ERR

        if self.last_update_time == 0:
            self.last_update_time = time.time()
        self.state_trans[self.state](temp)
        self.last_update_time = time.time()
        self.temp = temp
        return self.state

    
    def state_lotemp(self, temp):
        if temp > self.boiler.low_temp:
            self.state = STATE_NORMAL


    def state_normal(self, temp):
        if temp < self.boiler.low_temp:
            self.state = STATE_LOTEMP
        elif temp > self.boiler.alert_temp:
            self.state = STATE_PASTEU

    
    def state_pasteu(self, temp):
        if temp > self.boiler.alert_temp:
            self.pasteu_time -= (time.time() - self.last_update_time)
            if self.pasteu_time <= 0:
                self.state = STATE_FINISH
                return
        if temp > self.boiler.high_temp:
            self.state = STATE_HITEMP


    def state_hitemp(self, temp):
        if temp > self.boiler.alert_temp:
            self.pasteu_time -= (time.time() - self.last_update_time)
            if self.pasteu_time <= 0:
                self.state = STATE_FINISH
                return        
        if temp < self.boiler.high_temp:
            self.state = STATE_PASTEU

            
    def state_finish(self, temp):
        if temp < self.boiler.low_temp:
            self.state = STATE_END
        

    def state_end(self, temp):
        pass
