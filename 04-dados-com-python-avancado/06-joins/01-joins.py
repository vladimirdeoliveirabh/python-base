# %%
import pandas as pd

file_path = '/home/vladimir/Documentos/Estudos/python-base/04-dados-com-python-avancado/06-joins/'

# %%
df_vendas = pd.read_csv(file_path + 'vendas_joins.csv')
print(df_vendas)

# %%
df_custos = pd.read_csv(file_path + 'custos_joins.csv')
print(df_custos)

# %%
# Join e coluna calculada
df_vendas_custos = pd.merge(df_vendas,
                            df_custos,
                            on='Produto',
                            how='inner')

df_vendas_custos['Lucro Bruto'] = df_vendas_custos['Vendas'] - df_vendas_custos['Custo']

print(df_vendas_custos)
