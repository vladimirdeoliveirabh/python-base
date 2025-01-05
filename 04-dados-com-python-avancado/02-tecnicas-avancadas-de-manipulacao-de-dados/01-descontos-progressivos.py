# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file_path = '/home/vladimir/Documentos/Estudos/python-base/04-dados-com-python-avancado/02-tecnicas-avancadas-de-manipulacao-de-dados/'

# %%
df_vendas = pd.read_csv(file_path + 'vendas.csv')
print(df_vendas)

# %%
# Calcule o desconto para vendas
df_vendas['Desconto_Perc'] = (pd.cut(df_vendas['Vendas'], bins=[0, 500, 1000, np.inf], labels=[0.05, 0.1, 0.15])
                              .astype(float))

df_vendas['Desconto'] = df_vendas['Vendas'] * df_vendas['Desconto_Perc']
print(df_vendas)

# %%
# Classificação por Intervalos
df_vendas['Classificacao'] = pd.cut(df_vendas['Vendas'], bins=[0, 500, 1000, np.inf], labels=['Baixa', 'Média', 'Alta'])
print(df_vendas)

# %%
# Operações Condicionais: Adicione uma coluna indicando se a venda ultrapassou a meta de 600 unidades
df_vendas['Meta_Atingida'] = df_vendas['Vendas'].apply(lambda x: 'Sim' if x > 600 else 'Não')
print(df_vendas)

# %%
# Tabela Dinâmica: Crie uma tabela dinâmica com as vendas totais por categoria e classificação de vendas (Alta, Média, Baixa)
tabela_dianmica = df_vendas.pivot_table(values='Vendas',
                                        index=['Categoria'],
                                        columns=['Classificacao'],
                                        aggfunc='sum',
                                        fill_value=0,
                                        observed=True)
print(tabela_dianmica)


# %%
tabela_dianmica.plot(kind='bar', figsize=(10, 6))
plt.title('Vendas por Categoria e Classificação')
plt.ylabel('Total de Vendas')
plt.xlabel('Categoria')
plt.show()



# %%
# String Manipulation: Extraia apenas os nomes que contêm a palavra "Eletrônicos"
df_produtos = pd.read_csv(file_path + 'produtos.csv')

# %%
df_eletronicos = df_produtos[df_produtos['Categoria'] == 'Eletrônicos']
print(df_eletronicos)
