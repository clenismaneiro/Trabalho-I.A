import pygame
import random

# Configurações do jogo
largura_tela = 400
altura_tela = 600
gravidade = 0.25
forca_pulo = -5
velocidade_obstaculo = 2

# Cores
branco = (255, 255, 255)
preto = (0, 0, 0)

# Inicialização do Pygame
pygame.init()
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Flappy")

# Classe do jogador
class Jogador:
    def __init__(self):
        self.x = 100
        self.y = altura_tela // 2
        self.velocidade = 0
        self.altura_jogador = 30
        self.largura_jogador = 30

    def pular(self):
        self.velocidade = forca_pulo

    def atualizar(self):
        self.velocidade += gravidade
        self.y += self.velocidade

    def desenhar(self):
        pygame.draw.rect(tela, branco, (self.x, self.y, self.largura_jogador, self.altura_jogador))

# Classe do obstáculo
class Obstaculo:
    def __init__(self, x):
        self.x = x
        self.altura = random.randint(100, 400)
        self.largura = 50

    def atualizar(self):
        self.x -= velocidade_obstaculo

    def desenhar(self):
        pygame.draw.rect(tela, branco, (self.x, 0, self.largura, self.altura))
        pygame.draw.rect(tela, branco, (self.x, self.altura + 150, self.largura, altura_tela - self.altura - 150))

# Função principal do jogo
def jogo_flappy_bird():
    jogador = Jogador()
    obstaculos = [Obstaculo(largura_tela + i * 250) for i in range(3)]
    score = 0

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return

        if jogador.y < obstaculos[0].altura or jogador.y + jogador.altura_jogador > obstaculos[0].altura + 150:
            jogador.pular()

        jogador.atualizar()

        for obstaculo in obstaculos:
            obstaculo.atualizar()

        if obstaculos[0].x + obstaculos[0].largura < 0:
            obstaculos.pop(0)
            obstaculos.append(Obstaculo(obstaculos[-1].x + 250))
            score += 1

        if jogador.y > altura_tela or jogador.y < 0:
            pygame.quit()
            return

        tela.fill(preto)

        for obstaculo in obstaculos:
            obstaculo.desenhar()

        jogador.desenhar()

        pygame.display.flip()
        clock.tick(60)

jogo_flappy_bird()
