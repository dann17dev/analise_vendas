"""
Este módulo contém funções para analisar dados de vendas e gerar visualizações gráficas.

Bibliotecas necessárias:
- pandas
- matplotlib

Funções:
- carregar_dados: Carrega os dados de vendas a partir de um arquivo CSV.
- analise_vendas: Realiza a análise dos dados de vendas e gera gráficos.
"""

import pandas as pd
import matplotlib.pyplot as plt
import os

def carregar_dados(caminho_arquivo):
    """
    Carrega os dados de vendas a partir de um arquivo CSV.

    Parâmetros:
    caminho_arquivo (str): O caminho para o arquivo CSV.

    Retorna:
    DataFrame: Um DataFrame contendo os dados de vendas.
    """
    try:
        return pd.read_csv(caminho_arquivo)
    except FileNotFoundError:
        print(f"Erro: O arquivo {caminho_arquivo} não foi encontrado.")
        return None
    except pd.errors.EmptyDataError:
        print("Erro: O arquivo está vazio.")
        return None
    except Exception as e:
        print(f"Erro ao ler o arquivo: {e}")
        return None

def analise_vendas(df):
    """
    Realiza a análise dos dados de vendas e gera gráficos.

    Parâmetros:
    df (DataFrame): Um DataFrame contendo os dados de vendas.
    """
    # Agrupar os dados por produto e calcular a quantidade total vend ida
    vendas_por_produto = df.groupby('produto')['quantidade'].sum().reset_index()

    # Gráfico de barras
    plt.figure(figsize=(10, 6))
    plt.bar(vendas_por_produto['produto'], vendas_por_produto['quantidade'], color='skyblue')
    plt.title('Quantidade Total Vendida por Produto')
    plt.xlabel('Produto')
    plt.ylabel('Quantidade Vendida')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Criar pasta para salvar os gráficos
    if not os.path.exists('graficos'):
        os.makedirs('graficos')

    plt.savefig('graficos/vendas_por_produto.png')
    plt.show()

    # Gráfico de vendas ao longo do tempo
    df['data_venda'] = pd.to_datetime(df['data_venda'])
    vendas_por_data = df.groupby('data_venda')['quantidade'].sum().reset_index()

    plt.figure(figsize=(10, 6))
    plt.plot(vendas_por_data['data_venda'], vendas_por_data['quantidade'], marker='o', color='orange')
    plt.title('Vendas ao Longo do Tempo')
    plt.xlabel('Data')
    plt.ylabel('Quantidade Vendida')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('graficos/vendas_ao_longo_do_tempo.png')
    plt.show()

# Carregar dados e realizar análise
df = carregar_dados('data/vendas.csv')
if df is not None and 'produto' in df.columns and 'quantidade' in df.columns:
    analise_vendas(df)
else:
    print("Erro: O DataFrame não contém as colunas necessárias.")