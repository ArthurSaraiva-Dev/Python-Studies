print("Iterando sobre arquivo")

with open("dados_with.txt", "r") as arquivo:
    for linha in arquivo:
        print(linha)
    print("Fim do arquivo: ", arquivo.name)