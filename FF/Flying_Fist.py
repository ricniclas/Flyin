import math, random, sys, time
import pygame
from pygame.locals import *
from operator import itemgetter
import pickle
import ptext
import Tela_Inicial


# Essa função define parametros da janela do windows que será aberta
def events():
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()


pygame.display.set_caption("Claaaaase")

AndarDireita = [pygame.image.load('images\Personagem_Sprites\Personagem__Andando_1.png'),
                pygame.image.load('images\Personagem_Sprites\Personagem__Andando_2.png'),
                pygame.image.load('images\Personagem_Sprites\Personagem__Andando_3.png'),
                pygame.image.load('images\Personagem_Sprites\Personagem__Andando_4.png'),
                pygame.image.load('images\Personagem_Sprites\Personagem__Andando_5.png'),
                pygame.image.load('images\Personagem_Sprites\Personagem__Andando_6.png'),
                ]
AndarEsquerda = [pygame.image.load('images\Personagem_Sprites\R_Personagem__Andando_1.png'),
                 pygame.image.load('images\Personagem_Sprites\R_Personagem__Andando_2.png'),
                 pygame.image.load('images\Personagem_Sprites\R_Personagem__Andando_3.png'),
                 pygame.image.load('images\Personagem_Sprites\R_Personagem__Andando_4.png'),
                 pygame.image.load('images\Personagem_Sprites\R_Personagem__Andando_5.png'),
                 pygame.image.load('images\Personagem_Sprites\R_Personagem__Andando_6.png'),
                 ]

Soco = [pygame.image.load('images\Personagem_Sprites\Personagem__Soco_0.png'),
        pygame.image.load('images\Personagem_Sprites\Personagem__Soco_1.png'),
        pygame.image.load('images\Personagem_Sprites\Personagem__Soco_3.png'),
        pygame.image.load('images\Personagem_Sprites\Personagem__Soco_4.png')
        ]

char = pygame.image.load('images\Personagem_Sprites\Personagem__Parado_0.png')

clock = pygame.time.Clock()


