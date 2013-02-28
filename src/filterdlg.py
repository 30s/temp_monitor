from PyQt4.QtCore import *
from PyQt4.QtGui import *
import ui_filterdlg


class FilterDlg(QDialog, ui_filterdlg.Ui_FilterDlg):
    def __init__(self, parser=None):
        super(FilterDlg, self).__init__(parser)
        self.setupUi(self)


    def get_bounds(self):
        return (self.spin_low.value(), self.spin_hig.value())


        
if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    form = FilterDlg()
    print form.exec_()
    form.get_bounds()
    # sys.exit(app.exec_())

