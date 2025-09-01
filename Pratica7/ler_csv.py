"""
Crie um script en Python que leia um arquivo CSV e exiba os dados na tela. 
O arquivo CSV deve conter informações de pessoas, com colunas Nome, Idade e Cidade.
"""

import csv
def ler_csv(nome_arquivo):
    with open(nome_arquivo, mode='r', newline='', encoding='utf-8') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)
        dados = list(leitor_csv)
        return dados
def main():
    nome_arquivo = input("Digite o nome do arquivo CSV a ser lido (ex: dados.csv): ").strip()
    try:
        dados = ler_csv(nome_arquivo)
        print(f"\nDados do arquivo {nome_arquivo}:")
        for linha in dados:
            print(f"Nome: {linha[0]}, Idade: {linha[1]}, Cidade: {linha[2]}")
    except FileNotFoundError:
        print(f"Erro: O arquivo {nome_arquivo} não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao ler o arquivo: {e}")
if __name__ == "__main__":
    main()
    