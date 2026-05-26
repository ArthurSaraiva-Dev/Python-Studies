import os

try:
    os.mkdir("meu_diretorio")
    print("Diretório Criado")
except PermissionError as erro:
    print("Sem permissão para criar diretório")
    print("descrição", erro)
except FileExistsError as erro:
    print("O diretório já existe")    
    print("descrição", erro)

print("Termino do Programa")