"""
Crie um programa que gera um perfil de usuário aleatório usando a API 'Random User Generator'. 
O programa deve exibir o nome, email e país do usuário gerado.
"""

import requests
import json
def gerar_perfil():
    url = "https://randomuser.me/api/"
    resposta = requests.get(url)
    
    if resposta.status_code == 200:
        dados = resposta.json()
        usuario = dados['results'][0]
        
        nome = f"{usuario['name']['first']} {usuario['name']['last']}"
        email = usuario['email']
        pais = usuario['location']['country']
        
        return nome, email, pais
    else:
        return None
def main():
    print("=== GERADOR DE PERFIL DE USUÁRIO ALEATÓRIO ===")
    perfil = gerar_perfil()
    
    if perfil:
        nome, email, pais = perfil
        print(f"Nome: {nome}")
        print(f"Email: {email}")
        print(f"País: {pais}")
    else:
        print("Erro ao obter o perfil do usuário.")
if __name__ == "__main__":
    main()
