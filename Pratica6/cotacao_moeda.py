"""
Crie um programa que consulte a cotação atual de uma moeda estrangeira em relação ao Real Brasileiro (BRL). 
O usuário deve informar o código da moeda desejada (ex: USD, EUR, GBP), e o programa deve exibir o valor atual, 
máximo e mínimo da cotação, além da data e hora da última atualização. 
Utilize a API da AwesomeAPI para obter os dados de cotação.
"""

import requests
import json
def consultar_cotacao(moeda):
    url = f"https://economia.awesomeapi.com.br/json/last/{moeda}-BRL"
    resposta = requests.get(url)
    
    if resposta.status_code == 200:
        dados = resposta.json()
        chave = f"{moeda}BRL"
        
        if chave in dados:
            cotacao = dados[chave]
            valor = cotacao['bid']
            maximo = cotacao['high']
            minimo = cotacao['low']
            data_hora = cotacao['create_date']
            
            return valor, maximo, minimo, data_hora
        else:
            return None
    else:
        return None
    
def main():
    print("=== CONSULTA DE COTAÇÃO DE MOEDA ===")
    moeda = input("Digite o código da moeda (ex: USD, EUR, GBP): ").upper().strip()
    
    cotacao = consultar_cotacao(moeda)
    
    if cotacao:
        valor, maximo, minimo, data_hora = cotacao
        print(f"\nCotação atual do {moeda} em relação ao BRL:")
        print(f"Valor: R$ {valor}")
        print(f"Máximo: R$ {maximo}")
        print(f"Mínimo: R$ {minimo}")
        print(f"Última atualização: {data_hora}")
    else:
        print("Moeda inválida ou erro ao consultar a cotação.")
if __name__ == "__main__":
    main()
