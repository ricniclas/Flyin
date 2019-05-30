import math, random, sys, time
import pygame
from pygame.locals import *
from operator import itemgetter
import pickle
import ptext
import Tela_Inicial

# Essa função define parametros da janela do windows que será aberta. Caso clique no X, ela irá fechar.
def events():
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()

#Carrega os Sprites que compoem o Personagem do Player 1
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
SocoVirado = [pygame.image.load('images\Personagem_Sprites\R_Personagem__Soco_0.png'),
        pygame.image.load('images\Personagem_Sprites\R_Personagem__Soco_1.png'),
        pygame.image.load('images\Personagem_Sprites\R_Personagem__Soco_3.png'),
        pygame.image.load('images\Personagem_Sprites\R_Personagem__Soco_4.png')
        ]
virado = [pygame.image.load('images\Personagem_Sprites\Personagem__Parado_R0.png'),
                 pygame.image.load('images\Personagem_Sprites\R_Personagem__Parado_1.png'),
                 pygame.image.load('images\Personagem_Sprites\R_Personagem__Parado_2.png'),
                 pygame.image.load('images\Personagem_Sprites\R_Personagem__Parado_3.png'),
                 pygame.image.load('images\Personagem_Sprites\R_Personagem__Parado_4.png'),
                 pygame.image.load('images\Personagem_Sprites\R_Personagem__Parado_5.png'),
                 ]
char = [pygame.image.load('images\Personagem_Sprites\Personagem__Parado_0.png'),
                 pygame.image.load('images\Personagem_Sprites\Personagem__Parado_1.png'),
                 pygame.image.load('images\Personagem_Sprites\Personagem__Parado_2.png'),
                 pygame.image.load('images\Personagem_Sprites\Personagem__Parado_3.png'),
                 pygame.image.load('images\Personagem_Sprites\Personagem__Parado_4.png'),
                 pygame.image.load('images\Personagem_Sprites\Personagem__Parado_5.png'),
                 ]

Dano = [pygame.image.load('images\Personagem_Sprites\R_Personagem__Dano_0.png'),
                 pygame.image.load('images\Personagem_Sprites\R_Personagem__Dano_1.png'),
                 pygame.image.load('images\Personagem_Sprites\R_Personagem__Dano_2.png'),
                 ]

DanoVirado = [pygame.image.load('images\Personagem_Sprites\L_Personagem__Dano_0.png'),
                 pygame.image.load('images\Personagem_Sprites\L_Personagem__Dano_1.png'),
                 pygame.image.load('images\Personagem_Sprites\L_Personagem__Dano_2.png'),
                 ]

#Carrega os Sprites que compoem o Personagem do Player 2
AndarDireita2 = [pygame.image.load('images\Personagem_Sprites\Personagem__Andando_1.png'),
                pygame.image.load('images\Personagem_Sprites\Personagem__Andando_2.png'),
                pygame.image.load('images\Personagem_Sprites\Personagem__Andando_3.png'),
                pygame.image.load('images\Personagem_Sprites\Personagem__Andando_4.png'),
                pygame.image.load('images\Personagem_Sprites\Personagem__Andando_5.png'),
                pygame.image.load('images\Personagem_Sprites\Personagem__Andando_6.png'),
                ]
AndarEsquerda2 = [pygame.image.load('images\Personagem_Sprites\R_Personagem__Andando_1.png'),
                 pygame.image.load('images\Personagem_Sprites\R_Personagem__Andando_2.png'),
                 pygame.image.load('images\Personagem_Sprites\R_Personagem__Andando_3.png'),
                 pygame.image.load('images\Personagem_Sprites\R_Personagem__Andando_4.png'),
                 pygame.image.load('images\Personagem_Sprites\R_Personagem__Andando_5.png'),
                 pygame.image.load('images\Personagem_Sprites\R_Personagem__Andando_6.png'),
                 ]
Soco2 = [pygame.image.load('images\Personagem_Sprites\Personagem__Soco_0.png'),
        pygame.image.load('images\Personagem_Sprites\Personagem__Soco_1.png'),
        pygame.image.load('images\Personagem_Sprites\Personagem__Soco_3.png'),
        pygame.image.load('images\Personagem_Sprites\Personagem__Soco_4.png')
        ]
SocoVirado2 =[pygame.image.load('images\Personagem_Sprites\R_Personagem__Soco_0.png'),
        pygame.image.load('images\Personagem_Sprites\R_Personagem__Soco_1.png'),
        pygame.image.load('images\Personagem_Sprites\R_Personagem__Soco_3.png'),
        pygame.image.load('images\Personagem_Sprites\R_Personagem__Soco_4.png')
        ]
