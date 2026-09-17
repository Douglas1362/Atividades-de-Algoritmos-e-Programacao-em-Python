# 18. Ano bissexto
# Leia um ano e determine se ele é bissexto.
# Utilize as seguintes regras:
# ● o ano deve ser divisível por 4;
# ● se for divisível por 100, ele não é bissexto;
# ● porém, se também for divisível por 400, ele é bissexto.
# Exemplos:
# 2024 → Bissexto
# 1900 → Não bissexto
# 2000 → Bissexto
# 2023 → Não bissexto
# O desafio é construir corretamente a condição utilizando and, or e not.

ano = int(input("Digite um ano: "))

if (ano % 4 == 0 and not ano % 100 == 0) or ano % 400 == 0:
    print("Ano bissexto")
else:
    print("Ano não bissexto")