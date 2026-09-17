# 17. Triângulo
# Leia três valores correspondentes aos lados de um possível triângulo.
# Primeiro, verifique se os três valores podem formar um triângulo.
# Para isso:
# lado A < lado B + lado C
# lado B < lado A + lado C
# lado C < lado A + lado B
# Caso não possa formar um triângulo, informe:
# Os valores não formam um triângulo.
# Caso possa, classifique-o como:
# Equilátero → três lados iguais
# Isósceles → dois lados iguais
# Escaleno → três lados diferentes

print("três valores correspondentes aos lados de um possível triângulo.")

ladoA = int(input("Digite o lado A: "))
ladoB = int(input("Digite o lado B: "))
ladoC = int(input("Digite o lado C: "))

if ladoA >= ladoB + ladoC or ladoB >= ladoA + ladoC or ladoC >= ladoA + ladoB: 
    print("Os valores não formam um triângulo.")
elif ladoA == ladoB and ladoB == ladoC: 
    print("Triângulo Equilátero")
elif ladoA == ladoB or ladoA == ladoC or ladoB == ladoC: 
    print("Triângulo Isósceles")
else: 
    print("Triângulo Escaleno")