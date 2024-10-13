class ContaBancaria:
    #Criação do id que vai aumentando conforme os números dos usuários
    _id_incremental = 1

    #Definindo cada atributo
    def __init__(self, nome, cpf):
        self.id = ContaBancaria._id_incremental
        ContaBancaria._id_incremental += 1
        self.nome = nome
        self.cpf = cpf
        self.saldo = 0

    #Criando e definindo a função depositar
    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R$ {valor} realizado. Saldo atual: R$ {self.saldo}")

    #Criando e definindo a função sacar
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R$ {valor} realizado. Saldo atual: R$ {self.saldo}")
        else:
            print("Saldo insuficiente")

# Exemplo de uso
conta = ContaBancaria("Rafael", "000.000.000-00")
conta.depositar(100)
conta.sacar(50)