class player(object):
    def __init__(self, x, y, largura, altura, playerVelocityX, playerVelocityY):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.playerVelocityX = playerVelocityX
        self.playerVelocityY = playerVelocityX
        self.esquerda = False
        self.direita = False
        self.baixo = False
        self.cima = False
        self.soco = False
        self.parado = False
        self.ContarPassos = 0
        self.HP = 155
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)

    def draw(self, Janela):
        if self.ContarPassos + 1 >= 27:
            self.ContarPassos = 0

        if self.esquerda:
            Janela.blit(AndarEsquerda[self.ContarPassos // 5], (self.x, self.y))
            self.ContarPassos += 3
        elif self.direita:
            Janela.blit(AndarDireita[self.ContarPassos // 5], (self.x, self.y))
            self.ContarPassos += 3
        elif self.cima:
            Janela.blit(AndarDireita[self.ContarPassos // 5], (self.x, self.y))
            self.ContarPassos += 3
        elif self.baixo:
            Janela.blit(AndarDireita[self.ContarPassos // 5], (self.x, self.y))
            self.ContarPassos += 3

        elif self.soco:
            Janela.blit(Soco[self.ContarPassos // 50], (self.x, self.y))
            self.ContarPassos += 3




        else:
            if self.direita:
                Janela.blit(AndarDireita[0], (self.x, self.y))
            else:
                Janela.blit(AndarDireita[0], (self.x, self.y))
        self.hitbox = (self.x + 17, self.y + 11, 70, 90)
        pygame.draw.rect(Janela, (255, 0, 0), self.hitbox, 2)


class projetosoco(object):
    def __init__(self, x, y, raio, cor, mira):
        self.x = x
        self.y = y
        self.raio = raio
        self.cor = cor
        self.mira = mira
        self.vel = 8 * mira

    def draw(self, Janela):
        pygame.draw.circle(Janela, self.cor, (self.x, self.y), self.raio)


class inimigo(object):
    Direta = [pygame.image.load('images\inimigo\R1E.png'), pygame.image.load('images\inimigo\R2E.png'),
              pygame.image.load('images\inimigo\R3E.png'),
              pygame.image.load('images\inimigo\R4E.png'), pygame.image.load('images\inimigo\R5E.png'),
              pygame.image.load('images\inimigo\R6E.png'),
              pygame.image.load('images\inimigo\R7E.png'), pygame.image.load('images\inimigo\R8E.png'),
              pygame.image.load('images\inimigo\R9E.png'),
              pygame.image.load('images\inimigo\R10E.png'), pygame.image.load('images\inimigo\R11E.png')]
    Esquerda = [pygame.image.load('images\inimigo\L1E.png'), pygame.image.load('images\inimigo\L2E.png'),
                pygame.image.load('images\inimigo\L3E.png'),
                pygame.image.load('images\inimigo\L4E.png'), pygame.image.load('images\inimigo\L5E.png'),
                pygame.image.load('images\inimigo\L6E.png'),
                pygame.image.load('images\inimigo\L7E.png'), pygame.image.load('images\inimigo\L8E.png'),
                pygame.image.load('images\inimigo\L9E.png'),
                pygame.image.load('images\inimigo\L10E.png'), pygame.image.load('images\inimigo\L11E.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.health = 10
        self.visible = True

    def draw(self, win):
        self.move()
        if self.visible:
            if self.walkCount + 1 >= 33:
                self.walkCount = 0

            if self.vel > 0:
                win.blit(self.Direta[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1
            else:
                win.blit(self.Esquerda[self.walkCount // 3], (self.x, self.y))
                self.walkCount += 1

            pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(win, (0, 128, 0),
                             (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))
            self.hitbox = (self.x + 17, self.y + 2, 31, 57)
            # pygame.draw.rect(win, (255,0,0), self.hitbox,2)

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0

    def hit(self):
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False
        print('miseravi')


# Classes e seus parametros


Classe = player(200, 410, 64, 64, 64, 64)
inimigo = inimigo(100, 410, 64, 64, 450)
loop = 0
socobala = []

# Propriedades da Janela a ser aberta
Largura, Altura = 640, 448
HW, HH = Largura / 2, Altura / 2
Area = Largura * Altura
Nome_da_Janela = "FLYING FIST"

# Esse código inicializa a Janela com as propriedades definidas nas variaveis
pygame.init()
CLOCK = pygame.time.Clock()
Janela = pygame.display.set_mode((Largura, Altura))
pygame.display.set_caption(Nome_da_Janela)

# mainClock = FPS
mainClock = pygame.time.Clock()

# Esta variável controlará as telas do jogo
Controlador_Jogo = 1

# Essa variável define a pontuação do jogador, e o Timer da fase
Score = 0
Timer = 60
Nome_do_player = ("AKI")

# Scoreboard_Player = {'Nome':Nome_do_player, 'Pontos': Score}


Leaderboard = [
    {'Nome': ("AAA"), 'Pontos': 3000},
    {'Nome': ("AAA"), 'Pontos': 4000},
    {'Nome': ("AAA"), 'Pontos': 5000},
    {'Nome': ("AAA"), 'Pontos': 2000},
    {'Nome': ("AAA"), 'Pontos': 300},
]

# Leaderboard.insert(0, Scoreboard_Player)
# Leaderboard.sort(key=itemgetter('Pontos'), reverse=True)

# sorted(Leaderboard, key=itemgetter('Pontos'), reverse=True)


# pickle.dump(Leaderboard, open("top_scores", "wb"))
Load_Top_Scores = pickle.load(open("top_scores", "rb"))

for key in Load_Top_Scores:
    print(key)

# Essa carrega uma fonte para o projeto do jogo, definindo seu tamanho
fonte_small = pygame.font.Font("fontes/start.ttf", 18)
fonte_med = pygame.font.Font("fontes/start.ttf", 25)
fonte_big = pygame.font.Font("fontes/start.ttf", 35)

# Carrega as imagem do jogo em geral
Background_Fase = pygame.image.load("images/Background_Fase.png").convert()
Background_Tela_Inicial = pygame.image.load("images/Tela_Inicial/Tela_de_Titulo.png").convert()
Personagem_HUD = pygame.image.load("images/Personagem_Vida.png").convert_alpha()

# Define a Altura e Largura do background
Background_Largura, Background_Altura = Background_Fase.get_rect().size

# Define o tamanho da fase
Fase_Largura = Background_Largura * 10
# Define a posicao do background da fase em relação a janela
Background_Fase_Posicao = 0
startScrollingPosX = HW

# Propriedades da Janela a ser aberta
Largura, Altura = 640, 448
HW, HH = Largura / 2, Altura / 2
Area = Largura * Altura
Nome_da_Janela = "FLYING FIST"

# Variaveis relacionadas ao Personagem
circleRadius = 25
circlePosX = circleRadius
Classe.x = circleRadius + 50
Classe.y = 300
Classe.playerVelocityX = 0
Classe.playerVelocityY = 0

# Vraiaves de inimigos
inimigo.y = 300

# Musica é tocada assim que executa o jogo, mas não em loop
# Musica_Fase = pygame.mixer.music.load('Musica_SFX\Musica_Fase.wav')
pygame.mixer.music.load('Musica_SFX\intro.mp3')
pygame.mixer.music.play(1)

SFX_Punch1 = pygame.mixer.Sound('Musica_SFX\SFX\Punch_1.wav')
SFX_Punch2 = pygame.mixer.Sound('Musica_SFX\SFX\Punch_2.wav')
SFX_Miss = pygame.mixer.Sound('Musica_SFX\SFX\Punch_miss.wav')
SFX_Death = pygame.mixer.Sound('Musica_SFX\SFX\Death.wav')
SFX_Text = pygame.mixer.Sound('Musica_SFX\SFX\Text_Sound.wav')

Cutscene1 = pygame.image.load("images/Tela_Inicial/Cutscene1.jpg").convert()
Cutscene2 = pygame.image.load("images/Tela_Inicial/Cutscene2.jpg").convert()
Cutscene3 = pygame.image.load("images/Tela_Inicial/Cutscene3.jpg").convert()

text_orig = """O mundo já não é

mais o mesmo """

text_orig2 = """As guerras apagaram 

todos os registros 

históricos """

text_orig3 = """Não existe mais passado

ou futuro.

Apenas sobrevivência """

text_orig4 = """Sem família, a única

coisa que importa para

Akira é lutar """

text_orig5 = """Seu mestre reconhece seu 

potencial, mas a fúria de

Akira é seu maior inimigo. """

text_orig6 = """Após a morte de seu

mestre, Akira decide voltar

Para seu vilarejo """

text_orig7 = """Mas a raiva que banhava

seu coração também era a

realidade de sua vila """

text_orig8 = """Sua cidade era dominada

pela gangue de Kobra """

text_orig9 = """E somente ele poderia 

defender seu lar """

text_orig10 = """Esse é seu destino.

Akira irá pulverizar todos 

que ameacem o seu povo! """

text_orig11 = """E com suas próprias
mãos! """

# Create an iterator so that we can get one character after the other.
text_iterator = iter(text_orig)
text_iterator2 = iter(text_orig2)
text_iterator3 = iter(text_orig3)
text_iterator4 = iter(text_orig4)
text_iterator5 = iter(text_orig5)
text_iterator6 = iter(text_orig6)
text_iterator7 = iter(text_orig7)
text_iterator8 = iter(text_orig8)
text_iterator9 = iter(text_orig9)
text_iterator10 = iter(text_orig10)
text_iterator11 = iter(text_orig11)

text = ''
text2 = ''
text3 = ''
text4 = ''
text5 = ''
text6 = ''
text7 = ''
text8 = ''
text9 = ''
text10 = ''
text11 = ''

textnumber = 1


def redrawGameWindow():
    if Controlador_Jogo == 1:
        Janela.blit(Background_Tela_Inicial, (0, -10))
        Tela_Inicial.Press_Start.blit(Janela, (110, 320))
        Tela_Inicial.Tela_de_titulo_animacao.blit(Janela, (0, -10))

        pygame.display.update()
    if Controlador_Jogo == 0:
        Janela.blit(Background_Fase, (rel_x, 0), )
        # Janela.blit ( Texto_Timer , ((Largura / 2) - 17 , 10) )
        # Janela.blit ( Texto_Placar , (190 , 30) )

        Janela.blit(Personagem_HUD, (10, 10))
        pygame.draw.rect(Janela, (255, 255, 0), (78, 57, Classe.HP, 19), 0)
        Classe.draw(Janela)
        inimigo.draw(Janela)

        seconds = int((pygame.time.get_ticks() - start_ticks) / 1000)

        ptext.draw(str(Score), topleft=(190, 28), fontname="fontes/start.ttf", color=(255, 100, 0),
                   gcolor=(255, 200, 20), fontsize=19,
                   shadow=(3, 1), scolor="#000000")
        ptext.draw(str(Timer - seconds), center=(Largura / 2, 30), fontname="fontes/start.ttf", color=(255, 255, 255),
                   gcolor=(150, 150, 150),
                   shadow=(3, 3), scolor="#000000")

        for balau in socobala:
            balau.draw(Janela)

        pygame.display.update()


# mainloop

run = True

while run:

    keys = pygame.key.get_pressed()

    # Essa parte do código é referente ao SideScrolling e posição do personagem na tela. Para entender, ver https://www.youtube.com/watch?v=AX8YU2hLBUg&t=478s
    # Controlador_Jogo é igual a 1, você está na tela de título

    if Classe.x > Fase_Largura:
        Classe.x = Fase_Largura
    if Classe.x < circleRadius:
        Classe.x = circleRadius
    if Classe.x < startScrollingPosX:
        Classe.x = Classe.x
    elif Classe.x > Fase_Largura - startScrollingPosX:
        Classe.x = Classe.x - Fase_Largura + Largura
    else:
        Classe.x = startScrollingPosX
        Background_Fase_Posicao += -Classe.playerVelocityX

    rel_x = Background_Fase_Posicao % Background_Largura

    Janela.blit(Background_Fase, (rel_x - Background_Largura, 0))

    clock.tick(27)

    if loop > 0:
        loop += 1
    if loop > 3:
        loop = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    for bullet in socobala:
        if bullet.y - bullet.raio < inimigo.hitbox[1] + inimigo.hitbox[3] and bullet.y + bullet.raio > inimigo.hitbox[
            1]:
            if bullet.x + bullet.raio > inimigo.hitbox[0] and bullet.x - bullet.raio < inimigo.hitbox[0] + \
                    inimigo.hitbox[2]:
                inimigo.hit()
                socobala.pop(socobala.index(bullet))

        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            socobala.pop(socobala.index(bullet))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if keys[pygame.K_LEFT]:
        Classe.playerVelocityX = -4
        Classe.x += Classe.playerVelocityX
        Classe.esquerda = True
        Classe.direita = False

    elif keys[pygame.K_RIGHT]:
        Classe.playerVelocityX = 4
        Classe.x += Classe.playerVelocityX
        Classe.direita = True
        Classe.esquerda = False

    elif keys[pygame.K_UP]:
        Classe.playerVelocityY = -4
        Classe.y += Classe.playerVelocityY
        Classe.baixo = False
        Classe.cima = True

    elif keys[pygame.K_DOWN]:
        Classe.playerVelocityY = 4
        Classe.y += Classe.playerVelocityY
        Classe.cima = False
        Classe.baixo = True


    elif keys[pygame.K_a]:
        SFX_Miss.play(0)
        if Classe.esquerda:
            mira = -1
        else:
            mira = 1
        if len(socobala) < 1:
            socobala.append(
                projetosoco(round(Classe.x + Classe.largura // 2), round(Classe.y + Classe.altura // 2), 6, (0, 0, 0),
                            mira))

        shootLoop = 1

        Classe.soco = True





    else:
        Classe.direita = False
        Classe.esquerda = False
        Classe.baixo = False
        Classe.cima = False
        Classe.soco = False
        Classe.parado = True
        Classe.playerVelocityY = 0
        Classe.playerVelocityX = 0
        Classe.ContarPassos = 0

        # Essa parte do código incrementa a posição do jogador com a variavel de velocidade, relativa a X e Y

        # Classe.x += Classe.playerVelocityX
        # Classe.y += Classe.playerVelocityY

    if Controlador_Jogo == 1:

        Tela_Inicial.Press_Start.play()
        if keys[K_RETURN]:
            Tela_Inicial.Tela_de_titulo_animacao.play()
        if Tela_Inicial.Tela_de_titulo_animacao.currentFrameNum == 9:
            Controlador_Jogo = 3
            start_ticks = pygame.time.get_ticks()
            pygame.mixer.music.stop()
            pygame.mixer.music.load('Musica_SFX\intro_akira.mp3')
            pygame.mixer.music.play()

    if Controlador_Jogo == 3:
        pygame.display.update()
        Janela.fill((0, 0, 0))

        if keys[K_RETURN]:
            Controlador_Jogo = 0
            start_ticks = pygame.time.get_ticks()
            pygame.mixer.music.stop()
            pygame.mixer.music.load('Musica_SFX\Musica_Fase.wav')
            pygame.mixer.music.play(-1)

        if textnumber == 1:
            Janela.blit(Cutscene1, (0, 0))
            if len(text) < len(text_orig):
                text += next(text_iterator)
                SFX_Text.play(0)

        ptext.draw(text, center=(Largura / 2, Altura / 2), fontname="fontes/start.ttf", color=(255, 255, 255),
                   gcolor=(150, 150, 150),
                   shadow=(3, 3), scolor="#000000")
        if len(text) == len(text_orig):
            Janela.fill((0, 0, 0))
            time.sleep(2)
            text += " "
            textnumber = 2
            Janela.fill((0, 0, 0))

        if textnumber == 2:
            Janela.blit(Cutscene2, (0, 0))
            if len(text2) < len(text_orig2):
                text2 += next(text_iterator2)
                SFX_Text.play(0)

        ptext.draw(text2, center=(Largura / 2, Altura / 2), fontname="fontes/start.ttf", color=(255, 255, 255),
                   gcolor=(150, 150, 150),
                   shadow=(3, 3), scolor="#000000")

        if len(text2) == len(text_orig2):
            Janela.fill((0, 0, 0))
            textnumber = 3
            time.sleep(2)
            text2 += " "
            Janela.fill((0, 0, 0))

        if textnumber == 3:
            Janela.blit(Cutscene3, (0, 0))
            if len(text3) < len(text_orig3):
                text3 += next(text_iterator3)
                SFX_Text.play(0)

        ptext.draw(text3, center=(Largura / 2, Altura / 2), fontname="fontes/start.ttf", color=(255, 255, 255),
                   gcolor=(150, 150, 150),
                   shadow=(3, 3), scolor="#000000")

        if len(text3) == len(text_orig3):
            Janela.fill((0, 0, 0))
            textnumber = 4
            time.sleep(3)
            text3 += " "
            Janela.fill((0, 0, 0))

        if textnumber == 4:
            Janela.blit(Cutscene2, (0, 0))
            if len(text4) < len(text_orig4):
                text4 += next(text_iterator4)
                SFX_Text.play(0)

        ptext.draw(text4, center=(Largura / 2, Altura / 2), fontname="fontes/start.ttf", color=(255, 255, 255),
                   gcolor=(150, 150, 150),
                   shadow=(3, 3), scolor="#000000")

        if len(text4) == len(text_orig4):
            Janela.fill((0, 0, 0))
            textnumber = 5
            time.sleep(2)
            text4 += " "
            Janela.fill((0, 0, 0))

        if textnumber == 5:
            Janela.blit(Cutscene1, (0, 0))
            if len(text5) < len(text_orig5):
                text5 += next(text_iterator5)
                SFX_Text.play(0)

        ptext.draw(text5, center=(Largura / 2, Altura / 2), fontname="fontes/start.ttf", color=(255, 255, 255),
                   gcolor=(150, 150, 150),
                   shadow=(3, 3), scolor="#000000")

        if len(text5) == len(text_orig5):
            Janela.fill((0, 0, 0))
            textnumber = 6
            time.sleep(2)
            text5 += " "
            Janela.fill((0, 0, 0))

        if textnumber == 6:
            Janela.blit(Cutscene1, (0, 0))
            if len(text6) < len(text_orig6):
                text6 += next(text_iterator6)
                SFX_Text.play(0)

        ptext.draw(text6, center=(Largura / 2, Altura / 2), fontname="fontes/start.ttf", color=(255, 255, 255),
                   gcolor=(150, 150, 150),
                   shadow=(3, 3), scolor="#000000")

        if len(text6) == len(text_orig6):
            Janela.fill((0, 0, 0))
            textnumber = 7
            time.sleep(3)
            text6 += " "
            Janela.fill((0, 0, 0))

        if textnumber == 7:
            Janela.blit(Cutscene2, (0, 0))
            if len(text7) < len(text_orig7):
                text7 += next(text_iterator7)
                SFX_Text.play(0)

        ptext.draw(text7, center=(Largura / 2, Altura / 2), fontname="fontes/start.ttf", color=(255, 255, 255),
                   gcolor=(150, 150, 150),
                   shadow=(3, 3), scolor="#000000")

        if len(text7) == len(text_orig7):
            Janela.fill((0, 0, 0))
            textnumber = 8
            time.sleep(2)
            text7 += " "
            Janela.fill((0, 0, 0))

        if textnumber == 8:
            Janela.blit(Cutscene3, (0, 0))
            if len(text8) < len(text_orig8):
                text8 += next(text_iterator8)
                SFX_Text.play(0)

        ptext.draw(text8, center=(Largura / 2, Altura / 2), fontname="fontes/start.ttf", color=(255, 255, 255),
                   gcolor=(150, 150, 150),
                   shadow=(3, 3), scolor="#000000")

        if len(text8) == len(text_orig8):
            Janela.fill((0, 0, 0))
            textnumber = 9
            time.sleep(2)
            text8 += " "
            Janela.fill((0, 0, 0))

        if textnumber == 9:
            Janela.blit(Cutscene2, (0, 0))
            if len(text9) < len(text_orig9):
                text9 += next(text_iterator9)
                SFX_Text.play(0)

        ptext.draw(text9, center=(Largura / 2, Altura / 2), fontname="fontes/start.ttf", color=(255, 255, 255),
                   gcolor=(150, 150, 150),
                   shadow=(3, 3), scolor="#000000")

        if len(text9) == len(text_orig9):
            Janela.fill((0, 0, 0))
            textnumber = 10
            time.sleep(2)
            text9 += " "
            Janela.fill((0, 0, 0))

        if textnumber == 10:
            Janela.blit(Cutscene1, (0, 0))
            if len(text10) < len(text_orig10):
                text10 += next(text_iterator10)
                SFX_Text.play(0)

        ptext.draw(text10, center=(Largura / 2, Altura / 2), fontname="fontes/start.ttf", color=(255, 255, 255),
                   gcolor=(150, 150, 150),
                   shadow=(3, 3), scolor="#000000")

        if len(text10) == len(text_orig10):
            Janela.fill((0, 0, 0))
            textnumber = 11
            time.sleep(2)
            text10 += " "
            Janela.fill((0, 0, 0))

        if textnumber == 11:
            Janela.blit(Cutscene2, (0, 0))
            if len(text11) < len(text_orig11):
                text11 += next(text_iterator11)
                SFX_Text.play(0)

        ptext.draw(text11, center=(Largura / 2, Altura / 2), fontname="fontes/start.ttf", color=(255, 255, 255),
                   gcolor=(150, 150, 150),
                   shadow=(3, 3), scolor="#000000")

        if len(text11) == len(text_orig11):
            Janela.fill((0, 0, 0))
            textnumber = 12
            time.sleep(5)
            text11 += " "
            Janela.fill((0, 0, 0))

        if textnumber == 12:
            Controlador_Jogo = 0
            start_ticks = pygame.time.get_ticks()
            pygame.mixer.music.stop()
            pygame.mixer.music.load('Musica_SFX\Musica_Fase.wav')
            pygame.mixer.music.play(-1)

        # Teste de Leaderboards com valores atualizados

    if keys[K_l]:
        Scoreboard_Player = {'Nome': Nome_do_player, 'Pontos': Score}
        Load_Top_Scores.insert(0, Scoreboard_Player)
        pickle.dump(Load_Top_Scores, open("top_scores", "wb"))
        Load_Top_Scores = pickle.load(open("top_scores", "rb"))
        Load_Top_Scores.sort(key=itemgetter('Pontos'), reverse=True)
        for key in Load_Top_Scores:
            print(key)

        # Teste para ver a barra de vida diminuindo
    if keys[K_b] and Classe.HP >= 0.9:
        Classe.HP -= 0.2
        Score += 1

    redrawGameWindow()
pygame.quit()