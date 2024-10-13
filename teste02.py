import json

dados = {
    "nome": "Loja Exemplo",
    "endereço": {
        "rua": "Rua Exemplo",
        "cidade": "Exemplo City"
    },
    "produtos": [
        {"id": 1, "nome": "Produto A", "preço": 29.99},
        {"id": 2, "nome": "Produto B", "preço": 19.99}
    ]
}
#Dados já convertidos para string

for produto in dados["produtos"]:
#Pegando os produtos na lista
    if produto["nome"] == "Produto B":
    #Verificando se é o produto b
        precob = produto["preço"]
        #Separando o preço do produto b
        print(precob)
        #Printando o preço


        