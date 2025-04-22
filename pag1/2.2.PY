import random

class Personagem:
    def __init__(self, nome):
        self.nome = nome
        self.__vida = 100
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
    
    @property
    def vida(self):
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
        while jogador.vida > 0:
            inimigos = [Inimigo(f"Inimigo {i+1}") for i in range(random.randint(1, 3))]
            print(f"{len(inimigos)} inimigo(s) apareceu(am)!")
            for inimigo in inimigos:
                while inimigo.vida > 0 and jogador.vida > 0:
                    jogador.atacar(inimigo)
                    if inimigo.vida > 0:
                        inimigo.atacar(jogador)
                    print(f"Vida de {jogador.nome}: {jogador.vida}, Energia: {jogador._Jogador__energia}")
                    if jogador.vida <= 0:
                        print("Você foi derrotado!")
                        return
                jogador.descansar()
            print(f"Pontuação atual: {jogador.pontos}")
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