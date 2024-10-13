lista = ["   joao   ","   maria   ","  joana  "]
#Lista com espaços

lista_sem_espaco = [nome.strip() for nome in lista]
#Criando lista nova vazia, usando a função strip() que tira espaços dos cantos nos nomes da lista
print(lista_sem_espaco)
#Printando a lista

