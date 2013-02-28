# -*- coding: utf-8 -*-
"""
 @file communicatie.py
 
 Serial port communication for temperature monitoring system.
 Controler's valid address: \x81 ~ \x8F

 Frame structure:
 | start | data length | cmd | address | params | check sum | end |
 | (1B)  | HB LB (2B)  | 1B  |  1B     | <=249B | 1B        | 1B  |

 @author ax003d@gmail.com
"""

import struct
import logging
import time
import serial
from logger import logger


LOG_SEND_SHAKE_HANDS      = u"发送风炉 #%02d 握手信号..."
LOG_RSHAKE_HANDS_OK       = u"风炉 #%02d 回复握手信号 OK!" 
LOG_RSHAKE_HANDS_ERR      = u"风炉 #%02d 回复握手信号失败!" 
LOG_RSHAKE_HANDS_CODE_ERR = u"风炉 #%02d 回复握手信号通信码错误 %02X!"
LOG_SET_PARMS             = u"发送风炉 #%02d 设置参数命令...<br/> "
LOG_RSET_PARAMS_OK        = u"风炉 #%02d 设置参数成功!"
LOG_RSET_PARAMS_ERR       = u"风炉 #%02d 设置参数失败!"
LOG_OPEN_FAN              = u"开启风炉 #%02d %02d 号风机..."
LOG_ROPEN_FAN_OK          = u"风炉 #%02d %02d 号风机开启成功!"
LOG_ROPEN_FAN_ERR         = u"风炉 #%02d %02d 号风机开启失败!"
LOG_GET_TEMP_ERR          = u"风炉 #%02d 采集温度失败!"

FRAME_STRUCT    = "BH2Bs2B"
FRAME_START     = 0x24
FRAME_END       = 0x0D

CMD_SHAKE_HANDS = 0x50
CMD_GET_TEMP    = 0x52
CMD_SET_PARAMS  = 0x54
CMD_GET_PARAMS  = 0x56
CMD_FAN_ON      = 0x58
CMD_FAN_OFF     = 0x5A
CMD_ALARM_ON    = 0x5C
CMD_ALARM_OFF   = 0x5E

TRY_NUM         = 3


def print_frame(frame):
    for i in frame:
        print "0x%02X" % ord(i),
    print ""


def check_sum(frame):
    chk_sum = 0
    for i in frame:
        chk_sum ^= ord(i)
    return chk_sum


def build_send_frame(cmd, data):
    head = struct.pack('%dB' % (4 + len(data)), 
                       FRAME_START, 0, len(data), cmd, *data)
    frame = struct.pack("%ds2B" % len(head), head, check_sum(head), FRAME_END)
    # print_frame(frame)
    return frame


def common_check(port, cmd, addr):
    start = port.read(1)
    if len(start) != 1:
        # logging.error("common_check: get frame_start error!")
        return (False, )
    if ord(start) != FRAME_START:
        # logging.error(
        #     "common_check: first byte not frame_start! %02X" % ord(start))
        return (False, )

    data_len = port.read(2)
    if len(data_len) != 2:
        # logging.error("common_check: get data length error!")
        return (False, )
    if (ord(data_len[0]) != 0x00) or (ord(data_len[1]) > 0xFA):
        # logging.error("common_check: frame data length error!")
        return (False, )

    rsp = port.read(1)
    if len(rsp) != 1:
        # logging.error("common_check: get rsp code error!")
        return (False, )
    if ord(rsp) != (cmd + 1):
        # logging.error("common_check: response code error!")
        return (False, )

    length = ord(data_len[1]) + 2
    res = port.read(length)
    if len(res) != length:
        # logging.error("common_check: frame length error! %d" % len(res))
        return (False, )
    if ord(res[0]) != addr:
        # logging.error("common_check: response address error!")
        return (False, )
    if ord(res[-2]) != check_sum("".join([start, data_len, rsp, res[:-2]])):
        # logging.error("common_check: check sum error!")
        return (False, )
    if ord(res[-1]) != FRAME_END:
        # logging.error("common_check: last byte not frame_end!")
        return (False, )
    return (True, res[1: -2])


