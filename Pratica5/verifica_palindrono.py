"""
Crie uma função que verifique se uma palavra ou frase é um palíndromo (lê-se igual de trás para frente, 
ignorando espaços e pontuação). 
Se o resultado é True, responda “Sim”, se o resultado for False, responda “Não”.
"""

import string
def verifica_palindromo(texto):
    try:
        # Remover espaços e pontuação, e converter para minúsculas
        texto_limpo = ''.join(char.lower() for char in texto if char.isalnum())
        
        # Verificar se o texto é igual ao seu reverso
        if texto_limpo == texto_limpo[::-1]:
            return "Sim"
        else:
            return "Não"
    
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")
        return None