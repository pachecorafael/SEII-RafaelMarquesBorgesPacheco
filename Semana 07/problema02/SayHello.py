# Rafael Pacheco - Sistemas Embasrcados 2 / Sistemas Digitais
# Engenharia Mecatrônica - UFU
# 10/07/2022 - Semestre 2021-2

# Python App with Kivy

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class SayHello(App):
    def build(self):
        self.window = GridLayout() #cria o layout com uma só coluna (formatação tipo tabela)
        self.window.cols = 1
        #add widgets to window -> customizar a página
        self.window.size_hint = (0.6,0.7) #margem sup e inf são 30% e laterais são 40%
        self.window.pos_hint = {"center_x":0.5,"center_y":0.5} #posiciona no meio

        #image widget
        self.window.add_widget(Image(source='logo.png')) #adiciona a imagem logo no fundo

        #Label widget
        self.greeting = Label(
                        text="What's your name?",
                        font_size = 18,
                        color = "00FFCE" #muda a cor do texto e o tamanho
                        )
        self.window.add_widget(self.greeting)

        #Text input widget
        self.user = TextInput(
                    multiline=False,
                    padding_y = (20,20), #adiciona um preenchimento de 20 pixels
                    size_hint = (1, 0.5)
                    ) #aceita o input do usuario (nome em uma linha)
        self.window.add_widget(self.user)

        #Button widget
        self.button = Button(
                        text="GREET",
                        size_hint = (1,0.5),
                        bold = True,
                        background_color = '00FFCE'
                        #background_normal = '' #corrige a cor do botão, sempre fica um pouco mais escura
                        ) #insere o botão
        self.button.bind(on_press=self.callback) #adiciona uma função
        self.window.add_widget(self.button)
        return self.window

    def callback(self,instance):
        self.greeting.text = "Hello " + self.user.text + "!"
        return self.window

if __name__ == "__main__":
    SayHello().run()