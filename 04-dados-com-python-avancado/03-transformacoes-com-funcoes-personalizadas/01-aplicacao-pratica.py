# %%
import pandas as pd

file_path = '/home/vladimir/Documentos/Estudos/python-base/04-dados-com-python-avancado/03-transformacoes-com-funcoes-personalizadas/'

# %%
df = pd.read_csv(file_path + 'vendas_custos.csv')
print(df)

# %%
# Cálculo de Lucro Bruto
def lucro_bruto(vendas, custo):
    return vendas - custo

df['Lucro_Bruto'] = df.apply(lambda row: lucro_bruto(row['Vendas'], row['Custo']), axis=1)
print(df)

# %%
# Classificação de Lucro
def classificacao_lucro(lucro):
    if lucro > 500:
        return 'Lucro Alto'
    elif lucro > 200:
        return 'Lucro Médio'
    else:
        return 'Lucro Baixo'

df['Classificacao_Lucro'] = df.apply(lambda row: classificacao_lucro(row['Lucro_Bruto']), axis=1)
print(df)

# %%
# Cálculo de Margem
def margem(lucro, vendas):
    return (lucro / vendas) * 100

df['Margem'] = df.apply(lambda row: margem(row['Lucro_Bruto'], row['Vendas']), axis=1)
print(df)

# %%
# Flag de Alta Margem
def flag_alta_margem(margem):
    if margem >= 40:
        return 'Sim'
    else:
        return 'Não'

df['Alta_Margem'] = df.apply(lambda row: flag_alta_margem(row['Margem']), axis=1)
print(df)

# %%
# Normalização de Vendas
def normalizacao_vendas(v, v_min, v_max):
    return (v - v_min) / (v_max - v_min)

df['Venda_Normalizada'] = df.apply(lambda row: normalizacao_vendas(row['Vendas'], df['Vendas'].min(), df['Vendas'].max()), axis=1)
print(df)
