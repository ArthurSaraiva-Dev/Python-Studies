# Métodos com retorno
# Válida o estado de um objeto

class Conta():
    def __init__(self, numero, cpf, nomeTitular, saldo):
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

    def gerar_extrato(self):
        print(f'Titular: {self.nomeTitular}\nNúmero: {self.numero}\nCPF: {self.cpf}\nSaldo: {self.saldo}')

# Testando o método com retorno
def main():
    c1 = Conta(1, 123, 'Arthur Saraiva', 1200)

    valor_saque = 100
    resultado_saque = c1.sacar(valor_saque)

    # VALIDANDO O RETORNO DO MÉTODO SACAR
    if resultado_saque:
        print(f'O saque de R${valor_saque} foi realizado com sucesso!')
        print(f'Saldo atual: R${c1.saldo}')
    else:
        print(f'Saldo insuficiente para realizar o saque.')

if __name__ == '__main__':
    main()
