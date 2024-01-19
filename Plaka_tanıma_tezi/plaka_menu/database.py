import pymysql
baglanti = pymysql.connect(host="localhost",
                           user="root",
                           password="123456",
                           db="plaka_database",
                           charset="utf8mb4",
                           cursorclass=pymysql.cursors.DictCursor)

import sqlite3

baglanti= sqlite3.connect("kayit.db")
islem = baglanti.cursor()
baglanti.commit()

table = islem.execute("CREATE TABLE kayit (id	INTEGER NOT NULL UNIQUE,ad	text NOT NULL,soyad	text NOT NULL,tel	text NOT NULL UNIQUE,plaka	text NOT NULL UNIQUE,araba_tur	text NOT NULL,PRIMARY KEY(id AUTOINCREMENT))")
baglanti.commit()




