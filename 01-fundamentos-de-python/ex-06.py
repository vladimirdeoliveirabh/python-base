# Primos
def primo(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False

    return True

# Entrada
print("Digite um intervalo")
ini = int(input("Início: "))
fim = int(input("Fim: "))



# Resultado
if ini > fim:
    print("O valor inicial deve ser menor que o valor final.")
else:
    # Lista de primos
    primos = [i for i in range(ini, fim + 1) if primo(i)]

    # Resultado
    print("\nNúmeros primos no intervalo:")
    if primos:
        print(", ".join(map(str, primos)))
    else:
        print("Nenhum número primo foi encontrado no intervalo.")
