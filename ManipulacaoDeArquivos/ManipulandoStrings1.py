 #Funções Essenciais
# - Strip: tira espaços
# - Split: Quebra um texto, sem argumento, quebra nas quebras de linha
# - Join: Junta caracteres utilizando um separador a ser passado

arquivo = open('dadoss.txt', 'r', encoding="utf-8")

conteudo = arquivo.readline()

print("Tipo de conteúdo: ",  type(conteudo))

print("Conteudo retornado pelo readline => \n")

print(repr(conteudo))

prox_cont = arquivo.readline()

print("Próximo conteudo retornado pelo readline => \n")
print(repr(prox_cont))

arquivo.close()