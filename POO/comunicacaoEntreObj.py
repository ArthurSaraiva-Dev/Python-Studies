# Comunicação entre objetos na memória
# Uma classe pode se comunicar com outra classe através de métodos e atributos.

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
            return True
        
    def gerarExtrato(self):
        print(f'Titular: {self.nomeTitular}\nNúmero: {self.numero}\nCPF: {self.cpf}\nSaldo: {self.saldo}')

def main():
    c1 = Conta(1, 123, 'Arthur Saraiva', 0)
    c2 = Conta(2, 456, 'Rayssa Peres', 0)

    # Verificando endereço de memória dos objetos
    if (c1 != c2):
        print('[--- Endereços de memória diferentes. ---]')

    print(c1)
    print(c2)

    print(c1.saldo)
    print(c2.saldo)
    c1.depositar(300)
    print(c1.saldo)
    print(c2.saldo)

    c1 = c2  # c1 agora referencia o mesmo objeto que c2
    if (c1 == c2):
        print('[--- Endereços de memória iguais. ---]')

    print(c1.saldo)
    print(c2.saldo)
    c1.depositar(1000)
    print(c1.saldo)
    print(c2.saldo)

if __name__ == '__main__':
    main()