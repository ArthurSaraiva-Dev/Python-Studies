with open('dadoss.txt', encoding="utf-8") as arquivo:
    contador = 0
    print("REPRESENTAÇÃO DO ARQUIVO")
    for linha in arquivo:
        print(repr(linha))
        if linha:
            contador += 1
    print("Total de linhas = ", contador)

with open('dadoss.txt', encoding="utf-8") as arquivo:
    contador = 0
    print("REPRESENTAÇÃO DO ARQUIVO PÓS STRIP")
    for linha in arquivo:
        linha_limpa = linha.strip()
        print(repr(linha_limpa))
        if linha_limpa:
            contador += 1
    print("TOTAL DE LINHAS = ", contador)