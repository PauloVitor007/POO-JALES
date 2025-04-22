class Aluno:
    def __init__(self):
        self.__matricula = ""
        self.__nome = ""
        self.__media = 0

    def set_matricula(self, matricula):
        self.__matricula = matricula

    def get_matricula(self):
        return self.__matricula

    def set_nome(self, nome):
        self.__nome = nome

    def get_nome(self):
        return self.__nome

    def set_media(self, media):
        if 0 <= media <= 100:
            self.__media = media
        else:
            print("A média deve estar entre 0 e 100.")

    def get_media(self):
        return self.__media


aluno = Aluno()
aluno.set_matricula("2025A001")
aluno.set_nome("Paulo Vitor")
aluno.set_media(85)

print("Matrícula:", aluno.get_matricula())
print("Nome:", aluno.get_nome())
print("Média Final:", aluno.get_media())
