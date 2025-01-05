import random

def gerar_lista(i, f):
    if i > f:
        return "Erro: O valor inicial deve ser menor que o valor final."
    else:
        return [random.randint(i, f) for _ in range(10)]


# Entrada
inicio_lista = int(input("Digite o valor inicial da lista: "))
fim_lista = int(input("Digite o valor final da lista: "))

# Gerar lista
try:
    if inicio_lista > fim_lista:
        raise ValueError
    else:
        lista = gerar_lista(inicio_lista, fim_lista)

        # Gerar dados
        maior_numero = max(lista)
        menor_numero = min(lista)
        soma = sum(lista)
        pares = [x for x in lista if x % 2 == 0]
        impares = [x for x in lista if x % 2 != 0]
        lista_ordenada = sorted(lista)

        print(f"Lista original: {lista}")
        print(f"Lista ordenada: {lista_ordenada}")
        print(f"Maior número: {maior_numero}")
        print(f"Menor número: {menor_numero}")
        print(f"Soma: {soma}")
        print(f"Números pares: {pares}")
        print(f"Números ímpares: {impares}")
except ValueError:
    print("Erro: O valor inicial deve ser menor que o valor final.")
