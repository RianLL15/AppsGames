#############################################################################################################################

# Sistema de input e indentificação da operação(simples):


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

# Sistema de input e indentificação da operação(Mediano):

# import math

# op = str(input("\nEscolha a operação: "))
# r = int
# Cop = str

# if op == "!":
#     n1 = int(input("\nEscolha um número: "))
#     r = math.factorial(n1)
#     Cop = "fatorial"
#     print(f"O {Cop} de {n1} é igual a {r}")
#     exit()

# elif op == "log":
#     n1 = float(input("\nEscolha o primeiro número: "))
#     n2 = float(input("\nEscolha o segundo número: "))
#     r = math.log(n2, n1)
#     print(f"Log na base {n1} e o logaritmando {n2} o X é igual a {r}")
#     exit()

# else:
#     n1 = float(input("\nEscolha o primeiro número: "))
#     n2 = float(input("\nEscolha o segundo número: "))

# if op == "+": r = n1 + n2
# elif op == "-": r = n1 - n2
# elif op == "/":
#     r = n1 / n2
#     round(r, 2)
# elif op == "*": r = n1 * n2
# elif op == "^": r = n1 ** n2
# elif op == "%": 
#     r = n1 * (n2 / 100)
#     round(r, 2)

# if op == "+": Cop = " mais "
# elif op == "-": Cop = " menos "
# elif op == "/": Cop = " dividido "
# elif op == "*": Cop = " multiplicado por "
# elif op == "^": Cop = " elevado "
# elif op == "%": Cop = " porcento de "

# print(f"\n{n1}{Cop}{n2} é igual a {r}")
# exit()

#############################################################################################################################


#############################################################################################################################

# Sistema de input e indentificação da operação(complexo):

# import math

# def Inicio():
    
#     opG = ["!", "log", "+", "-", "/", "*", "%", "^"]

#     while True:

#         print("\n====================================================================")
#         print("\nTemos essa opções de operação: !, log, +, -, /, *, %, ^")
#         op = input("\nEscolha a operação: ")
#         if op in opG:
#             return op
#         else:
#             print("\nOperação inválida. Tente novamente.")        

# def Fatorial():
    
#     n1 = int(input("\nEscolha um número: "))
#     r = math.factorial(n1)
#     Cop = "fatorial"
#     print(f"\nO {Cop} de {n1} é igual a {r}\n")
#     print("====================================================================")

# def Log():

#     n1 = float(input("\nEscolha o primeiro número: "))
#     n2 = float(input("\nEscolha o segundo número: "))
#     r = math.log(n2, n1)
#     print(f"\nLog na base {n1} e o logaritmando {n2} o X é igual a {r}\n")
#     print("====================================================================")

# def Add():

#     n1 = float(input("\nEscolha o primeiro número: "))
#     n2 = float(input("\nEscolha o segundo número: "))
#     r = n1 + n2
#     Cop = " mais "
#     print(f"\n{n1}{Cop}{n2} é igual a {r}\n")
#     print("====================================================================")

# def Sub():

#     n1 = float(input("\nEscolha o primeiro número: "))
#     n2 = float(input("\nEscolha o segundo número: "))
#     r = n1 - n2
#     Cop = " menos "
#     print(f"\n{n1}{Cop}{n2} é igual a {r}\n")
#     print("====================================================================")

# def Mult():

#     n1 = float(input("\nEscolha o primeiro número: "))
#     n2 = float(input("\nEscolha o segundo número: "))
#     r = n1 * n2
#     Cop = " multiplaicado por "
#     print(f"\n{n1}{Cop}{n2} é igual a {r}\n")
#     print("====================================================================")

# def Div():

#     n1 = float(input("\nEscolha o primeiro número: "))
#     n2 = float(input("\nEscolha o segundo número: "))
#     r = n1 / n2
#     round(r, 2)
#     Cop = " dividido "
#     print(f"\n{n1}{Cop}{n2} é igual a {r}\n")
#     print("====================================================================")

# def Elev():

