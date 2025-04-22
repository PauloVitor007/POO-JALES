class Livro:
    def __init__(self, titulo, autor, paginas, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas
        self.ano_publicacao = ano_publicacao

    def exibir_info(self):
        print(self.titulo)
        print(self.autor)
        print(self.paginas)
        print(self.ano_publicacao)

produto1 = Livro("Italo", "Sexofone", 666, 2060)

produto1.exibir_info()

class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    def exibir_info(self):
        print(self.titular)
        print(self.saldo)

class Tarefa:
    def __init__(self, descricao, data_limite, concluida):
        self.descricao = descricao
        self.data_limite = data_limite
        self.concluida = concluida

    def exibir_info(self):
        print(self.descricao)
        print(self.data_limite)
        print(self.concluida)


conta = ContaBancaria("Felizberto", 1500)
conta.exibir_info()

tarefa = Tarefa("Estudar Python", "2025-04-01", False)
tarefa.exibir_info()

class Termostato:
    def __init__(self, temperatura_atual, temperatura_desejada):
        self.temperatura_atual = temperatura_atual
        self.temperatura_desejada = temperatura_desejada

    def exibir_info(self):
        print(self.temperatura_atual)
        print(self.temperatura_desejada)


termostato = Termostato(22, 24)
termostato.exibir_info()