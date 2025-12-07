from Conta import Conta

conta = Conta(123, 1000)
saldo1 = conta._Conta__saldo  # Acesso direto ao atributo privado (não recomendado)
print(saldo1)

saldo2 = conta.saldo
print(saldo2)