# 2. Calculadora de área 
# Faça um programa que receba a largura e a altura de um retângulo. 
# Calcule e mostre: 
# ● a área; 
# ● o perímetro. 

largura = int(input("Digite a largura do retângulo: "))
altura = int(input("Digite a altura do retângulo: "))

area = largura * altura

perímetro = 2 * (largura + altura) 

print("área do retângulo: ", area)
print("perímetro do retângulo: ", perímetro)
