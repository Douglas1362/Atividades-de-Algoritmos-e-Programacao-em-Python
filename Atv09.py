# 9. Classificação por idade 
# Leia a idade de uma pessoa e classifique-a: 
# 0 a 12     → Criança 
# 13 a 17    → Adolescente 
# 18 a 59    → Adulto 
# 60 ou mais → Idoso 
# Caso seja informada uma idade negativa, informe: 
# Idade inválida.

idade = int(input("Digite a sua idade: "))

if idade <=0:
    print("Idade inválida")
elif idade <= 12:
    print("Criança")
elif idade <= 17:
    print("Adolescente")
elif idade <= 59:
    print("Adulto")
elif idade >= 60:
    print("Idoso")