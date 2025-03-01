#############################################################################################################################

# Sistema de operação feita em aula(Wendel):

# n1 = int(input("Escolha o primeiro número: ")) 
# n2 = int(input("\nEscolha o segundo número: "))

# print(n1 + n2)
# print(n1 - n2)
# print(n1 / n2)
# print(n1 * n2)
# print(n1 ** n2)
# print(n1 * (n2 / 100))

#############################################################################################################################


#############################################################################################################################

# Melhorando o sistem anterior(Wendel):

# n1 = int(input("Escolha o primeiro número: ")) 
# n2 = int(input("\nEscolha o segundo número: "))

# print(f"n1 + n2")
# print(n1 - n2)
# print(n1 / n2)
# print(n1 * n2)
# print(n1 ** n2)
# print(n1 * (n2 / 100))

#############################################################################################################################


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

fig = 90
opI = ["!","!!", "+", "-", "/", "*", "%", "^", "subpag"]
opS = ["pa","pg", "gp", "ge", "f2g", "raizq", "pit", "log", "voltar"]

def Inicio():

    while True:

        print("\n" + "=" * fig)        
        print("\nTemos essa opções de operação: !, !!, +, -, /, *, %, ^, subpag")
        op = input("\nEscolha a operação: ").lower()

        if op in opI:

            return op
        
        else:
            
            print("\nOperação inválida. Tente novamente.") 

def SubP():

    while True:

        print("\n" + "=" * fig)
        print("\nTemos essa opções de operação: pa, pg, gp, ge, f2g, raizq, pit, log, voltar")
        sub_op = input("\nEscolha a operação: ").lower()

        if sub_op in opS:

            return sub_op
        
        else:
            
            print("\nOperação inválida. Tente novamente.")

def GP():

    print("\nAs opção de formas planas são: quadrado, retangulo, circulo e triangulo")
    Fg = str(input("\nEscolha uma forma geométrica para calcular sua área: ")).lower()

    if Fg == "quadrado":

        l = float(input("\nDigite um lado do quadrado: "))
        r = l ** 2

        print(f"\nA área do quadrado é igual a {r}")

    elif Fg == "retangulo":

        b = float(input("\nDigite a base do retângulo: "))
        h = float(input("\nDigite a altura do retângulo: "))

        if b == h:

            print("\nIsso não é um retângulo!")

        else:

            r = b * h
            print(f"\nA área do retângulo é igual a {r}")

    elif Fg == "triangulo":

        print("Nos temos essas opções de triângulo: equilatero")
        top = input("Escolha qual triângulo você quer calcular: ")

        if top == "equilatero":

            l = int(input("Digite um lado do triângulo: "))
            r = ((l ** 2) * math.sqrt(3)) / 4

            print(f"\nA área do triângulo equiláteto é igual a {r}")

    elif Fg == "circulo":

        c = input("\nVocê sabe a circunferência(Digite y ou n)? ").lower()

        if c == "y":
            
            c = float(input("\nDigite a circunferência: "))
            r = c / (2 * 3.14)
            a = 3.14 * (r ** 2)
            d = 2 * r

        elif c == "n":

            a = input("\nVocê sabe a área(Digite y ou n)? ")

            if a == "y":

                a = float(input("\nDigite a área: "))
                r = math.sqrt(a / 3.14)
                d = r * 2
                c = 2 * 3.14 * r
            
            elif a == "n":

                d = input("\nVocê sabe o diâmetro(Digite y ou n)? ")

                if d == "y":

                    d = float(input("\nDigite o  diâmetro: "))
                    r = d / 2
                    a = 3.14 * (r ** 2)
                    c = 2 * 3.14 * r

                elif d == "n":

                    r = float(input("\nDigite o raio: "))
                    a = 3.14 * (r ** 2)
                    d = 2 * r
                    c = 2 * 3.14 * r

                else: 
                    print("\nDigito errado!!")

            else: 
                print("\nDigito errado!!")
 
        else:
            print("\nDigito errado!!")

        print(f"\nA área do círculo é igual a {round(a, 2)}")
        print(f"A circunferência é igual {round(c, 2)}")
        print(f"O diâmetro do círculo é igual a {round(d, 2)}")
        print(f"raio do círculo é igual a {round(r, 2)}")          

    else:
        print("\nDigito errado!!")

    print("\n" + "=" * fig)

