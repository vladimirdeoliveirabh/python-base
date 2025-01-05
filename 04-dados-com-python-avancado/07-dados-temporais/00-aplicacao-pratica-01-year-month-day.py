# %%
import pandas as pd

# %%
# Criando um DataFrame com strings de datas
data = {'Data': ['2024-01-01', '2024-02-15', '2024-03-10']}
df = pd.DataFrame(data)
print(df)

# %%
# Convertendo para datetime
df['Data'] = pd.to_datetime(df['Data'])
print(df)

# %%
# Extraindo ano, mês e dia
df['Ano'] = df['Data'].dt.year
df['Mes'] = df['Data'].dt.month
df['Dia'] = df['Data'].dt.day

print(df)