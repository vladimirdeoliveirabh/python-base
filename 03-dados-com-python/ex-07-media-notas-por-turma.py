#%%
import pandas as pd
file_path = '/home/vladimir/Documentos/Estudos/python-base/03-dados-com-python/'

#%%
df = pd.read_csv(file_path + 'ex-07-media-notas-por-turma.csv')
print(df)


#%%
df_media = df.groupby('Turma')['Nota'].mean().round(1)
print(df_media)
