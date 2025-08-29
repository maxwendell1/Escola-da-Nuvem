"""
Crie um programa que gera uma senha aleatória com o módulo random, 
utilizando caracteres especiais, possibilitando o usuário a informar a quantidade de caracteres dessa senha aleatória.
"""

import random
import string

def gerar_senha(comprimento):
    
    letras_minusculas = string.ascii_lowercase
    letras_maiusculas = string.ascii_uppercase
    numeros = string.digits
    caracteres_especiais = "!@#$%&*()_+-=[]{}|;:,.<>?"
    
    todos_caracteres = letras_minusculas + letras_maiusculas + numeros + caracteres_especiais
    
    senha = [
        random.choice(letras_minusculas),
        random.choice(letras_maiusculas),
        random.choice(numeros),
        random.choice(caracteres_especiais)
    ]
    
    for _ in range(comprimento - 4):
        senha.append(random.choice(todos_caracteres))
    
    random.shuffle(senha)
    
    return ''.join(senha)

def main():
    print("=== GERADOR DE SENHAS ALEATÓRIAS ===")
    print("Este programa gera senhas seguras com caracteres especiais")
    print()
    
    while True:
        try:
            comprimento = int(input("Digite o número de caracteres para a senha (mínimo 8): "))
            
            if comprimento < 8:
                print("Para uma senha segura, recomendamos no mínimo 8 caracteres!")
                continue
                
            senha = gerar_senha(comprimento)
        
            print("\n" + "="*50)
            print(f"SENHA GERADA ({comprimento} caracteres):")
            print(f"{senha}")
            print("="*50)
            
            if comprimento >= 12:
                print("Senha FORTE - Boa escolha!")
            elif comprimento >= 8:
                print("Senha MÉDIA - Considere usar mais caracteres para maior segurança")
            
            # Continuação caso queira gerar outra senha
            print("\nDeseja gerar outra senha?")
            continuar = input("Digite 's' para sim ou qualquer tecla para sair: ").lower()
            
            if continuar != 's':
                print("\nObrigado por usar o gerador de senhas!")
                break
                
            print("\n" + "-"*50)
            
        except ValueError:
            print("Erro: Por favor, digite um número válido!")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    main()

