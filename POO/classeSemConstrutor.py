# Classe sem construtor
# Python não obriga a existencia do construtor
# ele somente é necessário se o objeto a ser instanciado necessitar
# de alguma ação como a inicialização e/ou a atribuição de valores

class A():
    def f(self):
        print('Classe sem construtor')

def main():
    obj_A = A() #Objeto instanciado
    obj_A.f()

if __name__ == '__main__':
    main()

