# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Window.ui'
#
# Created by: PyQt5 UI code generator 5.5.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(502, 382)
        Form.setStyleSheet("background-color: rgb(255, 255, 255);")
        Form.setInputMethodHints(QtCore.Qt.ImhHiddenText)
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(230, 20, 261, 351))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setFrameShape(QtWidgets.QFrame.Box)
        self.label_3.setScaledContents(False)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_6.addWidget(self.label_3)
        self.lv_details = QtWidgets.QListView(self.layoutWidget)
        self.lv_details.setObjectName("lv_details")
        self.verticalLayout_6.addWidget(self.lv_details)
        self.layoutWidget1 = QtWidgets.QWidget(Form)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 20, 210, 351))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setFrameShape(QtWidgets.QFrame.Box)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.rb_corporate = QtWidgets.QRadioButton(self.layoutWidget1)
        self.rb_corporate.setChecked(True)
        self.rb_corporate.setObjectName("rb_corporate")
        self.verticalLayout.addWidget(self.rb_corporate)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.rb_standart = QtWidgets.QRadioButton(self.layoutWidget1)
        self.rb_standart.setObjectName("rb_standart")
        self.horizontalLayout.addWidget(self.rb_standart)
        self.cb_quantity = QtWidgets.QComboBox(self.layoutWidget1)
        self.cb_quantity.setEnabled(True)
        self.cb_quantity.setObjectName("cb_quantity")
        self.cb_quantity.addItem("")
        self.cb_quantity.addItem("")
        self.cb_quantity.addItem("")
        self.cb_quantity.addItem("")
        self.cb_quantity.addItem("")
        self.cb_quantity.addItem("")
        self.cb_quantity.addItem("")
        self.cb_quantity.addItem("")
        self.cb_quantity.addItem("")
        self.cb_quantity.addItem("")
        self.horizontalLayout.addWidget(self.cb_quantity)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.verticalLayout_5.addLayout(self.verticalLayout_2)
        spacerItem = QtWidgets.QSpacerItem(20, 28, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_2.setFrameShape(QtWidgets.QFrame.Box)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_3.addWidget(self.label_2)
        self.dte_datetime = QtWidgets.QDateTimeEdit(self.layoutWidget1)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dte_datetime.sizePolicy().hasHeightForWidth())
        self.dte_datetime.setSizePolicy(sizePolicy)
        self.dte_datetime.setMaximumSize(QtCore.QSize(16777215, 300))
        self.dte_datetime.setInputMethodHints(QtCore.Qt.ImhPreferNumbers)
        self.dte_datetime.setDate(QtCore.QDate(2000, 1, 1))
        self.dte_datetime.setMaximumDateTime(QtCore.QDateTime(QtCore.QDate(7999, 12, 31), QtCore.QTime(23, 59, 59)))
        self.dte_datetime.setCalendarPopup(True)
        self.dte_datetime.setObjectName("dte_datetime")
        self.verticalLayout_3.addWidget(self.dte_datetime)
        self.verticalLayout_5.addLayout(self.verticalLayout_3)
        spacerItem1 = QtWidgets.QSpacerItem(20, 28, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_5.addItem(spacerItem1)
        self.label_4 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_4.setFrameShape(QtWidgets.QFrame.Box)
        self.label_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_4.setObjectName("label_4")
        self.verticalLayout_5.addWidget(self.label_4)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.cb_issms = QtWidgets.QCheckBox(self.layoutWidget1)
        self.cb_issms.setText("")
        self.cb_issms.setObjectName("cb_issms")
        self.horizontalLayout_2.addWidget(self.cb_issms)
        self.le_phone = QtWidgets.QLineEdit(self.layoutWidget1)
        self.le_phone.setInputMethodHints(QtCore.Qt.ImhNone)
        self.le_phone.setFrame(True)
        self.le_phone.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.le_phone.setDragEnabled(True)
        self.le_phone.setReadOnly(False)
        self.le_phone.setPlaceholderText("")
        self.le_phone.setObjectName("le_phone")
        self.horizontalLayout_2.addWidget(self.le_phone)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 28, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem2)
        self.verticalLayout_5.addLayout(self.verticalLayout_4)
        self.pb_ready = QtWidgets.QPushButton(self.layoutWidget1)
        self.pb_ready.setStyleSheet("background-color: rgb(230, 208, 208);")
        self.pb_ready.setObjectName("pb_ready")
        self.verticalLayout_5.addWidget(self.pb_ready)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form1"))
        self.label_3.setText(_translate("Form", "Детали заказа"))
        self.label.setText(_translate("Form", "Тип заказа"))
        self.rb_corporate.setText(_translate("Form", "Корпоративный"))
        self.rb_standart.setText(_translate("Form", "Стандартный"))
        self.cb_quantity.setItemText(0, _translate("Form", "1"))
        self.cb_quantity.setItemText(1, _translate("Form", "2"))
        self.cb_quantity.setItemText(2, _translate("Form", "3"))
        self.cb_quantity.setItemText(3, _translate("Form", "4"))
        self.cb_quantity.setItemText(4, _translate("Form", "5"))
        self.cb_quantity.setItemText(5, _translate("Form", "6"))
        self.cb_quantity.setItemText(6, _translate("Form", "7"))
        self.cb_quantity.setItemText(7, _translate("Form", "8"))
        self.cb_quantity.setItemText(8, _translate("Form", "9"))
        self.cb_quantity.setItemText(9, _translate("Form", "10"))
        self.label_2.setText(_translate("Form", "Дата и время заказа"))
        self.label_4.setText(_translate("Form", "Уведомление по смс"))
        self.le_phone.setInputMask(_translate("Form", "+7-999-999-99-99"))
        self.le_phone.setText(_translate("Form", "+7-800-000-11-77"))
        self.pb_ready.setText(_translate("Form", "Готово"))
