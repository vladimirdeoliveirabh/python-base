#%%
import pandas as pd
file_path = '/home/vladimir/Documentos/Estudos/python-base/03-dados-com-python/'

#%%
df = pd.read_csv(file_path + 'ex-06-produtos-com-estoque-acima-50.csv')
print(df)

#%%
filtro = df['Estoque'] >= 50
produtos = df[filtro]
print(produtos)
