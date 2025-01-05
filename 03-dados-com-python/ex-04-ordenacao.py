#%%
import pandas as pd

#%%
df = pd.read_csv('/home/vladimir/Documentos/Estudos/python-base/03-dados-com-python/ex-04-ordenacao.csv')
print(df)

#%%
# Ordenar salários em ordem decresciente
salarios_desc = df.sort_values('Salário', ascending=False)
print(salarios_desc)


#%%
# Ordenar por salário e idade
salarios_mult = df.sort_values(['Salário', 'Idade'], ascending=[False, True])
print(salarios_mult)
