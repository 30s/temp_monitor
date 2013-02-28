# -*- coding: utf-8 -*-
#!/usr/bin/env python
#
# @file model.py
#
# @author ax003d@gmail.com
#

import os
import sys
import time
import datetime
import traceback
import sqlite3
from PyQt4.QtCore import Qt
from PyQt4.QtGui import QColor

COLORS = [QColor(Qt.white), QColor(Qt.green), QColor(Qt.yellow), 
          QColor(Qt.red), QColor(Qt.red), QColor(Qt.red)]

MAX_SENSOR_NUM = 40

DB_CONFIG = "config.db3"

DB_LOG = "data_log_%s.db3"

TBL_USR = """
CREATE TABLE tbl_usr (id INTEGER PRIMARY KEY, usr_name TEXT UNIQUE, pwd TEXT)
"""

SQL_GET_USR = "SELECT * FROM tbl_usr WHERE usr_name=?"

RET_NO_SUCH_USR = u"该用户不存在!"
RET_PWD_ERR     = u"密码错误！"

ERRNO_OK              = 0
ERRNO_NO_SUCH_USR     = 1
ERRNO_PWD_ERR         = 2

SQL_SET_PWD = "UPDATE tbl_usr SET pwd=? WHERE usr_name=?"
SQL_ADD_USR = "INSERT INTO tbl_usr(usr_name, pwd) VALUES(?, ?)"
SQL_DEL_USR = "DELETE FROM tbl_usr WHERE usr_name=?"
SQL_GET_USRS = "SELECT usr_name FROM tbl_usr"

TBL_BOILER_CONFIG = """
CREATE TABLE tbl_boiler_config (id INTEGER PRIMARY KEY, low_temp INTEGER, 
high_temp INTERGER, alert_temp INTERGER, alert_hold_time INTERGER,
pasteu_time INTERGER, pasteu_alert_time INTERGER, sensor_num INTERGER, 
hi_temp_alert INTERGER)
"""

SQL_GET_BOILER_CONFIG = "SELECT * FROM tbl_boiler_config"

SQL_SET_SENSOR_NUM = "UPDATE tbl_boiler_config SET sensor_num=? WHERE id = 0"

SQL_GET_BOILER_CONFIG_BY_ID = "SELECT * FROM tbl_boiler_config WHERE id=?"

SQL_SET_BOILER_CONFIG = """UPDATE tbl_boiler_config SET low_temp=?,
high_temp=?, alert_temp=?, alert_hold_time=?, pasteu_time=?,
pasteu_alert_time=?, sensor_num=?, hi_temp_alert=? WHERE id=?"""

SQL_ADD_BOILER_CONFIG = """INSERT INTO tbl_boiler_config VALUES
(?, ?, ?, ?, ?, ?, ?, ?, ?)"""


TBL_SYS_CONFIG = """
CREATE TABLE tbl_sys_config (boiler_num INTERGER, com_str TEXT, 
company_info TEXT, fan_num INTERGER, acq_intvl INTERGER, timeout INTERGER)
"""

SQL_GET_SYS_CONFIG = "SELECT * FROM tbl_sys_config LIMIT 1"
SQL_SET_BOILER_NUM = "UPDATE tbl_sys_config SET boiler_num =?"
SQL_SET_COM_STR = "UPDATE tbl_sys_config SET com_str=?"
SQL_SET_COMPANY_INFO = "UPDATE tbl_sys_config SET company_info=?"
SQL_SET_FAN_NUM = "UPDATE tbl_sys_config SET fan_num=?"
SQL_SET_ACQ_INTVL = "UPDATE tbl_sys_config SET acq_intvl=?"
SQL_SET_TIMEOUT = "UPDATE tbl_sys_config SET timeout=?"


SQL_DEFAULT_USR = """INSERT INTO tbl_usr 
VALUES(NULL, 'admin', '123456')"""

SQL_GLOBAL_BOILER_CONFIG = """INSERT INTO tbl_boiler_config 
VALUES(0, 50, 75, 71, 15, 2100, 20, 20, 2)"""

