import pygame

#pygame.font.init()
#pygame.mixer.init()

WIDTH, HEIGHT = 500,700 #Largura e altura da janela
WIN = pygame.display.set_mode((WIDTH,HEIGHT)) #definição de uma janela -surface - window
pygame.display.set_caption("Aeropêndulo! ")

BRANCO = (255,255,255)
PRETO = (0,0,0)

FPS = 60 #FRAMES PER SECONDS

AEROPENDULO_LARGURA, AEROPENDULO_ALTURA = 200,500

AEROPENDULO_IMAGE = pygame.image.load('aeropendulo.png') #(os.path.join('',''))
AEROPENDULO = pygame.transform.rotate(
                            pygame.transform.scale(AEROPENDULO_IMAGE,(AEROPENDULO_LARGURA, AEROPENDULO_ALTURA)), 0)#redimensioa e rotaciona

#BACKGROUND = pygame.transform.scale(pygame.image.load(''), (WIDTH, HEIGHT))#(os.path.join('Assets','space.png'))

def draw_window(aeropendulo):
    WIN.fill(BRANCO)

    WIN.blit(AEROPENDULO, (aeropendulo.x, aeropendulo.y))
    pygame.display.update()

def main():
    aeropendulo = pygame.Rect(120,20,AEROPENDULO_LARGURA,AEROPENDULO_ALTURA)
    clock = pygame.time.Clock()  # controla a velocidade do while loop
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get(): #pega todos os eventos
            if event.type == pygame.QUIT: #se algum dos eventos for de saída
                run = False #saí do while com run falso
                pygame.quit()

        draw_window(aeropendulo)

    # pygame.quit() --> fecha o jogo
    main()  # --> recomeça o jogo

if __name__ == "__main__":
    main()