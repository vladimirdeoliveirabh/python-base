# Escrevendo números no arquivo
with open('dados.txt', 'w') as file:
    for i in range(1, 21):
        file.write(f'{i}\n')

# Lendo e processando os números do arquivo
with open('dados.txt', 'r') as file:
    numeros = [int(line.strip()) for line in file]

# Processamento
soma = sum(numeros)
pares = [n for n in numeros if n % 2 == 0]

# Saída
print(f"Números no arquivo: {numeros}")
print(f"Soma dos números: {soma}")
print(f"Números pares: {pares}")

