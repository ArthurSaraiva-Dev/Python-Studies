class Livro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn

class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)
        print(f'[ADD] - "{livro.titulo}" adicionado à biblioteca "{self.nome}" com sucesso!\n')

    def remover_livro(self, isbn):
        for livro in self.livros:
            if livro.isbn == isbn:
                self.livros.remove(livro)
                print(f'[RMV] - "{livro.titulo}" foi removido da biblioteca "{self.nome}"\n')
                return
        print(f'O livro com ISBN [{isbn}] não encontrado na biblioteca "{self.nome}"\n')

    def listar_livros(self):
        if not self.livros:
            print(f'A biblioteca "{self.nome}" não tem livros!\n')
        else:
            print(f'[--- Livros da biblioteca "{self.nome}" ---]\n')
            for livro in self.livros:
                print(f'"{livro.titulo}" por {livro.autor}\n[ISBN: {livro.isbn}]\n')

# Criando livros
l1 = Livro('O senhor dos Anéis', 'J.R.R Tolkien', 12334556)
l2 = Livro('1984', 'George Orwell', 13425436)
l3 = Livro('O Apenhador no Campo de Centeio', 'J.D Salinger', 923954287)

# Criando Bibliotecas
biblioteca = Biblioteca('Biblioteca Do Parque')

# Adicionando Livros a biblioteca
biblioteca.adicionar_livro(l1)
biblioteca.adicionar_livro(l2)
biblioteca.adicionar_livro(l3)

# Removendo Livro
biblioteca.remover_livro(923954287)

# Listando Livros após remoção
biblioteca.listar_livros()
