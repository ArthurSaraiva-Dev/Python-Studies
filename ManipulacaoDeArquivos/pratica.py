import os

arquivo = open("dados3.txt", "r")

conteudo = arquivo.read() #ler arquivo
print("Conteúdo completo: ", repr(conteudo), '\n')

conteudo_releitura = arquivo.read()
print("Conteúdo releitura: ", repr(conteudo_releitura), '\n')

arquivo.close

arquivo_reaberto = open("dados3.txt", "r")

conteudo_reaberto = arquivo_reaberto.read()
print("Conteúdo reaberto: ", repr(conteudo_reaberto), '\n')

arquivo_reaberto.seek(0)
conteudo_seek = arquivo_reaberto.read()
print("Conteúdo completo após o seek", repr(conteudo_seek), '\n')

arquivo_reaberto.close
