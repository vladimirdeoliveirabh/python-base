class Deque:
    def __init__(self):
        self.items = []

    def append(self, item):
        self.items.append(item)

    def appendleft(self, item):
        self.items.insert(0, item)

    def pop(self):
        if self.is_empty():
            return "Erro: A fila está vazia"
        return self.items.pop()

    def popleft(self):
        if self.is_empty():
            return "Erro: A fila está vazia"
        return self.items.pop(0)

    def is_empty(self):
        return len(self.items) == 0


fila = Deque()

fila.append(5)
fila.append(15)
fila.append(25)

print(fila.items)


fila.appendleft(10)

print(fila.items)

fila.append(100)

print(fila.items)

fila.pop()

print(fila.items)

fila.popleft()

print(fila.items)
