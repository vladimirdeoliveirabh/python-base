class Fila:
    def __init__(self):
        self.items = []

    def enqueue(self, items):
        # Adiciona ao final
        self.items.append(items)

    def dequeue(self):
        # Remove do início
        if self.is_empty():
            return "Erro: A fila está vazia"
        return self.items.pop(0)

    def peek(self):
        # Acessa o início
        if self.is_empty():
            return "Erro: A fila está vazia"
        return self.items[0]


    def is_empty(self):
        return len(self.items) == 0


# Testando a fila
fila = Fila()

# Adicionando elementos
fila.enqueue(5)
fila.enqueue(15)
fila.enqueue(25)

print(f"Fila: {fila.items}")

# Removendo um elemento
fila.dequeue()
print(f"Fila atualizada: {fila.items}")
print(f"Próximo da fila: {fila.peek()}")
