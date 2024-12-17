import pygame
import screen

class Player:
    def __init__(self):
        self.x = 200
        self.y = 400
        self.width = 50
        self.height = 50
        self.gravity = 5

    def draw(self, screen):
        pygame.image.load("./Icons/player.jpeg")
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.width, self.height))

    def move(self):
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            self.y += -1 * self.gravity
        else:
            self.y += self.gravity