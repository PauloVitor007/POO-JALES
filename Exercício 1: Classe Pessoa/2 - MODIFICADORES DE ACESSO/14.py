class Personagem:
    def __init__(self, nome, vida):
        self.nome = nome
        self.__vida = vida  # Atributo privado

    def mostrar_vida(self):
        return self.__vida
