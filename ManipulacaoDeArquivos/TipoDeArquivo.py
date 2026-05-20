import os

#Criando arquivos
arquivo = open("data.txt", 'w', encoding='utf-8')
arquivo2 = open("data2.txt", 'r', encoding='utf-8')

# Exibe os atributos do arquivo
print("Nome do arquivo:", arquivo.name) #nome
print("Modo do arquivo:", arquivo.mode) #modo
print("Arquivo fechado?:", arquivo.closed) #verifica se está fechado

arquivo.close() #fechando arquivo
print("Está fechado agora?:", arquivo.closed)

#Lendo o Conteúdo de um arquivo
print("-----------------------------------------------")
print("Utilizando READ")

conteudo = arquivo2.read() #leitura do conteúdo
print("Tipo do Conteúdo:", type(conteudo)) #tipo do conteúdo
print("Conteúdo do arquivo2:", repr(conteudo)) #exibe o conteúdo
arquivo2.close #fecha o arquivo

print("-----------------------------------------------")
print("Utilizando READLINE")

conteudo2 = arquivo2.readline()
print("Tipo do Conteúdo:", type(conteudo2)) #tipo do conteúdo
print("Conteúdo do arquivo2:", repr(conteudo2)) #exibe o conteúdo

prox_conteudo = arquivo2.readline()
print("Próxmo conteúdo: ", repr(prox_conteudo))


print("-----------------------------------------------")
print("Utilizando READLINES")

conteudo3 = arquivo2.readlines()
print("Tipo do Conteúdo:", type(conteudo3)) #tipo do conteúdo
print("Conteúdo do arquivo2:", repr(conteudo3)) #exibe o conteúdo

