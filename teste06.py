lista = ["joao", "ana", "joana", "joao", "ricardo", "joao"]
#Lista bruta

for i in range(len(lista)):
#Estrutura de repetição para passar em cada item da lista
    if lista[i] == "joao":
    #Condição que caso o item seja igual a "joao"
        lista[i] = "maria"
        #Vira "maria"

print(lista)
#Printando a nova lista
#Creio que a maneira que fiz se encaixa em outra linguagens pela lógica, pois não usa sintaxes especificas do python
