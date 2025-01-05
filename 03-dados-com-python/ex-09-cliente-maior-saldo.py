# %%
import pandas as pd

file_path = '/home/vladimir/Documentos/Estudos/python-base/03-dados-com-python/'

# %%
df = pd.read_csv(file_path + 'ex-09-cliente-maior-saldo.csv')
print(df)

# %%
# Localizar o maior saldo
# idxmax() retorna o índice da linha onde a coluna Saldo possui o maior valor.
# loc seleciona a linha correspondente ao índice retornado.
maior_saldo = df.loc[df['Saldo'].idxmax()]
print(maior_saldo)
