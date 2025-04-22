class Termostato:
    def __init__(self, temperatura_atual, temperatura_desejada):
        self.temperatura_atual = temperatura_atual
        self.temperatura_desejada = temperatura_desejada

    def exibir_info(self):
        print(self.temperatura_atual)
        print(self.temperatura_desejada)

termostato = Termostato(32, 17)
termostato.exibir_info()

class DNA:
    def __init__(self, sequencia):
        self.sequencia = sequencia

    def exibir_info(self):
        print(self.sequencia)

dna = DNA("ATCGGCTA")
dna.exibir_info()

class Pixel:
    def __init__(self, x, y, cor):
        self.x = x
        self.y = y
        self.cor = cor

    def exibir_info(self):
        print(self.x)
        print(self.y)
        print(self.cor)

pixel = Pixel(9, 13, "Preto Claro")
pixel.exibir_info()

