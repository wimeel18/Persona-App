from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.dialog  import MDDialog
from kivy.lang import Builder
import sqlite3
import bcrypt

class Hallog(MDScreen):
    pass

    def __init__(self, **kwargs):
        Builder.load_file("kv/hallog.kv")
        super().__init__(**kwargs)

    def loginAcc(self):
        email = self.ids.email.text.strip().lower()
        password = self.ids.password.text

                # cek input kosong
        if not (email and password):
            self.dialog = MDDialog(
                text="Password dan email tidak boleh kosong! Untuk mengulangi klik di luar box.",
                radius=[20, 7, 20, 7],
            )
            self.dialog.open()
            return
        
        conn = None
        try:
            # ambil data user berdasarkan email
            conn = sqlite3.connect('C:/Users/Karin Sihotang/Documents/PersonaQuest.db')
            c = conn.cursor()
            c.execute("SELECT username, password FROM member WHERE email = ?", (email,))
            row = c.fetchone()
        
            if row is None:
                self.dialog = MDDialog(
                    text="Maaf email tidak terdaftar! untuk mengulangi klik di luar box.",
                    radius=[20, 7, 20, 7],
                )
                self.dialog.open()
                return

            nama_user, hashed_password = row

            # cek password benar
            if not bcrypt.checkpw(password.encode('utf-8'), hashed_password):
                self.dialog = MDDialog(
                    text="Password salah! Untuk mengulangi klik di luar box.",
                    radius=[20, 7, 20, 7],
                )
                self.dialog.open()
                return

            # jika lolos semua
            app = MDApp.get_running_app()
            app.logged_user = nama_user
            self.manager.current = "beranda"

        except Exception as e:
            print("Error saat login:", e)
        finally:
            if conn:
                conn.close()

        #if not (email and password):
#
 #           conn = sqlite3.connect('C:/Users/Karin Sihotang/Documents/PersonaQuest.db')
  #          c = conn.cursor()
   #         c.execute("SELECT username, email, password FROM member")
    #        rows = c.fetchall()
     #       conn.close()

      #      userdata = {email: (username, hashed_pw) for (username, email, hashed_pw) in rows}

       #     if email in userdata:
        #        nama_user, hashed_password = userdata[email]
         #       if bcrypt.checkpw(password.encode(), hashed_password):
          #          print("Berhasil login!")

           #         app = MDApp.get_running_app()
            #        app.logged_user = nama_user   
             #       self.manager.current = "beranda"
              #  else:
               #     self.dialog = MDDialog(
                #        text = "Password salah! Untuk mengulangi klik di luar box.",
                 #  )
                  #  self.dialog.open()
                   # return
#            else:
 #               self.dialog = MDDialog(
  #                  text = "Maaf email tidak terdaftar! untuk mengulangi klik di luar box.",
   #                 radius = [20, 7, 20, 7]
    #            )
     #           self.dialog.open()
      #          return
       # else:
        #    self.dialog = MDDialog(
         #       text = "Password dan email tidak boleh kosong! Untuk mengulangi klik di luar box.",
          #      radius = [20, 7, 20, 7]
           # )
#            self.dialog.open()
 #       return 
    
