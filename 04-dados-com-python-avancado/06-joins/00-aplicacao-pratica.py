# %%
import pandas as pd

# %%
# Criando DataFrames
df1 = pd.DataFrame({
    'Produto': ['A', 'B', 'C'],
    'Vendas': [500, 300, 400]
})
df2 = pd.DataFrame({
    'Produto': ['A', 'B', 'D'],
    'Custo': [200, 150, 100]
})

# %%
# Inner Join
df_inner = pd.merge(df1,
                    df2,
                    on='Produto',
                    how='inner')

df_inner['Lucro'] = df_inner['Vendas'] - df_inner['Custo']
print(df_inner)

# %%
# Outer Join: Retorna todos os registros de ambos os DataFrames, preenchendo valores ausentes com NaN.
df_outer = pd.merge(df1,
                    df2,
                    on='Produto',
                    how='outer')
print(df_outer)

# %%
# Join com chaves diferentes
df3 = pd.DataFrame({
    'Item': ['A', 'B', 'C'],
    'Desconto': [10, 20, 15]
})

df_join_df3 = pd.merge(df1,
                       df3,
                       left_on='Produto',
                       right_on='Item',
                       how='left')

df_join_df3 = df_join_df3[['Produto', 'Vendas', 'Desconto']]

print(df_join_df3)