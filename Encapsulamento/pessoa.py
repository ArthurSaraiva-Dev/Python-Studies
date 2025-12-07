# CALCULANDO IDADE A PARTIR DA DATA DE NASCIMENTO
from datetime import date

class pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
# um metodo para criar
# um objeto pessoa a partir do ano de nascimento

@classmethod
def apartiranonasc(cls, nome, ano):
    return cls(nome, date.today().year - ano)

# metodo estático para verificar se é maior de idade

@staticmethod
def maior(idade):
    return idade >= 18

p1 = pessoa('Arthur', 20)
print(p1.nome)
print(p1.idade)
print(pessoa.maior(p1.idade))
p2 = pessoa.apartiranonasc('Lucas', 2010)
print(p2.nome)
