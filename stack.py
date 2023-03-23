# exemplo de uma estrutura de dados em pilha, seguindo a regra LIFO em python

# criação da pilha
def criar_pilha():
    pilha = []  # array
    return pilha

# checa se está vazia


def eh_vazia(pilha):
    return len(pilha) == 0

# adiciona item aa pilha (push)


def push_pilha(pilha, item):
    pilha.append(item)
    print("pushed item:" + item)

# remove item da pilha (pop)


def pop_pilha(pilha):
    if(eh_vazia(pilha)):
        return "pilha vazia"

    return pilha.pop()


# usando as funções de manipulação de pilha
pilha = criar_pilha()
