import pygame
import random

# Inicialização
pygame.init()

# Configurações da tela
LARGURA = 800
ALTURA = 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Jogo de Blocos")

# Cores
BRANCO = (255, 255, 255)
AZUL = (0, 0, 255)
VERMELHO = (255, 0, 0)
PRETO = (0, 0, 0)
VERDE = (0, 255, 0)

# Barra do jogador
barra = pygame.Rect(350, 550, 100, 15)
velocidade_barra = 8

# Bola
bola = pygame.Rect(390, 300, 20, 20)
vel_x = 4
vel_y = -4

# Blocos
blocos = []
for linha in range(5):
    for coluna in range(10):
        bloco = pygame.Rect(coluna * 75 + 25, linha * 35 + 40, 70, 25)
        blocos.append(bloco)

# Fonte
fonte = pygame.font.SysFont(None, 36)
pontos = 0

# Relógio
clock = pygame.time.Clock()

rodando = True

while rodando:
    clock.tick(60)

    # Eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Movimento da barra
    teclas = pygame.key.get_pressed()

    if teclas[pygame.K_LEFT] and barra.left > 0:
        barra.x -= velocidade_barra

    if teclas[pygame.K_RIGHT] and barra.right < LARGURA:
        barra.x += velocidade_barra

    # Movimento da bola
    bola.x += vel_x
    bola.y += vel_y

    # Colisão com paredes
    if bola.left <= 0 or bola.right >= LARGURA:
        vel_x *= -1

    if bola.top <= 0:
        vel_y *= -1

    # Colisão com a barra
    if bola.colliderect(barra):
        vel_y *= -1

    # Colisão com blocos
    for bloco in blocos[:]:
        if bola.colliderect(bloco):
            blocos.remove(bloco)
            vel_y *= -1
            pontos += 10
            break

    # Game Over
    if bola.bottom >= ALTURA:
        texto = fonte.render("GAME OVER", True, VERMELHO)
        tela.blit(texto, (320, 280))
        pygame.display.update()
        pygame.time.delay(3000)
        rodando = False

    # Vitória
    if len(blocos) == 0:
        texto = fonte.render("VOCÊ VENCEU!", True, VERDE)
        tela.blit(texto, (300, 280))
        pygame.display.update()
        pygame.time.delay(3000)
        rodando = False

    # Desenho
    tela.fill(PRETO)

    pygame.draw.rect(tela, AZUL, barra)
    pygame.draw.ellipse(tela, BRANCO, bola)

    for bloco in blocos:
        pygame.draw.rect(tela, VERMELHO, bloco)

    texto_pontos = fonte.render(f"Pontos: {pontos}", True, BRANCO)
    tela.blit(texto_pontos, (10, 10))

    pygame.display.update()

pygame.quit()


"""Conceitos trabalhados
Variáveis
Estruturas de repetição (for e while)
Estruturas condicionais (if)
Listas
Funções da biblioteca Pygame
Detecção de colisão
Lógica de jogos
Programação orientada a eventos
Desafio para os alunos
Adicionar níveis de dificuldade.
Criar blocos com cores diferentes e pontuações variadas.
Adicionar sons.
Criar tela inicial.
Implementar sistema de vidas.
Salvar recordes em arquivo."""