def flush_port(port):
    port.flushInput()
    port.flushOutput()


def common_send(port, cmd, params):
    port.flushInput()
    port.flushOutput()
    frame = build_send_frame(cmd, params)
    tried = 0
    while tried < TRY_NUM:
        port.write(frame)
        ret = common_check(port, cmd, params[0])
        if ret[0]:
            break
        tried += 1
        time.sleep(0.1)
    return ret


def shake_hands(port, addr):
    logger.debug(LOG_SEND_SHAKE_HANDS % (addr - 0x80))
    ret = common_send(port, CMD_SHAKE_HANDS, [addr,])
    if not ret[0]:
        logger.error(LOG_RSHAKE_HANDS_ERR % (addr - 0x80))
        return ret
    logger.info(LOG_RSHAKE_HANDS_OK % (addr - 0x80))
    return (True, ord(ret[1][0]))
    

def get_temp(port, addr):
    ret = common_send(port, CMD_GET_TEMP, [addr,])
    if not ret[0]:
        logger.error(LOG_GET_TEMP_ERR % (addr - 0x80))
        return ret
    temps = []
    for idx, i in enumerate(ret[1][::2]):
        if (i == '\xFF') and (ret[1][idx * 2 + 1] == '\xFF'):
            temps.append(None)
            continue
        minus = False
        if ord(i) > 0x7F:
            minus = True
        temp = ord(i) % 0x7F + ord(ret[1][idx * 2 + 1]) * 0.0625
        if minus:
            temp = -(temp - 1)
        temps.append(temp)
    return (True, temps)


def set_params(port, addr, alert_temp, pasteu_time, alert_hold_time):
    ret = common_send(
        port, CMD_SET_PARAMS, [addr, alert_temp, pasteu_time, alert_hold_time])
    if not ret[0]:
        return ret
    return (True, ord(ret[1][0]))


def get_params(port, addr):
    ret = common_send(port, CMD_GET_PARAMS, [addr,])
    if not ret[0]:
        return ret
    return (True, [ord(i) for i in ret[1]])


def fan_on(port, addr, fan_id):
    logger.debug(LOG_OPEN_FAN % (addr - 0x80, fan_id))
    ret = common_send(port, CMD_FAN_ON, [addr, fan_id])
    if not ret[0]:
        logger.error(LOG_ROPEN_FAN_ERR % (addr - 0x80, fan_id))
        return ret
    logger.info(LOG_ROPEN_FAN_OK % (addr - 0x80, fan_id))
    return (True, ord(ret[1][0]))    


def fan_off(port, addr, fan_id):
    ret = common_send(port, CMD_FAN_OFF, [addr, fan_id])
    if not ret[0]:
        return ret
    return (True, ord(ret[1][0]))


def alarm_on(port, addr, red, green, alarm):
    ret = common_send(port, CMD_ALARM_ON, [addr, red, green, alarm])
    if not ret[0]:
        return ret
    return (True, ord(ret[1][0]))


def alarm_off(port, addr, red, green, alarm):
    ret = common_send(port, CMD_ALARM_OFF, [addr, red, green, alarm])
    if not ret[0]:
        return ret
    return (True, ord(ret[1][0]))


if __name__ == "__main__":
    port = serial.Serial('COM1', timeout=2)
    print "shake hand:", shake_hands(port, 0x81)
    print "get temp:",   get_temp(port, 0x81)
    print "set params:", set_params(port, 0x81, 70, 30, 15)
    print "get params:", get_params(port, 0x81)
    print "fan on:",  fan_on(port, 0x81, 1)
    print "fan off:", fan_off(port, 0x81, 1)
    print "alarm on:", alarm_on(port, 0x81, True, True, True)
    print "alarm off:", alarm_off(port, 0x81, True, True, True)

