"""
Desenvolva um programa que consulte informações de endereço a partir de um CEP fornecido pelo usuário, 
utilizando a API ViaCEP. 
O programa deve exibir o logradouro, bairro, cidade e estado correspondentes ao CEP consultado.
"""

import requests
import json
def consultar_cep(cep):
    url = f"https://viacep.com.br/ws/{cep}/json/"
    resposta = requests.get(url)
    
    if resposta.status_code == 200:
        dados = resposta.json()
        
        if 'erro' in dados:
            return None
        else:
            logradouro = dados.get('logradouro', 'N/A')
            bairro = dados.get('bairro', 'N/A')
            cidade = dados.get('localidade', 'N/A')
            estado = dados.get('uf', 'N/A')
            
            return logradouro, bairro, cidade, estado
    else:
        return None
def main():
    print("=== CONSULTA DE ENDEREÇO POR CEP ===")
    cep = input("Digite o CEP (somente números): ").strip()
    
    if not cep.isdigit() or len(cep) != 8:
        print("CEP inválido! Certifique-se de digitar 8 números.")
        return
    
    endereco = consultar_cep(cep)
    
    if endereco:
        logradouro, bairro, cidade, estado = endereco
        print("\nEndereço encontrado:")
        print(f"Logradouro: {logradouro}")
        print(f"Bairro: {bairro}")
        print(f"Cidade: {cidade}")
        print(f"Estado: {estado}")
    else:
        print("CEP não encontrado ou inválido.")
if __name__ == "__main__":
    main()
