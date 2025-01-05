# %%
import pandas as pd
import matplotlib.pyplot as plt

file_path = '/home/vladimir/Documentos/Estudos/python-base/04-dados-com-python-avancado/04-trabalhando-com-indices-hierarquicos/'

# %%
df = pd.read_csv(file_path + 'regioes_multiindex.csv')
print(df)

# %%
df = df.set_index(['Ano', 'Região', 'Mês'])
print(df)

# %%
df.sort_index()
df_norte = df.loc[(slice(None), 'Norte'), :]
print(df_norte)

# %%
df_total_regiao = df.groupby(level=1).sum()
print(df_total_regiao)
