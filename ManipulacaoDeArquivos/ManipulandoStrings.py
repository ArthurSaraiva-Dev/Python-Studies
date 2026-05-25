 #Funções Essenciais
# - Strip: tira espaços
# - Split: Quebra um texto, sem argumento, quebra nas quebras de linha
# - Join: Junta caracteres utilizando um separador a ser passado

arquivo = open('dadoss.txt', 'r', encoding="utf-8")

conteudo = arquivo.read()

print("Tipo de conteúdo: ",  type(conteudo))

print("Conteudo refatorado pelo read => \n")

print(repr(conteudo))

arquivo.close()