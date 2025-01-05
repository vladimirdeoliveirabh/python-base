# %%
import pandas as pd

file_path = '/home/vladimir/Documentos/Estudos/python-base/04-dados-com-python-avancado/06-joins/'

# %%
df_produtos = pd.read_csv(file_path + 'informacoes_produtos.csv')
print(df_produtos)

# %%
df_valores = pd.read_csv(file_path + 'valores_produtos.csv')
print(df_valores)

# %%
df_produtos_valores = pd.merge(df_produtos,
                               df_valores,
                               on='Produto',
                               how='left',
                               )

df_produtos_valores.fillna(0, inplace=True)

df_produtos_valores['Lucro Bruto'] = df_produtos_valores['Vendas'] - df_produtos_valores['Custos']

print(df_produtos_valores)
