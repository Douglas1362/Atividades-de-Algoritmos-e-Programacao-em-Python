#. Saudação ao usuário 
#Faça um programa que solicite o nome e a idade do usuário e, ao final, mostre uma 
#mensagem informando: 
#● o nome digitado; 
#● a idade; 
#● a idade que a pessoa terá no próximo ano.

nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))

idade1ano = idade + 1

print("Ola,", nome)
print("Sua idade é:", idade)
print("No próximo ano você terá:", idade1ano, "anos")
