# %%
import pandas as pd
import numpy as np

# %%
data = {
    'Produto': ['A', 'B', 'C', 'D', 'E'],
    'Vendas': [500, 300, 800, 200, 700],
    'Categoria': ['Eletrônicos', 'Eletrônicos', 'Móveis', 'Móveis', 'Eletrônicos']
}
df = pd.DataFrame(data)
print(df)

# %%
# Transformações com appy
df['Desconto'] = df['Vendas'].apply(lambda x: 0.1 * x if x > 400 else 0.05 * x)
print(df)

# %%
# Operacões condicionais com np.where
df['Classificacao'] = np.where(df['Vendas'] > 600, 'Alta', 'Baixa')
print(df)

# %%
# [0, 300)   → 'Baixa'
# [300, 600) → 'Média'
# [600, 900) → 'Alta'
df['Faixa_Vendas'] = pd.cut(df['Vendas'], bins=[0, 300, 600, 900], labels=['Baixa', 'Média', 'Alta'])
print(df)

# %%
# Pivot Table
pivot = df.pivot_table(values='Vendas', index='Categoria', columns='Classificacao', aggfunc='sum', fill_value=0)
print(pivot)

# %%
# Pivot Table
pivot = df.pivot_table(values='Desconto', index='Categoria', columns='Classificacao', aggfunc='sum', fill_value=0)
print(pivot)