def PA():

    an = int(input("\nDetermine o termo da PA: "))
    a1 = int(input("\nInforme o primeiro número da PA: "))
    a2 = int(input("\nInforme o segundo número da PA: "))
    
    r = a2 - a1  
    n = an

    termo_n = a1 + (n - 1) * r  

    print(f"\nO {n}º termo da PA é: {termo_n}")
    print("\n" + "=" * fig)


def PG():

    an = int(input("\nDetermine o termo da PG: "))
    a1 = int(input("\nInforme o primeiro número da PG: "))
    a2 = int(input("\nInforme o segundo número da PG: "))
    
    r = a2 / a1  

    termo_n = a1 * (r ** (an - 1))

    print(f"\nO {an}º termo da PG é: {termo_n}")
    print("\n" + "=" * fig)

def Pit():

    a = input("\nEscolha o valor da hipotenusa (Pressione Enter se deseja calcular): ")
    b = input("\nEscolha o valor do primeiro cateto (Pressione Enter se deseja calcular): ")
    c = input("\nEscolha o valor do segundo cateto (Pressione Enter se deseja calcular): ")

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
      {b}    #           #   {a}
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

    print("\n" + "=" * fig)

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

    print("\n" + "=" * fig)


def Fatorial():

    if op == "!":

        n1 = int(input("\nEscolha um número: "))
        r = math.factorial(n1)
        print(f"\nO fatorial de {n1} é igual a {r}")
        
    print("\n" + "=" * fig)

def Dfatorial():

    n1f = int(input("\nEscolha um número: "))
    n1r = n1f
    r = 1
    
    while n1f > 0:

        r *= n1f
        n1f -= 2

    print(f"\nO duplo fatorial de {n1r} é igual a {r}")
    print("\n" + "=" * fig)


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
    print(f"\nLogartimando de {n1} na base {n2} é igual a {r}")

    print("\n" + "=" * fig)

def Raiz():

        n1 = int(input("\nEscolha um número: "))
        
        if n1 < 0:

            print("\nNão é possível calcular a raiz quadrada de um número negativo")

        else:

            r = math.sqrt(n1)
            print(f"\n A raiz quadrada de {n1} é igual a {r}")

        print("\n" + "=" * fig)

def Add():

    n1 = float(input("\nEscolha o primeiro número: "))
    n2 = float(input("\nEscolha o segundo número: "))
    r = n1 + n2
    print(f"\n{n1} mais {n2} é igual a {r}")
    print("\n" + "=" * fig)

def Sub():

    n1 = float(input("\nEscolha o primeiro número: "))
    n2 = float(input("\nEscolha o segundo número: "))
    r = n1 - n2
    print(f"\n{n1} menos {n2} é igual a {r}\n")
    print("\n" + "=" * fig)

def Mult():

    n1 = float(input("\nEscolha o primeiro número: "))
    n2 = float(input("\nEscolha o segundo número: "))
    r = n1 * n2
    print(f"\n{n1} multiplaicado por {n2} é igual a {r}")
    print("\n" + "=" * fig)

def Div():

    n1 = float(input("\nEscolha o primeiro número: "))
    n2 = float(input("\nEscolha o segundo número: "))

    if n2 == 0:

        print("\nErro: divisão por zero não é permitida.")

    else:
        r = round(n1 / n2, 2)
        print(f"\n{n1} dividido por {n2} é igual a {r}")

    print("\n" + "=" * fig)

def Elev():

    n1 = float(input("\nEscolha o primeiro número: "))
    n2 = float(input("\nEscolha o segundo número: "))
    r = n1 ** n2
    print(f"\n{n1} elevado {n2} é igual a {r}")
    print("\n" + "=" * fig)

def Porc():

    n1 = float(input("\nEscolha a porcetagem: "))
    n2 = float(input("\nEscolha um número: "))
    r = round(n1 * (n2 / 100),2) 
    print(f"\n{n1} por cento de {n2} é igual a {r}") 
    print("\n" + "=" * fig)

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
    elif op == "%": 
        Porc()

    else:      
        sub_op = SubP()
        if sub_op == "pa":
            PA()
        elif sub_op == "pg":
            PG()
        elif sub_op == "gp":
            GP()
        elif sub_op == "pit":
            Pit()
        elif sub_op == "log":
            Log()
        elif sub_op == "raizq":
            Raiz()
            
#############################################################################################################################
