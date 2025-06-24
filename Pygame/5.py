import pygame
import random

# definicao das cores
preto = (0, 0, 0)
branco = (255, 255, 255)
azul = (0, 0, 255)
vermelho = (255, 0, 0)

# inicializa pygame
pygame.init()
pygame.mixer.init()

# tela
tela = pygame.display.set_mode((660, 660))
pygame.display.set_caption("Pacman")
background = pygame.Surface(tela.get_size()).convert()
background.fill(preto)
relogio = pygame.time.Clock()
font = pygame.font.Font("freesansbold.ttf", 24)

# imagem favicon
logo = pygame.image.load("Sprites/PacManDaZuera-5/FastasmasDaZUERA/LOGO.png")
pygame.display.set_icon(logo)

class Parede(pygame.sprite.Sprite):
    def __init__(self, x, y, largura, altura, cor):
        super().__init__()
        self.image = pygame.Surface([largura, altura])
        self.image.fill(cor)
        self.rect = self.image.get_rect()
        self.rect.top = y
        self.rect.left = x

def iniciarParedes(lista_sprite):
    lista_parede = pygame.sprite.RenderPlain()
    paredes = [
        [0, 0, 660, 6],
        [0, 0, 6, 660],
        [0, 654, 660, 6],
        [654, 0, 6, 660]
    ]
    for item in paredes:
        parede = Parede(item[0], item[1], item[2], item[3], azul)
        lista_parede.add(parede)
        lista_sprite.add(parede)
    return lista_parede

def iniciarPortao(lista_sprites):
    # Removido o portão para liberar o meio da tela
    return None

class Bola(pygame.sprite.Sprite):
    def __init__(self, cor, largura, altura):
        super().__init__()
        self.image = pygame.Surface([largura, altura])
        self.image.fill(preto)
        self.image.set_colorkey(preto)
        pygame.draw.ellipse(self.image, cor, [0, 0, largura, altura])
        self.rect = self.image.get_rect()

