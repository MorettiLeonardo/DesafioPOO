from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, agencia, numero_conta, saldo):
        self.agencia = agencia
        self.numero_conta = numero_conta
        self.saldo = saldo
    
    @abstractmethod
    def sacar(self, valor):
        pass
        
    def depositar(self, valor):
        self.saldo += valor
        self.mostrar_dados()
         
    def mostrar_dados(self):
        print(f"Agencia: {self.agencia}")
        print(f"Numero da conta: {self.numero_conta}")
        print(f"Saldo: {self.saldo}")


class ContaCorrente(Conta):
    def __init__(self, agencia, numero_conta, saldo, limite=100):
        super().__init__(agencia, numero_conta, saldo)
        self.limite = limite

    def sacar(self, valor):
        if (self.saldo + self.limite) < self.limite:
            print(f"Saldo insuficiente, saldo: {self.saldo}")
            return

        self.saldo -= valor
        print(f"Saque de valor R${valor} realizado.")
        self.mostrar_dados()


class ContaPoupanca(Conta):    
    def sacar(self, valor):
        if valor > self.saldo:
            print(f"Saldo insuficiente: {self.saldo}")
            return

        self.saldo -= valor
        self.mostrar_dados()
