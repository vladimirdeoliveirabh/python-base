# Entrada de dados
n1 = float(input("Nota 1: "))
n2 = float(input("Nota 2: "))
n3 = float(input("Nota 3: "))

# Validação e resultados
if 0 <= n1 <= 10 and 0 <= n2 <= 10 and 0 <= n3 <= 10:
    media = (n1 + n2 + n3) / 3
    resultado = 'Passou' if media >= 7 else 'Ficou em recuperação' if media >= 5 else 'Reprovou'
    print(f"Média: {media:.2f}")
    print(f"Resultado: {resultado}")
else:
    print("Erro: As notas devem estar entre 0 e 10.")
