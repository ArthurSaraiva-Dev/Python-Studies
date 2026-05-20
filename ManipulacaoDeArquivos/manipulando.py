import os


arquivo1 = open("dados1.txt", 'w', encoding='utf-8') #ABRE O ARQUIVO EM MODO WRITE
#CASO NÃO HAJA ARQUIVO, ELE CRIARÁ AUTOMATICAMENTE
print("Caminho Absoluto ARQUIVO 1: " + os.path.abspath(arquivo1.name)) #PRINTA O CAMINHO ABSOLUTO DO ARQUIVO

arquivo2 = open("C:/Users/Arthur/Documents/GitHub/Python-Studies/ManipulacaoDeArquivos/dados2.txt", 'w', encoding='utf-8')
#ABRINDO/CRIANDO ARQUIVO ESPECIFICANDO O CAMINHO


arquivo1.write("Hello World!")
arquivo2.write("Olá Mundo!")

print("Caminho Real Arquivo 1: " + os.path.abspath(arquivo1.name)) #CAMINHO ABSOLUTO
print("Caminho Relativo Arquivo 2: " + os.path.relpath(arquivo2.name)) #CAMINHO RELATIVO
print(arquivo1)

arquivo1.close
arquivo2.close