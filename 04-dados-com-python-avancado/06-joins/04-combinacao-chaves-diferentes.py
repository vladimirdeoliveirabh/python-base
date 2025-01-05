# %%
import pandas as pd

file_path = '/home/vladimir/Documentos/Estudos/python-base/04-dados-com-python-avancado/06-joins/'

# %%
df_produtos = pd.read_csv(file_path + 'produtos_joins.csv')
print(df_produtos)

# %%
df_descontos = pd.read_csv(file_path + 'descontos_joins.csv')
print(df_descontos)

# %%
df_produtos_descontos = pd.merge(df_produtos,
                                 df_descontos,
                                 left_on='Produto',
                                 right_on='Item',
                                 how='left')

df_produtos_descontos.fillna(0, inplace=True)

df_produtos_descontos = df_produtos_descontos[['Produto', 'Vendas', 'Desconto']]

print(df_produtos_descontos)