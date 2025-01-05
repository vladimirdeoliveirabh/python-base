#%%
import pandas as pd

#%%
alunos = {'Aluno': ['Reuven', 'Shimon', 'Levi'], 'Idade': [120, 130, 140], 'Nota': [5.8, 6.7, 7.6]}
df = pd.DataFrame(alunos)
print(df)

# %%
filtro = df['Nota'] >= 7.0
print(df[filtro])
