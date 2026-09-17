# 14. Calculadora de IMC
# Leia:
# ● peso em kg;
# ● altura em metros.
# Calcule o IMC utilizando:
# IMC = peso / (altura × altura)
# Classifique o resultado:
# Menor que 18,5 → Abaixo do peso
# 18,5 até 24,9 → Peso normal
# 25 até 29,9 → Sobrepeso
# 30 ou mais → Obesidade
# Também verifique se o peso e a altura são valores válidos.

print("========= Calculadora de IMC =========")

peso = float(input("Digite o peso em kg: "))
altura = float(input("Digite a altura em metros: "))

IMC = peso / (altura * altura)

if peso <= 0 or altura <= 0: 
    print("Peso e a altura  inválidos")
elif IMC < 18.5:
    print("Abaixo do peso")
elif IMC <= 24.9:
    print("Peso normal")
elif IMC <= 29.9:
    print("Sobrepeso")
elif IMC >= 30:
    print("Obesidade")