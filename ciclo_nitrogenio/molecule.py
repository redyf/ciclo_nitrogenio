import pygame
from pygame.math import Vector2
from config import WIDTH, HEIGHT, GROUND_HEIGHT, STATE_COLORS, STATES, BLACK

class NitrogenMolecule:
    def __init__(self):
        self.pos = Vector2(WIDTH // 2, HEIGHT // 4) # Posição inicial no céu
        self.radius = 20
        self.state = 0
        self.speed = 5
        self.in_soil = False
        self.font = pygame.font.Font(None, 24)

    def update(self, keys):
        if keys[pygame.K_LEFT]:
            self.pos.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.pos.x += self.speed
        if keys[pygame.K_UP]:
            self.pos.y -= self.speed
        if keys[pygame.K_DOWN]:
            self.pos.y += self.speed

        if self.state == 0:
            self.in_soil = False
        elif self.state in [1, 2, 3]:
            if self.state == 1 and not self.in_soil:
                self.pos.y = min(self.pos.y, HEIGHT - GROUND_HEIGHT - self.radius)
            elif self.state in [2, 3]:
                self.in_soil = True
                self.pos.y = min(max(self.pos.y, HEIGHT - GROUND_HEIGHT), HEIGHT - self.radius)
        elif self.state == 4:
            self.in_soil = False
            self.pos.y = min(self.pos.y, HEIGHT - GROUND_HEIGHT - self.radius)

        self.pos.x = max(self.radius, min(self.pos.x, WIDTH - self.radius))
        self.pos.y = max(self.radius, min(self.pos.y, HEIGHT - self.radius))

    def next_state(self):
        self.state = (self.state + 1) % len(STATES)
        if self.state == 0:
            self.in_soil = False
            self.pos.y = HEIGHT // 4

    def draw(self, screen):
        pygame.draw.circle(screen, STATE_COLORS[self.state], (int(self.pos.x), int(self.pos.y)), self.radius)
        text = self.font.render(STATES[self.state].split()[0], True, BLACK)
        text_rect = text.get_rect(center=(self.pos.x, self.pos.y))
        screen.blit(text, text_rect)

    def is_on_ground(self):
        return self.pos.y >= HEIGHT - GROUND_HEIGHT - self.radius or self.in_soil

