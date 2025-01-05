# Entrada de dados
n1 = float(input("N1: "))
n2 = float(input("N2: "))

# Operações
soma = n1 + n2
diferenca = abs(n1 - n2)
produto = n1 * n2
divisao = n1 / n2 if n2 != 0 else "Indefinido (divisão por zero)"

# Saída formatada
print("\nResultados")
print(f"Soma: {soma}")
print(f"Diferença: {diferenca}")
print(f"Produto: {produto}")
print(f"Divisão: {divisao:.2f}")
