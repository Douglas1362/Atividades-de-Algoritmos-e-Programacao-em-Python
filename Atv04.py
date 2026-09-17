# 4. Média de três notas 
# Um aluno realizou três avaliações. 
# Leia as três notas e calcule a média. 
# Depois: 
# ● se a média for maior ou igual a 7, mostre Aprovado; 
# ● caso contrário, mostre Reprovado.

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 7:
    print("Aprovado")
else:
    print("Reprovado")