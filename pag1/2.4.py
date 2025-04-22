import random

class Personagem:
    def __init__(self, nome, vida=100):
        self.nome = nome
        self.__vida = vida
        self.__defesa = 0
    
    def atacar(self, alvo):
        dano = random.randint(5, 20)
        alvo.receber_dano(dano)
        print(f"{self.nome} atacou {alvo.nome} causando {dano} de dano!")
    
    def receber_dano(self, dano):
        dano_final = max(0, dano - self.__defesa)
        self.__vida -= dano_final
    
    @property
    def vida(self):
        return self.__vida
    
    @property
    def defesa(self):
        return self.__defesa
    
    @defesa.setter
    def defesa(self, valor):
        self.__defesa = max(0, min(100, valor))

class NPC(Personagem):
    def __init__(self, nome, vida=100):
        super().__init__(nome, vida)
    
    def atacar(self, alvo):
        print(f"{self.nome} é um NPC e não pode atacar!")

class Inimigo:
    def __init__(self, nome, vida=100, forca=None):
        self.nome = nome
        self.__vida = vida
        self.__forca = forca if forca is not None else random.randint(5, 20)
    
    def atacar(self, alvo):
        print(f"{self.nome} atacou com força de {self.__forca}!")
        alvo.receber_dano(self.__forca)
    
    def receber_dano(self, dano):
        self.__vida -= dano
    
    @property
    def vida(self):
        return self.__vida

class Chefe(Inimigo):
    def __init__(self, nome, vida=200, forca=40):
        super().__init__(nome, vida, forca)

class Jogador(Personagem):
    def __init__(self, nome, energia=100, pontos=0):
        super().__init__(nome)
        self.__energia = energia
        self.__pontos = pontos
    
    def atacar(self, inimigo):
        if self.__energia <= 0:
            print("Sem energia! Precisa descansar.")
            return
        super().atacar(inimigo)
        self.usar_energia(10)
        if inimigo.vida <= 0:
            print(f"{inimigo.nome} foi derrotado!")
            self.pontos += 10
    
    def descansar(self):
        self.recuperar_energia(20)
        print(f"{self.nome} descansou e recuperou energia. Energia atual: {self.__energia}")
    
    def usar_energia(self, valor):
        self.__energia = max(0, self.__energia - valor)
    
    def recuperar_energia(self, valor):
        self.__energia = min(100, self.__energia + valor)
    
    @property
    def pontos(self):
        return self.__pontos
    
    @pontos.setter
    def pontos(self, valor):
        if valor >= 0:
            self.__pontos = valor

class JogadorPremium(Jogador):
    def __init__(self, nome, energia=100, pontos=0):
        super().__init__(nome, energia, pontos)
    
    def vencer_desafio(self):
        self.pontos += 20

class Jogo:
    def __init__(self):
        self.__dificuldade = 1
    
    @property
    def dificuldade(self):
        return self.__dificuldade
    
    @dificuldade.setter
    def dificuldade(self, valor):
        if 1 <= valor <= 3:
            self.__dificuldade = valor

class JogoMultiplayer(Jogo):
    def __init__(self):
        super().__init__()
        self.jogadores = []
    
    def adicionar_jogador(self, jogador):
        self.jogadores.append(jogador)

class Menu:
    def __init__(self, titulo):
        self.titulo = titulo
    
    def mostrar(self):
        print(self.titulo)
        print("1. Iniciar Jogo")
        print("2. Mostrar Opções")
        print("3. Sair")
        escolha = input("Escolha uma opção: ")
        return escolha

class MenuAvancado(Menu):
    def __init__(self, titulo):
        super().__init__(titulo)
        self.configuracoes = {}
    
    def salvar_configuracao(self, chave, valor):
        self.configuracoes[chave] = valor

class Fase:
    def iniciar(self):
        pass

class FaseFloresta(Fase):
    def iniciar(self):
        print("Iniciando fase na Floresta!")

class FaseDeserto(Fase):
    def iniciar(self):
        print("Iniciando fase no Deserto!")

class Aliado(Personagem):
    def habilidade_especial(self):
        pass

class Mago(Aliado):
    def habilidade_especial(self):
        print("Mago lançou uma bola de fogo!")

class Guerreiro(Aliado):
    def habilidade_especial(self):
        print("Guerreiro usou golpe poderoso!")

if __name__ == "__main__":
    menu = Menu("=== MENU PRINCIPAL ===")
    while True:
        opcao = menu.mostrar()
        if opcao == "1":
            print("Jogo iniciado!")
        elif opcao == "2":
            print("Opções: Derrote os inimigos e gerencie sua energia!")
        elif opcao == "3":
            print("Saindo do jogo...")
            break
        else:
            print("Opção inválida!")
