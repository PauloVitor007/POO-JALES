class Jogo:
    def iniciar(self):
        print("O jogo começou!")

jogo = Jogo()
jogo.iniciar()

class Personagem:
    def pular(self):
        print("O personagem pulou!")

personagem = Personagem()
personagem.pular()

class Inimigo:
    def atacar(self):
        print("O inimigo atacou!")

inimigo = Inimigo()
inimigo.atacar()

class Pontuacao:
    def zerar_pontos(self):
        print("Pontuação zerada!")

pontuacao = Pontuacao()
pontuacao.zerar_pontos()

class Menu:
    def iniciar_jogo(self):
        print("Iniciando jogo...")
    
    def mostrar_opcoes(self):
        print("Exibindo opções do menu...")
    
    def sair(self):
        print("Saindo do jogo...")

menu = Menu()
menu.iniciar_jogo()
menu.mostrar_opcoes()
menu.sair()

class Personagem:
    def __init__(self, nome):
        self.nome = nome
    
    def dizer_nome(self):
        print(f"Meu nome é {self.nome}")

personagem = Personagem("Arthur")
personagem.dizer_nome()

class Pontuacao:
    def __init__(self):
        self.pontos = 0
    
    def adicionar_pontos(self, quantidade):
        self.pontos += quantidade
    
    def mostrar_pontos(self):
        print(f"Pontuação atual: {self.pontos}")

pontuacao = Pontuacao()
pontuacao.adicionar_pontos(10)
pontuacao.mostrar_pontos()

class Personagem:
    def __init__(self):
        self.vida = 100
    
    def tomar_dano(self, dano):
        self.vida -= dano
        if self.vida <= 0:
            print("Game Over!")
        else:
            print(f"Vida restante: {self.vida}")

personagem = Personagem()
personagem.tomar_dano(30)
personagem.tomar_dano(80)

class Jogador:
    def __init__(self):
        self.energia = 50
    
    def recuperar_energia(self, quantidade):
        self.energia += quantidade
        print(f"Energia recuperada. Nível atual: {self.energia}")
    
    def usar_energia(self, quantidade):
        if self.energia < quantidade:
            print("Sem energia suficiente!")
        else:
            self.energia -= quantidade
            print(f"Energia usada. Nível atual: {self.energia}")

jogador = Jogador()
jogador.usar_energia(30)
jogador.usar_energia(30)
jogador.recuperar_energia(20)

class Inimigo:
    def __init__(self, nome):
        self.nome = nome
        self.vida = 100
    
    def atacar(self, alvo):
        if isinstance(alvo, Personagem):
            alvo.tomar_dano(10)
            print(f"{self.nome} atacou o personagem!")
        else:
            print("O alvo não é um personagem válido!")

personagem = Personagem()
inimigo = Inimigo("Goblin")
inimigo.atacar(personagem)