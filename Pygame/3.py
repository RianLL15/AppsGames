import pygame
from pygame.locals import *
from sys import exit

pygame.init()

largura = 1280
altura = 720

PRETO = (0, 0, 0)

# Carrega e executa uma música de fundo
pygame.mixer.music.load('Som\\Pygame\\Garotos-Podres-Mancha.wav')
pygame.mixer.music.play(-1)

tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Sprites')

class Personagem(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites_esquerda = [
            pygame.image.load('Sprites\\BonecoDeNeveA1.png'),
            pygame.image.load('Sprites\\BonecoDeNeveA2.png'),
            pygame.image.load('Sprites\\BonecoDeNeveA3.png'),
            pygame.image.load('Sprites\\BonecoDeNeveA4.png'),
            pygame.image.load('Sprites\\BonecoDeNeveA5.png'),
            pygame.image.load('Sprites\\BonecoDeNeveA6.png'),
            pygame.image.load('Sprites\\BonecoDeNeveA7.png'),
            pygame.image.load('Sprites\\BonecoDeNeveA8.png'),
            pygame.image.load('Sprites\\BonecoDeNeveA9.png')
        ]
        self.sprites_direita = [
            pygame.image.load('Sprites\\BonecoDeNeveD1.png'),
            pygame.image.load('Sprites\\BonecoDeNeveD2.png'),
            pygame.image.load('Sprites\\BonecoDeNeveD3.png'),
            pygame.image.load('Sprites\\BonecoDeNeveD4.png'),
            pygame.image.load('Sprites\\BonecoDeNeveD5.png'),
            pygame.image.load('Sprites\\BonecoDeNeveD6.png'),
            pygame.image.load('Sprites\\BonecoDeNeveD7.png'),
            pygame.image.load('Sprites\\BonecoDeNeveD8.png'),
            pygame.image.load('Sprites\\BonecoDeNeveD9.png')
        ]
        self.sprites_cima = [
            pygame.image.load('Sprites\\BonecoDeNeveW1.png'),
            pygame.image.load('Sprites\\BonecoDeNeveW2.png'),
            pygame.image.load('Sprites\\BonecoDeNeveW3.png'),
            pygame.image.load('Sprites\\BonecoDeNeveW4.png'),
            pygame.image.load('Sprites\\BonecoDeNeveW5.png'),
            pygame.image.load('Sprites\\BonecoDeNeveW6.png'),
            pygame.image.load('Sprites\\BonecoDeNeveW7.png'),
            pygame.image.load('Sprites\\BonecoDeNeveW8.png'),
            pygame.image.load('Sprites\\BonecoDeNeveW9.png')
        ]
        self.sprites_baixo = [
            pygame.image.load('Sprites\\BonecoDeNeveS1.png'),
            pygame.image.load('Sprites\\BonecoDeNeveS2.png'),
            pygame.image.load('Sprites\\BonecoDeNeveS3.png'),
            pygame.image.load('Sprites\\BonecoDeNeveS4.png'),
            pygame.image.load('Sprites\\BonecoDeNeveS5.png')
        ]
        self.sprites_parado = [
            pygame.image.load('Sprites\\BonecoDeNeveW1.png')
        ]
        self.atual = 0
        self.image = self.sprites_parado[self.atual]
        self.image = pygame.transform.scale(self.image, (32*7, 32*7))
        self.rect = self.image.get_rect()
        self.rect.topleft = 300, 255

        # Velocidade do personagem
        self.velocidade = 3
        self.parado = True

    def update(self):
        # Obtém as teclas pressionadas
        keys = pygame.key.get_pressed()

        # Armazena a posição anterior para reverter em caso de saída da tela
        x_anterior = self.rect.x
        y_anterior = self.rect.y

        # Verifica se o personagem está se movendo
        if keys[K_w] or keys[K_a] or keys[K_s] or keys[K_d] or keys[K_UP] or keys[K_LEFT] or keys[K_DOWN] or keys[K_RIGHT]:
            self.parado = False
        else:
            self.parado = True

        # Se o personagem estiver parado, mostra a animação de ficar parado
        if self.parado:
            self.atual += 1
            if self.atual >= len(self.sprites_parado):
                self.atual = 0
            self.image = self.sprites_parado[self.atual]
            self.image = pygame.transform.scale(self.image, (32*13, 32*13))
        else:
            # Verifica se a tecla D está pressionada
            if keys[K_d] or keys[K_RIGHT]:
                self.atual += 1
                if self.atual >= len(self.sprites_direita):
                    self.atual = 0
                self.image = self.sprites_direita[self.atual]
                self.image = pygame.transform.scale(self.image, (32*13, 32*13))
                self.rect.x += self.velocidade

            # Verifica se a tecla A está pressionada
            elif keys[K_a] or keys[K_LEFT]:
                self.atual += 1
                if self.atual >= len(self.sprites_esquerda):
                    self.atual = 0
                self.image = self.sprites_esquerda[self.atual]
                self.image = pygame.transform.scale(self.image, (32*13, 32*13))
                self.rect.x -= self.velocidade

            # Verifica se a tecla W está pressionada
            elif keys[K_w] or keys[K_UP]:
                self.atual += 1
                if self.atual >= len(self.sprites_cima):
                    self.atual = 0
                self.image = self.sprites_cima[self.atual]
                self.image = pygame.transform.scale(self.image, (32*13, 32*13))
                self.rect.y -= self.velocidade

            # Verifica se a tecla S está pressionada
            elif keys[K_s] or keys[K_DOWN]:
                self.atual += 1
                if self.atual >= len(self.sprites_baixo):
                    self.atual = 0
                self.image = self.sprites_baixo[self.atual]
                self.image = pygame.transform.scale(self.image, (32*13, 32*13))
                self.rect.y += self.velocidade

        # Verifica se o personagem saiu da tela
        if self.rect.x < 0 or self.rect.x > largura - self.rect.width + 100 or self.rect.y < 0 or self.rect.y > altura - self.rect.height + 100:
            # Reverte para a posição anterior
            self.rect.x = x_anterior
            self.rect.y = y_anterior

# Grupo de sprites
todas_as_sprites = pygame.sprite.Group()
personagem = Personagem()
todas_as_sprites.add(personagem)

# Carrega fundo
imagem_fundo = pygame.image.load('Fundo\\fundo.png').convert()
imagem_fundo = pygame.transform.scale(imagem_fundo, (largura, altura))

relogio = pygame.time.Clock()

while True:
    relogio.tick(15)
    tela.fill(PRETO)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

    # Atualiza o personagem
    personagem.update()

    tela.blit(imagem_fundo, (0, 0))
    todas_as_sprites.draw(tela)
    todas_as_sprites.update()
    pygame.display.flip()