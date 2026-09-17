# 20. Sistema de tarifa de corrida
# Faça um programa que calcule o valor de uma corrida de aplicativo.
# O programa deverá solicitar:
# ● ;
# ● quantidade de passageiros;
# ● se a corrida acontece durante o horário de pico (1 para sim e 0 para não).
# O valor da corrida deverá ser calculado da seguinte forma:
# Taxa inicial: R$ 5,00
# Valor por quilômetro: R$ 2,00
# A fórmula inicial será:
# Valor da corrida = 5 + (distância × 2)
# Porém, existem algumas regras:
# 1. Horário de pico
# Se a corrida acontecer no horário de pico, será acrescentado 30% ao valor da corrida.
# 2. Mais de 3 passageiros
# Se houver mais de 3 passageiros, será acrescentada uma taxa fixa de R$ 10,00.
# 3. Distância longa
# Se a corrida tiver mais de 20 km, o passageiro receberá um desconto de 10% sobre o
# valor final.
# 4. Validação
# A distância deve ser maior que zero e a quantidade de passageiros deve ser maior que
# zero.
# Caso contrário:
# Dados inválidos.
# Ao final, mostre:
# Distância: 15 km
# Passageiros: 2
# Horário de pico: Não
# Valor da corrida: R$ 35,00
# O programa deverá considerar todas as regras na ordem correta, aplicando os
# acréscimos e descontos quando suas condições forem atendidas.

print("=========== Sistema de tarifa de corrida ===========")

quilometros = float(input("Digite a distância da corrida em quilômetros: "))
passageiros = int(input("Digite a quantidade de passageiros: "))
pico = int(input("A corrida acontece durante o horário de pico (1 para sim e 0 para não): "))

valordacorrida = 5 + (quilometros * 2)

if quilometros <= 0 or passageiros <= 0:
    print("Dados inválidos")
else:
    if pico == 1:
         valordacorrida = valordacorrida * 1.30
    if passageiros > 3:
        valordacorrida = valordacorrida + 10
    if quilometros > 20:
        valordacorrida = valordacorrida * 0.90

print("Distância:", quilometros, "km")
print("Passageiros: ", passageiros)

if pico == 1:
    print("Horário de pico: Sim")
else:
    print("Horário de pico: Não")

print("Valor da corrida: R$", valordacorrida)