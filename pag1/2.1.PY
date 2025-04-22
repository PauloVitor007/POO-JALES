import random

class Personagem:
    def __init__(self, nome):
        self.nome = nome
        self.__vida = 100
    
    def atacar(self, alvo):
        dano = random.randint(5, 20)
        alvo.receber_dano(dano)
        print(f"{self.nome} atacou {alvo.nome} causando {dano} de dano!")
    
    def receber_dano(self, dano):
        self.__vida -= dano
    
    def mostrar_vida(self):
        return self.__vida

class Inimigo:
    def __init__(self, nome):
        self.nome = nome
        self.__vida = 100
        self.__forca = random.randint(5, 20)
    
    def atacar(self, alvo):
        print(f"{self.nome} atacou com força de {self.__forca}!")
        alvo.receber_dano(self.__forca)
    
    def receber_dano(self, dano):
        self.__vida -= dano
    
    def mostrar_vida(self):
        return self.__vida

class Jogador(Personagem):
    def __init__(self, nome):
        super().__init__(nome)
        self.__energia = 100
        self.__pontos = 0
    
    def atacar(self, inimigo):
        if self.__energia <= 0:
            print("Sem energia! Precisa descansar.")
            return
        super().atacar(inimigo)
        self.usar_energia(10)
        if inimigo.mostrar_vida() <= 0:
            print(f"{inimigo.nome} foi derrotado!")
            self.adicionar_pontos(10)
    
    def descansar(self):
        self.recuperar_energia(20)
        print(f"{self.nome} descansou e recuperou energia. Energia atual: {self.__energia}")
    
    def usar_energia(self, valor):
        self.__energia = max(0, self.__energia - valor)
    
    def recuperar_energia(self, valor):
        self.__energia = min(100, self.__energia + valor)
    
    def adicionar_pontos(self, valor):
        self.__pontos += valor

class Menu:
    @staticmethod
    def mostrar():
        print("1. Iniciar Jogo")
        print("2. Mostrar Opções")
        print("3. Sair")
        escolha = input("Escolha uma opção: ")
        return escolha

    @staticmethod
    def iniciar_jogo():
        nome_jogador = input("Digite o nome do jogador: ")
        jogador = Jogador(nome_jogador)
        while jogador.mostrar_vida() > 0:
            inimigos = [Inimigo(f"Inimigo {i+1}") for i in range(random.randint(1, 3))]
            print(f"{len(inimigos)} inimigo(s) apareceu(am)!")
            for inimigo in inimigos:
                while inimigo.mostrar_vida() > 0 and jogador.mostrar_vida() > 0:
                    jogador.atacar(inimigo)
                    if inimigo.mostrar_vida() > 0:
                        inimigo.atacar(jogador)
                    print(f"Vida de {jogador.nome}: {jogador.mostrar_vida()}, Energia: {jogador._Jogador__energia}")
                    if jogador.mostrar_vida() <= 0:
                        print("Você foi derrotado!")
                        return
                jogador.descansar()
            print(f"Pontuação atual: {jogador._Jogador__pontos}")
        print("Jogo encerrado!")

if __name__ == "__main__":
    while True:
        opcao = Menu.mostrar()
        if opcao == "1":
            Menu.iniciar_jogo()
        elif opcao == "2":
            print("Opções: Derrote os inimigos e gerencie sua energia!")
        elif opcao == "3":
            print("Saindo do jogo...")
            break
        else:
            print("Opção inválida!")