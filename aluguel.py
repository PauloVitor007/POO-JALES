class Produto:
    def __init__(self, titulo, preco, codigo_de_barras):
        self.titulo = titulo
        self.preco = preco
        self.codigo_de_barras = codigo_de_barras

    def exibir_info(self):
        print(self.titulo)
        print(self.preco)
        print(self.codigo_de_barras)

produto1 = Produto("Attack on Titan", 5.99, "0000000000001")

produto1.exibir_info()