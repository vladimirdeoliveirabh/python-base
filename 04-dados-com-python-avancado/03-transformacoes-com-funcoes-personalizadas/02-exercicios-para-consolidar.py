# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import unicodedata
import re

file_path = '/home/vladimir/Documentos/Estudos/python-base/04-dados-com-python-avancado/03-transformacoes-com-funcoes-personalizadas/'

# %%
df = pd.read_csv(file_path + 'desempenho_produtos.csv')
print(df)

# %%
# Transformações de Texto
# Crie uma função que padronize os nomes dos produtos (remova espaços extras e capitalize)

def remover_acentuacao(texto):
    texto = unicodedata.normalize('NFKD', texto)
    return ''.join([c for c in texto if not unicodedata.combining(c)])

def padronizar_nomes(texto):
    texto = texto.strip()   # Remove espaços no início e no final
    texto = remover_acentuacao(texto) # Remove acentuação
    texto = re.sub(r'[^a-zA-Z0-9\s]', '', texto) # Remove caracteres especiais
    texto = re.sub(r'\s+', ' ', texto) # Remove espaços múltiplos
    texto = texto.title() # Captaliza
    return texto

df['Produto'] = df['Produto'].apply(padronizar_nomes)
df['Categoria'] = df['Categoria'].apply(padronizar_nomes)
print(df)

# %%
# Margem de lucro
df['Lucro_Bruto'] = df['Vendas'] - df['Custo']
df['Margem'] = (df['Lucro_Bruto'] / df['Vendas']) * 100
print(df)

# %%
# Cálculo por Grupo:
# Agrupe os produtos por categoria e calcule a soma das vendas e a média da margem de lucro.
df_agrupado = df.groupby(['Categoria']).agg(
    Vendas=('Vendas', 'sum'),
    Margem=('Margem', 'mean'),
    Produtos=('Produto', 'count')
)
print(df_agrupado)

# %%
# Relatório Resumido
# Crie um relatório que mostre o total de vendas, lucro total e margem média para cada categoria de produto
df_resumido = df.groupby(['Categoria']).agg(
    Vendas=('Vendas', 'sum'),
    Lucro_Total=('Lucro_Bruto', 'sum'),
    Margem_Media=('Margem', 'mean')
)
print(df_resumido)

# %%
# Identificação de Produtos Premium
# Adicione uma coluna indicando se o produto é "Premium" (margem > 50% e lucro bruto > 500)
df['Premium'] = np.where(
    (df['Margem'] > 30) & (df['Lucro_Bruto'] > 300),
    'Premium',
    'Standard'
)
print(df)

# %%
# Estatísticas Personalizadas
# Crie uma função para calcular estatísticas personalizadas por categoria, incluindo desvio padrão do lucro
total_vendas = df['Vendas'].sum()
custo_total = df['Custo'].sum()
lucro_bruto_total = df['Lucro_Bruto'].sum()
margem_total = (lucro_bruto_total / total_vendas) * 100
margem_media = df['Margem'].mean()
perc_premium = (df['Premium'].value_counts(normalize=True) * 100)
desv_lucro = df['Lucro_Bruto'].std()

stats = pd.DataFrame({
    'Total Vendas': [total_vendas],
    'Custo Total': [custo_total],
    'Lucro Total': [lucro_bruto_total],
    'Margem Total (%)': [margem_total],
    'Margem Média (%)': [margem_media],
    'Desvio Padrão do Lucro': [desv_lucro]
})
print(stats)


# %%
# Visualização dos Dados
sns.barplot(data=df_resumido.reset_index(), x='Categoria', y='Lucro_Total')
plt.title('Lucro Total por Categoria')
plt.show()
