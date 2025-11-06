class Conta:
    def __init__(self, clientes, numero, saldo):
        self.clientes = clientes
        self.numero = numero
        self.saldo = saldo
    
    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo < valor:
            print('Saldo insuficiente para realizar o saque.')
        else:
            self.saldo -= valor
            print(f'Saque de R$ {valor} realizado com sucesso.')

    def transfereValor(self, contaDestino, valor):
        if self.saldo < valor:
            print('Saldo insuficiente para realizar a transferência.')
        else:
            self.saldo -= valor
            contaDestino.depositar(valor)
    
    def gerarSaldo(self):
        print(f'O saldo da conta [{self.numero}] é R$ {self.saldo}.')