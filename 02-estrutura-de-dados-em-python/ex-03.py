
def cadastro(nome, idade, notas, media):
    return {'nome': nome, 'idade': idade, 'notas': notas, 'media': media}

# Inicializa aluno
alunos = []

# Entrada de dados
while True:
    nome = input('Digite o nome do aluno: ')
    idade = int(input('Idade: '))
    notas = []

    for i in range(3):
        notas.append(int(input(f'Nota {i+1}: ')))

    media = sum(notas) / 3

    alunos.append(cadastro(nome, idade, notas, media))

    continuar = input('Deseja cadastrar mais um aluno? [S/N] ').strip().upper()
    if continuar == 'N':
        break




# Saída
for aluno in alunos:
    print("\nAluno cadastrado:")
    print(f"Nome: {aluno['nome']}")
    print(f"Idade: {aluno['idade']}")
    print(f"Notas: {aluno['notas']}")
    print(f"Média: {aluno['media']:.2f}")
    print(f"Maior nota: {max(aluno['notas'])}")
    print(f"Menor nota: {min(aluno['notas'])}")
