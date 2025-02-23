import pygame
import sys
import random

pygame.init()

L = 800
H = 600

T = pygame.display.set_mode((L, H))

pygame.display.set_caption("Jogo da Zuera")

backG = (0, 0, 0)
player = (255, 255, 255)

Pp = [L // 2, H //2]
vel = 5

while True:
    for evento in pygame.event.get():

        if evento.type == pygame.K_0:

            pygame.quit()
            sys.exit()

        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE and player == (255, 255, 255):

            backG = (255, 255, 255)
            player = (0, 0, 0)

        elif evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE and player == (0, 0, 0):

            backG = (0, 0, 0)
            player = (255, 255, 255)

        if evento.type == pygame.KEYDOWN and evento.key == pygame.K_LSHIFT:

            vel = 5 * 2

        else:

            vel = 5
            Teclas = pygame.key.get_pressed()

    if Teclas[pygame.K_ESCAPE]:

        pygame.quit()
        sys.exit()

    if Teclas[pygame.K_a] and Pp [0] > 0:

        Pp[0] -= vel

    if Teclas[pygame.K_d] and Pp [0] < L - 50:

        Pp[0] += vel

    if Teclas[pygame.K_w] and Pp [1] > 0:

     Pp[1] -= vel

    if Teclas[pygame.K_s] and Pp [1] < H - 50:

         Pp[1] += vel

    T.fill(backG)

    pygame.draw.rect(T, player, (Pp[0], Pp[1], 50, 50))
    pygame.display.flip()
    pygame.time.Clock().tick(120)
