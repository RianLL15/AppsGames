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

op = str(input("\nEscolha a operação: "))
r = int
Cop = str

if op == "!":

    n1 = int(input("\nEscolha um número: "))
    r = math.factorial(n1)
    Cop = "fatorial"
    print(f"O {Cop} de {n1} é igual a {r}")
    exit()

elif op == "log":

    n1 = float(input("\nEscolha o primeiro número: "))
    n2 = float(input("\nEscolha o segundo número: "))
    r = math.log(n2, n1)
    print(f"Log na base {n1} e o logaritmando {n2} o X é igual a {r}")
    exit()

else:
    n1 = float(input("\nEscolha o primeiro número: "))
    n2 = float(input("\nEscolha o segundo número: "))


if op == "+": r = n1 + n2
elif op == "-": r = n1 - n2
elif op == "/":
    r = n1 / n2
    round(r, 2)
elif op == "*": r = n1 * n2
elif op == "^": r = n1 ** n2
elif op == "%": 
    r = n1 * (n2 / 100)
    round(r, 2)

if op == "+": Cop = " mais "
elif op == "-": Cop = " menos "
elif op == "/": Cop = " dividido "
elif op == "*": Cop = " multiplicado por "
elif op == "^": Cop = " elevado "
elif op == "%": Cop = " porcento de "

print(f"\n{n1}{Cop}{n2} é igual a {r}")
exit()

#############################################################################################################################
