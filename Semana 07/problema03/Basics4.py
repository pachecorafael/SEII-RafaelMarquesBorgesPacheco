# Rafael Pacheco - Sistemas Embasrcados 2 / Sistemas Digitais
# Engenharia Mecatrônica - UFU
# 10/07/2022 - Semestre 2021-2

# Kivy Basics in 60 Minutes


from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.widget import Widget

class GameScreen(Widget):
    pass


class LanguageLearnerApp(App):
    def build(self):
        return GameScreen()

if __name__ == '__main__':
    LanguageLearnerApp().run()