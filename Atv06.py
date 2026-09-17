# 6. Maior entre dois números 
# Leia dois números inteiros e mostre qual deles é o maior. 
# Caso os dois sejam iguais, informe: 
# Os números são iguais.

numero1 = int(input("Digite o primerio numero: "))
numero2 = int(input("Digite o segundo numero: "))

if numero1 > numero2:
    print("O primeiro é o maior")
elif numero2 > numero1:
    print("O segundo é o maior")
elif numero1 == numero2:
    print("Os números são iguais")