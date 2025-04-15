import pygame
from pygame. locals import *
from sys import exit

# Inicialização do Pygame
pygame.init ()

# Definição das dimensões da tela
largura = 800
altura = 600

# Cor preta (para usar no fundo se necessário)
PRETO = (0, 0, 0)

# Carregar a imagem de fundo
fundo = pygame.image.load('Sprites2\\fundo.png') 
fundo = pygame.transform.scale(fundo,(largura, altura)) # Redimensiona o fundo para o tamanho da tela

# Carregar o som de ataque
pygame.mixer.init() # Inicializa o mixer de áudio
som_ataque = pygame.mixer.Sound('Sprites2\\Garotos-Podres-Mancha.wav') #Arquivo de áudio do movimento

# Criação da janela
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption('Sprites')

class Neve(pygame.sprite.Sprite):

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)

        # Lista de sprites para a animação de ataque
        self.sprites_ataque = [pygame.image.load('Sprites2\\BonecoDeNeve.gif')]
        
        # Lista de sprites para a animação de movimento (em pé)
        self.sprites_movimento = [pygame.image.load('Sprites2\\BonecoDeNeveP.png')]

        # Índices para controlar as animações
        self.atual_ataque = 0
        self.atual_movimento = 0

        # Carregamento e escala da imagem inicial
        self.image = self.sprites_movimento[self.atual_movimento]
        self.image = pygame.transform.scale(self.image, (128*5, 64*5))

        # Obtém o retângulo da imagem e define a posição inicial
        self.rect = self.image.get_rect()
        self.rect.topleft = 100, 100

        # Flag para indicar se a animação de ataque está ocorrendo
        self.animar_ataque = False

    def atacar(self):

        # Método chamado quando a tecla é pressionada para iniciar a animação de ataque
        self.animar_ataque = True
        som_ataque.play() # Toca o som de ataque sempre que o sapo atacar

    def update(self):

        # Método chamado a cada quadro para atualizar a animação
        if self.animar_ataque:

            # Incrementa o índice para mudar para o próximo sprite da animação de ataque
            self.atual_ataque = self.atual_ataque + 0.5

            if self.atual_ataque >= len(self.sprites_ataque):

                # Reinicia a animação se atingir o final da lista de sprites
                self.atual_ataque = 0
                self.animar_ataque = False # Finaliza a animação de ataque

            # Atualiza a imagem de ataque
            self.image = self.sprites_ataque[int(self.atual_ataque) ]
            self.image = pygame.transform.scale(self.image,(128*5, 64*5))

        else:
        
            # Animação de espera (em pé) quando não está atacando
            self.atual_movimento = self.atual_movimento + 0.1

            if self.atual_movimento >= len(self.sprites_movimento):

                self.atual_movimento = 0

        # Atualiza a imagem de espera
        self.image = self.sprites_movimento[int(self.atual_movimento)]
        self.image = pygame.transform.scale(self.image,(128*5, 64*5))

# Criação do grupo de sprites
todas_as_sprites = pygame.sprite.Group()
boneco = Neve()
todas_as_sprites.add(boneco)

# Configuração do relógio para controlar a taxa de quadros por segundo
relogio = pygame.time.Clock()

# Loop principal
while True:
    # Limita a taxa de quadros por segundo
    relogio. tick(30)

    # Preenche a tela com a cor preta e desenha o fundo
    tela.blit(fundo,(0, 0)) # Desenha o fundo na posição (0, 0)

    # Verifica eventos
    for event in pygame. event. get():
        if event.type == QUIT:
            pygame. quit()
            exit ()
        if event. type == KEYDOWN:
            # Chama o método de ataque quando a tecla é pressionada
            boneco.atacar()

    # Desenha todas as sprites na tela
    todas_as_sprites.draw(tela)

    # Atualiza todas as sprites
    todas_as_sprites.update()

    # Atualiza a tela
    pygame.display.flip() 