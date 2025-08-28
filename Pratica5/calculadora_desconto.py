"""
Crie um programa que receba o preço original de um produto e um percentual de desconto, 
realizando o cálculo do preço final após a aplicação do desconto. 
Requisitos:
Permitir que o usuário informe o preço do produto e o percentual de desconto.
Utilizar operações matemáticas para calcular o valor do desconto e o preço final.
Exibir o preço final com duas casas decimais para garantir precisão. 
Entrada esperada: preço do produto (exemplo: 250.75) e o percentual de desconto (exemplo: 10).
"""

def calcula_desconto(preco_original, percentual_desconto):
    try:
        if preco_original < 0:
            raise ValueError("O preço original não pode ser negativo.")
        if not (0 <= percentual_desconto <= 100):
            raise ValueError("O percentual de desconto deve estar entre 0 e 100.")
        
        valor_desconto = (preco_original * percentual_desconto) / 100
        preco_final = preco_original - valor_desconto
        return round(preco_final, 2)
    
    except TypeError:
        print("Erro: Os parâmetros devem ser números (float ou int).")
        return None
    except ValueError as ve:
        print(f"Erro: {ve}")
        return None
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        return None