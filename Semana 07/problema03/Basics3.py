# Rafael Pacheco - Sistemas Embasrcados 2 / Sistemas Digitais
# Engenharia Mecatrônica - UFU
# 10/07/2022 - Semestre 2021-2

# Kivy Basics in 60 Minutes

from kivy.app import App
from kivy.uix.button import Button

class FunkyButton(Button):
    pass

class LanguageLearnerApp(App):
    def build(self):
        return FunkyButton(
            pos=(100,100),
            size_hint=(None,None),
            size=(500,500)
        )

if __name__ == '__main__':
    LanguageLearnerApp().run()