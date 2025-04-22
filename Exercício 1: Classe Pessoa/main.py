class Pessoa:
    def __init__(self):
        self.__nome = ""
        self.__idade = 0

    def set_nome(self, nome):
        self.__nome = nome

    def get_nome(self):
        return self.__nome

    def set_idade(self, idade):
        if idade < 0:
            print("Idade não pode ser negativa.")
        else:
            self.__idade = idade

    def get_idade(self):
        return self.__idade


pessoa = Pessoa()

pessoa.set_nome("Paulo")
pessoa.set_idade(19)

print("Nome:", pessoa.get_nome())
print("Idade:", pessoa.get_idade(), "anos")


pessoa.set_idade(-5)
