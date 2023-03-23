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
