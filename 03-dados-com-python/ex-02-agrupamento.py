# %%
import pandas as pd

# %%
df = pd.read_csv('/home/vladimir/Documentos/Estudos/python-base/03-dados-com-python/ex-02-agrupamento.csv')
print(df)

# %%
vendas = df.groupby('Categoria',
                    as_index=False  # Mantém a coluna Categoria como parte do DataFrame e não como índice.
                    )['Vendas'].sum()
print(vendas)
