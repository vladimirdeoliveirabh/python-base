#%%
import pandas as pd
file_path = '/home/vladimir/Documentos/Estudos/python-base/03-dados-com-python/'

#%%
df = pd.read_csv(file_path + 'ex-05-leitura-escrita-de-arquivos.csv')
print(df)

#%%
# Filtrar saldos maiores que 500
filtro = df['Saldo'] >= 500
saldos_maiores_500 = df[filtro]
print(saldos_maiores_500)

#%%
saldos_maiores_500.to_csv(file_path + 'ex-05-saldos_maiores_500.csv')
