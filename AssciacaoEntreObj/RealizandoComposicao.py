from Cliente import Cliente
from ContaClienteExtrato import ContaClienteExtrato

cliente1 = Cliente('123', 'João', 'Rua X, 100')
cliente2 = Cliente('456', 'Maria', 'Avenida Y, 250')

conta1 = ContaClienteExtrato(cliente1, 123456, 1500)
conta2 = ContaClienteExtrato(cliente2, 78900, 3500)

conta1.depositar(500)
conta1.sacar(220)
conta1.extrato.extrato(conta1.numero)