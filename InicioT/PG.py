#############################################################################################################################

#Sistema de input e indentificação da operação(simples):

# n1 = float(input("Escolha o primeiro número: "))
# n2 = float(input("\nEscolha o segundo número: "))
# op = str(input("\nEscolha a operação: "))

# if op == "+": print(n1 + n2)
# elif op == "-": print(n1 - n2)
# elif op == "/": print(n1 / n2)
# elif op == "*": print(n1 * n2)
# elif op == "^": print(n1 ** n2)
# elif op == "%": print(n1 * (n2 / 100))

#############################################################################################################################


#############################################################################################################################

#Sistema de input e indentificação da operação(complexo):

# n1 = float(input("Escolha o primeiro número: "))
# n2 = float(input("\nEscolha o segundo número: "))
# op = str(input("\nEscolha a operação: "))
# r = int
# Cop = str

# if op == "+": r = n1 + n2
# elif op == "-": r = n1 - n2
# elif op == "/": r = n1 / n2
# elif op == "*": r = n1 * n2
# elif op == "^": r = n1 ** n2
# elif op == "%": r = n1 * (n2 / 100)

# if op == "+": Cop = " mais "
# elif op == "-": Cop = " menos "
# elif op == "/": Cop = " dividido "
# elif op == "*": Cop = " multiplicado por "
# elif op == "^": Cop = " elevado "
# elif op == "%": Cop = " porcento de "

# print(f"\n{n1}{Cop}{n2} é igual a {r}")

#############################################################################################################################


#############################################################################################################################

#Indice de Massa Corporal

# KG = float(input("Qual é o seu peso atual:"))
# H = float(input("Qual é a sua altura atual:"))
# IMC = float(KG / (H ** 2))

# if IMC < 18.5: print(f"Abaixo do peso: {IMC}")
# elif IMC > 18.5 and IMC < 24.9: print(f"Peso normal: {IMC}")
# elif IMC > 25.0 and IMC < 29.9: print(f"Acima do peso: {IMC}")
# elif IMC > 30.0 and IMC <= 34.9: print(f"Obesidade Grau I: {IMC}")
# elif IMC > 35.0 and IMC <= 39.9: print(f"Obesidade Grau II: {IMC}")
# elif IMC >= 40.0: print(f"Obesidade Grau III: {IMC}")

#############################################################################################################################


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

# import pygame
# from pygame import mixer
# import random
# import time

# pygame.init()

# Erro = pygame.mixer.Sound('InicioT\\errou-rude.wav')
# Win = pygame.mixer.Sound('InicioT\\ai-que-delicia-mickey.wav')
# Decepcao = pygame.mixer.Sound('InicioT\\faz-o-l-luan-gameplays.wav')

# nA = random.randint(1, 100)
# T = 0
# TM = 3
# t = 0
# tm = 600

# while T < TM:
#     T += 1

#     P = int(input("Advinhe um número de 1 a 100: "))

#     if P == nA: 
#         print("\nVocê acertou!!!!")
#         Win.play()
#         time.sleep(5)
#         exit()
#     elif T == TM: 
#         print(f"\nA resposta correta era {nA}")
#         while t < tm:
#             Decepcao.play()
#             time.sleep(3)
        
#         tm -= 1
#         exit()
#     elif  P > nA: 
#         print("\nVocê está no caminho, tente um número menor")
#         Erro.play()
#         time.sleep(2)
#         pygame.mixer.music.unpause()
#     elif P < nA:
#         print("\nVocê está no caminho, tente um número maior")
#         Erro.play()
#         time.sleep(2)
#         pygame.mixer.music.unpause() 

#######################################################################################################################################


#############################################################################################################################
