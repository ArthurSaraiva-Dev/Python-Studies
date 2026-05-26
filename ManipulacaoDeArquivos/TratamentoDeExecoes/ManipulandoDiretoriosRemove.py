import os

try:
    os.rmdir("meu_diretorio")
    print("Diretório Removido")
except PermissionError as erro:
    print("Sem permissão para excluir o diretório")
    print("descrição", erro)
except FileExistsError as erro:
    print("O diretório inexistente")    
    print("descrição", erro)
except OSError as erro:
    print("Outro erro")
    print("O diretório está vazio?")
    print("Descrição ", erro)


print("Termino do Programa")