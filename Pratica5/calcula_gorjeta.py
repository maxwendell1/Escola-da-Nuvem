"""
Crie uma função que calcule a gorjeta a ser deixada em um restaurante, 
baseada no valor total da conta e na porcentagem de gorjeta desejada. 
Calcula o valor da gorjeta baseado no total da conta e na porcentagem desejada.
Parâmetros: valor_conta (float): O valor total da conta porcentagem_gorjeta (float): A porcentagem da gorjeta (ex: 15 para 15%)
Retorna: float: O valor da gorjeta calculada
"""

def calcula_gorjeta(valor_conta, porcentagem_gorjeta):
    try:
        if valor_conta < 0:
            raise ValueError("O valor da conta não pode ser negativo.")
        if porcentagem_gorjeta < 0:
            raise ValueError("A porcentagem da gorjeta não pode ser negativa.")
        
        gorjeta = (valor_conta * porcentagem_gorjeta) / 100
        return gorjeta
    
    except TypeError:
        print("Erro: Os parâmetros devem ser números (float ou int).")
        return None
    except ValueError as ve:
        print(f"Erro: {ve}")
        return None
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        return None