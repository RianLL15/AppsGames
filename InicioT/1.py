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
from functools import reduce
from collections import Counter

fig = 100
opI = ["+", "-", "/", "*", "%", "^", "pm", "arrs", "cbs", "pa","pg", "gp", "f2g", "raizq", "log", "js", "jc", "media", "moda", "mediana", "comprimento", "area", "volume", "massa", "tempo", "capacidade", "subpag", "subsubpag", "subpag3"] # Opções para a tela inicial, junto com comando segreto
opS = ["pm", "arrs", "cbs", "pa", "pg", "gp", "f2g", "raizq", "log", "js", "jc", "subpag", "voltar"] # Opções para a tela secundária
opSS = ["media", "moda", "mediana", "subpag", "voltar"] # Opções para a tela terciária
opSSS = ["comprimento", "area", "volume", "massa", "tempo", "capacidade", "voltar"] # opções para a tela quaternária

com = ["mm", "cm", "dm", "m", "dam", "hm", "km"] # Comprimento
area = ["mm2", "cm2", "dm2", "m2", "dam2", "hm2", "km2"] # Área
vol = ["mm3", "cm3", "dm3", "m3", "dam3", "hm3", "km3"] # Volume
massa = ["mg", "cg", "dg", "g", "dag", "hg", "kg"] # Peso ou massa
temp = ["ms", "seg", "min", "h", "dia", "semana", "mes", "ano", "ano bissexto"] # Tempo
cap = ["ml", "cl", "dl", "l", "dal", "hl", "kl"] # Capacidade

# Dicionário para conversão de unidades de comprimento
fatores_com = {

    "mm": 0.01,  # Milímetro para decímetro
    "cm": 0.1,   # Centímetro para decímetro
    "dm": 1,     # Decímetro (unidade base)
    "m": 10,     # Metro para decímetros
    "dam": 100,  # Decâmetro para decímetros
    "hm": 1000,  # Hectômetro para decímetros
    "km": 10000  # Quilômetro para decímetros
}

# Dicionário para conversão de unidades de área
fatores_area = {

    "mm2": 0.000001,   # Milímetro quadrado para metro quadrado
    "cm2": 0.0001,     # Centímetro quadrado para metro quadrado
    "dm2": 0.01,       # Decímetro quadrado para metro quadrado
    "m2": 1,           # Metro quadrado (unidade base)
    "dam2": 100,       # Decâmetro quadrado para metro quadrado
    "hm2": 10000,      # Hectômetro quadrado para metro quadrado
    "km2": 1000000     # Quilômetro quadrado para metro quadrado
}

# Dicionário para conversão de unidades de volume
fatores_vol = {
    "mm3": 0.000000001,  # Milímetro cúbico para metro cúbico
    "cm3": 0.000001,     # Centímetro cúbico para metro cúbico
    "dm3": 0.001,        # Decímetro cúbico para metro cúbico
    "m3": 1,            # Metro cúbico (unidade base)
    "dam3": 1000,       # Decâmetro cúbico para metro cúbico
    "hm3": 1000000,     # Hectômetro cúbico para metro cúbico
    "km3": 1000000000   # Quilômetro cúbico para metro cúbico
}

# Dicionário para conversão de unidades de massa
fatores_mass = {
    "mg": 0.01,   # Miligrama para decigrama
    "cg": 0.1,    # Centigrama para decigrama
    "dg": 1,      # Decigrama (unidade base)
    "g": 10,      # Grama para decigramas
    "dag": 100,   # Decagrama para decigramas
    "hg": 1000,   # Hectograma para decigramas
    "kg": 10000   # Quilograma para decigramas
}

# Dicionário para conversão de unidades de tempo
fatores_temp = {
    "ms": 0.001,       # Milissegundo para segundos
    "seg": 1,          # Segundo (unidade base)
    "min": 60,         # Minuto para segundos
    "h": 3600,         # Hora para segundos
    "dia": 86400,      # Dia para segundos
    "semana": 604800,  # Semana para segundos
    "mes": 2592000,    # Mês (média de 30 dias) para segundos
    "ano": 31536000,   # Ano (365 dias) para segundos
    "ano bissexto": 31622400  # Ano bissexto (366 dias) para segundos
}

# Dicionário para conversão de unidades de capacidade (volume de líquidos)
fatores_cap = {

    "ml": 0.0001,  # Mililitro para litro
    "cl": 0.001,   # Centilitro para litro
    "dl": 0.1,     # Decilitro para litro
    "l": 1,        # Litro (unidade base)
    "dal": 10,     # Decalitro para litros
    "hl": 100,     # Hectolitro para litros
    "kl": 1000     # Quilolitro para litros
}

def Inicio():

    """
    Função que exibe o menu principal e solicita ao usuário que escolha uma operação matemática.
    Retorna a operação escolhida se for válida, caso contrário, solicita uma nova entrada.
    """

    while True:

        print("\n" + "=" * fig)        
        print("\nTemos essas opções de operação: +, -, /, *, %, ^, subpag")
        op = input("\nEscolha a operação: ").lower()

        if op in opI: # Verifica se a operação escolhida está na lista de operações válidas

            return op
        
        else:

            print("\nOperação inválida. Tente novamente.")  # Mensagem de erro se a operação for inválida

def SubP():

    """
    Função que exibe um menu de operações secundárias e solicita ao usuário que escolha uma.
    Retorna a operação escolhida se for válida, caso contrário, solicita uma nova entrada.
    """

    while True:
        
        print("\n" + "=" * fig)
        print("\nTemos essas opções de operação: pm, arrs, cbs pa, pg, gp, f2g, raizq, log, js, jc, subpag, voltar")
        sub_op = input("\nEscolha a operação: ").lower()

        if sub_op in opS:  # Verifica se a operação escolhida está na lista de operações secundárias válidas

            return sub_op
        
        else:

            print("\nOperação inválida. Tente novamente.")  # Mensagem de erro se a operação for inválida

def SubSubP():

    """
    Função que exibe um menu de conversões disponíveis e solicita ao usuário que escolha uma opção.
    Retorna a opção escolhida se for válida, caso contrário, solicita uma nova entrada.
    """

    while True:

        print("\n" + "=" * fig)
        print("\nTemos essas opções de operação: media, moda, mediana, subpag, voltar")
        subsub_op = input("\nEscolha a operação: ").lower()

        if subsub_op in opSS:  # Verifica se a opção escolhida está na lista de conversões válidas

            return subsub_op
        
        else:

            print("\nConversão inválida. Tente novamente.")  # Mensagem de erro se a opção for inválida

