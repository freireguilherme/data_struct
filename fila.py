# exemplo de uma estrutura de dados em fila, seguindo a regra FIFO, escrito em Pthon

class Fila:

    def __init__(self):
        self.fila = []

    # adiciona um elemento a fila
    def enfileirar(self, item):
        self.fila.append(item)

    # remove um elemento da fila
    def defileirar(self):
        if len(self.fila) < 1:
            return None
        return self.fila.pop(0)

    # imprime a fila
    def imprimir(self):
        print(self.fila)

    def tamanho(self):
        return len(self.fila)


q = Fila()
q.enfileirar(str("esta"))
q.enfileirar(str("é"))
q.enfileirar(str("uma"))
q.enfileirar(str("fila"))

print("fila antes de remover um item")
q.imprimir()

q.defileirar()

print("fila apos de remover um item")
q.imprimir()
