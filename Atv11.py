#11. Aprovação completa 
# Uma faculdade utiliza três critérios para aprovação: 
# ● média das provas deve ser maior ou igual a 7; 
# ● frequência deve ser maior ou igual a 75%; 
# ● o aluno não pode possuir nenhuma pendência financeira. 
# Leia: 
# ● nota 1; 
# ● nota 2; 
# ● nota 3; 
# ● percentual de frequência; 
# ● situação financeira (1 para regular e 0 para pendente). 
# O programa deverá informar se o aluno está: 
# Aprovado 
# ou 
# Reprovado 
 #Caso seja reprovado, informe o motivo.

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
frequencia = float(input("Digite a porgentagem de frequência: "))
financeira = int(input("situação financeira (1 para regular e 0 para pendente): "))

media = (nota1 + nota2 + nota3) / 3

if frequencia <=74:
    print("Reprovado por falta")
elif media <=6:
    print("Reprovado por Nota")
elif financeira == 0:
    print("Reprovado por pendencia financeira")
else:
    print("Aprovado!")