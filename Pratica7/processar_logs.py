"""
Leia um arquivo que contenha dados de log de treinamento de modelos de Machine Learning. 
Calcule a média e o desvio padrão do tempo de exercução constantes.
"""

import csv
import statistics
def processar_logs(nome_arquivo):
    tempos = []
    with open(nome_arquivo, mode='r', newline='', encoding='utf-8') as arquivo_csv:
        leitor_csv = csv.reader(arquivo_csv)
        next(leitor_csv)
        for linha in leitor_csv:
            try:
                tempo = float(linha[1])
                tempos.append(tempo)
            except ValueError:
                print(f"Valor inválido encontrado na linha: {linha}")
    
    if tempos:
        media = statistics.mean(tempos)
        desvio_padrao = statistics.stdev(tempos)
        return media, desvio_padrao
    else:
        return None, None
def main():
    nome_arquivo = input("Digite o nome do arquivo CSV de logs a ser processado (ex: logs.csv): ").strip()
    try:
        media, desvio_padrao = processar_logs(nome_arquivo)
        if media is not None:
            print(f"Média do tempo de execução: {media:.2f}")
            print(f"Desvio padrão do tempo de execução: {desvio_padrao:.2f}")
        else:
            print("Nenhum dado válido encontrado para calcular a média e o desvio padrão.")
    except FileNotFoundError:
        print(f"Erro: O arquivo {nome_arquivo} não foi encontrado.")
    except Exception as e:
        print(f"Ocorreu um erro ao processar o arquivo: {e}")
if __name__ == "__main__":
    main()