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

import math

opG = ["!","!!", "bhaskara", "teoremapit", "log", "+", "-", "/", "*", "%", "^"]

def Inicio():

    while True:

        print("\n====================================================================")
        print("\nTemos essa opções de operação: !, !!, bhaskara, teoremapit, log, +, -, /, *, %, ^")
        op = input("\nEscolha a operação: ").lower()

        if op in opG:

            return op
        
        else:
            
            print("\nOperação inválida. Tente novamente.") 

def Pit():

    a = input("\nEscolha o valor da hipotenusa (pressione Enter se deseja calcular): ")
    b = input("\nEscolha o valor do primeiro cateto (pressione Enter se deseja calcular): ")
    c = input("\nEscolha o valor do segundo cateto (pressione Enter se deseja calcular): ")

    a = float(a) if a.strip() else None
    b = float(b) if b.strip() else None
    c = float(c) if c.strip() else None

    if a is None and b is not None and c is not None:

        a = math.sqrt(b**2 + c**2)
        
    elif b is None and a is not None and c is not None:
        if a > c:

            b = math.sqrt(a**2 - c**2)

        else:

            print("\nErro: A hipotenusa deve ser maior que o cateto.")
            return

    elif c is None and a is not None and b is not None:
        if a > b:

            c = math.sqrt(a**2 - b**2)

        else:

            print("\nErro: A hipotenusa deve ser maior que o cateto.")
            return
    
    else:

        print("\nErro: Você deve deixar exatamente um dos valores em branco para calcular.")
        return

    print(f"""\n
             #
             # #
             #   #
             #     #
             #       #
             #         #    
        {b}  #           #   {a}
             #             #
             #               #
             # # #             #
             #   #               #
             #####################

                     {c}\n""")
    
    if a.is_integer() and b.is_integer() and c.is_integer():

        a, b, c = int(a), int(b), int(c)

        if a**2 == b**2 + c**2:

            print(f"\nÉ um triângulo pitagórico perfeito!")

        else:

            print(f"\nNão é um triângulo pitagórico perfeito!")
    else:
        
        print(f"\nNão é um triângulo perfeito, porque tem valores decimais.")

    print("\n====================================================================")

def Bhaskara():

    a = int(input("\nQual o valor de a: "))
    b = int(input("\nQual o valor de b: "))
    c = int(input("\nQual o valor de c: "))

    delta = b ** 2 - 4 * a * c

    if delta == 0:

        X1 = ((-1 * b) + math.sqrt(delta)) / 2 * a

        print (f"\nA equação possui apenas uma raiz real: x' = {X1}")

    elif delta > 0:

        X1 = (-b + delta ** (1 / 2)) / (2 * a)
        X2 = (-b - delta ** (1 / 2)) / (2 * a)

        print (f"\nAs raízes da equação são: x' = {X1} e x'' = {X2}")

    else:
        print ("\nEssa equação não possui raizes reais" )

    print("\n====================================================================")


def Fatorial():

    if op == "!":

        n1 = int(input("\nEscolha um número: "))
        r = math.factorial(n1)
        print(f"\nO fatorial de {n1} é igual a {r}\n")
        
    print("====================================================================")

def Dfatorial():

    n1f = int(input("\nEscolha um número: "))
    n1r = n1f
    r = 1
    
    while n1f > 0:

        r *= n1f
        n1f -= 2

    print(f"\nO duplo fatorial de {n1r} é igual a {r}\n")
    print("====================================================================")


def Log():

    n1 = float(input("\nEscolha o logaritmando: "))
    n2 = input("\nEscolha a base(pressione Enter para base 10): ")
    str

    if n1 <= 0:

        print("\nErro: o logaritmando deve ser maior que zero.")
        return

    if n2.strip() == "":

        n2 = 10

    else:

        n2 = float(n2)

        if n2 <= 0:

            print("\nErro: a base deve ser maior que zero.")
            return

    r = round(math.log(n1, n2), 2)
    print(f"\nLogartimando de {n1} na base {n2} é igual a {r}\n")

    print("====================================================================")

def Add():

    n1 = float(input("\nEscolha o primeiro número: "))
    n2 = float(input("\nEscolha o segundo número: "))
    r = n1 + n2
    print(f"\n{n1} mais {n2} é igual a {r}\n")
    print("====================================================================")

def Sub():

    n1 = float(input("\nEscolha o primeiro número: "))
    n2 = float(input("\nEscolha o segundo número: "))
    r = n1 - n2
    print(f"\n{n1} menos {n2} é igual a {r}\n")
    print("====================================================================")

def Mult():

    n1 = float(input("\nEscolha o primeiro número: "))
    n2 = float(input("\nEscolha o segundo número: "))
    r = n1 * n2
    print(f"\n{n1} multiplaicado por {n2} é igual a {r}\n")
    print("====================================================================")

def Div():

    n1 = float(input("\nEscolha o primeiro número: "))
    n2 = float(input("\nEscolha o segundo número: "))

    if n2 == 0:

        print("\nErro: divisão por zero não é permitida.")

    else:
        r = round(n1 / n2, 2)
        print(f"\n{n1} dividido por {n2} é igual a {r}\n")

    print("====================================================================")

def Elev():

    n1 = float(input("\nEscolha o primeiro número: "))
    n2 = float(input("\nEscolha o segundo número: "))
    r = n1 ** n2
    print(f"\n{n1} elevado {n2} é igual a {r}\n")
    print("====================================================================")

def Porc():

    n1 = float(input("\nEscolha a porcetagem: "))
    n2 = float(input("\nEscolha um número: "))
    r = round(n1 * (n2 / 100),2) 
    print(f"\n{n1} por cento de {n2} é igual a {r}\n") 
    print("====================================================================")

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
    elif op == "!!":
        Dfatorial()
    elif op == "bhaskara": 
        Bhaskara()
    elif op == "log": 
        Log()
    elif op == "teoremapit":
        Pit()
    else: 
        Porc()

#############################################################################################################################
