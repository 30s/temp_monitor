# -*- coding: utf-8 -*-

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import ui_addusrdlg
import model

class AddUsrDlg(QDialog, ui_addusrdlg.Ui_AddUsrDlg):
    def __init__(self, parent=None):
        super(AddUsrDlg, self).__init__(parent)
        self.setupUi(self)


    def accept(self):
        usr_name = unicode(self.edit_usr_name.text())
        pwd = unicode(self.edit_pwd.text())
        if (len(usr_name) == 0) or (len(pwd) == 0):
            QMessageBox.warning(self, u"添加用户", u"请填写完整信息!")
            return
        if model.add_usr(usr_name, pwd):
            QMessageBox.information(self, u"添加用户", u"添加用户成功!")
        else:
            QMessageBox.critical(self, u"添加用户", u"添加用户失败!")
        self.done(QDialog.Accepted)
        

if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    form = AddUsrDlg()
    form.show()
    sys.exit(app.exec_())
    
