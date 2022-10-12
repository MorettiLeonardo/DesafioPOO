class Banco():
    def __init__(self):
        self.clientes = []
        self.agencias = [1111, 2222, 3333]
        self.contas = []

    def inserir_cliente(self, cliente):
        self.clientes.append(cliente)

    def inserir_conta(self, conta):
        self.contas.append(conta)

    def mostrar_cliente(self):
        for cliente in self.clientes:
            print(f"Cliente: {cliente.nome}, Cpf: {cliente.cpf}")

    def verificar_cliente(self, cliente):
        if cliente not in self.clientes:
            return False
        
        if cliente.conta not in self.contas:
            return False
        
        if cliente.conta.agencia not in self.agencias:
            return False
        
        return True
