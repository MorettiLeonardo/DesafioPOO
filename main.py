from banco import Banco
from cliente import Cliente
from conta import ContaCorrente, ContaPoupanca

# Instânciando a classe Banco
banco = Banco()

# Criando clientes
cliente1 = Cliente("Leonardo", 19)
cliente2 = Cliente("Cleber", 45)
cliente3 = Cliente("João", 30)

# Agência 1111(existe na conta Banco), número da conta 123456, saldo 0
conta1 = ContaPoupanca(1111, 304050, 0)
# Agência 2222(existe na classe Banco), número da conta 676869, saldo 0
conta2 = ContaCorrente(2222, 676869, 0)


# Inserindo clientes nas contas
cliente1.inserir_conta(conta1)
cliente2.inserir_conta(conta2)


#Inserindo o cliente1 e a conta1 no Banco
banco.inserir_cliente(cliente1)
banco.inserir_conta(conta1)

#verifcando se o cliente1 pode fazer um deposito
if banco.verificar_cliente(cliente1):
    #Fazendo um deposito
    cliente1.conta.depositar(40)
    #Fazendo um saque
    cliente1.conta.sacar(20)
else:
    print("Cliente não verificado")

print("-="*20)

#verifcando se o cliente2 pode fazer um deposito
if banco.verificar_cliente(cliente2):
    #Fazendo um deposito
    cliente1.conta.depositar(40)
    #Fazendo um saque
    cliente1.conta.sacar(20)
else:
    print("Cliente não verificado")

print("-="*20)

#Inserindo o cliente2 e a conta2 no Banco
banco.inserir_cliente(cliente2)
banco.inserir_conta(conta2)

#verifcando se o cliente2 pode fazer um deposito
if banco.verificar_cliente(cliente2):
    #Fazendo um deposito
    cliente1.conta.depositar(40)
    #Fazendo um saque
    cliente1.conta.sacar(20)
else:
    print("Cliente não verificado")
