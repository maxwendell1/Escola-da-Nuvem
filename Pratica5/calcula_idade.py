"""
Crie uma função que calcule a idade de uma pessoa em dias, baseada no ano de nascimento.
"""

def calcula_idade(ano_nascimento, ano_atual):
    try:
        if ano_nascimento > ano_atual:
            raise ValueError("O ano de nascimento não pode ser maior que o ano atual.")
        if ano_nascimento < 0 or ano_atual < 0:
            raise ValueError("Os anos não podem ser negativos.")
        
        idade_anos = ano_atual - ano_nascimento
        idade_dias = idade_anos * 365
        return idade_dias
    
    except TypeError:
        print("Erro: Os parâmetros devem ser números inteiros.")
        return None
    except ValueError as ve:
        print(f"Erro: {ve}")
        return None
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        return None