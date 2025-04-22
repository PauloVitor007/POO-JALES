# Criando objeto da classe Aluno
aluno = Aluno()

aluno.set_matricula("2025A001")
aluno.set_nome("Paulo Vitor")
aluno.set_media(85)

# Exibindo os valores
print("Matrícula:", aluno.get_matricula())
print("Nome:", aluno.get_nome())
print("Média Final:", aluno.get_media())

# Testando valor inválido para média
aluno.set_media(-10)  # Vai mostrar a mensagem de erro
