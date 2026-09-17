# 16. Caixa eletrônico simplificado
# Um caixa eletrônico possui apenas notas de:
# R$ 100
# R$ 50
# R$ 20
# R$ 10
# Leia um valor inteiro que o usuário deseja sacar.
# O programa deverá verificar:
# 1. Se o valor é positivo;
# 2. Se é possível formar o valor utilizando apenas essas notas;
# 3. Caso seja possível, informe quantas notas de cada valor serão utilizadas.
# Exemplo:
# Valor: 380
# 3 notas de R$100
# 1 nota de R$50
# 1 nota de R$20
# 1 nota de R$10
# Restrição: não utilize laços de repetição. O cálculo deve ser realizado diretamente
# através das operações matemáticas.

valor = int(input("Valor: R$ "))

if valor <= 0:
    print("Valor inválido")
elif valor % 10 != 0:
    print("Não é possível formar esse valor apenas com notas de R$100, R$50, R$20 e R$10")
else:
    notas100 = valor // 100
    resto = valor % 100

    notas50 = resto // 50
    resto = resto % 50

    notas20 = resto // 20
    resto = resto % 20

    notas10 = resto // 10

    print(notas100, "nota(s) de R$100")
    print(notas50, "nota(s) de R$50")
    print(notas20, "nota(s) de R$20")
    print(notas10, "nota(s) de R$10")
