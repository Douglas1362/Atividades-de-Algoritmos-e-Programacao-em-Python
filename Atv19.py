# 19. Sistema de estacionamento
# Um estacionamento cobra de acordo com o tempo de permanência:
# Até 1 hora → R$ 10,00
# Mais de 1 até 3h → R$ 20,00
# Mais de 3 até 5h → R$ 30,00
# Mais de 5 horas → R$ 40,00
# Porém, existem duas condições especiais:
# ● clientes cadastrados recebem 20% de desconto;
# ● se o cliente permanecer mais de 8 horas, o valor final será R$ 50,00,
# independentemente do cadastro.
# Leia:
# ● quantidade de horas;
# ● se o cliente é cadastrado (1 para sim e 0 para não).
# Calcule e mostre o valor final.
# O programa também deverá rejeitar valores de horas menores ou iguais a zero.

cadastro = int(input("Cliente é cadastrado (1 para sim e 0 para não): "))
horas = int(input("Numero de horas no estacionamento: "))

if horas <= 0:
    print("Valor Invalido")
elif horas > 8:
    print("Valor final: R$ 50.00")
else:
    if horas <= 1:
        valor = 10
    elif horas <= 3:
        valor = 20
    elif horas <= 5:
        valor = 30
    elif horas <= 8:
        valor = 40
    if cadastro == 1:
        valor = valor * 0.80

print("Valor final: R$", valor)