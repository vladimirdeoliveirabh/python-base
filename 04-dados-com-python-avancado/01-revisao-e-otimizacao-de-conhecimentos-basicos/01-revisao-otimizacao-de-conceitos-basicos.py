# %%
import pandas as pd

# %%
# Criando um DataFrame simples
data = {
    'Produto': ['A', 'B', 'C', 'D'],
    'Preço': [10.0, 20.5, 15.0, 30.0],
    'Quantidade': [100, 150, 200, 80]
}
df = pd.DataFrame(data)

# %%
print("DataFrame Original:")
print(df)

# %%
# Selecionando uma coluna
print("\nColuna 'Preço':")
print(df['Preço'])

# %%
# Adicionando uma nova coluna
df['Total_Vendas'] = df['Preço'] * df['Quantidade']
print("\nDataFrame com a coluna 'Total':")
print(df)

# %%
# Alterando o índice
df.set_index('Produto', inplace=True)
print("\nDataFrame com novo índice:")
print(df)

# %%
# Filtrando produtos com vendas totais acima de 500
filtro = df['Total_Vendas'] > 2000
print(df[filtro])
