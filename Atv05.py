# 5. Positivo, negativo ou zero 
# Leia um número inteiro e informe se ele é: 
# ● positivo; 
# ● negativo; 
# ● zero. 

numero = int(input("Digite um número inteiro: "))

if numero > 0:
    print("Número positivo")
elif numero < 0:
    print("Número negativo")
elif numero == 0:
    print("Zero")