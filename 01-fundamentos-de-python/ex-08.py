import string

def cnt_vog_con(f):
    f = ''.join(char for char in f if char in string.ascii_letters)
    f = f.lower()
    l = len(f)
    v = 0
    c = 0
    for letra in f:
        if letra in 'aeiou':
            v += 1
        else:
            c += 1

    return v, c, l


# Entrada
frase = input("Digite uma frase: ")
vogais, consoantes, letras = cnt_vog_con(frase)

# Saída
print(f"A frase tem {vogais} vogais, {consoantes} consoantes e {letras} letras.")
