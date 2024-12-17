import random
import pygame

class Pipe:
    def __init__(self):
        self.x = 800
        self.y = 0
        self.width = 80
        self.height = random.randint(75, 350)

    def draw(self, screen):
        pipe = pygame.image.load("./Icons/pipe.png").convert_alpha()
        pipe = pygame.transform.scale(pipe, (self.width, self.height))
        pipe = pygame.transform.rotate(pipe, 180)

        pipe2  = pipe.copy()
        pipe2 = pygame.transform.scale(pipe2, (self.width, 600 - self.height))
        pipe2 = pygame.transform.rotate(pipe2, 180)

        screen.blit(pipe, (self.x, self.y))
        screen.blit(pipe2, (self.x, self.height + 200))


    def move(self):
        self.x += -5
        if self.x < -100:
            self.x = 800
            self.height = random.randint(100, 400)
