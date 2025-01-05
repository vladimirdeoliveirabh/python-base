# Função fatorial
def fatorial(num):
    if num < 0 or not num.is_integer():
        return 'Não existe fatorial de número negativo ou decimal.'

    num = int(num)

    if num == 0:
        return 1
    else:
        return num * fatorial(num - 1)


# Entrada
n = float(input("Digite um número: "))

# Cálculo fatorial
resultado = fatorial(n)

# Resultado
print(f"Fatorial: {resultado}")
