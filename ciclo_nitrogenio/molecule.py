import pygame
from pygame.math import Vector2
from config import WIDTH, HEIGHT, GROUND_HEIGHT, STATE_COLORS, STATES

class NitrogenMolecule:
    def __init__(self):
        self.pos = Vector2(WIDTH // 2, HEIGHT // 4)  # Posição inicial no céu
        self.radius = 20
        self.state = 0  # Estado inicial: Gasoso
        self.speed = 5

    def update(self, keys):
        # Movimento baseado nas teclas pressionadas
        if keys[pygame.K_LEFT]:
            self.pos.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.pos.x += self.speed
        if keys[pygame.K_UP]:
            self.pos.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.pos.y += self.speed

        # Colisão com o solo
        if self.state != 0:  # Se não estiver no estado gasoso
            self.pos.y = min(self.pos.y, HEIGHT - GROUND_HEIGHT - self.radius)

        # Verificar se a molécula saiu da tela
        if self.pos.y > HEIGHT + self.radius:  # Saiu pela parte inferior
            if self.state == 0:  # Se estiver no estado gasoso
                self.state = 1  # Muda para o estado de fixação
            else:
                self.state = (self.state + 1) % len(STATES)
            self.pos = Vector2(WIDTH // 2, self.radius)  # Reposiciona no topo
        elif self.pos.x < -self.radius or self.pos.x > WIDTH + self.radius or self.pos.y < -self.radius:
            # Saiu por qualquer outra direção
            self.state = (self.state + 1) % len(STATES)
            self.pos = Vector2(WIDTH // 2, self.radius)  # Reposiciona no topo

    def draw(self, screen):
        pygame.draw.circle(screen, STATE_COLORS[self.state], (int(self.pos.x), int(self.pos.y)), self.radius)

    def is_on_ground(self):
        return self.pos.y >= HEIGHT - GROUND_HEIGHT - self.radius
