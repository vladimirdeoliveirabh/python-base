def soma(valores):
    try:
        valores = valores.split()
        numeros = [abs(int(x)) for x in valores]
        return sum(numeros)
    except ValueError:
        return "Erro: Insira apenas números inteiros"

# Entrada
v = input("Digite os valores: ")
resultado = soma(v)

# Saída
if isinstance(resultado, int):
    print(f"Soma: {resultado}")
else:
    print(resultado)
