#############################################################################################################################

# Indice de Massa Corporal

KG = float(input("Qual é o seu peso atual:"))
H = float(input("Qual é a sua altura atual:"))
IMC = float(KG / (H ** 2))

if IMC < 18.5: print(f"Abaixo do peso: {IMC}")
elif IMC > 18.5 and IMC < 24.9: print(f"Peso normal: {IMC}")
elif IMC > 25.0 and IMC < 29.9: print(f"Acima do peso: {IMC}")
elif IMC > 30.0 and IMC <= 34.9: print(f"Obesidade Grau I: {IMC}")
elif IMC > 35.0 and IMC <= 39.9: print(f"Obesidade Grau II: {IMC}")
elif IMC >= 40.0: print(f"Obesidade Grau III: {IMC}")

#############################################################################################################################

