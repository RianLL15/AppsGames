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

# Sistema de input e indentificação da operação(complexo):

import math

def Inicio():
    
    opG = ["!", "log", "+", "-", "/", "*", "%", "^"]

    while True:

        print("Temos essa opções de operação: !, log, +, -, /, *, %, ^")
        op = input("\nEscolha a operação: ")
        if op in opG:
            return op
        else:
            print("Operação inválida. Tente novamente.")        

def Fatorial():
    
    n1 = int(input("\nEscolha um número: "))
    r = math.factorial(n1)
    Cop = "fatorial"
    print(f"O {Cop} de {n1} é igual a {r}")
    exit()

def Log():

    n1 = float(input("\nEscolha o primeiro número: "))
    n2 = float(input("\nEscolha o segundo número: "))
    r = math.log(n2, n1)
    print(f"Log na base {n1} e o logaritmando {n2} o X é igual a {r}")
    exit()

def Add():

    n1 = float(input("\nEscolha o primeiro número: "))
    n2 = float(input("\nEscolha o segundo número: "))
    r = n1 + n2
    Cop = " mais "
    print(f"{n1}{Cop}{n2} é igual a {r}")
    exit()

def Sub():

    n1 = float(input("\nEscolha o primeiro número: "))
    n2 = float(input("\nEscolha o segundo número: "))
    r = n1 - n2
    Cop = " menos "
    print(f"{n1}{Cop}{n2} é igual a {r}")
    exit()

def Mult():

    n1 = float(input("\nEscolha o primeiro número: "))
    n2 = float(input("\nEscolha o segundo número: "))
    r = n1 * n2
    Cop = " multiplaicado por "
    print(f"{n1}{Cop}{n2} é igual a {r}")
    exit()

def Div():

    n1 = float(input("\nEscolha o primeiro número: "))
    n2 = float(input("\nEscolha o segundo número: "))
    r = n1 / n2
    round(r, 2)
    Cop = " dividido "
    print(f"{n1}{Cop}{n2} é igual a {r}")
    exit()

def Elev():

    n1 = float(input("\nEscolha o primeiro número: "))
    n2 = float(input("\nEscolha o segundo número: "))
    r = n1 ** n2
    Cop = " elevado "
    print(f"{n1}{Cop}{n2} é igual a {r}")
    exit()

def Porc():

    n1 = float(input("\nEscolha o primeiro número: "))
    n2 = float(input("\nEscolha o segundo número: "))
    r = n1 * (n2 / 100)
    round(r, 2)
    Cop = " porcento de "
    print(f"{n1}{Cop}{n2} é igual a {r}")  
    exit()

while True:
    op = Inicio()

    if op == "+": 
        Add()
    elif op == "-": 
        Sub()
    elif op == "/": 
        Div()
    elif op == "*": 
        Mult() 
    elif op == "^": 
        Elev() 
    elif op == "!": 
        Fatorial()
    elif op == "log": 
        Log() 
    else: 
        Porc() 

#############################################################################################################################
