class Pontuacao:
    def __init__(self):
        self.__pontos = 0  # Atributo privado

    def adicionar_pontos(self, valor):
        if valor > 0:
            self.__pontos += valor
        else:
            print("Valor inválido. Apenas valores positivos são permitidos.")

    def mostrar_pontos(self):
        return self.__pontos
