import pygame

class Screen:
    def __init__(self):
        self.width = 800
        self.height = 600
        self.background = None
        self.running = True

    def set_screen(self):
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Flappy Bird")

        if not self.background:
            self.background = pygame.image.load("./Icons/background.png").convert_alpha()
            self.background = pygame.transform.scale(self.background, (self.width, self.height))
        
        self.clock = pygame.time.Clock()
