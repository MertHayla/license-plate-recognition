# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'arac_sil.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_arac_sil_form(object):
    def setupUi(self, arac_sil_form):
        arac_sil_form.setObjectName("arac_sil_form")
        arac_sil_form.resize(1236, 811)
        self.groupBox = QtWidgets.QGroupBox(arac_sil_form)
        self.groupBox.setGeometry(QtCore.QRect(10, 20, 961, 101))
        self.groupBox.setObjectName("groupBox")
        self.label = QtWidgets.QLabel(self.groupBox)
        self.label.setGeometry(QtCore.QRect(50, 30, 55, 16))
        self.label.setObjectName("label")
        self.ara_plaka = QtWidgets.QLineEdit(self.groupBox)
        self.ara_plaka.setGeometry(QtCore.QRect(20, 50, 113, 22))
        self.ara_plaka.setObjectName("ara_plaka")
        self.ara_tel = QtWidgets.QLineEdit(self.groupBox)
        self.ara_tel.setGeometry(QtCore.QRect(140, 50, 113, 22))
        self.ara_tel.setObjectName("ara_tel")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(170, 30, 81, 16))
        self.label_2.setObjectName("label_2")
        self.ara_ad = QtWidgets.QLineEdit(self.groupBox)
        self.ara_ad.setGeometry(QtCore.QRect(260, 50, 113, 22))
        self.ara_ad.setObjectName("ara_ad")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(280, 30, 61, 16))
        self.label_3.setObjectName("label_3")
        self.ara_soyad = QtWidgets.QLineEdit(self.groupBox)
        self.ara_soyad.setGeometry(QtCore.QRect(380, 50, 113, 22))
        self.ara_soyad.setObjectName("ara_soyad")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(400, 30, 81, 16))
        self.label_4.setObjectName("label_4")
        self.ara_button = QtWidgets.QPushButton(self.groupBox)
        self.ara_button.setGeometry(QtCore.QRect(530, 50, 93, 28))
        self.ara_button.setObjectName("ara_button")
        self.temizle_button = QtWidgets.QPushButton(self.groupBox)
        self.temizle_button.setGeometry(QtCore.QRect(650, 50, 93, 28))
        self.temizle_button.setObjectName("temizle_button")
        self.arac_sil = QtWidgets.QPushButton(self.groupBox)
        self.arac_sil.setGeometry(QtCore.QRect(770, 50, 93, 28))
        self.arac_sil.setObjectName("arac_sil")
        self.groupBox_2 = QtWidgets.QGroupBox(arac_sil_form)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 140, 1201, 651))
        self.groupBox_2.setObjectName("groupBox_2")
        self.tableWidget = QtWidgets.QTableWidget(self.groupBox_2)
        self.tableWidget.setGeometry(QtCore.QRect(20, 30, 1171, 601))
        self.tableWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setMidLineWidth(0)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget.verticalHeader().setSortIndicatorShown(True)
        self.tableWidget.verticalHeader().setStretchLastSection(True)

        self.retranslateUi(arac_sil_form)
        QtCore.QMetaObject.connectSlotsByName(arac_sil_form)

    def retranslateUi(self, arac_sil_form):
        _translate = QtCore.QCoreApplication.translate
        arac_sil_form.setWindowTitle(_translate("arac_sil_form", "Araç Sil"))
        self.groupBox.setTitle(_translate("arac_sil_form", "Abone Ara"))
        self.label.setText(_translate("arac_sil_form", "Plaka"))
        self.label_2.setText(_translate("arac_sil_form", "Telefon"))
        self.label_3.setText(_translate("arac_sil_form", "Abone Adı"))
        self.label_4.setText(_translate("arac_sil_form", "Abone Soyadı"))
        self.ara_button.setText(_translate("arac_sil_form", "ARA"))
        self.temizle_button.setText(_translate("arac_sil_form", "TEMİZLE"))
        self.arac_sil.setText(_translate("arac_sil_form", "ARAÇ SİL"))
        self.groupBox_2.setTitle(_translate("arac_sil_form", "Aboneler"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("arac_sil_form", "No"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("arac_sil_form", "Abone Adı"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("arac_sil_form", "Abone Soyadı"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("arac_sil_form", "Araç Plakası"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("arac_sil_form", "Araç Türü"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("arac_sil_form", "Telefon Numarası"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    arac_sil_form = QtWidgets.QWidget()
    ui = Ui_arac_sil_form()
    ui.setupUi(arac_sil_form)
    arac_sil_form.show()
    sys.exit(app.exec_())
