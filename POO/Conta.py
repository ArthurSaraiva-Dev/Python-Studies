# Criando uma classe
# Self é uma forma da classe se referir a ela mesma
# --init-- é o método construtor que cria o objeto da classe

class Conta():
    def __init__(self, numero, cpf, nomeTitular, saldo):
        self.numero = numero
        self.cpf = cpf
        self.nomeTitular = nomeTitular
        self.saldo = saldo

def main():
    c1 = Conta(1, 1, 'Arthur', 1500)
    print(f'Nome do Titular: {c1.nomeTitular}')
    print(f'Número da conta: {c1.numero}')
    print(f'CPF do titular: {c1.cpf}')
    print(f'Saldo em conta: {c1.saldo}')

# Mostrando:
# Nesse caso, se a condição do IF for True
# Então o corpo do IF será executado

if __name__ == '__main__':
    main()