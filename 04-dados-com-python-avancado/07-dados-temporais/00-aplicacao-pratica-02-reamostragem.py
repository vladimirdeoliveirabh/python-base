# %%
import pandas as pd

# %%
data = {
    'Data': pd.date_range(start='2024-01-01', periods=12, freq='D'),
    'Vendas': [100, 150, 200, 250, 300, 350, 100, 150, 200, 250, 300, 350]
}

df = pd.DataFrame(data).set_index('Data')
print(df)

# %%
# Reamostrando para frequência semanal (soma das vendas)
df_semana = df.resample('W').sum()
print(df_semana)

# %%
# Calculando diferenças de tempo
df['Diferenca'] = df.index.to_series().diff()
print(df)