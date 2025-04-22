class Personagem:
    def __init__(self, nome, vida, defesa):
        self.nome = nome
        self.__vida = vida 
        self.__defesa = defesa

    @property
    def vida(self):
        return self.__vida

    @property
    def defesa(self):
        return self.__defesa

    @defesa.setter
    def defesa(self, valor): 
        if 0 <= valor <= 100:
            self.__defesa = valor
        else:
            print("Valor de defesa deve estar entre 0 e 100.")
