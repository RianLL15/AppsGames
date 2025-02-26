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
import random
import time

pygame.init()

Erro = pygame.mixer.Sound('Som\\P3IT\\errou-rude.wav')
Win = pygame.mixer.Sound('Som\\P3IT\\ai-que-delicia-mickey.wav')
Decepcao = pygame.mixer.Sound('Som\\P3IT\\faz-o-l-luan-gameplays.wav')
Special = pygame.mixer.Sound('Som\\P3IT\\ai-meu-c-zinho-w-penelope-di-monaco.wav')

nA = random.randint(1, 100)

def Inicio(): #Primeira verificacao
        
        print("Dificuldades disponíveis: f(Fácil) ou d(Difícl)")
        Df = input("Escolha a dificuldade: ").lower()

        while Df != "f" and Df != "d":
            print("\nDificuldades disponíveis: f(Fácil) ou d(Difícl)")
            Df = input("Escolha a dificuldade: ").lower()

        return Df
        
def DfD(): 

        T = 0 #Tentativas
        TM = 90 #Tentativas Max
        t = 0 #Tempo
        tm = 600 #Tempo Max

        while T < TM:

            T += 1

            P = int(input("\nAdvinhe um número de 1 a 100: "))

            if P == nA: 
                print("\nVocê acertou!!!!")
                while t < tm:
                    Special.play()
                    time.sleep(2)
                tm -= 1
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
            else:
                print("\nVocê está no caminho, tente um número maior")
                Erro.play()
                time.sleep(2)
                pygame.mixer.music.unpause()

def DfF():
        
        T = 0 #Tentativas
        t = 0 #Tempo
        tm = 600 #Tempo Max

        while True:

            T += 1

            P = int(input("\nAdvinhe um número de 1 a 100: "))

            if P == nA: 
                print(f"\nVocê acertou o numero em {T} tentativa(s)!!!!")
                while t < tm:
                    Win.play()
                    time.sleep(1)
                tm -= 1
                exit()
            elif  P > nA: 
                print("\nVocê está no caminho, tente um número menor")
                Erro.play()
                time.sleep(2)
                pygame.mixer.music.unpause()

            else:
                print("\nVocê está no caminho, tente um número maior")
                Erro.play()
                time.sleep(2)
                pygame.mixer.music.unpause()

# Açao do jogo:

Df = Inicio()

if Df == "d": # Caso a escolha tenha sido "d", ele executa essa parte
    DfD() 
else: # Caso contrario ele ira escolher essa parte para executar
    DfF() 

#######################################################################################################################################
