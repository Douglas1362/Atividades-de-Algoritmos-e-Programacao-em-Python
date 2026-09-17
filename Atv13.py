# 13. Sistema de login
# Crie um programa que solicite:
# ● nome de usuário;
# ● senha.
# Considere que os dados corretos são:
# Usuário: admin
# Senha: 1234
# O programa deverá verificar os dois dados.
# Se ambos estiverem corretos:
# Login realizado com sucesso!
# Caso contrário:
# Usuário ou senha incorretos.

usuario = input("Usuário: ")
senha = int(input("Digite a sua senha:"))

usuarioc = "admin"
senhac = 1234

if usuario == usuarioc and senha == senhac:
    print("login sucesso")
else:
    print("Usuário ou senha incorretos.")