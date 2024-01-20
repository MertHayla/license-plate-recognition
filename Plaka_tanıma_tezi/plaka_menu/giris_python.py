import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget
from giris import Ui_giris
from anamenu_python import AnapencerePage


class LoginPage(QWidget):
    def __init__(self) -> None:
        
        super().__init__()
        self.loginform = Ui_giris()
        self.loginform.setupUi(self)
        self.anapencereac = AnapencerePage()
        self.loginform.pushButton.clicked.connect(self.girisyap)
        self.loginform.pushButton_2.clicked.connect(self.cikisyap)
        self.loginform.checkBox.stateChanged.connect(self.checkdegisim)
    def girisyap(self):
        kadi = self.loginform.lineEdit.text()
        sifre= self.loginform.lineEdit_2.text()
        if kadi== "mert" and sifre == "123":
            self.close()
            self.anapencereac.show()
    def cikisyap(self):
        self.close()
    def checkdegisim(self,state):
        if self.loginform.checkBox.isChecked():
            self.loginform.lineEdit_2.setEchoMode(QLineEdit.Normal)
        else:
            self.loginform.lineEdit_2.setEchoMode(QLineEdit.Password)
            
    