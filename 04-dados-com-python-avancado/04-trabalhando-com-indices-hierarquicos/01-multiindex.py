# %%
import pandas as pd
import matplotlib.pyplot as plt

file_path = '/home/vladimir/Documentos/Estudos/python-base/04-dados-com-python-avancado/04-trabalhando-com-indices-hierarquicos/'

# %%
df = pd.read_csv(file_path + 'vendas_multiindex.csv')
print(df)

# %%
# Configurando o MultiIndex
df.set_index(['Categoria', 'Subcategoria', 'Mês'], inplace=True)
print(df)

# %%
df_total_categoria = df.groupby(level=0).sum()
print(df_total_categoria)

# %%
df_elet = df.loc['Eletrônicos']
print(df_elet)

# %%
df = df.sort_index() # garantir que o MultiIndex esteja lexicograficamente ordenado
df_cel = df.loc['Eletrônicos', 'Smartphones']
print(df_cel)

# %%
df_total_categoria.plot(kind='bar', figsize=(8, 6), legend=False)
plt.title('Total de Vendas por Categoria')
plt.ylabel('Vendas')
plt.xlabel('Categorias')
plt.show()
