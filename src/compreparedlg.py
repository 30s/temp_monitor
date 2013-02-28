# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ui_compreparedlg import *
import communicate
from logger import *


SIG_PREPARE_OK         = "prepareOk()"
SIG_SHAKE_HANDS_ERR_3  = "shakeHandsErr3(int)"


class PrepareThread(QThread):
    def __init__(self, port, boilers, fan_num, parent):
        super(PrepareThread, self).__init__(parent)
        self.port = port
        self.boilers = boilers
        self.fan_num = fan_num
        self.running = False
        

    def run(self):
        self.running = True
        for i, boiler in enumerate(self.boilers):
            if not self.running:
                break

            ret = communicate.shake_hands(self.port, 0x81 + i)
            if ret[0]:
                boiler.set_com_state(ret[1] == 0)
            else:
                boiler.set_com_state(False)

            if not boiler.com_state:
                self.emit(SIGNAL(SIG_SHAKE_HANDS_ERR_3), i + 1)
                continue

            for f in range(self.fan_num):
                if not self.running:
                    break
                ret = communicate.fan_on(self.port, 0x81 + i, f + 1)
        self.emit(SIGNAL(SIG_PREPARE_OK))



class ComPrepareDlg(QDialog, Ui_ComPrepareDlg):
    def __init__(self, port, boilers, fan_num, parent=None):
        super(ComPrepareDlg, self).__init__(parent)
        self.setupUi(self)
        self.th_prepare = PrepareThread(
            port, boilers, fan_num, self)
        self.connect(logger, SIGNAL(SIG_ADD_LOG), self.add_log)
        self.connect(self.th_prepare, SIGNAL(SIG_SHAKE_HANDS_ERR_3), 
                     self.shake_hands_err_3)
        self.connect(self.th_prepare, SIGNAL(SIG_PREPARE_OK), self.prepare_ok)
        self.th_prepare.start()


    def add_log(self, log, level):
        self.edit_log.moveCursor(QTextCursor.Start, )
        log = unicode(log)
        if level == 0:
            self.edit_log.insertHtml(
                "".join(["<font color=\"black\">", log, "</font><br/> "]))
        elif level == 1:
            self.edit_log.insertHtml(
                "".join(["<font color=\"green\">", log, "</font><br/> "]))
        elif level == 2:
            self.edit_log.insertHtml(
                "".join(["<font color=\"yellow\">", log, "</font><br/> "]))
        elif level == 3:
            self.edit_log.insertHtml(
                "".join(["<font color=\"red\">", log, "</font><br/> "]))

    def prepare_ok(self):
        self.btn_start.setEnabled(True)
        self.btn_cancel.setEnabled(True)
        self.on_btn_start_clicked()

        
    @pyqtSignature("")
    def on_btn_start_clicked(self):
        self.done(QDialog.Accepted)


    @pyqtSignature("")
    def on_btn_cancel_clicked(self):
        self.done(QDialog.Rejected)


    def shake_hands_err_3(self, bid):
        log = u"风炉 #%02d 三次握手失败!" % bid
        QMessageBox.critical(self, u"监控准备", log)
        logger.error(log)


    def reject(self):
        """
        Do not let the user close the window before prepare ok
        """
        self.th_prepare.running = False
        self.th_prepare.wait()
        super(ComPrepareDlg, self).reject()


        
if __name__ == "__main__":
    import sys
    import serial
    
    port = serial.Serial('COM1', timeout=2)
    app = QApplication(sys.argv)
    form = ComPrepareDlg(port, 16, 4)
    form.show()
    sys.exit(app.exec_())

