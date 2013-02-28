# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import ui_accountsmanagedlg
import addusrdlg
import setusrpwddlg
import model


class AccountsManageDlg(QDialog, 
                       ui_accountsmanagedlg.Ui_AccountManageDlg):
    def __init__(self, parent=None):
        super(AccountsManageDlg, self).__init__(parent)
        self.setupUi(self)
        
        accounts = model.get_usrs()
        accounts.remove(u"admin")
        self.lst_accounts.addItems(accounts)
        

    @pyqtSignature("")
    def on_btn_add_clicked(self):
        add_dlg = addusrdlg.AddUsrDlg()
        add_dlg.setModal(True)
        if QDialog.Accepted == add_dlg.exec_():
            self.lst_accounts.addItem(add_dlg.edit_usr_name.text())

    
    @pyqtSignature("")
    def on_btn_del_clicked(self):
        cur_row = self.lst_accounts.currentRow()
        if cur_row == -1:
            QMessageBox.warning(self, u"删除用户", u"请选择一个用户!")
            return

        if QMessageBox.Ok == QMessageBox.question(
            self, u"删除用户", u"确认删除该用户?", 
            QMessageBox.Ok | QMessageBox.Cancel):
            cur_item = self.lst_accounts.takeItem(cur_row)
            if model.del_usr(unicode(cur_item.text())):
                QMessageBox.information(self, u"删除用户", u"成功删除用户!")
                self.lst_accounts.removeItemWidget(cur_item)
                del cur_item
            else:
                QMessageBox.critical(self, u"删除用户", u"删除用户失败!")
                self.lst_accounts.insertItem(cur_row, cur_item)


    @pyqtSignature("")
    def on_btn_set_pwd_clicked(self):
        cur_item = self.lst_accounts.currentItem()
        if cur_item == None:
            QMessageBox.warning(self, u"重设密码", u"请选择一个用户!")
            return

        set_pwd_dlg = setusrpwddlg.SetUsrPwdDlg(unicode(cur_item.text()))
        set_pwd_dlg.exec_()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    form = AccountsManageDlg()
    form.show()
    sys.exit(app.exec_())