def Sub3P():

    """
    Função que exibe um menu de conversões disponíveis e solicita ao usuário que escolha uma opção.
    Retorna a opção escolhida se for válida, caso contrário, solicita uma nova entrada.
    """

    while True:

        print("\n" + "=" * fig)
        print("\nAqui convertemos: comprimento, area, volume, massa, capacidade, tempo, voltar")
        sub3_op = input("\nO que você quer converter: ").lower()

        if sub3_op in opSSS:  # Verifica se a opção escolhida está na lista de conversões válidas

            return sub3_op
        
        else:

            print("\nConversão inválida. Tente novamente.")  # Mensagem de erro se a opção for inválida


def Com():

    """
    Função para conversão de comprimentos entre diferentes unidades (mm, cm, dm, m, dam, hm, km).
    O usuário insere a unidade de origem, a unidade de destino e o valor a ser convertido.
    O programa realiza a conversão e exibe o resultado.
    """

    try:

        print("\nAqui convertemos comprimentos: mm, cm, dm, m, dam, hm, km")
        c = input("\nO que você quer converter: ").lower()

        if c not in com:  # Verifica se a unidade inserida está na lista de unidades válidas

            print("\nComprimento inválido. Tente novamente.")
            return 

        cp = input("\nConverter para: ").lower()

        if cp not in com:  # Verifica se a unidade de destino é válida

            print("\nComprimento inválido. Tente novamente.")
            return

        c1 = float(input(f"\nDigite o valor em {c}: "))  # Recebe o valor a ser convertido

        vm = c1 * fatores_com[c]  # Converte o valor para a unidade base (dm)

        c2 = vm / fatores_com[cp]  # Converte para a unidade desejada

        print(f"\n{c1} {c} equivale a {c2} {cp}")
        print("\n" + "=" * fig)

    except ValueError:

        print("\nErro: Certifique-se de inserir um número válido.")

def Area():

    """
    Função para conversão de área entre diferentes unidades (mm², cm², dm², m², dam², hm², km²).
    Segue a mesma lógica da função Com(), porém utilizando fatores de conversão específicos para área.
    """

    try:
        print("\nAqui convertemos áreas: mm2, cm2, dm2, m2, dam2, hm2, km2")
        c = input("\nO que você quer converter: ").lower()

        if c not in area:

            print("\nOperação inválida. Tente novamente.")
            return 

        cp = input("\nConverter para: ").lower()

        if cp not in area:

            print("\nOperação inválida. Tente novamente.")
            return

        c1 = float(input(f"\nDigite o valor em {c}: "))  

        vmq = c1 * fatores_area[c]  # Converte para a unidade base (m²)

        c2 = vmq / fatores_area[cp]  # Converte para a unidade desejada

        print(f"\n{c1} {c} equivale a {c2} {cp}")
        print("\n" + "=" * fig)

    except ValueError:

        print("\nErro: Certifique-se de inserir um número válido.")

def Vol():

    """
    Função para conversão de volume entre diferentes unidades (mm³, cm³, dm³, m³, dam³, hm³, km³).
    Segue a mesma lógica da função Com(), mas para volumes.
    """

    try:

        print("\nAqui convertemos volumes: mm3, cm3, dm3, m3, dam3, hm3, km3")
        c = input("\nO que você quer converter: ").lower()

        if c not in vol:

            print("\nOperação inválida. Tente novamente.")
            return 

        cp = input("\nConverter para: ").lower()

        if cp not in vol:

            print("\nOperação inválida. Tente novamente.")
            return

        c1 = float(input(f"\nDigite o valor em {c}: "))  

        vmc = c1 * fatores_vol[c]  # Converte para a unidade base (m³)

        c2 = vmc / fatores_vol[cp]  # Converte para a unidade desejada

        print(f"\n{c1} {c} equivale a {c2} {cp}")
        print("\n" + "=" * fig)

    except ValueError:

        print("\nErro: Certifique-se de inserir um número válido.")

def Massa():

    """
    Função para conversão de massa entre diferentes unidades (mg, cg, dg, g, dag, hg, kg).
    Segue a mesma lógica das funções anteriores, mas para massas.
    """

    try:

        print("\nAqui convertemos massas: mg, cg, dg, g, dag, hg, kg")
        c = input("\nO que você quer converter: ").lower()

        if c not in massa:

            print("\nOperação inválida. Tente novamente.")
            return 

        cp = input("\nConverter para: ").lower()

        if cp not in massa:

            print("\nOperação inválida. Tente novamente.")
            return

        c1 = float(input(f"\nDigite o valor em {c}: "))  

        vm = c1 * fatores_mass[c]  # Converte para a unidade base (g)

        c2 = vm / fatores_mass[cp]  # Converte para a unidade desejada

        print(f"\n{c1} {c} equivale a {c2} {cp}")
        print("\n" + "=" * fig)

    except ValueError:

        print("\nErro: Certifique-se de inserir um número válido.")

def Cap():

    """
    Função para conversão de capacidade entre diferentes unidades (ml, cl, dl, l, dal, hl, kl).
    Segue a mesma lógica das funções anteriores.
    """

    try:

        print("\nAqui convertemos capacidades: ml, cl, dl, l, dal, hl, kl")
        c = input("\nO que você quer converter: ").lower()

        if c not in cap:

            print("\nOperação inválida. Tente novamente.")
            return 

        cp = input("\nConverter para: ").lower()

        if cp not in cap:

            print("\nOperação inválida. Tente novamente.")
            return

        c1 = float(input(f"\nDigite o valor em {c}: "))  

        t = c1 * fatores_cap[c]  # Converte para a unidade base (litros)

        c2 = t / fatores_cap[cp]  # Converte para a unidade desejada

        print(f"\n{c1} {c} equivale a {c2} {cp}")
        print("\n" + "=" * fig)

    except ValueError:

        print("\nErro: Certifique-se de inserir um número válido.")

