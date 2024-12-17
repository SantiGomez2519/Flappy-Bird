import pygame
import screen

class Player:
    def __init__(self):
        self.x = 200
        self.y = 400
        self.width = 100
        self.height = 100
        self.gravity = 5
        self.icon = None
        self.icon_falling = None
        self.angle = 0

    def draw(self, screen):
        if not self.icon: # Load only once
            self.icon = pygame.image.load("./Icons/player.png").convert_alpha()
            self.icon_falling = pygame.image.load("./Icons/player_falling.png").convert_alpha()

            self.icon = pygame.transform.scale(self.icon, (self.width, self.height))
            self.icon_falling = pygame.transform.scale(self.icon_falling, (self.width + 35, self.height + 35))
        screen.blit(self.icon, (self.x, self.y))

    def move(self, screen):
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            if self.y > 0:
                self.y += -1 * self.gravity
                # Remove the old icon
                screen.screen.blit(screen.background, (0, 0))
                screen.screen.blit(self.icon, (self.x, self.y))
        else:
            if self.y < 500:
                self.y += self.gravity
                # Remove the old icon
                screen.screen.blit(screen.background, (0, 0))
                screen.screen.blit(self.icon_falling, (self.x, self.y))