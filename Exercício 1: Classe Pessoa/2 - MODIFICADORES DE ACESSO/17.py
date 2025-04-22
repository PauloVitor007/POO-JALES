class Jogador:
    def __init__(self, nome, energia=100):
        self.nome = nome
        self.__energia = energia  # Atributo privado

    def usar_energia(self, valor):
        if valor > 0:
            self.__energia -= valor
            if self.__energia < 0:
                self.__energia = 0

    def recuperar_energia(self, valor):
        if valor > 0:
            self.__energia += valor
            if self.__energia > 100:
                self.__energia = 100

    def mostrar_energia(self):
        return self.__energia
2.2 Getters e Setters