class Pontuacao:
    def __init__(self):
        self.__pontos = 0

    @property
    def pontos(self):
        return self.__pontos

    @pontos.setter
    def pontos(self, valor):
        if valor >= 0:
            self.__pontos = valor
        else:
            print("Pontuação não pode ser negativa.")
