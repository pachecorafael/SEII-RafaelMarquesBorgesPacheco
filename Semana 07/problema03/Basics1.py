# Rafael Pacheco - Sistemas Embasrcados 2 / Sistemas Digitais
# Engenharia Mecatrônica - UFU
# 10/07/2022 - Semestre 2021-2

# Kivy Basics in 60 Minutes

from kivy.app import App
from kivy.uix.button import Button

class LanguageLearnerApp(App): #criação da subclasse -> sempre deve terminar com App
    def build(self):
        return Button(
            text="Hello World",
            pos=(50,50), #pixels -> origem no canto inferior esquerdo
            #size=(500,500),
            size_hint = (0.8,0.8) #faz o tamanho do botão ser reponsivo ao tamanho da tela
            )


if __name__=='__main__':
    LanguageLearnerApp().run()