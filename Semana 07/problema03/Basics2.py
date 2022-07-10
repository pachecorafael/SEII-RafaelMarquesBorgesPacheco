# Rafael Pacheco - Sistemas Embasrcados 2 / Sistemas Digitais
# Engenharia Mecatrônica - UFU
# 10/07/2022 - Semestre 2021-2

# Kivy Basics in 60 Minutes

from kivy.app import App
from kivy.uix.button import Button

class FunkyButton(Button):
    def __init__(self,**kwargs):
        super(FunkyButton,self).__init__(**kwargs)
        self.text = "Funky Button"
        self.pos = (100,100)
        self.size_hint = (.25,.25)

 class LanguageLearnerApp(App): #criação da subclasse -> sempre deve terminar com App
    def build(self):
        return FunkyButton()


if __name__ == '__main__':
    LanguageLearnerApp().run()

