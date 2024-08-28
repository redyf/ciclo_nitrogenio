import pygame
import sys
from config import WIDTH, HEIGHT, WHITE, BLACK, STATES
from molecule import NitrogenMolecule
from terrain import draw_terrain

# Inicialização do Pygame
pygame.init()

#Configurações da tela
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ciclo do Nitrogênio")

#Criação da molécula
molecule = NitrogenMolecule()

# Tamanho da fonte
font = pygame.font.Font(None, 24)
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                molecule.next_state()

    keys = pygame.key.get_pressed()
    screen.fill(WHITE)
    show_ground = molecule.state != 0
    draw_terrain(screen, show_ground)
    molecule.update(keys)
    molecule.draw(screen)

    # Exibição do estado atual
    text = font.render(STATES[molecule.state], True, BLACK)
    screen.blit(text, (10, 10))

    # Exibição das instruções
    instructions = font.render("Use as setas para mover. Pressione ESPAÇO para mudar de estado.", True, BLACK)
    screen.blit(instructions, (120, HEIGHT - 40))

    pygame.display.flip()
    clock.tick(60)
