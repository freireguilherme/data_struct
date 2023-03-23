# exemplo de uma estrutura de dados em fila circular,
# fazendo um melhor uso de memoria do que uma fila simples, escrito em Python

class Fila_Circular():
    # fila circular vai receber um tamanho previo k
    def __init__(self, k):
        self.k = k
        self.fila = [None] * k
        self.inicio = self.fim = -1

    # insere um elemento na fila circular
    def enfileirar(self, item):
        if((self.fim + 1) % self.k == self.inicio):
            print("A fila circular está cheia\n")

        elif(self.inicio == -1):
            self.inicio = 0
            self.fim = 0
            self.fila[self.fim] = item

        else:
            self.fim = (self.fim + 1) % self.k
            self.fila[self.fim] = item

    # deletar um item da fila circular
    def desfileirar(self):
        if(self.inicio == -1):
            print("A fila circular está vazia")

        elif(self.inicio == self.fim):
            temp = self.fila[self.inicio]
            self.inicio = -1
            self.fim = -1
            return temp
        else:
            temp = self.fila[self.inicio]
            self.inicio = (self.inicio + 1) % self.k
            return temp

    def imprimirFila(self):
        if(self.inicio == -1):
            print("Fila circular vazia")

        elif (self.fim >= self.inicio):
            for i in range(self.inicio, self.fim + 1):
                print(self.fila[i], end=" ")
            print()

        else:
            for i in range(self.inicio, self.k):
                print(self.fila[i], end=" ")
            for i in range(0, self.fim + 1):
                print(self.fila[i], end=" ")
            print()


# instanciar uma fila circular de tamanho 5
fila_circular = Fila_Circular(5)
fila_circular.enfileirar(str("eu"))
fila_circular.enfileirar(str("me"))
fila_circular.enfileirar(str("chamo"))
fila_circular.enfileirar(str("g"))
fila_circular.enfileirar(str("u"))
# vai apontar que a fila esta cheia e nao vai inserir esse item
fila_circular.enfileirar(str("i"))

print("Fila inicial")
fila_circular.imprimirFila()

fila_circular.desfileirar()
print("Fila depois de remover um item")
fila_circular.imprimirFila()

fila_circular.desfileirar()
print("Fila depois de remover mais um item")
fila_circular.imprimirFila()
