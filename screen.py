import pygame

class Screen:
    def __init__(self):
        self.width = 800
        self.height = 600
        self.background = "blue"

    def set_screen(self):
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.screen.fill(self.background)
        self.clock = pygame.time.Clock()
        self.running = True
