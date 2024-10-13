import requests
#Chamando a bibloteca para trabalhar com ela

def parse_users():
#Definindo a função
    response = requests.get("https://jsonplaceholder.typicode.com/users")
    #Pegando os dados
    users = response.json()
    #Infelizmente consegui chegar apenas até essa parte nesse desafio, mas creio que seja pouca coisa para finalizar o código
    
   
