# Entrada de dados
n = float(input("Digite um número: "))

par_ou_impar = 'Não aplicável (número decimal)' if not n.is_integer() else 'Par' if n % 2 == 0 else 'Impar'
sinal = 'Positivo' if n > 0 else 'Negativo' if n < 0 else 'Zero'

# Saída
print(f"Par ou ímpar: {par_ou_impar}")
print(f"Sinal: {sinal}")
