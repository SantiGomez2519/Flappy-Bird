import pygame, screen, player, pipe


class Game:
    def __init__(self):
        self.screen = screen.Screen()
        self.player = player.Player()
        self.screen.set_screen()
        self.player.draw(self.screen.screen)
        self.pipe = pipe.Pipe()
        self.lose = False


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

            # Lose if the player hits the pipe
            if self.player.x + self.player.width > self.pipe.x and self.player.x < self.pipe.x + self.pipe.width:
                if self.player.y < self.pipe.height or self.player.y + self.player.height > self.pipe.height + 200:
                    self.lose = True

            if self.lose:
                # Freeze the screen by skipping updates
                self.draw_lose_message()
                pygame.display.flip()
                self.screen.clock.tick(0)  # Limit FPS in lose state
                if pygame.key.get_pressed()[pygame.K_SPACE]:
                    self.lose = False
                    self.player.y = 400
                    self.pipe.x = 800
                    self.game_running()
            

            # flip() the display to put your work on screen
            pygame.display.flip()

            self.screen.clock.tick(60)  # limits FPS to 60

    def draw_lose_message(self):
        # Draw a 'Paused' message on the screen.
        font = pygame.font.Font(None, 74)
        text = font.render("You failed", True, (255, 255, 255))
        text_rect = text.get_rect(center=(self.screen.width // 2, self.screen.height // 2))
        self.screen.screen.blit(self.screen.background, (0, 0))  # Keep the background visible
        self.screen.screen.blit(text, text_rect)