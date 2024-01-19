import typing
from PyQt5 import QtCore
from ast import Index
import enum
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget , QFileDialog
from PyQt5.QtGui import QIcon, QPixmap
from anamenu import *
from arac_ekle import *
import sqlite3
import sys
from plaka_tespit_resim_python import *
############################
uygulama = QApplication(sys.argv)
pencere= QWidget()
ui = Ui_arac_ekle()
ui.setupUi(pencere)

baglanti= sqlite3.connect("kayit.db")
islem = baglanti.cursor()
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
        self.aracekleform.kayit_sil.clicked.connect(self.kayitsil)
        self.aracekleform.plaka_oku_buton.clicked.connect(self.plakaokuma)
        self.aracekleform.browse_button.clicked.connect(self.browse)
    

        


    def kayitlistele(self):
        baglanti= sqlite3.connect("kayit.db")
        islem = baglanti.cursor()
        baglanti.commit()
        #ui.tablo_arac.clear()
        #ui.tablo_arac.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        #ui.tablo_arac.setHorizontalHeaderLabels(("NO","AD","SOYAD","TEL","PLAKA","ARABA TÜRÜ"))
        sorgu = "select * from kayit"
        self.aracekleform.tablo_arac.clear()
        #self.aracekleform.tablo_arac.horizontalHeader().setSectionResizeMode(QHeaderView.trect)
        
        islem.execute(sorgu)
        
        for indexSatir,kayitNumarasi in enumerate(islem):
            for IndexSutun,kayitSutun in enumerate(kayitNumarasi):
                self.aracekleform.tablo_arac.setItem(indexSatir,IndexSutun,QTableWidgetItem(str(kayitSutun)))
    
    def kayitsil(self):

        baglanti= sqlite3.connect("kayit.db")
        islem = baglanti.cursor()
        baglanti.commit()
        sil_mesaj = QMessageBox.question(pencere,"Silme Onayi","Silmek istediğinize eminmisiniz ?")
        QMessageBox.Yes | QMessageBox.No
        if sil_mesaj == QMessageBox.Yes:
            secilen_kayit = self.aracekleform.tablo_arac.selectedItems()#self.aracekleform.tablo_arac.selectedItems()
            
            silinecek_kayit = secilen_kayit[0].text()
            sorgu = "delete from kayit where ad = ?"

            try:
                islem.execute(sorgu,(str(silinecek_kayit),))
                baglanti.commit()
                
                
                #kayitlistele()
            except:
                pass
        else:
            ui.statusbar.showMessage("Silme işlemi İptal Edildi")
                    

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

    def browse(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            print(fileName)
        self.aracekleform.lineEdit_browse.setText(fileName)#self.resim_tespitform.lineEdit.setText(fileName)
        #pixmap = QPixmap(fileName)
        #self.resim_tespitform.label_resim.setPixmap(pixmap)
        #self.resize(pixmap.width(),pixmap.height())

    def plakaokuma(self):
        resim_adres_line = self.aracekleform.lineEdit_browse.text()#self.resim_tespitform.lineEdit.text()
        #resim_adresler = os.listdir(resim_adres_line)
        img = cv2.imread(resim_adres_line)#+"/"+resim_adresler[0])
        plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
        img_bgr = img
        img_gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

        ir_img = cv2.medianBlur(img_gray,5)
        ir_img = cv2.medianBlur(ir_img,5)

        medyan = np.median(ir_img)
        low = 0.67*medyan
        high = 1.33*medyan
        
        kenarlik = cv2.Canny(ir_img,low,high)

        kenarlik = cv2.dilate(kenarlik,np.ones((3,3),np.uint8),iterations=1)

        cnt = cv2.findContours(kenarlik,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        cnt = cnt[0]
        cnt = sorted(cnt,key=cv2.contourArea,reverse=True)
        H,W = 500,500
        plaka = None
        for c in cnt:
             rect = cv2.minAreaRect(c) #dikdortgen yapıda al (1)
             (x,y),(w,h),r = rect
             if(w>h and w>h*2) or (h>w and h>w*2):#oran en az 2 (2)
                box = cv2.boxPoints(rect) #[[12,13],[25,13],[20,13],[13,45]]
                box = np.int64(box)
                minx = np.min(box[:,0])
                miny = np.min(box[:,1])
                maxx = np.max(box[:,0])
                maxy = np.max(box[:,1])

                muh_plaka = img_gray[miny:maxy,minx:maxx].copy()
                muh_medyan = np.median(muh_plaka)
                kon1 = muh_medyan>53 and muh_medyan<200 # yogunluk kontrolu (3)
                kon2 = (w<483 and h<100)##(w<48 and h<170) or (h<50 and w<170) #sınır kontrolu (4)
                kon3 = (w<100 and h<400) #or (h<50 and w<170) #sınır kontrolu (4)
                #print(f"muh_plaka medyan:{muh_medyan} genislik: {w} yukseklik:{h}")
                kon=False
                if(kon1 and (kon2 or kon3)):
                    cv2.drawContours(img,[box],0,(0,255,0),2)
                    plaka =[int(i) for i in [minx,miny,w,h]]#x,y,w,h
                    kon=True
                    if(plaka[2]<plaka[3]):
                        plaka_resmi=img_gray[plaka[1]:plaka[1]+plaka[2],plaka[0]:plaka[0]+plaka[3]].copy()
                    else:
                        plaka_resmi=img_gray[plaka[1]:plaka[1]+plaka[3],plaka[0]:plaka[0]+plaka[2]].copy()
                else:
                    pass
                if(kon):
                    metin = pytesseract.image_to_string(plaka_resmi)
                    #plt.title(f"Plaka:{metin}")
                    cv2.imwrite(f"{metin}.jpg",plaka_resmi)
                    yaz_metin = metin.strip("\n")
                    self.aracekleform.arac_plaka.setText(yaz_metin)
                    baglanti= sqlite3.connect("kayit.db")
                    islem = baglanti.cursor()
                    baglanti.commit()
                    

                    return metin
                    metin = None
                    
                    break
    #def resim_goster_ac(self):
        #self.resim_tespitform.label_resim.setScaledContents(True)
        



        
