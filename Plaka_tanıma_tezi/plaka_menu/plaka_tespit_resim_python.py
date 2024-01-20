import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget , QFileDialog
from PyQt5.QtGui import QIcon, QPixmap
from anamenu import Ui_ana_menu
from plaka_tespit_resim import Ui_resim_tespit
import os
import sqlite3
import cv2
import matplotlib.pyplot as plt
import numpy as np
import pytesseract
from PyQt5.QtSql import QSqlDatabase, QSqlQuery

pytesseract.pytesseract.tesseract_cmd = "C:\Program Files\Tesseract-OCR\\tesseract.exe"#BU PYTESSERACT KURULUMUNUN KONUMU OLACAK.


arac_sayisi= 0
class Resim_tespitPage(QWidget):
    def __init__(self,) -> None:
        super().__init__()
        self.resim_tespitform = Ui_resim_tespit()
        self.resim_tespitform.setupUi(self)
        self.resim_tespitform.pushButton_2.clicked.connect(self.browse)
        self.resim_tespitform.plaka_oku.clicked.connect(self.plakaokuma)
        
    def plakakayitac(self):
        self.araceklemeac.show()
        
    def browse(self): # Dosya yolunun seçildiği bölüm.
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            print(fileName)
        self.resim_tespitform.lineEdit.setText(fileName)
        pixmap = QPixmap(fileName)
        self.resim_tespitform.label_resim.setPixmap(pixmap)
        
    def plakaokuma(self): #plaka okumanın gerçekleştiği bölüm.
        resim_adres_line = self.resim_tespitform.lineEdit.text()
        img = cv2.imread(resim_adres_line)
        
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
                    
                    cv2.imwrite(f"{metin}.jpg",plaka_resmi)
                    plaka_metni = self.resim_tespitform.okunan_plaka.text()
                    baglanti= sqlite3.connect("kayit.db")
                    islem = baglanti.cursor()
                    baglanti.commit()
                    silinmişveri = metin.strip("\n")
                    
                    islem.execute("SELECT * FROM kayit WHERE plaka = ? ",(silinmişveri,))
                    data = islem.fetchall()
                    print("Data Verisi:"+str(data))
                    listesiz_data=str(data)
                    plaka_verileri = listesiz_data.split(',')
                    silinecekler1 = "'"
                    silinecekler2 = " "
                    yenimetin = plaka_verileri[3].replace(silinecekler1,"")
                    yenimetin= yenimetin.replace(silinecekler2,"")
                    plaka_yeni = silinmişveri.replace(silinecekler2,"")
                    
                    plaka_ad = plaka_verileri[0].replace(silinecekler1,"") # okunan verideki anlamsız ',' boşluk gibi karakterlerin silindiği bölüm
                    plaka_ad = plaka_ad.replace("[","")
                    plaka_ad =plaka_ad.replace("(","")
                    plaka_soyad = plaka_verileri[1].replace(silinecekler1,"")
                    
                    

                    if str(yenimetin) == str(plaka_yeni):
                        self.resim_tespitform.giris_izni.setText("Giriş İzni Var")
                        self.resim_tespitform.musteriadi.setText(plaka_ad+" "+plaka_soyad)
                    else:
                        self.resim_tespitform.giris_izni.setText("Giriş İzni Yok")

                    

                    
                    self.resim_tespitform.okunan_plaka.setText(plaka_yeni)
                    self.resim_tespitform.giris_izni.setStyleSheet("color: green")
                    self.resim_tespitform.giris_izni.setStyleSheet("font-weight: bold")
                    
                    
                    return metin
                    metin = None
                    
                    break
    
        