def Temp():

    """
    Função para conversão de tempo entre diferentes unidades (ms, seg, min, h, dia, semana, mês, ano, ano bissexto).
    Utiliza um fator de conversão baseado no tempo em segundos.
    """

    try:

        print("\nAqui convertemos tempos: ms, seg, min, h, dia, semana, mes, ano, ano bissexto")
        c = input("\nO que você quer converter: ").lower()

        if c not in temp:

            print("\nOperação inválida. Tente novamente.")
            return 

        cp = input("\nConverter para: ").lower()

        if cp not in temp:

            print("\nOperação inválida. Tente novamente.")
            return

        c1 = float(input(f"\nDigite o valor em {c}: "))  

        t = c1 * fatores_temp[c]  # Converte para a unidade base (segundos)

        c2 = t / fatores_temp[cp]  # Converte para a unidade desejada

        print(f"\n{c1} {c} equivale a {c2} {cp}")
        print("\n" + "=" * fig)

    except ValueError:

        print("\nErro: Certifique-se de inserir um número válido.")

def Me():

    """
    Função para calcular a Média Aritmética.  
    O usuário insere vários números, e o programa calcula a média usando a fórmula:  
    Me = (soma dos valores) / quantidade de valores  
    O resultado representa o valor médio dos números informados.
    """

    try:

        qtd = int(input("\nQuantos número você deseja inserir para calcular a média? ")) 

        vs = [] # Lista para armazenar os valores inseridos
        soma = 0

        # Loop para solicitar os elementos
        for i in range(qtd):
            
            v = float(input(f"\nDigite o {i+1}º valor: "))
            vs.append(v)  # Adiciona o valor à lista
            soma += v  # Soma os valores

        # Calcula a média
        media = soma / qtd

        # Exibe a fórmula
        print("\nA fórmula da média é: Me = n1 + n2 +.../ n")
        print(f"\nMe = {' + '.join(map(str, vs))} / {qtd}")
        print(f"\nMe = {soma} / {qtd}")
        print(f"\nA média dos valores é {media}")

        print("\n" + "=" * fig) # Linha divisória para organização da saída
        
    except ValueError:

        print("\nErro: Certifique-se de inserir um número válido.")

def Md():

    """
    Função para calcular a Moda.  
    O usuário insere vários números, e o programa identifica o valor mais frequente.  
    Se houver um único número com maior frequência, ele será a moda.  
    Se houver múltiplos valores com a mesma frequência máxima, o conjunto será bimodal ou multimodal.  
    Se todos os valores aparecerem com a mesma frequência, não há moda.  
    O resultado representa o(s) número(s) que mais se repetem na amostra.
    """

    try:

        qtd = int(input("\nQuantos números você deseja inserir para calcular a moda? "))  

        # Inicializa uma lista para armazenar os valores
        vs = []

        # Loop para solicitar os elementos
        for i in range(qtd):

            v = float(input(f"\nDigite o {i+1}º valor: "))
            vs.append(v)

        # Calcula a frequência dos valores
        c = Counter(vs)
        f_m = max(c.values())  # Obtém a maior frequência

        # Filtra os valores que aparecem com a frequência máxima
        modas = [num for num, freq in c.items() if freq == f_m]

        # Exibe o resultado
        if len(modas) == len(vs):  # Caso em que todos aparecem com a mesma frequência

            print("\nNão há moda, todos os valores aparecem com a mesma frequência.")

        elif len(modas) == 1:

            print(f"\nA moda é: {modas[0]} (aparece {f_m} vezes)")

        else:

            print(f"\nAs modas são: {', '.join(map(str, modas))} (aparecem {f_m} vezes cada)")

    except ValueError:

        print("\nErro: Certifique-se de inserir números válidos.")
    
