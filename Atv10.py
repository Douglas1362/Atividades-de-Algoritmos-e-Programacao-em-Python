# 10. Maior entre três números 
# Leia três números inteiros e informe: 
# ● qual é o maior número; 
# ● qual é o menor número. 
# Considere também a possibilidade de haver números iguais.

numero1 = int(input("Digite o primerio numero: "))
numero2 = int(input("Digite o segundo numero: "))
numero3 = int(input("Digite o terceiro numero: "))

#maior número
if numero1 > numero2 and numero1 > numero3:
    print("O primeiro é o maior")
elif numero2 > numero1 and numero2 > numero3:
    print("O segundo é o maior")
elif numero3 > numero1 and numero3 > numero2:
    print("O terceiro é o maior")

#menor número
if numero1 < numero2 and numero1 < numero3:
    print("O primeiro é o menor")
elif numero2 < numero1 and numero2 < numero3:
    print("O segundo é o menor")
elif numero3 < numero1 and numero3 < numero2:
    print("O terceiro é o menor")

if numero1 == numero2 and numero1 == numero3:
    print("Os numeros são iguais")
elif numero1 == numero2:
     print("O primeiro numero e o segundo são iguais")
elif numero1 == numero3:
     print("O primeiro numero e o terceiro são iguais")
elif numero2 == numero3:
     print("O segundo numero e o terceiro são iguais")
else:
    print("nenhum dos numeros são iguais")

