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

Nome_Jogador_Primeira_Letra = 0
Nome_Jogador_Segunda_Letra = 0
Nome_Jogador_Terceira_Letra = 0
Nome_Jogador_Letra_Atual = 0
Nome_Jogador_Letra_Temporaria = 0
SlowMotion = False

def events():
    for event in pygame.event.get():
        if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
            pygame.quit()
            sys.exit()

class Player(object):
    Andar_Direita_Animacao = [pygame.image.load('images/Personagem_Sprites/Personagem__Andando_1.png'),
                    pygame.image.load('images/Personagem_Sprites/Personagem__Andando_2.png'),
                    pygame.image.load('images/Personagem_Sprites/Personagem__Andando_3.png'),
                    pygame.image.load('images/Personagem_Sprites/Personagem__Andando_4.png'),
                    pygame.image.load('images/Personagem_Sprites/Personagem__Andando_5.png'),
                    pygame.image.load('images/Personagem_Sprites/Personagem__Andando_6.png'),
                    ]
    Andar_Esquerda_Animacao = [pygame.image.load('images/Personagem_Sprites/R_Personagem__Andando_1.png'),
                     pygame.image.load('images/Personagem_Sprites/R_Personagem__Andando_2.png'),
                     pygame.image.load('images/Personagem_Sprites/R_Personagem__Andando_3.png'),
                     pygame.image.load('images/Personagem_Sprites/R_Personagem__Andando_4.png'),
                     pygame.image.load('images/Personagem_Sprites/R_Personagem__Andando_5.png'),
                     pygame.image.load('images/Personagem_Sprites/R_Personagem__Andando_6.png'),
                     ]
    Soco_Animacao = [pygame.image.load('images/Personagem_Sprites/Personagem__Soco_2.png'),
            pygame.image.load('images/Personagem_Sprites/Personagem__Soco_1.png'),
            pygame.image.load('images/Personagem_Sprites/Personagem__Soco_0.png'),
            pygame.image.load('images/Personagem_Sprites/Personagem__Soco_4.png')
            ]
    Soco_Esquerda_Animacao = [pygame.image.load('images/Personagem_Sprites/R_Personagem__Soco_2.png'),
                  pygame.image.load('images/Personagem_Sprites/R_Personagem__Soco_1.png'),
                  pygame.image.load('images/Personagem_Sprites/R_Personagem__Soco_0.png'),
                  pygame.image.load('images/Personagem_Sprites/R_Personagem__Soco_4.png')
                  ]
    Personagem_Parado_Esquerda_Animacao = [pygame.image.load('images/Personagem_Sprites/Personagem__Parado_R0.png'),
              pygame.image.load('images/Personagem_Sprites/R_Personagem__Parado_1.png'),
              pygame.image.load('images/Personagem_Sprites/R_Personagem__Parado_2.png'),
              pygame.image.load('images/Personagem_Sprites/R_Personagem__Parado_3.png'),
              pygame.image.load('images/Personagem_Sprites/R_Personagem__Parado_4.png'),
              pygame.image.load('images/Personagem_Sprites/R_Personagem__Parado_5.png'),
              ]
    Personagem_Parado_Direita_Animacao = [pygame.image.load('images/Personagem_Sprites/Personagem__Parado_0.png'),
            pygame.image.load('images/Personagem_Sprites/Personagem__Parado_1.png'),
            pygame.image.load('images/Personagem_Sprites/Personagem__Parado_2.png'),
            pygame.image.load('images/Personagem_Sprites/Personagem__Parado_3.png'),
            pygame.image.load('images/Personagem_Sprites/Personagem__Parado_4.png'),
            pygame.image.load('images/Personagem_Sprites/Personagem__Parado_5.png'),
            ]
    Personagem_Dano_Direita_Animacao = [pygame.image.load('images/Personagem_Sprites/R_Personagem__Dano_0.png'),
            pygame.image.load('images/Personagem_Sprites/R_Personagem__Dano_1.png'),
            pygame.image.load('images/Personagem_Sprites/R_Personagem__Dano_2.png'),
            ]
    Personagem_Dano_Esquerda_Animacao = [pygame.image.load('images/Personagem_Sprites/L_Personagem__Dano_0.png'),
                  pygame.image.load('images/Personagem_Sprites/L_Personagem__Dano_1.png'),
                  pygame.image.load('images/Personagem_Sprites/L_Personagem__Dano_2.png'),
                  ]

    def __init__(self, x, y, largura, altura, velocidade_Personagem_X, velocidade_Personagem_Y, verificador_de_lado_esquerdo):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.velocidade_Personagem_X = velocidade_Personagem_X
        self.velocidade_Personagem_Y = velocidade_Personagem_Y
        self.esquerda = False
        self.verificador_de_lado_esquerdo=True
        self.direita = False
        self.baixo = False
        self.cima = False
        self.soco = False
        self.contador_de_passos = 0
        self.parado = False
        self.Virado=False
        self.soco_para_esquerda=False
        self.verificar_hitstun = False
        self.esta_atacando = False
        self.parartela = False
        self.contador_frames_animacao = 0
        self.HP = 155
        self.Score = 0
        self.Nome_Player = "AAA"
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)

    def danoPlayer(self):
        if Classe.verificar_hitstun == False:
            SFX_Punch2.play()
            Classe.verificar_hitstun = True
            Classe.contador_frames_animacao = 0
            Classe.Virado = False
            Classe.direita = False
            Classe.esquerda = False
            Classe.baixo = False
            Classe.cima = False
            Classe.soco = False
            Classe.soco_para_esquerda = False
            Classe.parado = False
            Classe.HP -= 10

    def draw(self, Janela):
        if self.contador_frames_animacao + 1 >= 27:
            self.contador_frames_animacao = 0
            self.verificar_hitstun = False
            self.esta_atacando = False

        if self.esquerda:
            Janela.blit(self.Andar_Esquerda_Animacao[self.contador_frames_animacao // 5], (self.x, self.y))
            self.contador_frames_animacao += 3
        elif self.Virado:
            Janela.blit(self.Personagem_Parado_Esquerda_Animacao[self.contador_frames_animacao // 10], (self.x, self.y))
            self.contador_frames_animacao += 3
        elif self.direita:
            Janela.blit(self.Andar_Direita_Animacao[self.contador_frames_animacao // 5], (self.x, self.y))
            self.contador_frames_animacao += 3
        elif self.cima:
            Janela.blit(self.Andar_Direita_Animacao[self.contador_frames_animacao // 5], (self.x, self.y))
            self.contador_frames_animacao += 3
        elif self.baixo:
            Janela.blit(self.Andar_Direita_Animacao[self.contador_frames_animacao // 5], (self.x, self.y))
            self.contador_frames_animacao += 3
        elif self.soco:
            Janela.blit(self.Soco_Animacao[self.contador_frames_animacao // 7], (self.x, self.y))
            self.contador_frames_animacao += 3
        elif self.soco_para_esquerda:
            Janela.blit(self.Soco_Esquerda_Animacao[self.contador_frames_animacao // 7], (self.x, self.y))
            self.contador_frames_animacao += 3
        elif self.parado:
            Janela.blit(self.Personagem_Parado_Direita_Animacao[self.contador_frames_animacao//10], (self.x, self.y))
            self.contador_frames_animacao += 2
        elif self.verificar_hitstun == True:
            if self.verificador_de_lado_esquerdo==True:
                Janela.blit(self.Personagem_Dano_Direita_Animacao[self.contador_frames_animacao // 9], (self.x, self.y))
                self.contador_frames_animacao += 1
            elif self.verificador_de_lado_esquerdo == False:
                Janela.blit(self.Personagem_Dano_Esquerda_Animacao[self.contador_frames_animacao // 9], (self.x, self.y))
                self.contador_frames_animacao += 1
        else:
            if self.direita:
                Janela.blit(self.Andar_Direita_Animacao[0], (self.x, self.y))
            else:
                Janela.blit(self.Andar_Direita_Animacao[0], (self.x, self.y))
        self.hitbox = (self.x + 17, self.y + 11, 70, 90)

class Player2(object):
    Andar_Direita_Animacao_Player_2 = [pygame.image.load('images/Personagem2_Sprites/Personagem2_R__Andando_0.png'),
                     pygame.image.load('images/Personagem2_Sprites/Personagem2_R__Andando_1.png'),
                     pygame.image.load('images/Personagem2_Sprites/Personagem2_R__Andando_1.png'),
                     pygame.image.load('images/Personagem2_Sprites/Personagem2_R__Andando_2.png'),
                     pygame.image.load('images/Personagem2_Sprites/Personagem2_R__Andando_3.png'),
                     pygame.image.load('images/Personagem2_Sprites/Personagem2_R__Andando_4.png'),
                     pygame.image.load('images/Personagem2_Sprites/Personagem2_R__Andando_5.png'),
                     pygame.image.load('images/Personagem2_Sprites/Personagem2_R__Andando_6.png')]
    Andar_Esquerda_Animacao_Player_2 = [pygame.image.load('images/Personagem2_Sprites/Personagem2_L__Andando_0.png'),
                      pygame.image.load('images/Personagem2_Sprites/Personagem2_L__Andando_1.png'),
                      pygame.image.load('images/Personagem2_Sprites/Personagem2_L__Andando_2.png'),
                      pygame.image.load('images/Personagem2_Sprites/Personagem2_L__Andando_3.png'),
                      pygame.image.load('images/Personagem2_Sprites/Personagem2_L__Andando_4.png'),
                      pygame.image.load('images/Personagem2_Sprites/Personagem2_L__Andando_5.png'),
                      pygame.image.load('images/Personagem2_Sprites/Personagem2_L__Andando_6.png')]
    Soco_Animacao_Player2 = [pygame.image.load('images/Personagem2_Sprites/Personagem2_R__Soco_0.png'),
             pygame.image.load('images/Personagem2_Sprites/Personagem2_R__Soco_1.png'),
             pygame.image.load('images/Personagem2_Sprites/Personagem2_R__Soco_2.png'),
             pygame.image.load('images/Personagem2_Sprites/Personagem2_R__Soco_3.png'),
             pygame.image.load('images/Personagem2_Sprites/Personagem2_R__Soco_4.png')
             ]
    Soco_Esquerda_Player2 = [pygame.image.load('images/Personagem2_Sprites/Personagem2_L__Soco_0.png'),
                   pygame.image.load('images/Personagem2_Sprites/Personagem2_L__Soco_1.png'),
                   pygame.image.load('images/Personagem2_Sprites/Personagem2_L__Soco_2.png'),
                   pygame.image.load('images/Personagem2_Sprites/Personagem2_L__Soco_3.png'),
                   pygame.image.load('images/Personagem2_Sprites/Personagem2_L__Soco_4.png')
                   ]
    Personagem_Parado_Esquerda_Animacao2 = [pygame.image.load('images/Personagem2_Sprites/Personagem2_L__Parado_0.png'),
               pygame.image.load('images/Personagem2_Sprites/Personagem2_L__Parado_1.png'),
               pygame.image.load('images/Personagem2_Sprites/Personagem2_L__Parado_2.png'),
               pygame.image.load('images/Personagem2_Sprites/Personagem2_L__Parado_3.png'),
               pygame.image.load('images/Personagem2_Sprites/Personagem2_L__Parado_4.png'),
               pygame.image.load('images/Personagem2_Sprites/Personagem2_L__Parado_5.png'),
               ]
    Personagem_Parado_Direita_Animacao2 = [pygame.image.load('images/Personagem2_Sprites/Personagem2_R__Parado_0.png'),
             pygame.image.load('images/Personagem2_Sprites/Personagem2_R__Parado_1.png'),
             pygame.image.load('images/Personagem2_Sprites/Personagem2_R__Parado_2.png'),
             pygame.image.load('images/Personagem2_Sprites/Personagem2_R__Parado_3.png'),
             pygame.image.load('images/Personagem2_Sprites/Personagem2_R__Parado_4.png'),
             pygame.image.load('images/Personagem2_Sprites/Personagem2_R__Parado_5.png'),
             ]
    Dano_Personagem_Player2 = [pygame.image.load('images/Personagem2_Sprites/Personagem2_R__Dano_0.png'),
             pygame.image.load('images/Personagem2_Sprites/Personagem2_R__Dano_1.png'),
             pygame.image.load('images/Personagem2_Sprites/Personagem2_R__Dano_2.png'),
             ]
    Dano_Esquerda_Personagem_Player2 = [pygame.image.load('images/Personagem2_Sprites/Personagem2_L__Dano_0.png'),
                   pygame.image.load('images/Personagem2_Sprites/Personagem2_L__Dano_1.png'),
                   pygame.image.load('images/Personagem2_Sprites/Personagem2_L__Dano_2.png'),
                   ]
    Personagem_Parado_Esquerda_Animacao2 = [pygame.image.load('images/Personagem2_Sprites/Personagem2_L__Parado_0.png'),
             pygame.image.load('images/Personagem2_Sprites/Personagem2_L__Parado_1.png'),
             pygame.image.load('images/Personagem2_Sprites/Personagem2_L__Parado_2.png'),
             pygame.image.load('images/Personagem2_Sprites/Personagem2_L__Parado_3.png'),
             pygame.image.load('images/Personagem2_Sprites/Personagem2_L__Parado_4.png'),
             pygame.image.load('images/Personagem2_Sprites/Personagem2_L__Parado_5.png')]

    def __init__(self, x, y, largura, altura, velocidade_Personagem_X, velocidade_Personagem_Y):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.velocidade_Personagem_X = velocidade_Personagem_X
        self.velocidade_Personagem_Y = velocidade_Personagem_Y
        self.esquerda = False
        self.verificador_de_lado_esquerdo=True
        self.direita = False
        self.baixo = False
        self.cima = False
        self.soco = False
        self.parado = False
        self.Virado=False
        self.soco_para_esquerda=False
        self.verificar_hitstun = False
        self.esta_atacando = False
        self.contador_frames_animacao = 0
        self.contador_de_passos = 0
        self.HP = 155
        self.Score = 0
        self.Nome_Player = "PL2"
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        
    def danoPlayer2(self):
        if Classe2.verificar_hitstun == False:
            SFX_Punch2.play()
            Classe2.verificar_hitstun = True
            Classe2.contador_frames_animacao = 0
            Classe2.Virado = False
            Classe2.direita = False
            Classe2.esquerda = False
            Classe2.baixo = False
            Classe2.cima = False
            Classe2.soco = False
            Classe2.soco_para_esquerda = False
            Classe2.parado = False
            Classe2.HP -= 10

    def draw(self, Janela):
        if self.contador_frames_animacao + 1 >= 27:
            self.contador_frames_animacao = 0
            self.verificar_hitstun = False
            self.esta_atacando = False
        if self.esquerda:
            Janela.blit(self.Andar_Esquerda_Animacao_Player_2[self.contador_frames_animacao // 5], (self.x, self.y))
            self.contador_frames_animacao += 3
        elif self.Virado:
            Janela.blit(self.Personagem_Parado_Esquerda_Animacao2[self.contador_frames_animacao // 10], (self.x, self.y))
            self.contador_frames_animacao += 3
        elif self.direita:
            Janela.blit(self.Andar_Direita_Animacao_Player_2[self.contador_frames_animacao // 5], (self.x, self.y))
            self.contador_frames_animacao += 3
        elif self.cima:
            Janela.blit(self.Andar_Direita_Animacao_Player_2[self.contador_frames_animacao // 5], (self.x, self.y))
            self.contador_frames_animacao += 3
        elif self.baixo:
            Janela.blit(self.Andar_Direita_Animacao_Player_2[self.contador_frames_animacao // 5], (self.x, self.y))
            self.contador_frames_animacao += 3
        elif self.soco:
            Janela.blit(self.Soco_Animacao_Player2[self.contador_frames_animacao // 7], (self.x, self.y))
            self.contador_frames_animacao += 3
        elif self.soco_para_esquerda:
            Janela.blit(self.Soco_Esquerda_Player2[self.contador_frames_animacao // 7], (self.x, self.y))
            self.contador_frames_animacao += 3
        elif self.parado:
            Janela.blit(self.Personagem_Parado_Direita_Animacao2[self.contador_frames_animacao//10], (self.x, self.y))
            self.contador_frames_animacao += 3
        elif self.verificar_hitstun == True:
            if self.verificador_de_lado_esquerdo==True:
                Janela.blit(self.Dano_Personagem_Player2[self.contador_frames_animacao // 9], (self.x, self.y))
                self.contador_frames_animacao += 1
            elif self.verificador_de_lado_esquerdo == False:
                Janela.blit(self.Dano_Esquerda_Personagem_Player2[self.contador_frames_animacao // 9], (self.x, self.y))
                self.contador_frames_animacao += 1
        else:
            if self.direita:
                Janela.blit(self.Andar_Direita_Animacao_Player_2[0], (self.x, self.y))
            else:
                Janela.blit(self.Andar_Direita_Animacao_Player_2[0], (self.x, self.y))
        self.hitbox = (self.x + 17, self.y + 11, 70, 90)

class Classe_Soco_Player1(object):
    def __init__(self, x, y, raio, cor, verificador_de_direcao):
        self.x = x + 60
        self.y = y + 5
        self.raio = raio
        self.cor = cor
        self.verificador_de_direcao = verificador_de_direcao
        self.vel = 0 * verificador_de_direcao
        self.mostrar_hitbox=False
        if Classe.verificador_de_lado_esquerdo == False:
            self.x = self.x + (-73)
            self.y = self.y + (-5)
 
    def draw(self, Janela):
        if self.mostrar_hitbox:
            pygame.draw.circle(Janela, self.cor, (self.x, self.y), self.raio)

class Classe_Soco_Player2(object):
    def __init__(self, x, y, raio, cor, verificador_de_direcao):

        self.x = x + 60
        self.y = y + 5
        self.raio = raio
        self.cor = cor
        self.verificador_de_direcao = verificador_de_direcao
        self.vel = 0 * verificador_de_direcao
        self.mostrar_hitbox=False

        if Classe2.verificador_de_lado_esquerdo == False:
            self.x = self.x + (-73)
            self.y = self.y + (-5)

    def draw(self, Janela):
      if self.mostrar_hitbox:
        pygame.draw.circle(Janela, self.cor, (self.x, self.y), self.raio)

class Classe_Dano_Inimigo(object):
    def __init__(self, x, y, raio, cor, verificador_de_direcao):
        self.x = x
        self.y = y
        self.raio = raio
        self.cor = cor
        self.verificador_de_direcao = verificador_de_direcao
        self.vel = 0 * verificador_de_direcao
        self.mostrar_hitbox=True

    def draw(self, Janela):
      if self.mostrar_hitbox:
        pygame.draw.circle(Janela, self.cor, (self.x, self.y), self.raio)

class InimigoBase(object):
    Ataque_Animacao =  [pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_R__Atacando_0.png'), pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_R__Atacando_1.png'),
                pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_R__Atacando_2.png'), pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_R__Atacando_3.png'),
                pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_R__Atacando_4.png'), pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_R__Atacando_5.png'),
                pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_R__Atacando_6.png'),pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_R__Atacando_7.png'), pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_R__Atacando_8.png'),
                pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_R__Atacando_9.png')]
    Ataque_Esquerda_Animacao =  [pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_L__Atacando_0.png'), pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_L__Atacando_1.png'),
                pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_L__Atacando_2.png'), pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_L__Atacando_3.png'),
                pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_L__Atacando_4.png'), pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_L__Atacando_5.png'),
                pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_L__Atacando_6.png'),pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_L__Atacando_7.png'), pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_L__Atacando_8.png'),
                pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_L__Atacando_9.png')]
    Andar_Direita_Animacao = [pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_R__Andando_0.png'), pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_R__Andando_1.png'),
              pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_R__Andando_2.png'), pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_R__Andando_3.png'),
              pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_R__Andando_4.png'), pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_R__Andando_5.png'),
              pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_R__Andando_6.png')]
    Andar_Esquerda_Animacao = [pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_L__Andando_0.png'), pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_L__Andando_1.png'),
                pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_L__Andando_2.png'), pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_L__Andando_3.png'),
                pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_L__Andando_4.png'), pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_L__Andando_5.png'),
                pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_L__Andando_6.png')]
    Parado_Direita = [pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_R__Idle_0.png'),
                  pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_R__Idle_1.png'),
                  pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_R__Idle_2.png'),
                  pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_R__Idle_3.png')]
    Parado_Esquerda = [pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_L__Idle_0.png'),
                  pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_L__Idle_1.png'),
                  pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_L__Idle_2.png'),
                  pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_L__Idle_2.png'),
                  pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_L__Idle_3.png')]
    Personagem_Dano_Direita_Animacao = [pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_R__Dano_0.png'),
              pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_R__Dano_1.png'),
              pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_R__Dano_2.png'),
              pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_R__Dano_3.png'),
              pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_R__Dano_4.png')]
    Dano_Esquerda = [pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_L__Dano_0.png'),
              pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_L__Dano_1.png'),
              pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_L__Dano_2.png'),
              pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_L__Dano_3.png'),
              pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_L__Dano_4.png')]

    def __init__(self, x, y, largura, altura):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.contador_de_frames_animacao = 0
        self.vel = 3
        self.hitbox = (self.x + 17, self.y + 2)
        self.HP = 10
        self.visible = True
        self.aleatorio = random.randint (0,3)
        self.verificar_hitstun = 0
        self.atacando=False
        self.esquerda=True
        self.direita=False
        self.Parado = True
        self.andando = False
        self.hitstun = False
        self.gerar_soco = []
        self.timer = 0
        self.velX = 0

    def draw(self , win):
     if Classe.contador_de_passos >=10 or Classe2.contador_de_passos >=10:
        Classe.parartela=True
        self.move ()
        if self.visible:
            if self.contador_de_frames_animacao + 1 >= 27:
                self.contador_de_frames_animacao = 0
            if self.Parado == True:
                if self.direita == True:
                    win.blit(self.Parado_Direita[self.contador_de_frames_animacao // 7], (self.x, self.y))
                    self.contador_de_frames_animacao += 3
                elif self.esquerda == True:
                    win.blit(self.Parado_Esquerda[self.contador_de_frames_animacao // 7], (self.x, self.y))
                    self.contador_de_frames_animacao += 3
            if self.andando == True and self.atacando == False:
                if self.direita == True:
                    win.blit(self.Andar_Direita_Animacao[self.contador_de_frames_animacao // 7], (self.x, self.y))
                    self.contador_de_frames_animacao += 3
                elif self.esquerda == True:
                    win.blit(self.Andar_Esquerda_Animacao[self.contador_de_frames_animacao // 7], (self.x, self.y))
                    self.contador_de_frames_animacao += 3
            if self.hitstun == True:
                if self.direita == True:
                    win.blit(self.Personagem_Dano_Direita_Animacao[self.contador_de_frames_animacao // 6], (self.x, self.y))
                    self.contador_de_frames_animacao += 3
                elif self.esquerda == True:
                    win.blit(self.Dano_Esquerda[self.contador_de_frames_animacao // 6], (self.x, self.y))
                    self.contador_de_frames_animacao += 3
            if self.atacando == True:
                if self.direita == True:
                    win.blit(self.Ataque_Animacao[self.contador_de_frames_animacao // 3], (self.x, self.y))
                    self.contador_de_frames_animacao += 3
                elif self.esquerda == True:
                    win.blit(self.Ataque_Esquerda_Animacao[self.contador_de_frames_animacao // 3], (self.x, self.y))
                    self.contador_de_frames_animacao += 3
            pygame.draw.rect ( win , (255 , 0 , 0) , (self.hitbox[0] , self.hitbox[1] - 20 , 50 , 10) )
            pygame.draw.rect ( win , (0 , 128 , 0) , (self.hitbox[0] , self.hitbox[1] - 20 , 50 - (5 * (10 - self.HP)) , 10) )
            self.hitbox = (self.x + 17 , self.y + 2 , 31 , 57)

     if inimigo.visible==False:
         Classe.parartela = False
         Classe.contador_de_passos = 0
         Classe2.contador_de_passos = 0

    def move(self):
        if self.verificar_hitstun == 0:
            self.vel = 0
            self.Contador(27)
        if self.verificar_hitstun == 1:
            self.MoverX()
            self.MoverY()
            if self.prontoY == True and self.prontoX == True:
                self.Contador(5)
        if self.verificar_hitstun == 2:
            self.Achar_Personagem_X()
            self.Achar_Personagem_Y()
            if self.prontoX == True and self.prontoY == True:
                self.atacando = True
                self.atacar()
                self.vel = 0
                self.andando = False
                self.Parado = False
                self.Contador(60)
        if self.verificar_hitstun == 3:
            self.hitstun = True
            self.andando = False
            self.Parado = False
            self.atacando = False
            self.vel = 0
            self.Contador(13)

    def Reset_Variaveis_de_Estado(self):
        self.hitstun = False
        self.atacando = False
        self.andando = False
        self.prontoX = False
        self.prontoY = False
        self.caminhoY = 100
        self.caminhoX = 100
        self.Caminho_Y_Gerado = False
        self.Caminho_X_Gerado = False
        self.troca_verificar_hitstun = False
        self.Parado = True

    def Contador(self, tempo):
        self.timer +=1
        if self.timer >= tempo:
            self.Reset_Variaveis_de_Estado()
            self.verificar_hitstun = random.randint(0, 2)
            self.timer = 0

    def Achar_Personagem_X(self):
        self.x += self.velX
        if self.prontoX == False:
            if self.Caminho_X_Gerado == False:
                self.escolher_alvo = random.randint(0, 1)
                if self.escolher_alvo == 0:
                    self.caminhoX = Classe.x
                else:
                    self.caminhoX = Classe2.x
                self.Caminho_X_Gerado = True
            if self.x < self.caminhoX:
                self.velX = 6
                self.Parado = False
                self.andando = True
                self.esquerda = False
                self.direita = True
            if self.x > self.caminhoX:
                self.Parado = False
                self.andando = True
                self.esquerda = True
                self.direita = False
                self.velX = -6
            if self.x - 6 < self.caminhoX and self.x + 6 > self.caminhoX:
                self.caminhoX = self.x
                self.velX = 0
                self.prontoX = True
                
    def Achar_Personagem_Y(self):
        self.y += self.vel
        if self.prontoY == False:
            if self.Caminho_Y_Gerado == False:
                self.escolher_alvo = random.randint(0, 1)
                if self.escolher_alvo == 0:
                    self.caminhoY = Classe.y
                else:
                    self.caminhoY = Classe2.y
                self.Caminho_Y_Gerado = True
            if self.y < self.caminhoY:
                self.vel = 3
                self.andando = True
            if self.y > self.caminhoY:
                self.vel = -3
                self.andando = True
            if self.y - 5 < self.caminhoY and self.y + 5 > self.caminhoY:
                self.caminhoY = self.y
                self.vel = 0
                self.prontoY = True

    def MoverX(self):
        self.x += self.velX

        if self.prontoX == False:
            if self.Caminho_X_Gerado == False:
                while self.caminhoX % 3 != 0:
                    self.caminhoX = random.randint(50, 540)
                self.Caminho_X_Gerado = True
            if self.x < self.caminhoX:
                self.velX = 6
                self.Parado = False
                self.andando = True
                self.esquerda = False
                self.direita = True
            if self.x > self.caminhoX:
                self.Parado = False
                self.andando = True
                self.esquerda = True
                self.direita = False
                self.velX = -6
            if self.x - 6 < self.caminhoX  and self.x + 6 > self.caminhoX :
                self.caminhoX  = self.x
                self.velX = 0
                self.prontoX = True

    def MoverY(self):
        self.y +=self.vel
        if self.prontoY == False:
            if self.Caminho_Y_Gerado == False:
                while self.caminhoY % 3 != 0:
                    self.caminhoY = random.randint(209, 380)
                self.Caminho_Y_Gerado = True
            if self.y < self.caminhoY:
                self.vel = 3
            if self.y > self.caminhoY:
                self.vel =-3
            if self.y - 5 < self.caminhoY and self.y + 5 > self.caminhoY:
                self.caminhoY = self.y
                self.vel = 0
                self.prontoY = True

    def Colisao_Soco_Inimigo(self):
        for soco in self.gerar_soco:
            if (soco.x + soco.raio >= Classe.hitbox[0] and soco.x + soco.raio <= Classe.hitbox[0] + 30):
                if soco.y >= Classe.hitbox[1] and soco.y <= Classe.hitbox[1] + 40:
                    Classe.danoPlayer()
                    self.gerar_soco.pop(self.gerar_soco.index(soco))
            elif (soco.x + soco.raio >= Classe2.hitbox[0] and soco.x + soco.raio <= Classe2.hitbox[0] + 30):
                if soco.y >= Classe2.hitbox[1] and soco.y <= Classe2.hitbox[1] + 40:
                    Classe2.danoPlayer2()
                    self.gerar_soco.pop(self.gerar_soco.index(soco))
            else:
                self.gerar_soco.pop(self.gerar_soco.index(soco))

    def atacar(self):
        if self.atacando==True:
            self.Colisao_Soco_Inimigo()
            if self.esquerda == True:
                verificador_de_direcao3 = -1
            else:
                verificador_de_direcao3 = 1
            if len(self.gerar_soco) <= 1:
                self.gerar_soco.append (Classe_Dano_Inimigo ( round ( inimigo.x + inimigo.largura // 2 )
                ,round ( inimigo.y + inimigo.altura // 2 ) , 6 ,(0 , 0 , 0),verificador_de_direcao3))

            else:
                self.atacando=False
                self.Reset_Variaveis_de_Estado()



    def Hit_Inimigo(self, personagem_hit):
        global showPoints
        global Score
        global InimigosVencidos
        if self.HP >=0:
            self.contador_de_frames_animacao = 0
            SFX_Punch1.play()
            if self.HP > 0:
                self.timer = 0
                self.HP -= 1
                self.verificar_hitstun = 3
                self.vel = 3
                self.atacando = False
            else:
                if personagem_hit == "J1":
                    Classe.Score += 500

                else:
                    Classe2.Score += 500
                self.visible = False
                InimigosVencidos += 1
                self.HP -= 1

class Boss(object):
    Andar_Direita_Animacao = [pygame.image.load('images/Inimigo/Boss/Boss_R_Ataque_0.png'),
              pygame.image.load('images/Inimigo/Boss/Boss_R_Ataque_1.png'),
              pygame.image.load('images/Inimigo/Boss/Boss_R_Ataque_2.png'),
              pygame.image.load('images/Inimigo/Boss/Boss_R_Ataque_3.png'),]
    Andar_Esquerda_Animacao = [pygame.image.load('images/Inimigo/Boss/Boss_L_Ataque_0.png'),
              pygame.image.load('images/Inimigo/Boss/Boss_L_Ataque_1.png'),
              pygame.image.load('images/Inimigo/Boss/Boss_L_Ataque_2.png'),
              pygame.image.load('images/Inimigo/Boss/Boss_L_Ataque_3.png'),]
    IdleLeft = [pygame.image.load('images/Inimigo/Boss/Boss_L_Risada_0.png'),
                 pygame.image.load('images/Inimigo/Boss/Boss_L_Risada_1.png'),
                 pygame.image.load('images/Inimigo/Boss/Boss_L_Risada_2.png'),
                 pygame.image.load('images/Inimigo/Boss/Boss_L_Risada_3.png'),]
    IdleRight = [pygame.image.load('images/Inimigo/Boss/Boss_R_Risada_0.png'),
                 pygame.image.load('images/Inimigo/Boss/Boss_R_Risada_1.png'),
                 pygame.image.load('images/Inimigo/Boss/Boss_R_Risada_2.png'),
                 pygame.image.load('images/Inimigo/Boss/Boss_R_Risada_3.png'),]
    PrepararEsq = [pygame.image.load('images/Inimigo/Boss/Boss_L_Andando_1.png'),
                   pygame.image.load('images/Inimigo/Boss/Boss_L_Andando_2.png'),
                   pygame.image.load('images/Inimigo/Boss/Boss_L_Andando_3.png'),]
    PrepararDir = [pygame.image.load('images/Inimigo/Boss/Boss_R_Andando_1.png'),
                   pygame.image.load('images/Inimigo/Boss/Boss_R_Andando_2.png'),
                   pygame.image.load('images/Inimigo/Boss/Boss_R_Andando_3.png'),]
    DeathAnimDir = [pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_R__Morte_00.png'), pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_R__Morte_01.png'),
              pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_R__Morte_02.png'), pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_R__Morte_03.png'), pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_R__Morte_04.png'),
                 pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_R__Morte_05.png'),pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_R__Morte_06.png'),
                 pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_R__Morte_07.png'),pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_R__Morte_08.png'),
                 pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_R__Morte_09.png')]
    DeathAnimEsq = [pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_L__Morte_00.png'), pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_L__Morte_01.png'),
              pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_L__Morte_02.png'), pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_L__Morte_03.png'), pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_L__Morte_04.png'),
                 pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_L__Morte_05.png'),pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_L__Morte_06.png'),
                 pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_L__Morte_07.png'),pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_L__Morte_08.png'),
                 pygame.image.load('images/Inimigo/Inimigo_1/Inimigo_L__Morte_09.png')]

    def __init__(self, x, y, largura, altura):
        self.x = x
        self.y = y
        self.largura = largura
        self.altura = altura
        self.HP = 10
        self.verificar_hitstun = 1
        self.lado = 1
        self.timer = 0
        self.visible = True
        self.idle = True
        self.direita = False
        self.esquerda = False
        self.verificador_de_esquerda = False
        self.contador_de_frames_animacao = 0
        self.verificador_de_direcao = random.randint (209,300)
        self.hitbox = (self.x + 17, self.y + 2)


    def draw(self, Janela):
        global SlowMotion
        if self.visible == True:
            self.hitbox = (self.x + 20, self.y + 20, 31, 57)
            self.ataque()
            if self.contador_de_frames_animacao + 1 >= 27:
                self.contador_de_frames_animacao = 0
            if self.idle == True:
                if self.lado == 1:
                    Janela.blit(self.IdleLeft[self.contador_de_frames_animacao // 10], (self.x, self.y))
                    self.contador_de_frames_animacao += 3
                else:
                    Janela.blit(self.IdleRight[self.contador_de_frames_animacao // 10], (self.x, self.y))
                    self.contador_de_frames_animacao += 3
            if self.esquerda == True:
                Janela.blit(self.Andar_Direita_Animacao[self.contador_de_frames_animacao // 8], (self.x, self.y))
                self.contador_de_frames_animacao += 5
            if self.direita == True:
                Janela.blit(self.Andar_Esquerda_Animacao[self.contador_de_frames_animacao // 8], (self.x, self.y))
                self.contador_de_frames_animacao += 5
            if self.verificador_de_esquerda == True:
                if self.lado == 1:
                    Janela.blit(self.PrepararEsq[self.contador_de_frames_animacao // 10], (self.x, self.y))
                    self.contador_de_frames_animacao += 3
                else:
                    Janela.blit(self.PrepararDir[self.contador_de_frames_animacao // 10], (self.x, self.y))
                    self.contador_de_frames_animacao += 3

            if self.verificar_hitstun == 6:
                if self.lado == 1:
                    Janela.blit(self.DeathAnimEsq[self.contador_de_frames_animacao // 3], (self.x, self.y))
                    self.contador_de_frames_animacao += 1
                else:
                    Janela.blit(self.DeathAnimDir[self.contador_de_frames_animacao // 3], (self.x, self.y))
                    self.contador_de_frames_animacao += 1

                if self.contador_de_frames_animacao >= 25:
                    self.visible = False
                    SlowMotion = False

    def ataque(self):
        self.timer+=1
        if self.verificar_hitstun == 1:
            self.verificador_de_esquerda = False
            self.idle = True
            if self.timer >= 30:
                self.verificador_de_direcao = random.randint(209, 280)
                self.timer = 0
                self.contador_de_frames_animacao = 0
                self.verificar_hitstun = 3


        if self.verificar_hitstun == 2:
            self.Personagem_Parado_Direita_Animacaoge()
            if self.lado == 1:
                if self.x >= 10 and self.verificar_hitstun == 2:
                    self.x += -10
                    if self.x <= 10 and self.verificar_hitstun == 2:
                        SFX_KobraLaugh.play()
                        self.verificar_hitstun = 1
                        self.lado = 2
                        self.timer = 0
                        self.contador_de_frames_animacao = 0

            else:
                if self.x <= 500 and self.verificar_hitstun == 2:
                    self.x += 10
                    if self.x >= 500 and self.verificar_hitstun == 2:
                        SFX_KobraLaugh.play()
                        self.verificar_hitstun = 1
                        self.lado = 1
                        self.timer = 0
                        self.contador_de_frames_animacao = 0

        if self.verificar_hitstun == 3:
            self.verificador_de_esquerda = True
            self.idle = False
            if self.y > self.verificador_de_direcao:
                self.y -= 1
            elif self.y < self.verificador_de_direcao:
                self.y += 1
            elif self.y == self.verificador_de_direcao:
                self.verificar_hitstun = 2
                SFX_Attack.play()


        if self.verificar_hitstun == 2:
            self.idle = False
            self.verificador_de_esquerda = False
            if self.lado == 1:
                self.direita = True
                self.esquerda = False
            else:
                self.esquerda = True
                self.direita = False
        else:
            self.direita= False
            self.esquerda = False

    def Hit_Inimigo(self, personagem_hit):
        if self.HP >= 0:
            global Score
            global SlowMotion
            SFX_Punch1.play()
            if self.HP > 0:
                self.HP -= 1
            else:
                self.HP -= 1
                SFX_Death.play()
                SlowMotion = True
                self.esquerda = False
                self.direita = False
                self.verificador_de_esquerda = False
                self.idle = False
                self.verificar_hitstun = 6
                if personagem_hit == "J1":
                    Classe.Score += 500
                else:
                    Classe2.Score += 500

    def Personagem_Parado_Direita_Animacaoge(self):
        if self.x <= Classe.x+28 and self.x+100 >= Classe.x+ 64:
            if self.y+66 <= Classe.y+23 and self.y+157 >= Classe.y+68:
                Classe.danoPlayer()

        if self.x <= Classe2.x+28 and self.x+100 >= Classe2.x+ 64:
            if self.y+66 <= Classe2.y+23 and self.y+157 >= Classe2.y+68:
                Classe2.danoPlayer2()

Classe = Player(30, 250, 64, 64, 64, 64, 64)
Classe2 = Player2(40, 300, 64, 64, 64, 64)
inimigo = InimigoBase(-10, 410, 64, 64)
inimigo2 = InimigoBase(660, 410, 64, 64)
Kobra = Boss(400, 230, 64, 64)

Gerador_Soco_Player1 = []
Gerador_Soco_Player2 = []
gerar_soco=[]

Largura, Altura = 640, 480
HW, HH = Largura / 2, Altura / 2
Area = Largura * Altura
Nome_da_Janela = "FLYING FIST"
pygame.init()
clock = pygame.time.Clock()
Janela = pygame.display.set_mode((Largura, Altura),)
pygame.display.set_caption(Nome_da_Janela)
Controlador_Jogo = "Tela_de_Titulo"
Score = 0
Timer = 60
Nome_do_player = ("RIC")
InimigosVencidos = 0

Leaderboard = [
    {'Nome': ("AAA"), 'Pontos': 3000},
    {'Nome': ("AAA"), 'Pontos': 4000},
    {'Nome': ("AAA"), 'Pontos': 5000},
    {'Nome': ("AAA"), 'Pontos': 2000},
    {'Nome': ("AAA"), 'Pontos': 300},]

showPoints = False
primeira_fase = 0

def showPointFunc():
    compressao_save.compressao()
    pygame.mixer.fadeout(3000)
    pygame.mixer.music.set_endevent(SONG_END)
    pygame.mixer.music.load('Musica_SFX/Fanfare.mp3')
    pygame.mixer.music.play(1)

def mostrarPlacar(Pontos):
    resultado = ""
    for key in Pontos[:8]:
        linha = "Nome : "
        nome = (key['Nome'])
        pontos = (key['Pontos'])
        linha += nome
        linha += " Pontos: "
        linha += str(pontos)
        resultado += linha
        resultado += "\n"

    return resultado

if os.path.exists("top_scores") == True:
    pass
else:
    Load_Top_Scores = Leaderboard
    pickle.dump(Load_Top_Scores, open("top_scores", "wb"))
    Load_Top_Scores = pickle.load(open("top_scores", "rb"))
    Load_Top_Scores.sort(key=itemgetter('Pontos'), reverse=True)
Load_Top_Scores = pickle.load(open("top_scores", "rb"))
for key in Load_Top_Scores:
    print(key)
textoPlacar = mostrarPlacar(Load_Top_Scores)
compressao_save.compressao()

Background_Fase = pygame.image.load("images/Background_Fase.png").convert_alpha()
Background_Fase_0 = pygame.image.load("images/Background_Fase_0.png").convert()
Background_Fase2 = pygame.image.load("images/Background_Fase2.png").convert_alpha()
Background_Fase2_0 = pygame.image.load("images/Background_Fase2_0.png").convert()
Background_Tela_Inicial = pygame.image.load("images/Tela_Inicial/Tela_de_Titulo.png").convert()
Personagem_HUD = pygame.image.load("images/Personagem_Vida.png").convert_alpha()
Personagem_HUD2 = pygame.image.load("images/Personagem2_Vida.png").convert_alpha()
Go = pygame.image.load("images/Go.png").convert_alpha()
Start = False

Background_Largura, Background_Altura = Background_Fase.get_rect().size

Fase_Largura = Background_Largura * 10
Background_Fase_Posicao = 0
Background_Fase_Posicao_0 = 0
Posicao_inicial_paralaxe = HW+150

Largura, Altura = 640, 448
HW, HH = Largura / 2, Altura / 2
Area = Largura * Altura
Nome_da_Janela = "FLYING FIST"

run = True

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
SFX_KobraLaugh = pygame.mixer.Sound('Musica_SFX/SFX/Voice_KobraLaugh.wav')
SFX_Attack = pygame.mixer.Sound('Musica_SFX/SFX/Attack_2.wav')
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
    global InimigosVencidos
    global showPoints
    if Controlador_Jogo == "Tela_de_Titulo":
        Janela.blit(Background_Tela_Inicial, (0, -10))
        Tela_Inicial.Press_Start.blit(Janela, (110, 320))
        Tela_Inicial.Tela_de_titulo_animacao.blit(Janela, (0, -10))
        pygame.display.update()
    if Controlador_Jogo == "Tela_da_Fase_1":
        Janela.blit(Background_Fase_0, (rel_x2, 0))
        Janela.blit(Background_Fase, (rel_x, 0), )
        Janela.blit(Background_Fase_0, (rel_x2 - Background_Largura, 0))
        Janela.blit(Background_Fase, (rel_x - Background_Largura, 0))
        if InimigosVencidos == 1:
            showPoints = True
            showPointFunc()
            InimigosVencidos = 2
        Janela.blit(Personagem_HUD, (10, 10))
        Janela.blit(Personagem_HUD2, (392, 10))
        pygame.draw.rect(Janela, (255, 255, 0), (78, 57, Classe.HP, 19), 0)
        pygame.draw.rect(Janela, (255, 255, 0), (555, 57, Classe2.HP*-1, 19), 0)
        if Classe.y >= Classe2.y:
            Classe2.draw(Janela)
            Classe.draw(Janela)
        else:
            Classe.draw(Janela)
            Classe2.draw(Janela)
        inimigo.draw(Janela)
        segundos = int((pygame.time.get_ticks() - start_ticks) / 1000)
        ptext.draw(str(Classe.Score), topleft=(190, 28), fontname="fontes/start.ttf", color=(255, 100, 0),
                   gcolor=(255, 200, 20), fontsize=19,
                   shadow=(3, 1), scolor="#000000")
        ptext.draw(str(Classe2.Score), topright=(450, 28), fontname="fontes/start.ttf", color=(255, 100, 0),
                   gcolor=(255, 200, 20), fontsize=19,
                   shadow=(3, 1), scolor="#000000")
        ptext.draw(str(Timer - segundos), center=(Largura / 2, 30), fontname="fontes/start.ttf", color=(255, 255, 255),
                   gcolor=(150, 150, 150),
                   shadow=(3, 3), scolor="#000000")
        for soco in Gerador_Soco_Player1:
            soco.draw(Janela)
        for soco_player2 in Gerador_Soco_Player2:
            soco_player2.draw(Janela)
        for soco_player2 in gerar_soco:
            soco_player2.draw(Janela)
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
    if Controlador_Jogo == "Tela_da_Fase_2":
        Janela.blit(Background_Fase2_0, (rel_x2, 0))
        Janela.blit(Background_Fase2, (rel_x, 0), )
        Janela.blit(Background_Fase2_0, (rel_x2 - Background_Largura, 0))
        Janela.blit(Background_Fase2, (rel_x - Background_Largura, 0))
        Janela.blit(Personagem_HUD, (10, 10))
        Janela.blit(Personagem_HUD2, (392, 10))
        pygame.draw.rect(Janela, (255, 255, 0), (78, 57, Classe.HP, 19), 0)
        pygame.draw.rect(Janela, (255, 255, 0), (555, 57, Classe2.HP*-1, 19), 0)
        if Classe.y >= Classe2.y:
            Classe2.draw(Janela)
            Classe.draw(Janela)
        else:
            Classe.draw(Janela)
            Classe2.draw(Janela)
        Kobra.draw(Janela)

        segundos = int((pygame.time.get_ticks() - start_ticks) / 1000)


        ptext.draw(str(Classe.Score), topleft=(190, 28), fontname="fontes/start.ttf", color=(255, 100, 0),
                   gcolor=(255, 200, 20), fontsize=19,
                   shadow=(3, 1), scolor="#000000")

        ptext.draw(str(Classe2.Score), topright=(450, 28), fontname="fontes/start.ttf", color=(255, 100, 0),
                   gcolor=(255, 200, 20), fontsize=19,
                   shadow=(3, 1), scolor="#000000")

        ptext.draw(str(Timer - segundos), center=(Largura / 2, 30), fontname="fontes/start.ttf", color=(255, 255, 255),
                   gcolor=(150, 150, 150),
                   shadow=(3, 3), scolor="#000000")

        for soco in Gerador_Soco_Player1:
            soco.draw(Janela)

        for soco_player2 in Gerador_Soco_Player2:
            soco_player2.draw(Janela)

        for soco_player2 in gerar_soco:
            soco_player2.draw(Janela)



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
    if Controlador_Jogo == "Tela_de_Cutscenes":
        if textnumber == 4:
            Cutscenes.Cutscene_2.blit(Janela, (0,0))
        if textnumber >= 6 and textnumber < 9:
            Cutscenes.Cutscene_Kobra.blit(Janela,(0,0))
            
def MovimentoPersonagem1():
    if Botao_Pressionado[pygame.K_LEFT] and Classe.x >5 and Start == False:
        if Classe.verificar_hitstun == False:
            if Classe.esta_atacando == False:
                Classe.velocidade_Personagem_X=0
                Classe.esquerda = True
                Classe.direita = False
                Classe.Virado=True
                Classe.verificador_de_lado_esquerdo = True
    if Botao_Pressionado[pygame.K_LEFT] and Classe.x > 5 and Start == False:
        if Classe.verificar_hitstun == False:
            if Classe.esta_atacando == False:
                Classe.velocidade_Personagem_X = -4
                Classe.x += Classe.velocidade_Personagem_X
                Classe.esquerda = True
                Classe.direita = False
                Classe.Virado=False
                Classe.verificador_de_lado_esquerdo = False
    elif Botao_Pressionado[pygame.K_RIGHT] and Classe.x <530 and Start == False:
        if Classe.verificar_hitstun == False:
            if Classe.esta_atacando == False:
                Classe.velocidade_Personagem_X = 4
                Classe.x += Classe.velocidade_Personagem_X
                Classe.direita = True
                Classe.esquerda = False
                Classe.Virado=False
                Classe.verificador_de_lado_esquerdo = True
    elif Botao_Pressionado[pygame.K_UP] and Classe.y > 209 and Start == False:
        if Classe.verificar_hitstun == False:
            if Classe.esta_atacando == False:
                Classe.velocidade_Personagem_Y = -4
                Classe.y += Classe.velocidade_Personagem_Y
                if Classe.verificador_de_lado_esquerdo == False:
                    Classe.esquerda = True
                    Classe.baixo = False
                else:
                    Classe.baixo = False
                    Classe.cima = True
    elif Botao_Pressionado[pygame.K_DOWN] and Classe.y <380 and Start == False:
        if Classe.verificar_hitstun == False:
            if Classe.esta_atacando == False:
                Classe.velocidade_Personagem_Y = 4
                Classe.y += Classe.velocidade_Personagem_Y
                if Classe.verificador_de_lado_esquerdo == False:
                    Classe.esquerda = True
                    Classe.baixo = False
                else:
                    Classe.baixo = True
                    Classe.cima = False
    elif Botao_Pressionado[pygame.K_x]:
        if Classe.verificar_hitstun == False:
            Classe.danoPlayer()
            Classe2.danoPlayer2()
    elif Botao_Pressionado[pygame.K_m]:
        if Classe.verificar_hitstun == False:
            if Classe.esta_atacando == False:
                Classe.contador_frames_animacao = 0
                Classe.esta_atacando = True
                SFX_Miss.play(0)
                if Classe.esquerda:
                    verificador_de_direcao = -1
                else:
                    verificador_de_direcao = 1
                if len(Gerador_Soco_Player1) < 1:
                    Gerador_Soco_Player1.append(
                        Classe_Soco_Player1(round(Classe.x + Classe.largura // 2), round(Classe.y + Classe.altura // 2), 6, (0, 0, 0),
                                    verificador_de_direcao))
                if Classe.verificador_de_lado_esquerdo==True:
                    Classe.soco = True

                if Classe.verificador_de_lado_esquerdo == False:
                    Classe.soco_para_esquerda = True
                    Classe.Virado=False
                else:
                    Classe.soco_para_esquerda=False
    else:
        if Classe.verificar_hitstun == False:
            if Classe.esta_atacando == False:
                Classe.direita = False
                Classe.esquerda = False
                Classe.baixo = False
                Classe.cima = False
                Classe.soco = False
                Classe.soco_para_esquerda=False
                Classe.parado=False
                Classe.velocidade_Personagem_Y = 0
                Classe.velocidade_Personagem_X = 0

        if Classe.velocidade_Personagem_X == 0 :
            if Classe.verificar_hitstun == False:
                if Classe.esta_atacando == False:
                    Classe.parado = True
        if Classe.verificador_de_lado_esquerdo==False:
            if Classe.verificar_hitstun == False:
                if Classe.esta_atacando == False:
                    Classe.Virado=True

def MovimentoPersonagem2():
    if Botao_Pressionado[pygame.K_a] and Classe2.x > 5 and Start == False:
        if Classe2.verificar_hitstun == False:
            if Classe2.esta_atacando == False:
                Classe2.velocidade_Personagem_X = 0
                Classe2.esquerda = True
                Classe2.direita = False
                Classe2.Virado = True
                Classe2.verificador_de_lado_esquerdo = True
    if Botao_Pressionado[pygame.K_a] and Classe2.x > 5 and Start == False:
        if Classe2.verificar_hitstun == False:
            if Classe2.esta_atacando == False:
                Classe2.velocidade_Personagem_X = -4
                Classe2.x += Classe2.velocidade_Personagem_X
                Classe2.esquerda = True
                Classe2.direita = False
                Classe2.Virado = False
                Classe2.verificador_de_lado_esquerdo = False
    elif Botao_Pressionado[pygame.K_d] and Classe2.x < 530 and Start == False:
        if Classe2.verificar_hitstun == False:
            if Classe2.esta_atacando == False:
                Classe2.velocidade_Personagem_X = 4
                Classe2.x += Classe2.velocidade_Personagem_X
                Classe2.direita = True
                Classe2.esquerda = False
                Classe2.Virado = False
                Classe2.verificador_de_lado_esquerdo = True
    elif Botao_Pressionado[pygame.K_w] and Classe2.y > 209 and Start == False:
        if Classe2.verificar_hitstun == False:
            if Classe2.esta_atacando == False:
                Classe2.velocidade_Personagem_Y = -4
                Classe2.y += Classe2.velocidade_Personagem_Y
                if Classe2.verificador_de_lado_esquerdo == False:
                    Classe2.esquerda = True
                    Classe2.baixo = False
                else:
                    Classe2.baixo = False
                    Classe2.cima = True
    elif Botao_Pressionado[pygame.K_s] and Classe2.y < 380 and Start == False:
        if Classe2.verificar_hitstun == False:
            if Classe2.esta_atacando == False:
                Classe2.velocidade_Personagem_Y = 4
                Classe2.y += Classe2.velocidade_Personagem_Y
                if Classe2.verificador_de_lado_esquerdo == False:
                    Classe2.esquerda = True
                    Classe2.baixo = False
                else:
                    Classe2.baixo = True
                    Classe2.cima = False
    elif Botao_Pressionado[pygame.K_i]:
        if Classe2.verificar_hitstun == False:
            if Classe2.esta_atacando == False:
                Classe2.contador_frames_animacao = 0
                Classe2.esta_atacando = True
                SFX_Miss.play(0)
                if Classe2.esquerda:
                    verificador_de_direcao2 = -1
                else:
                    verificador_de_direcao2 = 1
                if len(Gerador_Soco_Player2) < 1:
                    Gerador_Soco_Player2.append(
                        Classe_Soco_Player2(round(Classe2.x + Classe2.largura // 2), round(Classe2.y + Classe2.altura // 2), 6,
                                     (0, 0, 0),
                                     verificador_de_direcao2))
                if Classe2.verificador_de_lado_esquerdo == True:
                    Classe2.soco = True

                if Classe2.verificador_de_lado_esquerdo == False:
                    Classe2.soco_para_esquerda = True
                    Classe2.Virado = False
                else:
                    Classe2.soco_para_esquerda = False
    else:
        if Classe2.verificar_hitstun == False:
            if Classe2.esta_atacando == False:
                Classe2.direita = False
                Classe2.esquerda = False
                Classe2.baixo = False
                Classe2.cima = False
                Classe2.soco = False
                Classe2.soco_para_esquerda = False
                Classe2.parado = False
                Classe2.velocidade_Personagem_Y = 0
                Classe2.velocidade_Personagem_X = 0
        if Classe2.velocidade_Personagem_X == 0:
            if Classe2.verificar_hitstun == False:
                if Classe2.esta_atacando == False:
                    Classe2.parado = True
        if Classe2.verificador_de_lado_esquerdo == False:
            if Classe2.verificar_hitstun == False:
                if Classe2.esta_atacando == False:
                    Classe2.Virado = True

def Colisao_Soco_Personagem1():
    for soco in Gerador_Soco_Player1:
        if (soco.x + soco.raio >= inimigo.x+26 and soco.x + soco.raio <= inimigo.x+60):
            if soco.y >= inimigo.y+21 and soco.y <= inimigo.y+69:
                inimigo.Hit_Inimigo("J1")
                Gerador_Soco_Player1.pop(Gerador_Soco_Player1.index(soco))
        elif (soco.x + soco.raio >= inimigo2.x+26 and soco.x + soco.raio <= inimigo2.x+60):
            if soco.y >= inimigo2.y+21 and soco.y <= inimigo2.y+69:
                inimigo2.Hit_Inimigo("J1")
                Gerador_Soco_Player1.pop(Gerador_Soco_Player1.index(soco))
        elif (soco.x + soco.raio >= Kobra.x+29 and soco.x + soco.raio <= Kobra.x+66):
            if soco.y >= Kobra.y+54 and soco.y <= Kobra.y+146:
                Kobra.Hit_Inimigo("J1")
                Gerador_Soco_Player1.pop(Gerador_Soco_Player1.index(soco))
        else:
            Gerador_Soco_Player1.pop(Gerador_Soco_Player1.index(soco))

def Colisao_Soco_Personagem2():
    for soco in Gerador_Soco_Player2:
        if (soco.x + soco.raio >=  inimigo.x+26 and soco.x + soco.raio <= inimigo.x+60):
            if soco.y >= inimigo.y+21 and soco.y <= inimigo.y+69:
                inimigo.Hit_Inimigo("J2")
                Gerador_Soco_Player2.pop(Gerador_Soco_Player2.index(soco))
        elif (soco.x + soco.raio >= inimigo2.x+26 and soco.x + soco.raio <= inimigo2.x+60):
            if soco.y >= inimigo2.y+21 and soco.y <= inimigo2.y+69:
                inimigo2.Hit_Inimigo("J2")
                Gerador_Soco_Player2.pop(Gerador_Soco_Player2.index(soco))
        elif (soco.x + soco.raio >= Kobra.x+29 and soco.x + soco.raio <= Kobra.x+66):
            if soco.y >= Kobra.y+54 and soco.y <= Kobra.y+146:
                Kobra.Hit_Inimigo("J2")
                Gerador_Soco_Player2.pop(Gerador_Soco_Player2.index(soco))
        else:
            Gerador_Soco_Player2.pop(Gerador_Soco_Player2.index(soco))

def Colisao_Soco_Inimigo():
    for soco in gerar_soco:
        if (soco.x + soco.raio >= Classe.hitbox[0] and soco.x + soco.raio <= Classe.hitbox[0] + 30):
            if soco.y >= Classe.hitbox[1] and soco.y <= Classe.hitbox[1] + 40:
                Classe.danoPlayer()
                gerar_soco.pop(gerar_soco.index(soco))
        elif (soco.x + soco.raio >= Classe2.hitbox[0] and soco.x + soco.raio <= Classe2.hitbox[0] + 30):
            if soco.y >= Classe2.hitbox[1] and soco.y <= Classe2.hitbox[1] + 40:
                Classe2.danoPlayer2()
                gerar_soco.pop(gerar_soco.index(soco))
        else:
            gerar_soco.pop(gerar_soco.index(soco))

while run:

    if SlowMotion == False:
        clock.tick(27)
    else:
        clock.tick(5)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == SONG_END:
            if primeira_fase == 0:
                Controlador_Jogo = "Tela_de_Cutscenes"
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

    if Classe.parartela == False:
      if Classe2.x <= Posicao_inicial_paralaxe:
         Classe2.x = Classe2.x
      elif  Classe2.velocidade_Personagem_X >=0:
         Classe.contador_de_passos += 1
         Classe2.x = Posicao_inicial_paralaxe
         Background_Fase_Posicao += -Classe2.velocidade_Personagem_X
         Background_Fase_Posicao_0 += -1
         if Classe.direita == False:
             Classe.velocidade_Personagem_X = -4
             Classe.x += Classe.velocidade_Personagem_X


      rel_x = Background_Fase_Posicao % Background_Largura
      rel_x2 = Background_Fase_Posicao_0 % Background_Largura

    Colisao_Soco_Personagem1()
    Colisao_Soco_Personagem2()
    Colisao_Soco_Inimigo ()
    MovimentoPersonagem1()
    Colisao_Soco_Inimigo ()
    MovimentoPersonagem2()

    if Controlador_Jogo == "Tela_de_Titulo":

        Tela_Inicial.Press_Start.play()
        if Botao_Pressionado[K_RETURN]:
            Tela_Inicial.Tela_de_titulo_animacao.play()

        if Botao_Pressionado[K_s]:
            pickle.dump(Leaderboard, open("top_scores", "wb"))
            Load_Top_Scores = pickle.load(open("top_scores", "rb"))

        if Botao_Pressionado[K_d]:
            Load_Top_Scores = pickle.load(open("top_scores", "rb"))
            Load_Top_Scores.sort(key=itemgetter('Pontos'), reverse=True)
            mostrarPlacar(Load_Top_Scores)

        if Tela_Inicial.Tela_de_titulo_animacao.currentFrameNum == 9:
            Controlador_Jogo = "Tela_de_Nomeacao"
            start_ticks = pygame.time.get_ticks()


    if Controlador_Jogo == "Tela_de_Cutscenes":
        pygame.display.update()


        if Botao_Pressionado[K_RETURN]:
            Controlador_Jogo = "Tela_da_Fase_1"
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
            Controlador_Jogo = "Tela_da_Fase_1"
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
            Controlador_Jogo = "Tela_da_Fase_2"
            start_ticks = pygame.time.get_ticks()
            pygame.mixer.music.stop()
            pygame.mixer.music.load('Musica_SFX/Musica_Fase.wav')
            pygame.mixer.music.play(-1)
            textnumber = 15


    if Controlador_Jogo == "Tela_de_Nomeacao":
        Janela.fill((0, 0, 0))
        Letra1 = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
        if pygame.key.get_pressed()[pygame.K_RETURN] and Nome_Jogador_Letra_Atual <3:
            SFX_Text.play()
            time.sleep(0.2)
            Nome_Jogador_Letra_Atual += 1
            Nome_Jogador_Letra_Temporaria = 0
            if Nome_Jogador_Letra_Atual == 3:
                Classe.Nome_Player = str(Letra1[Nome_Jogador_Primeira_Letra])+str(Letra1[Nome_Jogador_Segunda_Letra])+str(Letra1[Nome_Jogador_Terceira_Letra])
                Controlador_Jogo = "Tela_de_Cutscenes"
                pygame.mixer.music.stop()
                pygame.mixer.music.load('Musica_SFX/intro_akira.mp3')
                pygame.mixer.music.play()
        if Nome_Jogador_Letra_Atual == 0:
            if pygame.key.get_pressed()[pygame.K_UP]:
                SFX_Text.play()
                if Nome_Jogador_Letra_Temporaria >= 25:
                    time.sleep(0.1)
                    Nome_Jogador_Letra_Temporaria = 0
                    Nome_Jogador_Primeira_Letra = Nome_Jogador_Letra_Temporaria
                else:
                    time.sleep(0.1)
                    Nome_Jogador_Letra_Temporaria += 1
                    Nome_Jogador_Primeira_Letra = Nome_Jogador_Letra_Temporaria
            if pygame.key.get_pressed()[pygame.K_DOWN]:
                SFX_Text.play()
                time.sleep(0.1)
                Nome_Jogador_Letra_Temporaria -=1
                Nome_Jogador_Primeira_Letra = Nome_Jogador_Letra_Temporaria
                if Nome_Jogador_Letra_Temporaria < 0:
                    Nome_Jogador_Letra_Temporaria = 25
                    Nome_Jogador_Primeira_Letra = Nome_Jogador_Letra_Temporaria
        if Nome_Jogador_Letra_Atual == 1:
            if pygame.key.get_pressed()[pygame.K_UP]:
                SFX_Text.play()
                if Nome_Jogador_Letra_Temporaria >= 25:
                    time.sleep(0.1)
                    Nome_Jogador_Letra_Temporaria = 0
                    Nome_Jogador_Segunda_Letra = Nome_Jogador_Letra_Temporaria
                else:
                    time.sleep(0.1)
                    Nome_Jogador_Letra_Temporaria += 1
                    Nome_Jogador_Segunda_Letra = Nome_Jogador_Letra_Temporaria
            elif pygame.key.get_pressed()[pygame.K_DOWN]:
                SFX_Text.play()
                time.sleep(0.1)
                Nome_Jogador_Letra_Temporaria -= 1
                Nome_Jogador_Segunda_Letra = Nome_Jogador_Letra_Temporaria
                if Nome_Jogador_Letra_Temporaria < 0:
                    Nome_Jogador_Letra_Temporaria = 25
                    Nome_Jogador_Segunda_Letra = Nome_Jogador_Letra_Temporaria
        if Nome_Jogador_Letra_Atual == 2:
            if pygame.key.get_pressed()[pygame.K_UP]:
                SFX_Text.play()
                if Nome_Jogador_Letra_Temporaria >= 25:
                    time.sleep(0.1)
                    Nome_Jogador_Letra_Temporaria = 0
                    Nome_Jogador_Terceira_Letra = Nome_Jogador_Letra_Temporaria
                else:
                    time.sleep(0.1)
                    Nome_Jogador_Letra_Temporaria += 1
                    Nome_Jogador_Terceira_Letra = Nome_Jogador_Letra_Temporaria
            elif pygame.key.get_pressed()[pygame.K_DOWN]:
                SFX_Text.play()
                time.sleep(0.1)
                Nome_Jogador_Letra_Temporaria -= 1
                Nome_Jogador_Terceira_Letra=Nome_Jogador_Letra_Temporaria
                if Nome_Jogador_Letra_Temporaria < 0:
                    Nome_Jogador_Letra_Temporaria = 25
                    Nome_Jogador_Terceira_Letra = Nome_Jogador_Letra_Temporaria

        ptext.draw("DIGITE SEU NOME", center=(Largura / 2, Altura / 2-60), fontname="fontes/start.ttf",
                   color=(255, 255, 255),
                   gcolor=(150, 150, 150),
                   shadow=(3, 3), scolor="#000000")
        ptext.draw(str(Letra1[Nome_Jogador_Primeira_Letra]), center=(Largura / 2-27, Altura / 2), fontname="fontes/start.ttf",
                   color=(255, 255, 255),
                   gcolor=(150, 150, 150),
                   shadow=(3, 3), scolor="#000000")
        ptext.draw(str(Letra1[Nome_Jogador_Segunda_Letra]), center=(Largura / 2, Altura / 2), fontname="fontes/start.ttf",
                   color=(255, 255, 255),
                   gcolor=(150, 150, 150),
                   shadow=(3, 3), scolor="#000000")
        ptext.draw(str(Letra1[Nome_Jogador_Terceira_Letra]), center=(Largura / 2+27, Altura / 2), fontname="fontes/start.ttf",
                   color=(255, 255, 255),
                   gcolor=(150, 150, 150),
                   shadow=(3, 3), scolor="#000000")
        pygame.display.update()


    if Botao_Pressionado[pygame.K_r]:
        textoPlacar = mostrarPlacar(Load_Top_Scores)
        time.sleep(1)

    if Botao_Pressionado[K_l]:
        Scoreboard_Player = {'Nome': Nome_do_player, 'Pontos': Score}
        Load_Top_Scores.insert(0, Scoreboard_Player)
        pickle.dump(Load_Top_Scores, open("top_scores", "wb"))
        Load_Top_Scores = pickle.load(open("top_scores", "rb"))
        Load_Top_Scores.sort(key=itemgetter('Pontos'), reverse=True)
        for key in Load_Top_Scores:
            print(key)

    if Botao_Pressionado[K_b] and Classe.HP >= 0.9:
        Classe.HP -= 0.2
        Classe.Score += 10
        Classe2.Score += 10

    redrawGameWindow()

pygame.quit()