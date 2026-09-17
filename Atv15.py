# 15. Custo de combustível para uma viagem
# Faça um programa que ajude o usuário a calcular quanto ele gastará com gasolina em
# uma viagem.
# O programa deverá solicitar:
# ● distância da viagem em quilômetros;
# ● consumo médio do carro em km/L;
# ● preço da gasolina por litro.
# Calcule:
# 1. Quantos litros de gasolina serão necessários para realizar a viagem;
# 2. Quanto será gasto em reais com combustível.

distancia = float(input("Digite a distância da viagem em km: "))
consumo = float(input("Digite o consumo médio do carro em km/L: "))
preco = float(input("Digite o preço da gasolina por litro: R$ "))

litros = distancia / consumo
gasto = litros * preco

print(f"Litros necessários: ", litros,"L")
print(f"Valor gasto com combustível: R$", gasto)