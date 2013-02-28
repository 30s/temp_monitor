# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ui_chgpwddlg import *
import model


class ChgPwdDlg(QDialog, Ui_ChgPwdDlg):
    def __init__(self, usr_name, parent=None):
        super(ChgPwdDlg, self).__init__(parent)
        self.setupUi(self)

        self.usr_name = usr_name

    @pyqtSignature("")
    def on_btn_ok_clicked(self):
        if not model.authenticate(
            self.usr_name, 
            unicode(self.edit_old_pwd.text())):
            QMessageBox.critical(self, u"修改密码", u"旧密码错误!")
            return

        if self.edit_new_pwd.text() != self.edit_new_pwd_2.text():
            QMessageBox.critical(self, u"修改密码", u"两次输入的密码不一致!!")
            return

        if model.set_pwd(
            self.usr_name, 
            unicode(self.edit_new_pwd.text())):
            QMessageBox.information(self, u"修改密码", u"密码修改成功!")
            self.done(QDialog.Accepted)
        else:
            QMessageBox.critical(self, u"修改密码", u"密码修改失败!")


    @pyqtSignature("")
    def on_btn_cancel_clicked(self):
        self.done(QDialog.Rejected)



if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    form = ChgPwdDlg('admin')
    form.show()
    sys.exit(app.exec_())
    
