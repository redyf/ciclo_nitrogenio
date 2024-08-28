import pygame

# Configurações da tela
WIDTH, HEIGHT = 800, 600

# Cores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)
LIGHT_BROWN = (210, 180, 140)  # Cor marrom claro para fixação
SOIL_BROWN = (139, 69, 19)  # Cor marrom para o solo
GRASS_GREEN = (34, 139, 34)  # Cor verde para a grama
DARK_YELLOW = (238,173,45)
LIGHT_BLUE = (135, 206, 250)  # Cor azul claro para o estado gasoso

# Estados do ciclo
STATES = ["Gasoso", "Fixação", "Amonização", "Nitrificação", "Desnitrificação"]
STATE_COLORS = [LIGHT_BLUE, LIGHT_BROWN, DARK_YELLOW, GREEN, YELLOW]

# Configurações do terreno
GROUND_HEIGHT = 100
GRASS_HEIGHT = 10
