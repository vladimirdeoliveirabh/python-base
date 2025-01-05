# %%
import pandas as pd

# %%
data = {
    'Categoria': ['Eletrônicos', 'Eletrônicos', 'Móveis', 'Móveis'],
    'Subcategoria': ['Smartphones', 'Notebooks', 'Sofás', 'Camas'],
    'Vendas': [1200, 3000, 800, 1000],
    'Custo': [800, 2000, 500, 700]
}
df = pd.DataFrame(data)
print(df)

# %%
# Configurando MultIndex
df.set_index(['Categoria', 'Subcategoria'], inplace=True)
print(df)

# %%
# Acessando Dados com MultIndex
print(df.loc['Eletrônicos'])

# %%
# Resetando o índice para voltar ao formato padrão
df_reset = df.reset_index()
print(df_reset)

# %%
# Operações com MultIndex
df_summary = df.groupby(level=0).sum() # Agrega no nível 'Categoria'
print(df_summary)