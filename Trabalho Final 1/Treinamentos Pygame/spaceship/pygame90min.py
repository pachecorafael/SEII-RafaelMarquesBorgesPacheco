import pygame

pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 900,500 #Largura e altura da janela
WIN = pygame.display.set_mode((WIDTH,HEIGHT)) #definição de uma janela -surface - window
pygame.display.set_caption("First Game!")

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
YELLOW = (255,255,0)

BORDER = pygame.Rect(WIDTH//2 - 5, 0, 10, HEIGHT)

BULLET_HIT_SOUND = pygame.mixer.Sound('Grenade+1.mp3')
BULLET_FIRE_SOUND = pygame.mixer.Sound('Gun+Silencer.mp3')

HEALTH_FONT = pygame.font.SysFont('comicsans',40)
WINNER_FONT = pygame.font.SysFont('comicsans',30)

FPS = 60 #FRAMES PER SECONDS
VEL = 5
BULLET_VEL = 7
MAX_BULLETS = 3
SPACESHIP_WIDTH, SPACESHIP_HEIGHT = 55,40

YELLOW_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2

YELLOW_SPACESHIP_IMAGE = pygame.image.load('spaceship_yellow.png') #(os.path.join('Assets','spaceship_yellow.png))
YELLOW_SPACESHIP = pygame.transform.rotate(
                            pygame.transform.scale(YELLOW_SPACESHIP_IMAGE,(SPACESHIP_WIDTH, SPACESHIP_HEIGHT)), 90)#redimensioa e rotaciona

RED_SPACESHIP_IMAGE = pygame.image.load('spaceship_red.png') #imagens carregas como surfaces
RED_SPACESHIP = pygame.transform.rotate(
                            pygame.transform.scale(RED_SPACESHIP_IMAGE,(SPACESHIP_WIDTH, SPACESHIP_HEIGHT)),270)#redimensioa e rotaciona

SPACE = pygame.transform.scale(pygame.image.load('space.png'), (WIDTH, HEIGHT))#(os.path.join('Assets','space.png'))


def draw_window(red,yellow, red_bullets, yellow_bullets, red_health, yellow_health):
    #WIN.fill(WHITE)  # branco em rgb vai de 0 a 255 inclusos
    WIN.blit(SPACE, (0,0))
    pygame.draw.rect(WIN, BLACK, BORDER)

    red_health_text = HEALTH_FONT.render("Health: " + str(red_health),1, WHITE)
    yellow_health_text = HEALTH_FONT.render("Health: " + str(yellow_health), 1, WHITE)
    WIN.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10))
    WIN.blit(yellow_health_text, (10,10))

    WIN.blit(YELLOW_SPACESHIP, (yellow.x, yellow.y)) #blit mostra as surfaces na tela
    WIN.blit(RED_SPACESHIP,(red.x, red.y))

    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet)

    for bullet in yellow_bullets:
        pygame.draw.rect(WIN, YELLOW, bullet)


    pygame.display.update()

def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - VEL > 0:  # LEFT # bloqueia a movimentação pra fora da janela
        yellow.x -= VEL
    if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x:  # RIGHT
        yellow.x += VEL
    if keys_pressed[pygame.K_w] and yellow.y - VEL > 0:  # UP
        yellow.y -= VEL
    if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT - 15:  # DOWN #-15 pq bugou a borda inferior
        yellow.y += VEL

def red_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width:  # LEFT
        red.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width < WIDTH:  # RIGHT
        red.x += VEL
    if keys_pressed[pygame.K_UP] and red.y - VEL > 0:  # UP
        red.y -= VEL
    if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT - 15:  # DOWN
        red.y += VEL

def handle_bullets(yellow_bullets,red_bullets, yellow, red):
    for bullet in yellow_bullets:
        bullet.x += BULLET_VEL
        if red.colliderect(bullet): #checa colisão de dois obejetos rectangles
            pygame.event.post(pygame.event.Event(RED_HIT))
            yellow_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            yellow_bullets.remove(bullet)

    for bullet in red_bullets:
        bullet.x -= BULLET_VEL
        if yellow.colliderect(bullet): #checa colisão de dois obejetos rectangles
            pygame.event.post(pygame.event.Event(YELLOW_HIT))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)

def draw_winner(text):
    draw_text = WINNER_FONT.render(text,1, WHITE)
    WIN.blit(draw_text, (WIDTH/2 - draw_text.get_width()/2, HEIGHT/2 - draw_text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(5000) #mostra o resultado de vencedor por 5 segundos e depois reinicia o jogo

def main():
    red = pygame.Rect(700, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)
    yellow = pygame.Rect(100, 300, SPACESHIP_WIDTH, SPACESHIP_HEIGHT)

    red_bullets = []
    yellow_bullets =[]

    red_health = 10
    yellow_health = 10

    clock = pygame.time.Clock() #controla a velocidade do while loop
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get(): #pega todos os eventos
            if event.type == pygame.QUIT: #se algum dos eventos for de saída
                run = False #saí do while com run falso
                pygame.quit()

            if event.type == pygame.KEYDOWN: #pressionou a tecla uma vez
                if event.key == pygame.K_LCTRL and len(yellow_bullets)<MAX_BULLETS:
                    bullet = pygame.Rect(yellow.x + yellow.width, yellow.y + yellow.height//2 -2, 10, 5)
                    yellow_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()

                if event.key == pygame.K_RCTRL and len(red_bullets) <MAX_BULLETS:
                    bullet = pygame.Rect(red.x, red.y + red.height//2 - 2, 10, 5)
                    red_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()

            if event.type == RED_HIT:
                red_health -= 1
                BULLET_HIT_SOUND.play()

            if event.type == YELLOW_HIT:
                yellow_health -= 1
                BULLET_HIT_SOUND.play()

        winner_text = ""

        if red_health <= 0:
            winner_text = "Yellow Wins!"

        if yellow_health <= 0:
            winner_text = "Red Wins!"

        if winner_text != "":
            draw_winner(winner_text) #alguem ganhou (ou alguem morreu rsrs)
            break

        #print(red_bullets,yellow_bullets) testa se o control tá pressionado
        keys_pressed = pygame.key.get_pressed() # 0,0 canto superior esquerdo
        yellow_handle_movement(keys_pressed,yellow)
        red_handle_movement(keys_pressed, red)

        handle_bullets(yellow_bullets, red_bullets, yellow, red)

        #red.x += 1 #teste para ver se o retangulo vermelho representando a nave se move
        draw_window(red,yellow, red_bullets, yellow_bullets, red_health,yellow_health)

    #pygame.quit() --> fecha o jogo
    main() #--> recomeça o jogo

if __name__ == "__main__":
    main()