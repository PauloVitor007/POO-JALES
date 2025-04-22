class Livro:
    def __init__(self, titulo, autor, isbn, copias_totais):
        self.__titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.__copias_totais = copias_totais
        self.__emprestimos = []

    def get_emprestimos(self):
        return self.__emprestimos

    def adicionar_emprestimo(self, emprestimo):
        if self.get_quantidade_disponiveis() > 0:
            self.__emprestimos.append(emprestimo)
            return True
        else:
            print("Não há mais livros disponíveis para empréstimo.")
            return False

    def remover_emprestimo(self, emprestimo):
        if emprestimo in self.__emprestimos:
            self.__emprestimos.remove(emprestimo)
            return True
        else:
            print("Empréstimo não encontrado.")
            return False

    def get_quantidade_disponiveis(self):
        return self.__copias_totais - len(self.__emprestimos)

    def get_disponibilidade(self):
        return f"{self.get_quantidade_disponiveis()}/{self.__copias_totais}"

    def get_titulo(self):
        return self.titulo

    def get_titulo(self):
        return self._titulo