SQL_DEFAULT_SYS_CONFIG = """INSERT INTO tbl_sys_config 
VALUES(7, 'COM1;9600', 'XXX Company', 4, 1, 1000)"""

TBL_PASTEU_PROCS = """
CREATE TABLE tbl_pasteu_procs (id INTEGER PRIMARY KEY, boiler_id INTEGER,
start_log TIMESTAMP NOT NULL DEFAULT (DATETIME('now', 'localtime')), 
start_pasteu TIMESTAMP, end_pasteu TIMESTAMP, end_log TIMESTAMP)
"""

SQL_ADD_PASTEU_PROCS = """
INSERT INTO tbl_pasteu_procs(boiler_id) VALUES(?)
"""

SQL_GET_PASTEU_PROCS = """
SELECT * FROM tbl_pasteu_procs WHERE boiler_id = ?
"""

SQL_PASTEU_STARTED = """
UPDATE tbl_pasteu_procs SET start_pasteu = (DATETIME('now', 'localtime')) WHERE id = ?
"""

SQL_PASTEU_FINISHED = """
UPDATE tbl_pasteu_procs SET end_pasteu = (DATETIME('now', 'localtime')) WHERE id = ?
"""

SQL_LOG_FINISHED = """
UPDATE tbl_pasteu_procs SET end_log = (DATETIME('now', 'localtime')) WHERE id = ?
"""

TBL_DATA_LOG = """
CREATE TABLE tbl_data_log (id INTEGER PRIMARY KEY AUTOINCREMENT, 
log_date TIMESTAMP NOT NULL DEFAULT (STRFTIME('%s', 'now')),
boiler_id INTEGER, 
sensor_1 INTEGER,
sensor_2 INTEGER,
sensor_3 INTEGER,
sensor_4 INTEGER,
sensor_5 INTEGER,
sensor_6 INTEGER,
sensor_7 INTEGER,
sensor_8 INTEGER,
sensor_9 INTEGER,
sensor_10 INTEGER,
sensor_11 INTEGER,
sensor_12 INTEGER,
sensor_13 INTEGER,
sensor_14 INTEGER,
sensor_15 INTEGER,
sensor_16 INTEGER,
sensor_17 INTEGER,
sensor_18 INTEGER,
sensor_19 INTEGER,
sensor_20 INTEGER,
sensor_21 INTEGER,
sensor_22 INTEGER,
sensor_23 INTEGER,
sensor_24 INTEGER,
sensor_25 INTEGER,
sensor_26 INTEGER,
sensor_27 INTEGER,
sensor_28 INTEGER,
sensor_29 INTEGER,
sensor_30 INTEGER,
sensor_31 INTEGER,
sensor_32 INTEGER,
sensor_33 INTEGER,
sensor_34 INTEGER,
sensor_35 INTEGER,
sensor_36 INTEGER,
sensor_37 INTEGER,
sensor_38 INTEGER,
sensor_39 INTEGER,
sensor_40 INTEGER )
"""

