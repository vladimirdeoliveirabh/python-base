# %%
import pandas as pd

file_path = '/home/vladimir/Documentos/Estudos/python-base/03-dados-com-python/'

# %%
df = pd.read_csv(file_path + 'ex-08-contar-produtos-por-categoria.csv')
print(df)

# %%
categoria_qtde = df.groupby('Categoria')['Produto'].count().sort_values(ascending=False)
print(categoria_qtde)
