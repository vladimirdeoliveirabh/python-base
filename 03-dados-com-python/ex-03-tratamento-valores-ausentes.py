# %%
import pandas as pd

# %%
df = pd.read_csv(
    '/home/vladimir/Documentos/Estudos/python-base/03-dados-com-python/ex-03-tratamento-valores-ausentes.csv')
print(df)

#%%
# Verificar valores faltantes
print(df.isnull().sum())


# %%
# Preencher médias das idades e notas
media_idade = int(df['Idade'].mean())
media_nota = round(df['Nota'].mean(), 1)
print(media_idade, media_nota)


#%%
# Preencher dados faltantes com as médias
df['Idade'] = df['Idade'].fillna(media_idade)
df['Nota'] = df['Nota'].fillna(media_nota)
print(df)
