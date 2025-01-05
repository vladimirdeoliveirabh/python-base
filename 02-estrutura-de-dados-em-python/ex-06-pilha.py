class Pilha:
    def __init__(self):
        self.items = []

    def push(self, item):
        # Adiciona ao topo
        self.items.append(item)

    def pop(self):
        # Remove do topo
        if self.is_empyt():
            return "Erro: A pilha está vazia"
        return self.items.pop()

    def peek(self):
        # Acessa o topo
        if self.is_empyt():
            return "Erro: A pilha está vazia"
        return self.items[-1]

    def is_empyt(self):
        # Verifica se a pilha está vazia
        return len(self.items) == 0


pilha = Pilha()

pilha.push(10)
pilha.push(20)
pilha.push(30)

print(pilha.peek())
print(pilha.pop())
print(pilha.peek())
print(pilha.is_empyt())
pilha.pop()
pilha.pop()
print(pilha.is_empyt())
