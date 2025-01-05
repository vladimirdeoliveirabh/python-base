# %%
import pandas as pd
import numpy as np

file_path = '/home/vladimir/Documentos/Estudos/python-base/04-dados-com-python-avancado/03-transformacoes-com-funcoes-personalizadas/'

# %%
df = pd.read_csv(file_path + 'vendas_custos.csv')
print(df)

# %%
# Verificação de dados ausentes
if df.isnull().any().any():
    print("Dados ausentes detectados!")
else:
    print("Nenhum dado ausente detectado.")

# %%
# Cálculo de Lucro Bruto (vetorizada)
df['Lucro_Bruto'] = df['Vendas'] - df['Custo']
print(df)

# %%
# Classificação de Lucro (com np.select)
condicoes = [
    df['Lucro_Bruto'] > 500,
    (df['Lucro_Bruto'] > 200) & (df['Lucro_Bruto'] <= 500),
    df['Lucro_Bruto'] <= 200
]
escolhas = ['Lucro Alto', 'Lucro Médio', 'Lucro Baixo']
df['Classificacao_Lucro'] = np.select(condicoes, escolhas, default='Não classificado')
print(df)

# %%
# Cálculo de Margem (vetorizado)
df['Margem'] = df['Lucro_Bruto'] / df['Vendas'] * 100
print(df)

# %%
# Flag de Alta Margem (com np.where)
df['Alta_Margem'] = np.where(df['Margem'] >= 40, 'Sim', 'Não')
print(df)

# %%
# Normalização de Vendas (vetorizada)
df['Venda_Normalizada'] = (
        (df['Vendas'] - df['Vendas'].min()) /
        (df['Vendas'].max() - df['Vendas'].min())
)
print(df)

