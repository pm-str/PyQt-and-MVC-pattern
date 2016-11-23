from PyQt5.QtWidgets import QMainWindow
from View.Window import Ui_Form
from PyQt5 import QtWidgets
import sys

from Model.MModel import Model


class View(QMainWindow):

    def __init__(self, model, parent=None):

        super(QMainWindow, self).__init__(parent)

        self.model = model

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.ui.lv_details.setModel(model)
        self.ui.pb_ready.clicked.connect(self.ready)

    def ready(self):
        data = {
            'type': 1 if self.ui.rb_corporate.isChecked() else 2,
            'capacity': self.ui.cb_quantity.currentText(),
            'dt': self.ui.dte_datetime.dateTime(),
            'issms': 1 if self.ui.cb_issms.isChecked() else 0,
            'phone': self.ui.le_phone.text()
        }
        self.model.to_book(**data)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    a = View(Model())
    a.show()
    sys.exit(app.exec_())
