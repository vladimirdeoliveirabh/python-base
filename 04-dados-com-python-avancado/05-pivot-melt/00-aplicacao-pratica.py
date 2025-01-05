# %%
import pandas as pd

# %%
# DataFrame exemplo
data = {
    'Ano': [2023, 2023, 2024, 2024],
    'Categoria': ['Eletrônicos', 'Móveis', 'Eletrônicos', 'Móveis'],
    'Vendas': [1200, 800, 1500, 900],
    'Lucro': [300, 200, 400, 250]
}
df = pd.DataFrame(data)

# %%
# Converte dados no formato "longo" (long format) para "largo" (wide format).
# Útil para criar tabelas dinâmicas e sumarizar informações.
# Permite agregar valores, como somas, médias, contagens, etc.
pivot = df.pivot_table(
    values = 'Vendas',
    index='Ano',
    columns='Categoria',
    aggfunc='sum',
    fill_value=0
)
print(pivot)

# %%
# Converte dados no formato "largo" para "longo".
# Útil para reorganizar colunas em linhas, facilitando a
# análise ou integração com bibliotecas como Seaborn.
melted = pd.melt(df, id_vars=['Ano', 'Categoria'],
                 value_vars=['Vendas', 'Lucro'],
                 var_name='Métrica',
                 value_name='Valor')
print(melted)
