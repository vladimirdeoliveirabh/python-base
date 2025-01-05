# %%
import pandas as pd

file_path = '/home/vladimir/Documentos/Estudos/python-base/03-dados-com-python/'

# %%
df = pd.read_csv(file_path + 'ex-10-filtrar-vendas-acima-1000.csv')
print(df)

# %%
filtro = df['Valor'] > 1000
df_filtrado = df[filtro]
print(df_filtrado)
