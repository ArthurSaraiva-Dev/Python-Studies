# utilizando métodos decorados

class Conta:
    def __init__(self, numero):
        self.numero = numero
        self._saldo = 0 #

    # Utilizando o decorador @property, pode-se proteger os atributos
    # e acessálos somente por meio de métodos decorados
    @property #definindo método decorado
    def saldo(self):
        return self._saldo
    
    # O decorador @setter força todas as alterações de valor dos 
    # atributos privados a passas por esses métodos
    @saldo.setter
    def saldo(self, saldo):
        if saldo < 0:
            print("Saldo inválido")
        else:
            self._saldo = saldo

def main():
    conta = Conta(1)
    conta.saldo = 1000 # usando o saldo.setter
    print(f"Saldo da conta: {conta.saldo}")

if __name__ == "__main__":
    main()