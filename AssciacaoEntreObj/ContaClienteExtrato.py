import datetime
from Extrato import Extrato

class ContaClienteExtrato:
    def __init__(self,clientes, numero, saldo):
        self.clientes = clientes
        self.numero = numero
        self.saldo = saldo
        self.data_abertura = datetime.datetime.today()
        self.extrato = Extrato() # Inicializa a composição com um objeto Extrato

    def depositar(self, valor):
        self.saldo += valor
        self.extrato.transacoes.append(["\nDEPÓSITO", valor, "\nDATA", datetime.datetime.today()])

    def sacar(self, valor):
        if self.saldo < valor:
            print('Saldo insuficiente para realizar o saque.')
        else:
            self.saldo -= valor
            self.extrato.transacoes.append(["\nSAQUE", valor,"\nDATA", datetime.datetime.today()])

    def transfereValor(self, contaDestino, valor):
        if self.saldo < valor:
            print('Saldo insuficiente para realizar a tranferência.')
        else:
            self.saldo -= valor
            contaDestino.depositar(valor)
            self.extrato.trasacoes.append(["\nTRANSFERÊNCIA", valor, "\nDATA", datetime.datetime.today()])
            return 'Transferência realizada com sucesso.'
        
    def gerarSaldo(self):
        print(f'O saldo da conta [{self.numero}] é R$ {self.saldo}.')