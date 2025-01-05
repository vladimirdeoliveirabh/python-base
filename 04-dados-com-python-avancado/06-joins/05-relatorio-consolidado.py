# %%
import pandas as pd

file_path = '/home/vladimir/Documentos/Estudos/python-base/04-dados-com-python-avancado/06-joins/'

# %%
df_vendas = pd.read_csv(file_path + 'relatorio_vendas.csv')
print(df_vendas)

# %%
df_custos = pd.read_csv(file_path + 'relatorio_custos.csv')
print(df_custos)

# %%
df_consolidado = pd.merge(df_vendas,
                          df_custos,
                          on='Produto',
                          how='outer')

df_consolidado.fillna(0, inplace=True)

df_consolidado['Lucro Bruto'] = df_consolidado['Vendas'] - df_consolidado['Custos']

print(df_consolidado)