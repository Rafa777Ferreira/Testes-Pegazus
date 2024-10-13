# Criar uma lista vazia
lista = []

# Adicionar itens à lista (fila) usando append
lista.append("item 1")
lista.append("item 2")
lista.append("item 3")

# Exibir a fila
print("Fila inicial:", lista)

# Remover o primeiro item da lista usando pop e o indice
item_removido = lista.pop(0)

# Exibir o item removido e a fila após a remoção
print("Item removido:", item_removido)
print("Fila após remoção:", lista)