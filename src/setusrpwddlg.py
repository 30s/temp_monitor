# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import ui_setusrpwddlg
import model


class SetUsrPwdDlg(QDialog, ui_setusrpwddlg.Ui_SetUsrPwdDlg):
    def __init__(self, usr_name, parent=None):
        super(SetUsrPwdDlg, self).__init__(parent)
        self.usr_name = usr_name
        self.setupUi(self)


    def accept(self):
        new_pwd = unicode(self.edit_new_pwd.text())
        if len(new_pwd) == 0:
            QMessageBox.warning(self, u"重设密码", u"请输入密码!")
            return

        if new_pwd != unicode(self.edit_new_pwd_2.text()):
            QMessageBox.critical(self, u"重设密码", u"两次输入的密码不一致!")
            return

        if model.set_pwd(self.usr_name, new_pwd):
            QMessageBox.information(self, u"重设密码", u"密码重设成功!")
        else:
            QMessageBox.critical(self, u"重设密码", u"重设密码失败!")
        self.done(QDialog.Accepted)

        
if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    form = SetUsrPwdDlg("abc")
    form.show()
    sys.exit(app.exec_())
    
