# %%
import pandas as pd

# %%
data = {
    'Produto': ['A', 'B', 'C', 'D'],
    'Vendas': [500, 300, 800, 200],
    'Custo': [300, 200, 500, 150]
}
df = pd.DataFrame(data)
print(df)

# %%
# Função personalizada para calcular margem de lucro
def calcular_margem(vendas, custo):
    return (vendas - custo) / vendas * 100

# Aplicar função personalizada com apply
df['Margem'] = df.apply(lambda row: calcular_margem(row['Vendas'], row['Custo']), axis=1)
print(df)

# %%
# Função para normalizar valores
def normalizar(val, min_val, max_val):
    return (val - min_val) / (max_val - min_val)

# Normalizando a coluna Vendas
df['Vendas_Normalizadas'] = df['Vendas'].apply(lambda x: normalizar(x, df['Vendas'].min(), df['Vendas'].max()))
print(df)

# %%
# Operar em várias colunas ao mesmo tempo
def classificar_produto(vendas, custo):
    margem = vendas - custo
    if margem > 400:
        return 'Alto'
    elif margem > 200:
        return 'Medio'
    else:
        return 'Baixo'

df['Classificacao'] = df.apply(lambda row: classificar_produto(row['Vendas'], row['Custo']), axis=1)
print(df)

# %%
# Classificar os produtos com base na margem
def classificar_margem(margem):
    if margem > 50:
        return 'Alta margem'
    elif margem > 30:
        return 'Média margem'
    else:
        return 'Baixa margem'

df['Classificacao_Margem'] = df['Margem'].apply(classificar_margem)
print(df)

# %%
# Verificar se a margem ultrapassou 50%
df['Margem_Acima_30'] = df['Margem'].apply(lambda x: 'Sim' if x > 30 else 'Não')
print(df[['Margem', 'Margem_Acima_30']])