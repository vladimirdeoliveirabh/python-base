import string


def p(f):
    f = f.lower().replace(' ', '')
    f = ''.join(char for char in f if char in string.ascii_letters + string.digits)
    return f == f[::-1]

# Entrada
frase = input("Digite uma frase: ")
resultado = 'Palindroma' if p(frase) else 'Não Palindroma'

# Saida
print(f"A frase: {frase} é {resultado}")
