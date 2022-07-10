# Rafael Pacheco - Sistemas Embasrcados 2 / Sistemas Digitais
# Engenharia Mecatrônica - UFU
# 10/07/2022 - Semestre 2021-2

# Recriando a interface do WhatsApp com Kivy

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.screenmanager import Screen,ScreenManager

class BoxLayout(ScreenManager):
    pass

class Whats(App):
    def build(self):
        return BoxLayout()

Whats().run()