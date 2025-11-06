# Realizando Tranferencias entre Contas

class Conta:
    def __init__ (self, numero, cpf, nomeTitular, saldo):
        self.numero = numero
        self.cpf = cpf
        self.nomeTitular = nomeTitular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            return True
        
    def gerarExtrato(self):
        print(f'Titular: {self.nomeTitular}\nNúmero: {self.numero}\nCPF: {self.cpf}\nSaldo: {self.saldo}')

    def tranfereValor(self, contaDestino, valor):
        if self.saldo < valor:
            return ('Não foi possível realizar a transferência. Saldo insuficiente.')
        else:
            contaDestino.depositar(valor)
            self.saldo -= valor
            return ('Transferência realizada com sucesso.')
        
def main():
    c1 = Conta(1, 123, 'Arthur Saraiva', 1500)
    c2 = Conta(2, 456, 'Rayssa Peres', 2000)

    print('SALDOS INICIAIS:\n')
    print(f'{c1.nomeTitular}: R$ {c1.saldo}')
    print(f'{c2.nomeTitular}: R$ {c2.saldo}\n')

    c1.tranfereValor(c2, 500)
    print('SALDOS APÓS TRANFERÊNCIA DE R$ 500,00 DA CONTA DE ARTHUR PARA RAYSSA:\n')
    print(f'{c1.nomeTitular}: R$ {c1.saldo}')
    print(f'{c2.nomeTitular}: R$ {c2.saldo}\n')

if __name__ == '__main__':
    main()