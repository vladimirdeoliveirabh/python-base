# Tabuada
def tabuada(num, oper, inter):
    for i in range(1, inter + 1):
        if oper == '+':
            resultado = num + i
        elif oper == '-':
            resultado = num - i
        elif oper == '*':
            resultado = num * i
        else:
            resultado = num / i
        print(f"{num} {oper} {i} = {resultado:.2f}")

# Entrada
numero = int(input("Digite um número: "))
operacao = input("Operador: ")
intervalo = int(input("Intervalo: "))

# Saída
if operacao not in ['+', '-', '*', '/']:
    print("Erro: Operador inválido.")
else:
    tabuada(numero, operacao, intervalo)
