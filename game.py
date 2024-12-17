import pygame, screen, player


class Game:
    def __init__(self):
        self.screen = screen.Screen()
        self.player = player.Player()
        self.screen.set_screen()
        self.player.draw(self.screen.screen)


    def game_running(self):
        while self.screen.running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.screen.running = False

            # Clear the screen
            self.screen.screen.fill(self.screen.background)

            # Draw the player
            self.player.draw(self.screen.screen)
            self.player.move()

            

            # flip() the display to put your work on screen
            pygame.display.flip()

            self.screen.clock.tick(60)  # limits FPS to 60