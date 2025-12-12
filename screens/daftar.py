from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.dialog import MDDialog
from kivy.lang import Builder
import sqlite3
import bcrypt

class Daftar(MDScreen):
    pass

    def __init__(self, **kwargs):
        Builder.load_file("kv/daftar.kv")
        super().__init__(**kwargs)

    def submit(self):
        username = self.ids.username.text
        email = self.ids.email.text.strip().lower()
        nohp = self.ids.nohp.text
        password = self.ids.password.text
        passconf = self.ids.passconf.text
        print("DEBUG: input =", username, email)

        # cek form kosong
        if not (username and email and nohp and password and passconf):
            print("DEBUG: gagal - ada yang kosong")
            self.dialog = MDDialog(
                text="Data diri tidak boleh kosong! Untuk mengulangi klik di luar box.",
                radius=[20, 7, 20, 7],
            )
            self.dialog.open()
            return
        
            # cek panjang username 3-12 karakter
        if len(username) < 3 or len(username) > 12:
            print("DEBUG: gagal - username panjangnya tidak valid")
            self.dialog = MDDialog(
                text="Username harus 3-12 karakter, untuk mengulangi klik di luar box.",
                radius=[20, 7, 20, 7],
            )
            self.dialog.open()
            return

        # cek panjang password (kurang dari 8 -> error)
        if len(password) < 8:
            print("DEBUG: gagal - password kependekan")
            self.dialog = MDDialog(
                text="Password terlalu pendek minimal 8 karakter, untuk mengulangi klik di luar box",
                radius=[20, 7, 20, 7],
            )
            self.dialog.open()
            return
        
        if password != passconf:
            print("DEBUG: gagal - password kependekan")
            self.dialog = MDDialog(
                text="Password harus sama dengan konfirmasi password, untuk mengulangi klik di luar box.",
                radius=[20, 7, 20, 7],
            )
            self.dialog.open()
            return

        # koneksi database
        conn = None
        try:
            print("DEBUG: buka koneksi DB")
            conn = sqlite3.connect('C:/Users/Karin Sihotang/Documents/PersonaQuest.db')
            c = conn.cursor()
            c.execute("""
                CREATE TABLE IF NOT EXISTS member(
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT NOT NULL UNIQUE,
                    email TEXT NOT NULL,
                    nohp TEXT NOT NULL,
                    password BLOB NOT NULL
                )
            """)
            conn.commit()

            # cek username sdh ada
            print("DEBUG: cek username duplikat")
            c.execute("SELECT username FROM member WHERE username = ?", (username,))
            existing = c.fetchone()
            if existing:
                print("DEBUG: gagal - username sudah ada")
                self.dialog = MDDialog(
                    text="Username sudah terdaftar, untuk mengulangi klik di luar box",
                    radius=[20, 7, 20, 7],
                )
                self.dialog.open()
                return

            # simpan user baru
            print("DEBUG: insert user baru")
            hashed = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())
            c.execute(
                "INSERT INTO member(username, email, nohp, password) VALUES (?, ?, ?, ?)",
                (username, email, nohp, hashed),
            )
            conn.commit()
            print("DEBUG: insert berhasil")

            self.dialog = MDDialog(
                title="S E L A M A T",
                text="Kamu telah terdaftar, silahkan login di halaman utama.",
                radius=[20, 7, 20, 7],
            )
            self.dialog.open()

        except Exception as e:
            print("Error saat daftar:", e)
        finally:
            if conn:
                conn.close()

        #if username in z:
        #    self.dialog = MDDialog(
        #        text="Username sudah terdaftar, untuk mengulangi klik di luar box",
        #        radius=[20, 7, 20, 7],
        #    )
        #    self.dialog.open()
        #    conn.close()
        #    return

        # cek password == konfirmasi
        #if password != passconf:
        #    self.dialog = MDDialog(
        #        text="Password harus sama dengan konfirmasi password, untuk mengulangi klik di luar box.",
        #        radius=[20, 7, 20, 7],
        #    )
        #    self.dialog.open()
        #    conn.close()
        #    return

        # jika semua valid -> hash dan simpan
        #hashed = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        #c.execute(
        #    "INSERT INTO member(username, email, nohp, password) VALUES (?, ?, ?, ?)",
        #    (username, email, nohp, hashed),
        #)
        #conn.commit()
        #conn.close()

        #self.dialog = MDDialog(
        #    title="S E L A M A T",
        #    text="Kamu telah terdaftar, silahkan login di halaman utama.",
        #    radius=[20, 7, 20, 7],
        #)
        #self.dialog.open()