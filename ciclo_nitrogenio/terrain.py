import pygame
from config import WIDTH, HEIGHT, GROUND_HEIGHT, GRASS_HEIGHT, SOIL_BROWN, GRASS_GREEN

def draw_terrain(screen, show_ground):
    if show_ground:
        # Desenhar o solo (marrom)
        pygame.draw.rect(screen, SOIL_BROWN, (0, HEIGHT - GROUND_HEIGHT, WIDTH, GROUND_HEIGHT))
        
        # Desenhar a camada de grama (verde)
        pygame.draw.rect(screen, GRASS_GREEN, (0, HEIGHT - GROUND_HEIGHT, WIDTH, GRASS_HEIGHT))
