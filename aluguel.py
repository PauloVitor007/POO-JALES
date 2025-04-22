class Produto:
    def __init__(self, titulo, preco, codigo_de_barras, quantidade):
        self.titulo = titulo
        self.preco = preco
        self.codigo_de_barras = codigo_de_barras
        self.quantidade = quantidade

    def exibir_info(self):
        print(self.titulo)
        print(self.preco)
        print(self.codigo_de_barras)
        print(self.quantidade)

produto1 = Produto("Attack on Titan", 5.99, "1234567890123", 10)

produto1.exibir_info()
