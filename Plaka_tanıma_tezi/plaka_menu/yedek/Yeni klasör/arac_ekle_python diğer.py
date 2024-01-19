import typing
import enum
from ast import Index
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget , QFileDialog
from PyQt5.QtGui import QIcon, QPixmap
from anamenu import *
from arac_ekle import *
import sqlite3
import sys
############################
#uygulama = QApplication(sys.argv)
#pencere= QWidget()
#ui = Ui_arac_ekle()
#ui.setupUi(pencere)








#ui.tablo_arac.setHorizontalHeaderLabels("NO","AD","SOYAD","TEL","PLAKA","ARABA_TURU")

############################


class AraceklePage(QWidget):
    
    def __init__(self) -> None:
        super().__init__()
        self.aracekleform = Ui_arac_ekle()
        self.aracekleform.setupUi(self)
        self.aracekleform.kaydet_arac.clicked.connect(self.arackaydet)
        self.aracekleform.kayit_listele.clicked.connect(self.kayitlistele)


    def kayitlistele(self):
        baglanti= sqlite3.connect("kayit.db")
        islem = baglanti.cursor()
        baglanti.commit()
        
        ad=islem.execute("select ad from kayit")
        soyad=islem.execute("select soyad from kayit")
        tel=islem.execute("select tel from kayit")
        plaka_nu =islem.execute("select plaka from kayit")
        ara_tur=islem.execute("select arac_tur from kayit")
        self.aracekleform.tablo_arac.setColumnWidth(0,10)
        self.aracekleform.tablo_arac.setColumnWidth(1,60)
        self.aracekleform.tablo_arac.setColumnWidth(2,60)
        self.aracekleform.tablo_arac.setColumnWidth(3,60)
        self.aracekleform.tablo_arac.setColumnWidth(4,60)
        self.aracekleform.tablo_arac.setRowCount(len(islem))
        satir =0
        sutun=0
        for veriler in islem:
            ad=islem.execute("select ad from kayit")
            soyad=islem.execute("select soyad from kayit")
            tel=islem.execute("select tel from kayit")
            plaka_nu =islem.execute("select plaka from kayit")
            ara_tur=islem.execute("select arac_tur from kayit")
            self.aracekleform.tablo_arac.setColumnWidth(0,10)
            self.aracekleform.tablo_arac.setColumnWidth(1,60)
            self.aracekleform.tablo_arac.setColumnWidth(2,60)
            self.aracekleform.tablo_arac.setColumnWidth(3,60)
            self.aracekleform.tablo_arac.setColumnWidth(4,60)
            self.aracekleform.tablo_arac.setItem(int(satir),0,QTableWidgetItem(str(ad)))
            self.aracekleform.tablo_arac.setItem(int(satir),0,QTableWidgetItem(str(soyad)))
            self.aracekleform.tablo_arac.setItem(int(satir),0,QTableWidgetItem(str(tel)))
            self.aracekleform.tablo_arac.setItem(int(satir),0,QTableWidgetItem(str(plaka_nu)))
            self.aracekleform.tablo_arac.setItem(int(satir),0,QTableWidgetItem(str(ara_tur)))
            satir +=1
    

    def arackaydet(self):
        baglanti= sqlite3.connect("kayit.db")
        islem = baglanti.cursor()
        baglanti.commit()
        #id = None
        ad =self.aracekleform.ad_linedit.text()
        soyad = self.aracekleform.soy_ad_linedit.text()
        tel_no = self.aracekleform.tel_lineedit.text()
        plaka = self.aracekleform.arac_plaka.text()
        arac_tur = self.aracekleform.arac_tur_combobox.currentText()
        try:
            
            ekle = ("INSERT INTO kayit (ad,soyad,tel,plaka,araba_tur) values (?,?,?,?,?)")
            islem.execute(ekle,(ad,soyad,tel_no,plaka,arac_tur))
            baglanti.commit()
            
        except:
            pass
    
    
        
        



        
