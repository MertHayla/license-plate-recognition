import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QWidget
from anamenu import Ui_ana_menu
from plaka_tespit_resim_python import Resim_tespitPage 
import os
import cv2
import matplotlib.pyplot as plt
import numpy as np
import pytesseract
from arac_ekle_python import AraceklePage
import serial
import time
from serial.tools import list_ports

pytesseract.pytesseract.tesseract_cmd = "C:\Program Files\Tesseract-OCR\\tesseract.exe"


arac_sayisi= 0



class AnapencerePage(QMainWindow):
    
    def __init__(self) -> None:
        super().__init__()
        self.anapencereform = Ui_ana_menu()
        self.anapencereform.setupUi(self)
        self.resimtespitac =Resim_tespitPage()
        self.araceklemeac = AraceklePage()
        self.anapencereform.resim_tespit.clicked.connect(self.resimtespit)
        #self.arac_ekleform = arac_eklePage()
        #self.anapencereform.arac_ekle.triggered.connect(self.aracekleme)
        #self.anapencereform.kamera_tespit.clicked.connect(self.kameraacma)
        #self.anapencereform.resim_tespit.clicked.connect(self.resimtespit)
        self.anapencereform.bariyer_ac.clicked.connect(self.bariyerac)
        self.anapencereform.bariyer_kapa.clicked.connect(self.bariyerkapa)
        self.anapencereform.resim_tespit.clicked.connect(self.resimtespit)
        self.anapencereform.arac_islem.triggered.connect(self.aracislemac)

        
        #self.anapencereform.arac_sil.triggered.connect(self.aracsilme)
    #def aracekleme(self):
        #
    #def aracsilme(self):
        #
    def aracislemac(self):
        self.araceklemeac.show()

    def bariyerac(self):
        global arac_sayisi
        arac_sayisi = arac_sayisi+1
        self.anapencereform.arac_sayi_label.setText(str(arac_sayisi))
        arduino = serial.Serial('COM7',9600)
        a =0
        while a<3:
            arduino.write(b'1')
            time.sleep(90/100)
            a=a+1
            while(a == 2):
                break
        
    def bariyerkapa(self):
        global arac_sayisi
        arac_sayisi = arac_sayisi-1
        self.anapencereform.arac_sayi_label.setText(str(arac_sayisi))
        arduino = serial.Serial('COM7',9600)
        b=0
        while b<3:
            arduino.write(b'0')
            time.sleep(90/100)
            b= b+1
            while(b==2):
                break
    def resimtespit(self):
        self.resimtespitac.show()
