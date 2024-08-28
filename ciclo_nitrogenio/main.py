import pygame
import sys
from config import WIDTH, HEIGHT, WHITE, BLACK, STATES
from molecule import NitrogenMolecule
from terrain import draw_terrain

# Inicialização do Pygame
pygame.init()

# Configurações da tela
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ciclo do Nitrogênio")

# Criação da molécula
molecule = NitrogenMolecule()

# Fonte para o texto
font = pygame.font.Font(None, 36)

# Loop principal
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Obter as teclas pressionadas
    keys = pygame.key.get_pressed()

    screen.fill(WHITE)

    # Determinar se o solo deve ser mostrado
    show_ground = molecule.state != 0  # Mostra o solo se não estiver no estado gasoso

    # Desenhar o terreno
    draw_terrain(screen, show_ground)

    # Atualização e desenho da molécula
    molecule.update(keys)
    molecule.draw(screen)

    # Exibição do estado atual
    text = font.render(STATES[molecule.state], True, BLACK)
    screen.blit(text, (10, 10))

    pygame.display.flip()
    clock.tick(60)
