# Métodos de classes
# definem as ações que o objeto pode realizar

class Conta:
    def __init__(self, numero, cpf, nomeTitular, saldo):
        self.numero = numero
        self.cpf = cpf
        self.nomeTitular = nomeTitular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor

    def gerar_extrato(self):
        print(f'Titular: {self.nomeTitular}\nNúmero: {self.numero}\nCPF: {self.cpf}\nSaldo: {self.saldo}')

def main():
    c1 = Conta(1, 1, 'Arthur', 0)
    print('[--- EXTRATO INCIAL ---]')
    c1.gerar_extrato()
    c1.depositar(300)
    print('\n[--- EXTRATO APÓS DEPÓSITO ---]')
    c1.gerar_extrato()
    c1.sacar(100)
    print('\n[--- EXTRATO APÓS SAQUE ---]')
    c1.gerar_extrato()
    

if __name__ == '__main__':
    main()

