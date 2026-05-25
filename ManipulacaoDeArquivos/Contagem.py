frase = "Eu amo comer amoras no café da manhã"

#RESULTADO OBTIDO UTILIZANDO O MÉTODO COUNT DIRETAMENTE
print("CONTAGEM DIRETA DO COUNT: (amo) ", frase.count('amo'))
#O resultado dará 2, pois existe "amo" em amora.

#RESULTADO OBTIDO UTILIZANDO A QUEBRA DA FRASE EM PALAVRAS
contador = 0
lista_termos = frase.split()
for termo in lista_termos:
    if termo == 'amo':
        contador += 1
print("CONTAGEM CORRETA => ", contador)