class Jogo:
    def __init__(self, dificuldade):
        self.__dificuldade = dificuldade

    @property
    def dificuldade(self):
        return self.__dificuldade

    @dificuldade.setter
    def dificuldade(self, valor):
        if valor in [1, 2, 3]:
            self.__dificuldade = valor
        else:
            print("A dificuldade deve ser 1 (Fácil), 2 (Média) ou 3 (Difícil).")
