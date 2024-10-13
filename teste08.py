import requests
#Chamando a bibloteca para trabalhar com ela

def contar_tasks():
#Definindo a função

    response = requests.get("https://jsonplaceholder.typicode.com/todos")
    #Pegando os dados
    tasks = response.json()
    #Definindo os dados como uma variável
    completas = sum(1 for task in tasks if task["completed"])
    #Criando um contador para task completa
    pendentes = len(tasks) - completas
    #Criando um contador para task pendentes, que basicamente é todas as tasks menos as completas
    return completas, pendentes

completas, pendentes = contar_tasks()
print(f"Tasks completas: {completas}, pendentes: {pendentes}")
#Printando cada valor