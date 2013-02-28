# -*- coding: utf-8 -*-

#
# @file Application.pyw
#
# Temperature Monitor's application entry.
# 
# @author ax003d@gmail.com
#
# Change Logs:
# 
#

import sys
import sip
sip.setapi('QVariant', 2)

from mainwindow import MainWindow
from PyQt4 import QtGui
from logindlg import *


def main():
    app = QtGui.QApplication(sys.argv)
    # app.setOrganizationName("Qtrac Ltd.")
    # app.setOrganizationDomain("qtrac.eu")
    app.setApplicationName("Temperature Monitor")
    app.setWindowIcon(QIcon(":images/tempmonitor.ico"))
    # app.setWindowIcon(QIcon(":/icon.ico"))    
    dlg_login = LoginDlg()
    if  QDialog.Accepted != dlg_login.exec_():
        return 
    main_win = MainWindow(unicode(dlg_login.edit_usr_name.text()))
    main_win.showMaximized()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
