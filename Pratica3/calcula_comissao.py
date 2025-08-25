"""
6- Calculadora de Comissão


Faça um programa que leia o nome de um vendedor, o seu salário fixo e o total de vendas
efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 15% de comissão
sobre suas vendas efetuadas, informar o total a receber no final do mês, com duas casas decimais. 

Entrada: O arquivo de entrada contém um texto (primeiro nome do vendedor) e 2 valores de
dupla precisão (double) com duas casas decimais, representando o salário fixo do vendedor e
montante total das vendas efetuadas por este vendedor, respectivamente. 

Saída: Imprima o total que o funcionário deverá receber, conforme exemplo fornecido.
"""

nome = input("Digite o nome do vendedor: ")
salario_fixo = float(input("Digite o salário fixo do vendedor (Ex: 1500.00): "))
total_vendas = float(input("Digite o total de vendas efetuadas no mês (Ex: 5000.00): "))
comissao = total_vendas * 0.15
total_receber = salario_fixo + comissao

print(f"O total a receber no final do mês é: R$ {total_receber:.2f}")
print(f"Detalhes: Salário Fixo = R$ {salario_fixo:.2f}, Comissão = R$ {comissao:.2f}")
print(f"Vendedor: {nome}")