virado2 = [pygame.image.load('images\Personagem_Sprites\Personagem__Parado_R0.png'),
                 pygame.image.load('images\Personagem_Sprites\R_Personagem__Parado_1.png'),
                 pygame.image.load('images\Personagem_Sprites\R_Personagem__Parado_2.png'),
                 pygame.image.load('images\Personagem_Sprites\R_Personagem__Parado_3.png'),
                 pygame.image.load('images\Personagem_Sprites\R_Personagem__Parado_4.png'),
                 pygame.image.load('images\Personagem_Sprites\R_Personagem__Parado_5.png'),
                 ]
char2 = [pygame.image.load('images\Personagem_Sprites\Personagem__Parado_0.png'),
                 pygame.image.load('images\Personagem_Sprites\Personagem__Parado_1.png'),
                 pygame.image.load('images\Personagem_Sprites\Personagem__Parado_2.png'),
                 pygame.image.load('images\Personagem_Sprites\Personagem__Parado_3.png'),
                 pygame.image.load('images\Personagem_Sprites\Personagem__Parado_4.png'),
                 pygame.image.load('images\Personagem_Sprites\Personagem__Parado_5.png'),
                 ]

parado = [pygame.image.load('images\inimiga snack beijin\D1.png'), pygame.image.load('images\inimiga snack beijin\D2.png')]

