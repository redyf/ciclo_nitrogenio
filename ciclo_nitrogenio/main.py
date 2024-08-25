import pygame
import sys
import math

class NitrogenCycle:
    def __init__(self):
        pygame.init()
        self.width, self.height = 800, 600
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Ciclo do Nitrogênio Interativo")
        
        self.WHITE = (255, 255, 255)
        self.BLACK = (0, 0, 0)
        self.BLUE = (0, 0, 255)
        self.GREEN = (0, 255, 0)
        self.RED = (255, 0, 0)
        self.YELLOW = (255, 255, 0)
        
        self.font = pygame.font.Font(None, 24)
        self.clock = pygame.time.Clock()
        
        self.stages = [
            {"name": "Fixação", "color": self.BLUE, "pos": (200, 300), "info": "Conversão de N2 atmosférico em formas utilizáveis"},
            {"name": "Nitrificação", "color": self.GREEN, "pos": (400, 150), "info": "Conversão de amônia em nitrato"},
            {"name": "Assimilação", "color": self.RED, "pos": (600, 300), "info": "Absorção de nitrogênio por organismos"},
            {"name": "Desnitrificação", "color": self.YELLOW, "pos": (400, 450), "info": "Conversão de nitrato em N2 gasoso"}
        ]
        
        self.selected_stage = None

    def draw_arrow(self, start, end):
        pygame.draw.line(self.screen, self.BLACK, start, end, 2)
        rotation = math.atan2(start[1] - end[1], end[0] - start[0])
        pygame.draw.polygon(self.screen, self.BLACK, [
            (end[0] + 20 * math.cos(rotation), end[1] - 20 * math.sin(rotation)),
            (end[0] + 20 * math.cos(rotation + math.pi/6), end[1] - 20 * math.sin(rotation + math.pi/6)),
            (end[0] + 20 * math.cos(rotation - math.pi/6), end[1] - 20 * math.sin(rotation - math.pi/6))
        ])

    def draw_cycle(self):
        self.screen.fill(self.WHITE)
        
        for stage in self.stages:
            pygame.draw.circle(self.screen, stage["color"], stage["pos"], 50)
            text = self.font.render(stage["name"], True, self.BLACK)
            text_rect = text.get_rect(center=(stage["pos"][0], stage["pos"][1] + 70))
            self.screen.blit(text, text_rect)
        
        self.draw_arrow((250, 300), (350, 200))
        self.draw_arrow((450, 150), (550, 250))
        self.draw_arrow((600, 350), (450, 425))
        self.draw_arrow((350, 450), (250, 350))
        
        if self.selected_stage:
            info_text = self.font.render(self.selected_stage["info"], True, self.BLACK)
            pygame.draw.rect(self.screen, self.WHITE, (50, 50, 700, 30))
            self.screen.blit(info_text, (50, 50))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for stage in self.stages:
                    distance = math.hypot(mouse_pos[0] - stage["pos"][0], mouse_pos[1] - stage["pos"][1])
                    if distance <= 50:
                        self.selected_stage = stage
                        break
                else:
                    self.selected_stage = None
        return True

    def run(self):
        running = True
        while running:
            running = self.handle_events()
            self.draw_cycle()
            pygame.display.flip()
            self.clock.tick(60)
        
        pygame.quit()
        sys.exit()

if __name__ == "__main__":
    NitrogenCycle().run()
