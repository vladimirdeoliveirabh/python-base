def fb(num):
    if num <= 0:
        return "Erro: Digite um número inteiro positivo."
    elif num == 1:
        return [0]

    res = [0, 1]
    for n in range(2, num):
        res.append(res[-1] + res[-2])
    return res

# Entrada com validação
try:
    numero = int(input("Digite um número: "))
    if numero <= 0:
        print("Erro: Digite um número inteiro positivo.")
    else:
        resultado = fb(int(numero))
        print(', '.join(map(str, resultado)))
except ValueError:
    print("Erro: Entrada inválida. Digite apenas números inteiros positivos.")
