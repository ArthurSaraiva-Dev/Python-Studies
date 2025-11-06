from Conta import Conta
from Cliente import Cliente

cliente1 = Cliente(123, 'João','Rua A, 123')
cliente2 = Cliente(456, 'Carla', 'Rua B, 456')

conta1 = Conta(cliente1, 123456, 1500)
conta2 = Conta(cliente2, 78900, 3500)

conta1.gerarSaldo()
conta1.depositar(700)
conta1.sacar(200)
conta1.gerarSaldo()