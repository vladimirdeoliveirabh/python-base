import random

tp = tuple((random.randint(1, 100) for _ in range(10)))

# Entrada
num = int(input("Digite um número: "))
esta_na_tupla = 'Sim' if num in tp else 'Não'
soma = sum(tp)
tupla_ordenada = sorted(tp)
tupla_unica = sorted(tuple(set(tp)))

print(f"Tupla original: {tp}")
print(f"3 Primeiros elementos da tupla: {tp[:3]}")
print(f"Último elemento da tupla: {tp[-1]}")
print(f"Seu número está na tupla? {esta_na_tupla}")
print(f"Soma dos elementos da tupla: {soma}")
print(f"Tupla ordenada: {tupla_ordenada}")
print(f"Tupla sem elementos duplicados: {tupla_unica}")