SQL_ADD_LOG = """INSERT INTO tbl_data_log(boiler_id, 
sensor_1, sensor_2, sensor_3, sensor_4, sensor_5, sensor_6, sensor_7, sensor_8, 
sensor_9, sensor_10, sensor_11, sensor_12, sensor_13, sensor_14, sensor_15, 
sensor_16, sensor_17, sensor_18, sensor_19, sensor_20, sensor_21, sensor_22, 
sensor_23, sensor_24, sensor_25, sensor_26, sensor_27, sensor_28, sensor_29, 
sensor_30, sensor_31, sensor_32, sensor_33, sensor_34, sensor_35, sensor_36, 
sensor_37, sensor_38, sensor_39, sensor_40) 
VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 
?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""

SQL_GET_SENSOR_LOG = """SELECT log_date, sensor_%d FROM tbl_data_log 
WHERE boiler_id=? AND log_date > ? AND log_date < ?"""




class ConfigManager:
    def __init__(self):
        self._connect = None
        self._cursor = None

        if not os.path.exists(DB_CONFIG):
            self.create_db()
        else:
            self._connect = sqlite3.connect(DB_CONFIG)
            self._cursor = self._connect.cursor()            
            

    def create_db(self):
        self._connect = sqlite3.connect(DB_CONFIG)
        self._cursor = self._connect.cursor()
        self._cursor.execute(TBL_USR)
        self._cursor.execute(SQL_DEFAULT_USR)

        self._cursor.execute(TBL_BOILER_CONFIG)
        self._cursor.execute(SQL_GLOBAL_BOILER_CONFIG)

        self._cursor.execute(TBL_SYS_CONFIG)
        self._cursor.execute(SQL_DEFAULT_SYS_CONFIG)

        # self._cursor.execute(TBL_PASTEU_PROCS)
        self._connect.commit()


    def authenticate(self, usr_name, pwd):
        try:
            self._cursor.execute(SQL_GET_USR, (usr_name,))
            result = self._cursor.fetchone()
            if not result:
                return False
            if pwd != result[2]:
                return False
            return True
        except Exception, e:
            print e
            return False


    def set_pwd(self, usr_name, new_pwd):
        try:
            self._cursor.execute(SQL_SET_PWD, (new_pwd, usr_name))
            self._connect.commit()
            if self._cursor.rowcount == 1:
                return True
            else:
                return False
        except Exception, e:
            print e
            return False


    def add_usr(self, usr_name, pwd):
        try:
            self._cursor.execute(SQL_ADD_USR, (usr_name, pwd))
            self._connect.commit()
            if self._cursor.rowcount == 1:
                return True
            else:
                return False
        except sqlite3.IntegrityError, e:
            print e
            return False


    def del_usr(self, usr_name):
        try:
            self._cursor.execute(SQL_DEL_USR, (usr_name,))
            self._connect.commit()
            if self._cursor.rowcount == 1:
                return True
            else:
                return False
        except Exception, e:
            print e
            return False


    def get_usrs(self):
        try:
            self._cursor.execute(SQL_GET_USRS)
            return [record[0] for record in self._cursor.fetchall()]
        except Exception, e:
            print e
            return None


    def get_sys_config(self):
        try:
            self._cursor.execute(SQL_GET_SYS_CONFIG)
            return self._cursor.fetchone()
        except Exception, e:
            print e
            return None


    def get_boiler_config(self):
        try:
            self._cursor.execute(SQL_GET_BOILER_CONFIG)
            return self._cursor.fetchall()
        except Exception, e:
            print e
            return None


    def set_boiler_num(self, num):
        try:
            self._cursor.execute(SQL_SET_BOILER_NUM, (num,))
            self._connect.commit()
            if self._cursor.rowcount == 1:
                return True
            else:
                return False
        except Exception, e:
            print e
            return False


    def set_sensor_num(self, num):
        try:
            self._cursor.execute(SQL_SET_SENSOR_NUM, (num,))
            self._connect.commit()
            if self._cursor.rowcount == 1:
                return True
            else:
                return False
        except Exception, e:
            print e
            return False


    def set_boiler_config(self, bid, configs):
        try:
            self._cursor.execute(SQL_GET_BOILER_CONFIG_BY_ID, (bid, ))
            if not self._cursor.fetchone():
                self._cursor.execute(SQL_ADD_BOILER_CONFIG, tuple([bid] + configs))
            else:
                self._cursor.execute(SQL_SET_BOILER_CONFIG, tuple(configs + [bid]))
            self._connect.commit()
            if self._cursor.rowcount == 1:
                return True
            else:
                return False
        except Exception, e:
            print e            
            traceback.print_tb(sys.exc_info()[2])
            return False

    
    def set_company_info(self, info):
        try:
            self._cursor.execute(SQL_SET_COMPANY_INFO, (info, ))
            self._connect.commit()
            if self._cursor.rowcount == 1:
                return True
            else:
                return False
        except Exception, e:
            print e
            return False


    def set_com_str(self, com_str):
        try:
            self._cursor.execute(SQL_SET_COM_STR, (com_str, ))
            self._connect.commit()
            if self._cursor.rowcount == 1:
                return True
            else:
                return False
        except Exception, e:
            print e
            return False


    def common_set(self, sql, params):
        try:
            self._cursor.execute(sql, params)
            self._connect.commit()
            if self._cursor.rowcount == 1:
                return True
            else:
                return False
        except Exception, e:
            print e
            return False
    

    def set_fan_num(self, fan_num):
        return self.common_set(SQL_SET_FAN_NUM, (fan_num, ))


    def set_acq_intvl(self, acq_intvl):
        return self.common_set(SQL_SET_ACQ_INTVL, (acq_intvl, ))


    def set_timeout(self, timeout):
        return self.common_set(SQL_SET_TIMEOUT, (timeout, ))


    def add_pasteu_procs(self, boiler_id):
        if self.common_set(SQL_ADD_PASTEU_PROCS, (boiler_id,)):
            return self._cursor.lastrowid 
        return False


    def pasteu_started(self, proc_id):
        return self.common_set(SQL_PASTEU_STARTED, (proc_id,))

    
    def pasteu_finished(self, proc_id):
        return self.common_set(SQL_PASTEU_FINISHED, (proc_id,))


    def log_finished(self, proc_id):
        return self.common_set(SQL_LOG_FINISHED, (proc_id,))


    def get_pasteu_procs(self, boiler_id):
        try:
            self._cursor.execute(SQL_GET_PASTEU_PROCS, (boiler_id,))
            return self._cursor.fetchall()
        except Exception, e:
            print e
            return []


class BoilerConfig(object):
    def __init__(self, configs=[]):
        self.low_temp,
        self.high_temp,
        self.alert_temp,
        self.alert_hold_time,
        self.pasteu_time,
        self.pasteu_alert_time,
        self.sensor_num,
        self.hi_temp_alert = configs[1:]


class DataLogger(object):
    def __init__(self, path):
        self._connect = None
        self._cursor = None

        if not os.path.exists(path):
            self.create_db(path)
        else:
            self._connect = sqlite3.connect(path)
            self._cursor = self._connect.cursor()


    def close(self):
        self._cursor.close()
        self._connect.close()


    def create_db(self, path):
        self._connect = sqlite3.connect(path)
        self._cursor = self._connect.cursor()
        self._cursor.execute(TBL_DATA_LOG)
        self._connect.commit()

        
    def add_log(self, boiler_id, temps):
        vals = [boiler_id]
        none_append = [None] * (40 - len(temps))
        vals.extend(temps)
        vals.extend(none_append)
        try:
             self._cursor.execute(SQL_ADD_LOG, tuple(vals)).lastrowid
        except Exception, e:
            print e


    def commit(self):
        try:
            self._connect.commit()
        except Exception, e:
            print e


    def get_boiler_log(self, boiler_id, start_t, end_t):
        pass


    def get_sensor_log(self, boiler_id, sensor_id, start_t, end_t):
        try:
            self._cursor.execute(SQL_GET_SENSOR_LOG % sensor_id, 
                                 (boiler_id, start_t, end_t))
            return self._cursor.fetchall()
        except Exception, e:
            print e
            return []



CONFIG_MAN = ConfigManager()
DATA_LOGGER = DataLogger(time.strftime("%Y-%m") + ".db3")


def authenticate(usr_name, pwd):
    return CONFIG_MAN.authenticate(usr_name, pwd)


def set_pwd(usr_name, pwd):
    return CONFIG_MAN.set_pwd(usr_name, pwd)


def add_usr(usr_name, pwd):
    return CONFIG_MAN.add_usr(usr_name, pwd)


def del_usr(usr_name):
    return CONFIG_MAN.del_usr(usr_name)


def get_usrs():
    return CONFIG_MAN.get_usrs()


def get_sys_config():
    return CONFIG_MAN.get_sys_config()


def get_boiler_config():
    boiler_config = {}
    configs = CONFIG_MAN.get_boiler_config()
    for c in configs:
        boiler_config[c[0]] = list(c[1:])
    return boiler_config


def set_boiler_num(num):
    return CONFIG_MAN.set_boiler_num(num)


def set_sensor_num(num):
    return CONFIG_MAN.set_sensor_num(num)


def set_boiler_config(configs):
    for bid in configs.keys():
        if not CONFIG_MAN.set_boiler_config(bid, configs[bid]):
            return False
    return True


def set_company_info(info):
    return CONFIG_MAN.set_company_info(info)


def set_com_str(com_str):
    return CONFIG_MAN.set_com_str(com_str)


def set_fan_num(fan_num):
    return CONFIG_MAN.set_fan_num(fan_num)


def set_acq_intvl(acq_intvl):
    return CONFIG_MAN.set_acq_intvl(acq_intvl)


def set_timeout(timeout):
    return CONFIG_MAN.set_timeout(timeout)


def add_pasteu_procs(boiler_id):
    return CONFIG_MAN.add_pasteu_procs(boiler_id)


def get_pasteu_procs(boiler_id):
    return CONFIG_MAN.get_pasteu_procs(boiler_id)


def pasteu_started(proc_id):
    return CONFIG_MAN.pasteu_started(proc_id)


def pasteu_finished(proc_id):
    return CONFIG_MAN.pasteu_finished(proc_id)


def log_finished(proc_id):
    return CONFIG_MAN.log_finished(proc_id)


def add_log(boiler_id, data):
    DATA_LOGGER.add_log(boiler_id, data)


def get_log_db_names(start_t, end_t):
    log_db_names = []
    year = start_t.year
    month = start_t.month
    dt = datetime.datetime(year, month, 1)
    while end_t > dt:
        log_db_names.append("%d-%02d.db3" % (dt.year, dt.month))
        year += month / 12
        month = month % 12 + 1
        dt = datetime.datetime(year, month, 1)
    return log_db_names


def get_sensor_log(boiler_id, sensor_id, start_t, end_t):
    # print boiler_id, sensor_id, start_t, end_t
    logs = []
    db_names = get_log_db_names(start_t, end_t)
    str_start = time.mktime(start_t.timetuple())
    str_end   = time.mktime(end_t.timetuple())
    for i in db_names:
        if not os.path.exists(i):
            continue
        logger = DataLogger(i)
        logs.extend(logger.get_sensor_log(
                boiler_id - 1, sensor_id, str_start, str_end))
        logger.close()
    return logs


def conf_test():
    conf_man = ConfigManager()
    conf_man.authenticate('admin', 'abc')
    conf_man.set_pwd('abc', '123')
    conf_man.set_pwd('admin', '123')
    proc_id = conf_man.add_pasteu_procs(1)
    time.sleep(1)
    conf_man.pasteu_started(proc_id)
    time.sleep(1)
    conf_man.pasteu_finished(proc_id)
    time.sleep(1)
    conf_man.log_finished(proc_id)
    


def data_test():
    # print len(get_sensor_log(1, 1, 
    #                          datetime.datetime(2011, 10, 27, 20, 41, 20, 234000),
    #                          datetime.datetime(2011, 10, 27, 20, 41, 23, 234000)))
    # print len(get_sensor_log(1, 1, 
    #                          datetime.datetime(2011, 10, 27, 20, 19, 54, 140000),
    #                          datetime.datetime(2011, 10, 27, 20, 21, 14, 140000)))
    # print len(get_sensor_log(1, 1, 
    #                          datetime.datetime(2011, 10, 30, 20, 19, 54, 140000),
    #                          datetime.datetime(2011, 10, 30, 20, 21, 14, 140000)))
    # return
    dl = DataLogger("./201108.db3")
    dl.add_log(1, [50] * 25)
    dl.commit()
    dl.get_sensor_log(1, 20, "2008-01-10", "2013-01-10")
    


if __name__ == '__main__':
    data_test()
    # conf_test()