#     n1 = float(input("\nEscolha o primeiro número: "))
#     n2 = float(input("\nEscolha o segundo número: "))
#     r = n1 ** n2
#     Cop = " elevado "
#     print(f"\n{n1}{Cop}{n2} é igual a {r}\n")
#     print("====================================================================")

# def Porc():

#     n1 = float(input("\nEscolha o primeiro número: "))
#     n2 = float(input("\nEscolha o segundo número: "))
#     r = n1 * (n2 / 100)
#     round(r, 2)
#     Cop = " porcento de "
#     print(f"\n{n1}{Cop}{n2} é igual a {r}\n") 
#     print("====================================================================")

# while True:
#     op = Inicio()

#     if op == "+": 
#         Add()
#     elif op == "-": 
#         Sub()
#     elif op == "/": 
#         Div()
#     elif op == "*": 
#         Mult() 
#     elif op == "^": 
#         Elev() 
#     elif op == "!": 
#         Fatorial()
#     elif op == "log": 
#         Log() 
#     else: 
#         Porc() 

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
# import random
# import time

# pygame.init()

# Erro = pygame.mixer.Sound('Som\\P3IT\\errou-rude.wav')
# Win = pygame.mixer.Sound('Som\\P3IT\\ai-que-delicia-mickey.wav')
# Decepcao = pygame.mixer.Sound('Som\\P3IT\\faz-o-l-luan-gameplays.wav')
# Special = pygame.mixer.Sound('Som\\P3IT\\ai-meu-c-zinho-w-penelope-di-monaco.wav')

# nA = random.randint(1, 100)

# def Inicio():
        
#         print("Dificuldades disponíveis: f(Fácil) ou d(Difícl)")
#         Df = input("Escolha a dificuldade: ").lower()

#         while Df != "f" and Df != "d":
#             print("\nDificuldades disponíveis: f(Fácil) ou d(Difícl)")
#             Df = input("Escolha a dificuldade: ").lower()

#         return Df
        
# def DfD(): 

#         T = 0 #Tentativas
#         TM = 90 #Tentativas Max
#         t = 0 #Tempo
#         tm = 600 #Tempo Max

#         while T < TM:

#             T += 1

#             P = int(input("\nAdvinhe um número de 1 a 100: "))

#             if P == nA: 
#                 print("\nVocê acertou!!!!")
#                 while t < tm:
#                     Special.play()
#                     time.sleep(2)
#                 tm -= 1
#                 exit()
#             elif T == TM: 
#                 print(f"\nA resposta correta era {nA}")
#                 while t < tm:
#                      Decepcao.play()
#                      time.sleep(3)
#                 tm -= 1
#                 exit()
#             elif  P > nA: 
#                 print("\nVocê está no caminho, tente um número menor")
#                 Erro.play()
#                 time.sleep(2)
#                 pygame.mixer.music.unpause()
#             else:
#                 print("\nVocê está no caminho, tente um número maior")
#                 Erro.play()
#                 time.sleep(2)
#                 pygame.mixer.music.unpause()

# def DfF():
        
#         T = 0 #Tentativas
#         t = 0 #Tempo
#         tm = 600 #Tempo Max

#         while True:

#             T += 1

#             P = int(input("\nAdvinhe um número de 1 a 100: "))

#             if P == nA: 
#                 print(f"\nVocê acertou o numero em {T} tentativa(s)!!!!")
#                 while t < tm:
#                     Win.play()
#                     time.sleep(1)
#                 tm -= 1
#                 exit()
#             elif  P > nA: 
#                 print("\nVocê está no caminho, tente um número menor")
#                 Erro.play()
#                 time.sleep(2)
#                 pygame.mixer.music.unpause()

#             else:
#                 print("\nVocê está no caminho, tente um número maior")
#                 Erro.play()
#                 time.sleep(2)
#                 pygame.mixer.music.unpause()

# Df = Inicio()

# if Df == "d": 
#     DfD() 
# else: 
#     DfF() 

#######################################################################################################################################


#######################################################################################################################################
