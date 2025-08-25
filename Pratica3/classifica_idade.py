"""
2- Classificador de Idade


Crie um programa que solicite a idade do usuário e classifique-o
em uma das seguintes categorias:

Criança (0-12 anos),

Adolescente (13-17 anos),

Adulto (18-59 anos)

Idoso (60 anos ou mais).
"""

idade = int(input("Digite sua idade: "))
if 0 <= idade <= 12:
    print("Você é classificado como: Criança")
elif 13 <= idade <= 17:
    print("Você é classificado como: Adolescente")
elif 18 <= idade <= 59:
    print("Você é classificado como: Adulto")
elif idade >= 60:
    print("Você é classificado como: Idoso")
else:
    print("Idade inválida. Por favor, insira uma idade válida.")
