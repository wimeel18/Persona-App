from kivy.app import App
from kivymd.app  import MDApp
from kivy.uix.label import Label
from kivymd.uix.screen import MDScreen
from kivymd.uix.label import MDLabel
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.lang import Builder
from datetime import datetime
import sqlite3
import bcrypt

from screen import *

HARI_ID = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
BULAN_ID = [
"Januari", "Februari", "Maret", "April", "Mei", "Juni",
"Juli", "Agustus", "September", "Oktober", "November", "Desember"
]

import random

QUOTES = [
"Isi harimu dengan hal-hal yang membuatmu hidup.",
"Setiap hari adalah kesempatan baru untuk belajar.",
"Langkah kecil hari ini membawa perubahan besar esok.",
"Kamu dilahirkan untuk menjadi apa adanya dirimu, bukan untuk menjadi sempurna.",
"Banggalah dengan dirimu dan jangan malu dengan cara orang lain melihatmu.",
"Kesempurnaan bukan berarti tidak memiliki kelemahan, tetapi menggunakan kelemahan itu sebagai kekuatan.",
]

def get_tanggal_indonesia():
    now = datetime.now()
    hari = HARI_ID[now.weekday()]
    tanggal = now.day
    bulan = BULAN_ID[now.month - 1]
    tahun = now.year
    return f"{hari}, {tanggal} {bulan} {tahun}"

class Beranda(MDScreen):
    def __init__(self, **kwargs):
        Builder.load_file("kv/beranda.kv")
        super().__init__(**kwargs)

    def on_pre_enter(self):
        app = MDApp.get_running_app()
        nama = app.logged_user or 'User'
        if "welcome_label" in self.ids:
            self.ids.welcome_label.text = f"Hi {nama}!"
        if "tanggal_label" in self.ids:
            self.ids.tanggal_label.text = get_tanggal_indonesia()
        # ganti quote setiap kali screen beranda mau ditampilkan
        if "quote_label" in self.ids:
            self.ids.quote_label.text = random.choice(QUOTES)
            print("QUOTE:", self.ids.quote_label.text)