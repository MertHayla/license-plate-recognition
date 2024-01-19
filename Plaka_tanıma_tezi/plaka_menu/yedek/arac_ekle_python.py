import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget , QFileDialog
from PyQt5.QtGui import QIcon, QPixmap
from anamenu import *
from arac_ekle import *
import sqlite3
import sys
############################
uygulama = QApplication(sys.argv)
pencere= QWidget()
ui = Ui_arac_ekle()
ui.setupUi(pencere)

#Rbaglanti= sqlite3.connect("kayit.db")
#islem = baglanti.cursor()
#baglanti.commit()
def kayitlistele():
        baglanti= sqlite3.connect("kayit.db")
        islem = baglanti.cursor()
        baglanti.commit()
        ui.tablo_arac.clear()
        ui.tablo_arac.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        ui.tablo_arac.setHorizontalHeaderLabels(("NO","AD","SOYAD","TEL","PLAKA","ARABA TÜRÜ"))
        sorgu = "select * from kayit"
        ui.tablo_arac.setItem
        islem.execute(sorgu)
        for indexSatir,kayitNumarasi in enumerate(islem):
            for IndexSutun,kayitSutun in enumerate(kayitNumarasi):
                ui.tablo_arac.setItem(indexSatir,IndexSutun,QTableWidgetItem(str(kayitSutun)))

        

#ui.tablo_arac.setHorizontalHeaderLabels("NO","AD","SOYAD","TEL","PLAKA","ARABA_TURU")

############################
ui.kayit_listele.clicked.connect(kayitlistele)

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
        #ui.tablo_arac.clear()
        #ui.tablo_arac.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        #ui.tablo_arac.setHorizontalHeaderLabels(("NO","AD","SOYAD","TEL","PLAKA","ARABA TÜRÜ"))
        sorgu = "select * from kayit"
        self.aracekleform.tablo_arac.clear()
        #self.aracekleform.tablo_arac.horizontalHeader().setSectionResizeMode(QHeaderView.strect)
        
        islem.execute(sorgu)
        for indexSatir,kayitNumarasi in enumerate(islem):
            for IndexSutun,kayitSutun in enumerate(kayitNumarasi):
                self.aracekleform.tablo_arac.setItem(indexSatir,IndexSutun,QTableWidgetItem(str(kayitSutun)))

    

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
    
    
        
        



        
