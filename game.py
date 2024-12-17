import pygame, screen, player, pipe


class Game:
    def __init__(self):
        self.screen = screen.Screen()
        self.player = player.Player()
        self.screen.set_screen()
        self.player.draw(self.screen.screen)
        self.pipe = pipe.Pipe()


    def game_running(self):
        while self.screen.running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.screen.running = False

            # Draw the backgrond
            self.screen.screen.blit(self.screen.background, (0, 0))

            # Draw the player
            self.player.draw(self.screen.screen)
            self.player.move(self.screen)

            # Draw the pipe
            self.pipe.draw(self.screen.screen)
            self.pipe.move()
            

            # flip() the display to put your work on screen
            pygame.display.flip()

            self.screen.clock.tick(60)  # limits FPS to 60