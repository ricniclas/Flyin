import math, random, sys, time
import pygame
from pygame.locals import *
from operator import itemgetter
import os
import pickle
import ptext
import Tela_Inicial
import compressao_save
import Cutscenes

LetraA = 0
LetraB = 0
LetraC = 0
LetraAtual = 0
Auxiliar = 0

# Essa função define parametros da janela do windows que será aberta. Caso clique no X, ela irá fechar.
def events():
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()

#Classe do Personagem do Player 1
class Player(object):
    # Carrega os Sprites que compoem o Personagem do Player 1
    AndarDireita = [pygame.image.load('images/Personagem_Sprites/Personagem__Andando_1.png'),
                    pygame.image.load('images/Personagem_Sprites/Personagem__Andando_2.png'),
                    pygame.image.load('images/Personagem_Sprites/Personagem__Andando_3.png'),
                    pygame.image.load('images/Personagem_Sprites/Personagem__Andando_4.png'),
                    pygame.image.load('images/Personagem_Sprites/Personagem__Andando_5.png'),
                    pygame.image.load('images/Personagem_Sprites/Personagem__Andando_6.png'),
                    ]
    AndarEsquerda = [pygame.image.load('images/Personagem_Sprites/R_Personagem__Andando_1.png'),
                     pygame.image.load('images/Personagem_Sprites/R_Personagem__Andando_2.png'),
                     pygame.image.load('images/Personagem_Sprites/R_Personagem__Andando_3.png'),
                     pygame.image.load('images/Personagem_Sprites/R_Personagem__Andando_4.png'),
                     pygame.image.load('images/Personagem_Sprites/R_Personagem__Andando_5.png'),
                     pygame.image.load('images/Personagem_Sprites/R_Personagem__Andando_6.png'),
                     ]
    Soco = [pygame.image.load('images/Personagem_Sprites/Personagem__Soco_2.png'),
            pygame.image.load('images/Personagem_Sprites/Personagem__Soco_1.png'),
            pygame.image.load('images/Personagem_Sprites/Personagem__Soco_0.png'),
            pygame.image.load('images/Personagem_Sprites/Personagem__Soco_4.png')
            ]
    SocoVirado = [pygame.image.load('images/Personagem_Sprites/R_Personagem__Soco_2.png'),
                  pygame.image.load('images/Personagem_Sprites/R_Personagem__Soco_1.png'),
                  pygame.image.load('images/Personagem_Sprites/R_Personagem__Soco_0.png'),
                  pygame.image.load('images/Personagem_Sprites/R_Personagem__Soco_4.png')
                  ]
    virado = [pygame.image.load('images/Personagem_Sprites/Personagem__Parado_R0.png'),
              pygame.image.load('images/Personagem_Sprites/R_Personagem__Parado_1.png'),
              pygame.image.load('images/Personagem_Sprites/R_Personagem__Parado_2.png'),
              pygame.image.load('images/Personagem_Sprites/R_Personagem__Parado_3.png'),
              pygame.image.load('images/Personagem_Sprites/R_Personagem__Parado_4.png'),
              pygame.image.load('images/Personagem_Sprites/R_Personagem__Parado_5.png'),
              ]
    char = [pygame.image.load('images/Personagem_Sprites/Personagem__Parado_0.png'),
            pygame.image.load('images/Personagem_Sprites/Personagem__Parado_1.png'),
            pygame.image.load('images/Personagem_Sprites/Personagem__Parado_2.png'),
            pygame.image.load('images/Personagem_Sprites/Personagem__Parado_3.png'),
            pygame.image.load('images/Personagem_Sprites/Personagem__Parado_4.png'),
            pygame.image.load('images/Personagem_Sprites/Personagem__Parado_5.png'),
            ]

    Dano = [pygame.image.load('images/Personagem_Sprites/R_Personagem__Dano_0.png'),
            pygame.image.load('images/Personagem_Sprites/R_Personagem__Dano_1.png'),
            pygame.image.load('images/Personagem_Sprites/R_Personagem__Dano_2.png'),
            ]

    DanoVirado = [pygame.image.load('images/Personagem_Sprites/L_Personagem__Dano_0.png'),
                  pygame.image.load('images/Personagem_Sprites/L_Personagem__Dano_1.png'),
                  pygame.image.load('images/Personagem_Sprites/L_Personagem__Dano_2.png'),
                  ]

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
        self.andarcount = 0
        self.parado = False
        self.Virado=False
        self.cimaEs=False
        self.baixoEs=False
        self.socovirado=False
        self.estado = False
        self.socoestado = False
        self.parartela = False
        self.ContarPassos = 0
        self.HP = 155
        self.Score = 0
        self.Nome_Player = "AAA"
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)

    def danoPlayer(self):
        if Classe.estado == False:
            SFX_Punch1.play()
            Classe.estado = True
            Classe.ContarPassos = 0
            Classe.Virado = False
            Classe.direita = False
            Classe.esquerda = False
            Classe.baixo = False
            Classe.cima = False
            Classe.soco = False
            Classe.socovirado = False
            Classe.parado = False
            Classe.HP -= 10



    def draw(self, Janela):

        if self.ContarPassos + 1 >= 27:
            self.ContarPassos = 0
            self.estado = False
            self.socoestado = False




        if self.esquerda:
            Janela.blit(self.AndarEsquerda[self.ContarPassos // 5], (self.x, self.y))
            self.ContarPassos += 3

        elif self.Virado:
            Janela.blit(self.virado[self.ContarPassos // 10], (self.x, self.y))
            self.ContarPassos += 3

        elif self.direita:
            Janela.blit(self.AndarDireita[self.ContarPassos // 5], (self.x, self.y))
            self.ContarPassos += 3
            self.andarcount += 1
        elif self.cima:
            Janela.blit(self.AndarDireita[self.ContarPassos // 5], (self.x, self.y))
            self.ContarPassos += 3
        elif self.baixo:
            Janela.blit(self.AndarDireita[self.ContarPassos // 5], (self.x, self.y))
            self.ContarPassos += 3

        elif self.cimaEs:
            Janela.blit(self.AndarDireita[self.ContarPassos // 5], (self.x, self.y))
            self.ContarPassos += 3

        elif self.baixoEs:
            Janela.blit(self.AndarDireita[self.ContarPassos // 5], (self.x, self.y))
            self.ContarPassos += 3

        elif self.soco:
            Janela.blit(self.Soco[self.ContarPassos // 7], (self.x, self.y))
            self.ContarPassos += 3


        elif self.socovirado:
            Janela.blit(self.SocoVirado[self.ContarPassos // 7], (self.x, self.y))
            self.ContarPassos += 3


        elif self.parado:
            Janela.blit(self.char[self.ContarPassos//10], (self.x, self.y))
            self.ContarPassos += 2


        elif self.estado == True:
            if self.apertou1==True:
                Janela.blit(self.Dano[self.ContarPassos // 9], (self.x, self.y))
                self.ContarPassos += 1
            elif self.apertou1 == False:
                Janela.blit(self.DanoVirado[self.ContarPassos // 9], (self.x, self.y))
                self.ContarPassos += 1
                print("socoesquerda")


        else:
            if self.direita:
                Janela.blit(self.AndarDireita[0], (self.x, self.y))
            else:
                Janela.blit(self.AndarDireita[0], (self.x, self.y))
        self.hitbox = (self.x + 17, self.y + 11, 70, 90)
        #pygame.draw.rect(Janela, (255, 0, 0), self.hitbox, 2)

#Classe do Personagem do Player 2
class Player2(object):

    # Carrega os Sprites que compoem o Personagem do Player 2
    AndarDireita2 = [pygame.image.load('images/Personagem2_Sprites/Personagem2_R__Andando_0.png'),
                     pygame.image.load('images/Personagem2_Sprites/Personagem2_R__Andando_1.png'),
                     pygame.image.load('images/Personagem2_Sprites/Personagem2_R__Andando_1.png'),
                     pygame.image.load('images/Personagem2_Sprites/Personagem2_R__Andando_2.png'),
                     pygame.image.load('images/Personagem2_Sprites/Personagem2_R__Andando_3.png'),
                     pygame.image.load('images/Personagem2_Sprites/Personagem2_R__Andando_4.png'),
                     pygame.image.load('images/Personagem2_Sprites/Personagem2_R__Andando_5.png'),
                     pygame.image.load('images/Personagem2_Sprites/Personagem2_R__Andando_6.png')]
    AndarEsquerda2 = [pygame.image.load('images/Personagem2_Sprites/Personagem2_L__Andando_0.png'),
                      pygame.image.load('images/Personagem2_Sprites/Personagem2_L__Andando_1.png'),
                      pygame.image.load('images/Personagem2_Sprites/Personagem2_L__Andando_2.png'),
                      pygame.image.load('images/Personagem2_Sprites/Personagem2_L__Andando_3.png'),
                      pygame.image.load('images/Personagem2_Sprites/Personagem2_L__Andando_4.png'),
                      pygame.image.load('images/Personagem2_Sprites/Personagem2_L__Andando_5.png'),
                      pygame.image.load('images/Personagem2_Sprites/Personagem2_L__Andando_6.png')]
    Soco2 = [pygame.image.load('images/Personagem2_Sprites/Personagem2_R__Soco_0.png'),
             pygame.image.load('images/Personagem2_Sprites/Personagem2_R__Soco_1.png'),
             pygame.image.load('images/Personagem2_Sprites/Personagem2_R__Soco_2.png'),
             pygame.image.load('images/Personagem2_Sprites/Personagem2_R__Soco_3.png'),
             pygame.image.load('images/Personagem2_Sprites/Personagem2_R__Soco_4.png')
             ]
    SocoVirado2 = [pygame.image.load('images/Personagem2_Sprites/Personagem2_L__Soco_0.png'),
                   pygame.image.load('images/Personagem2_Sprites/Personagem2_L__Soco_1.png'),
                   pygame.image.load('images/Personagem2_Sprites/Personagem2_L__Soco_2.png'),
                   pygame.image.load('images/Personagem2_Sprites/Personagem2_L__Soco_3.png'),
                   pygame.image.load('images/Personagem2_Sprites/Personagem2_L__Soco_4.png')
                   ]
    virado2 = [pygame.image.load('images/Personagem2_Sprites/Personagem2_L__Parado_0.png'),
               pygame.image.load('images/Personagem2_Sprites/Personagem2_L__Parado_1.png'),
               pygame.image.load('images/Personagem2_Sprites/Personagem2_L__Parado_2.png'),
               pygame.image.load('images/Personagem2_Sprites/Personagem2_L__Parado_3.png'),
               pygame.image.load('images/Personagem2_Sprites/Personagem2_L__Parado_4.png'),
               pygame.image.load('images/Personagem2_Sprites/Personagem2_L__Parado_5.png'),
               ]
    char2 = [pygame.image.load('images/Personagem2_Sprites/Personagem2_R__Parado_0.png'),
             pygame.image.load('images/Personagem2_Sprites/Personagem2_R__Parado_1.png'),
             pygame.image.load('images/Personagem2_Sprites/Personagem2_R__Parado_2.png'),
             pygame.image.load('images/Personagem2_Sprites/Personagem2_R__Parado_3.png'),
             pygame.image.load('images/Personagem2_Sprites/Personagem2_R__Parado_4.png'),
             pygame.image.load('images/Personagem2_Sprites/Personagem2_R__Parado_5.png'),
             ]

    Dano2 = [pygame.image.load('images/Personagem2_Sprites/Personagem2_R__Dano_0.png'),
             pygame.image.load('images/Personagem2_Sprites/Personagem2_R__Dano_1.png'),
             pygame.image.load('images/Personagem2_Sprites/Personagem2_R__Dano_2.png'),
             ]

    DanoVirado2 = [pygame.image.load('images/Personagem2_Sprites/Personagem2_L__Dano_0.png'),
                   pygame.image.load('images/Personagem2_Sprites/Personagem2_L__Dano_1.png'),
                   pygame.image.load('images/Personagem2_Sprites/Personagem2_L__Dano_2.png'),
                   ]

    parado = [pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_L__Dano_1.png'),
              pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_L__Dano_2.png'),
              pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_L__Dano_3.png'),
              pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_L__Dano_3.png'),
              pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_L__Dano_4.png')]

    def __init__(self, x, y, largura, altura, playerVelocityX, playerVelocityY):
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
        self.socoestado = False
        self.ContarPassos = 0
        self.andarcount = 0
        self.HP = 155
        self.Score = 0
        self.Nome_Player = "PL2"
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)


    def danoPlayer2(self):
        if Classe2.estado == False:
            SFX_Punch1.play()
            Classe2.estado = True
            Classe2.ContarPassos = 0
            Classe2.Virado = False
            Classe2.direita = False
            Classe2.esquerda = False
            Classe2.baixo = False
            Classe2.cima = False
            Classe2.soco = False
            Classe2.socovirado = False
            Classe2.parado = False
            Classe2.HP -= 10

    def draw(self, Janela):



        if self.ContarPassos + 1 >= 27:
            self.ContarPassos = 0
            self.estado = False
            self.socoestado = False

        if self.esquerda:
            Janela.blit(self.AndarEsquerda2[self.ContarPassos // 5], (self.x, self.y))
            self.ContarPassos += 3

        elif self.Virado:
            Janela.blit(self.virado2[self.ContarPassos // 10], (self.x, self.y))
            self.ContarPassos += 3

        elif self.direita:
            Janela.blit(self.AndarDireita2[self.ContarPassos // 5], (self.x, self.y))
            self.ContarPassos += 3
            self.andarcount += 1
        elif self.cima:
            Janela.blit(self.AndarDireita2[self.ContarPassos // 5], (self.x, self.y))
            self.ContarPassos += 3
        elif self.baixo:
            Janela.blit(self.AndarDireita2[self.ContarPassos // 5], (self.x, self.y))
            self.ContarPassos += 3

        elif self.cimaEs:
            Janela.blit(self.AndarDireita2[self.ContarPassos // 5], (self.x, self.y))
            self.ContarPassos += 3

        elif self.baixoEs:
            Janela.blit(self.AndarDireita2[self.ContarPassos // 5], (self.x, self.y))
            self.ContarPassos += 3

        elif self.soco:
            Janela.blit(self.Soco2[self.ContarPassos // 7], (self.x, self.y))
            self.ContarPassos += 3


        elif self.socovirado:
            Janela.blit(self.SocoVirado2[self.ContarPassos // 7], (self.x, self.y))
            self.ContarPassos += 3


        elif self.parado:
            Janela.blit(self.char2[self.ContarPassos//10], (self.x, self.y))
            self.ContarPassos += 3


        elif self.estado == True:
            if self.apertou1==True:
                Janela.blit(self.Dano2[self.ContarPassos // 9], (self.x, self.y))
                self.ContarPassos += 1
            elif self.apertou1 == False:
                Janela.blit(self.DanoVirado2[self.ContarPassos // 9], (self.x, self.y))
                self.ContarPassos += 1
                print("socoesquerda")


        else:
            if self.direita:
                Janela.blit(self.AndarDireita2[0], (self.x, self.y))
            else:
                Janela.blit(self.AndarDireita2[0], (self.x, self.y))
        self.hitbox = (self.x + 17, self.y + 11, 70, 90)
        #pygame.draw.rect(Janela, (255, 0, 0), self.hitbox, 2)

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
        #pygame.draw.circle(Janela, self.cor, (self.x, self.y), self.raio)
        pass
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

        if Classe2.apertou1 == False:
            self.x = self.x + (-73)
            self.y = self.y + (-5)
            # print(self.x,y)

    def draw(self, Janela):
      if self.tavenon:
        #pygame.draw.circle(Janela, self.cor, (self.x, self.y), self.raio)
        pass













class InimigoDano(object):
    def __init__(self, x, y, raio, cor, mira):

        self.x = x
        self.y = y
        self.raio = raio
        self.cor = cor
        self.mira = mira
        self.vel = 0 * mira
        self.tavenon=True



    def draw(self, Janela):
      if self.tavenon:
        pygame.draw.circle(Janela, self.cor, (self.x, self.y), self.raio)












class InimigoBase(object):
    Direta = [pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_R__Andando_0.png'), pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_R__Andando_1.png'),
              pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_R__Andando_2.png'), pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_R__Andando_3.png'),
              pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_R__Andando_4.png'), pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_R__Andando_5.png'),
              pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_R__Andando_6.png')]
    Esquerda = [pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_L__Andando_0.png'), pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_L__Andando_1.png'),
                pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_L__Andando_2.png'), pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_L__Andando_3.png'),
                pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_L__Andando_4.png'), pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_L__Andando_5.png'),
                pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_L__Andando_6.png')]

    Ataque =  [pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_R__Atacando_0.png'), pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_R__Atacando_1.png'),
                pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_R__Atacando_2.png'), pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_R__Atacando_3.png'),
                pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_R__Atacando_4.png'), pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_R__Atacando_5.png'),
                pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_R__Atacando_6.png'),pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_R__Atacando_7.png'), pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_R__Atacando_8.png'),
                pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_R__Atacando_9.png')]

    parado = [pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_L__Dano_0.png'), pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_L__Dano_1.png'),
              pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_L__Dano_2.png'), pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_L__Dano_3.png'), pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_L__Dano_4.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkCount = 0
        self.vel = 3
        self.hitbox = (self.x + 17, self.y + 2)
        self.hitbox2 = (self.hitbox[0], self.y + 57)
        self.health = 10
        self.visible = True
        self.aleatorio = random.randint ( 0 , 3 )
        self.estado = 0
        self.pare= False
        self.atacando=False
        self.esquerda=False
        self.direita=False
        self.stop=False

    def draw(self , win):
     if Classe.andarcount >=200 or Classe2.andarcount >=200:
        Classe.parartela=True
        #print(Classe.parartela)
        self.move ()
        if self.visible:
            if self.walkCount + 1 >= 33:
                self.walkCount = 0
            elif self.stop and self.vel == 0:

                win.blit (self.parado[self.walkCount // 6] , (self.x , self.y) )

                self.walkCount += 3

            elif self.vel > 0:
                win.blit ( self.Direta[self.walkCount // 9] , (self.x , self.y) )
                self.walkCount += 1


            elif self.atacando and self.vel==0 :

                win.blit (self.Ataque[self.walkCount // 9] , (self.x , self.y) )

                self.walkCount += 3



            else:
                win.blit ( self.Esquerda[self.walkCount // 9] , (self.x , self.y) )
                self.walkCount += 1

            pygame.draw.rect ( win , (255 , 0 , 0) , (self.hitbox[0] , self.hitbox[1] - 20 , 50 , 10) )
            pygame.draw.rect ( win , (0 , 128 , 0) , (self.hitbox[0] , self.hitbox[1] - 20 , 50 - (5 * (10 - self.health)) , 10) )
            self.hitbox = (self.x + 17 , self.y + 2 , 31 , 57)

            # pygame.draw.rect(win, (255,0,0), self.hitbox,2)
     if inimigo.visible==False:
         Classe.parartela = False
         # print(Classe.parartela)
         Classe.andarcount = 0
         Classe2.andarcount = 0

    def move(self):
        if self.estado == 1:
            self.vel = 0

        if self.estado == 2:
            self.vel = 0


        if self.walkCount == 30:
                self.estado = 0
                self.vel = 3

        if self.estado == 0 and self.atacando == False:
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





        if self.x==Classe.x:
            self.atacando=True
            inimigo.atacar()
            self.stop=False
            self.vel=0
        else:
            self.atacando=False

            print ( "Oh CARALHIO " , self.vel, self.atacando )












    def atacar(self):

        if self.atacando==True:
            mira3 = -1
        else:
            mira3 = 1
        if len ( luis ) < 1:
            luis.append (
                InimigoDano ( round ( inimigo.x + inimigo.width // 2 ) , round ( inimigo.y + inimigo.height // 2 ) , 6 ,
                              (0 , 0 , 0) ,
                              mira3 ) )





        else:
            self.atacando=False

            print("Oh CARALHIO ",self.vel)



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

    def hit(self, personagem_hit):
        global showPoints
        global Score
        self.walkCount = 0
        SFX_Punch1.play()
        if self.health > 0 :
            self.health -= 1
            self.estado = 1
            self.vel = 3
            self.stop=True
            self.pare = False
        else:
            self.visible = False
            showPoints = True
            showPointFunc()
            if personagem_hit == "J1":
                Classe.Score += 500
            else:
                Classe2.Score += 500
        print('miseravi', self.estado)

    def __delete__(self, instance):
        pass
    def __del__(self):
        pass

Classe = Player(200, 410, 64, 64, 64, 64, 64)
Classe2 = Player2(200, 250, 64, 64, 64, 64)
inimigo = InimigoBase(100, 410, 64, 64, 450)
inimigo2 = InimigoBase(100, 410, 64, 64, 450)

#Criação dos objetos de hitbox do soco dos Personagens
soco=projetosoco(200, 410, 64, 64, 64)
soco2=projetosoco2(200, 410, 64, 64, 64)
loop = 0
socobala = []
socobala2 = []
luis=[]

# Propriedades da Janela a ser aberta
Largura, Altura = 640, 480
HW, HH = Largura / 2, Altura / 2
Area = Largura * Altura
Nome_da_Janela = "FLYING FIST"

# Esse código inicializa a Janela com as propriedades definidas nas variaveis
pygame.init()
clock = pygame.time.Clock()
Janela = pygame.display.set_mode((Largura, Altura),)
pygame.display.set_caption(Nome_da_Janela)

# Esta variável controlará as telas do jogo
Controlador_Jogo = 1

# Essa variável define a pontuação do jogador, e o Timer da fase
Score = 0
Timer = 60
Nome_do_player = ("JOG")


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

showPoints = False
primeira_fase = 0

def showPointFunc():
    compressao_save.compressao()
    pygame.mixer.fadeout(2)
    pygame.mixer.music.set_endevent(SONG_END)
    pygame.mixer.music.load('Musica_SFX/Fanfare.mp3')
    pygame.mixer.music.play(1)



def mostrarPlacar(Pontos):
    D = ""
    for key in Pontos[:8]:
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

    return D

if os.path.exists("top_scores") == True:
    pass
else:
    Load_Top_Scores = Leaderboard
    pickle.dump(Load_Top_Scores, open("top_scores", "wb"))
    Load_Top_Scores = pickle.load(open("top_scores", "rb"))
    Load_Top_Scores.sort(key=itemgetter('Pontos'), reverse=True)


Load_Top_Scores = pickle.load(open("top_scores", "rb"))
"""""
Scoreboard_Player = {'Nome': Classe.Nome_Player, 'Pontos': Classe.Score}
Scoreboard_Player2 = {'Nome': Classe2.Nome_Player, 'Pontos': Classe2.Score}
Load_Top_Scores.insert(0, Scoreboard_Player)
Load_Top_Scores.insert(0, Scoreboard_Player2)
pickle.dump(Load_Top_Scores, open("top_scores", "wb"))
Load_Top_Scores = pickle.load(open("top_scores", "rb"))
Load_Top_Scores.sort(key=itemgetter('Pontos'), reverse=True)
"""
for key in Load_Top_Scores:
    print(key)

textoPlacar = mostrarPlacar(Load_Top_Scores)

compressao_save.compressao()

print(textoPlacar)

# Carrega as imagem do jogo em geral
Background_Fase = pygame.image.load("images/Background_Fase.png").convert_alpha()
Background_Fase_0 = pygame.image.load("images/Background_Fase_0.png").convert()
Background_Fase2 = pygame.image.load("images/Background_Fase2.png").convert_alpha()
Background_Fase2_0 = pygame.image.load("images/Background_Fase2_0.png").convert()
Background_Tela_Inicial = pygame.image.load("images/Tela_Inicial/Tela_de_Titulo.png").convert()
Personagem_HUD = pygame.image.load("images/Personagem_Vida.png").convert_alpha()
Go = pygame.image.load("images/Go.png").convert_alpha()
Start = False
# Define a Altura e Largura do background
Background_Largura, Background_Altura = Background_Fase.get_rect().size

# Define o tamanho da fase
Fase_Largura = Background_Largura * 10
# Define a posicao do background da fase em relação a janela
Background_Fase_Posicao = 0
Background_Fase_Posicao_0 = 0
startScrollingPosX = HW+150

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
Classe2.Y = 100
Classe.playerVelocityX = 0
Classe.playerVelocityY = 0



# Musica é tocada assim que executa o jogo, mas não em loop
# Musica_Fase = pygame.mixer.music.load('Musica_SFX/Musica_Fase.wav')
SONG_END = pygame.USEREVENT + 1

SFX_Voice_Flying2 = pygame.mixer.Sound('Musica_SFX/SFX/Voice_Flying2.wav')
SFX_Voice_Flying2.play(0)

SFX_Punch1 = pygame.mixer.Sound('Musica_SFX/SFX/Punch_1.wav')
SFX_Punch1.set_volume(0.5)
SFX_Punch2 = pygame.mixer.Sound('Musica_SFX/SFX/Punch_2.wav')
SFX_Miss = pygame.mixer.Sound('Musica_SFX/SFX/Punch_miss.wav')
SFX_Miss.set_volume(0.5)
SFX_Death = pygame.mixer.Sound('Musica_SFX/SFX/Death.wav')
SFX_Text = pygame.mixer.Sound('Musica_SFX/SFX/Text_Sound.wav')
SFX_Text.set_volume(0.07)

Cutscene1 = pygame.image.load("images/Tela_Inicial/Cutscene_1.png").convert()
Cutscene2 = pygame.image.load("images/Tela_Inicial/Cutscene_2.png").convert()
Cutscene3 = pygame.image.load("images/Tela_Inicial/Cutscene_3.png").convert()
Cutscene4 = pygame.image.load("images/Tela_Inicial/Cutscene_4.png").convert()
Cutscene7 = pygame.image.load("images/Tela_Inicial/Cutscene_7_0.png").convert()
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
Akira é lutar. """

text_orig5 = """Seu mestre reconhece seu 
potencial, mas a fúria de
Akira é seu maior inimigo. """

text_orig6 = """Após a morte de seu
mestre, Akira decide 
voltar para seu vilarejo """

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

text_orig12 = """Você zerou o
jogo! """

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
text_iterator12 = iter(text_orig12)

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
text12 = ''

textnumber = 1

def redrawGameWindow():
    if Controlador_Jogo == 1:
        Janela.blit(Background_Tela_Inicial, (0, -10))
        Tela_Inicial.Press_Start.blit(Janela, (110, 320))
        Tela_Inicial.Tela_de_titulo_animacao.blit(Janela, (0, -10))
        pygame.display.update()

    if Controlador_Jogo == 0:
        Janela.blit(Background_Fase_0, (rel_x2, 0))
        Janela.blit(Background_Fase, (rel_x, 0), )
        Janela.blit(Background_Fase_0, (rel_x2 - Background_Largura, 0))
        Janela.blit(Background_Fase, (rel_x - Background_Largura, 0))
        # Janela.blit ( Texto_Timer , ((Largura / 2) - 17 , 10) )
        # Janela.blit ( Texto_Placar , (190 , 30) )

        Janela.blit(Personagem_HUD, (10, 10))
        Janela.blit(Personagem_HUD, (392, 10))
        pygame.draw.rect(Janela, (255, 255, 0), (78, 57, Classe.HP, 19), 0)
        pygame.draw.rect(Janela, (255, 255, 0), (460, 57, Classe2.HP, 19), 0)
        Classe.draw(Janela)
        Classe2.draw(Janela)
        inimigo2.draw(Janela)
        inimigo.draw(Janela)

        seconds = int((pygame.time.get_ticks() - start_ticks) / 1000)


        ptext.draw(str(Classe.Score), topleft=(190, 28), fontname="fontes/start.ttf", color=(255, 100, 0),
                   gcolor=(255, 200, 20), fontsize=19,
                   shadow=(3, 1), scolor="#000000")

        ptext.draw(str(Classe2.Score), topleft=(572, 28), fontname="fontes/start.ttf", color=(255, 100, 0),
                   gcolor=(255, 200, 20), fontsize=19,
                   shadow=(3, 1), scolor="#000000")

        ptext.draw(str(Timer - seconds), center=(Largura / 2, 30), fontname="fontes/start.ttf", color=(255, 255, 255),
                   gcolor=(150, 150, 150),
                   shadow=(3, 3), scolor="#000000")

        for balau in socobala:
            balau.draw(Janela)

        for balau2 in socobala2:
            balau2.draw(Janela)

        for balau2 in luis:
            balau2.draw(Janela)



        if showPoints == True:
            textoPlacar = mostrarPlacar(Load_Top_Scores)
            ptext.draw(str(textoPlacar), midtop=(Largura / 2, 175), fontname="fontes/start.ttf",
                       color=(255, 255, 255),
                       gcolor=(150, 150, 150),
                       shadow=(3, 3), scolor="#000000")

            ptext.draw("FASE COMPLETA!!", center=(Largura / 2, 135), fontname="fontes/start.ttf",
                       color=(255, 100, 0),
                       gcolor=(255, 200, 20),
                       shadow=(3, 3), scolor="#000000",fontsize=35)

        if Classe.parartela == False and Start == False and showPoints == False:
            Cutscenes.Go.blit(Janela,(450,60))


        Cutscenes.Start_Play.blit(Janela,(80, 100))
        pygame.display.update()

    if Controlador_Jogo == 4:
        Janela.blit(Background_Fase2_0, (rel_x2, 0))
        Janela.blit(Background_Fase2, (rel_x, 0), )
        Janela.blit(Background_Fase2_0, (rel_x2 - Background_Largura, 0))
        Janela.blit(Background_Fase2, (rel_x - Background_Largura, 0))
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

        if showPoints == True:
            ptext.draw(str(compressao_save.umcompressed_string), center=(Largura / 2, Altura / 2), fontname="fontes/start.ttf",
                       color=(255, 255, 255),
                       gcolor=(150, 150, 150),
                       shadow=(3, 3), scolor="#000000")

        pygame.display.update()

    if Controlador_Jogo == 3:
        #Janela.blit(Background_Tela_Inicial, (0, -10))
        #Tela_Inicial.Press_Start.blit(Janela, (110, 320))
        if textnumber == 4:
            Cutscenes.Cutscene_2.blit(Janela, (0,0))
        #Tela_Inicial.Tela_de_titulo_animacao.blit(Janela, (0, -10))
        if textnumber >= 6 and textnumber < 9:
            Cutscenes.Cutscene_Kobra.blit(Janela,(0,0))
def MovimentoPersonagem1():
    if Botao_Pressionado[pygame.K_LEFT] and Classe.x >5 and Start == False:
        if Classe.estado == False:
            if Classe.socoestado == False:
                Classe.playerVelocityX=0
                Classe.esquerda = True
                Classe.direita = False
                Classe.Virado=True
                Classe.apertou1 = True

    if Botao_Pressionado[pygame.K_LEFT] and Classe.x > 5 and Start == False:
        if Classe.estado == False:
            if Classe.socoestado == False:
                Classe.playerVelocityX = -4
                Classe.x += Classe.playerVelocityX
                Classe.esquerda = True
                Classe.direita = False
                Classe.Virado=False
                Classe.apertou1 = False


    elif Botao_Pressionado[pygame.K_RIGHT] and Classe.x <530 and Start == False:
        if Classe.estado == False:
            if Classe.socoestado == False:
                Classe.playerVelocityX = 4
                Classe.x += Classe.playerVelocityX
                Classe.direita = True
                Classe.esquerda = False
                Classe.Virado=False
                Classe.apertou1 = True


    elif Botao_Pressionado[pygame.K_UP] and Classe.y > 209 and Start == False:
        if Classe.estado == False:
            if Classe.socoestado == False:
                Classe.playerVelocityY = -4
                Classe.y += Classe.playerVelocityY
                if Classe.apertou1 == False:
                    Classe.esquerda = True
                    Classe.baixo = False
                else:
                    Classe.baixo = False
                    Classe.cima = True

    elif Botao_Pressionado[pygame.K_DOWN] and Classe.y <380 and Start == False:
        if Classe.estado == False:
            if Classe.socoestado == False:
                Classe.playerVelocityY = 4
                Classe.y += Classe.playerVelocityY
                if Classe.apertou1 == False:
                    Classe.esquerda = True
                    Classe.baixo = False
                else:
                    Classe.baixo = True
                    Classe.cima = False

    elif Botao_Pressionado[pygame.K_x]:
        if Classe.estado == False:
            Classe.danoPlayer()
            Classe2.danoPlayer2()

    elif Botao_Pressionado[pygame.K_m]:
        if Classe.estado == False:
            if Classe.socoestado == False:
                Classe.ContarPassos = 0
                Classe.socoestado = True
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
                    print(Classe.socovirado)
                print("PORRADA !! *20:", Classe.socovirado)

    else:
        if Classe.estado == False:
            if Classe.socoestado == False:
                Classe.direita = False
                Classe.esquerda = False
                Classe.baixo = False
                Classe.cima = False
                Classe.soco = False
                Classe.socovirado=False
                Classe.parado=False
                Classe.playerVelocityY = 0
                Classe.playerVelocityX = 0

        if Classe.playerVelocityX == 0 :
            if Classe.estado == False:
                if Classe.socoestado == False:
                    Classe.parado = True
        if Classe.apertou1==False:
            if Classe.estado == False:
                if Classe.socoestado == False:
                    Classe.Virado=True
def MovimentoPersonagem2():
    # Player2
    if Botao_Pressionado[pygame.K_a] and Classe2.x > 5 and Start == False:
        if Classe2.estado == False:
            if Classe2.socoestado == False:
                Classe2.playerVelocityX = 0
                Classe2.esquerda = True
                Classe2.direita = False
                Classe2.Virado = True
                Classe2.apertou1 = True

    if Botao_Pressionado[pygame.K_a] and Classe2.x > 5 and Start == False:
        if Classe2.estado == False:
            if Classe2.socoestado == False:
                Classe2.playerVelocityX = -4
                Classe2.x += Classe2.playerVelocityX
                Classe2.esquerda = True
                Classe2.direita = False
                Classe2.Virado = False
                Classe2.apertou1 = False


    elif Botao_Pressionado[pygame.K_d] and Classe2.x < 530 and Start == False:
        if Classe2.estado == False:
            if Classe2.socoestado == False:
                Classe2.playerVelocityX = 4
                Classe2.x += Classe2.playerVelocityX
                Classe2.direita = True
                Classe2.esquerda = False
                Classe2.Virado = False
                Classe2.apertou1 = True


    elif Botao_Pressionado[pygame.K_w] and Classe2.y > 209 and Start == False:
        if Classe2.estado == False:
            if Classe2.socoestado == False:
                Classe2.playerVelocityY = -4
                Classe2.y += Classe2.playerVelocityY
                if Classe2.apertou1 == False:
                    Classe2.esquerda = True
                    Classe2.baixo = False
                else:
                    Classe2.baixo = False
                    Classe2.cima = True


    elif Botao_Pressionado[pygame.K_s] and Classe2.y < 380 and Start == False:
        if Classe2.estado == False:
            if Classe2.socoestado == False:
                Classe2.playerVelocityY = 4
                Classe2.y += Classe2.playerVelocityY
                if Classe2.apertou1 == False:
                    Classe2.esquerda = True
                    Classe2.baixo = False
                else:
                    Classe2.baixo = True
                    Classe2.cima = False

    elif Botao_Pressionado[pygame.K_i]:
        if Classe2.estado == False:
            if Classe2.socoestado == False:
                Classe2.ContarPassos = 0
                Classe2.socoestado = True
                SFX_Miss.play(0)
                if Classe2.esquerda:
                    mira2 = -1
                else:
                    mira2 = 1
                if len(socobala2) < 1:
                    socobala2.append(
                        projetosoco2(round(Classe2.x + Classe2.largura // 2), round(Classe2.y + Classe2.altura // 2), 6,
                                     (0, 0, 0),
                                     mira2))

                shootLoop = 1
                if Classe2.apertou1 == True:
                    Classe2.soco = True

                if Classe2.apertou1 == False:
                    Classe2.socovirado = True
                    Classe2.Virado = False
                else:
                    Classe2.socovirado = False
                    print(Classe2.socovirado)
                print("PORRADA !! *20:", Classe2.socovirado)

    else:
        if Classe2.estado == False:
            if Classe2.socoestado == False:
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
            if Classe2.estado == False:
                if Classe2.socoestado == False:
                    Classe2.parado = True
        if Classe2.apertou1 == False:
            if Classe2.estado == False:
                if Classe2.socoestado == False:
                    Classe2.Virado = True
def Colisao_Soco_Personagem1():
    # Testa a colisão do soco do Player 1
    for bullet in socobala:
        if (bullet.x + bullet.raio >= inimigo.hitbox[0] and bullet.x + bullet.raio <= inimigo.hitbox[0] + 30):
            if bullet.y >= inimigo.hitbox[1] and bullet.y <= inimigo.hitbox[1] + 40:
                inimigo.hit("J1")
                socobala.pop(socobala.index(bullet))
        elif (bullet.x + bullet.raio >= inimigo2.hitbox[0] and bullet.x + bullet.raio <= inimigo2.hitbox[0] + 30):
            if bullet.y >= inimigo2.hitbox[1] and bullet.y <= inimigo2.hitbox[1] + 40:
                inimigo2.hit("J1")
                socobala.pop(socobala.index(bullet))
        else:
            socobala.pop(socobala.index(bullet))
def Colisao_Soco_Personagem2():
    # Testa a colisão do soco do Player 2
    for bullet in socobala2:
        if (bullet.x + bullet.raio >= inimigo.hitbox[0] and bullet.x + bullet.raio <= inimigo.hitbox[0] + 30):
            if bullet.y >= inimigo.hitbox[1] and bullet.y <= inimigo.hitbox[1] + 40:
                inimigo.hit("J2")
                socobala2.pop(socobala2.index(bullet))
        elif (bullet.x + bullet.raio >= inimigo2.hitbox[0] and bullet.x + bullet.raio <= inimigo2.hitbox[0] + 30):
            if bullet.y >= inimigo2.hitbox[1] and bullet.y <= inimigo2.hitbox[1] + 40:
                inimigo2.hit("J2")
                socobala2.pop(socobala2.index(bullet))
        else:
            socobala2.pop(socobala2.index(bullet))



def Colisao_Soco_Inimigo():
    # Testa a colisão do soco do Player 2
    for bullet in luis:
        if (bullet.x + bullet.raio >= inimigo.hitbox[0] and bullet.x + bullet.raio <= Classe.hitbox[0] + 30):
            if bullet.y >= Classe.hitbox[1] and bullet.y <= Classe.hitbox[1] + 40:
                Classe.danoPlayer()
                luis.pop(luis.index(bullet))
        elif (bullet.x + bullet.raio >= Classe2.hitbox[0] and bullet.x + bullet.raio <= Classe2.hitbox[0] + 30):
            if bullet.y >= Classe2.hitbox[1] and bullet.y <= Classe2.hitbox[1] + 40:
                Classe2.danoPlayer2()
                luis.pop(luis.index(bullet))
        else:
            luis.pop(luis.index(bullet))






while run:
    clock.tick(27)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == SONG_END:
            if primeira_fase == 0:
                Controlador_Jogo = 3
                primeira_fase+=1
                textnumber = 13
                showPoints = False

    Botao_Pressionado = pygame.key.get_pressed()

    Cutscenes.Go.play()

    if Start == True:
        Cutscenes.Start_Play.play()
    else:
        Cutscenes.Start_Play.stop()
    if Cutscenes.Start_Play.currentFrameNum == 18:
        Start = False

    # Essa parte do código é referente ao SideScrolling e posição do personagem na tela. Para entender, ver https://www.youtube.com/watch?v=AX8YU2hLBUg&t=478s
    if Classe.parartela == False:
      #if Classe.x and Classe2.x > Fase_Largura:
       #  Classe.x = Fase_Largura
       #  Classe2.x = Fase_Largura
      if Classe2.x <= startScrollingPosX:
        # Classe.x = Classe.x
         Classe2.x = Classe2.x

      #elif Classe.x and Classe2.x > Fase_Largura - startScrollingPosX:
       #  Classe.x = Classe.x - Fase_Largura + Largura
        # Classe2.x = Classe2.x - Fase_Largura + Larguraw
      elif  Classe2.playerVelocityX >=0:
        # Classe.x = startScrollingPosX
         #Background_Fase_Posicao += -Classe.playerVelocityX
         #Background_Fase_Posicao_0 += -1
         Classe2.x = startScrollingPosX
         Background_Fase_Posicao += -Classe2.playerVelocityX
         Background_Fase_Posicao_0 += -1
         if Classe.direita == False:
             Classe.playerVelocityX = -4
             Classe.x += Classe.playerVelocityX
             print("andando")

      rel_x = Background_Fase_Posicao % Background_Largura
      rel_x2 = Background_Fase_Posicao_0 % Background_Largura

    Colisao_Soco_Personagem1()
    Colisao_Soco_Personagem2()
    Colisao_Soco_Inimigo ()
    MovimentoPersonagem1()
    Colisao_Soco_Inimigo ()
    MovimentoPersonagem2()

# Controlador_Jogo é igual a 1, você está na tela de título
    if Controlador_Jogo == 1:

        Tela_Inicial.Press_Start.play()
        if Botao_Pressionado[K_RETURN]:
            Tela_Inicial.Tela_de_titulo_animacao.play()

        #Esse comando reseta o scoreboard
        if Botao_Pressionado[K_s]:
            pickle.dump(Leaderboard, open("top_scores", "wb"))
            Load_Top_Scores = pickle.load(open("top_scores", "rb"))

        if Botao_Pressionado[K_d]:
            Load_Top_Scores = pickle.load(open("top_scores", "rb"))
            Load_Top_Scores.sort(key=itemgetter('Pontos'), reverse=True)
            mostrarPlacar(Load_Top_Scores)

        if Tela_Inicial.Tela_de_titulo_animacao.currentFrameNum == 9:
            Controlador_Jogo = 6
            start_ticks = pygame.time.get_ticks()
            pygame.mixer.music.stop()
            pygame.mixer.music.load('Musica_SFX/intro_akira.mp3')
            pygame.mixer.music.play()

    if Controlador_Jogo == 3:
        pygame.display.update()


        if Botao_Pressionado[K_RETURN]:
            Controlador_Jogo = 0
            start_ticks = pygame.time.get_ticks()
            pygame.mixer.music.stop()
            pygame.mixer.music.load('Musica_SFX/Musica_Fase.wav')
            pygame.mixer.music.play(-1)
            Start = True

        if textnumber == 1:
            Janela.blit(Cutscene1, (0, 0))
            if len(text) < len(text_orig):
                text += next(text_iterator)
                SFX_Text.play(0)

        ptext.draw(text, center=(Largura / 2, 350), fontname="fontes/start.ttf", color=(255, 255, 255),
                   gcolor=(150, 150, 150),
                   shadow=(3, 3), scolor="#000000")
        if len(text) == len(text_orig):
            Janela.fill((0, 0, 0))
            time.sleep(2)
            text += " "
            textnumber = 2
            Janela.fill((0, 0, 0))

        if textnumber == 2:
            Janela.blit(Cutscene1, (0, 0))
            if len(text2) < len(text_orig2):
                text2 += next(text_iterator2)
                SFX_Text.play(0)

        ptext.draw(text2, center=(Largura / 2, 350), fontname="fontes/start.ttf", color=(255, 255, 255),
                   gcolor=(150, 150, 150),
                   shadow=(3, 3), scolor="#000000")

        if len(text2) == len(text_orig2):
            Janela.fill((0, 0, 0))
            textnumber = 3
            time.sleep(2)
            text2 += " "
            Janela.fill((0, 0, 0))

        if textnumber == 3:
            Janela.blit(Cutscene1, (0, 0))
            if len(text3) < len(text_orig3):
                text3 += next(text_iterator3)
                SFX_Text.play(0)

        ptext.draw(text3, center=(Largura / 2, 350), fontname="fontes/start.ttf", color=(255, 255, 255),
                   gcolor=(150, 150, 150),
                   shadow=(3, 3), scolor="#000000")

        if len(text3) == len(text_orig3):

            textnumber = 4
            time.sleep(3)
            text3 += " "
            Janela.fill((0, 0, 0))

        if textnumber == 4:
            Janela.fill((0, 0, 0))
            ptext.draw(text4, center=(Largura / 2, 350), fontname="fontes/start.ttf", color=(255, 255, 255),
                       gcolor=(150, 150, 150),
                       shadow=(3, 3), scolor="#000000")
            Cutscenes.Cutscene_2.play()
            #Janela.blit(Cutscene2, (0, 0))
            if len(text4) < len(text_orig4):
                text4 += next(text_iterator4)
                SFX_Text.play(0)



        if len(text4) == len(text_orig4):
            Janela.fill((0, 0, 0))
            textnumber = 5
            time.sleep(3)
            text4 += " "
            Janela.fill((0, 0, 0))

        if textnumber == 5:
            Janela.blit(Cutscene3, (0, 0))
            if len(text5) < len(text_orig5):
                text5 += next(text_iterator5)
                SFX_Text.play(0)

        ptext.draw(text5, center=(Largura / 2, 350), fontname="fontes/start.ttf", color=(255, 255, 255),
                   gcolor=(150, 150, 150),
                   shadow=(3, 3), scolor="#000000")

        if len(text5) == len(text_orig5):
            Janela.fill((0, 0, 0))
            textnumber = 6
            time.sleep(2)
            text5 += " "
            Janela.fill((0, 0, 0))

        if textnumber == 6:
            Janela.fill((0, 0, 0))
            Janela.blit(Cutscene7, (0, 0))
            if len(text6) < len(text_orig6):
                text6 += next(text_iterator6)
                SFX_Text.play(0)

        ptext.draw(text6, center=(Largura / 2, 350), fontname="fontes/start.ttf", color=(255, 255, 255),
                   gcolor=(150, 150, 150),
                   shadow=(3, 3), scolor="#000000")

        if len(text6) == len(text_orig6):
            Janela.fill((0, 0, 0))
            textnumber = 7
            time.sleep(3)
            text6 += " "
            Janela.fill((0, 0, 0))

        if textnumber == 7:
            Janela.fill((0, 0, 0))
            Janela.blit(Cutscene7, (0, 0))
            if len(text7) < len(text_orig7):
                text7 += next(text_iterator7)
                SFX_Text.play(0)

        ptext.draw(text7, center=(Largura / 2, 350), fontname="fontes/start.ttf", color=(255, 255, 255),
                   gcolor=(150, 150, 150),
                   shadow=(3, 3), scolor="#000000")

        if len(text7) == len(text_orig7):
            Janela.fill((0, 0, 0))
            textnumber = 8
            time.sleep(2)
            text7 += " "
            Janela.fill((0, 0, 0))

        if textnumber == 8:
            Janela.fill((0, 0, 0))
            Cutscenes.Cutscene_Kobra.play()
            if len(text8) < len(text_orig8):
                text8 += next(text_iterator8)
                SFX_Text.play(0)

        ptext.draw(text8, center=(Largura / 2, 350), fontname="fontes/start.ttf", color=(255, 255, 255),
                   gcolor=(150, 150, 150),
                   shadow=(3, 3), scolor="#000000")

        if len(text8) == len(text_orig8):
            Janela.fill((0, 0, 0))
            textnumber = 9
            time.sleep(2)
            text8 += " "
            Janela.fill((0, 0, 0))

        if textnumber == 9:
            Janela.fill((0, 0, 0))
            Cutscenes.Cutscene_Kobra.play()
            if len(text9) < len(text_orig9):
                text9 += next(text_iterator9)
                SFX_Text.play(0)

        ptext.draw(text9, center=(Largura / 2, 220), fontname="fontes/start.ttf", color=(255, 255, 255),
                   gcolor=(150, 150, 150),
                   shadow=(3, 3), scolor="#000000")

        if len(text9) == len(text_orig9):
            Janela.fill((0, 0, 0))
            textnumber = 10
            time.sleep(3)
            text9 += " "
            Janela.fill((0, 0, 0))

        if textnumber == 10:

            Janela.fill((0, 0, 0))
            Janela.blit(Cutscene4, (0, 0))
            if len(text10) < len(text_orig10):
                text10 += next(text_iterator10)
                SFX_Text.play(0)

        ptext.draw(text10, center=(Largura / 2, 350), fontname="fontes/start.ttf", color=(255, 255, 255),
                   gcolor=(150, 150, 150),
                   shadow=(3, 3), scolor="#000000")

        if len(text10) == len(text_orig10):
            Janela.fill((0, 0, 0))
            textnumber = 11
            time.sleep(2)
            text10 += " "
            Janela.fill((0, 0, 0))

        if textnumber == 11:
            Janela.fill((0, 0, 0))
            Janela.blit(Cutscene4, (0, 0))
            if len(text11) < len(text_orig11):
                text11 += next(text_iterator11)
                SFX_Text.play(0)

        ptext.draw(text11, center=(Largura / 2, 350), fontname="fontes/start.ttf", color=(255, 255, 255),
                   gcolor=(150, 150, 150),
                   shadow=(3, 3), scolor="#000000")

        if len(text11) == len(text_orig11):
            Janela.fill((0, 0, 0))
            textnumber = 12
            time.sleep(5)
            text11 += " "
            Janela.fill((0, 0, 0))

        if textnumber == 12:
            Janela.fill((0, 0, 0))
            Janela.blit(Cutscene4, (0, 0))
            Controlador_Jogo = 0
            start_ticks = pygame.time.get_ticks()
            pygame.mixer.music.stop()
            pygame.mixer.music.load('Musica_SFX/Musica_Fase.wav')
            pygame.mixer.music.play(-1)
            textnumber = 13

            Start = True

        if textnumber == 13:
            Janela.fill((0, 0, 0))
            Janela.blit(Cutscene4, (0, 0))
            if len(text12) < len(text_orig12):
                text12 += next(text_iterator12)
                SFX_Text.play(0)

        ptext.draw(text12, center=(Largura / 2, Altura / 2), fontname="fontes/start.ttf", color=(255, 255, 255),
                   gcolor=(150, 150, 150),
                   shadow=(3, 3), scolor="#000000")

        if len(text12) == len(text_orig12):
            Janela.fill((0, 0, 0))
            textnumber = 14
            time.sleep(2)
            text12 += " "
            Janela.fill((0, 0, 0))

        if textnumber == 14:
            Controlador_Jogo = 4
            start_ticks = pygame.time.get_ticks()
            pygame.mixer.music.stop()
            pygame.mixer.music.load('Musica_SFX/Musica_Fase.wav')
            pygame.mixer.music.play(-1)
            textnumber = 15


        # Teste de Leaderboards com valores atualizados

    if Controlador_Jogo == 6:
        Janela.fill((0, 0, 0))
        Letra1 = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        if pygame.key.get_pressed()[pygame.K_RETURN] and LetraAtual <3:
            time.sleep(0.2)
            LetraAtual +=1
            Auxiliar = 0
            print (LetraAtual)
            if LetraAtual == 3:
                Classe.Nome_Player = str(Letra1[LetraA])+str(Letra1[LetraB])+str(Letra1[LetraC])
                print (Classe.Nome_Player)
                Controlador_Jogo = 3
        if LetraAtual == 0:
            if pygame.key.get_pressed()[pygame.K_UP]:
                if Auxiliar >= 25:
                    time.sleep(0.1)
                    Auxiliar = 0
                    LetraA = Auxiliar
                    print("UP")
                else:
                    time.sleep(0.1)
                    Auxiliar += 1
                    LetraA = Auxiliar
                    print("UP")
            if pygame.key.get_pressed()[pygame.K_DOWN]:
                time.sleep(0.1)
                Auxiliar -=1
                LetraA = Auxiliar
                if Auxiliar < 0:
                    Auxiliar = 25
                    LetraA = Auxiliar
                    print("DOWN")
        if LetraAtual == 1:
            if pygame.key.get_pressed()[pygame.K_UP]:
                if Auxiliar >= 25:
                    time.sleep(0.1)
                    Auxiliar = 0
                    LetraB = Auxiliar
                    print("UP")
                else:
                    time.sleep(0.1)
                    Auxiliar += 1
                    LetraB = Auxiliar
                    print("DOWN")
            elif pygame.key.get_pressed()[pygame.K_DOWN]:
                time.sleep(0.1)
                Auxiliar -= 1
                LetraB = Auxiliar
                if Auxiliar < 0:
                    Auxiliar = 25
                    LetraB = Auxiliar
        if LetraAtual == 2:
            if pygame.key.get_pressed()[pygame.K_UP]:
                if Auxiliar >= 25:
                    time.sleep(0.1)
                    Auxiliar = 0
                    LetraC = Auxiliar
                    print("UP")
                else:
                    time.sleep(0.1)
                    Auxiliar += 1
                    LetraC = Auxiliar
                    print("DOWN")
            elif pygame.key.get_pressed()[pygame.K_DOWN]:
                time.sleep(0.1)
                Auxiliar -= 1
                LetraC=Auxiliar
                if Auxiliar < 0:
                    Auxiliar = 25
                    LetraC = Auxiliar

        ptext.draw("DIGITE SEU NOME", center=(Largura / 2, Altura / 2-60), fontname="fontes/start.ttf",
                   color=(255, 255, 255),
                   gcolor=(150, 150, 150),
                   shadow=(3, 3), scolor="#000000")
        ptext.draw(str(Letra1[LetraA]), center=(Largura / 2-27, Altura / 2), fontname="fontes/start.ttf",
                   color=(255, 255, 255),
                   gcolor=(150, 150, 150),
                   shadow=(3, 3), scolor="#000000")
        ptext.draw(str(Letra1[LetraB]), center=(Largura / 2, Altura / 2), fontname="fontes/start.ttf",
                   color=(255, 255, 255),
                   gcolor=(150, 150, 150),
                   shadow=(3, 3), scolor="#000000")
        ptext.draw(str(Letra1[LetraC]), center=(Largura / 2+27, Altura / 2), fontname="fontes/start.ttf",
                   color=(255, 255, 255),
                   gcolor=(150, 150, 150),
                   shadow=(3, 3), scolor="#000000")
        pygame.display.update()


    if Botao_Pressionado[pygame.K_r]:
        textoPlacar = mostrarPlacar(Load_Top_Scores)
        time.sleep(1)

    #Carrega o scoreboard
    if Botao_Pressionado[K_l]:
        Scoreboard_Player = {'Nome': Nome_do_player, 'Pontos': Score}
        Load_Top_Scores.insert(0, Scoreboard_Player)
        pickle.dump(Load_Top_Scores, open("top_scores", "wb"))
        Load_Top_Scores = pickle.load(open("top_scores", "rb"))
        Load_Top_Scores.sort(key=itemgetter('Pontos'), reverse=True)
        for key in Load_Top_Scores:
            print(key)

# Teste para ver a barra de vida diminuindo
    if Botao_Pressionado[K_b] and Classe.HP >= 0.9:
        Classe.HP -= 0.2
        Classe.Score += 10
        Classe2.Score += 10

    redrawGameWindow()

pygame.quit()