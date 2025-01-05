# %%
import pandas as pd

file_path = '/home/vladimir/Documentos/Estudos/python-base/04-dados-com-python-avancado/06-joins/'

# %%
df_vendas = pd.read_csv(file_path + 'vendas_regiao.csv')
print(df_vendas)

# %%
df_custos = pd.read_csv(file_path + 'custos_regiao.csv')
print(df_custos)

# %%
df_vendas_custos = pd.merge(df_vendas,
                            df_custos,
                            on='Região',
                            how='outer')
print(df_vendas_custos)