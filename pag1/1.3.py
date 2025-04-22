import random

class Personagem:
    def __init__(self, nome):
        self.nome = nome
        self.vida = 100
    
    def atacar(self, alvo):
        dano = random.randint(5, 20)
        alvo.vida -= dano
        print(f"{self.nome} atacou {alvo.nome} causando {dano} de dano!")

class Inimigo:
    def __init__(self, nome):
        self.nome = nome
        self.vida = 100

class Jogador(Personagem):
    def __init__(self, nome):
        super().__init__(nome)
        self.energia = 100
        self.pontos = 0
    
    def atacar(self, inimigo):
        if self.energia <= 0:
            print("Sem energia! Precisa descansar.")
            return
        super().atacar(inimigo)
        self.energia -= 10
        if inimigo.vida <= 0:
            print(f"{inimigo.nome} foi derrotado!")
            self.pontos += 10
    
    def descansar(self):
        self.energia = min(100, self.energia + 20)
        print(f"{self.nome} descansou e recuperou energia. Energia atual: {self.energia}")

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
        while jogador.vida > 0 and jogador.energia > 0:
            inimigos = [Inimigo(f"Inimigo {i+1}") for i in range(random.randint(1, 3))]
            print(f"{len(inimigos)} inimigo(s) apareceu(am)!")
            for inimigo in inimigos:
                while inimigo.vida > 0 and jogador.vida > 0:
                    jogador.atacar(inimigo)
                    if inimigo.vida > 0:
                        inimigo.atacar(jogador)
                    print(f"Vida de {jogador.nome}: {jogador.vida}, Energia: {jogador.energia}")
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
