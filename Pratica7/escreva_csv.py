"""
Crie um script em Python que escreva dados em um arquivo CSV. 
O arquivo CSV deve conter informações pessoais, como colunas Nome, Idade e Cidade.
"""

import csv
def escrever_csv(nome_arquivo, dados):
    with open(nome_arquivo, mode='w', newline='', encoding='utf-8') as arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv)
        escritor_csv.writerow(['Nome', 'Idade', 'Cidade'])  # Escreve o cabeçalho
        escritor_csv.writerows(dados)  # Escreve os dados
def main():
    dados_pessoais = [
        ['Alice', 30, 'São Paulo'],
        ['Bruno', 25, 'Rio de Janeiro'],
        ['Carla', 28, 'Belo Horizonte'],
        ['Daniel', 35, 'Curitiba']
    ]
    
    nome_arquivo = input("Digite o nome do arquivo CSV a ser criado (ex: dados.csv): ").strip()
    escrever_csv(nome_arquivo, dados_pessoais)
    print(f"Dados escritos com sucesso em {nome_arquivo}")
if __name__ == "__main__":
    main()