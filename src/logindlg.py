# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ui_logindlg import *
import model


class LoginDlg(QDialog, Ui_LoginDlg):
    def __init__(self, parent=None):
        super(LoginDlg, self).__init__(parent)
        self.setupUi(self)


    @pyqtSignature("")
    def on_btn_login_clicked(self):
        usr_name = unicode(self.edit_usr_name.text())
        pwd = unicode(self.edit_pwd.text())
        if not model.authenticate(usr_name, pwd):
            QMessageBox.critical(self, u"登录", u"用户名或密码错误!")            
        else:
            self.done(QDialog.Accepted)
        

    @pyqtSignature("")
    def on_btn_cancel_clicked(self):
        self.done(QDialog.Rejected)



if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    form = LoginDlg()
    form.show()
    sys.exit(app.exec_())

