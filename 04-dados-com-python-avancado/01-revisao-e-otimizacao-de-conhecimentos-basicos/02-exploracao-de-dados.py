# %%
import pandas as pd
import matplotlib.pyplot as plt

file_path = '/04-dados-com-python-avancado/'

# %%
# Carregue um arquivo produtos.csv com colunas Produto, Preço, Quantidade
df = pd.read_csv(file_path + 'produtos.csv')
print(df)

# %%
# Identifique a quantidade de produtos e os tipos de dados
df.info()

# %%
# Adicione uma coluna que calcule o estoque total
df['Estoque_Total'] = df['Preço'] * df['Quantidade']
print(df)

# %%
# Crie uma coluna com o imposto aplicado (10% do preço)
df['Imposto_Aplicado'] = df['Preço'] * 0.1
print(df)

# %%
# Filtre os produtos com preço acima de 20 e salve em um novo DataFrame.
filtro = df['Preço'] > 20
df_filtrado = df[filtro]
print(df_filtrado)

# %%
# Ordene os produtos por preço em ordem decrescente
df.sort_values(by='Preço', ascending=False, inplace=True)
print(df)

# %%
# Calcule a média, mediana e desvio padrão do preço
# Média
media = df['Preço'].mean()
mediana = df['Preço'].median()
desvio = df['Preço'].std()

print(f"Média do preço: {media}")
print(f"Mediana do preço: {mediana}")
print(f"Desvio padrão do preço: {desvio:.2f}")

# %%
# Altere o índice para a coluna "Produto"
# Resete o índice para o formato padrão
df.set_index('Produto', inplace=True)
print(df)

# %%
df.reset_index(inplace=True)
print(df)

# %%
df['Preço'].hist()
plt.title('Distribuição de Preços')
plt.show()