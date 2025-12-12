from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.screenmanager import ScreenManager
from kivy.core.text import LabelBase
from kivy.core.window import Window

Window.maximize()

from screens.screen import *
from screens.beranda import Beranda
from screens.quizmbti import QuizScreen

class WindowManager(ScreenManager):
    pass

class PersonaQuest(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.logged_user = None

    def build(self):
        Builder.load_file("kv/hallog.kv")
        Builder.load_file("kv/daftar.kv")
        Builder.load_file("kv/beranda.kv")
        Builder.load_file("kv/quizmbti.kv")

        self.wm = WindowManager()
        screens = [
            Hallog(name = "hallog"),
            Daftar(name = "daftar"),
            Beranda(name = "beranda"),
            QuizScreen(name = "quizmbti")
        ]
        for screen in screens:
            self.wm.add_widget(screen)
        return self.wm
    
    def logout(self):
        self.wm.current = "hallog"
    
if __name__ == '__main__':
    LabelBase.register(name = "TT-Slabs", fn_regular = "kv/asset/font/OttineSlab-Regular.ttf")
    LabelBase.register(name = "OpenSans", fn_regular = "kv/asset/font/OpenSans-Bold.ttf")
    LabelBase.register(name = "Monradok", fn_regular = "kv/asset/font/MonradokTrial-Regular.otf")
    LabelBase.register(name = "LeagueSpartan", fn_regular = "kv/asset/font/leaguespartan-bold.ttf")
    PersonaQuest().run()
    