#Classe do Personagem do Player 1
class Player(object):
    def __init__(self, x, y, largura, altura, playerVelocityX, playerVelocityY, apertou1):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.playerVelocityX = playerVelocityX
        self.playerVelocityY = playerVelocityY
        self.esquerda = False
        self.apertou1=True
        self.direita = False
        self.baixo = False
        self.cima = False
        self.soco = False
        self.parado = False
        self.Virado=False
        self.cimaEs=False
        self.baixoEs=False
        self.socovirado=False
        self.estado = False
        self.ContarPassos = 0
        self.HP = 155
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)


    def draw(self, Janela):
        if self.ContarPassos + 1 >= 27:
            self.ContarPassos = 0

        if self.estado == True:
            if self.ContarPassos == 27:
                self.estado = False
                print("aqui")


        if self.esquerda:
            Janela.blit(AndarEsquerda[self.ContarPassos // 5], (self.x, self.y))
            self.ContarPassos += 3

        elif self.Virado:
            Janela.blit(virado[self.ContarPassos // 10], (self.x, self.y))
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

        elif self.cimaEs:
            Janela.blit(AndarDireita[self.ContarPassos // 5], (self.x, self.y))
            self.ContarPassos += 3

        elif self.baixoEs:
            Janela.blit(AndarDireita[self.ContarPassos // 5], (self.x, self.y))
            self.ContarPassos += 3

        elif self.soco:
            Janela.blit(Soco[self.ContarPassos // 7], (self.x, self.y))
            self.ContarPassos =7

        elif self.socovirado:
            Janela.blit(SocoVirado[self.ContarPassos // 7], (self.x, self.y))
            self.ContarPassos =7


        elif self.parado:
            Janela.blit(char[self.ContarPassos//10], (self.x, self.y))
            self.ContarPassos += 3


        elif self.estado == True:
            if self.apertou1==True:
                Janela.blit(Dano[self.ContarPassos // 9], (self.x, self.y))
                self.ContarPassos += 1
            elif self.apertou1 == False:
                Janela.blit(DanoVirado[self.ContarPassos // 9], (self.x, self.y))
                self.ContarPassos += 1
                print("socoesquerda")



        else:
            if self.direita:
                Janela.blit(AndarDireita[0], (self.x, self.y))
            else:
                Janela.blit(AndarDireita[0], (self.x, self.y))
        self.hitbox = (self.x + 17, self.y + 11, 70, 90)
        pygame.draw.rect(Janela, (255, 0, 0), self.hitbox, 2)

#Classe do Personagem do Player 2
class Player2(object):
    def __init__(self, x, y, largura, altura, playerVelocityX, playerVelocityY):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.playerVelocityX = playerVelocityX
        self.playerVelocityY = playerVelocityY
        self.esquerda = False
        self.direita = False
        self.baixo = False
        self.cima = False
        self.soco = False
        self.parado = False
        self.Virado=False
        self.socovirado=False
        self.apertou2 = True
        self.ContarPassos = 0
        self.HP = 155
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)

    def draw(self, Janela):
        if self.ContarPassos + 1 >= 27:
            self.ContarPassos = 0

        if self.esquerda:
            Janela.blit(AndarEsquerda2[self.ContarPassos // 5], (self.x, self.y))
            self.ContarPassos += 3

        elif self.Virado:
            Janela.blit(virado2[self.ContarPassos // 10], (self.x, self.y))
            self.ContarPassos += 3

        elif self.direita:
            Janela.blit(AndarDireita2[self.ContarPassos // 5], (self.x, self.y))
            self.ContarPassos += 3
        elif self.cima:
            Janela.blit(AndarDireita2[self.ContarPassos // 5], (self.x, self.y))
            self.ContarPassos += 3
        elif self.baixo:
            Janela.blit(AndarDireita2[self.ContarPassos // 5], (self.x, self.y))
            self.ContarPassos += 3

        elif self.soco:
            Janela.blit(Soco2[self.ContarPassos // 10], (self.x, self.y))
            self.ContarPassos += 3

        elif self.parado:
            Janela.blit(char2[self.ContarPassos//10], (self.x, self.y))
            self.ContarPassos += 3

        elif self.socovirado:
            Janela.blit(SocoVirado2[self.ContarPassos // 7], (self.x, self.y))
            self.ContarPassos =7




        else:
            if self.direita:
                Janela.blit(AndarDireita2[0], (self.x, self.y))
            else:
                Janela.blit(AndarDireita2[0], (self.x, self.y))
        self.hitbox = (self.x + 17, self.y + 11, 70, 90)
        pygame.draw.rect(Janela, (255, 0, 0), self.hitbox, 2)

#Classe do hitbox do Player 1
class projetosoco(object):
    def __init__(self, x, y, raio, cor, mira):
        self.x = x + 60
        self.y = y + 5
        self.raio = raio
        self.cor = cor
        self.mira = mira
        self.vel = 0 * mira
        self.tavenon=True

        if Classe.apertou1 == False:
            self.x = self.x + (-73)
            self.y = self.y + (-5)
            # print(self.x,y)

    def draw(self, Janela):
      if self.tavenon:
        pygame.draw.circle(Janela, self.cor, (self.x, self.y), self.raio)

#Classe do hitbox do Player 2
class projetosoco2(object):
    def __init__(self, x, y, raio, cor, mira):

        self.x = x + 60
        self.y = y + 5
        self.raio = raio
        self.cor = cor
        self.mira = mira
        self.vel = 0 * mira
        self.tavenon=True

        if Classe2.apertou2 == False:
            self.x = self.x + (-73)
            self.y = self.y + (-5)
            # print(self.x,y)

    def draw(self, Janela):
      if self.tavenon:
        pygame.draw.circle(Janela, self.cor, (self.x, self.y), self.raio)

class InimigoBase(object):
    Direta = [pygame.image.load('images\Inimigo\Inimigo_1\Inimigo_R__Andando_0.png'), pygame.image.load('images\Inimigo\Inimigo_1\Inimigo_R__Andando_1.png'),
              pygame.image.load('images\Inimigo\Inimigo_1\Inimigo_R__Andando_2.png'), pygame.image.load('images\Inimigo\Inimigo_1\Inimigo_R__Andando_3.png'),
              pygame.image.load('images\Inimigo\Inimigo_1\Inimigo_R__Andando_4.png'), pygame.image.load('images\Inimigo\Inimigo_1\Inimigo_R__Andando_5.png'),
              pygame.image.load('images\Inimigo\Inimigo_1\Inimigo_R__Andando_6.png')]
    Esquerda = [pygame.image.load('images\Inimigo\Inimigo_1\Inimigo_L__Andando_0.png'), pygame.image.load('images\Inimigo\Inimigo_1\Inimigo_L__Andando_1.png'),
                pygame.image.load('images\Inimigo\Inimigo_1\Inimigo_L__Andando_2.png'), pygame.image.load('images\Inimigo\Inimigo_1\Inimigo_L__Andando_3.png'),
                pygame.image.load('images\Inimigo\Inimigo_1\Inimigo_L__Andando_4.png'), pygame.image.load('images\Inimigo\Inimigo_1\Inimigo_L__Andando_5.png'),
                pygame.image.load('images\Inimigo\Inimigo_1\Inimigo_L__Andando_6.png')]

    parado = [pygame.image.load('images\inimiga snack beijin\D1.png'), pygame.image.load('images\inimiga snack beijin\D2.png')]

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
        self.aleatorio = random.randint ( 0 , 3 )
        self.estado = 0
        self.pare= False

    def draw(self, win):
        self.move()


        if self.visible:
            if self.walkCount + 1 >= 2:
                self.walkCount = 0
            elif self.parado and self.vel==0:
                win.blit ( parado[self.walkCount], (self.x , self.y) )
                self.walkCount += 1

            elif self.vel > 0:
                win.blit(self.Direta[self.walkCount], (self.x, self.y))
                self.walkCount += 1
            else:
                win.blit(self.Esquerda[self.walkCount], (self.x, self.y))
                self.walkCount += 1

            pygame.draw.rect(win, (255, 0, 0), (self.hitbox[0], self.hitbox[1] - 20, 50, 10))
            pygame.draw.rect(win, (0, 128, 0),
                             (self.hitbox[0], self.hitbox[1] - 20, 50 - (5 * (10 - self.health)), 10))
            self.hitbox = (self.x + 17, self.y + 2, 31, 57)
            #pygame.draw.rect(win, (255,0,0), self.hitbox,2)

    def move(self):
        if self.estado == 1:
            self.vel = 0

        if self.walkCount == 30:
                self.estado = 0
                self.vel = 3

        if self.estado == 0:
            if self.x + self.vel < self.path[1] :
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0

        else:
            if self.x - self.vel > self.path[0] :
                self.x += self.vel
            else:
                self.vel = self.vel * -1
                self.walkCount = 0

        if self.x > Classe.x and Classe.x>=400:
                self.x -= self.vel
        elif self.x < Classe.x:
                self.x += self.vel
        if self.y < Classe.y:
                self.y += self.vel
        elif self.y > Classe.y:
                self.y -= self.vel
        #print(self.x)

    '''''''''''''''def Penis(self):
     if self.x - self.vel > self.path[0]:
        if self.aleatorio == 0:=
            self.x += 0.1
        elif self.aleatorio == 1:
            self.y += 0.1
        elif self.aleatorio == 2:
            self.y -= 0.1
        elif self.aleatorio == 3:
            self.x -= 0.1
        else:
            self.walkCount = 0'''''''''''''''

    def hit(self):
        self.walkCount=0
        SFX_Punch1.play()
        if self.health > 0:
            self.health -= 1
            self.estado = 1
            self.vel = 3
            self.pare=False
        else:
            self.visible = False
        print('miseravi', self.estado)

# Criação dos objetos (Personagens e NPCS) com seus atributos:
#Personagem possui x, y, largura, altura, playerVelocityX, playerVelocityY
# Inimigo possui x, y, width, height, end
Classe = Player(200, 410, 64, 64, 64, 64, 64)
Classe2 = Player2(200, 410, 64, 64, 64, 64)
inimigo = InimigoBase(100, 410, 64, 64, 450)
inimigo2 = InimigoBase(100, 410, 64, 64, 450)

#Criação dos objetos de hitbox do soco dos Personagens
soco=projetosoco(200, 410, 64, 64, 64)
soco2=projetosoco2(200, 410, 64, 64, 64)
loop = 0
socobala = []
socobala2 = []

# Propriedades da Janela a ser aberta
Largura, Altura = 640, 448
HW, HH = Largura / 2, Altura / 2
Area = Largura * Altura
Nome_da_Janela = "FLYING FIST"

# Esse código inicializa a Janela com as propriedades definidas nas variaveis
pygame.init()
clock = pygame.time.Clock()
Janela = pygame.display.set_mode((Largura, Altura))
pygame.display.set_caption(Nome_da_Janela)

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



def mostrarPlacar(Pontos):
    D = ""
    for key in Pontos:
        # print(key)
        C = "Nome : "
        A = (key['Nome'])
        B = (key['Pontos'])
        # C = ("Nome: ",A, "Pontos: ",B)
        # print(A)
        # print(B)
        C += A
        C += " Pontos: "
        C += str(B)
        D += C
        D += "\n"

    print(D)
    return D

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

# mainloop
run = True

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
SFX_Punch1.set_volume(0.5)
SFX_Punch2 = pygame.mixer.Sound('Musica_SFX\SFX\Punch_2.wav')
SFX_Miss = pygame.mixer.Sound('Musica_SFX\SFX\Punch_miss.wav')
SFX_Miss.set_volume(0.3)
SFX_Death = pygame.mixer.Sound('Musica_SFX\SFX\Death.wav')
SFX_Text = pygame.mixer.Sound('Musica_SFX\SFX\Death.wav')
SFX_Text.set_volume(0.05)

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
        Classe2.draw(Janela)
        inimigo2.draw(Janela)
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

        for balau2 in socobala2:
            balau2.draw(Janela)

        if keys[pygame.K_y]:
            print(textoPlacar)
            ptext.draw(str(textoPlacar), center=(Largura / 2, Altura / 2), fontname="fontes/start.ttf",
                       color=(255, 255, 255),
                       gcolor=(150, 150, 150),
                       shadow=(3, 3), scolor="#000000")

        pygame.display.update()


while run:

    apertou2=0
    keys = pygame.key.get_pressed()

    # Essa parte do código é referente ao SideScrolling e posição do personagem na tela. Para entender, ver https://www.youtube.com/watch?v=AX8YU2hLBUg&t=478s

    if Classe.x and Classe2.x > Fase_Largura:
        Classe.x = Fase_Largura
        Classe2.x = Fase_Largura
    if Classe.x and Classe2.x < circleRadius:
        Classe.x = circleRadius
        Classe2.x = circleRadius
    if Classe.x and Classe2.x  < startScrollingPosX:
        Classe.x = Classe.x
        Classe2.x = Classe2.x
    elif Classe.x and Classe2.x > Fase_Largura - startScrollingPosX:
        Classe.x = Classe.x - Fase_Largura + Largura
        Classe2.x = Classe2.x - Fase_Largura + Largura
    else:
        Classe.x = startScrollingPosX
        Background_Fase_Posicao += -Classe.playerVelocityX
        Classe2.x = startScrollingPosX
        Background_Fase_Posicao += -Classe2.playerVelocityX

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

#Testa a colisão do soco do Player 1
    for bullet in socobala:
        if  inimigo.hitbox[1] + inimigo.hitbox[3] and inimigo.hitbox[
            1]:
            if bullet.x + bullet.raio > inimigo.hitbox[0] and bullet.x - bullet.raio < inimigo.hitbox[0] + \
                    inimigo.hitbox[2]:
                inimigo.hit()
                socobala.pop(socobala.index(bullet))
            else:
             socobala.pop(socobala.index(bullet))

# Testa a colisão do soco do Player 2
    for bullet in socobala2:
        if  inimigo.hitbox[1] + inimigo.hitbox[3] and inimigo.hitbox[
            1]:
            if bullet.x + bullet.raio > inimigo.hitbox[0] and bullet.x - bullet.raio < inimigo.hitbox[0] + \
                    inimigo.hitbox[2]:
                inimigo.hit()
                socobala2.pop(socobala2.index(bullet))
            else:
             socobala2.pop(socobala2.index(bullet))

#Tirar esse primeiro
    print(Classe.estado, Classe.ContarPassos, Classe.apertou1)

    if keys[pygame.K_r]:
        textoPlacar = mostrarPlacar(Load_Top_Scores)
        time.sleep(1)


    if keys [pygame.K_t]:
        ptext.draw(textoPlacar, center=(Largura / 2, Altura / 2), fontname="fontes/start.ttf", color=(255, 255, 255),
                   gcolor=(150, 150, 150),
                   shadow=(3, 3), scolor="#000000")


    if keys[pygame.K_LEFT]:
        if Classe.estado == False:
            Classe.playerVelocityX=0
            Classe.esquerda = True
            Classe.direita = False
            Classe.Virado=True
            Classe.apertou1 = True

    if keys[pygame.K_LEFT]  :
        if Classe.estado == False:
            Classe.playerVelocityX = -4
            Classe.x += Classe.playerVelocityX
            Classe.esquerda = True
            Classe.direita = False
            Classe.Virado=False
            Classe.apertou1 = False
            #print(Classe.apertou1)

    elif keys[pygame.K_RIGHT]:
        if Classe.estado == False:
            Classe.playerVelocityX = 4
            Classe.x += Classe.playerVelocityX
            Classe.direita = True
            Classe.esquerda = False
            Classe.Virado=False
            Classe.apertou1 = True
            print(Classe.apertou1)

    elif keys[pygame.K_UP]:
        if Classe.estado == False:
            Classe.playerVelocityY = -4
            Classe.y += Classe.playerVelocityY
            Classe.baixo = False
            Classe.cima = True

    elif keys[pygame.K_DOWN]:
        if Classe.estado == False:
            Classe.playerVelocityY = 4
            Classe.y += Classe.playerVelocityY
            Classe.cima = False
            Classe.baixo = True

    elif keys[pygame.K_f]:
        if Classe.estado == False:
            Classe.Virado=False
            Classe.direita = False
            Classe.esquerda = False
            Classe.baixo = False
            Classe.cima = False
            Classe.soco = False
            Classe.socovirado = False
            Classe.parado = False
            Classe.estado = True
            Classe.ContarPassos = 0
            Classe.estado = True




    elif keys[pygame.K_m]:
        if Classe.estado == False:
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
            if Classe.apertou1==True:
                Classe.soco = True
            if Classe.apertou1 == False:
                Classe.socovirado = True
                Classe.Virado=False
            else:
                Classe.socovirado=False
                print(Classe2.socovirado)
            print("PORRADA !! *20:", Classe.socovirado)

    else:
        Classe.direita = False
        Classe.esquerda = False
        Classe.baixo = False
        Classe.cima = False
        Classe.soco = False
        Classe.socovirado=False
        Classe.parado=False
        Classe.estado = False
        Classe.playerVelocityY = 0
        Classe.playerVelocityX = 0
        #print ( "Vira ? !! *20:" , Classe.Virado )

        if Classe.playerVelocityX == 0 :
           Classe.parado = True
        if Classe.apertou1==False:
            if Classe.estado == False:
                Classe.Virado=True
        # Essa parte do código incrementa a posição do jogador com a variavel de velocidade, relativa a X e Y
        # Classe.x += Classe.playerVelocityX
        # Classe.y += Classe.playerVelocityY

#Player2
    if keys[pygame.K_a]:
        Classe2.playerVelocityX = 0
        Classe2.esquerda = True
        Classe2.direita = False
        Classe2.Virado = True
        Classe2.apertou2 = True

    if keys[pygame.K_a]:
        Classe2.playerVelocityX = -4
        Classe2.x += Classe2.playerVelocityX
        Classe2.esquerda = True
        Classe2.direita = False
        Classe2.Virado = False
        Classe2.apertou2 = False

    elif keys[pygame.K_d]:
        Classe2.playerVelocityX = 4
        Classe2.x += Classe2.playerVelocityX
        Classe2.direita = True
        Classe2.esquerda = False
        Classe2.Virado = False
        Classe2.apertou2 = True

    elif keys[pygame.K_w]:
        Classe2.playerVelocityY = -4
        Classe2.y += Classe2.playerVelocityY
        Classe2.baixo = False
        Classe2.cima = True

    elif keys[pygame.K_s]:
        Classe2.playerVelocityY = 4
        Classe2.y += Classe2.playerVelocityY
        Classe2.cima = False
        Classe2.baixo = True

    elif keys[pygame.K_i]:
        SFX_Miss.play ( 0 )
        if Classe2.esquerda:
            mira2 = -1
        else:
            mira2 = 1
        if len ( socobala2 ) < 1:
            socobala2.append (
                projetosoco2 ( round ( Classe2.x + Classe2.largura // 2 ) , round ( Classe2.y + Classe2.altura // 2 ) , 6 ,
                              (0 , 0 , 0) ,
                              mira2 ) )
        shootLoop2 = 1

        if Classe2.apertou2 == True:
            Classe2.soco = True
        if Classe2.apertou2 == False:
            Classe2.socovirado = True
            Classe2.Virado = False
            Classe2.parado=False
        else:
            Classe2.socovirado = False

    else:
        Classe2.direita = False
        Classe2.esquerda = False
        Classe2.baixo = False
        Classe2.cima = False
        Classe2.soco = False
        Classe2.socovirado = False
        Classe2.parado = False
        Classe2.playerVelocityY = 0
        Classe2.playerVelocityX = 0

        if Classe2.playerVelocityX == 0:
            Classe2.parado = True
        if Classe2.apertou2 == False:
            Classe2.Virado = True

# Controlador_Jogo é igual a 1, você está na tela de título
    if Controlador_Jogo == 1:

        Tela_Inicial.Press_Start.play()
        if keys[K_RETURN]:
            Tela_Inicial.Tela_de_titulo_animacao.play()

        #Esse comando reseta o scoreboard
        if keys[K_s]:
            pickle.dump(Leaderboard, open("top_scores", "wb"))

        if keys[K_d]:
            Load_Top_Scores = pickle.load(open("top_scores", "rb"))
            Load_Top_Scores.sort(key=itemgetter('Pontos'), reverse=True)
            mostrarPlacar(Load_Top_Scores)


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

#Carrega o scoreboard
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