class Inimigo:
    def __init__(self, nome, forca):
        self.nome = nome
        self.__forca = forca  # Atributo privado

    def atacar(self):
        print(f"{self.nome} atacou com força {self.__forca}!")