def Med():

    try:

        qtd = int(input("\nQuantos números você deseja inserir para calcular a mediana? "))

        # Inicializa uma lista para armazenar os valores
        vs = []

        # Loop para solicitar os números
        for i in range(qtd):
            v = float(input(f"\nDigite o {i+1}º valor: "))
            vs.append(v)

        # Ordena a lista de valores
        vs.sort()

        # Exibe os valores inseridos e a fórmula da mediana
        print(f"\nValores inseridos ordenados: {vs}")
        
        if qtd % 2 == 1:  # Se o número de elementos for ímpar

            mediana = vs[qtd // 2]
            print(f"\nA fórmula da mediana para quantidade ímpar n = {qtd}:")
            print(f"\nMediana = {vs[qtd // 2]} (valor central da lista ordenada)")

        else:  # Se o número de elementos for par

            mediana = (vs[qtd // 2 - 1] + vs[qtd // 2]) / 2
            print(f"\nA fórmula da mediana para quantidade par n = {qtd}:")
            print(f"\nMediana = {vs[qtd // 2 - 1]} + {vs[qtd // 2]} / 2")
            print(f"\nMediana = {mediana} (média dos dois valores centrais)")

        print("\n" + "=" * fig)  # Linha divisória para organização da saída

    except ValueError:

        print("\nErro: Certifique-se de inserir números válidos.")

def PM():

    """
    Programa para calcular diferentes tipos de Permutações.
    Permutação Simples (P(n) = n!), que calcula o número de maneiras distintas de organizar 
    n elementos sem repetições; 
    Permutação com Repetição (P(n; a, b, ...) = n! / (a! x b! x ...)), que considera repetições 
    nos elementos; 
    e Permutação Circular (Pc = (n - 1)!), que calcula o número de arranjos possíveis em um círculo. 
    O programa exibe o processo completo de cálculo, mostrando a fórmula utilizada, os valores dos 
    fatoriais e o resultado final.
    """

    try:

        print("\nAs opções de permutação são: simples, repeticao, circular")
        p = str(input("\nEscolha uma permutação para calcular: ")).lower().strip()

        # Permutação Simples
        if p == "simples":

            n = int(input("\nDigite o número total de elementos(n): "))  
            r = math.factorial(n)  # Calcula o fatorial de n

            # Exibe a fórmula
            print("\nA fórmula da permutação simples é: Pn = n!")

            # Exibe o processo e o resultado
            print(f"\nPn = {n}!")
            print(f"\nO resultado dessa permutação simples é igual a {r}")

        # Permutação com Repetição
        elif p == "repeticao":

            n = int(input("\nDigite o número total de elementos(n): "))  

            # Solicita a quantidade de grupos repetidos e os converte para uma lista de inteiros
            rep = input("\nDigite as quantidades de elementos repetidos separadas por espaço(ex: 2 3 7 12): ")
            rep = list(map(int, rep.split()))

            f_n = math.factorial(n)  # Calcula o fatorial de n

            # Inicializa variáveis para calcular o produto dos fatoriais dos elementos repetidos
            p_f = 1
            f_text = []  # Lista para exibir a equação sem os valores numéricos
            f_v = []  # Lista para exibir os valores calculados

            for r in rep:

                    f_r = math.factorial(r)  # Calcula o fatorial de cada número repetido
                    p_f *= f_r  # Multiplica os fatoriais dos elementos repetidos
                    f_text.append(f"{r}!")  # Adiciona o texto da equação
                    f_v.append(f"{f_r}")  # Adiciona os valores calculados

            p_f_v = reduce(lambda x, y: x * y, [int(i) for i in f_v])
            permutacao = f_n // p_f  # Calcula a permutação com repetição

            # Exibe a fórmula
            print("\n A fórmula da permutação com repetição é: Pn^(a, b,...) = n! / a! x b!...")

            # Verifica se a variável rep tem mais de um elemento
            if len(rep) > 1:

                # Exibe o processo completo do cálculo
                print(f"\nPn^(a, b,...) = {n}! / {' × '.join(f_text)}")  # Fórmula sem valores
                print(f"\nPn^(a, b,...) = {f_n} / {' × '.join(f_v)}")  # Fórmula com os valores calculados
                print(f"\nPn^(a, b,...) = {f_n} / {p_f_v}")  # Fórmula com os valores calculados
                print(f"\nO resultado dessa permutação com repetição é igual a {permutacao}")  # Exibe o resultado final

            else: 

                print(f"\nPn^(a, b,...) = {n}! / {' × '.join(f_text)}")  # Fórmula sem valores
                print(f"\nPn^(a, b,...) = {f_n} / {' × '.join(f_v)}")  # Fórmula com os valores calculados
                print(f"\nO resultado dessa permutação com repetição é igual a {permutacao}")  # Exibe o resultado final

        # Permutação Circular
        elif p == "circular":

            n = int(input("\nDigite o número total de elementos(n): "))  
            r = math.factorial(n - 1)  # Calcula (n-1)!

            # Exibe a fórmula
            print("\nA fórmula da permutação circular é: Pc = (n - 1)!")

            # Exibe o processo e o resultado
            print(f"\nPc = ({n} - 1)! = {n - 1}!")
            print(f"\nO resultado da permutação circular é igual a {r}")

        else:

            print("\nOpção inválida. Escolha uma permutação mencionada.")

        print("\n" + "=" * fig)  # Linha divisória para organização da saída

    except ValueError:

        print("\nErro: Certifique-se de inserir números válidos.")


def Arrs():

    """
    Programa para calcular o Arranjo Simples, que determina o número de maneiras de 
    selecionar e organizar p elementos distintos a partir de um total de n elementos, 
    sem repetição, utilizando a fórmula A(n, p) = n! / (n - p)!. O programa exibe 
    o processo completo do cálculo, incluindo a fórmula e o valor final.
    """

    try:

        n = int(input("\nDigite o número total de elementos (n): "))
        p = int(input("\nDigite o número de elementos escolhidos (p): "))

        # Verifica se p é válido
        if p > n or p < 0:

            print("\nErro: p deve ser menor ou igual a n e maior ou igual a 0.")
            return

        # Calcula fatoriais necessários
        f_n = math.factorial(n)
        f_n_p = math.factorial(n - p)
        n_p = n - p

        # Calcula o arranjo
        arranjo = f_n // f_n_p
        
        # Exibe a fórmula
        print("\nA fórmula do arranjo simples é: Anp = n! / (n - p)!")

        # Exibe o processo completo do cálculo
        print(f"\nAnp = {n}! / ({n} - {p})!")
        print(f"\nAnp = {n}! / {n_p}!")
        print(f"\nAnp = {f_n} / {f_n_p}")
        print(f"\nO resultado do arranjo simples é igual a {arranjo}")

        print("\n" + "=" * fig)  # Linha divisória para organização da saída

    except ValueError:

        print("\nErro: Certifique-se de inserir números válidos.")

def Cbs():

    """
    Programa para calcular a Combinação Simples: 
    Combinação Simples (C(n, p) = n! / (p! x (n - p)!)), que calcula o número de maneiras de 
    selecionar p elementos distintos de um total de n elementos, sem considerar a ordem. 
    O programa exibe o processo completo de cálculo, incluindo a fórmula utilizada, os valores dos 
    fatoriais e o resultado final.
    """

    try:
    
        n = int(input("\nDigite o número total de elementos (n): "))
        p = int(input("\nDigite o número de elementos escolhidos (p): "))

        # Verifica se p é válido
        if p > n or p < 0:
            print("\nErro: p deve ser menor ou igual a n e maior ou igual a 0.")
            return

        # Calcula fatoriais necessários
        f_n = math.factorial(n)
        f_p = math.factorial(p)
        f_n_p = math.factorial(n - p)

        f_n_p_f = f_p * f_n_p
        n_p = n - p
        
        # Calcula a combinação
        combinacao = f_n // (f_p * f_n_p)

        # Exibe a fórmula
        print("\nA formula da combinação sinples é: Cnp = n! / p!(n - p)!")

        # Exibe o processo completo do cálculo
        print(f"\nCnp = {n}! / {p}! × ({n} - {p})!")
        print(f"\nCnp = {n}! / {p}! × {n_p}!")
        print(f"\nCnp = {f_n} / {f_p} × {f_n_p}")
        print(f"\nCnp = {f_n} / {f_n_p_f}")
        print(f"\nO resultado da combinação simples é igual a {combinacao}")

        print("\n" + "=" * fig)

    except ValueError:

        print("\nErro: Certifique-se de inserir números válidos.")

def JC():

    """
    Função para calcular Juros Compostos.
    O usuário insere o capital inicial, a taxa de juros anual e o período de tempo (anos).
    O programa calcula o valor final e o total de juros acumulados usando a fórmula dos juros compostos.
    """

    try:

        c = float(input("\nQual é o valor principal (capital) em R$: "))
        t = float(input("\nQual é a taxa de juros anual: "))
        p = float(input("\nQual o período de tempo em anos: "))

        t = t / 100  # Convertendo a taxa percentual para decimal
        vf = c * (1 + t) ** p  # Fórmula dos juros compostos: VF = C * (1 + i) ^ t
        j = vf - c  # Calcula os juros acumulados

        print(f"\nO valor final após o período de tempo é de R$: {round(vf, 2)}") 
        print(f"\nO total de juros acumulados é de R$: {round(j, 2)}")
        print("\n" + "=" * fig)  # Linha divisória para organização da saída

    except ValueError:

        print("\nErro: Certifique-se de inserir números válidos.")


def JS():

    """
    Função para calcular Juros Simples.
    O usuário insere o capital inicial, a taxa de juros (mensal ou anual) e o tempo (meses ou anos).
    O programa calcula os juros simples e o montante total após o período.
    """

    try:

        c = float(input("\nDigite o capital inicial em R$: "))
        i = float(input("\nDigite a taxa de juros (% ao ano ou mês): "))

        # Pergunta se o tempo está em anos ou meses
        tf = input("\nInforme se o tempo está em 'meses' ou 'anos': ").strip().lower()
        t = float(input("\nDigite o tempo: "))

        if tf == "anos":

            t = t * 12  # Converte anos para meses caso necessário

        j = (c * i * t) / 100  # Fórmula dos juros simples: J = C * i * t
        m = c + j  # Calcula o montante total

        print(f"\nO juros simples é: R$ {round(j, 2)}")
        print(f"\nO montante total após {t} meses será: R$ {round(m, 2)}")
        print("\n" + "=" * fig)  # Linha divisória para organização da saída

    except ValueError:

        print("\nErro: Certifique-se de inserir números válidos.")

def GP():

    """
    Função para calcular a área de diferentes formas geométricas.
    O usuário escolhe uma forma (quadrado, retângulo, triângulo ou círculo) e insere as informações necessárias 
    (como lados, base, altura, raio, etc.). O programa calcula a área da forma escolhida e, no caso de triângulos 
    retângulos, verifica se é um triângulo pitagórico perfeito. Também oferece opções para calcular a área de 
    triângulos isósceles e escaleno com base em dados fornecidos pelo usuário. Para círculos, o programa pode calcular 
    a área, a circunferência e o diâmetro com base em diferentes entradas (como circunferência, área ou diâmetro).
    O código também lida com erros de entrada para garantir que o usuário insira valores válidos.
    """

    try:

        # Apresenta as opções de formas geométricas e pede para o usuário escolher uma
        print("\nAs opção de formas planas são: quadrado, retangulo, circulo e triangulo")
        Fg = str(input("\nEscolha uma forma geométrica para calcular sua área: ")).lower()

        # Se a forma escolhida for 'quadrado', calcula a área
        if Fg == "quadrado":
            
            l = float(input("\nDigite um lado do quadrado: "))
            r = l ** 2  # Área do quadrado: lado²
            print(f"\nA área do quadrado é igual a {r}")

        # Se a forma escolhida for 'retângulo', calcula a área
        elif Fg == "retangulo":

            b = float(input("\nDigite a base do retângulo: "))
            h = float(input("\nDigite a altura do retângulo: "))

            if b == h:

                print("\nIsso não é um retângulo!")

            else:

                r = b * h  # Área do retângulo: base * altura
                print(f"\nA área do retângulo é igual a {r}")

        # Se a forma escolhida for 'triângulo', oferece opções de tipos de triângulo
        elif Fg == "triangulo":

            print("\nNos temos essas opções de triângulo: retangulo, equilatero, escaleno, isoseles")
            top = input("\nEscolha qual triângulo você quer calcular: ").lower()

            # Cálculos para o triângulo retângulo usando o Teorema de Pitágoras
            if top == "retangulo":

                a = input("\nDigite o valor da hipotenusa(Pressione Enter se deseja calcular): ")
                b = input("\nDigite o valor do primeiro cateto(Pressione Enter se deseja calcular): ")
                c = input("\nDigite o valor do segundo cateto(Pressione Enter se deseja calcular): ")

                # Conversão de entradas para float, permitindo que o valor seja vazio (None)
                a = float(a) if a.strip() else None
                b = float(b) if b.strip() else None
                c = float(c) if c.strip() else None

                # Lógica para calcular os valores ausentes utilizando o Teorema de Pitágoras
                if a is None and b is not None and c is not None:

                    a = math.sqrt(b**2 + c**2)  # Calcular a hipotenusa

                elif b is None and a is not None and c is not None:

                    if a > c:

                        b = math.sqrt(a**2 - c**2)  # Calcular o primeiro cateto

                    else:

                        print("\nErro: A hipotenusa deve ser maior que o cateto.")
                        return
                    
                elif c is None and a is not None and b is not None:

                    if a > b:

                        c = math.sqrt(a**2 - b**2)  # Calcular o segundo cateto

                    else:

                        print("\nErro: A hipotenusa deve ser maior que o cateto.")
                        return
                    
                else:

                    print("\nErro: Você deve deixar exatamente um dos valores em branco para calcular.")
                    return

                # Exibe os resultados dos cálculos
                print(f"\nO valor da hipotenusa é igual a {a}")
                print(f"\nO valor do primeiro cateto(b) é igual a {b}")
                print(f"\nO valor do segundo cateto(c) é igual a {c}")

                # Verifica se o triângulo é pitagórico perfeito (números inteiros e satisfaz a equação)
                if a.is_integer() and b.is_integer() and c.is_integer():

                    a, b, c = int(a), int(b), int(c)

                    if a**2 == b**2 + c**2:

                        print("\nÉ um triângulo pitagórico perfeito!")

                    else:

                        print("\nNão é um triângulo pitagórico perfeito!")

                else:

                    print("\nNão é um triângulo perfeito, porque tem valores decimais.")

            # Cálculos para o triângulo equilátero
            elif top == "equilatero":

                l = float(input("\nDigite um lado do triângulo: "))
                r = ((l ** 2) * math.sqrt(3)) / 4  # Área do triângulo equilátero: (lado² * √3) / 4

                print(f"\nA área do triângulo equilátero é igual a {r}")

            # Cálculos para o triângulo escaleno
            elif top == "escaleno":

                a = float(input("\nDigite o primeiro lado: "))
                b = float(input("\nDigite o segundo lado: "))
                c = float(input("\nDigite o terceiro lado: "))

                if a and b and c:

                    p = (a + b + c) / 2  # Semi-perímetro: (a + b + c) / 2
                    area = math.sqrt((p * (p - a) * (p - b) * (p - c)))  # Fórmula de Heron

                    print(f"\nO valor do semi-perímetro é igual a {p}")
                    print(f"\nA área desse triângulo é igual a {area}")

                else:

                    print("\nErro: Você deve colocar todos os valores para calcular.")

            # Cálculos para o triângulo isósceles
            elif top == "isoseles":

                l = input("\nDigite um lado do triângulo(Pressione Enter se deseja calcular): ")
                h = input("\nDigite a altura do triângulo(Pressione Enter se deseja calcular): ")
                mb = input("\nDigite a metade da base do triângulo(Pressione Enter se deseja calcular): ")

                l = float(l) if l.strip() else None
                mb = float(mb) if mb.strip() else None
                h = float(h) if h.strip() else None

                # Lógica para calcular valores ausentes de um triângulo isósceles
                if l is None and h is not None and mb is not None:

                    resultado = h ** 2 + mb ** 2

                    if resultado >= 0:

                        l = math.sqrt(resultado)

                elif mb is None and l is not None and h is not None:

                    resultado = l ** 2 - h ** 2

                    if resultado >= 0:

                        mb = math.sqrt(resultado)

                elif h is None and l is not None and mb is not None:

                    resultado = l ** 2 - mb ** 2

                    if resultado >= 0:

                        h = math.sqrt(resultado)

                # Exibe resultados dos cálculos para o triângulo isósceles
                if h is not None:

                    bt = mb * 2 if mb is not None else None

                    area = (bt * h) / 2 if bt is not None else None

                    if l is not None:

                        print(f"\nOs dois lados do triângulo medem {l}")

                    if bt is not None and mb is not None:

                        print(f"\nA base inteira mede {bt} e a metade da base mede {mb}")

                    if h is not None:

                        print(f"\nA altura do triângulo é igual a {h}")

                    if area is not None:

                        print(f"\nA área do triângulo é igual a {area}")

                else:

                    print("\nNão foi possível calcular a área, pois faltam informações.")

        # Cálculos para o círculo
        elif Fg == "circulo":

            c = input("\nVocê sabe a circunferência(Digite y ou n)? ").lower()

            if c == "y":

                c = float(input("\nDigite a circunferência: "))
                r = c / (2 * 3.14)
                a = 3.14 * (r ** 2)
                d = 2 * r

            elif c == "n":

                a = input("\nVocê sabe a área(Digite y ou n)? ").lower()

                if a == "y":

                    a = float(input("\nDigite a área: "))
                    r = math.sqrt(a / 3.14)
                    d = r * 2
                    c = 2 * 3.14 * r

                elif a == "n":

                    d = input("\nVocê sabe o diâmetro(Digite y ou n)? ").lower()

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
                        return
                    
                else: 

                    print("\nDigito errado!!")
                    return
                
            else:

                print("\nDigito errado!!")
                return

            print(f"\nA área do círculo é igual a {round(a, 2)}")
            print(f"\nA circunferência é igual {round(c, 2)}")
            print(f"\nO diâmetro do círculo é igual a {round(d, 2)}")
            print(f"\nraio do círculo é igual a {round(r, 2)}")          

        else:

            print("\nOpção inválida. Escolha uma das formas geométricas mencionadas.")
            print("\n" + "=" * fig)

    except ValueError:

        print("\nErro: Certifique-se de inserir números válidos.")

def PA():

    """
    Função para calcular um termo específico de uma Progressão Aritmética (PA).
    O usuário insere o termo desejado, o primeiro termo da PA e o segundo termo.
    O programa calcula a razão da PA e retorna o termo desejado usando a fórmula:
    an = a1 + (n - 1) * r
    """

    try:

        an = int(input("\nDetermine o termo da PA: "))  # Termo desejado
        a1 = int(input("\nDigite o primeiro número da PA: "))  # Primeiro termo
        a2 = input("\nDigite o segundo número da PA(Precise Enter se não souber): ").strip()  # Segundo termo

        if a2 == "":

            r = int(input("\nDigite a razão da PG: "))

        else:

            a2 = float(a2) # Converte o segundo termo para float
            r = a2 - a1  # Calcula a razão da PA

        termo_n = a1 + (an - 1) * r  # Fórmula do termo geral da PA

        print("\nA fórmula da PA é An = a1 + (n - 1) x r")
        print(f"\nO {an}º termo da PA é: {termo_n}")
        print("\n" + "=" * fig)  # Linha divisória para organização da saída

    except ValueError:

        print("\nErro: Certifique-se de inserir números válidos.")


def PG():

    """
    Função para calcular um termo específico de uma Progressão Geométrica (PG).
    O usuário insere o termo desejado, o primeiro termo da PG e o segundo termo.
    O programa calcula a razão da PG e retorna o termo desejado usando a fórmula:
    an = a1 * (r ** (n - 1))
    """

    try:

        an = int(input("\nDetermine o termo da PG: "))  # Termo desejado
        a1 = int(input("\nDigite o primeiro número da PG: "))  # Primeiro termo
        a2 = input("\nDigite o segundo número da PG(Precise Enter se não souber): ").strip()  # Segundo termo

        if a2 == "":

            r = int(input("\nDigite a razão da PG: "))

        else:

            a2 = float(a2)  # Converte o segundo termo para float
            r = a2 / a1  # Calcula a razão da PG

        termo_n = a1 * (r ** (an - 1))  # Fórmula do termo geral da PG

        print("\nA fórmula da PG é An = a1 x r ^n-1")
        print(f"\nO {an}º termo da PG é: {termo_n}")
        print("\n" + "=" * fig)  # Linha divisória para organização da saída

    except ValueError:

        print("\nErro: Certifique-se de inserir números válidos.")

def Bhaskara():

    """
    Resolve a equação quadrática ax² + bx + c = 0 utilizando a Fórmula de Bhaskara.
    O cálculo é feito considerando o valor de delta e verifica se a equação possui raízes reais.
    """

    try:

        a = int(input("\nQual o valor de a: "))
        b = int(input("\nQual o valor de b: "))
        c = int(input("\nQual o valor de c: "))

        # Calcula o discriminante (delta) da equação.
        delta = b ** 2 - 4 * a * c

        # Se o delta for igual a 0, a equação possui apenas uma raiz real.
        if delta == 0:

            X1 = (-b + math.sqrt(delta)) / (2 * a)  # Calcula a raiz única da equação.
            print(f"\nA equação possui apenas uma raiz real: x' = {X1}")

        # Se o delta for maior que 0, a equação possui duas raízes reais distintas.
        elif delta > 0:

            X1 = (-b + math.sqrt(delta)) / (2 * a)  # Calcula a primeira raiz.
            X2 = (-b - math.sqrt(delta)) / (2 * a)  # Calcula a segunda raiz.
            print(f"\nAs raízes da equação são: x' = {X1} e x'' = {X2}")

        # Se o delta for menor que 0, a equação não possui raízes reais.
        else:

            print("\nEssa equação não possui raízes reais")

        print("\n" + "=" * fig) # Linha divisória para organização da saída

    except ValueError:

        print("\nErro: Certifique-se de inserir números válidos.")

def Log():

    """
    Calcula o logaritmo de um número (logaritmando) em uma base fornecida pelo usuário.
    Se a base não for fornecida, o logaritmo será calculado na base 10 por padrão.
    """

    try:

        n1 = float(input("\nEscolha o logaritmando: "))  
        n2 = input("\nEscolha a base (pressione Enter para base 10): ")  

        # Verifica se o logaritmando é maior que zero, caso contrário, exibe erro.
        if n1 <= 0:

            print("\nErro: o logaritmando deve ser maior que zero.")
            return

        # Se o usuário não informar a base, usa a base 10 por padrão.
        if n2.strip() == "":

            n2 = 10

        else:

            n2 = float(n2)

            # Verifica se a base é maior que zero, caso contrário, exibe erro.
            if n2 <= 0:

                print("\nErro: a base deve ser maior que zero.")
                return

        # Calcula o logaritmo e arredonda o resultado para duas casas decimais.
        r = round(math.log(n1, n2), 2)
        print(f"\nLogaritmo de {n1} na base {n2} é igual a {r}")

        print("\n" + "=" * fig) # Linha divisória para organização da saída

    except ValueError:

        print("\nErro: Certifique-se de inserir números válidos.")

def Raiz():

    """
    Calcula a raiz quadrada de um número inteiro não negativo.
    """

    try:

        n1 = int(input("\nEscolha um número: "))

        # Verifica se o número é negativo, pois não é possível calcular a raiz quadrada de números negativos.
        if n1 < 0:

            print("\nNão é possível calcular a raiz quadrada de um número negativo")

        else:

            r = math.sqrt(n1)  # Calcula a raiz quadrada.
            print(f"\nA raiz quadrada de {n1} é igual a {r}")

        print("\n" + "=" * fig) # Linha divisória para organização da saída

    except ValueError:

        print("\nErro: Certifique-se de inserir números válidos.")

def Add():

    """
    Realiza a soma de múltiplos números.
    """
    try:

        qtd = int(input("\nQuantos números deseja somar? "))  # Pergunta quantos números serão somados

        if qtd < 2:

            print("\nErro: É necessário somar pelo menos dois números.")
            return

        t = 0  # Inicializa a variável que armazenará a soma
        numeros = [] # Lista para armazenar os números digitados

        for i in range(qtd):

            num = float(input(f"\nDigite o {i+1}º número: "))
            numeros.append(num)
            t += num  # Soma os valores

        print("\nA fórmula da soma é: n1 + n2 +...")
        print(f"\n{' + '.join(map(str, numeros))}")
        print(f"\nA soma dos {qtd} números é {t}")

        print("\n" + "=" * fig) # Linha divisória para organização da saída

    except ValueError:

        print("\nErro: Certifique-se de inserir números válidos.")

def Sub():

    """
    Realiza a subtração de múltiplos números e exibe a fórmula da operação.
    """

    try:

        qtd = int(input("\nQuantos números deseja subtrair? "))  # Pergunta quantos números serão usados na subtração

        if qtd < 2:

            print("\nErro: É necessário pelo menos dois números para a subtração.")
            return

        numeros = []  # Lista para armazenar os números digitados

        for i in range(qtd):
            
            num = float(input(f"\nDigite o {i+1}º número: "))
            numeros.append(num)  # Adiciona o número à lista

        t = numeros[0]  # Define o primeiro número como base da subtração

        for num in numeros[1:]:  # Percorre a lista a partir do segundo número

            t -= num  # Subtrai os valores

        print("\nA fórmula da subtração é: n1 - n2 -...")
        print(f"\n{' - '.join(map(str, numeros))}")
        print(f"\nO resultado da subtração dos {qtd} números é {t}")

        print("\n" + "=" * fig) # Linha divisória para organização da saída

    except ValueError:

        print("\nErro: Certifique-se de inserir números válidos.")

def Mult():

    """
    Realiza a multiplicação de múltiplos números e exibe a fórmula da operação.
    """

    try:

        qtd = int(input("\nQuantos números deseja multiplicar? "))  # Pergunta quantos números serão multiplicados

        if qtd < 2:

            print("\nErro: É necessário multiplicar pelo menos dois números.")
            return

        t = 1  # Inicializa a variável que armazenará o resultado da multiplicação
        numeros = []  # Lista para armazenar os números digitados

        for i in range(qtd):

            num = float(input(f"\nDigite o {i+1}º número: "))
            numeros.append(num)
            t *= num  # Multiplica os valores

        print("\nA fórmula da multiplicação é: n1 × n2 ×...")
        print(f"\n{' × '.join(map(str, numeros))}")
        print(f"\nO resultado da multiplicação dos {qtd} números é {t}")

        print("\n" + "=" * fig) # Linha divisória para organização da saída

    except ValueError:

        print("\nErro: Certifique-se de inserir números válidos.")

def Div():

    """
    Realiza a divisão de múltiplos números e exibe a fórmula da operação.
    """

    try:

        qtd = int(input("\nQuantos números deseja dividir? "))  # Pergunta quantos números serão divididos

        if qtd < 2:
            print("\nErro: É necessário dividir pelo menos dois números.")
            return

        numeros = []  # Lista para armazenar os números digitados

        for i in range(qtd):
            num = float(input(f"\nDigite o {i+1}º número: "))

            # Evita a divisão por zero
            if i > 0 and num == 0:

                print("\nErro: Não é possível dividir por zero.")
                return

            numeros.append(num)

        t = numeros[0]  # Define o primeiro número como base da divisão

        for num in numeros[1:]:  # Percorre a lista a partir do segundo número

            t /= num  # Divide os valores

        print("\nA fórmula da divisão é: n1 ÷ n2 ÷...")
        print(f"\n{' ÷ '.join(map(str, numeros))}")
        print(f"\nO resultado da divisão dos {qtd} números é: {t}")

        print("\n" + "=" * fig) # Linha divisória para organização da saída

    except ValueError:

        print("\nErro: Certifique-se de inserir números válidos.")  

def Elev():

    """
    Realiza a exponenciação (potência) entre dois números.
    """

    try:

        n1 = float(input("\nEscolha o primeiro número: ")) 
        n2 = float(input("\nEscolha o segundo número: "))  
        r = n1 ** n2  # Realiza a operação de exponenciação.

        print("\nA fórmula da divisão é: n1ⁿ = n1 x n1...(n vezes)")
        print(f"\n{n1} elevado a {n2} é igual a {r}")

        print("\n" + "=" * fig) # Linha divisória para organização da saída

    except ValueError:

        print("\nErro: Certifique-se de inserir números válidos.")

def Porc():

    """
    Calcula o valor de uma porcentagem de um número.
    """

    try:

        n1 = float(input("\nEscolha a porcentagem: "))
        n2 = float(input("\nEscolha o número: "))  
        r = round(n1 * (n2 / 100), 2)  # Calcula a porcentagem do número.
        print(f"\n{n1} por cento de {n2} é igual a {r}")

        print("\n" + "=" * fig) # Linha divisória para organização da saída

    except ValueError:

        print("\nErro: Certifique-se de inserir números válidos.") 

# Função que executa comandos secretos ou operações especiais baseadas na entrada do usuário.
def comando_secreto(op):

    """
    A função verifica se o comando fornecido pelo usuário é válido e executa a função correspondente.
    """

    # Dicionário de comandos secretos, onde cada chave é um comando e o valor é a função associada.
    comandos = {

        "media": Me, "moda": Md, "mediana": Med,   # Operações avançadas matemáticas
        "pm": PM, "arrs": Arrs, "cbs": Cbs,"pa": PA, "pg": PG, "gp": GP, "f2g": Bhaskara, # Operações avançadas matemáticas
        "raizq": Raiz, "log": Log, "js": JS, "jc": JC,  # Operações avançadas matemáticas
        "comprimento": Com, "area": Area, "volume": Vol,  # Conversões de unidades
        "massa": Massa, "capacidade": Cap, "tempo": Temp  # Conversões de unidades

    }

    # Verifica se o comando fornecido pelo usuário está no dicionário de comandos
    if op in comandos:

        comandos[op]()  # Chama a função associada ao comando

# Função que direciona para as operações principais, dependendo da operação escolhida pelo usuário.
def pag(op):

    """
    Direciona para a função correspondente de acordo com o operador fornecido pelo usuário.
    """

    # Dicionário das operações matemáticas básicas
    operacoes = {

        "+": Add, "-": Sub, "*": Mult, # Operações aritméticas básicas
        "/": Div, "^": Elev, "%": Porc  # Mais operações

    }

    # Se o operador fornecido estiver nas operações matemáticas básicas
    if op in operacoes:

        operacoes[op]()  # Chama a função correspondente à operação

# Função que direciona para operações matemáticas mais avançadas.
def sub_pag():

    """
    Direciona para operações matemáticas mais avançadas, como progressões e equações.
    """

    while True:

        sub_op = SubP()  # Obtém a entrada do usuário para a operação avançada

        # Dicionário de operações avançadas
        opSub = {

            "pm": PM, "arrs": Arrs, "cbs": Cbs,"pa": PA, "pg": PG,  # Operações avançadas matemáticas
            "gp": GP, "f2g": Bhaskara, "raizq": Raiz, "log": Log, "js": JS, "jc": JC  # Mais operações

        }

        # Verifica se a opção digitada está no dicionário de operações avançadas
        if sub_op in opSub:

            opSub[sub_op]()  # Chama a função correspondente à operação avançada

        elif sub_op == "voltar":  # Se o usuário escolher voltar

            break  # Sai do loop e volta para a função anterior (pag)

        elif sub_op == "subpag":  # Se o usuário escolher "subpag", navega para subsub_pag

            subsub_pag()

        else:

            print("Opção inválida. Tente novamente.")  # Mensagem de erro para opção inválida

# Função que direciona para operações matemáticas mais avançadas.
def subsub_pag():

    """
    Direciona para conversões de unidades como comprimento, área, volume etc.
    """

    while True:

        subsub_op = SubSubP()  # Obtém a entrada do usuário para conversão de unidades

        # Dicionário de conversões de unidades
        opSubSub = {

            "media": Me, "moda": Md, "mediana": Med 

        }

        # Verifica se a opção digitada está nas conversões de unidades
        if subsub_op in opSubSub:

            opSubSub[subsub_op]()  # Chama a função correspondente à conversão de unidade

        elif subsub_op == "voltar":  # Se o usuário escolher voltar

            break  # Sai do loop e volta para a função anterior

        elif subsub_op == "subpag":  # Se o usuário escolher "subpag", navega para subsub_pag

            sub3_pag()

        else:
            print("Opção inválida. Tente novamente.")  # Mensagem de erro para opção inválida

# Função que direciona para conversões de unidades e cálculos adicionais.
def sub3_pag():

    """
    Direciona para conversões de unidades como comprimento, área, volume etc.
    """

    while True:

        sub3_op = Sub3P()  # Obtém a entrada do usuário para conversão de unidades

        # Dicionário de conversões de unidades
        conversoes = {

            "comprimento": Com, "area": Area, "volume": Vol,  # Conversões de unidades de comprimento, área e volume
            "massa": Massa, "capacidade": Cap, "tempo": Temp  # Conversões de unidades de massa, capacidade e tempo

        }

        # Verifica se a opção digitada está nas conversões de unidades
        if sub3_op in conversoes:

            conversoes[sub3_op]()  # Chama a função correspondente à conversão de unidade

        elif sub3_op == "voltar":  # Se o usuário escolher voltar

            break  # Sai do loop e volta para a função anterior

        else:
            print("Opção inválida. Tente novamente.")  # Mensagem de erro para opção inválida

# Loop principal que gerencia a navegação do programa.
while True:

    op = Inicio()  # Solicita uma opção inicial ao usuário.

    if op == "subpag3":  # Se o usuário escolher 'subpag3', chama a função de sub3_pag().
        sub3_pag()

    if op == "subsubpag":  # Se o usuário escolher 'subpag3', chama a função de sub3_pag().
        subsub_pag()

    elif op == "subpag":  # Se o usuário escolher 'subpag', chama a função de sub_pag().
        sub_pag()

    # Se a operação for uma das operações matemáticas básicas (+, -, *, /, ^, !, !!, %), chama a função correspondente.
    elif op in ["+", "-", "*", "/", "^", "%"]:
        pag(op)

    # Para operações avançadas que requerem um comando secreto
    elif op in ["pm", "arrs", "cbs", "pa", "pg", "gp", "f2g", "raizq", "log", "js", "jc", "media", "moda", "mediana"]:
        comando_secreto(op)

    # Para conversões que requerem um comando secreto
    elif op in ["comprimento", "area", "volume", "massa", "tempo", "capacidade"]:
        comando_secreto(op)
    
#############################################################################################################################
