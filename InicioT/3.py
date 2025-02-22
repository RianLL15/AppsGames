#############################################################################################################################

#Adivinhe o número(Simples):

# import random
# nA = random.randint(1, 100)
# T = 0
# TM = 3

# while T < TM:
#     P = int(input("Advinhe um número de 1 a 100: "))

#     if P == nA: 
#         print("Você acertou!!!!")
#         exit()
#     elif  P > nA: print("Você está no caminho, tente um número menor")
#     else: print("Você está no caminho, tente um número maior")

#     T += 1
#     if T == TM: print(f"A resposta correta era {nA}")

#############################################################################################################################


#############################################################################################################################


#Adivinhe o número(Complexo):

import pygame
from pygame import mixer
import random
import time

pygame.init()

Erro = pygame.mixer.Sound('Som\\P3IT\\errou-rude.wav')
Win = pygame.mixer.Sound('Som\\P3IT\\ai-que-delicia-mickey.wav')
Decepcao = pygame.mixer.Sound('Som\\P3IT\\faz-o-l-luan-gameplays.wav')

nA = random.randint(1, 100)
T = 0
TM = 3
t = 0
tm = 600

while T < TM:
    T += 1

    P = int(input("Advinhe um número de 1 a 100: "))

    if P == nA: 
        print("\nVocê acertou!!!!")
        Win.play()
        time.sleep(5)
        exit()
    elif T == TM: 
        print(f"\nA resposta correta era {nA}")
        while t < tm:
            Decepcao.play()
            time.sleep(3)
        
        tm -= 1
        exit()
    elif  P > nA: 
        print("\nVocê está no caminho, tente um número menor")
        Erro.play()
        time.sleep(2)
        pygame.mixer.music.unpause()
    elif P < nA:
        print("\nVocê está no caminho, tente um número maior")
        Erro.play()
        time.sleep(2)
        pygame.mixer.music.unpause() 

    
#######################################################################################################################################