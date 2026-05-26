#A cifra ZENIT POLAR é uma cifra de substituição simples
#Letras de ZENIT são substituidas por letras correspondentes
#de "POLAR" e vise-versa

def zenit_polar_replace(text):
    #Aplicando:
    replacements = [('z', 'p'), ('e', 'o'), ('n', 'l'), ('i', 'a'), ('t', 'r'),
                    ('Z', 'P'), ('E', 'O'), ('N', 'L'), ('I', 'A'), ('T', 'R')]
    for old, new in replacements:
        text = text.replace(old, new)
    return text

def main():
    frase = "The quick brown fox jumps over the lazy dog"
    frase = frase.title() # Primeira letra de cada palavra para maiúscula

    #Dividir a frase em palavras
    words = frase.split()

    #Processar cada palavra na lista utilizando o ZENIT POLAR
    coded_words = [zenit_polar_replace(word) for word in words]

    # Juntar todas as palavras codificadas em uma frasa
    coded_frase = " ".join(coded_words)
    print("Original: ", frase)
    print("CODED: ", coded_frase)

if __name__ == "__main__":
    main()