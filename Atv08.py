# 8. Calculadora simples 
# Faça uma calculadora que receba: 
# ● primeiro número; 
# ● segundo número; 
# ● operação desejada. 
# As operações disponíveis são: 
# 1 - Soma 
# 2 - Subtração 
# 3 - Multiplicação 
# 4 - Divisão 
# O programa deverá realizar a operação escolhida e mostrar o resultado. 
# Caso o usuário escolha uma opção diferente de 1 a 4, mostre: 
# Operação inválida. 

print("=======Calculadora simples=======")

numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

print("Operação Desejada")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão ")

soma = numero1 + numero2
subtr = numero1 - numero2
mult = numero1 * numero2
divis = numero1 / numero2

operacao = int(input("Escolha a Operação: "))

if operacao == 1:
    print(numero1, "+", numero2, "=", soma)
elif operacao == 2:
    print(numero1, "-", numero2, "=", subtr)
elif operacao == 3:
    print(numero1, "*", numero2, "=", mult)
elif operacao == 4:
    print(numero1, "/", numero2, "=", divis)
else:
    print("Operação inválida")