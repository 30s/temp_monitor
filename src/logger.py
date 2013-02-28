from PyQt4.QtCore import QObject, SIGNAL

SIG_ADD_LOG = "addLog(QString, int)"


class Logger(QObject):
    def __init__(self, parent=None):
        super(Logger, self).__init__(parent)

    
    def debug(self, log):
        self.emit(SIGNAL(SIG_ADD_LOG), log, 0)

        
    def info(self, log):
        self.emit(SIGNAL(SIG_ADD_LOG), log, 1)
    

    def warning(self, log):
        self.emit(SIGNAL(SIG_ADD_LOG), log, 2)


    def error(self, log):
        self.emit(SIGNAL(SIG_ADD_LOG), log, 3)


logger = Logger()
