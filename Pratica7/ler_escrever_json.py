"""
Crie um script em Python que leia e escreva dados em um arquivo JSON. 
O arquivo JSON deve conter informações de uma pessoa, com campos nome, idade e cidade.
"""

import json

def ler_json(nome_arquivo):
    with open(nome_arquivo, 'r', encoding='utf-8') as arquivo_json:
        dados = json.load(arquivo_json)
        return dados
    
def escrever_json(nome_arquivo, dados):
    with open(nome_arquivo, 'w', encoding='utf-8') as arquivo_json:
        json.dump(dados, arquivo_json, ensure_ascii=False, indent=4)
        
def main():
    dados_pessoa = {
        "nome": "João",
        "idade": 29,
        "cidade": "São Paulo"
    }
    
    nome_arquivo = input("Digite o nome do arquivo JSON a ser criado (ex: pessoa.json): ").strip()
    escrever_json(nome_arquivo, dados_pessoa)
    print(f"Dados escritos com sucesso em {nome_arquivo}")
    
    try:
        dados_lidos = ler_json(nome_arquivo)
        print(f"\nDados lidos do arquivo {nome_arquivo}:")
        print(f"Nome: {dados_lidos['nome']}, Idade: {dados_lidos['idade']}, Cidade: {dados_lidos['cidade']}")
    except FileNotFoundError:
        print(f"Erro: O arquivo {nome_arquivo} não foi encontrado.")
    except json.JSONDecodeError:
        print(f"Erro: O arquivo {nome_arquivo} não contém um JSON válido.")
    except Exception as e:
        print(f"Ocorreu um erro ao processar o arquivo: {e}")
if __name__ == "__main__":
    main()