class Jogador(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.imagens = {
            "direita": [pygame.image.load(f"Sprites/PacManDaZuera-5/PacmanD ({i}).png").convert() for i in range(1, 7)],
            "esquerda": [pygame.image.load(f"Sprites/PacManDaZuera-5/PacmanA ({i}).png").convert() for i in range(1, 7)],
            "cima": [pygame.image.load(f"Sprites/PacManDaZuera-5/PacmanW ({i}).png").convert() for i in range(1, 7)],
            "baixo": [pygame.image.load(f"Sprites/PacManDaZuera-5/PacmanS ({i}).png").convert() for i in range(1, 7)]
        }
        for direcao in self.imagens:
            for img in self.imagens[direcao]:
                img.set_colorkey(preto)

        self.direcao = "direita"
        self.frame_index = 0
        self.image = self.imagens[self.direcao][self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y

        self.mudar_x = 0
        self.mudar_y = 0
        self.frame_contador = 0

    def mudarvelocidade(self, x, y):
        self.mudar_x = x
        self.mudar_y = y
        if x > 0: self.direcao = "direita"
        elif x < 0: self.direcao = "esquerda"
        elif y > 0: self.direcao = "baixo"
        elif y < 0: self.direcao = "cima"

    def atualizar(self, paredes, portao):
        antigo_x, antigo_y = self.rect.left, self.rect.top
        self.rect.left += self.mudar_x
        if pygame.sprite.spritecollide(self, paredes, False):
            self.rect.left = antigo_x
        self.rect.top += self.mudar_y
        if pygame.sprite.spritecollide(self, paredes, False):
            self.rect.top = antigo_y
        if portao and pygame.sprite.spritecollide(self, portao, False):
            self.rect.left, self.rect.top = antigo_x, antigo_y

        if self.mudar_x != 0 or self.mudar_y != 0:
            self.frame_contador += 1
            if self.frame_contador >= 3:
                self.frame_contador = 0
                self.frame_index = (self.frame_index + 1) % len(self.imagens[self.direcao])
                self.image = self.imagens[self.direcao][self.frame_index]
        else:
            self.image = self.imagens[self.direcao][0]

class Fantasma(pygame.sprite.Sprite):
    def __init__(self, x, y, imagem_path):
        super().__init__()
        self.image = pygame.image.load(imagem_path).convert()
        self.image.set_colorkey(preto)
        self.rect = self.image.get_rect()
        self.rect.left = x
        self.rect.top = y
        self.direcao = random.choice([(20, 0), (-20, 0), (0, 20), (0, -20)])
        self.timer = 0

    def atualizar(self, paredes, portao):
        antigo_x, antigo_y = self.rect.left, self.rect.top
        self.rect.left += self.direcao[0]
        self.rect.top += self.direcao[1]
        if pygame.sprite.spritecollide(self, paredes, False):
            self.rect.left, self.rect.top = antigo_x, antigo_y
            self.direcao = random.choice([(20, 0), (-20, 0), (0, 20), (0, -20)])
        self.timer += 1
        if self.timer > 20:
            self.direcao = random.choice([(20, 0), (-20, 0), (0, 20), (0, -20)])
            self.timer = 0

def iniciarJogo():
    pygame.mixer.music.load("Som/Pygame/Garotos-Podres-Mancha.wav")
    pygame.mixer.music.play(-1, 0.0)
    lista_sprites = pygame.sprite.RenderPlain()
    lista_bola = pygame.sprite.RenderPlain()
    lista_monstros = pygame.sprite.RenderPlain()
    lista_parede = iniciarParedes(lista_sprites)
    portao = iniciarPortao(lista_sprites)

    pacman = Jogador(330, 330)
    lista_sprites.add(pacman)

    fantasmas_info = [
        "Sprites/PacManDaZuera-5/FastasmasDaZUERA/LOGO.png",
        "Sprites/PacManDaZuera-5/FastasmasDaZUERA/WENDEL.jpg",
        "Sprites/PacManDaZuera-5/FastasmasDaZUERA/Biscate.jpeg",
        "Sprites/PacManDaZuera-5/FastasmasDaZUERA/BrunoBacon.jpeg",
        "Sprites/PacManDaZuera-5/FastasmasDaZUERA/BrunoNiver.jpeg",
        "Sprites/PacManDaZuera-5/FastasmasDaZUERA/BrunoPaz.jpeg"
    ]
    for imagem in fantasmas_info:
        f = Fantasma(400, 100, imagem)
        lista_monstros.add(f)
        lista_sprites.add(f)

    for linha in range(1, 21):
        for coluna in range(1, 21):
            bola = Bola(vermelho, 10, 10)
            bola.rect.x = (30 * coluna)
            bola.rect.y = (30 * linha)
            if not pygame.sprite.spritecollide(bola, lista_parede, False) and not pygame.sprite.spritecollide(bola, lista_sprites, False):
                lista_bola.add(bola)
                lista_sprites.add(bola)

    pontos = 0
    pontuacao_maxima = len(lista_bola)
    finalizar = False

    while not finalizar:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                finalizar = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    pacman.mudarvelocidade(-20, 0)
                if event.key == pygame.K_RIGHT:
                    pacman.mudarvelocidade(20, 0)
                if event.key == pygame.K_UP:
                    pacman.mudarvelocidade(0, -20)
                if event.key == pygame.K_DOWN:
                    pacman.mudarvelocidade(0, 20)

        pacman.atualizar(lista_parede, portao)
        for fantasma in lista_monstros:
            fantasma.atualizar(lista_parede, portao)

        blocks_hit_list = pygame.sprite.spritecollide(pacman, lista_bola, True)
        pontos += len(blocks_hit_list)

        tela.fill(preto)
        lista_parede.draw(tela)
        lista_sprites.draw(tela)

        texto = font.render(f"Pontos: {pontos}/{pontuacao_maxima}", True, azul)
        tela.blit(texto, [10, 10])

        if pontos == pontuacao_maxima:
            resultado("Parabens, voce venceu!", 145)

        if pygame.sprite.spritecollide(pacman, lista_monstros, False):
            resultado("Game Over", 235)

        pygame.display.flip()
        relogio.tick(10)

def resultado(mensagem, left):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    return
                if event.key == pygame.K_RETURN:
                    iniciarJogo()
                    return

        overlay = pygame.Surface((400, 200))
        overlay.set_alpha(10)
        overlay.fill((128, 128, 128))
        tela.blit(overlay, (100, 200))

        tela.blit(font.render(mensagem, True, branco), [left, 233])
        tela.blit(font.render("Aperte Enter para reiniciar", True, branco), [135, 303])
        tela.blit(font.render("Sair: ESC", True, branco), [255, 333])

        pygame.display.flip()
        relogio.tick(10)

iniciarJogo()
pygame.quit()