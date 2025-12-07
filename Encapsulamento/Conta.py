class Conta:
    def __init__(self, numero, saldo):
        self.__numero = numero #atributo privado
        self.__saldo = saldo #atributo privado

        def sacar(self, valor):
            if self.saldo < valor:
                return False
            else:
                self.__saldo -= valor
                return True

def main():
    conta = Conta(123, 1000)
    saldo = conta.saldo
    print(saldo)

if __name__ == "__main__":
    main()