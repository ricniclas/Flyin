import pygame
pygame.init()

height = 640
width = 480

Janela = pygame.display.set_mode((height,width))
pygame.time.delay(100)

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


def redrawGameWindow():




        # Janela.blit ( Texto_Timer , ((Largura / 2) - 17 , 10) )
        # Janela.blit ( Texto_Placar , (190 , 30) )


        pygame.draw.rect(Janela, (255, 255, 0), (78, 57, Classe.HP, 19), 0)
        Classe.draw(Janela)


        pygame.display.update()





Classe = player(200, 410, 64, 64, 64, 64)

circleRadius = 25
circlePosX = circleRadius
Classe.x = circleRadius + 50
Classe.y = 300
Classe.playerVelocityX = 0
Classe.playerVelocityY = 0



run = True
while run:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            run = False



        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("Space bar pressed down.")
            if event.key == pygame.K_w:
                print("W key pressed down.")
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                print("Space bar released.")
            if event.key == pygame.K_w:
                print("W key released.")

    keys = pygame.key.get_pressed()








    pygame.display.update()
    redrawGameWindow()



pygame.quit()